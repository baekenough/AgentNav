# NAV-AGENT Test Report: gemini-cli × txt

## Metadata

| Field | Value |
|-------|-------|
| Source | gemini-cli |
| Format | txt |
| Model | default |
| Site | Gemini CLI Documentation |
| Total Pages | 90 |
| Sections | 14 |
| Queries | 33 |
| Elapsed | 18.8s |
| Timestamp | 2026-04-17 19:32:41 |

## Overall Score

**31.2 / 33 (94.5%) — Grade A**

## Category Summary

| Category | Queries | Score | % |
|----------|---------|-------|---|
| Direct Lookup | 12 | 10.2 | 85% |
| Full URL Construction | 8 | 8.0 | 100% |
| Page Type | 4 | 4.0 | 100% |
| Section Enumeration | 1 | 1.0 | 100% |
| Structure | 8 | 8.0 | 100% |

## Failed Queries (2)

| ID | Query | Expected | Got | Score |
|----|-------|----------|-----|-------|
| B1 | Find the path for 'Gemini CLI Documentation'. | `/docs/` | / | 0.0 |
| B8 | Find the path for 'CLI Cheatsheet'. | `/docs/cli/cli-reference/` | /docs/reference/commands/ | 0.17 |

## Full Results

### Direct Lookup

| ID | Query | Expected | Got | Score |
|----|-------|----------|-----|-------|
| B1 | Find the path for 'Gemini CLI Documentation'. | `/docs/` | / | FAIL (0.0) |
| B2 | Find the path for 'Gemini 3 on Gemini CLI'. | `/docs/get-started/gemini-3/` | /docs/get-started/gemini-3/ | PASS (1.0) |
| B3 | Find the path for 'Get Started with Agent Skills'. | `/docs/cli/tutorials/skills-getting-started/` | /docs/cli/tutorials/skills-getting-started/ | PASS (1.0) |
| B4 | Find the path for 'File Management'. | `/docs/cli/tutorials/file-management/` | /docs/cli/tutorials/file-management/ | PASS (1.0) |
| B5 | Find the path for 'Checkpointing'. | `/docs/cli/checkpointing/` | /docs/cli/checkpointing/ | PASS (1.0) |
| B6 | Find the path for 'Agent Skills'. | `/docs/cli/skills/` | /docs/cli/skills/ | PASS (1.0) |
| B7 | Find the path for 'Custom Commands'. | `/docs/cli/custom-commands/` | /docs/cli/custom-commands/ | PASS (1.0) |
| B8 | Find the path for 'CLI Cheatsheet'. | `/docs/cli/cli-reference/` | /docs/reference/commands/ | partial (0.17) |
| B9 | Find the path for 'Gemini CLI Core'. | `/docs/core/` | /docs/core/ | PASS (1.0) |
| B10 | Find the path for 'Local Model Routing'. | `/docs/core/local-model-routing/` | /docs/core/local-model-routing/ | PASS (1.0) |
| B11 | Find the path for 'Extensions'. | `/docs/extensions/` | /docs/extensions/ | PASS (1.0) |
| B12 | Find the path for 'Build Extensions'. | `/docs/extensions/writing-extensions/` | /docs/extensions/writing-extensions/ | PASS (1.0) |

### Full URL Construction

| ID | Query | Expected | Got | Score |
|----|-------|----------|-----|-------|
| D1 | What is the full URL for 'Installation'? | `https://geminicli.com/docs/get-started/installation/` | https://geminicli.com/docs/get-started/installation/ | PASS (1.0) |
| D2 | What is the full URL for 'Get Started with Agent S | `https://geminicli.com/docs/cli/tutorials/skills-getting-star` | https://geminicli.com/docs/cli/tutorials/skills-getting-started/ | PASS (1.0) |
| D3 | What is the full URL for 'Headless Mode'? | `https://geminicli.com/docs/cli/headless/` | https://geminicli.com/docs/cli/headless/ | PASS (1.0) |
| D4 | What is the full URL for 'Custom Commands'? | `https://geminicli.com/docs/cli/custom-commands/` | https://geminicli.com/docs/cli/custom-commands/ | PASS (1.0) |
| D5 | What is the full URL for 'Remote Subagents'? | `https://geminicli.com/docs/core/remote-agents/` | https://geminicli.com/docs/core/remote-agents/ | PASS (1.0) |
| D6 | What is the full URL for 'Extensions'? | `https://geminicli.com/docs/extensions/` | https://geminicli.com/docs/extensions/ | PASS (1.0) |
| D7 | What is the full URL for 'Hooks Overview'? | `https://geminicli.com/docs/hooks/` | https://geminicli.com/docs/hooks/ | PASS (1.0) |
| D8 | What is the full URL for 'IDE Integration'? | `https://geminicli.com/docs/ide-integration/` | https://geminicli.com/docs/ide-integration/ | PASS (1.0) |

### Page Type

| ID | Query | Expected | Got | Score |
|----|-------|----------|-----|-------|
| E1 | What type is the 'Installation' page? | `tutorial` | tutorial | PASS (1.0) |
| E2 | What type is the 'Gemini 3 on Gemini CLI' page? | `overview` | overview | PASS (1.0) |
| E3 | What type is the 'Execute Shell Commands' page? | `tutorial` | tutorial | PASS (1.0) |
| E4 | What type is the 'Manage Sessions and History' pag | `tutorial` | tutorial | PASS (1.0) |

### Section Enumeration

| ID | Query | Expected | Got | Score |
|----|-------|----------|-----|-------|
| C1 | List all section names in this document. | `Get Started,Tutorials,CLI Features,Configuration,Core` | Get Started, Tutorials, CLI Features, Configuration, Core, Extensions, Hooks, ID | PASS (1.0) |

### Structure

| ID | Query | Expected | Got | Score |
|----|-------|----------|-----|-------|
| A1 | How many total pages are listed in this document? | `90` | 90 | PASS (1.0) |
| A2 | How many sections are listed in this document? | `14` | 14 | PASS (1.0) |
| A3 | How many pages does the 'Get Started' section have | `5` | 5 | PASS (1.0) |
| A4 | How many pages does the 'Tutorials' section have? | `10` | 10 | PASS (1.0) |
| A5 | How many pages does the 'CLI Features' section hav | `16` | 16 | PASS (1.0) |
| A6 | How many pages does the 'Configuration' section ha | `10` | 10 | PASS (1.0) |
| A7 | How many pages does the 'Core' section have? | `4` | 4 | PASS (1.0) |
| A8 | How many pages does the 'Extensions' section have? | `5` | 5 | PASS (1.0) |
