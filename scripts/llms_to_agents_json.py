#!/usr/bin/env python3
"""Convert llms.txt (or sitemap XML) to agents.json format.

Supports two input modes:

  llms-links mode (default):
    Parses a llms.txt file that uses Markdown link lists:
      ## Section Name
      - [Title](https://example.com/path): Description
        - [Sub Title](https://example.com/path/sub): Description

    Usage:
      python scripts/llms_to_agents_json.py \\
          --url https://vercel.com/llms.txt \\
          --output public/vercel/agents.json \\
          --site-url https://vercel.com \\
          --site-name "Vercel Documentation"

  sitemap mode (--sitemap):
    Parses a sitemap.xml and derives titles from URL slugs.
    Optionally filters to a path prefix.

    Usage:
      python scripts/llms_to_agents_json.py \\
          --sitemap https://supabase.com/docs/sitemap.xml \\
          --output public/supabase/agents.json \\
          --site-url https://supabase.com \\
          --site-name "Supabase Documentation" \\
          --path-prefix /docs/guides/

  index mode (--index):
    Parses a llms.txt that is an index of sub-URLs (each line is a link to
    another llms.txt). Fetches each sub-file and treats it as a section.

    Usage:
      python scripts/llms_to_agents_json.py \\
          --index \\
          --url https://example.com/llms.txt \\
          --output public/example/agents.json \\
          --site-url https://example.com
"""

from __future__ import annotations

import argparse
import json
import re
import sys
import urllib.request
import urllib.error
from datetime import date
from pathlib import Path
from urllib.parse import urlparse
from xml.etree import ElementTree


# ---------------------------------------------------------------------------
# Page type classification
# ---------------------------------------------------------------------------

_TYPE_RULES: list[tuple[list[str], str]] = [
    # keyword lists are matched against the URL path (lowercase)
    (["overview", "introduction", "what-is", "about"], "overview"),
    (["quickstart", "getting-started", "quick-start", "tutorial", "tutorials"], "tutorial"),
    (["quickstarts", "examples"], "tutorial"),
    (["best-practices", "patterns", "style-guide"], "best-practices"),
    (["changelog", "release-notes", "releases", "whats-new"], "changelog"),
    (["cli", "command-line", "commands"], "tool-reference"),
    (["sdk", "client-library", "client-libraries"], "sdk-guide"),
    (["/api/", "api-reference", "endpoint", "endpoints"], "api-endpoint"),
    (["reference/javascript", "reference/python", "reference/dart",
      "reference/swift", "reference/kotlin", "reference/csharp"], "sdk-guide"),
    (["reference/cli"], "tool-reference"),
    (["reference/api"], "api-reference"),
    (["reference/"], "reference"),
    (["configuration", "config", "settings"], "reference"),
    (["pricing", "billing"], "reference"),
    (["guide", "guides", "how-to", "howto"], "guide"),
]

_TYPE_TITLE_RULES: list[tuple[list[str], str]] = [
    (["overview", "introduction", "what is"], "overview"),
    (["quickstart", "getting started", "tutorial"], "tutorial"),
    (["best practice", "pattern"], "best-practices"),
    (["changelog", "release note"], "changelog"),
    (["cli reference", "command reference", "command-line"], "tool-reference"),
    (["sdk reference", "client reference"], "sdk-guide"),
    (["api reference"], "api-reference"),
    (["configuration", "settings", "pricing", "billing"], "reference"),
]


def classify_page_type(path: str, title: str = "") -> str:
    """Return the most appropriate agents.txt page type for a given path/title.

    Applies path-based rules first (more reliable), then title-based rules,
    falling back to 'guide' when nothing matches.
    """
    path_lower = path.lower()
    title_lower = title.lower()

    for keywords, page_type in _TYPE_RULES:
        if any(kw in path_lower for kw in keywords):
            return page_type

    for keywords, page_type in _TYPE_TITLE_RULES:
        if any(kw in title_lower for kw in keywords):
            return page_type

    return "guide"


# ---------------------------------------------------------------------------
# Title derivation from URL slug
# ---------------------------------------------------------------------------

# Words that should stay lowercase in title-cased output (common stop words)
_LOWERCASE_WORDS = frozenset({
    "a", "an", "the", "and", "or", "but", "in", "on", "at", "to", "for",
    "of", "with", "by", "from", "as", "into", "via", "vs",
})

# Common acronyms to preserve as uppercase
_ACRONYMS = frozenset({
    "api", "sdk", "cli", "url", "uri", "sql", "id", "ai", "ml", "ui",
    "ux", "sso", "saml", "jwt", "oauth", "mcp", "http", "https", "dns",
    "ssl", "tls", "cdn", "cors", "rbac", "rls", "iam", "aws", "gcp",
    "oci", "s3", "kv",
})


def slug_to_title(slug: str) -> str:
    """Convert a URL slug to a human-readable title.

    Examples:
      'getting-started'     -> 'Getting Started'
      'api-reference'       -> 'API Reference'
      'saml-sso'            -> 'SAML SSO'
      'row-level-security'  -> 'Row Level Security'
    """
    # Strip hash anchors and query strings
    slug = slug.split("#")[0].split("?")[0]
    # Use last path segment
    slug = slug.rstrip("/").rsplit("/", 1)[-1]
    # Remove trailing random IDs.
    # Matches patterns like "-eWJo5Z" (camelCase) or "-a_Sg_e" (underscore-mixed).
    # Requires mixed case to avoid trimming real words like "embeddings".
    slug = re.sub(r"-[A-Z][A-Za-z0-9]{5,}$", "", slug)
    slug = re.sub(r"-[a-z][A-Z][A-Za-z0-9]{4,}$", "", slug)
    # Underscore-separated random ID suffix (e.g. "a_Sg_e")
    slug = re.sub(r"-[a-zA-Z0-9]+(?:_[a-zA-Z0-9]+){2,}$", "", slug)

    words = slug.replace("-", " ").replace("_", " ").split()
    result = []
    for i, word in enumerate(words):
        lower = word.lower()
        if lower in _ACRONYMS:
            result.append(lower.upper())
        elif i > 0 and lower in _LOWERCASE_WORDS:
            result.append(lower)
        else:
            result.append(word.capitalize())
    return " ".join(result) if result else slug


# ---------------------------------------------------------------------------
# HTTP helpers
# ---------------------------------------------------------------------------

_USER_AGENT = "AgentNav-Builder/1.0 (+https://agentnav.baekenough.com)"


def fetch_text(url: str) -> str:
    """Fetch URL content as text. Raises on HTTP error."""
    req = urllib.request.Request(url, headers={"User-Agent": _USER_AGENT})
    try:
        with urllib.request.urlopen(req, timeout=30) as resp:
            charset = "utf-8"
            ct = resp.headers.get_content_charset()
            if ct:
                charset = ct
            return resp.read().decode(charset, errors="replace")
    except urllib.error.HTTPError as exc:
        raise RuntimeError(f"HTTP {exc.code} fetching {url}") from exc
    except urllib.error.URLError as exc:
        raise RuntimeError(f"Network error fetching {url}: {exc.reason}") from exc


# ---------------------------------------------------------------------------
# llms.txt link-list parser
# ---------------------------------------------------------------------------

# Matches: "  - [Title](URL): Description" or "  - [Title](URL) - Description" at any indent level
_LINK_RE = re.compile(
    r"^(?P<indent>\s*)-\s+\[(?P<title>[^\]]+)\]\((?P<url>https?://[^)]+)\)"
    r"(?:(?::\s*|\s+-\s+)(?P<desc>.+))?$"
)

# Matches: "## Section Name" (H2 becomes a new section)
_H2_RE = re.compile(r"^##\s+(?P<name>.+)$")

# Matches: "# Title" or "> Description" at document root
_H1_RE = re.compile(r"^#\s+(?P<title>.+)$")
_BLOCKQUOTE_RE = re.compile(r"^>\s*(?P<desc>.+)$")

# Matches plain "- APIs & SDKs" style sub-headers without a URL
_PLAIN_ITEM_RE = re.compile(r"^(?P<indent>\s*)-\s+(?P<label>[A-Za-z].*)$")


def _indent_depth(indent_str: str) -> int:
    """Return nesting depth: 0 for no indent, 1 for 2-space, 2 for 4-space, etc."""
    return len(indent_str) // 2


class _Section:
    """Accumulator for one H2 section."""

    def __init__(self, name: str) -> None:
        self.name = name
        self.pages: list[dict] = []

    def add_page(self, url: str, title: str, description: str, site_url: str) -> None:
        parsed = urlparse(url)
        path = parsed.path or "/"
        page_type = classify_page_type(path, title)
        entry: dict = {"path": path, "title": title, "type": page_type}
        if description:
            entry["description"] = description
        self.pages.append(entry)


def parse_llms_links(text: str, site_url: str) -> tuple[str, str, list[_Section]]:
    """Parse a llms.txt link-list file.

    Returns:
        (site_name, site_description, sections)
    """
    lines = text.splitlines()
    site_name = ""
    site_description = ""
    sections: list[_Section] = []
    current: _Section | None = None

    # The first H1 after any top-level link is the site name.
    # Lines before the first ## are treated as a preamble section.
    preamble = _Section("Documentation")

    for line in lines:
        # H1 → site name (take first non-empty)
        m = _H1_RE.match(line)
        if m and not site_name:
            site_name = m.group("title").strip()
            continue

        # Blockquote → site description
        m = _BLOCKQUOTE_RE.match(line)
        if m and not site_description:
            site_description = m.group("desc").strip()
            continue

        # H2 → new section
        m = _H2_RE.match(line)
        if m:
            if current is None and preamble.pages:
                sections.append(preamble)
            elif current is not None:
                sections.append(current)
            current = _Section(m.group("name").strip())
            continue

        # Link line
        m = _LINK_RE.match(line)
        if m:
            url = m.group("url")
            title = m.group("title").strip()
            desc = (m.group("desc") or "").strip()
            target = current if current is not None else preamble
            target.add_page(url, title, desc, site_url)
            continue

    # Flush last section
    if current is not None:
        sections.append(current)
    elif preamble.pages:
        sections.append(preamble)

    return site_name, site_description, sections


# ---------------------------------------------------------------------------
# Sitemap XML parser
# ---------------------------------------------------------------------------

_SITEMAP_NS = "http://www.sitemaps.org/schemas/sitemap/0.9"


def parse_sitemap(xml_text: str, site_url: str, path_prefix: str = "") -> list[_Section]:
    """Parse a sitemap.xml and return sections grouped by the URL path segment
    immediately after *path_prefix*.

    Example: path_prefix='/docs/guides/' groups by the next segment
    (e.g. 'auth', 'database', ...).
    """
    root = ElementTree.fromstring(xml_text)
    urls: list[str] = []

    for url_el in root.iter(f"{{{_SITEMAP_NS}}}url"):
        loc_el = url_el.find(f"{{{_SITEMAP_NS}}}loc")
        if loc_el is not None and loc_el.text:
            loc = loc_el.text.strip()
            if not path_prefix or path_prefix in loc:
                urls.append(loc)

    # Derive the base path prefix from site_url if not provided
    parsed_site = urlparse(site_url)
    site_host = parsed_site.netloc

    # Group by the segment that follows path_prefix
    section_map: dict[str, _Section] = {}
    section_order: list[str] = []

    for url in sorted(urls):
        parsed = urlparse(url)
        full_path = parsed.path

        # Determine section key
        if path_prefix:
            remainder = full_path[len(path_prefix):]
        else:
            # Use the second path segment as section name
            parts = full_path.strip("/").split("/")
            remainder = "/".join(parts[1:]) if len(parts) > 1 else parts[0]

        section_key = remainder.split("/")[0] if remainder else "general"
        if not section_key:
            section_key = "general"

        if section_key not in section_map:
            section_map[section_key] = _Section(slug_to_title(section_key))
            section_order.append(section_key)

        title = slug_to_title(full_path)
        page_type = classify_page_type(full_path, title)
        entry: dict = {"path": full_path, "title": title, "type": page_type}
        section_map[section_key].pages.append(entry)

    return [section_map[k] for k in section_order]


# ---------------------------------------------------------------------------
# Index mode: llms.txt is a list of sub-file URLs
# ---------------------------------------------------------------------------

def parse_index_llms(text: str, site_url: str) -> tuple[str, str, list[_Section]]:
    """Parse an index llms.txt where each list item is a link to a sub-file.

    Each sub-file is fetched and treated as one section.
    Returns (site_name, site_description, sections).
    """
    site_name = ""
    site_description = ""
    sections: list[_Section] = []

    lines = text.splitlines()
    sub_urls: list[tuple[str, str]] = []  # (title, url)

    for line in lines:
        m = _H1_RE.match(line)
        if m and not site_name:
            site_name = m.group("title").strip()
            continue

        m = _BLOCKQUOTE_RE.match(line)
        if m and not site_description:
            site_description = m.group("desc").strip()
            continue

        m = _LINK_RE.match(line)
        if m:
            sub_urls.append((m.group("title").strip(), m.group("url")))

    for sub_title, sub_url in sub_urls:
        print(f"  Fetching sub-file: {sub_url}", file=sys.stderr)
        try:
            sub_text = fetch_text(sub_url)
        except RuntimeError as exc:
            print(f"  Warning: {exc}", file=sys.stderr)
            continue

        # Parse sub-file: for full-text (prose) sub-files, extract H2 as pages
        section = _Section(sub_title)
        sub_lines = sub_text.splitlines()
        seen_paths: set[str] = set()

        for sub_line in sub_lines:
            m = _LINK_RE.match(sub_line)
            if m:
                url = m.group("url")
                title = m.group("title").strip()
                desc = (m.group("desc") or "").strip()
                parsed = urlparse(url)
                path = parsed.path or "/"
                if path not in seen_paths:
                    seen_paths.add(path)
                    page_type = classify_page_type(path, title)
                    entry: dict = {"path": path, "title": title, "type": page_type}
                    if desc:
                        entry["description"] = desc
                    section.pages.append(entry)

        if section.pages:
            sections.append(section)

    return site_name, site_description, sections


# ---------------------------------------------------------------------------
# agents.json builder
# ---------------------------------------------------------------------------

def build_agents_json(
    *,
    site_name: str,
    site_url: str,
    site_description: str,
    sections: list[_Section],
    last_updated: str,
) -> dict:
    """Build an agents.json dict from parsed sections."""
    total_pages = sum(len(s.pages) for s in sections)
    out: dict = {
        "agents_txt_version": "0.2",
        "site": {
            "name": site_name,
            "url": site_url,
            "total_pages": total_pages,
            "last_updated": last_updated,
        },
        "sections": [],
    }
    if site_description:
        out["site"]["description"] = site_description

    for sec in sections:
        if not sec.pages:
            continue
        sec_entry: dict = {
            "name": sec.name,
            "page_count": len(sec.pages),
            "pages": sec.pages,
        }
        # Derive path_prefix from the common prefix of pages in this section
        paths = [p["path"] for p in sec.pages]
        if paths:
            prefix = _common_path_prefix(paths)
            if prefix and prefix != "/":
                sec_entry["path_prefix"] = prefix
        out["sections"].append(sec_entry)

    return out


def _common_path_prefix(paths: list[str]) -> str:
    """Return the longest common path prefix shared by all paths."""
    if not paths:
        return ""
    if len(paths) == 1:
        # Return parent directory of the single path
        parts = paths[0].rsplit("/", 1)
        return parts[0] + "/" if len(parts) > 1 else "/"

    # Split each path into segments and find common prefix
    split_paths = [p.split("/") for p in paths]
    common = split_paths[0]
    for other in split_paths[1:]:
        new_common = []
        for a, b in zip(common, other):
            if a == b:
                new_common.append(a)
            else:
                break
        common = new_common
        if not common:
            break

    prefix = "/".join(common)
    if not prefix.endswith("/"):
        prefix += "/"
    return prefix if prefix != "/" else ""


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------

def build_arg_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Convert llms.txt or sitemap.xml to agents.json.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=__doc__,
    )
    source = parser.add_mutually_exclusive_group(required=True)
    source.add_argument("--url", help="URL of llms.txt to fetch")
    source.add_argument(
        "--sitemap",
        metavar="URL",
        help="URL of sitemap.xml to fetch (use with --path-prefix)",
    )
    source.add_argument("--file", help="Local path to llms.txt file")

    parser.add_argument(
        "--output", "-o", required=True, help="Output path for agents.json"
    )
    parser.add_argument(
        "--site-url",
        required=True,
        help="Canonical URL of the documentation site (e.g. https://vercel.com)",
    )
    parser.add_argument("--site-name", help="Override detected site name")
    parser.add_argument("--site-description", help="Override detected description")
    parser.add_argument(
        "--index",
        action="store_true",
        help="Treat the llms.txt as an index of sub-file URLs",
    )
    parser.add_argument(
        "--path-prefix",
        default="",
        help="Filter sitemap URLs to this path prefix (e.g. /docs/guides/)",
    )
    parser.add_argument(
        "--last-updated",
        default=str(date.today()),
        help="last_updated field value (default: today)",
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Print stats without writing output file",
    )
    return parser


def main(argv: list[str] | None = None) -> int:
    parser = build_arg_parser()
    args = parser.parse_args(argv)

    # --- Fetch or load source ---
    if args.sitemap:
        print(f"Fetching sitemap: {args.sitemap}", file=sys.stderr)
        xml_text = fetch_text(args.sitemap)
        site_name = args.site_name or urlparse(args.site_url).netloc
        site_description = args.site_description or ""
        sections = parse_sitemap(xml_text, args.site_url, args.path_prefix)
    else:
        if args.url:
            print(f"Fetching: {args.url}", file=sys.stderr)
            text = fetch_text(args.url)
        else:
            print(f"Reading: {args.file}", file=sys.stderr)
            text = Path(args.file).read_text(encoding="utf-8")

        if args.index:
            print("Mode: index (fetching sub-files)", file=sys.stderr)
            site_name, site_description, sections = parse_index_llms(
                text, args.site_url
            )
        else:
            print("Mode: llms-links", file=sys.stderr)
            site_name, site_description, sections = parse_llms_links(
                text, args.site_url
            )

    # Apply overrides
    if args.site_name:
        site_name = args.site_name
    if args.site_description:
        site_description = args.site_description
    if not site_name:
        site_name = urlparse(args.site_url).netloc

    # --- Build output ---
    result = build_agents_json(
        site_name=site_name,
        site_url=args.site_url,
        site_description=site_description,
        sections=sections,
        last_updated=args.last_updated,
    )

    total = result["site"]["total_pages"]
    n_sections = len(result["sections"])
    print(
        f"Parsed: {total} pages across {n_sections} sections",
        file=sys.stderr,
    )

    if args.dry_run:
        print("Dry run — skipping write.", file=sys.stderr)
        return 0

    out_path = Path(args.output)
    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text(
        json.dumps(result, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )
    print(f"Written: {out_path}", file=sys.stderr)
    return 0


if __name__ == "__main__":
    sys.exit(main())
