#!/usr/bin/env python3
"""
Generic NAV-AGENT test framework for agents.txt format verification.

Validates how well agents.<format> files convey documentation structure
across multiple sources (claude-code, claude-api, gpt-codex, gemini-cli)
and formats (md, txt, json, xml).

Ground truth is auto-extracted from agents.json — no hardcoded queries.

Usage:
    python3 tests/nav-agent-test.py --source claude-code --format txt
    python3 tests/nav-agent-test.py --source claude-api --format md --max-queries 30
    python3 tests/nav-agent-test.py --source gemini-cli --format json --output tests/reports/
"""

import argparse
import json
import os
import random
import re
import subprocess
import sys
import tempfile
import time
from concurrent.futures import ThreadPoolExecutor, as_completed
from dataclasses import dataclass, field
from datetime import datetime
from pathlib import Path
from typing import Optional

# ---------------------------------------------------------------------------
# Constants
# ---------------------------------------------------------------------------

PROJECT_ROOT = Path(__file__).resolve().parent.parent
REPORTS_DIR = PROJECT_ROOT / "tests" / "reports"

VALID_SOURCES = ("claude-code", "claude-api", "gpt-codex", "gemini-cli")
VALID_FORMATS = ("md", "txt", "json", "xml")

BATCH_SIZE = 10
MAX_WORKERS = 10
BATCH_TIMEOUT = 300

GRADE_THRESHOLDS = {
    "A": 90,
    "B": 80,
    "C": 70,
    "D": 60,
}


# ---------------------------------------------------------------------------
# Data models
# ---------------------------------------------------------------------------

@dataclass
class SiteInfo:
    """Metadata extracted from agents.json."""

    name: str
    url: str
    total_pages: int
    last_updated: str
    description: str


@dataclass
class SectionInfo:
    """A single section from agents.json."""

    name: str
    page_count: int
    path_prefix: str
    pages: list[dict]


@dataclass
class AgentsDoc:
    """Parsed agents.json document."""

    site: SiteInfo
    sections: list[SectionInfo]
    raw_content: str  # Content of agents.<format> file passed to codex


@dataclass
class Query:
    """A single test query with expected answer and match type."""

    id: str
    category: str
    text: str
    expected: str
    match_type: str  # exact | substring | list


@dataclass
class Result:
    """Graded result for a single query."""

    query: Query
    raw_answer: str = ""
    score: float = 0.0

    @property
    def passed(self) -> bool:
        return self.score >= 1.0


@dataclass
class ReportData:
    """Aggregated test report."""

    source: str
    format: str
    model: str
    site: SiteInfo
    sections: list[SectionInfo]
    results: list[Result]
    elapsed: float
    timestamp: str = field(default_factory=lambda: datetime.now().strftime("%Y-%m-%d %H:%M:%S"))

    @property
    def total_score(self) -> float:
        return sum(r.score for r in self.results)

    @property
    def total_queries(self) -> int:
        return len(self.results)

    @property
    def score_pct(self) -> float:
        return (self.total_score / self.total_queries * 100) if self.total_queries else 0.0

    @property
    def letter_grade(self) -> str:
        pct = self.score_pct
        for letter, threshold in GRADE_THRESHOLDS.items():
            if pct >= threshold:
                return letter
        return "F"


# ---------------------------------------------------------------------------
# Ground truth extraction
# ---------------------------------------------------------------------------

def load_agents_doc(source: str, fmt: str) -> AgentsDoc:
    """Load and parse agents.json and agents.<fmt> for the given source."""
    source_dir = PROJECT_ROOT / "public" / source
    json_path = source_dir / "agents.json"
    format_path = source_dir / f"agents.{fmt}"

    if not json_path.exists():
        print(f"ERROR: agents.json not found at {json_path}", file=sys.stderr)
        sys.exit(1)
    if not format_path.exists():
        print(f"ERROR: agents.{fmt} not found at {format_path}", file=sys.stderr)
        sys.exit(1)

    with open(json_path, encoding="utf-8") as f:
        data = json.load(f)

    raw_site = data.get("site", {})
    site = SiteInfo(
        name=raw_site.get("name", source),
        url=raw_site.get("url", ""),
        total_pages=raw_site.get("total_pages", 0),
        last_updated=raw_site.get("last_updated", ""),
        description=raw_site.get("description", ""),
    )

    sections = [
        SectionInfo(
            name=s.get("name", ""),
            page_count=s.get("page_count", 0),
            path_prefix=s.get("path_prefix", ""),
            pages=s.get("pages", []),
        )
        for s in data.get("sections", [])
        if s.get("pages")  # only sections with pages
    ]

    with open(format_path, encoding="utf-8") as f:
        raw_content = f.read()

    return AgentsDoc(site=site, sections=sections, raw_content=raw_content)


# ---------------------------------------------------------------------------
# Query generation
# ---------------------------------------------------------------------------

def _sample_pages(pages: list[dict], n: int, seed: int = 42) -> list[dict]:
    """Return up to n pages sampled with a fixed seed for reproducibility."""
    rng = random.Random(seed)
    return rng.sample(pages, min(n, len(pages)))


def _strip_md_extension(path: str) -> str:
    """Remove trailing .md from a path segment for cleaner expected strings."""
    return path[:-3] if path.endswith(".md") else path


def generate_structure_queries(doc: AgentsDoc, max_count: int) -> list[Query]:
    """
    Category A: Structure queries.
    Ask about total pages, section counts, and per-section page counts.
    """
    queries: list[Query] = []

    # Total pages
    queries.append(Query(
        id="A1",
        category="Structure",
        text=f"How many total pages are listed in this document?",
        expected=str(doc.site.total_pages),
        match_type="exact",
    ))

    # Total section count
    queries.append(Query(
        id="A2",
        category="Structure",
        text="How many sections are listed in this document?",
        expected=str(len(doc.sections)),
        match_type="exact",
    ))

    # Per-section page counts (up to 8 more)
    slot = 3
    for section in doc.sections[: max_count - 2]:
        if slot > max_count:
            break
        queries.append(Query(
            id=f"A{slot}",
            category="Structure",
            text=f"How many pages does the '{section.name}' section have?",
            expected=str(section.page_count),
            match_type="exact",
        ))
        slot += 1

    return queries[:max_count]


def generate_direct_lookup_queries(doc: AgentsDoc, max_count: int) -> list[Query]:
    """
    Category B: Direct path lookup.
    Sample representative pages and ask for their paths.
    """
    queries: list[Query] = []
    slot = 1

    for section in doc.sections:
        if slot > max_count:
            break
        sampled = _sample_pages(section.pages, 2)
        for page in sampled:
            if slot > max_count:
                break
            path = _strip_md_extension(page.get("path", ""))
            title = page.get("title", path.split("/")[-1])
            queries.append(Query(
                id=f"B{slot}",
                category="Direct Lookup",
                text=f"Find the path for '{title}'.",
                expected=path,
                match_type="substring",
            ))
            slot += 1

    return queries[:max_count]


def generate_section_enumeration_queries(doc: AgentsDoc, max_count: int) -> list[Query]:
    """
    Category C: Section enumeration.
    Ask for lists of section names or content-type groups within sections.
    """
    queries: list[Query] = []
    slot = 1

    # Enumerate section names
    section_names = [s.name for s in doc.sections]
    if section_names:
        queries.append(Query(
            id=f"C{slot}",
            category="Section Enumeration",
            text="List all section names in this document.",
            expected=",".join(section_names[:5]),  # check first 5
            match_type="list",
        ))
        slot += 1

    # For sections with multiple pages, list a subset of page names
    for section in doc.sections:
        if slot > max_count:
            break
        pages = section.pages
        if len(pages) < 2:
            continue
        sampled = _sample_pages(pages, 3)
        slugs = [
            _strip_md_extension(p.get("path", "")).split("/")[-1]
            for p in sampled
        ]
        slugs = [s for s in slugs if s]
        if not slugs:
            continue
        queries.append(Query(
            id=f"C{slot}",
            category="Section Enumeration",
            text=f"What pages are in the '{section.name}' section? List some slugs.",
            expected=",".join(slugs),
            match_type="list",
        ))
        slot += 1

    return queries[:max_count]


def generate_full_url_queries(doc: AgentsDoc, max_count: int) -> list[Query]:
    """
    Category D: Full URL construction.
    Ask for complete URLs combining site base URL and page paths.
    """
    queries: list[Query] = []
    slot = 1
    base_url = doc.site.url.rstrip("/")

    for section in doc.sections:
        if slot > max_count:
            break
        sampled = _sample_pages(section.pages, 1, seed=slot * 7)
        for page in sampled:
            if slot > max_count:
                break
            path = _strip_md_extension(page.get("path", ""))
            title = page.get("title", path.split("/")[-1])
            full_url = base_url + path
            queries.append(Query(
                id=f"D{slot}",
                category="Full URL Construction",
                text=f"What is the full URL for '{title}'?",
                expected=full_url,
                match_type="substring",
            ))
            slot += 1

    return queries[:max_count]


def generate_page_type_queries(doc: AgentsDoc, max_count: int) -> list[Query]:
    """
    Category E: Page type classification.
    Ask what type a specific page is, based on agents.json type field.
    """
    queries: list[Query] = []
    slot = 1

    for section in doc.sections:
        if slot > max_count:
            break
        typed_pages = [p for p in section.pages if p.get("type")]
        sampled = _sample_pages(typed_pages, 2, seed=slot * 13)
        for page in sampled:
            if slot > max_count:
                break
            path = _strip_md_extension(page.get("path", ""))
            title = page.get("title", path.split("/")[-1])
            page_type = page.get("type", "")
            if not page_type:
                continue
            queries.append(Query(
                id=f"E{slot}",
                category="Page Type",
                text=f"What type is the '{title}' page?",
                expected=page_type,
                match_type="exact",
            ))
            slot += 1

    return queries[:max_count]


def build_query_set(doc: AgentsDoc, max_queries: int) -> list[Query]:
    """
    Build a balanced query set from all categories, capped at max_queries.

    Distribution across 4 core categories + 1 optional:
      A (Structure)         : 20%
      B (Direct Lookup)     : 30%
      C (Section Enum)      : 20%
      D (Full URL)          : 20%
      E (Page Type)         : 10%
    """
    budget = max_queries
    a_budget = max(2, round(budget * 0.20))
    b_budget = max(2, round(budget * 0.30))
    c_budget = max(2, round(budget * 0.20))
    d_budget = max(2, round(budget * 0.20))
    e_budget = max(1, budget - a_budget - b_budget - c_budget - d_budget)

    all_queries: list[Query] = []
    all_queries.extend(generate_structure_queries(doc, a_budget))
    all_queries.extend(generate_direct_lookup_queries(doc, b_budget))
    all_queries.extend(generate_section_enumeration_queries(doc, c_budget))
    all_queries.extend(generate_full_url_queries(doc, d_budget))
    all_queries.extend(generate_page_type_queries(doc, e_budget))

    return all_queries[:max_queries]


# ---------------------------------------------------------------------------
# Codex invocation (adapted from navigator-codex-test.py)
# ---------------------------------------------------------------------------

def build_prompt(agents_content: str, batch: list[Query]) -> str:
    """Build the prompt for a batch of queries."""
    query_lines = "\n".join(f"Q{i + 1}: {q.text}" for i, q in enumerate(batch))
    return (
        "Parse this agents document and answer queries. "
        'Reply ONLY in format "Q{n}: {answer}" one per line.\n\n'
        f"[AGENTS DOCUMENT]\n{agents_content}\n\n"
        f"[QUERIES]\n{query_lines}"
    )


def run_codex(prompt: str, model: str = "default") -> str:
    """Run a single codex exec call and return stdout."""
    with tempfile.NamedTemporaryFile(mode="w", suffix=".txt", delete=False) as f:
        f.write(prompt)
        tmppath = f.name

    model_flag = f"--model {model}" if model and model != "default" else ""
    cmd = (
        f'codex {model_flag} --dangerously-bypass-approvals-and-sandbox exec '
        f'"$(cat {tmppath})" 2>&1'
    )

    try:
        proc = subprocess.run(
            cmd,
            shell=True,
            capture_output=True,
            text=True,
            timeout=BATCH_TIMEOUT,
        )
        return proc.stdout
    except subprocess.TimeoutExpired:
        return "ERROR: codex timed out"
    except FileNotFoundError:
        return "ERROR: codex CLI not found"
    finally:
        try:
            os.unlink(tmppath)
        except OSError:
            pass


# ---------------------------------------------------------------------------
# Response parsing
# ---------------------------------------------------------------------------

_Q_PATTERN = re.compile(r"Q(\d+)\s*:\s*(.+)", re.IGNORECASE)


def parse_response(raw: str) -> dict[int, str]:
    """Extract Q{n}: {answer} lines from codex output."""
    answers: dict[int, str] = {}
    for line in raw.splitlines():
        m = _Q_PATTERN.match(line.strip())
        if m:
            answers[int(m.group(1))] = m.group(2).strip()
    return answers


# ---------------------------------------------------------------------------
# Grading
# ---------------------------------------------------------------------------

def grade(query: Query, raw_answer: str) -> float:
    """Score a single answer against the expected value."""
    answer = raw_answer.strip().lower()
    expected = query.expected.strip().lower()

    if query.match_type == "exact":
        return 1.0 if expected in answer else 0.0

    elif query.match_type == "substring":
        if expected in answer:
            return 1.0
        # Partial credit for path segment matches
        segments = [s for s in expected.split("/") if s]
        if len(segments) > 1:
            matched = sum(1 for seg in segments if seg in answer)
            ratio = matched / len(segments)
            return round(ratio * 0.5, 2) if ratio > 0.3 else 0.0
        return 0.0

    elif query.match_type == "list":
        items = [x.strip() for x in expected.split(",") if x.strip()]
        if not items:
            return 0.0
        found = sum(1 for item in items if item in answer)
        return round(found / len(items), 2)

    return 0.0


# ---------------------------------------------------------------------------
# Batch runner
# ---------------------------------------------------------------------------

def make_batches(queries: list[Query], size: int = BATCH_SIZE) -> list[list[Query]]:
    """Split queries into fixed-size batches."""
    return [queries[i: i + size] for i in range(0, len(queries), size)]


def run_batch(
    batch_idx: int,
    batch: list[Query],
    agents_content: str,
    total_batches: int,
    model: str,
) -> list[Result]:
    """Execute a single batch against codex and return graded results."""
    prompt = build_prompt(agents_content, batch)
    cats = {q.category for q in batch}
    cat_label = ", ".join(sorted(cats))
    print(f"  [Batch {batch_idx + 1}/{total_batches}] Sending: {cat_label}...")

    raw = run_codex(prompt, model)
    answers = parse_response(raw)

    results: list[Result] = []
    for i, query in enumerate(batch):
        ans = answers.get(i + 1, "")
        score = grade(query, ans)
        results.append(Result(query=query, raw_answer=ans, score=score))

    passed = sum(1 for r in results if r.passed)
    print(f"  [Batch {batch_idx + 1}/{total_batches}] Done -- {passed}/{len(batch)} passed")
    return results


# ---------------------------------------------------------------------------
# Report generation
# ---------------------------------------------------------------------------

def generate_report(report: ReportData) -> str:
    """Render a Markdown report from aggregated results."""
    lines: list[str] = []

    # Header
    lines.append(f"# NAV-AGENT Test Report: {report.source} × {report.format}\n")
    lines.append("## Metadata\n")
    lines.append(f"| Field | Value |")
    lines.append(f"|-------|-------|")
    lines.append(f"| Source | {report.source} |")
    lines.append(f"| Format | {report.format} |")
    lines.append(f"| Model | {report.model} |")
    lines.append(f"| Site | {report.site.name} |")
    lines.append(f"| Total Pages | {report.site.total_pages} |")
    lines.append(f"| Sections | {len(report.sections)} |")
    lines.append(f"| Queries | {report.total_queries} |")
    lines.append(f"| Elapsed | {report.elapsed:.1f}s |")
    lines.append(f"| Timestamp | {report.timestamp} |")
    lines.append("")

    # Overall score
    grade_label = report.letter_grade
    lines.append("## Overall Score\n")
    lines.append(
        f"**{report.total_score:.1f} / {report.total_queries} "
        f"({report.score_pct:.1f}%) — Grade {grade_label}**\n"
    )

    # Category summary
    cat_results: dict[str, list[Result]] = {}
    for r in report.results:
        cat_results.setdefault(r.query.category, []).append(r)

    lines.append("## Category Summary\n")
    lines.append("| Category | Queries | Score | % |")
    lines.append("|----------|---------|-------|---|")

    for cat in sorted(cat_results):
        rs = cat_results[cat]
        s = sum(r.score for r in rs)
        pct = (s / len(rs)) * 100 if rs else 0
        lines.append(f"| {cat} | {len(rs)} | {s:.1f} | {pct:.0f}% |")
    lines.append("")

    # Failed queries
    failed = [r for r in report.results if not r.passed]
    if failed:
        lines.append(f"## Failed Queries ({len(failed)})\n")
        lines.append("| ID | Query | Expected | Got | Score |")
        lines.append("|----|-------|----------|-----|-------|")
        for r in failed:
            got = (r.raw_answer[:80].replace("|", "/")) or "(empty)"
            exp = r.query.expected[:60].replace("|", "/")
            q_text = r.query.text[:50]
            lines.append(
                f"| {r.query.id} | {q_text} | `{exp}` | {got} | {r.score} |"
            )
        lines.append("")

    # Full results
    lines.append("## Full Results\n")
    for cat in sorted(cat_results):
        lines.append(f"### {cat}\n")
        lines.append("| ID | Query | Expected | Got | Score |")
        lines.append("|----|-------|----------|-----|-------|")
        for r in cat_results[cat]:
            tag = "PASS" if r.passed else ("partial" if r.score > 0 else "FAIL")
            got = (r.raw_answer[:80].replace("|", "/")) or "(empty)"
            exp = r.query.expected[:60].replace("|", "/")
            lines.append(
                f"| {r.query.id} | {r.query.text[:50]} | `{exp}` | {got} | {tag} ({r.score}) |"
            )
        lines.append("")

    return "\n".join(lines)


# ---------------------------------------------------------------------------
# CLI argument parsing
# ---------------------------------------------------------------------------

def parse_args() -> argparse.Namespace:
    """Parse command-line arguments."""
    parser = argparse.ArgumentParser(
        description="Generic NAV-AGENT test framework for agents.txt format verification.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  python3 tests/nav-agent-test.py --source claude-code --format txt
  python3 tests/nav-agent-test.py --source claude-api --format md --max-queries 30
  python3 tests/nav-agent-test.py --source gemini-cli --format json --output tests/reports/
        """,
    )
    parser.add_argument(
        "--source",
        required=True,
        choices=VALID_SOURCES,
        help="Documentation source to test",
    )
    parser.add_argument(
        "--format",
        required=True,
        choices=VALID_FORMATS,
        dest="fmt",
        help="agents file format to test",
    )
    parser.add_argument(
        "--max-queries",
        type=int,
        default=40,
        metavar="N",
        help="Maximum number of queries to run (default: 40)",
    )
    parser.add_argument(
        "--output",
        type=Path,
        default=REPORTS_DIR,
        metavar="DIR",
        help="Output directory for report file (default: tests/reports/)",
    )
    parser.add_argument(
        "--model",
        default="default",
        help="Codex model to use (default: codex default)",
    )
    return parser.parse_args()


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main() -> None:
    """Entry point for the NAV-AGENT test runner."""
    args = parse_args()

    print("=" * 60)
    print("NAV-AGENT Generic Test Runner")
    print("=" * 60)
    print(f"Source : {args.source}")
    print(f"Format : {args.fmt}")
    print(f"Max Q  : {args.max_queries}")
    print(f"Model  : {args.model}")
    print()

    # Load documents
    print(f"[1/4] Loading agents.json and agents.{args.fmt}...")
    doc = load_agents_doc(args.source, args.fmt)
    print(
        f"      Site: {doc.site.name} | Pages: {doc.site.total_pages} | "
        f"Sections: {len(doc.sections)} | Content: {len(doc.raw_content)} chars"
    )

    # Build queries
    print(f"[2/4] Generating queries (max={args.max_queries})...")
    queries = build_query_set(doc, args.max_queries)
    print(f"      Generated {len(queries)} queries across {len({q.category for q in queries})} categories")

    cat_counts: dict[str, int] = {}
    for q in queries:
        cat_counts[q.category] = cat_counts.get(q.category, 0) + 1
    for cat, count in sorted(cat_counts.items()):
        print(f"      - {cat}: {count}")
    print()

    # Execute in parallel batches
    print(f"[3/4] Running batches (workers={MAX_WORKERS}, batch_size={BATCH_SIZE})...")
    batches = make_batches(queries, BATCH_SIZE)
    total_batches = len(batches)

    start = time.time()
    batch_results: dict[int, list[Result]] = {}

    with ThreadPoolExecutor(max_workers=MAX_WORKERS) as executor:
        futures = {
            executor.submit(
                run_batch, idx, batch, doc.raw_content, total_batches, args.model
            ): idx
            for idx, batch in enumerate(batches)
        }
        for future in as_completed(futures):
            idx = futures[future]
            try:
                batch_results[idx] = future.result()
            except Exception as exc:
                print(f"  [Batch {idx + 1}] FAILED: {exc}", file=sys.stderr)
                batch_results[idx] = []

    # Reassemble in original order
    all_results: list[Result] = []
    for idx in sorted(batch_results):
        all_results.extend(batch_results[idx])

    elapsed = time.time() - start

    # Aggregate
    report = ReportData(
        source=args.source,
        format=args.fmt,
        model=args.model,
        site=doc.site,
        sections=doc.sections,
        results=all_results,
        elapsed=elapsed,
    )

    # Console summary
    print(f"\n{'=' * 60}")
    print(
        f"RESULTS: {report.total_score:.1f}/{report.total_queries} "
        f"({report.score_pct:.1f}%) — Grade {report.letter_grade}"
    )
    print(f"Elapsed: {elapsed:.1f}s")
    print(f"{'=' * 60}")

    cat_results: dict[str, list[Result]] = {}
    for r in all_results:
        cat_results.setdefault(r.query.category, []).append(r)

    for cat in sorted(cat_results):
        rs = cat_results[cat]
        s = sum(r.score for r in rs)
        pct = (s / len(rs)) * 100 if rs else 0
        print(f"  {cat}: {s:.1f}/{len(rs)} ({pct:.0f}%)")

    failed = [r for r in all_results if not r.passed]
    if failed:
        print(f"\nFailed/Partial ({len(failed)}):")
        for r in failed[:10]:  # show first 10 failures
            print(
                f"  {r.query.id}: expected={r.query.expected[:40]!r}, "
                f"got={r.raw_answer[:40]!r}, score={r.score}"
            )
        if len(failed) > 10:
            print(f"  ... and {len(failed) - 10} more (see report)")

    # Save report
    print(f"\n[4/4] Saving report...")
    output_dir: Path = args.output
    output_dir.mkdir(parents=True, exist_ok=True)
    report_path = output_dir / f"{args.source}-{args.fmt}-report.md"

    report_text = generate_report(report)
    with open(report_path, "w", encoding="utf-8") as f:
        f.write(report_text)
    print(f"      Report saved to {report_path}")

    sys.exit(0 if report.score_pct >= 70 else 1)


if __name__ == "__main__":
    main()
