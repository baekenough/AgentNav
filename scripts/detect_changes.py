"""Detect changes in documentation sources for AgentNav.

Usage:
    python scripts/detect_changes.py [--source SOURCE] [--verbose] [--init]

Exit codes:
    0 — changes detected
    1 — no changes detected
"""

import argparse
import hashlib
import json
import logging
import sys
import xml.etree.ElementTree as ET
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

import httpx

CACHE_DIR = Path(__file__).parent / ".cache"
HASHES_FILE = CACHE_DIR / "hashes.json"

USER_AGENT = "AgentNav/1.0 (https://agentnav.baekenough.com)"
REQUEST_TIMEOUT = 15

SOURCES: dict[str, list[dict[str, str]]] = {
    "claude-code": [
        {
            "key": "llms_txt",
            "url": "https://code.claude.com/docs/llms.txt",
            "method": "hash",
        },
        {
            "key": "github_releases",
            "url": "https://github.com/anthropics/claude-code/releases.atom",
            "method": "atom",
        },
        {
            "key": "release_notes",
            "url": "https://platform.claude.com/docs/en/release-notes/overview",
            "method": "etag",
        },
    ],
    "gpt-codex": [
        {
            "key": "changelog",
            "url": "https://developers.openai.com/codex/changelog/",
            "method": "hash",
        },
        {
            "key": "github_releases",
            "url": "https://github.com/openai/codex/releases.atom",
            "method": "atom",
        },
    ],
}

log = logging.getLogger(__name__)


def _session() -> httpx.Client:
    """Return an httpx client with the project User-Agent."""
    return httpx.Client(headers={"User-Agent": USER_AGENT})


def _now_iso() -> str:
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def _sha256(content: bytes) -> str:
    return hashlib.sha256(content).hexdigest()


def _load_cache() -> dict[str, Any]:
    if HASHES_FILE.exists():
        with HASHES_FILE.open() as f:
            return json.load(f)
    return {}


def _save_cache(cache: dict[str, Any]) -> None:
    CACHE_DIR.mkdir(parents=True, exist_ok=True)
    with HASHES_FILE.open("w") as f:
        json.dump(cache, f, indent=2)


# ---------------------------------------------------------------------------
# Per-method checkers
# ---------------------------------------------------------------------------


def _check_hash(
    source_key: str,
    entry_key: str,
    url: str,
    prev: dict[str, Any],
    session: httpx.Client,
) -> dict[str, Any]:
    """Fetch URL, compare SHA-256 hash against cached value."""
    try:
        response = session.get(url, timeout=REQUEST_TIMEOUT)
        response.raise_for_status()
    except httpx.HTTPError as exc:
        log.warning("Skip %s/%s — network error: %s", source_key, entry_key, exc)
        return {"changed": False, "error": str(exc)}

    current_hash = _sha256(response.content)
    prev_hash = prev.get("hash")
    changed = prev_hash is not None and current_hash != prev_hash

    log.debug("%s/%s hash: %s (prev: %s)", source_key, entry_key, current_hash[:12], (prev_hash or "")[:12])

    return {
        "changed": changed,
        "_new_state": {"hash": current_hash, "checked_at": _now_iso()},
    }


def _check_atom(
    source_key: str,
    entry_key: str,
    url: str,
    prev: dict[str, Any],
    session: httpx.Client,
) -> dict[str, Any]:
    """Fetch Atom feed, compare latest entry id against cached value."""
    try:
        response = session.get(url, timeout=REQUEST_TIMEOUT)
        response.raise_for_status()
    except httpx.HTTPError as exc:
        log.warning("Skip %s/%s — network error: %s", source_key, entry_key, exc)
        return {"changed": False, "error": str(exc)}

    try:
        root = ET.fromstring(response.content)
    except ET.ParseError as exc:
        log.warning("Skip %s/%s — XML parse error: %s", source_key, entry_key, exc)
        return {"changed": False, "error": str(exc)}

    ns = {"atom": "http://www.w3.org/2005/Atom"}
    first_entry = root.find("atom:entry", ns)
    if first_entry is None:
        log.warning("Skip %s/%s — no entries in feed", source_key, entry_key)
        return {"changed": False, "error": "no entries in feed"}

    entry_id = (first_entry.findtext("atom:id", namespaces=ns) or "").strip()
    published_raw = (
        first_entry.findtext("atom:published", namespaces=ns)
        or first_entry.findtext("atom:updated", namespaces=ns)
        or ""
    ).strip()
    # Keep only the date portion for the report.
    published_date = published_raw[:10] if published_raw else ""

    # Extract tag name from the id field (last path segment).
    latest_tag = entry_id.rsplit("/", 1)[-1] if entry_id else ""

    prev_id = prev.get("latest_id")
    changed = prev_id is not None and entry_id != prev_id

    log.debug("%s/%s atom id: %s (prev: %s)", source_key, entry_key, entry_id[:40], (prev_id or "")[:40])

    result: dict[str, Any] = {
        "changed": changed,
        "_new_state": {"latest_id": entry_id, "checked_at": _now_iso()},
    }
    if changed:
        result["latest_tag"] = latest_tag
        result["published"] = published_date
    return result


def _check_etag(
    source_key: str,
    entry_key: str,
    url: str,
    prev: dict[str, Any],
    session: httpx.Client,
) -> dict[str, Any]:
    """Use HTTP ETag / Last-Modified headers to detect changes."""
    headers: dict[str, str] = {}
    if prev.get("etag"):
        headers["If-None-Match"] = prev["etag"]
    if prev.get("last_modified"):
        headers["If-Modified-Since"] = prev["last_modified"]

    try:
        response = session.get(url, headers=headers, timeout=REQUEST_TIMEOUT)
    except httpx.HTTPError as exc:
        log.warning("Skip %s/%s — network error: %s", source_key, entry_key, exc)
        return {"changed": False, "error": str(exc)}

    if response.status_code == 304:
        log.debug("%s/%s — 304 Not Modified", source_key, entry_key)
        return {
            "changed": False,
            "_new_state": {**prev, "checked_at": _now_iso()},
        }

    new_etag = response.headers.get("ETag", "")
    new_last_modified = response.headers.get("Last-Modified", "")

    # First run (no prev values) → not a change, just store.
    is_first_run = not prev.get("etag") and not prev.get("last_modified")
    changed = (
        not is_first_run
        and response.status_code == 200
        and (new_etag != prev.get("etag") or new_last_modified != prev.get("last_modified"))
    )

    log.debug(
        "%s/%s etag=%s lm=%s changed=%s",
        source_key, entry_key, new_etag[:20], new_last_modified[:20], changed,
    )

    return {
        "changed": changed,
        "_new_state": {
            "etag": new_etag,
            "last_modified": new_last_modified,
            "checked_at": _now_iso(),
        },
    }


# ---------------------------------------------------------------------------
# Orchestration
# ---------------------------------------------------------------------------

_CHECKERS = {
    "hash": _check_hash,
    "atom": _check_atom,
    "etag": _check_etag,
}


def check_source(
    source_name: str,
    entries: list[dict[str, str]],
    cache: dict[str, Any],
    session: httpx.Client,
    init_mode: bool,
) -> dict[str, Any]:
    """Check all entries for a named source and return the result map."""
    source_cache = cache.setdefault(source_name, {})
    result: dict[str, Any] = {}

    for entry in entries:
        key = entry["key"]
        url = entry["url"]
        method = entry["method"]

        prev = source_cache.get(key, {})
        checker = _CHECKERS[method]
        entry_result = checker(source_name, key, url, prev, session)

        # Persist new state unconditionally (whether init or normal run).
        new_state = entry_result.pop("_new_state", None)
        if new_state:
            source_cache[key] = new_state

        # In init mode suppress "changed" flag — we are just seeding the cache.
        if init_mode:
            entry_result["changed"] = False

        result[key] = entry_result

    return result


def run(
    source_filter: str | None,
    verbose: bool,
    init_mode: bool,
) -> dict[str, Any]:
    """Execute change detection and return the report dict.

    The returned dict has the shape::

        {
            "changes_detected": bool,
            "checked_at": str,          # ISO-8601 UTC
            "sources": {
                "<source-name>": {
                    "<entry-key>": {"changed": bool, ...},
                    ...
                },
                ...
            },
        }
    """
    logging.basicConfig(
        level=logging.DEBUG if verbose else logging.WARNING,
        format="%(levelname)s %(message)s",
    )

    cache = _load_cache()
    # First run with no cache → implicit init mode.
    if not HASHES_FILE.exists():
        log.warning("No cache found — running in init mode (seeding hashes).")
        init_mode = True

    session = _session()
    checked_at = _now_iso()

    sources_to_check = (
        {source_filter: SOURCES[source_filter]}
        if source_filter
        else SOURCES
    )

    all_results: dict[str, Any] = {}
    any_changed = False

    for source_name, entries in sources_to_check.items():
        source_result = check_source(source_name, entries, cache, session, init_mode)
        all_results[source_name] = source_result
        if any(v.get("changed") for v in source_result.values()):
            any_changed = True

    _save_cache(cache)

    return {
        "changes_detected": any_changed,
        "checked_at": checked_at,
        "sources": all_results,
    }


def _build_gha_markers(report: dict[str, Any]) -> str:
    """Return GitHub Actions-compatible marker lines for the given report.

    Format::

        CHANGES_DETECTED=true
        SOURCE_NAME=claude-code,gpt-codex
        REPORT_START
        ## Changes detected at <timestamp>
        ...
        REPORT_END

    Only sources with at least one changed entry appear in SOURCE_NAME and
    the REPORT block.  When no changes are detected, the REPORT block is
    omitted entirely.
    """
    any_changed: bool = report["changes_detected"]
    checked_at: str = report["checked_at"]
    sources: dict[str, Any] = report["sources"]

    changed_sources = [
        name
        for name, entries in sources.items()
        if any(v.get("changed") for v in entries.values())
    ]

    lines: list[str] = [
        f"CHANGES_DETECTED={'true' if any_changed else 'false'}",
        f"SOURCE_NAME={','.join(changed_sources)}",
    ]

    if not any_changed:
        return "\n".join(lines)

    report_lines: list[str] = [
        "REPORT_START",
        f"## Changes detected at {checked_at}",
    ]

    for source_name in changed_sources:
        entries = sources[source_name]
        report_lines.append(f"\n### {source_name}")
        for entry_key, entry_data in entries.items():
            if not entry_data.get("changed"):
                continue
            detail_parts: list[str] = ["changed"]
            if "latest_tag" in entry_data:
                detail_parts.append(f"latest: {entry_data['latest_tag']}")
            if "url" in entry_data:
                detail_parts.append(entry_data["url"])
            detail = " (" + ", ".join(detail_parts[1:]) + ")" if len(detail_parts) > 1 else ""
            report_lines.append(f"- **{entry_key}**: changed{detail}")

    report_lines.append("REPORT_END")
    lines.extend(report_lines)
    return "\n".join(lines)


def _build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Detect changes in AgentNav documentation sources.",
    )
    parser.add_argument(
        "--source",
        choices=list(SOURCES.keys()),
        default=None,
        help="Limit checks to a single source.",
    )
    parser.add_argument(
        "--verbose",
        action="store_true",
        help="Enable debug logging.",
    )
    parser.add_argument(
        "--init",
        action="store_true",
        help="Seed the hash cache without reporting changes.",
    )
    return parser


if __name__ == "__main__":
    parser = _build_parser()
    args = parser.parse_args()
    report = run(args.source, args.verbose, args.init)
    print(json.dumps(report, indent=2))
    print()
    print(_build_gha_markers(report))
    sys.exit(0 if report["changes_detected"] else 1)
