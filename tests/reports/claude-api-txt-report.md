# NAV-AGENT Test Report: claude-api × txt

## Metadata

| Field | Value |
|-------|-------|
| Source | claude-api |
| Format | txt |
| Model | default |
| Site | Claude API Documentation |
| Total Pages | 1035 |
| Sections | 1 |
| Queries | 10 |
| Elapsed | 24.9s |
| Timestamp | 2026-04-17 19:31:58 |

## Overall Score

**8.0 / 10 (80.1%) — Grade B**

## Category Summary

| Category | Queries | Score | % |
|----------|---------|-------|---|
| Direct Lookup | 2 | 0.7 | 34% |
| Full URL Construction | 1 | 1.0 | 100% |
| Page Type | 2 | 2.0 | 100% |
| Section Enumeration | 2 | 1.3 | 66% |
| Structure | 3 | 3.0 | 100% |

## Failed Queries (3)

| ID | Query | Expected | Got | Score |
|----|-------|----------|-----|-------|
| B1 | Find the path for 'Count tokens in a Message (Beta | `/docs/en/api/typescript/beta/messages/count_tokens` | api/typescript/beta/messages/count_tokens.md | 0.43 |
| B2 | Find the path for 'Streaming Messages'. | `/docs/en/build-with-claude/streaming` | build-with-claude/streaming.md | 0.25 |
| C2 | What pages are in the 'English' section? List some | `count_tokens,streaming,retrieve` | release-notes/overview.md, build-with-claude/overview.md, intro.md, managed-agen | 0.33 |

## Full Results

### Direct Lookup

| ID | Query | Expected | Got | Score |
|----|-------|----------|-----|-------|
| B1 | Find the path for 'Count tokens in a Message (Beta | `/docs/en/api/typescript/beta/messages/count_tokens` | api/typescript/beta/messages/count_tokens.md | partial (0.43) |
| B2 | Find the path for 'Streaming Messages'. | `/docs/en/build-with-claude/streaming` | build-with-claude/streaming.md | partial (0.25) |

### Full URL Construction

| ID | Query | Expected | Got | Score |
|----|-------|----------|-----|-------|
| D1 | What is the full URL for 'List Credentials (Beta)  | `https://platform.claude.com/docs/en/api/typescript/beta/vaul` | https://platform.claude.com/docs/en/api/typescript/beta/vaults/credentials/list. | PASS (1.0) |

### Page Type

| ID | Query | Expected | Got | Score |
|----|-------|----------|-----|-------|
| E1 | What type is the 'Get a Model (Ruby)' page? | `api-endpoint` | api-endpoint | PASS (1.0) |
| E2 | What type is the 'Get Session Resource (Beta) (Pyt | `api-endpoint` | api-endpoint | PASS (1.0) |

### Section Enumeration

| ID | Query | Expected | Got | Score |
|----|-------|----------|-----|-------|
| C1 | List all section names in this document. | `English` | English | PASS (1.0) |
| C2 | What pages are in the 'English' section? List some | `count_tokens,streaming,retrieve` | release-notes/overview.md, build-with-claude/overview.md, intro.md, managed-agen | partial (0.33) |

### Structure

| ID | Query | Expected | Got | Score |
|----|-------|----------|-----|-------|
| A1 | How many total pages are listed in this document? | `1035` | 1035 | PASS (1.0) |
| A2 | How many sections are listed in this document? | `1` | 1 | PASS (1.0) |
| A3 | How many pages does the 'English' section have? | `1035` | 1035 | PASS (1.0) |
