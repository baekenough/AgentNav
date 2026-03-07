#!/usr/bin/env python3
"""
NAVIGATOR.md spec test using Codex CLI.

Runs 100 test queries (10 categories x 10) against agents.txt via codex CLI,
batching 10 queries per call, 10 batches in parallel.

Usage:
    python3 tests/navigator-codex-test.py
"""

import json
import os
import re
import subprocess
import sys
import time
from concurrent.futures import ThreadPoolExecutor, as_completed
from dataclasses import dataclass
from datetime import datetime
from pathlib import Path

# ---------------------------------------------------------------------------
# Configuration
# ---------------------------------------------------------------------------

PROJECT_ROOT = Path(__file__).resolve().parent.parent
AGENTS_TXT_PATH = PROJECT_ROOT / "public" / "claude-code" / "agents.txt"
REPORT_PATH = PROJECT_ROOT / "tests" / "navigator-codex-report.md"
CODEX_MODEL = "default"  # use codex default model
MAX_WORKERS = 10
BATCH_SIZE = 10
BATCH_TIMEOUT = 300


def load_agents_txt() -> str:
    with open(AGENTS_TXT_PATH, "r") as f:
        return f.read()


# ---------------------------------------------------------------------------
# Test query definition
# ---------------------------------------------------------------------------

@dataclass
class Query:
    id: str
    text: str
    expected: str
    match_type: str  # exact | substring | list


@dataclass
class Result:
    query: Query
    raw_answer: str = ""
    score: float = 0.0


# fmt: off
TEST_QUERIES: list[Query] = [
    # --- Cat A: Structure (10) ---
    Query("A1",  "How many total pages are in agents.txt?", "651", "exact"),
    Query("A2",  "How many sections are in agents.txt?", "9", "exact"),
    Query("A3",  "How many pages does the API Reference section have?", "546", "exact"),
    Query("A4",  "How many pages does Build with Claude section have?", "35", "exact"),
    Query("A5",  "How many pages does the Agent SDK section have?", "27", "exact"),
    Query("A6",  "How many pages does Agents & Tools section have?", "18", "exact"),
    Query("A7",  "How many pages does About Claude section have?", "12", "exact"),
    Query("A8",  "How many pages does Test & Evaluate section have?", "8", "exact"),
    Query("A9",  "How many pages does Release Notes section have?", "2", "exact"),
    Query("A10", "How many pages does Resources section have?", "1", "exact"),

    # --- Cat B: Direct Lookup (10) ---
    Query("B1",  "Find the path for prompt-caching.", "/docs/en/build-with-claude/prompt-caching", "substring"),
    Query("B2",  "Find the path for glossary.", "/docs/en/about-claude/glossary", "substring"),
    Query("B3",  "Find the path for pricing.", "/docs/en/about-claude/pricing", "substring"),
    Query("B4",  "Find the path for extended-thinking.", "/docs/en/build-with-claude/extended-thinking", "substring"),
    Query("B5",  "Find the path for mcp-connector.", "/docs/en/agents-and-tools/mcp-connector", "substring"),
    Query("B6",  "Find the path for bash-tool.", "/docs/en/agents-and-tools/tool-use/bash-tool", "substring"),
    Query("B7",  "Find the path for quickstart in Agent SDK.", "/docs/en/agent-sdk/quickstart", "substring"),
    Query("B8",  "Find the path for subagents.", "/docs/en/agent-sdk/subagents", "substring"),
    Query("B9",  "Find the path for rate-limits.", "/docs/en/api/rate-limits", "substring"),
    Query("B10", "Find the path for reduce-hallucinations.", "/docs/en/test-and-evaluate/strengthen-guardrails/reduce-hallucinations", "substring"),

    # --- Cat C: API Navigation (10) ---
    Query("C1",  "What is the API path for messages create endpoint?", "messages/create", "substring"),
    Query("C2",  "What is the API overview path?", "api/overview", "substring"),
    Query("C3",  "What is the API errors page path?", "api/errors", "substring"),
    Query("C4",  "What is the Admin API hub path?", "api/admin", "substring"),
    Query("C5",  "What is the workspace management path?", "admin/workspaces", "substring"),
    Query("C6",  "What is the batch create endpoint path?", "messages/batches/create", "substring"),
    Query("C7",  "What is the beta files hub path?", "beta/files", "substring"),
    Query("C8",  "What is the models list endpoint path?", "models/list", "substring"),
    Query("C9",  "What is the completions API hub path?", "completions", "substring"),
    Query("C10", "What is the API versioning page path?", "api/versioning", "substring"),

    # --- Cat D: SDK Endpoint Lookup (10) ---
    Query("D1",  "What is the Python SDK path for messages/create?", "api/python/messages/create", "substring"),
    Query("D2",  "What is the TypeScript SDK path for models/list?", "api/typescript/models/list", "substring"),
    Query("D3",  "What is the Go SDK path for beta/files/upload?", "api/go/beta/files/upload", "substring"),
    Query("D4",  "What is the Java SDK path for messages/batches/create?", "api/java/messages/batches/create", "substring"),
    Query("D5",  "What is the Kotlin SDK path for completions/create?", "api/kotlin/completions/create", "substring"),
    Query("D6",  "What is the Ruby SDK path for beta/models/retrieve?", "api/ruby/beta/models/retrieve", "substring"),
    Query("D7",  "What is the PHP SDK path for messages/count_tokens?", "api/php/messages/count_tokens", "substring"),
    Query("D8",  "What is the C# SDK path for beta/skills/list?", "api/csharp/beta/skills/list", "substring"),
    Query("D9",  "What is the Terraform SDK path for messages/batches/cancel?", "api/terraform/messages/batches/cancel", "substring"),
    Query("D10", "What is the CLI SDK path for beta/files/delete?", "api/cli/beta/files/delete", "substring"),

    # --- Cat E: Natural Language Navigation (10) ---
    Query("E1",  "I want to send a message to the API. Which page?", "messages/create", "substring"),
    Query("E2",  "Where can I see available models?", "models/overview", "substring"),
    Query("E3",  "How do I cache prompts?", "prompt-caching", "substring"),
    Query("E4",  "Where is the web search tool documented?", "web-search-tool", "substring"),
    Query("E5",  "How do I get started with the Agent SDK?", "agent-sdk/quickstart", "substring"),
    Query("E6",  "How to reduce hallucinations?", "reduce-hallucinations", "substring"),
    Query("E7",  "What are the rate limiting rules?", "rate-limits", "substring"),
    Query("E8",  "Where is computer use documented?", "computer-use-tool", "substring"),
    Query("E9",  "Where is the Python SDK guide?", "python", "substring"),
    Query("E10", "How to get structured output from Claude?", "structured-outputs", "substring"),

    # --- Cat F: Section Enumeration (10) ---
    Query("F1",  "How many topics/pages are in Test & Evaluate?", "8", "exact"),
    Query("F2",  "How many use case guides are listed under About Claude?", "4", "exact"),
    Query("F3",  "List all tools in the Agents & Tools section tool-use subsection.", "bash-tool,code-execution-tool,computer-use-tool,fine-grained-tool-streaming,implement-tool-use,memory-tool,overview,programmatic-tool-calling,text-editor-tool,tool-search-tool,web-fetch-tool,web-search-tool", "list"),
    Query("F4",  "What Agent SDK configuration topics exist?", "hooks,permissions,plugins", "list"),
    Query("F5",  "Which cloud platform pages exist in Build with Claude?", "bedrock,vertex,foundry", "list"),
    Query("F6",  "How many API infrastructure pages are there?", "10", "exact"),
    Query("F7",  "How many SDK overview pages exist?", "7", "exact"),
    Query("F8",  "How many Admin resource groups exist (organizations, users, invites, api_keys, workspaces)?", "5", "exact"),
    Query("F9",  "How many Beta resource groups exist (files, messages, models, skills)?", "4", "exact"),
    Query("F10", "How many Release Notes pages are there?", "2", "exact"),

    # --- Cat G: Page Type Classification (10) ---
    Query("G1",  "What type is the quickstart page in Agent SDK?", "tutorial", "exact"),
    Query("G2",  "What type is the glossary page?", "reference", "exact"),
    Query("G3",  "What type is prompt-caching?", "guide", "exact"),
    Query("G4",  "What type is messages/create?", "api-endpoint", "exact"),
    Query("G5",  "What type is resources/overview?", "overview", "exact"),
    Query("G6",  "What type is web-search-tool?", "tool-reference", "exact"),
    Query("G7",  "What type is reduce-hallucinations?", "best-practices", "exact"),
    Query("G8",  "What type is agent-sdk/python?", "sdk-guide", "exact"),
    Query("G9",  "What type is system-prompts in Release Notes?", "changelog", "exact"),
    Query("G10", "What type is the messages hub page?", "api-hub", "exact"),

    # --- Cat H: Full URL Construction (10) ---
    Query("H1",  "Full URL for prompt-caching?", "https://platform.claude.com/docs/en/build-with-claude/prompt-caching", "substring"),
    Query("H2",  "Full URL for Python SDK messages/create?", "https://platform.claude.com/docs/en/api/python/messages/create", "substring"),
    Query("H3",  "Full URL for rate-limits?", "https://platform.claude.com/docs/en/api/rate-limits", "substring"),
    Query("H4",  "Full URL for mcp-connector?", "https://platform.claude.com/docs/en/agents-and-tools/mcp-connector", "substring"),
    Query("H5",  "Full URL for Agent SDK quickstart?", "https://platform.claude.com/docs/en/agent-sdk/quickstart", "substring"),
    Query("H6",  "Full URL for reduce-hallucinations?", "https://platform.claude.com/docs/en/test-and-evaluate/strengthen-guardrails/reduce-hallucinations", "substring"),
    Query("H7",  "Full URL for models/overview in About Claude?", "https://platform.claude.com/docs/en/about-claude/models/overview", "substring"),
    Query("H8",  "Full URL for the intro page?", "https://platform.claude.com/docs/en/intro", "substring"),
    Query("H9",  "Full URL for admin/workspaces?", "https://platform.claude.com/docs/en/api/admin/workspaces", "substring"),
    Query("H10", "Full URL for beta/skills/versions/create?", "https://platform.claude.com/docs/en/api/beta/skills/versions/create", "substring"),

    # --- Cat I: Cross-Section Navigation (10) ---
    Query("I1",  "List all overview pages across all sections.", "overview", "substring"),
    Query("I2",  "List all tutorial pages.", "intro,get-started,quickstart", "list"),
    Query("I3",  "Which sections contain model-related pages?", "about-claude/models,api/models", "list"),
    Query("I4",  "Which pages relate to streaming?", "streaming,streaming-output,fine-grained", "list"),
    Query("I5",  "Which pages relate to security?", "secure-deployment,mitigate-jailbreaks", "list"),
    Query("I6",  "Which pages relate to costs?", "pricing,cost-tracking,usage-cost-api", "list"),
    Query("I7",  "Which pages relate to batch processing?", "batch-processing,messages/batches", "list"),
    Query("I8",  "Which pages relate to MCP?", "mcp-connector,remote-mcp,agent-sdk/mcp", "list"),
    Query("I9",  "List all pages in the Test & Evaluate section.", "test-and-evaluate", "substring"),
    Query("I10", "Which pages relate to Python?", "python", "substring"),

    # --- Cat J: Edge Cases (10) ---
    Query("J1",  "Find prompt-cacheing page (note the typo).", "prompt-caching", "substring"),
    Query("J2",  "Find msg create endpoint (abbreviated).", "messages/create", "substring"),
    Query("J3",  "Find k8s deployment page.", "not found", "substring"),
    Query("J4",  "Find Claude 4.6 page.", "whats-new-claude-4-6", "substring"),
    Query("J5",  "What does ZDR stand for? Find the page.", "zero-data-retention", "substring"),
    Query("J6",  "Find stop reasons page.", "handling-stop-reasons", "substring"),
    Query("J7",  "Find websearch page (no space/hyphen).", "web-search-tool", "substring"),
    Query("J8",  "Find embeddings page.", "embeddings", "substring"),
    Query("J9",  "Find agent-loop page.", "agent-sdk/agent-loop", "substring"),
    Query("J10", "Find content moderation page.", "content-moderation", "substring"),
]
# fmt: on

CATEGORY_NAMES = {
    "A": "Structure",
    "B": "Direct Lookup",
    "C": "API Navigation",
    "D": "SDK Endpoint Lookup",
    "E": "Natural Language Navigation",
    "F": "Section Enumeration",
    "G": "Page Type Classification",
    "H": "Full URL Construction",
    "I": "Cross-Section Navigation",
    "J": "Edge Cases",
}


# ---------------------------------------------------------------------------
# Batching
# ---------------------------------------------------------------------------

def make_batches(queries: list[Query], size: int = BATCH_SIZE) -> list[list[Query]]:
    return [queries[i : i + size] for i in range(0, len(queries), size)]


# ---------------------------------------------------------------------------
# Codex invocation
# ---------------------------------------------------------------------------

def build_prompt(agents_txt: str, batch: list[Query]) -> str:
    query_lines = "\n".join(f"Q{i+1}: {q.text}" for i, q in enumerate(batch))
    return (
        "Parse this agents.txt and answer queries. "
        'Reply ONLY in format "Q{n}: {answer}" one per line.\n\n'
        f"[AGENTS.TXT]\n{agents_txt}\n\n"
        f"[QUERIES]\n{query_lines}"
    )


def run_codex(prompt: str) -> str:
    """Run a single codex exec call and return stdout."""
    import tempfile
    with tempfile.NamedTemporaryFile(mode='w', suffix='.txt', delete=False) as f:
        f.write(prompt)
        tmppath = f.name
    try:
        cmd = f'codex --dangerously-bypass-approvals-and-sandbox exec --ephemeral "$(cat {tmppath})" 2>&1'
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


def parse_response(raw: str, batch: list[Query]) -> dict[int, str]:
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
    answer = raw_answer.strip().lower()
    expected = query.expected.strip().lower()

    if query.match_type == "exact":
        # For counts: expected number must appear in answer
        return 1.0 if expected in answer else 0.0

    elif query.match_type == "substring":
        if expected in answer:
            return 1.0
        # Partial: check path segments
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

def run_batch(batch_idx: int, batch: list[Query], agents_txt: str) -> list[Result]:
    """Execute a single batch against codex and return graded results."""
    prompt = build_prompt(agents_txt, batch)
    cat = batch[0].id[0]
    cat_name = CATEGORY_NAMES.get(cat, cat)
    print(f"  [Batch {batch_idx + 1}/10] Sending Cat {cat} ({cat_name})...")

    raw = run_codex(prompt)
    answers = parse_response(raw, batch)

    results: list[Result] = []
    for i, q in enumerate(batch):
        ans = answers.get(i + 1, "")
        score = grade(q, ans)
        results.append(Result(query=q, raw_answer=ans, score=score))

    passed = sum(1 for r in results if r.score >= 1.0)
    print(f"  [Batch {batch_idx + 1}/10] Done Cat {cat} -- {passed}/{len(batch)} passed")
    return results


# ---------------------------------------------------------------------------
# Report
# ---------------------------------------------------------------------------

def generate_report(all_results: list[Result], elapsed: float) -> str:
    lines: list[str] = []
    lines.append("# NAVIGATOR.md Codex Test Report\n")
    lines.append(f"- **Date**: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    lines.append(f"- **Model**: {CODEX_MODEL}")
    lines.append(f"- **Total Queries**: {len(all_results)}")

    total_score = sum(r.score for r in all_results)
    total_max = len(all_results)
    pct = (total_score / total_max) * 100 if total_max else 0
    lines.append(f"- **Overall Score**: {total_score:.1f}/{total_max} ({pct:.1f}%)")
    lines.append(f"- **Elapsed**: {elapsed:.1f}s\n")

    # Per-category summary
    cat_results: dict[str, list[Result]] = {}
    for r in all_results:
        cat_results.setdefault(r.query.id[0], []).append(r)

    lines.append("## Category Summary\n")
    lines.append("| Category | Name | Score | Pct |")
    lines.append("|----------|------|-------|-----|")

    for cat in sorted(cat_results):
        rs = cat_results[cat]
        s = sum(r.score for r in rs)
        p = (s / len(rs)) * 100 if rs else 0
        lines.append(f"| {cat} | {CATEGORY_NAMES.get(cat, cat)} | {s:.1f}/{len(rs)} | {p:.0f}% |")

    lines.append("")

    # Detailed results
    lines.append("## Detailed Results\n")
    for cat in sorted(cat_results):
        lines.append(f"### Cat {cat}: {CATEGORY_NAMES.get(cat, cat)}\n")
        lines.append("| ID | Query | Expected | Got | Score |")
        lines.append("|----|-------|----------|-----|-------|")
        for r in cat_results[cat]:
            tag = "PASS" if r.score >= 1.0 else ("partial" if r.score > 0 else "FAIL")
            got = (r.raw_answer[:80].replace("|", "/") or "(empty)")
            exp = r.query.expected[:60].replace("|", "/")
            lines.append(
                f"| {r.query.id} | {r.query.text[:50]} | {exp} | {got} | {tag} ({r.score}) |"
            )
        lines.append("")

    return "\n".join(lines)


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main() -> None:
    print("=" * 60)
    print("NAVIGATOR.md Codex Test Runner")
    print("=" * 60)

    # Load agents.txt
    if not AGENTS_TXT_PATH.exists():
        print(f"ERROR: agents.txt not found at {AGENTS_TXT_PATH}")
        sys.exit(1)
    agents_txt = load_agents_txt()
    print(f"Loaded agents.txt ({len(agents_txt)} chars)")

    # Create batches
    batches = make_batches(TEST_QUERIES, BATCH_SIZE)
    print(f"Created {len(batches)} batches of {BATCH_SIZE} queries each")
    print(f"Running with max_workers={MAX_WORKERS}\n")

    # Execute in parallel
    all_results: list[Result] = []
    start = time.time()

    with ThreadPoolExecutor(max_workers=MAX_WORKERS) as executor:
        futures = {
            executor.submit(run_batch, idx, batch, agents_txt): idx
            for idx, batch in enumerate(batches)
        }
        batch_results: dict[int, list[Result]] = {}
        for future in as_completed(futures):
            idx = futures[future]
            try:
                batch_results[idx] = future.result()
            except Exception as exc:
                print(f"  [Batch {idx + 1}] FAILED: {exc}")
                batch_results[idx] = []

    # Reassemble in order
    for idx in sorted(batch_results):
        all_results.extend(batch_results[idx])

    elapsed = time.time() - start

    # Console summary
    total_score = sum(r.score for r in all_results)
    total_max = len(all_results)
    pct = (total_score / total_max) * 100 if total_max else 0

    print(f"\n{'=' * 60}")
    print(f"RESULTS: {total_score:.1f}/{total_max} ({pct:.1f}%) in {elapsed:.1f}s")
    print(f"{'=' * 60}")

    cat_results: dict[str, list[Result]] = {}
    for r in all_results:
        cat_results.setdefault(r.query.id[0], []).append(r)

    for cat in sorted(cat_results):
        rs = cat_results[cat]
        s = sum(r.score for r in rs)
        print(f"  {cat} ({CATEGORY_NAMES.get(cat, cat)}): {s:.1f}/{len(rs)}")

    # Show failures
    failed = [r for r in all_results if r.score < 1.0]
    if failed:
        print(f"\nFailed/Partial ({len(failed)}):")
        for r in failed:
            print(f"  {r.query.id}: expected={r.query.expected[:50]}, got={r.raw_answer[:50]}, score={r.score}")

    # Save report
    report = generate_report(all_results, elapsed)
    REPORT_PATH.parent.mkdir(parents=True, exist_ok=True)
    with open(REPORT_PATH, "w") as f:
        f.write(report)
    print(f"\nReport saved to {REPORT_PATH}")

    sys.exit(0 if pct >= 70 else 1)


if __name__ == "__main__":
    main()
