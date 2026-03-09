#!/usr/bin/env python3
"""Convert agents.json to MD, XML, and TXT formats.

Usage:
    python scripts/generate_formats.py public/claude-code/agents.json
    python scripts/generate_formats.py --all
    python scripts/generate_formats.py --all --dry-run
"""

import argparse
import json
import sys
from collections import defaultdict
from pathlib import Path
from xml.etree import ElementTree as ET
from xml.dom import minidom


# ---------------------------------------------------------------------------
# Data helpers
# ---------------------------------------------------------------------------

def _dir_to_title(dirname: str) -> str:
    """Convert a hyphenated directory name to Title Case."""
    return dirname.replace("-", " ").replace("_", " ").title()


def _group_pages_by_subdir(pages: list[dict], path_prefix: str) -> dict[str, list[dict]]:
    """Group pages by their immediate subdirectory relative to path_prefix.

    Pages whose path does not add a subdirectory level beyond path_prefix are
    placed under the empty-string key (top-level group).

    Example:
        path_prefix = "/docs/en/about-claude"
        "/docs/en/about-claude/glossary"         -> "" (top-level)
        "/docs/en/about-claude/models/overview"  -> "models"
    """
    groups: dict[str, list[dict]] = defaultdict(list)
    prefix = path_prefix.rstrip("/")

    for page in pages:
        remainder = page["path"][len(prefix):].lstrip("/")
        parts = remainder.split("/")
        subdir = parts[0] if len(parts) > 1 else ""
        groups[subdir].append(page)

    return dict(groups)


# ---------------------------------------------------------------------------
# Markdown generator
# ---------------------------------------------------------------------------

def _md_page_types(data: dict) -> list[str]:
    """Collect all unique page types across sections and sdk_pattern."""
    types: set[str] = set()
    for section in data.get("sections", []):
        for page in section.get("pages", []):
            if "type" in page:
                types.add(page["type"])
        for sub in section.get("subsections", []):
            for page in sub.get("pages", []):
                if "type" in page:
                    types.add(page["type"])
    sdk = data.get("sdk_pattern", {})
    if sdk:
        types.add("api-hub")
        types.add(sdk.get("endpoint_types", {}).get("endpoint_pages_type", "api-endpoint"))
    return sorted(types)


def _md_section_row(idx: int, section: dict) -> str:
    prefix = section.get("path_prefix", "")
    if prefix and not prefix.endswith("/"):
        prefix += "/"
    return f"| {idx} | {section['name']} | {section['page_count']} | {prefix} |"


def _md_page_line(page: dict) -> str:
    page_type = page.get("type", "")
    method = page.get("method", "")
    type_tag = f"`{page_type}`" if page_type else ""
    method_tag = f" `{method}`" if method else ""
    return f"- [{page['title']}]({page['path']}){method_tag} {type_tag}".rstrip()


def _md_nav_section_selection(nav: dict) -> list[str]:
    lines: list[str] = []
    sel = nav.get("section_selection", {})
    if sel:
        lines.append("### Section Selection by Intent")
        lines.append("")
        for key, pattern in sel.items():
            intent = _dir_to_title(key.replace("_", " "))
            lines.append(f"- **{intent}**: `{pattern}`")
        lines.append("")
    return lines


def _md_nav_tips(nav: dict) -> list[str]:
    lines: list[str] = []
    tips = nav.get("tips", [])
    if tips:
        lines.append("### Tips")
        lines.append("")
        for tip in tips:
            lines.append(f"- {tip}")
        lines.append("")
    return lines


def _md_nav_url_rules(sdk_pattern: dict) -> list[str]:
    if not sdk_pattern:
        return []
    template = sdk_pattern.get("url_template", "")
    sdks = sdk_pattern.get("sdks", [])
    lines = [
        "### URL Construction Rules",
        "",
        f"- SDK endpoint template: `{template}`",
        f"- Available SDKs: {', '.join(f'`{s}`' for s in sdks)}",
        "",
    ]
    return lines


def _md_nav_shortcuts(data: dict) -> list[str]:
    """Generate Common Task Shortcuts from overview-type pages."""
    lines = ["### Common Task Shortcuts", ""]
    for section in data.get("sections", []):
        for page in section.get("pages", []):
            if page.get("type") == "overview":
                lines.append(f"- {page['title']}: [{page['path']}]({page['path']})")
        for sub in section.get("subsections", []):
            for page in sub.get("pages", []):
                if page.get("type") == "overview":
                    lines.append(
                        f"- {page['title']}: [{page['path']}]({page['path']})"
                    )
    lines.append("")
    return lines


def generate_md(data: dict) -> str:
    """Generate Markdown format from agents.json data."""
    version = data.get("agents_txt_version", "0.1")
    site = data.get("site", {})
    sections = data.get("sections", [])
    sdk_pattern = data.get("sdk_pattern")
    navigation = data.get("navigation", {})

    page_types = _md_page_types(data)
    type_list = ", ".join(page_types) if page_types else "—"

    lines: list[str] = [
        "---",
        f'agents_txt_version: "{version}"',
        "format: markdown",
        "schema:",
        '  sections: "## heading = section name"',
        '  subsections: "### heading = subsection grouping"',
        '  pages: "- [title](path) {type}"',
        f"  page_types: [{type_list}]",
    ]

    if sdk_pattern:
        lines.append(
            f'  sdk_pattern: "{sdk_pattern.get("url_template", "")}"'
        )

    if navigation:
        lines.append('  navigation: "See ## Navigation Guide section"')

    lines += [
        "---",
        "",
        f"# {site.get('name', 'Documentation')}",
        "",
        f"- **URL**: {site.get('url', '')}",
        f"- **Standard**: agents.txt v{version} (AgentNav PoC)",
        f"- **Total Pages**: {site.get('total_pages', 0)}",
        f"- **Last Updated**: {site.get('last_updated', '')}",
        "",
        "## Site Overview",
        "",
        "| # | Section | Pages | Base Path |",
        "|---|---------|-------|-----------|",
    ]

    for idx, section in enumerate(sections, 1):
        lines.append(_md_section_row(idx, section))

    lines.append("")
    lines.append("---")
    lines.append("")

    # Per-section content
    for section in sections:
        name = section["name"]
        page_count = section["page_count"]
        prefix = section.get("path_prefix", "")
        lines.append(f"## {name} ({page_count} pages)")
        lines.append("")

        # Sections that use subsections[] instead of pages[]
        subsections = section.get("subsections")
        pages = section.get("pages")

        if subsections:
            for sub in subsections:
                sub_pages = sub.get("pages")
                if not sub_pages:
                    # Description-only subsection (e.g. Per-SDK Endpoint Pages)
                    desc = sub.get("description", "")
                    lines.append(f"### {sub['name']} ({sub['page_count']} pages)")
                    lines.append("")
                    if desc:
                        lines.append(f"_{desc}_")
                        lines.append("")
                    continue
                lines.append(f"### {sub['name']}")
                lines.append("")
                for page in sub_pages:
                    lines.append(_md_page_line(page))
                lines.append("")

        elif pages:
            groups = _group_pages_by_subdir(pages, prefix)

            # Top-level pages first (no subdirectory)
            top_pages = groups.pop("", [])
            if top_pages:
                for page in top_pages:
                    lines.append(_md_page_line(page))
                if groups:
                    lines.append("")

            for subdir, subpages in sorted(groups.items()):
                lines.append(f"### {_dir_to_title(subdir)}")
                lines.append("")
                for page in subpages:
                    lines.append(_md_page_line(page))
                lines.append("")

            if not groups:
                lines.append("")

        else:
            desc = section.get("description", "")
            if desc:
                lines.append(f"_{desc}_")
                lines.append("")
            lines.append("")

    # Navigation Guide
    if navigation or sdk_pattern:
        lines.append("## Navigation Guide")
        lines.append("")
        lines.extend(_md_nav_section_selection(navigation))
        lines.extend(_md_nav_url_rules(sdk_pattern or {}))
        lines.extend(_md_nav_tips(navigation))
        lines.extend(_md_nav_shortcuts(data))

    return "\n".join(lines)


# ---------------------------------------------------------------------------
# XML generator
# ---------------------------------------------------------------------------

def _xml_prettify(element: ET.Element) -> str:
    """Return a pretty-printed XML string for the element."""
    raw = ET.tostring(element, encoding="unicode")
    reparsed = minidom.parseString(raw)
    return reparsed.toprettyxml(indent="  ", encoding=None)


def generate_xml(data: dict) -> str:
    """Generate XML format from agents.json data."""
    version = data.get("agents_txt_version", "0.1")
    site = data.get("site", {})
    sections = data.get("sections", [])
    sdk_pattern = data.get("sdk_pattern")
    navigation = data.get("navigation", {})

    root = ET.Element("agents", version=version)

    # <site>
    ET.SubElement(
        root,
        "site",
        name=site.get("name", ""),
        url=site.get("url", ""),
        attrib={
            "total-pages": str(site.get("total_pages", 0)),
            "last-updated": site.get("last_updated", ""),
        },
    )

    # <sections>
    secs_el = ET.SubElement(root, "sections")

    for idx, section in enumerate(sections, 1):
        comment = ET.Comment(f" {idx}. {section['name']} ")
        secs_el.append(comment)

        sec_el = ET.SubElement(
            secs_el,
            "section",
            name=section["name"],
            attrib={
                "path-prefix": section.get("path_prefix", ""),
                "page-count": str(section["page_count"]),
            },
        )

        subsections = section.get("subsections")
        pages = section.get("pages")

        if subsections:
            for sub in subsections:
                sub_el = ET.SubElement(
                    sec_el,
                    "subsection",
                    name=sub["name"],
                    attrib={"page-count": str(sub["page_count"])},
                )
                desc = sub.get("description")
                if desc:
                    sub_el.set("description", desc)
                for page in sub.get("pages", []):
                    attribs = {"path": page["path"], "title": page["title"]}
                    if "type" in page:
                        attribs["type"] = page["type"]
                    if "method" in page:
                        attribs["method"] = page["method"]
                    ET.SubElement(sub_el, "page", **attribs)

        elif pages:
            for page in pages:
                attribs = {"path": page["path"], "title": page["title"]}
                if "type" in page:
                    attribs["type"] = page["type"]
                if "method" in page:
                    attribs["method"] = page["method"]
                ET.SubElement(sec_el, "page", **attribs)

    # <sdk-pattern> (optional)
    if sdk_pattern:
        sdk_el = ET.SubElement(
            root,
            "sdk-pattern",
            template=sdk_pattern.get("url_template", ""),
            attrib={"total-pages": str(sdk_pattern.get("total_sdk_pages", 0))},
        )

        sdks_el = ET.SubElement(sdk_el, "sdks")
        for sdk_name in sdk_pattern.get("sdks", []):
            ET.SubElement(sdks_el, "sdk", name=sdk_name)

        endpoints_el = ET.SubElement(sdk_el, "endpoints")
        hub_pages = set(sdk_pattern.get("endpoint_types", {}).get("hub_pages", []))
        endpoint_type = sdk_pattern.get("endpoint_types", {}).get(
            "endpoint_pages_type", "api-endpoint"
        )
        for ep_path in sdk_pattern.get("endpoint_paths", []):
            ep_type = "api-hub" if ep_path in hub_pages else endpoint_type
            ET.SubElement(endpoints_el, "endpoint", path=ep_path, type=ep_type)

    # <navigation> (optional)
    sel = navigation.get("section_selection", {})
    tips = navigation.get("tips", [])
    if sel or tips:
        nav_el = ET.SubElement(root, "navigation")
        for key, pattern in sel.items():
            ET.SubElement(nav_el, "rule", key=key, pattern=pattern)
        for tip in tips:
            tip_el = ET.SubElement(nav_el, "tip")
            tip_el.text = tip

    pretty = _xml_prettify(root)
    # minidom adds its own xml declaration; keep it
    return pretty


# ---------------------------------------------------------------------------
# TXT generator
# ---------------------------------------------------------------------------

_TXT_SCHEMA = """\
== SCHEMA ==
# Each section lists pages as:
#   {relative_path} | type={type}
# SDK template (if present):
#   TEMPLATE sdk={sdk1,sdk2,...}
#     {endpoint_path} | type={type}
# Navigation tips follow in == NAVIGATION ==
"""


def _txt_relative_path(page_path: str, path_prefix: str) -> str:
    prefix = path_prefix.rstrip("/")
    if page_path.startswith(prefix):
        return page_path[len(prefix):].lstrip("/") or "/"
    return page_path


def generate_txt(data: dict) -> str:
    """Generate plain-text format from agents.json data."""
    version = data.get("agents_txt_version", "0.1")
    site = data.get("site", {})
    sections = data.get("sections", [])
    sdk_pattern = data.get("sdk_pattern")
    navigation = data.get("navigation", {})

    lines: list[str] = [
        f"# agents.txt v{version}",
        f"# {site.get('name', '')} — {site.get('url', '')}",
        f"# Total: {site.get('total_pages', 0)} pages"
        f" | Last updated: {site.get('last_updated', '')}",
        "",
        f"SITE: {site.get('name', '')}",
        f"URL: {site.get('url', '')}",
        f"PAGES: {site.get('total_pages', 0)}",
        f"SECTIONS: {len(sections)}",
        "",
        _TXT_SCHEMA,
        "== SECTIONS ==",
        "",
    ]

    sdk_endpoint_paths = set()
    sdk_template = ""
    hub_pages: set[str] = set()
    endpoint_pages_type = "api-endpoint"

    if sdk_pattern:
        sdk_endpoint_paths = set(sdk_pattern.get("endpoint_paths", []))
        sdk_template = sdk_pattern.get("url_template", "")
        hub_pages = set(
            sdk_pattern.get("endpoint_types", {}).get("hub_pages", [])
        )
        endpoint_pages_type = sdk_pattern.get("endpoint_types", {}).get(
            "endpoint_pages_type", "api-endpoint"
        )

    for section in sections:
        prefix = section.get("path_prefix", "")
        lines.append(
            f"[{section['name']}] {section['page_count']} pages"
            f" | prefix={prefix}/"
        )

        subsections = section.get("subsections")
        pages = section.get("pages")

        if subsections:
            for sub in subsections:
                sub_pages = sub.get("pages")
                if not sub_pages:
                    desc = sub.get("description", "")
                    note = f"  # {desc}" if desc else ""
                    lines.append(
                        f"  [{sub['name']}] {sub['page_count']} pages{note}"
                    )
                    # Inject TEMPLATE block for SDK subsection
                    if sdk_pattern and "SDK" in sub["name"]:
                        sdk_names = ",".join(sdk_pattern.get("sdks", []))
                        lines.append(f"  TEMPLATE sdk={sdk_names}")
                        for ep in sdk_pattern.get("endpoint_paths", []):
                            ep_type = "api-hub" if ep in hub_pages else endpoint_pages_type
                            lines.append(f"    {ep} | type={ep_type}")
                    continue

                lines.append(f"  [{sub['name']}]")
                for page in sub_pages:
                    rel = _txt_relative_path(page["path"], prefix + "/" + sub["name"].lower())
                    page_type = page.get("type", "")
                    method = page.get("method", "")
                    method_tag = f" | method={method}" if method else ""
                    lines.append(f"    {page['path']} | type={page_type}{method_tag}")

        elif pages:
            for page in pages:
                rel = _txt_relative_path(page["path"], prefix)
                page_type = page.get("type", "")
                method = page.get("method", "")
                method_tag = f" | method={method}" if method else ""
                lines.append(f"  {rel} | type={page_type}{method_tag}")

        lines.append("")

    # Navigation
    sel = navigation.get("section_selection", {})
    tips = navigation.get("tips", [])
    default_section = navigation.get("default_section", "")
    search_priority = navigation.get("search_priority", [])

    if sel or tips or default_section:
        lines.append("== NAVIGATION ==")
        lines.append("")

        if default_section:
            lines.append(f"DEFAULT: {default_section}")
            lines.append("")

        if search_priority:
            lines.append(
                "SEARCH PRIORITY: " + " > ".join(f'"{s}"' for s in search_priority)
            )
            lines.append("")

        if sel:
            lines.append("RULES:")
            for idx, (key, pattern) in enumerate(sel.items(), 1):
                intent = _dir_to_title(key.replace("_", " "))
                lines.append(f"  {idx}. {intent} → {pattern}")
            lines.append("")

        if tips:
            lines.append("TIPS:")
            for tip in tips:
                lines.append(f"  - {tip}")
            lines.append("")

        if sel:
            lines.append("INTENT MAP:")
            for key, pattern in sel.items():
                intent = _dir_to_title(key.replace("_", " "))
                lines.append(f"  {intent} → {pattern}")
            lines.append("")

    return "\n".join(lines)


# ---------------------------------------------------------------------------
# File I/O
# ---------------------------------------------------------------------------

def convert_file(
    json_path: Path, dry_run: bool = False
) -> list[tuple[Path, int]]:
    """Convert a single agents.json to MD, XML, and TXT.

    Returns a list of (output_path, line_count) tuples.
    """
    with json_path.open(encoding="utf-8") as fh:
        data = json.load(fh)

    outputs: list[tuple[str, str]] = [
        ("md", generate_md(data)),
        ("xml", generate_xml(data)),
        ("txt", generate_txt(data)),
    ]

    results: list[tuple[Path, int]] = []

    for ext, content in outputs:
        out_path = json_path.with_suffix(f".{ext}")
        line_count = content.count("\n") + 1
        if not dry_run:
            out_path.write_text(content, encoding="utf-8")
        results.append((out_path, line_count))

    return results


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------

def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Convert agents.json to MD, XML, and TXT formats.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=__doc__,
    )
    parser.add_argument(
        "input",
        nargs="?",
        metavar="agents.json",
        help="Path to a single agents.json file",
    )
    parser.add_argument(
        "--all",
        action="store_true",
        dest="all_files",
        help="Process all public/*/agents.json files",
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Print output file paths without writing",
    )
    return parser


def main() -> None:
    parser = build_parser()
    args = parser.parse_args()

    if not args.input and not args.all_files:
        parser.print_help()
        sys.exit(1)

    project_root = Path(__file__).resolve().parent.parent

    json_paths: list[Path] = []
    if args.all_files:
        json_paths = sorted(project_root.glob("public/*/agents.json"))
        if not json_paths:
            print("No public/*/agents.json files found.", file=sys.stderr)
            sys.exit(1)
    else:
        json_paths = [Path(args.input).resolve()]

    for json_path in json_paths:
        if not json_path.exists():
            print(f"[Error] Not found: {json_path}", file=sys.stderr)
            continue

        print(f"\n[Converting] {json_path.relative_to(project_root)}")
        try:
            results = convert_file(json_path, dry_run=args.dry_run)
        except (json.JSONDecodeError, KeyError, TypeError) as exc:
            print(f"  [Error] {exc}", file=sys.stderr)
            continue

        for out_path, line_count in results:
            action = "(dry-run)" if args.dry_run else "written"
            rel = out_path.relative_to(project_root)
            print(f"  -> {rel}  [{line_count} lines] {action}")


if __name__ == "__main__":
    main()
