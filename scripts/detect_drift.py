#!/usr/bin/env python3
"""Docs Drift Detector — URL-set comparison for AgentNav documentation sets.

Compares baseline URL sets against upstream llms.txt sources to detect
structural documentation changes (added/removed pages). Ignores formatting
and description changes to minimize false positives.

Usage:
    python scripts/detect_drift.py             # Run drift detection
    python scripts/detect_drift.py --init      # Initialize baselines from upstream
    python scripts/detect_drift.py --dry-run   # Detect without creating issues
"""

from __future__ import annotations

import argparse
import json
import os
import re
import sys
import xml.etree.ElementTree as ET
from dataclasses import dataclass, field
from datetime import datetime, timezone
from pathlib import Path
from typing import Optional
from urllib.parse import urljoin, urlparse

import requests

# ---------------------------------------------------------------------------
# Constants
# ---------------------------------------------------------------------------

BASELINES_DIR = Path(__file__).resolve().parent / "baselines"

SOURCES: dict[str, dict] = {
    "claude-code": {
        "name": "Claude Code",
        "llms_url": "https://code.claude.com/llms.txt",
        "strategy": "markdown_links",
        "domain_filter": "code.claude.com",
    },
    "gpt-codex": {
        "name": "GPT Codex",
        "llms_url": "https://developers.openai.com/codex/llms.txt",
        "strategy": "markdown_links",
        "domain_filter": "developers.openai.com",
    },
    "gemini-cli": {
        "name": "Gemini CLI",
        "llms_url": "https://geminicli.com/llms.txt",
        "strategy": "markdown_links",
        "domain_filter": "geminicli.com",
    },
    "claude-api": {
        "name": "Claude API",
        "llms_url": "https://platform.claude.com/llms.txt",
        "strategy": "markdown_links",
        "domain_filter": "platform.claude.com",
    },
    "vercel": {
        "name": "Vercel",
        "llms_url": "https://vercel.com/llms.txt",
        "strategy": "markdown_links",
        "domain_filter": "vercel.com",
    },
    "supabase": {
        "name": "Supabase",
        "llms_url": "https://supabase.com/llms.txt",
        "strategy": "supabase_subfiles",
        "domain_filter": "supabase.com",
        "base_url": "https://supabase.com",
    },
}

GITHUB_API = "https://api.github.com"
ISSUE_LABELS = ["docs-drift", "automated"]
REQUEST_TIMEOUT = 30


# ---------------------------------------------------------------------------
# Data classes
# ---------------------------------------------------------------------------


@dataclass
class DriftResult:
    """Result of comparing baseline vs upstream URL sets."""

    source_key: str
    source_name: str
    added: set[str] = field(default_factory=set)
    removed: set[str] = field(default_factory=set)
    baseline_count: int = 0
    upstream_count: int = 0
    error: Optional[str] = None

    @property
    def has_drift(self) -> bool:
        return bool(self.added or self.removed)


# ---------------------------------------------------------------------------
# URL extraction strategies
# ---------------------------------------------------------------------------

# Matches: - [Title](URL) or - [Title](URL): Description
# Also:    [Title](URL) at line start (header links)
# Also:    nested items like "  - [Title](URL)"
# Note:    URL part excludes [ ] to avoid matching across nested markdown links
MARKDOWN_LINK_RE = re.compile(r"\[([^\]]*)\]\((https?://[^)\[\]]+)\)")


def extract_urls_markdown_links(
    content: str, domain_filter: str
) -> set[str]:
    """Extract documentation URLs from markdown link format.

    Only returns URLs matching the domain filter to exclude external
    references (GitHub PRs, blog posts, images, etc.).
    """
    urls: set[str] = set()
    for _title, url in MARKDOWN_LINK_RE.findall(content):
        try:
            parsed = urlparse(url)
        except ValueError:
            # Skip malformed URLs (e.g., invalid IPv6)
            continue
        # Match domain (with or without www prefix)
        host = parsed.hostname or ""
        if host == domain_filter or host == f"www.{domain_filter}":
            # Normalize: remove fragment, trailing slash, query params
            normalized = f"{parsed.scheme}://{parsed.netloc}{parsed.path}"
            normalized = normalized.rstrip("/")
            urls.add(normalized)
    return urls


def extract_urls_supabase_subfiles(
    content: str, source_cfg: dict
) -> set[str]:
    """Extract URLs from Supabase's sub-file index structure.

    Supabase llms.txt contains links to sub-files (guides.txt, js.txt, etc.).
    Each sub-file contains inline docs with relative paths like /docs/guides/ai.
    We fetch each sub-file and extract the relative doc paths.
    """
    base_url = source_cfg["base_url"]
    domain_filter = source_cfg["domain_filter"]

    # Step 1: Find sub-file URLs from the index
    subfile_urls: list[str] = []
    for _title, url in MARKDOWN_LINK_RE.findall(content):
        parsed = urlparse(url)
        host = parsed.hostname or ""
        if (host == domain_filter or host == f"www.{domain_filter}") and url.endswith(
            ".txt"
        ):
            subfile_urls.append(url)

    if not subfile_urls:
        return set()

    # Step 2: Fetch each sub-file and extract relative doc paths
    all_urls: set[str] = set()
    # Pattern for relative paths: [Text](/docs/...) or (/docs/...)
    relative_path_re = re.compile(r"\]\((/docs/[^)#]+)")

    for subfile_url in subfile_urls:
        try:
            resp = requests.get(subfile_url, timeout=REQUEST_TIMEOUT)
            resp.raise_for_status()
            sub_content = resp.text

            for match in relative_path_re.findall(sub_content):
                path = match.rstrip("/")
                full_url = f"{base_url}{path}"
                all_urls.add(full_url)
        except requests.RequestException as e:
            print(f"  Warning: Failed to fetch sub-file {subfile_url}: {e}")
            continue

    return all_urls


def extract_urls(source_key: str, content: str) -> set[str]:
    """Extract documentation URLs using the appropriate strategy."""
    cfg = SOURCES[source_key]
    strategy = cfg["strategy"]

    if strategy == "markdown_links":
        return extract_urls_markdown_links(content, cfg["domain_filter"])
    elif strategy == "supabase_subfiles":
        return extract_urls_supabase_subfiles(content, cfg)
    else:
        raise ValueError(f"Unknown strategy: {strategy}")


# ---------------------------------------------------------------------------
# Baseline management
# ---------------------------------------------------------------------------


def baseline_path(source_key: str) -> Path:
    """Return the baseline file path for a source."""
    return BASELINES_DIR / f"{source_key}.txt"


def load_baseline(source_key: str) -> set[str]:
    """Load baseline URL set from file."""
    path = baseline_path(source_key)
    if not path.exists():
        return set()
    return {line.strip() for line in path.read_text().splitlines() if line.strip()}


def save_baseline(source_key: str, urls: set[str]) -> None:
    """Save URL set to baseline file (sorted for stable diffs)."""
    path = baseline_path(source_key)
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("\n".join(sorted(urls)) + "\n")


# ---------------------------------------------------------------------------
# Upstream fetching
# ---------------------------------------------------------------------------


def fetch_upstream(source_key: str) -> tuple[str, Optional[str]]:
    """Fetch upstream llms.txt content. Returns (content, error)."""
    cfg = SOURCES[source_key]
    url = cfg["llms_url"]
    try:
        resp = requests.get(url, timeout=REQUEST_TIMEOUT)
        resp.raise_for_status()
        return resp.text, None
    except requests.RequestException as e:
        return "", f"Failed to fetch {url}: {e}"


# ---------------------------------------------------------------------------
# Drift detection
# ---------------------------------------------------------------------------


def detect_drift(source_key: str) -> DriftResult:
    """Compare baseline vs upstream for a single source."""
    cfg = SOURCES[source_key]
    result = DriftResult(source_key=source_key, source_name=cfg["name"])

    # Fetch upstream
    content, error = fetch_upstream(source_key)
    if error:
        result.error = error
        return result

    # Extract URLs
    upstream_urls = extract_urls(source_key, content)
    baseline_urls = load_baseline(source_key)

    result.upstream_count = len(upstream_urls)
    result.baseline_count = len(baseline_urls)
    result.added = upstream_urls - baseline_urls
    result.removed = baseline_urls - upstream_urls

    return result


# ---------------------------------------------------------------------------
# GitHub issue management
# ---------------------------------------------------------------------------


def get_github_env() -> tuple[str, str]:
    """Get GitHub token and repository from environment."""
    token = os.environ.get("GITHUB_TOKEN", "")
    repo = os.environ.get("GITHUB_REPOSITORY", "baekenough/AgentNav")
    return token, repo


def has_open_issue(token: str, repo: str, source_name: str) -> bool:
    """Check if there's already an open issue for this source."""
    url = f"{GITHUB_API}/repos/{repo}/issues"
    headers = {
        "Authorization": f"Bearer {token}",
        "Accept": "application/vnd.github+json",
    }
    params = {
        "labels": ",".join(ISSUE_LABELS),
        "state": "open",
        "per_page": 100,
    }

    try:
        resp = requests.get(url, headers=headers, params=params, timeout=REQUEST_TIMEOUT)
        resp.raise_for_status()
        issues = resp.json()

        # Check if any open issue title contains the source name
        prefix = f"[Docs Drift] {source_name}"
        return any(issue["title"].startswith(prefix) for issue in issues)
    except requests.RequestException:
        return False


def create_issue(token: str, repo: str, result: DriftResult) -> Optional[str]:
    """Create a GitHub issue for detected drift. Returns issue URL or None."""
    today = datetime.now(timezone.utc).strftime("%Y-%m-%d")
    title = f"[Docs Drift] {result.source_name} documentation changes detected — {today}"

    # Build body
    body_parts = [
        f"## Documentation Drift Detected: {result.source_name}\n",
        f"**Source**: `{SOURCES[result.source_key]['llms_url']}`",
        f"**Baseline pages**: {result.baseline_count}",
        f"**Upstream pages**: {result.upstream_count}",
        f"**Change**: {result.baseline_count} → {result.upstream_count} "
        f"({'+' if result.upstream_count >= result.baseline_count else ''}"
        f"{result.upstream_count - result.baseline_count})\n",
    ]

    if result.added:
        body_parts.append("### Added pages\n")
        added_sorted = sorted(result.added)
        display_count = min(len(added_sorted), 20)
        for url in added_sorted[:display_count]:
            body_parts.append(f"- {url}")
        if len(added_sorted) > 20:
            body_parts.append(f"- ... and {len(added_sorted) - 20} more\n")
        else:
            body_parts.append("")

    if result.removed:
        body_parts.append("### Removed pages\n")
        removed_sorted = sorted(result.removed)
        display_count = min(len(removed_sorted), 20)
        for url in removed_sorted[:display_count]:
            body_parts.append(f"- {url}")
        if len(removed_sorted) > 20:
            body_parts.append(f"- ... and {len(removed_sorted) - 20} more\n")
        else:
            body_parts.append("")

    body_parts.extend(
        [
            "### Action items\n",
            "- [ ] Review upstream changes",
            "- [ ] Update local agents.json if needed",
            "- [ ] Regenerate format files (md/xml/txt)",
            "- [ ] Deploy updated documentation",
            "",
            "---",
            "*This issue was automatically created by the docs drift detector.*",
        ]
    )

    body = "\n".join(body_parts)

    # Ensure labels exist
    ensure_labels(token, repo)

    url = f"{GITHUB_API}/repos/{repo}/issues"
    headers = {
        "Authorization": f"Bearer {token}",
        "Accept": "application/vnd.github+json",
    }
    payload = {
        "title": title,
        "body": body,
        "labels": ISSUE_LABELS,
    }

    try:
        resp = requests.post(
            url, headers=headers, json=payload, timeout=REQUEST_TIMEOUT
        )
        resp.raise_for_status()
        issue_data = resp.json()
        return issue_data.get("html_url")
    except requests.RequestException as e:
        print(f"  Error creating issue: {e}")
        return None


def ensure_labels(token: str, repo: str) -> None:
    """Ensure required labels exist in the repository."""
    headers = {
        "Authorization": f"Bearer {token}",
        "Accept": "application/vnd.github+json",
    }
    label_configs = {
        "docs-drift": {"color": "d93f0b", "description": "Documentation drift detected"},
        "automated": {"color": "0e8a16", "description": "Automatically generated"},
    }

    for label_name, config in label_configs.items():
        url = f"{GITHUB_API}/repos/{repo}/labels"
        payload = {"name": label_name, **config}
        try:
            resp = requests.post(
                url, headers=headers, json=payload, timeout=REQUEST_TIMEOUT
            )
            # 422 means label already exists — that's fine
            if resp.status_code not in (201, 422):
                resp.raise_for_status()
        except requests.RequestException:
            pass  # Non-critical — label may already exist


# ---------------------------------------------------------------------------
# Main commands
# ---------------------------------------------------------------------------


def cmd_init() -> int:
    """Initialize baselines from upstream sources."""
    print("Initializing baselines from upstream sources...\n")
    BASELINES_DIR.mkdir(parents=True, exist_ok=True)

    errors = 0
    for source_key, cfg in SOURCES.items():
        print(f"  [{cfg['name']}] Fetching {cfg['llms_url']}...")
        content, error = fetch_upstream(source_key)
        if error:
            print(f"  [{cfg['name']}] ERROR: {error}")
            errors += 1
            continue

        urls = extract_urls(source_key, content)
        save_baseline(source_key, urls)
        print(f"  [{cfg['name']}] Saved {len(urls)} URLs to {baseline_path(source_key)}")

    print(f"\nBaseline initialization complete. Errors: {errors}/{len(SOURCES)}")
    return 1 if errors > 0 else 0


def cmd_detect(dry_run: bool = False) -> int:
    """Run drift detection against all sources."""
    print("Running docs drift detection...\n")

    token, repo = get_github_env()
    if not dry_run and not token:
        print("ERROR: GITHUB_TOKEN not set. Use --dry-run for local testing.")
        return 1

    results: list[DriftResult] = []
    baselines_updated = False

    for source_key, cfg in SOURCES.items():
        print(f"  [{cfg['name']}] Checking...")
        result = detect_drift(source_key)

        if result.error:
            print(f"  [{cfg['name']}] ERROR: {result.error}")
            results.append(result)
            continue

        if not result.has_drift:
            print(
                f"  [{cfg['name']}] No drift detected "
                f"({result.upstream_count} pages)"
            )
            results.append(result)
            continue

        # Drift detected
        print(
            f"  [{cfg['name']}] DRIFT DETECTED: "
            f"{result.baseline_count} → {result.upstream_count} pages "
            f"(+{len(result.added)}, -{len(result.removed)})"
        )

        if dry_run:
            print(f"  [{cfg['name']}] DRY RUN — skipping issue creation")
            if result.added:
                for url in sorted(result.added)[:5]:
                    print(f"    + {url}")
                if len(result.added) > 5:
                    print(f"    ... and {len(result.added) - 5} more added")
            if result.removed:
                for url in sorted(result.removed)[:5]:
                    print(f"    - {url}")
                if len(result.removed) > 5:
                    print(f"    ... and {len(result.removed) - 5} more removed")
        else:
            # Check for existing open issue (dedup)
            if has_open_issue(token, repo, cfg["name"]):
                print(
                    f"  [{cfg['name']}] Open issue already exists — skipping"
                )
            else:
                issue_url = create_issue(token, repo, result)
                if issue_url:
                    print(f"  [{cfg['name']}] Issue created: {issue_url}")
                else:
                    print(f"  [{cfg['name']}] Failed to create issue")

        # Update baseline after detection (even in dry-run for testing)
        if not dry_run:
            upstream_urls = load_baseline(source_key)
            upstream_urls = upstream_urls | result.added
            upstream_urls = upstream_urls - result.removed
            save_baseline(source_key, upstream_urls)
            baselines_updated = True
            print(f"  [{cfg['name']}] Baseline updated")

        results.append(result)

    # Summary
    print("\n" + "=" * 60)
    print("SUMMARY")
    print("=" * 60)

    drift_count = sum(1 for r in results if r.has_drift)
    error_count = sum(1 for r in results if r.error)

    for r in results:
        if r.error:
            status = f"ERROR: {r.error}"
        elif r.has_drift:
            status = (
                f"DRIFT: {r.baseline_count} → {r.upstream_count} "
                f"(+{len(r.added)}, -{len(r.removed)})"
            )
        else:
            status = f"OK ({r.upstream_count} pages)"
        print(f"  {r.source_name}: {status}")

    print(f"\nTotal: {len(results)} sources, {drift_count} with drift, {error_count} errors")

    if baselines_updated:
        print("\nBaseline files updated — remember to commit changes.")

    return 0


# ---------------------------------------------------------------------------
# CLI entry point
# ---------------------------------------------------------------------------


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Docs Drift Detector — URL-set comparison for AgentNav"
    )
    parser.add_argument(
        "--init",
        action="store_true",
        help="Initialize baselines from upstream sources",
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Detect drift without creating GitHub issues",
    )
    args = parser.parse_args()

    if args.init:
        return cmd_init()
    else:
        return cmd_detect(dry_run=args.dry_run)


if __name__ == "__main__":
    sys.exit(main())
