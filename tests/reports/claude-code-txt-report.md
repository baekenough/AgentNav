# NAV-AGENT Test Report: claude-code × txt

## Metadata

| Field | Value |
|-------|-------|
| Source | claude-code |
| Format | txt |
| Model | default |
| Site | Claude Code Documentation |
| Total Pages | 111 |
| Sections | 80 |
| Queries | 35 |
| Elapsed | 25.7s |
| Timestamp | 2026-04-17 19:57:55 |

## Overall Score

**32.0 / 35 (91.4%) — Grade A**

## Category Summary

| Category | Queries | Score | % |
|----------|---------|-------|---|
| Direct Lookup | 12 | 12.0 | 100% |
| Full URL Construction | 8 | 8.0 | 100% |
| Page Type | 4 | 4.0 | 100% |
| Section Enumeration | 3 | 1.0 | 33% |
| Structure | 8 | 7.0 | 88% |

## Failed Queries (3)

| ID | Query | Expected | Got | Score |
|----|-------|----------|-----|-------|
| A2 | How many sections are listed in this document? | `80` | 1 | 0.0 |
| C1 | List all section names in this document. | `Agent Sdk,Whats New,Agent Teams,Amazon Bedrock,Analytics` | Docs | 0.0 |
| C2 | What pages are in the 'Agent Sdk' section? List so | `streaming-output,custom-tools,agent-loop` | No section named "Agent Sdk" exists; matching pages under `Docs` include `agent- | 0.0 |

## Full Results

### Direct Lookup

| ID | Query | Expected | Got | Score |
|----|-------|----------|-----|-------|
| B1 | Find the path for 'Stream responses in real-time'. | `/docs/en/agent-sdk/streaming-output` | /docs/en/agent-sdk/streaming-output.md | PASS (1.0) |
| B2 | Find the path for 'Give Claude custom tools'. | `/docs/en/agent-sdk/custom-tools` | /docs/en/agent-sdk/custom-tools.md | PASS (1.0) |
| B3 | Find the path for 'Week 13 · March 23–27, 2026'. | `/docs/en/whats-new/2026-w13` | /docs/en/whats-new/2026-w13.md | PASS (1.0) |
| B4 | Find the path for 'What's new'. | `/docs/en/whats-new/index` | /docs/en/whats-new/index.md | PASS (1.0) |
| B5 | Find the path for 'Orchestrate teams of Claude Cod | `/docs/en/agent-teams` | /docs/en/agent-teams.md | PASS (1.0) |
| B6 | Find the path for 'Claude Code on Amazon Bedrock'. | `/docs/en/amazon-bedrock` | /docs/en/amazon-bedrock.md | PASS (1.0) |
| B7 | Find the path for 'Track team usage with analytics | `/docs/en/analytics` | /docs/en/analytics.md | PASS (1.0) |
| B8 | Find the path for 'Authentication'. | `/docs/en/authentication` | /docs/en/authentication.md | PASS (1.0) |
| B9 | Find the path for 'Best Practices for Claude Code' | `/docs/en/best-practices` | /docs/en/best-practices.md | PASS (1.0) |
| B10 | Find the path for 'Changelog'. | `/docs/en/changelog` | /docs/en/changelog.md | PASS (1.0) |
| B11 | Find the path for 'Push events into a running sess | `/docs/en/channels` | /docs/en/channels.md | PASS (1.0) |
| B12 | Find the path for 'Channels reference'. | `/docs/en/channels-reference` | /docs/en/channels-reference.md | PASS (1.0) |

### Full URL Construction

| ID | Query | Expected | Got | Score |
|----|-------|----------|-----|-------|
| D1 | What is the full URL for 'Observability with OpenT | `https://code.claude.com/docs/en/agent-sdk/observability` | https://code.claude.com/docs/en/agent-sdk/observability.md | PASS (1.0) |
| D2 | What is the full URL for 'Week 13 · March 23–27, 2 | `https://code.claude.com/docs/en/whats-new/2026-w13` | https://code.claude.com/docs/en/whats-new/2026-w13.md | PASS (1.0) |
| D3 | What is the full URL for 'Orchestrate teams of Cla | `https://code.claude.com/docs/en/agent-teams` | https://code.claude.com/docs/en/agent-teams.md | PASS (1.0) |
| D4 | What is the full URL for 'Claude Code on Amazon Be | `https://code.claude.com/docs/en/amazon-bedrock` | https://code.claude.com/docs/en/amazon-bedrock.md | PASS (1.0) |
| D5 | What is the full URL for 'Track team usage with an | `https://code.claude.com/docs/en/analytics` | https://code.claude.com/docs/en/analytics.md | PASS (1.0) |
| D6 | What is the full URL for 'Authentication'? | `https://code.claude.com/docs/en/authentication` | https://code.claude.com/docs/en/authentication.md | PASS (1.0) |
| D7 | What is the full URL for 'Best Practices for Claud | `https://code.claude.com/docs/en/best-practices` | https://code.claude.com/docs/en/best-practices.md | PASS (1.0) |
| D8 | What is the full URL for 'Changelog'? | `https://code.claude.com/docs/en/changelog` | https://code.claude.com/docs/en/changelog.md | PASS (1.0) |

### Page Type

| ID | Query | Expected | Got | Score |
|----|-------|----------|-----|-------|
| E1 | What type is the 'Migrate to Claude Agent SDK' pag | `sdk-guide` | sdk-guide | PASS (1.0) |
| E2 | What type is the 'Modifying system prompts' page? | `sdk-guide` | sdk-guide | PASS (1.0) |
| E3 | What type is the 'Week 14 · March 30 – April 3, 20 | `changelog` | changelog | PASS (1.0) |
| E4 | What type is the 'What's new' page? | `changelog` | changelog | PASS (1.0) |

### Section Enumeration

| ID | Query | Expected | Got | Score |
|----|-------|----------|-----|-------|
| C1 | List all section names in this document. | `Agent Sdk,Whats New,Agent Teams,Amazon Bedrock,Analytics` | Docs | FAIL (0.0) |
| C2 | What pages are in the 'Agent Sdk' section? List so | `streaming-output,custom-tools,agent-loop` | No section named "Agent Sdk" exists; matching pages under `Docs` include `agent- | FAIL (0.0) |
| C3 | What pages are in the 'Whats New' section? List so | `2026-w13,index,2026-w14` | No section named "Whats New" exists; matching pages under `Docs` include `whats- | PASS (1.0) |

### Structure

| ID | Query | Expected | Got | Score |
|----|-------|----------|-----|-------|
| A1 | How many total pages are listed in this document? | `111` | 111 | PASS (1.0) |
| A2 | How many sections are listed in this document? | `80` | 1 | FAIL (0.0) |
| A3 | How many pages does the 'Agent Sdk' section have? | `29` | 29 | PASS (1.0) |
| A4 | How many pages does the 'Whats New' section have? | `4` | 4 | PASS (1.0) |
| A5 | How many pages does the 'Agent Teams' section have | `1` | 1 | PASS (1.0) |
| A6 | How many pages does the 'Amazon Bedrock' section h | `1` | 1 | PASS (1.0) |
| A7 | How many pages does the 'Analytics' section have? | `1` | 1 | PASS (1.0) |
| A8 | How many pages does the 'Authentication' section h | `1` | 1 | PASS (1.0) |
