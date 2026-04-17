# NAV-AGENT Test Report: claude-code × txt

## Metadata

| Field | Value |
|-------|-------|
| Source | claude-code |
| Format | txt |
| Model | default |
| Site | Claude Code Documentation |
| Total Pages | 111 |
| Sections | 1 |
| Queries | 10 |
| Elapsed | 16.8s |
| Timestamp | 2026-04-17 19:31:29 |

## Overall Score

**9.7 / 10 (96.7%) — Grade A**

## Category Summary

| Category | Queries | Score | % |
|----------|---------|-------|---|
| Direct Lookup | 2 | 2.0 | 100% |
| Full URL Construction | 1 | 1.0 | 100% |
| Page Type | 2 | 2.0 | 100% |
| Section Enumeration | 2 | 1.7 | 84% |
| Structure | 3 | 3.0 | 100% |

## Failed Queries (1)

| ID | Query | Expected | Got | Score |
|----|-------|----------|-----|-------|
| C2 | What pages are in the 'Docs' section? List some sl | `platforms,python,custom-tools` | Examples: `overview.md`, `quickstart.md`, `cli-reference.md`, `platforms.md`, `p | 0.67 |

## Full Results

### Direct Lookup

| ID | Query | Expected | Got | Score |
|----|-------|----------|-----|-------|
| B1 | Find the path for 'Platforms and integrations'. | `/docs/en/platforms` | /docs/en/platforms.md | PASS (1.0) |
| B2 | Find the path for 'Agent SDK reference - Python'. | `/docs/en/agent-sdk/python` | /docs/en/agent-sdk/python.md | PASS (1.0) |

### Full URL Construction

| ID | Query | Expected | Got | Score |
|----|-------|----------|-----|-------|
| D1 | What is the full URL for 'CLI reference'? | `https://code.claude.com/docs/en/cli-reference` | https://code.claude.com/docs/en/cli-reference.md | PASS (1.0) |

### Page Type

| ID | Query | Expected | Got | Score |
|----|-------|----------|-----|-------|
| E1 | What type is the 'Best Practices for Claude Code'  | `best-practices` | best-practices | PASS (1.0) |
| E2 | What type is the 'Checkpointing' page? | `guide` | guide | PASS (1.0) |

### Section Enumeration

| ID | Query | Expected | Got | Score |
|----|-------|----------|-----|-------|
| C1 | List all section names in this document. | `Docs` | Docs | PASS (1.0) |
| C2 | What pages are in the 'Docs' section? List some sl | `platforms,python,custom-tools` | Examples: `overview.md`, `quickstart.md`, `cli-reference.md`, `platforms.md`, `p | partial (0.67) |

### Structure

| ID | Query | Expected | Got | Score |
|----|-------|----------|-----|-------|
| A1 | How many total pages are listed in this document? | `111` | 111 | PASS (1.0) |
| A2 | How many sections are listed in this document? | `1` | 1 | PASS (1.0) |
| A3 | How many pages does the 'Docs' section have? | `111` | 111 | PASS (1.0) |
