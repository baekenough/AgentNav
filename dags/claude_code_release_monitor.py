"""
Claude Code Release Monitor DAG.

Monitors GitHub releases for anthropics/claude-code and creates tracking
issues on baekenough/oh-my-customcode when new releases are detected.
Each issue includes a summary of changes, breaking change detection,
and a link to the original release.

Graph:
    fetch_releases ─► filter_new_releases ─► create_issues
"""

from __future__ import annotations

import json
import logging
import os
import re
from datetime import datetime, timedelta, timezone

import requests
from airflow.sdk import dag, task
from airflow.exceptions import AirflowFailException
from airflow.sdk import Variable

log = logging.getLogger(__name__)

# ---------------------------------------------------------------------------
# Constants
# ---------------------------------------------------------------------------
CLAUDE_CODE_RELEASES_URL = (
    "https://api.github.com/repos/anthropics/claude-code/releases"
)
GITHUB_API_ISSUES_URL = "https://api.github.com/repos/{repo}/issues"

DEFAULT_REQUEST_TIMEOUT = 30  # seconds
MAX_RELEASES_TO_FETCH = 5
MAX_SUMMARY_LENGTH = 500

BREAKING_CHANGE_PATTERNS = re.compile(
    r"(?i)breaking[\s_-]*change|BREAKING|⚠️\s*breaking",
)

ISSUE_LABEL = "claude-code-release"
ISSUE_LABELS = ["automated", ISSUE_LABEL]

# ---------------------------------------------------------------------------
# DAG definition
# ---------------------------------------------------------------------------
default_args = {
    "owner": "agentnav",
    "retries": 1,
    "retry_delay": timedelta(minutes=5),
}


@dag(
    dag_id="claude_code_release_monitor",
    description=(
        "Monitors anthropics/claude-code GitHub releases and creates "
        "tracking issues on baekenough/oh-my-customcode for new releases."
    ),
    schedule="@daily",
    start_date=datetime(2026, 3, 14),
    catchup=False,
    tags=["claude-code", "release-monitoring", "automated"],
    default_args=default_args,
    doc_md=__doc__,
)
def claude_code_release_monitor() -> None:
    """Orchestrate release monitoring for Claude Code."""

    # ------------------------------------------------------------------
    # Task 1: Fetch recent releases
    # ------------------------------------------------------------------

    @task()
    def fetch_releases() -> list[dict]:
        """Fetch the most recent releases from anthropics/claude-code.

        Retrieves up to ``MAX_RELEASES_TO_FETCH`` releases from the GitHub
        Releases API. Each release dict contains: ``tag_name``, ``name``,
        ``published_at``, ``html_url``, ``body``, and ``prerelease``.

        Returns:
            List of release dicts with selected fields.
        """
        github_token = _resolve_github_token()
        headers = _github_headers(github_token)

        response = _get(
            CLAUDE_CODE_RELEASES_URL,
            headers=headers,
            params={"per_page": MAX_RELEASES_TO_FETCH},
        )

        try:
            releases = response.json()
        except json.JSONDecodeError as exc:
            raise AirflowFailException(
                f"Failed to parse JSON from {CLAUDE_CODE_RELEASES_URL}: {exc}"
            ) from exc

        if not isinstance(releases, list):
            msg = releases.get("message", str(releases)[:200]) if isinstance(releases, dict) else str(releases)[:200]
            raise AirflowFailException(
                f"Unexpected response from GitHub Releases API: {msg}"
            )

        if not releases:
            log.info("No releases found for anthropics/claude-code.")
            return []

        # Extract only the fields we need to keep XCom payload small.
        result = []
        for r in releases:
            result.append(
                {
                    "tag_name": r.get("tag_name", ""),
                    "name": r.get("name", ""),
                    "published_at": r.get("published_at", ""),
                    "html_url": r.get("html_url", ""),
                    "body": r.get("body", ""),
                    "prerelease": r.get("prerelease", False),
                }
            )

        log.info(
            "Fetched %d releases from anthropics/claude-code. "
            "Latest: %s (%s)",
            len(result),
            result[0]["tag_name"],
            result[0]["published_at"],
        )
        return result

    # ------------------------------------------------------------------
    # Task 2: Filter out releases that already have issues
    # ------------------------------------------------------------------

    @task()
    def filter_new_releases(releases: list[dict]) -> list[dict]:
        """Filter releases that do not yet have a tracking issue.

        Checks open issues on the target repository with the
        ``claude-code-release`` label. A release is considered "already
        tracked" if any open issue title contains its ``tag_name``.

        Args:
            releases: List of release dicts from ``fetch_releases``.

        Returns:
            List of release dicts that need new issues.
        """
        if not releases:
            log.info("No releases to filter.")
            return []

        github_token = _resolve_github_token()
        headers = _github_headers(github_token)
        target_repo = Variable.get(
            "omc_github_repo", default_var="baekenough/oh-my-customcode"
        )

        # Fetch open issues with the release label.
        list_url = GITHUB_API_ISSUES_URL.format(repo=target_repo)
        existing_tags: set[str] = set()

        try:
            list_resp = requests.get(
                list_url,
                params={
                    "state": "open",
                    "labels": ISSUE_LABEL,
                    "per_page": 100,
                    "sort": "created",
                    "direction": "desc",
                },
                headers=headers,
                timeout=DEFAULT_REQUEST_TIMEOUT,
            )
            list_resp.raise_for_status()
            existing_issues = list_resp.json()

            for issue in existing_issues:
                title = issue.get("title", "")
                # Extract version tag from title pattern:
                # [Claude Code v1.0.0] New release detected
                for release in releases:
                    tag = release["tag_name"]
                    if tag and tag in title:
                        existing_tags.add(tag)

        except requests.exceptions.RequestException as exc:
            log.warning(
                "Failed to check existing issues for dedup: %s. "
                "Proceeding without dedup — may create duplicates.",
                exc,
            )

        new_releases = [
            r for r in releases if r["tag_name"] not in existing_tags
        ]

        log.info(
            "Filtered releases: %d total, %d already tracked, %d new.",
            len(releases),
            len(existing_tags),
            len(new_releases),
        )
        return new_releases

    # ------------------------------------------------------------------
    # Task 3: Create issues for new releases
    # ------------------------------------------------------------------

    @task()
    def create_issues(new_releases: list[dict]) -> None:
        """Create a GitHub issue for each new release.

        Each issue includes:
        - A title with the version tag
        - A 500-character summary of the release body
        - Breaking change detection and warning
        - A link to the original GitHub release

        Args:
            new_releases: List of release dicts from ``filter_new_releases``.
        """
        if not new_releases:
            log.info("No new releases to create issues for.")
            return

        github_token = _resolve_github_token()
        headers = _github_headers(github_token)
        target_repo = Variable.get(
            "omc_github_repo", default_var="baekenough/oh-my-customcode"
        )
        api_url = GITHUB_API_ISSUES_URL.format(repo=target_repo)

        created_count = 0
        failed_count = 0

        for release in new_releases:
            tag = release["tag_name"]
            name = release.get("name", tag)
            body = release.get("body", "")
            html_url = release.get("html_url", "")
            published_at = release.get("published_at", "")
            prerelease = release.get("prerelease", False)

            # Detect breaking changes
            has_breaking = _detect_breaking_changes(body)

            # Build issue body
            issue_body = _build_issue_body(
                tag=tag,
                name=name,
                body=body,
                html_url=html_url,
                published_at=published_at,
                prerelease=prerelease,
                has_breaking=has_breaking,
            )

            issue_title = f"[Claude Code {tag}] New release detected"

            labels = list(ISSUE_LABELS)
            if has_breaking:
                labels.append("breaking-change")

            payload = {
                "title": issue_title,
                "body": issue_body,
                "labels": labels,
            }

            try:
                resp = requests.post(
                    api_url,
                    json=payload,
                    headers=headers,
                    timeout=DEFAULT_REQUEST_TIMEOUT,
                )
                resp.raise_for_status()
                issue_data = resp.json()
                log.info(
                    "Created issue #%s for %s: %s",
                    issue_data.get("number", "?"),
                    tag,
                    issue_data.get("html_url", ""),
                )
                created_count += 1
            except requests.exceptions.HTTPError as exc:
                status = exc.response.status_code
                resp_body = exc.response.text[:500]
                log.error(
                    "Failed to create issue for %s: HTTP %s — %s",
                    tag,
                    status,
                    resp_body,
                )
                failed_count += 1
            except requests.exceptions.RequestException as exc:
                log.error(
                    "Network error creating issue for %s: %s", tag, exc
                )
                failed_count += 1

        log.info(
            "Issue creation complete: %d created, %d failed out of %d.",
            created_count,
            failed_count,
            len(new_releases),
        )

        if failed_count > 0 and created_count == 0:
            raise AirflowFailException(
                f"All {failed_count} issue creation attempts failed."
            )

    # ------------------------------------------------------------------
    # Wire up the task graph
    # ------------------------------------------------------------------
    releases = fetch_releases()
    new = filter_new_releases(releases)
    create_issues(new)


# ---------------------------------------------------------------------------
# Module-level pure helper functions
# ---------------------------------------------------------------------------


def _github_headers(token: str) -> dict[str, str]:
    """Build standard GitHub API request headers.

    Args:
        token: GitHub personal access token.

    Returns:
        Dict of HTTP headers for GitHub API requests.
    """
    return {
        "Authorization": f"Bearer {token}",
        "Accept": "application/vnd.github+json",
        "X-GitHub-Api-Version": "2022-11-28",
    }


def _get(
    url: str,
    headers: dict[str, str] | None = None,
    params: dict | None = None,
) -> requests.Response:
    """Perform an HTTP GET with transient/permanent error distinction.

    Transient errors (timeout, connection error, 5xx, 429) raise a regular
    ``RuntimeError`` so that Airflow's built-in retry mechanism can retry the
    task. Permanent client errors (4xx except 429) raise
    ``AirflowFailException`` to skip retries immediately.

    Args:
        url: The URL to fetch.
        headers: Optional HTTP headers.
        params: Optional query parameters.

    Returns:
        The :class:`requests.Response` object on success.

    Raises:
        RuntimeError: For transient errors (timeout, connection, 5xx, 429).
        AirflowFailException: For permanent client errors (4xx except 429).
    """
    try:
        response = requests.get(
            url, headers=headers, params=params, timeout=DEFAULT_REQUEST_TIMEOUT
        )
        response.raise_for_status()
        return response
    except requests.exceptions.Timeout as exc:
        raise RuntimeError(
            f"Request timed out after {DEFAULT_REQUEST_TIMEOUT}s: {url}"
        ) from exc
    except requests.exceptions.ConnectionError as exc:
        raise RuntimeError(
            f"Connection error while fetching: {url}"
        ) from exc
    except requests.exceptions.HTTPError as exc:
        status = exc.response.status_code
        if 400 <= status < 500 and status != 429:
            raise AirflowFailException(
                f"HTTP {status} from {url}: {exc}"
            ) from exc
        raise RuntimeError(
            f"HTTP {status} from {url}: {exc}"
        ) from exc


def _resolve_github_token() -> str:
    """Resolve GitHub token from Airflow Variable or environment variable.

    Lookup order:
    1. Airflow Variable ``agentnav_github_token``
    2. Environment variable ``GITHUB_TOKEN``

    Returns:
        The token string.

    Raises:
        AirflowFailException: If no token is found in either location.
    """
    token = Variable.get("agentnav_github_token", default_var=None)
    if token:
        return token

    token = os.environ.get("GITHUB_TOKEN")
    if token:
        return token

    raise AirflowFailException(
        "GitHub token not found. Set the Airflow Variable 'agentnav_github_token' "
        "or the environment variable 'GITHUB_TOKEN'."
    )


def _escape_markdown_code(text: str) -> str:
    """Escape characters that break Markdown inline code spans."""
    return text.replace("`", "'")


def _detect_breaking_changes(body: str) -> bool:
    """Detect breaking changes in release body text.

    Scans the release notes body for common breaking change indicators.

    Args:
        body: The release notes body text.

    Returns:
        True if breaking change indicators are found.
    """
    if not body:
        return False
    return bool(BREAKING_CHANGE_PATTERNS.search(body))


def _summarize_body(body: str, max_length: int = MAX_SUMMARY_LENGTH) -> str:
    """Create a truncated summary of the release body.

    Preserves Markdown structure where possible. If truncation is needed,
    cuts at the last complete line that fits within ``max_length`` and
    appends an ellipsis indicator.

    Args:
        body: The full release body text.
        max_length: Maximum character count for the summary.

    Returns:
        A summary string of at most ``max_length`` characters.
    """
    if not body:
        return "_No release notes provided._"

    body = body.strip()
    if len(body) <= max_length:
        return body

    # Try to cut at the last newline before max_length to preserve structure.
    truncated = body[:max_length]
    last_newline = truncated.rfind("\n")
    if last_newline > max_length // 2:
        truncated = truncated[:last_newline]

    return truncated.rstrip() + "\n\n_... (truncated, see full release notes)_"


def _build_issue_body(
    *,
    tag: str,
    name: str,
    body: str,
    html_url: str,
    published_at: str,
    prerelease: bool,
    has_breaking: bool,
) -> str:
    """Build the Markdown body for a release tracking issue.

    Args:
        tag: Git tag name (e.g. "v1.0.23").
        name: Release title/name.
        body: Full release notes body.
        html_url: URL to the GitHub release page.
        published_at: ISO-8601 publication timestamp.
        prerelease: Whether this is a pre-release.
        has_breaking: Whether breaking changes were detected.

    Returns:
        Formatted Markdown string for the issue body.
    """
    summary = _summarize_body(body)
    prerelease_badge = " (pre-release)" if prerelease else ""
    breaking_section = ""

    if has_breaking:
        # Extract lines mentioning breaking changes for visibility.
        breaking_lines = []
        for line in body.splitlines():
            if BREAKING_CHANGE_PATTERNS.search(line):
                breaking_lines.append(f"- {line.strip()}")

        breaking_section = (
            "\n## Breaking Changes Detected\n\n"
            + "\n".join(breaking_lines[:10])
            + "\n"
        )

    lines = [
        f"# Claude Code {tag}{prerelease_badge}",
        "",
        f"**Release:** {_escape_markdown_code(name)}",
        f"**Published:** {published_at}",
        f"**Link:** {html_url}",
        "",
    ]

    if breaking_section:
        lines.append(breaking_section)

    lines += [
        "## Release Summary",
        "",
        summary,
        "",
        "---",
        "",
        "## Action Items",
        "",
        "- [ ] Review release notes for impact on oh-my-customcode",
        "- [ ] Update agent definitions if new Claude Code features affect agents",
        "- [ ] Test compatibility with current oh-my-customcode version",
        "- [ ] Update CLAUDE.md if new capabilities are relevant",
        "",
        "---",
        "",
        "_This issue was created automatically by the "
        "`claude_code_release_monitor` Airflow DAG._",
    ]

    return "\n".join(lines)


# Instantiate the DAG
dag_instance = claude_code_release_monitor()
