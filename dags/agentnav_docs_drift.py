"""
AgentNav Documentation Drift Detector DAG.

Monitors live documentation sites (Claude Platform Docs and Codex Docs) and
compares them against AgentNav baseline agents.json files to detect structural
changes (added or removed pages). When drift is detected, opens a GitHub issue
on the baekenough/AgentNav repository.

Graph:
    fetch_claude_sitemap ──┐
                           ├─► compare_claude ──┐
    fetch_agentnav_claude ─┘                    │
                                                ├─► generate_report ─► notify_if_drift
    fetch_codex_llms_txt ──┐                    │
                           ├─► compare_codex ───┘
    fetch_agentnav_codex ──┘
"""

from __future__ import annotations

import json
import logging
import os
import re
from datetime import datetime, timedelta
from urllib.parse import urlparse
from xml.etree import ElementTree as ET

import requests
from airflow.decorators import dag, task
from airflow.exceptions import AirflowFailException
from airflow.models import Variable

log = logging.getLogger(__name__)

# ---------------------------------------------------------------------------
# Constants – resolved lazily inside tasks to avoid top-level side-effects
# ---------------------------------------------------------------------------
CLAUDE_SITEMAP_URL = "https://platform.claude.com/sitemap.xml"
CLAUDE_SITEMAP_FILTER_PREFIX = "/docs/en/"

CODEX_LLMS_TXT_URL = "https://developers.openai.com/codex/llms.txt"
CODEX_BASE_DOMAIN = "https://developers.openai.com"

AGENTNAV_RAW_BASE = (
    "https://raw.githubusercontent.com/baekenough/AgentNav/main/public"
)
AGENTNAV_CLAUDE_JSON_URL = f"{AGENTNAV_RAW_BASE}/claude-code/agents.json"
AGENTNAV_CODEX_JSON_URL = f"{AGENTNAV_RAW_BASE}/gpt-codex/agents.json"

GITHUB_API_ISSUES_URL = "https://api.github.com/repos/{repo}/issues"

DEFAULT_REQUEST_TIMEOUT = 30  # seconds

# ---------------------------------------------------------------------------
# DAG definition
# ---------------------------------------------------------------------------
default_args = {
    "owner": "agentnav",
    "retries": 1,
    "retry_delay": timedelta(minutes=5),
}


@dag(
    dag_id="agentnav_docs_drift_detector",
    description=(
        "Detects documentation drift between live docs sites and "
        "AgentNav baseline agents.json files."
    ),
    schedule="@daily",
    start_date=datetime(2026, 3, 13),
    catchup=False,
    tags=["agentnav", "docs-monitoring", "drift-detection"],
    default_args=default_args,
    doc_md=__doc__,
)
def agentnav_docs_drift_detector() -> None:
    """Orchestrate drift detection for Claude and Codex documentation."""

    # ------------------------------------------------------------------
    # Helper – shared HTTP fetch with consistent error handling
    # ------------------------------------------------------------------
    def _get(url: str) -> requests.Response:
        """Perform an HTTP GET and raise AirflowFailException on errors."""
        try:
            response = requests.get(url, timeout=DEFAULT_REQUEST_TIMEOUT)
            response.raise_for_status()
            return response
        except requests.exceptions.Timeout as exc:
            raise AirflowFailException(
                f"Request timed out after {DEFAULT_REQUEST_TIMEOUT}s: {url}"
            ) from exc
        except requests.exceptions.ConnectionError as exc:
            raise AirflowFailException(
                f"Connection error while fetching: {url}"
            ) from exc
        except requests.exceptions.HTTPError as exc:
            raise AirflowFailException(
                f"HTTP {exc.response.status_code} from {url}: {exc}"
            ) from exc

    # ------------------------------------------------------------------
    # Fetch tasks
    # ------------------------------------------------------------------

    @task()
    def fetch_claude_sitemap() -> list[str]:
        """Fetch Claude Platform sitemap and return filtered /docs/en/ paths.

        Retrieves the sitemap XML from platform.claude.com, parses every
        ``<loc>`` element, and returns a sorted list of URL paths that start
        with ``/docs/en/``.  The domain portion is stripped so paths are
        directly comparable with the AgentNav baseline.
        """
        response = _get(CLAUDE_SITEMAP_URL)

        try:
            root = ET.fromstring(response.content)
        except ET.ParseError as exc:
            raise AirflowFailException(
                f"Failed to parse sitemap XML from {CLAUDE_SITEMAP_URL}: {exc}"
            ) from exc

        # Sitemap namespace varies; handle both namespaced and bare elements.
        namespace_pattern = re.compile(r"\{[^}]*\}")
        paths: list[str] = []

        for element in root.iter():
            local_tag = namespace_pattern.sub("", element.tag)
            if local_tag == "loc" and element.text:
                url = element.text.strip()
                parsed = urlparse(url)
                path = parsed.path
                if path.startswith(CLAUDE_SITEMAP_FILTER_PREFIX):
                    paths.append(path)

        if not paths:
            raise AirflowFailException(
                f"No /docs/en/ paths found in sitemap at {CLAUDE_SITEMAP_URL}. "
                "The sitemap may have changed structure."
            )

        log.info("Fetched %d Claude docs paths from sitemap.", len(paths))
        return sorted(paths)

    @task()
    def fetch_codex_llms_txt() -> list[str]:
        """Fetch Codex llms.txt and return normalised relative URL paths.

        Retrieves the llms.txt file, extracts URLs from two supported
        line formats:
          - Markdown link: ``- [Title](https://developers.openai.com/path)``
          - Bare URL:      ``https://developers.openai.com/path``

        Returns a sorted list of paths relative to developers.openai.com.
        """
        response = _get(CODEX_LLMS_TXT_URL)
        text = response.text

        paths: list[str] = []
        # Match markdown-style links: [Title](URL)
        md_pattern = re.compile(r"\[([^\]]*)\]\((https?://[^\)]+)\)")
        # Match bare absolute URLs at start of line or after whitespace
        bare_pattern = re.compile(r"(?:^|\s)(https?://developers\.openai\.com[^\s\)>\"']*)")

        for line in text.splitlines():
            line = line.strip()
            if not line:
                continue

            # Try markdown link first
            md_matches = md_pattern.findall(line)
            for _title, url in md_matches:
                url = url.strip()
                parsed = urlparse(url)
                if "developers.openai.com" in parsed.netloc:
                    paths.append(parsed.path or "/")
                continue

            # Try bare URL if no markdown match on this line
            if not md_matches:
                bare_matches = bare_pattern.findall(line)
                for url in bare_matches:
                    url = url.strip()
                    parsed = urlparse(url)
                    if "developers.openai.com" in parsed.netloc:
                        paths.append(parsed.path or "/")

        # Deduplicate while preserving uniqueness
        unique_paths = sorted(set(paths))

        if not unique_paths:
            raise AirflowFailException(
                f"No URLs extracted from llms.txt at {CODEX_LLMS_TXT_URL}. "
                "The file format may have changed."
            )

        log.info("Fetched %d Codex docs paths from llms.txt.", len(unique_paths))
        return unique_paths

    @task()
    def fetch_agentnav_claude() -> list[str]:
        """Fetch AgentNav Claude baseline agents.json and return page paths.

        Retrieves the Claude agents.json from the AgentNav GitHub repo and
        extracts all page paths from the nested ``sections[].pages[].path``
        structure.  Paths are sorted for deterministic comparison.
        """
        response = _get(AGENTNAV_CLAUDE_JSON_URL)

        try:
            data: dict = response.json()
        except json.JSONDecodeError as exc:
            raise AirflowFailException(
                f"Failed to parse JSON from {AGENTNAV_CLAUDE_JSON_URL}: {exc}"
            ) from exc

        paths = _extract_paths_from_agents_json(data, AGENTNAV_CLAUDE_JSON_URL)
        log.info("Loaded %d Claude baseline paths from AgentNav.", len(paths))
        return paths

    @task()
    def fetch_agentnav_codex() -> list[str]:
        """Fetch AgentNav Codex baseline agents.json and return page paths.

        Retrieves the Codex agents.json from the AgentNav GitHub repo and
        extracts all page paths from the nested ``sections[].pages[].path``
        structure.  Paths are sorted for deterministic comparison.
        """
        response = _get(AGENTNAV_CODEX_JSON_URL)

        try:
            data: dict = response.json()
        except json.JSONDecodeError as exc:
            raise AirflowFailException(
                f"Failed to parse JSON from {AGENTNAV_CODEX_JSON_URL}: {exc}"
            ) from exc

        paths = _extract_paths_from_agents_json(data, AGENTNAV_CODEX_JSON_URL)
        log.info("Loaded %d Codex baseline paths from AgentNav.", len(paths))
        return paths

    # ------------------------------------------------------------------
    # Compare tasks
    # ------------------------------------------------------------------

    @task()
    def compare_claude(
        live_pages: list[str],
        baseline_pages: list[str],
    ) -> dict:
        """Compute the diff between live Claude sitemap and AgentNav baseline.

        Args:
            live_pages: Sorted list of paths from the live sitemap.
            baseline_pages: Sorted list of paths from the AgentNav baseline.

        Returns:
            A dict with keys: ``added``, ``removed``, ``added_count``,
            ``removed_count``, ``drift_detected``.
        """
        return _compute_diff(live_pages, baseline_pages, site_label="Claude")

    @task()
    def compare_codex(
        live_pages: list[str],
        baseline_pages: list[str],
    ) -> dict:
        """Compute the diff between live Codex llms.txt and AgentNav baseline.

        Args:
            live_pages: Sorted list of paths from the live llms.txt.
            baseline_pages: Sorted list of paths from the AgentNav baseline.

        Returns:
            A dict with keys: ``added``, ``removed``, ``added_count``,
            ``removed_count``, ``drift_detected``.
        """
        return _compute_diff(live_pages, baseline_pages, site_label="Codex")

    # ------------------------------------------------------------------
    # Report and notify tasks
    # ------------------------------------------------------------------

    @task()
    def generate_report(claude_diff: dict, codex_diff: dict) -> dict:
        """Aggregate Claude and Codex diffs into a human-readable Markdown report.

        Args:
            claude_diff: Output from compare_claude.
            codex_diff: Output from compare_codex.

        Returns:
            A dict with keys: ``report`` (Markdown string) and
            ``drift_detected`` (bool, True if either site has drift).
        """
        now = datetime.utcnow()
        timestamp_str = now.strftime("%Y-%m-%d %H:%M UTC")
        overall_drift = claude_diff["drift_detected"] or codex_diff["drift_detected"]

        lines: list[str] = [
            "# AgentNav Documentation Drift Report",
            "",
            f"**Generated at:** {timestamp_str}",
            f"**Overall drift detected:** {'YES' if overall_drift else 'No'}",
            "",
        ]

        lines += _format_site_section(
            site_name="Claude Platform Docs",
            source_url=CLAUDE_SITEMAP_URL,
            baseline_url=AGENTNAV_CLAUDE_JSON_URL,
            diff=claude_diff,
        )

        lines += _format_site_section(
            site_name="Codex Docs",
            source_url=CODEX_LLMS_TXT_URL,
            baseline_url=AGENTNAV_CODEX_JSON_URL,
            diff=codex_diff,
        )

        lines += [
            "---",
            "",
            "_This report was generated automatically by the "
            "`agentnav_docs_drift_detector` Airflow DAG._",
        ]

        report = "\n".join(lines)
        log.info("Report generated. Drift detected: %s", overall_drift)
        return {"report": report, "drift_detected": overall_drift}

    @task()
    def notify_if_drift(report_payload: dict) -> None:
        """Open a GitHub issue if documentation drift was detected.

        Reads ``drift_detected`` from the payload.  If True, creates a GitHub
        issue on the configured repo with the Markdown report as the body.
        Requires either the ``agentnav_github_token`` Airflow Variable or the
        ``GITHUB_TOKEN`` environment variable to be set.

        If ``drift_detected`` is False, logs an informational message and
        returns without taking any action.

        Args:
            report_payload: Dict with ``report`` (str) and
                            ``drift_detected`` (bool).
        """
        drift_detected: bool = report_payload["drift_detected"]
        report: str = report_payload["report"]

        if not drift_detected:
            log.info("No documentation drift detected. Skipping GitHub notification.")
            return

        log.info("Drift detected. Creating GitHub issue...")
        log.info("Full drift report:\n%s", report)

        # Resolve GitHub token – Airflow Variable takes precedence over env.
        github_token = _resolve_github_token()

        # Resolve target repo.
        github_repo = Variable.get(
            "agentnav_github_repo", default_var="baekenough/AgentNav"
        )

        today = datetime.utcnow().strftime("%Y-%m-%d")
        issue_title = f"[Drift Detected] Documentation structure changed - {today}"

        payload = {
            "title": issue_title,
            "body": report,
            "labels": ["automated", "drift-detection"],
        }

        api_url = GITHUB_API_ISSUES_URL.format(repo=github_repo)
        headers = {
            "Authorization": f"Bearer {github_token}",
            "Accept": "application/vnd.github+json",
            "X-GitHub-Api-Version": "2022-11-28",
        }

        try:
            response = requests.post(
                api_url,
                json=payload,
                headers=headers,
                timeout=DEFAULT_REQUEST_TIMEOUT,
            )
            response.raise_for_status()
        except requests.exceptions.HTTPError as exc:
            status = exc.response.status_code
            body = exc.response.text[:500]
            raise AirflowFailException(
                f"GitHub API returned HTTP {status} when creating issue: {body}"
            ) from exc
        except requests.exceptions.RequestException as exc:
            raise AirflowFailException(
                f"Network error when calling GitHub API: {exc}"
            ) from exc

        issue_data = response.json()
        issue_number = issue_data.get("number", "unknown")
        issue_url = issue_data.get("html_url", "")
        log.info(
            "GitHub issue #%s created successfully: %s", issue_number, issue_url
        )

    # ------------------------------------------------------------------
    # Wire up the task graph
    # ------------------------------------------------------------------
    live_claude = fetch_claude_sitemap()
    live_codex = fetch_codex_llms_txt()
    baseline_claude = fetch_agentnav_claude()
    baseline_codex = fetch_agentnav_codex()

    claude_diff = compare_claude(live_claude, baseline_claude)
    codex_diff = compare_codex(live_codex, baseline_codex)

    report_payload = generate_report(claude_diff, codex_diff)
    notify_if_drift(report_payload)


# ---------------------------------------------------------------------------
# Module-level pure helper functions (no Airflow imports needed – safe at
# module level because they do zero I/O and no heavy computation)
# ---------------------------------------------------------------------------


def _extract_paths_from_agents_json(data: dict, source_url: str) -> list[str]:
    """Extract sorted page paths from an AgentNav agents.json structure.

    The agents.json format nests pages under sections::

        {
          "sections": [
            {
              "pages": [
                {"path": "/docs/en/intro", ...},
                ...
              ]
            },
            ...
          ]
        }

    Args:
        data: Parsed JSON dict.
        source_url: Original URL string (used in error messages only).

    Returns:
        Sorted list of path strings.

    Raises:
        AirflowFailException: If the expected structure is absent.
    """
    sections = data.get("sections")
    if sections is None:
        raise AirflowFailException(
            f"agents.json from {source_url} is missing the 'sections' key. "
            f"Keys found: {list(data.keys())}"
        )

    paths: list[str] = []
    for section in sections:
        for page in section.get("pages", []):
            path = page.get("path")
            if path:
                paths.append(path)

    if not paths:
        raise AirflowFailException(
            f"No page paths found in agents.json from {source_url}. "
            "The file may be empty or the structure has changed."
        )

    return sorted(paths)


def _compute_diff(
    live_pages: list[str],
    baseline_pages: list[str],
    site_label: str,
) -> dict:
    """Compute added/removed pages between live and baseline page sets.

    Args:
        live_pages: Current pages from the live documentation source.
        baseline_pages: Baseline pages from the AgentNav agents.json.
        site_label: Human-readable name used in log messages.

    Returns:
        Dict with keys: ``added`` (list), ``removed`` (list),
        ``added_count`` (int), ``removed_count`` (int),
        ``drift_detected`` (bool).
    """
    live_set = set(live_pages)
    baseline_set = set(baseline_pages)

    added = sorted(live_set - baseline_set)
    removed = sorted(baseline_set - live_set)

    drift = bool(added or removed)

    log.info(
        "[%s] Live: %d pages | Baseline: %d pages | Added: %d | Removed: %d | "
        "Drift: %s",
        site_label,
        len(live_set),
        len(baseline_set),
        len(added),
        len(removed),
        drift,
    )

    return {
        "added": added,
        "removed": removed,
        "added_count": len(added),
        "removed_count": len(removed),
        "drift_detected": drift,
    }


def _format_site_section(
    site_name: str,
    source_url: str,
    baseline_url: str,
    diff: dict,
) -> list[str]:
    """Render one site's diff as Markdown lines for the drift report.

    Args:
        site_name: Display name (e.g. "Claude Platform Docs").
        source_url: URL of the live source (sitemap or llms.txt).
        baseline_url: URL of the AgentNav baseline agents.json.
        diff: Dict produced by ``_compute_diff``.

    Returns:
        List of Markdown text lines (no trailing newline per item).
    """
    status_icon = "DRIFT DETECTED" if diff["drift_detected"] else "No drift"

    lines = [
        f"## {site_name}",
        "",
        f"- **Status:** {status_icon}",
        f"- **Live source:** {source_url}",
        f"- **Baseline:** {baseline_url}",
        f"- **Pages added (live has, baseline missing):** {diff['added_count']}",
        f"- **Pages removed (baseline has, live missing):** {diff['removed_count']}",
        "",
    ]

    if diff["added"]:
        lines += ["### Added pages", ""]
        for path in diff["added"]:
            lines.append(f"- `{path}`")
        lines.append("")

    if diff["removed"]:
        lines += ["### Removed pages", ""]
        for path in diff["removed"]:
            lines.append(f"- `{path}`")
        lines.append("")

    if not diff["drift_detected"]:
        lines += ["_No structural changes detected._", ""]

    return lines


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


# Instantiate the DAG
dag_instance = agentnav_docs_drift_detector()
