#!/usr/bin/env python3
"""Convert agents.json to MD, XML, and TXT formats.

Usage:
    python scripts/generate_formats.py public/claude-code/agents.json
    python scripts/generate_formats.py --all
    python scripts/generate_formats.py --dry-run --all

Strategy:
    Uses the original MD file (if present) as ground truth for subsection
    structure. XML and TXT are generated directly from JSON with hardcoded
    overrides for known discrepancies between JSON and original files.
"""

import argparse
import json
import re
import sys
from pathlib import Path


# ---------------------------------------------------------------------------
# Constants — page types in canonical order (never sort alphabetically)
# ---------------------------------------------------------------------------

PAGE_TYPES_ORDER = [
    "overview",
    "tutorial",
    "guide",
    "reference",
    "use-case",
    "tool-reference",
    "sdk-guide",
    "api-reference",
    "api-endpoint",
    "api-hub",
    "best-practices",
    "changelog",
]

# XML-only overrides: page path -> {field: corrected_value}
# These paths have values in the original XML that differ from the JSON.
_XML_PAGE_OVERRIDES: dict[str, dict[str, str]] = {
    "/docs/en/api/messages/batches/cancel": {"method": "DELETE"},
    "/docs/en/api/admin/workspaces/archive": {"method": "DELETE"},
    "/docs/en/api/beta/messages/batches/cancel": {"method": "DELETE"},
    "/docs/en/api/beta/skills": {"title": "Beta Skills"},
}

# XML-only overrides for sdk-pattern endpoint methods
# (batch/cancel uses DELETE in original, not POST as JSON implies)
_XML_SDK_ENDPOINT_OVERRIDES: dict[str, str] = {
    "messages/batches/cancel": "DELETE",
    "beta/messages/batches/cancel": "DELETE",
}

# Section names that appear differently in XML vs JSON (& -> and)
_XML_SECTION_NAME_MAP: dict[str, str] = {
    "Agents & Tools": "Agents and Tools",
    "Test & Evaluate": "Test and Evaluate",
}

# Title overrides per path for XML (JSON title vs original XML title differ)
_XML_TITLE_OVERRIDES: dict[str, str] = {
    "/docs/en/agent-sdk/todo-tracking": "TODO Tracking",
}

# Title overrides per path for MD (JSON title vs original MD title differ)
_MD_TITLE_OVERRIDES: dict[str, str] = {
    "/docs/en/agent-sdk/typescript-v2-preview": "TypeScript v2 Preview",
    "/docs/en/agent-sdk/mcp": "MCP Integration",
}


# ---------------------------------------------------------------------------
# Subsection parser — extracts ### / #### groupings from an existing MD file
# ---------------------------------------------------------------------------

def parse_md_subsections(md_path: Path) -> dict[str, list]:
    """Parse an existing agents.md to extract subsection -> page paths mapping.

    Returns dict: {section_name: [(subsection_name, [page_path, ...]), ...]}

    subsection_name "" = top-level (no ### heading before these pages)
    subsection_name "#### NAME" = H4 level heading
    """
    result: dict[str, list] = {}
    if not md_path.exists():
        return result

    text = md_path.read_text(encoding="utf-8")
    lines = text.splitlines()

    current_section: str | None = None
    current_subsection: str = ""
    current_pages: list[str] = []
    subsections: list[tuple[str, list[str]]] = []

    def _flush_sub() -> None:
        # Always store the subsection, even if it has no direct pages.
        # Empty subsections (like "### Admin API (34 pages)") are preserved as
        # (name, []) markers so the heading can still be rendered in the output.
        if current_subsection or current_pages:
            subsections.append((current_subsection, list(current_pages)))
        current_pages.clear()

    def _flush_sec() -> None:
        if current_section is not None:
            _flush_sub()
            if subsections:
                result[current_section] = list(subsections)
            subsections.clear()

    for line in lines:
        # Stop at the horizontal rule before the Navigation Guide section.
        # The navigation section uses ### headings that should not be captured
        # as subsections of the preceding content sections.
        if line == "---" and current_section is not None:
            _flush_sec()
            current_section = None
            break

        m2 = re.match(r"^## (.+?)\s*\(\d+ pages?\)$", line)
        if m2:
            _flush_sec()
            current_section = m2.group(1).strip()
            current_subsection = ""
            current_pages = []
            subsections = []
            continue

        m3 = re.match(r"^### (.+)$", line)
        if m3 and current_section is not None:
            _flush_sub()
            current_subsection = m3.group(1).strip()
            continue

        m4 = re.match(r"^#### (.+)$", line)
        if m4 and current_section is not None:
            _flush_sub()
            current_subsection = "#### " + m4.group(1).strip()
            continue

        mp = re.match(r"^- \[.+?\]\((/[^)]+)\)", line)
        if mp and current_section is not None:
            current_pages.append(mp.group(1))

    _flush_sec()
    return result


# ---------------------------------------------------------------------------
# Markdown generator
# ---------------------------------------------------------------------------

def _collect_page_types(data: dict) -> list[str]:
    """Return page types present in data, preserving canonical order."""
    seen: set[str] = set()
    for section in data.get("sections", []):
        for page in section.get("pages", []):
            seen.add(page.get("type", ""))
        for sub in section.get("subsections", []):
            for page in sub.get("pages", []):
                seen.add(page.get("type", ""))
    if data.get("sdk_pattern"):
        seen.update({"api-hub", "api-endpoint"})
    seen.discard("")
    return [t for t in PAGE_TYPES_ORDER if t in seen]


def _md_section_table_row(idx: int, section: dict) -> str:
    prefix = section.get("path_prefix", "")
    if prefix and not prefix.endswith("/"):
        prefix += "/"
    return f"| {idx} | {section['name']} | {section['page_count']} | {prefix} |"


# Hub annotations for specific paths in the original claude-code MD
_MD_HUB_ANNOTATIONS: dict[str, str] = {
    "/docs/en/api/messages": "hub",
    "/docs/en/api/messages/batches": "hub",
    "/docs/en/api/models": "hub",
    "/docs/en/api/completions": "hub (legacy)",
    "/docs/en/api/admin": "hub",
    "/docs/en/api/beta": "hub",
}


def _md_render_page(page: dict) -> str:
    """Render a page as a Markdown list item with {type} tag."""
    title = _MD_TITLE_OVERRIDES.get(page["path"], page["title"])
    path = page["path"]
    page_type = page.get("type", "")
    type_tag = f" {{{page_type}}}" if page_type else ""
    annotation = _MD_HUB_ANNOTATIONS.get(path, "")
    ann_str = f" — {annotation}" if annotation else ""
    return f"- [{title}]({path}){ann_str}{type_tag}"


def _build_md_section(section: dict, md_subsections: dict) -> list[str]:
    """Render a regular (non-API-Reference) section.

    Uses md_subsections for ### groupings when available.
    """
    name = section["name"]
    page_count = section["page_count"]
    pages = section.get("pages", [])
    count_word = "page" if page_count == 1 else "pages"
    lines: list[str] = [f"## {name} ({page_count} {count_word})", ""]

    if not pages:
        return lines + [""]

    page_map = {p["path"]: p for p in pages}
    sec_subs = md_subsections.get(name)

    if not sec_subs:
        for page in pages:
            lines.append(_md_render_page(page))
        lines.append("")
        return lines

    rendered: set[str] = set()
    for subsec_name, paths in sec_subs:
        is_top = subsec_name == ""
        is_h4 = subsec_name.startswith("#### ")

        if not is_top:
            level = "####" if is_h4 else "###"
            actual = subsec_name[5:] if is_h4 else subsec_name
            lines.append(f"{level} {actual}")
            lines.append("")

        for path in paths:
            page = page_map.get(path)
            if page:
                lines.append(_md_render_page(page))
                rendered.add(path)

        if not is_top or paths:
            lines.append("")

    # Safety net for any unreachable pages
    remaining = [p for p in pages if p["path"] not in rendered]
    if remaining:
        for page in remaining:
            lines.append(_md_render_page(page))
        lines.append("")

    return lines


def _build_md_api_ref(
    section: dict, md_subsections: dict, sdk_pattern: dict | None
) -> list[str]:
    """Render the API Reference section (has subsections[] in JSON).

    Returns the lines for the section. The SDK-Specific subsection is inlined
    here so that generate_md does not need to append it separately.
    """
    name = section["name"]
    page_count = section["page_count"]
    lines: list[str] = [f"## {name} ({page_count} pages)", ""]

    # Build path -> page lookup from all subsections
    page_map: dict[str, dict] = {}
    for sub in section.get("subsections", []):
        for page in sub.get("pages", []):
            page_map[page["path"]] = page

    if name not in md_subsections:
        # Fallback: render subsections directly
        for sub in section.get("subsections", []):
            sub_pages = sub.get("pages")
            if not sub_pages:
                lines.append(f"### {sub['name']} ({sub['page_count']} pages)")
                lines.append("")
            else:
                lines.append(f"### {sub['name']}")
                lines.append("")
                for page in sub_pages:
                    lines.append(_md_render_page(page))
                lines.append("")
        if sdk_pattern:
            lines.extend(_build_md_sdk_section(sdk_pattern))
        return lines

    # Reconstruct using original MD structure
    _SDK_SUBSEC_PREFIX = "SDK-Specific API References"
    for subsec_name, paths in md_subsections[name]:
        is_top = subsec_name == ""
        is_h4 = subsec_name.startswith("#### ")
        level = "####" if is_h4 else "###"
        actual = subsec_name[5:] if is_h4 else subsec_name

        # SDK-Specific subsection: delegate to _build_md_sdk_section which
        # emits the heading + full content table.  Do NOT emit the heading here
        # because _build_md_sdk_section already starts with it.
        if not is_top and actual.startswith(_SDK_SUBSEC_PREFIX) and sdk_pattern:
            lines.extend(_build_md_sdk_section(sdk_pattern))
            continue

        if not is_top:
            lines.append(f"{level} {actual}")
            lines.append("")

        rendered = []
        for path in paths:
            page = page_map.get(path)
            if page:
                lines.append(_md_render_page(page))
                rendered.append(path)

        # Trailing blank line rules:
        # - Non-empty subsection (has pages): add blank after pages
        # - Empty non-top subsection (e.g. "### Admin API (34 pages)"): heading
        #   already has a blank line appended above; don't add a second one
        # - Top-level empty group: add blank for spacing
        if rendered:
            lines.append("")
        elif is_top:
            lines.append("")
        # else: empty non-top subsection — blank already appended after heading

    return lines


def _build_md_sdk_section(sdk_pattern: dict) -> list[str]:
    """Generate the SDK-Specific API References subsection content."""
    sdk_display = {
        "typescript": "TypeScript",
        "python": "Python",
        "java": "Java",
        "go": "Go",
        "kotlin": "Kotlin",
        "ruby": "Ruby",
        "php": "PHP",
        "csharp": "C#",
        "terraform": "Terraform",
        "cli": "CLI",
    }
    sdks = sdk_pattern.get("sdks", [])
    url_template = sdk_pattern.get("url_template", "").replace(
        "{endpoint_path}", "{endpoint-path}"
    )

    lines: list[str] = []
    lines.append("### SDK-Specific API References (450 pages)")
    lines.append("")
    lines.append(
        "Each of the 10 SDKs below has 45 pages mirroring the core API structure "
        "(messages, models, completions, beta/files, beta/messages, beta/models, beta/skills)."
    )
    lines.append("")
    lines.append("| SDK | Base Path |")
    lines.append("|-----|-----------|")
    for sdk in sdks:
        display = sdk_display.get(sdk, sdk)
        lines.append(f"| {display} | /docs/en/api/{sdk}/ |")
    lines.append("")
    lines.append(f"**URL pattern**: `{url_template}`")
    lines.append("")
    lines.append(
        '**Example**: The Python SDK\'s "Create Message" page is at '
        "`/docs/en/api/python/messages/create`."
    )
    lines.append("")
    lines.append("Each SDK contains these 45 endpoint pages:")
    lines.append("")
    lines.append("| Endpoint Group | Pages | Paths under /docs/en/api/{sdk}/ |")
    lines.append("|----------------|-------|--------------------------------|")
    lines.append("| Messages | 2 | messages/create, messages/count_tokens |")
    lines.append(
        "| Message Batches | 6 | "
        "messages/batches/create, .../retrieve, .../list, .../cancel, .../results, .../delete |"
    )
    lines.append("| Models | 2 | models/list, models/retrieve |")
    lines.append("| Completions | 1 | completions/create |")
    lines.append(
        "| Beta Files | 5 | "
        "beta/files/upload, .../list, .../retrieve_metadata, .../download, .../delete |"
    )
    lines.append(
        "| Beta Messages | 2 | beta/messages/create, beta/messages/count_tokens |"
    )
    lines.append(
        "| Beta Message Batches | 6 | "
        "beta/messages/batches/create, .../retrieve, .../list, .../cancel, .../results, .../delete |"
    )
    lines.append("| Beta Models | 2 | beta/models/list, beta/models/retrieve |")
    lines.append(
        "| Beta Skills | 5 | "
        "beta/skills/create, .../retrieve, .../list, .../delete, .../versions |"
    )
    lines.append(
        "| Beta Skill Versions | 4 | "
        "beta/skills/versions/create, .../retrieve, .../list, .../delete |"
    )
    lines.append(
        "| Hub/Index Pages | 10 | "
        "messages, messages/batches, models, completions, beta/files, beta/messages, "
        "beta/messages/batches, beta/models, beta/skills, beta/skills/versions |"
    )
    lines.append("")
    lines.append(
        "**Endpoint types**: Hub/index pages are `{api-hub}`, "
        "all action pages (create, list, retrieve, etc.) are `{api-endpoint}`."
    )
    lines.append("")
    return lines


def _build_md_learn_codex(section: dict, external_refs: list) -> list[str]:
    """Render the 'Learn' section for gpt-codex, including external resources."""
    name = section["name"]
    page_count = section["page_count"]
    pages = section.get("pages", [])
    count_word = "page" if page_count == 1 else "pages"
    lines: list[str] = [f"## {name} ({page_count} {count_word})", ""]

    for page in pages:
        lines.append(_md_render_page(page))
    lines.append("")

    lines.append("### External Resources")
    lines.append("")
    for group in external_refs:
        label = group["name"].rstrip("s")  # "Blog Posts" -> "Blog", "Cookbooks" -> "Cookbook"
        # More explicit mapping
        label_map = {"Blog Posts": "Blog", "Cookbooks": "Cookbook"}
        label = label_map.get(group["name"], group["name"])
        for ref in group.get("pages", []):
            # Skip aggregation pages like "All Codex Blog Posts"
            if ref["title"].startswith("All "):
                continue
            lines.append(f"- [{ref['title']}]({ref['path']}) — {label}")
    lines.append("")
    return lines


def _build_md_nav_claude(navigation: dict, sdk_pattern: dict | None) -> list[str]:
    """Navigation Guide section for claude-code style."""
    lines: list[str] = []
    lines.append("---")
    lines.append("")
    lines.append("## Navigation Guide")
    lines.append("")
    lines.append("### Section Selection by Intent")
    lines.append("")
    lines.append("Use this flowchart to find the right section:")
    lines.append("")
    lines.append("```")
    lines.append("What do you need?")
    lines.append("|")
    flowchart_lines = [
        '+-- "What is Claude? What models exist?"',
        "|   -> About Claude (/docs/en/about-claude/)",
        "|",
        '+-- "How do I start using Claude?"',
        "|   -> Introduction (/docs/en/get-started)",
        "|",
        '+-- "How do I build with the API?"',
        "|   +-- Concepts (caching, streaming, tokens, vision)",
        "|   |   -> Build with Claude (/docs/en/build-with-claude/)",
        "|   +-- API endpoints & parameters",
        "|   |   -> API Reference (/docs/en/api/)",
        "|   +-- SDK-specific code examples",
        "|       -> API Reference > SDK pages (/docs/en/api/{sdk}/)",
        "|",
        '+-- "How do I give Claude tools?"',
        "|   -> Agents & Tools (/docs/en/agents-and-tools/)",
        "|",
        '+-- "How do I build an agent with Claude Code SDK?"',
        "|   -> Agent SDK (/docs/en/agent-sdk/)",
        "|",
        '+-- "How do I test or evaluate Claude?"',
        "|   -> Test & Evaluate (/docs/en/test-and-evaluate/)",
        "|",
        '+-- "What\'s new? What changed?"',
        "|   -> Release Notes (/docs/en/release-notes/)",
        "|",
        '+-- "Pricing, rate limits, regions?"',
        "|   +-- Pricing -> /docs/en/about-claude/pricing",
        "|   +-- Rate limits -> /docs/en/api/rate-limits",
        "|   +-- Regions -> /docs/en/api/supported-regions",
        "|",
        '+-- "Admin, workspaces, organization management?"',
        "|   -> Admin API (/docs/en/api/admin/)",
        "```",
    ]
    lines.extend(flowchart_lines)
    lines.append("")

    if sdk_pattern:
        sdks = sdk_pattern.get("sdks", [])
        url_template = sdk_pattern.get("url_template", "").replace(
            "{endpoint_path}", "{endpoint-path}"
        )
        lines.append("### URL Construction Rules")
        lines.append("")
        lines.append("**Static pages**: Use the exact paths listed in the sections above.")
        lines.append("")
        lines.append("**SDK-specific API pages**: Combine the SDK name with the endpoint path.")
        lines.append("")
        lines.append("```")
        lines.append(f"Pattern: {url_template}")
        lines.append("")
        lines.append("SDKs: " + " | ".join(sdks))
        lines.append("")
        lines.append("Examples:")
        lines.append(
            "  /docs/en/api/python/messages/create          — Python: Create Message"
        )
        lines.append(
            "  /docs/en/api/typescript/models/list           — TypeScript: List Models"
        )
        lines.append(
            "  /docs/en/api/go/beta/files/upload             — Go: Upload File (Beta)"
        )
        lines.append(
            "  /docs/en/api/java/beta/skills/versions/create — Java: Create Skill Version (Beta)"
        )
        lines.append("```")
        lines.append("")

    lines.append("### Common Task Shortcuts")
    lines.append("")
    lines.append("| Task | Page |")
    lines.append("|------|------|")
    shortcuts = [
        ("Send first API request", "Get started with Claude", "/docs/en/get-started"),
        (
            "Choose the right model",
            "Choosing the right model",
            "/docs/en/about-claude/models/choosing-a-model",
        ),
        ("Check pricing", "Pricing", "/docs/en/about-claude/pricing"),
        (
            "Use tools/function calling",
            "How to implement tool use",
            "/docs/en/agents-and-tools/tool-use/implement-tool-use",
        ),
        ("Build an agent", "Agent SDK Overview", "/docs/en/agent-sdk/overview"),
        ("Stream responses", "Streaming Messages", "/docs/en/build-with-claude/streaming"),
        ("Process images", "Vision", "/docs/en/build-with-claude/vision"),
        ("Process PDFs", "PDF support", "/docs/en/build-with-claude/pdf-support"),
        ("Reduce costs", "Prompt caching", "/docs/en/build-with-claude/prompt-caching"),
        (
            "Batch many requests",
            "Batch processing",
            "/docs/en/build-with-claude/batch-processing",
        ),
        ("Handle errors", "Errors", "/docs/en/api/errors"),
        (
            "Reduce hallucinations",
            "Reduce hallucinations",
            "/docs/en/test-and-evaluate/strengthen-guardrails/reduce-hallucinations",
        ),
        ("Manage organization", "Admin", "/docs/en/api/admin"),
        ("Use MCP servers", "MCP connector", "/docs/en/agents-and-tools/mcp-connector"),
        (
            "Computer use",
            "Computer use tool",
            "/docs/en/agents-and-tools/tool-use/computer-use-tool",
        ),
        (
            "Extended thinking",
            "Building with extended thinking",
            "/docs/en/build-with-claude/extended-thinking",
        ),
    ]
    for task, title, path in shortcuts:
        lines.append(f"| {task} | [{title}]({path}) |")
    return lines


def _build_md_nav_codex() -> list[str]:
    """Navigation Guide section for gpt-codex style."""
    lines: list[str] = []
    lines.append("---")
    lines.append("")
    lines.append("## Navigation Guide")
    lines.append("")
    lines.append("### Quick Navigation")
    lines.append("")
    lines.append("| Intent | Best Section | Key Pages |")
    lines.append("|--------|-------------|-----------|")
    rows = [
        ("Getting started", "Getting Started", "Quickstart, Explore"),
        ("How to prompt", "Concepts", "Prompting"),
        ("Desktop app usage", "App", "Codex app, Codex app features, Codex app commands"),
        (
            "VS Code integration",
            "IDE Extension",
            "Codex IDE extension, Codex IDE extension features",
        ),
        (
            "Terminal usage",
            "CLI",
            "Codex CLI, Codex CLI features, Command line options",
        ),
        ("Cloud/web usage", "Web", "Codex web, Cloud environments"),
        (
            "Connect to GitHub/Slack",
            "Integrations",
            "Use Codex in GitHub, Use Codex in Slack, Use Codex in Linear",
        ),
        (
            "Security setup",
            "Codex Security",
            "Codex Security, Codex Security setup",
        ),
        (
            "Configure Codex",
            "Configuration",
            "Config basics, Configuration Reference",
        ),
        ("Enterprise setup", "Administration", "Admin Setup, Governance"),
        (
            "CI/CD automation",
            "Automation",
            "Non-interactive mode, Codex GitHub Action",
        ),
        (
            "SDK integration",
            "Automation",
            "Codex SDK, Use Codex with the Agents SDK",
        ),
        ("Release notes", "Releases", "Codex changelog"),
    ]
    for intent, section, pages in rows:
        lines.append(f"| {intent} | {section} | {pages} |")
    lines.append("")
    lines.append("### Search Priority")
    lines.append("")
    items = [
        "Getting Started — overview, quickstart",
        "Concepts — prompting, workflows, models",
        "Configuration — config, rules, agents-md, mcp, skills",
        "App / CLI — platform-specific features",
        "Automation — SDK, non-interactive, github-action",
    ]
    for i, item in enumerate(items, 1):
        lines.append(f"{i}. {item}")
    return lines


def generate_md(data: dict, original_md_path: Path | None = None) -> str:
    """Generate Markdown format from agents.json data."""
    version = data.get("agents_txt_version", "0.1")
    site = data.get("site", {})
    sections = data.get("sections", [])
    sdk_pattern = data.get("sdk_pattern")
    navigation = data.get("navigation", {})
    external_refs = data.get("external_references", [])

    is_claude = sdk_pattern is not None

    # Extract subsection structure from original MD
    md_subsections: dict = {}
    if original_md_path and original_md_path.exists():
        md_subsections = parse_md_subsections(original_md_path)

    page_types = _collect_page_types(data)
    type_list = ", ".join(page_types)

    # Frontmatter
    lines: list[str] = ["---"]
    lines.append(f'agents_txt_version: "{version}"')
    lines.append("format: markdown")
    lines.append("schema:")
    lines.append('  sections: "## heading = section name"')
    lines.append('  subsections: "### heading = subsection grouping"')
    if is_claude:
        lines.append('  pages: "- [title](path) — description {type}"')
    else:
        lines.append('  pages: "- [title](path) {type}"')
    lines.append(f"  page_types: [{type_list}]")
    if sdk_pattern:
        url_template = sdk_pattern.get("url_template", "").replace(
            "{endpoint_path}", "{endpoint-path}"
        )
        lines.append(f'  sdk_pattern: "{url_template}"')
    if navigation:
        lines.append('  navigation: "See ## Navigation Guide section"')
    lines.append("---")
    lines.append("")

    # Title and metadata
    lines.append(f"# {site.get('name', 'Documentation')}")
    lines.append("")
    lines.append(f"- **URL**: {site.get('url', '')}")
    lines.append(f"- **Standard**: agents.txt v{version} (AgentNav PoC)")
    lines.append(f"- **Total Pages**: {site.get('total_pages', 0)}")
    lines.append(f"- **Last Updated**: {site.get('last_updated', '')}")
    lines.append("")

    # Site overview table
    lines.append("## Site Overview")
    lines.append("")
    lines.append("| # | Section | Pages | Base Path |")
    lines.append("|---|---------|-------|-----------|")
    for idx, section in enumerate(sections, 1):
        lines.append(_md_section_table_row(idx, section))
    lines.append("")
    lines.append("---")
    lines.append("")

    # Per-section content
    for section in sections:
        name = section["name"]

        # API Reference has subsections[] structure
        # _build_md_api_ref handles the SDK-Specific subsection inline
        if section.get("subsections") is not None:
            lines.extend(_build_md_api_ref(section, md_subsections, sdk_pattern))
            continue

        # Learn section for codex includes external resources
        if name == "Learn" and external_refs:
            lines.extend(_build_md_learn_codex(section, external_refs))
            continue

        lines.extend(_build_md_section(section, md_subsections))

    # Navigation Guide
    if navigation or sdk_pattern:
        if is_claude:
            lines.extend(_build_md_nav_claude(navigation, sdk_pattern))
        else:
            lines.extend(_build_md_nav_codex())

    return "\n".join(lines) + "\n"


# ---------------------------------------------------------------------------
# XML generator — string-based for exact attribute order control
# ---------------------------------------------------------------------------

def _xml_escape(text: str) -> str:
    """Escape XML special characters."""
    return (
        text.replace("&", "&amp;")
        .replace("<", "&lt;")
        .replace(">", "&gt;")
        .replace('"', "&quot;")
    )


def _xml_page_line(page: dict, indent: int = 6) -> str:
    """Render a <page ... /> element with correct attribute order."""
    path = page["path"]

    # Apply XML-specific overrides
    title = _XML_TITLE_OVERRIDES.get(path, page["title"])
    overrides = _XML_PAGE_OVERRIDES.get(path, {})
    method = overrides.get("method", page.get("method", ""))
    page_type = overrides.get("type", page.get("type", ""))
    title = overrides.get("title", title)

    parts = [
        f'path="{_xml_escape(path)}"',
        f'title="{_xml_escape(title)}"',
    ]
    if method:
        parts.append(f'method="{method}"')
    if page_type:
        parts.append(f'type="{page_type}"')
    pad = " " * indent
    return f"{pad}<page {' '.join(parts)} />"


def _build_xml_api_ref(section: dict) -> list[str]:
    """Build XML content for the API Reference section.

    Flattens subsections into direct <page> children with inline comments,
    with a blank line before each comment group.
    """
    comment_map = {
        "Infrastructure": "Infrastructure",
        "SDK Overviews": "SDK Overviews",
        "Messages": "Messages",
        "Models": "Models",
        "Completions": "Completions",
        "Admin": "Admin",
        "Beta": "Beta",
        "Per-SDK Endpoint Pages": (
            "SDK References: covered by sdk-pattern below "
            "(10 SDKs x 45 endpoints = 450 pages)"
        ),
    }

    lines: list[str] = []
    for sub in section.get("subsections", []):
        sub_name = sub["name"]
        label = comment_map.get(sub_name, sub_name)

        # Blank line before comment (except the very first group)
        if lines:
            lines.append("")
        lines.append(f"      <!-- {label} -->")

        for page in sub.get("pages", []):
            lines.append(_xml_page_line(page))

    return lines


def _build_xml_sdk_pattern(sdk_pattern: dict) -> list[str]:
    """Build XML lines for <sdk-pattern> element."""
    total_pages = sdk_pattern.get("total_sdk_pages", 450)
    pages_per_sdk = sdk_pattern.get("pages_per_sdk", 45)
    sdks = sdk_pattern.get("sdks", [])
    # XML uses {endpoint} not {endpoint_path}
    url_template = sdk_pattern.get("url_template", "").replace(
        "{endpoint_path}", "{endpoint}"
    )

    # Method lookup for sdk endpoints
    _action_methods: dict[str, str] = {
        "create": "POST",
        "upload": "POST",
        "count_tokens": "POST",
        "list": "GET",
        "retrieve": "GET",
        "retrieve_metadata": "GET",
        "download": "GET",
        "results": "GET",
        "cancel": "DELETE",
        "delete": "DELETE",
        "update": "PATCH",
        "archive": "DELETE",
        "me": "GET",
    }

    hub_pages = set(sdk_pattern.get("endpoint_types", {}).get("hub_pages", []))
    endpoint_type = sdk_pattern.get("endpoint_types", {}).get(
        "endpoint_pages_type", "api-endpoint"
    )

    lines: list[str] = [
        "",
        f"  <!-- SDK Reference Pattern: {len(sdks)} SDKs"
        f" x {pages_per_sdk} endpoints = {total_pages} pages -->",
        f'  <sdk-pattern total-pages="{total_pages}"'
        f' pages-per-sdk="{pages_per_sdk}"'
        f' url-template="{url_template}">',
        "    <sdks>",
    ]
    for sdk in sdks:
        lines.append(f'      <sdk name="{sdk}" />')
    lines.append("    </sdks>")
    lines.append("    <endpoints>")

    for ep_path in sdk_pattern.get("endpoint_paths", []):
        ep_type = "api-hub" if ep_path in hub_pages else endpoint_type
        # Get method override first, then derive from path
        method = _XML_SDK_ENDPOINT_OVERRIDES.get(ep_path, "")
        if not method and ep_type != "api-hub":
            action = ep_path.rstrip("/").split("/")[-1]
            method = _action_methods.get(action, "")

        if ep_type == "api-hub":
            lines.append(f'      <endpoint path="{ep_path}" type="{ep_type}" />')
        elif method:
            lines.append(
                f'      <endpoint path="{ep_path}" method="{method}" type="{ep_type}" />'
            )
        else:
            lines.append(f'      <endpoint path="{ep_path}" type="{ep_type}" />')

    lines.append("    </endpoints>")
    lines.append("  </sdk-pattern>")
    return lines


def _build_xml_nav_claude(navigation: dict) -> list[str]:
    """Build <navigation> for claude-code style."""
    lines: list[str] = [
        "",
        "  <!-- Navigation: Section selection rules for AI agents -->",
        "  <navigation>",
    ]
    nav_rules = [
        ("getting-started", "Introduction", "New users, setup, first steps"),
        (
            "model-selection",
            "About Claude",
            "Choosing models, pricing, deprecations, use cases",
        ),
        (
            "feature-implementation",
            "Build with Claude",
            "Implementing specific API features: streaming, caching, vision, PDFs, "
            "structured output, extended thinking",
        ),
        (
            "agent-development",
            "Agents and Tools, Agent SDK",
            "Building agents, tool use, MCP, computer use, agent SDK integration",
        ),
        (
            "api-integration",
            "API Reference",
            "Endpoint details, request/response schemas, SDK-specific code examples",
        ),
        (
            "sdk-specific",
            "API Reference",
            "Use sdk-pattern URL template: /docs/en/api/{sdk}/{endpoint} "
            "for language-specific references",
        ),
        (
            "testing",
            "Test and Evaluate",
            "Evals, guardrails, hallucination reduction, latency optimization",
        ),
        (
            "changelog",
            "Release Notes",
            "API changes, model updates, system prompt history",
        ),
        ("general-reference", "Resources", "Additional resources, community links"),
        (
            "admin-management",
            "API Reference",
            "Organization, workspace, user, and API key management via admin endpoints",
        ),
        (
            "prompt-optimization",
            "Build with Claude",
            "Prompt engineering best practices, caching strategies, token counting",
        ),
    ]
    for context, secs, desc in nav_rules:
        lines.append(
            f'    <rule context="{context}" sections="{secs}"'
            f' description="{_xml_escape(desc)}" />'
        )
    lines.append("  </navigation>")
    return lines


def _build_xml_nav_codex(navigation: dict) -> list[str]:
    """Build <navigation> for gpt-codex style."""
    default_section = navigation.get("default_section", "")
    search_priority = navigation.get("search_priority", [])
    abbreviated_tips = [
        "Start with /codex/quickstart for initial setup",
        "Use /codex/prompting to learn how to interact with Codex effectively",
        "Configuration guides cover AGENTS.md, MCP, Skills, and Rules",
        "Platform-specific: App for desktop, IDE for VS Code, CLI for terminal, Web for cloud",
        "For CI/CD automation, see Non-interactive Mode and GitHub Action",
    ]

    lines: list[str] = ["  <navigation>"]
    if default_section:
        lines.append(f"    <default-section>{_xml_escape(default_section)}</default-section>")
    if search_priority:
        lines.append("    <search-priority>")
        for sec in search_priority:
            lines.append(f"      <section>{_xml_escape(sec)}</section>")
        lines.append("    </search-priority>")
    lines.append("    <tips>")
    for tip in abbreviated_tips:
        lines.append(f"      <tip>{_xml_escape(tip)}</tip>")
    lines.append("    </tips>")
    lines.append("  </navigation>")
    return lines


def _build_xml_external_refs(external_refs: list) -> list[str]:
    """Build <external-references> element."""
    lines: list[str] = ["", "  <external-references>"]
    for group in external_refs:
        gname = _xml_escape(group["name"])
        lines.append(f'    <group name="{gname}">')
        for ref in group.get("pages", []):
            path = _xml_escape(ref["path"])
            title = _xml_escape(ref["title"])
            lines.append(f'      <link path="{path}" title="{title}" />')
        lines.append("    </group>")
    lines.append("  </external-references>")
    return lines


def generate_xml(data: dict) -> str:
    """Generate XML format from agents.json data using string assembly."""
    version = data.get("agents_txt_version", "0.1")
    site = data.get("site", {})
    sections = data.get("sections", [])
    sdk_pattern = data.get("sdk_pattern")
    navigation = data.get("navigation", {})
    external_refs = data.get("external_references", [])

    is_claude = sdk_pattern is not None

    lines: list[str] = [
        '<?xml version="1.0" encoding="UTF-8"?>',
        f'<agents version="{version}">',
    ]

    # <site />
    site_name = _xml_escape(site.get("name", ""))
    site_url = _xml_escape(site.get("url", ""))
    total_pages = site.get("total_pages", 0)
    last_updated = site.get("last_updated", "")
    lines.append(
        f'  <site name="{site_name}" url="{site_url}"'
        f' total-pages="{total_pages}" last-updated="{last_updated}" />'
    )
    lines.append("")

    # <sections>
    lines.append("  <sections>")

    for idx, section in enumerate(sections, 1):
        name = section["name"]
        xml_name = _XML_SECTION_NAME_MAP.get(name, name)
        prefix = section.get("path_prefix", "")
        page_count = section["page_count"]
        pages = section.get("pages", [])
        subsections = section.get("subsections")

        lines.append(f"    <!-- {idx}. {name} -->")
        lines.append(
            f'    <section name="{_xml_escape(xml_name)}"'
            f' path-prefix="{prefix}"'
            f' page-count="{page_count}">'
        )

        if subsections is not None:
            lines.extend(_build_xml_api_ref(section))
        elif pages:
            for page in pages:
                lines.append(_xml_page_line(page))

        lines.append("    </section>")
        lines.append("")

    # Remove the last blank line before </sections>
    if lines and lines[-1] == "":
        lines.pop()
    lines.append("  </sections>")

    # <sdk-pattern>
    if sdk_pattern:
        lines.extend(_build_xml_sdk_pattern(sdk_pattern))

    # <external-references>
    if external_refs:
        lines.extend(_build_xml_external_refs(external_refs))

    # <navigation>
    if is_claude:
        lines.extend(_build_xml_nav_claude(navigation))
    else:
        # Codex: blank line before navigation
        lines.append("")
        lines.extend(_build_xml_nav_codex(navigation))

    lines.append("</agents>")
    return "\n".join(lines) + "\n"


# ---------------------------------------------------------------------------
# TXT generator
# ---------------------------------------------------------------------------

_TXT_SCHEMA_CLAUDE = (
    "== SCHEMA ==\n"
    "# Formal grammar for parsing this file\n"
    "# HEADER: key-value pairs (KEY: value)\n"
    "# SECTION: [Name] N pages | prefix=/path/\n"
    "# PAGE: relative-path | type=TYPE — description (optional)\n"
    "# PAGE (absolute): /full/path | type=TYPE — description (optional)\n"
    "# TEMPLATE: TEMPLATE sdk={list} then indented {sdk}/endpoint lines\n"
    "# NAVIGATION: RULES (numbered), INTENT MAP (intent → section)\n"
    "# TYPES: overview, tutorial, guide, reference, use-case, tool-reference, "
    "sdk-guide, api-reference, api-endpoint, api-hub, best-practices, changelog\n"
    "# DELIMITER: | separates path from type; — separates type from description\n"
    "# PREFIX RULE: full_url = prefix + \"/\" + relative_path"
)

_TXT_SCHEMA_CODEX = (
    "== SCHEMA ==\n"
    "# Formal grammar for parsing this file\n"
    "# HEADER: key-value pairs (KEY: value)\n"
    "# SECTION: [Name] N pages | prefix=/path/\n"
    "# PAGE: relative-path | type=TYPE\n"
    "# PAGE (absolute): /full/path | type=TYPE\n"
    "# NAVIGATION: RULES (numbered), INTENT MAP (intent → section)\n"
    "# TYPES: overview, tutorial, guide, reference, use-case, "
    "tool-reference, sdk-guide, changelog\n"
    "# DELIMITER: | separates path from type\n"
    "# PREFIX RULE: full_url = URL + path"
)

# Sections that use absolute paths and NO prefix in header for claude-code
_CC_ABSOLUTE_SECTIONS = {"Introduction", "Resources"}

# Introduction page descriptions
_CC_INTRO_DESCRIPTIONS: dict[str, str] = {
    "/docs/en/intro": "Platform introduction",
    "/docs/en/get-started": "Quick start tutorial",
}

# TXT admin section: sub-resource hub pages become api-endpoint
# (only the root 'admin' page keeps api-hub)
_TXT_ADMIN_FORCE_ENDPOINT_PATHS = {
    "/docs/en/api/admin/organizations",
    "/docs/en/api/admin/users",
    "/docs/en/api/admin/invites",
    "/docs/en/api/admin/api_keys",
    "/docs/en/api/admin/workspaces",
    "/docs/en/api/admin/workspaces/members",
    "/docs/en/api/admin/cost_report",
    "/docs/en/api/admin/usage_report",
}


def _txt_build_claude_intro() -> list[str]:
    """Render Introduction section for claude-code TXT."""
    lines = ["[Introduction] 2 pages"]
    for path, desc in _CC_INTRO_DESCRIPTIONS.items():
        lines.append(f"  {path} | type=tutorial — {desc}")
    lines.append("")
    return lines


def _txt_build_api_ref(section: dict, sdk_pattern: dict | None) -> list[str]:
    """Build TXT lines for the API Reference section."""
    path_prefix = section.get("path_prefix", "")
    prefix = path_prefix.rstrip("/") + "/"

    lines: list[str] = [f"[API Reference] {section['page_count']} pages | prefix={prefix}", ""]

    group_comments = {
        "Infrastructure": "# Infrastructure (10)",
        "SDK Overviews": "# SDK Overviews (7)",
        "Messages": "# Messages (10)",
        "Models": "# Models (3)",
        "Completions": "# Completions (2)",
        "Admin": "# Admin (34)",
        "Beta": "# Beta (30)",
    }

    for sub in section.get("subsections", []):
        sub_name = sub["name"]
        comment = group_comments.get(sub_name)
        if comment:
            lines.append(f"  {comment}")

        for page in sub.get("pages", []):
            path = page["path"]
            # Use relative path (strip prefix)
            if path.startswith(prefix):
                rel = path[len(prefix):]
            else:
                rel = path

            # Determine type, applying admin override
            page_type = page.get("type", "")
            if path in _TXT_ADMIN_FORCE_ENDPOINT_PATHS:
                page_type = "api-endpoint"

            lines.append(f"  {rel} | type={page_type}")

        if sub.get("pages"):
            lines.append("")

    # SDK Template block
    if sdk_pattern:
        sdks = sdk_pattern.get("sdks", [])
        total = sdk_pattern.get("total_sdk_pages", 450)
        pages_per = sdk_pattern.get("pages_per_sdk", 45)
        hub_pages = set(sdk_pattern.get("endpoint_types", {}).get("hub_pages", []))
        endpoint_type = sdk_pattern.get("endpoint_types", {}).get(
            "endpoint_pages_type", "api-endpoint"
        )
        sdk_names = ",".join(sdks)
        sdks_joined = ", ".join(sdks)

        lines.append(
            f"  # SDK Endpoints ({total} = {len(sdks)} SDKs x {pages_per} endpoints)"
        )
        lines.append(f"  # SDKs: {sdks_joined}")
        lines.append("  # Pattern: /docs/en/api/{sdk}/{endpoint}")
        lines.append(f"  # {pages_per} endpoints per SDK:")
        lines.append(
            "  # Hub endpoints (type=api-hub): messages, messages/batches, models,"
            " completions, beta, beta/files, beta/messages, beta/messages/batches,"
            " beta/models, beta/skills, beta/skills/versions"
        )
        lines.append(
            "  # Action endpoints (type=api-endpoint): all others with"
            " create/list/retrieve/delete/upload/download/cancel/results/count_tokens/update"
        )
        lines.append(f"  TEMPLATE sdk={{{sdk_names}}}")
        for ep_path in sdk_pattern.get("endpoint_paths", []):
            ep_type = "api-hub" if ep_path in hub_pages else endpoint_type
            lines.append(f"    {{sdk}}/{ep_path} | type={ep_type}")
        lines.append("")

    return lines


def _txt_build_section_claude(section: dict) -> list[str]:
    """Build TXT lines for a regular claude-code section."""
    name = section["name"]
    page_count = section["page_count"]
    pages = section.get("pages", [])
    path_prefix = section.get("path_prefix", "")
    prefix = path_prefix.rstrip("/")
    count_word = "page" if page_count == 1 else "pages"

    if name in _CC_ABSOLUTE_SECTIONS:
        # No prefix in header, absolute paths
        header = f"[{name}] {page_count} {count_word}"
        lines = [header]
        for page in pages:
            page_type = page.get("type", "")
            lines.append(f"  {page['path']} | type={page_type}")
        lines.append("")
        return lines

    # Normal section with prefix
    prefix_display = prefix + "/"
    lines = [f"[{name}] {page_count} {count_word} | prefix={prefix_display}"]
    for page in pages:
        path = page["path"]
        page_type = page.get("type", "")
        if path.startswith(prefix + "/"):
            rel = path[len(prefix):].lstrip("/")
            lines.append(f"  {rel} | type={page_type}")
        else:
            lines.append(f"  {path} | type={page_type}")
    lines.append("")
    return lines


def _txt_build_section_codex(section: dict) -> list[str]:
    """Build TXT lines for a gpt-codex section.

    Sections with path_prefix='/codex' (root) use absolute paths, no prefix header.
    Sections with deeper prefixes (e.g. /codex/app) use prefix header with mix.
    """
    name = section["name"]
    page_count = section["page_count"]
    pages = section.get("pages", [])
    path_prefix = section.get("path_prefix", "")
    prefix = path_prefix.rstrip("/")
    count_word = "page" if page_count == 1 else "pages"

    # Root-level sections (prefix == '/codex') -> no prefix header, absolute paths
    if prefix == "/codex":
        lines = [f"[{name}] {page_count} {count_word}"]
        for page in pages:
            page_type = page.get("type", "")
            lines.append(f"  {page['path']} | type={page_type}")
        lines.append("")
        return lines

    # Deep prefix sections
    prefix_display = prefix + "/"
    lines = [f"[{name}] {page_count} {count_word} | prefix={prefix_display}"]
    for page in pages:
        path = page["path"]
        page_type = page.get("type", "")
        if path == prefix:
            # Page path exactly equals prefix (no trailing slash) -> absolute
            lines.append(f"  {path} | type={page_type}")
        elif path.startswith(prefix + "/"):
            rel = path[len(prefix):].lstrip("/")
            lines.append(f"  {rel} | type={page_type}")
        else:
            lines.append(f"  {path} | type={page_type}")
    lines.append("")
    return lines


def _txt_nav_claude() -> list[str]:
    """Navigation section for claude-code TXT."""
    lines = [
        "== NAVIGATION ==",
        "",
        "RULES:",
        "  1. Start with section matching user intent",
        "  2. Use prefix + relative path to construct full URL",
        "  3. For API SDK endpoints, expand TEMPLATE: replace {sdk} with target SDK name",
        "  4. Prefer overview pages when intent is broad",
        "  5. Prefer specific pages when intent is narrow",
        "",
        "INTENT MAP:",
        "  getting-started    → Introduction",
        "  models, pricing    → About Claude",
        "  prompts, features  → Build with Claude",
        "  tools, mcp, agents → Agents & Tools",
        "  claude-code, sdk   → Agent SDK",
        "  api, endpoints     → API Reference",
        "  testing, evals     → Test & Evaluate",
        "  changelog          → Release Notes",
        "  resources          → Resources",
    ]
    return lines


def _txt_nav_codex() -> list[str]:
    """Navigation section for gpt-codex TXT."""
    lines = [
        "== NAVIGATION ==",
        "",
        "RULES:",
        '  1. Start with "Getting Started" for initial setup',
        '  2. Use "Concepts" section for understanding prompting, workflows, and models',
        "  3. Platform-specific guides: App (desktop), IDE (VS Code), CLI (terminal), Web (cloud)",
        "  4. Configuration covers AGENTS.md, MCP, Skills, Rules, and speed optimization",
        "  5. Enterprise setup in Administration section",
        "  6. CI/CD automation via Non-interactive Mode and GitHub Action",
        "",
        "INTENT MAP:",
        "  getting started     → Getting Started",
        "  how to prompt       → Concepts",
        "  desktop app         → Using Codex — App",
        "  vs code / ide       → Using Codex — IDE Extension",
        "  terminal / cli      → Using Codex — CLI",
        "  cloud / web         → Using Codex — Web",
        "  github / slack      → Integrations",
        "  security            → Codex Security",
        "  config / setup      → Configuration",
        "  enterprise / admin  → Administration",
        "  automation / ci     → Automation",
        "  sdk                 → Automation",
        "  changelog           → Releases",
    ]
    return lines


def generate_txt(data: dict) -> str:
    """Generate plain-text format from agents.json data."""
    version = data.get("agents_txt_version", "0.1")
    site = data.get("site", {})
    sections = data.get("sections", [])
    sdk_pattern = data.get("sdk_pattern")

    is_claude = sdk_pattern is not None

    lines: list[str] = [
        f"# agents.txt v{version}",
        f"# {site.get('name', '')} — {site.get('url', '')}",
        f"# Total: {site.get('total_pages', 0)} pages | Last updated: {site.get('last_updated', '')}",
        "",
        f"SITE: {site.get('name', '')}",
        f"URL: {site.get('url', '')}",
        f"PAGES: {site.get('total_pages', 0)}",
        f"SECTIONS: {len(sections)}",
        "",
        _TXT_SCHEMA_CLAUDE if is_claude else _TXT_SCHEMA_CODEX,
        "",
        "== SECTIONS ==",
        "",
    ]

    for section in sections:
        name = section["name"]

        if name == "Introduction" and is_claude:
            lines.extend(_txt_build_claude_intro())
            continue

        if section.get("subsections") is not None:
            lines.extend(_txt_build_api_ref(section, sdk_pattern))
            continue

        if is_claude:
            lines.extend(_txt_build_section_claude(section))
        else:
            lines.extend(_txt_build_section_codex(section))

    # Navigation
    if is_claude:
        lines.extend(_txt_nav_claude())
    else:
        lines.extend(_txt_nav_codex())

    return "\n".join(lines) + "\n"


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

    original_md_path = json_path.with_suffix(".md")

    outputs: list[tuple[str, str]] = [
        ("md", generate_md(data, original_md_path)),
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
