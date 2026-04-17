# NAV-AGENT Test Report: gpt-codex × txt

## Metadata

| Field | Value |
|-------|-------|
| Source | gpt-codex |
| Format | txt |
| Model | default |
| Site | GPT Codex Documentation |
| Total Pages | 71 |
| Sections | 40 |
| Queries | 40 |
| Elapsed | 17.2s |
| Timestamp | 2026-04-17 19:32:19 |

## Overall Score

**40.0 / 40 (100.0%) — Grade A**

## Category Summary

| Category | Queries | Score | % |
|----------|---------|-------|---|
| Direct Lookup | 12 | 12.0 | 100% |
| Full URL Construction | 8 | 8.0 | 100% |
| Page Type | 4 | 4.0 | 100% |
| Section Enumeration | 8 | 8.0 | 100% |
| Structure | 8 | 8.0 | 100% |

## Full Results

### Direct Lookup

| ID | Query | Expected | Got | Score |
|----|-------|----------|-----|-------|
| B1 | Find the path for 'Combined Codex docs'. | `/codex/llms-full.txt` | /codex/llms-full.txt | PASS (1.0) |
| B2 | Find the path for 'Agent approvals & security'. | `/codex/agent-approvals-security` | /codex/agent-approvals-security.md | PASS (1.0) |
| B3 | Find the path for 'Automations'. | `/codex/app/automations` | /codex/app/automations.md | PASS (1.0) |
| B4 | Find the path for 'Codex app'. | `/codex/app` | /codex/app.md | PASS (1.0) |
| B5 | Find the path for 'Codex App Server'. | `/codex/app-server` | /codex/app-server.md | PASS (1.0) |
| B6 | Find the path for 'Authentication'. | `/codex/auth` | /codex/auth.md | PASS (1.0) |
| B7 | Find the path for 'Codex CLI'. | `/codex/cli` | /codex/cli.md | PASS (1.0) |
| B8 | Find the path for 'Slash commands in Codex CLI'. | `/codex/cli/slash-commands` | /codex/cli/slash-commands.md | PASS (1.0) |
| B9 | Find the path for 'Cloud environments'. | `/codex/cloud/environments` | /codex/cloud/environments.md | PASS (1.0) |
| B10 | Find the path for 'Codex web'. | `/codex/cloud` | /codex/cloud.md | PASS (1.0) |
| B11 | Find the path for 'Codex for Open Source'. | `/codex/community/codex-for-oss` | /codex/community/codex-for-oss.md | PASS (1.0) |
| B12 | Find the path for 'Customization'. | `/codex/concepts/customization` | /codex/concepts/customization.md | PASS (1.0) |

### Full URL Construction

| ID | Query | Expected | Got | Score |
|----|-------|----------|-----|-------|
| D1 | What is the full URL for 'Combined Codex docs'? | `https://developers.openai.com/codex/codex/llms-full.txt` | `https://developers.openai.com/codex/codex/llms-full.txt` | PASS (1.0) |
| D2 | What is the full URL for 'Agent approvals & securi | `https://developers.openai.com/codex/codex/agent-approvals-se` | `https://developers.openai.com/codex/codex/agent-approvals-security.md` | PASS (1.0) |
| D3 | What is the full URL for 'Codex app commands'? | `https://developers.openai.com/codex/codex/app/commands` | https://developers.openai.com/codex/codex/app/commands.md | PASS (1.0) |
| D4 | What is the full URL for 'Codex App Server'? | `https://developers.openai.com/codex/codex/app-server` | https://developers.openai.com/codex/codex/app-server.md | PASS (1.0) |
| D5 | What is the full URL for 'Authentication'? | `https://developers.openai.com/codex/codex/auth` | https://developers.openai.com/codex/codex/auth.md | PASS (1.0) |
| D6 | What is the full URL for 'Codex CLI'? | `https://developers.openai.com/codex/codex/cli` | https://developers.openai.com/codex/codex/cli.md | PASS (1.0) |
| D7 | What is the full URL for 'Codex web'? | `https://developers.openai.com/codex/codex/cloud` | https://developers.openai.com/codex/codex/cloud.md | PASS (1.0) |
| D8 | What is the full URL for 'Codex for Open Source'? | `https://developers.openai.com/codex/codex/community/codex-fo` | https://developers.openai.com/codex/codex/community/codex-for-oss.md | PASS (1.0) |

### Page Type

| ID | Query | Expected | Got | Score |
|----|-------|----------|-----|-------|
| E1 | What type is the 'Combined Codex docs' page? | `guide` | guide | PASS (1.0) |
| E2 | What type is the 'Agent approvals & security' page | `guide` | guide | PASS (1.0) |
| E3 | What type is the 'Codex app features' page? | `guide` | guide | PASS (1.0) |
| E4 | What type is the 'Codex app settings' page? | `reference` | reference | PASS (1.0) |

### Section Enumeration

| ID | Query | Expected | Got | Score |
|----|-------|----------|-----|-------|
| C1 | List all section names in this document. | `Documentation sets,Agent Approvals Security,App,App Server,A` | Documentation sets, Agent Approvals Security, App, App Server, Auth, Cli, Cloud, | PASS (1.0) |
| C2 | What pages are in the 'App' section? List some slu | `automations,app,settings` | `/codex/app.md`, `/codex/app/automations.md`, `/codex/app/commands.md`, `/codex/ | PASS (1.0) |
| C3 | What pages are in the 'Cli' section? List some slu | `cli,slash-commands,features` | `/codex/cli.md`, `/codex/cli/features.md`, `/codex/cli/reference.md`, `/codex/cl | PASS (1.0) |
| C4 | What pages are in the 'Cloud' section? List some s | `environments,cloud,internet-access` | `/codex/cloud.md`, `/codex/cloud/internet-access.md`, `/codex/cloud/environments | PASS (1.0) |
| C5 | What pages are in the 'Concepts' section? List som | `customization,subagents,cyber-safety` | `customization.md`, `cyber-safety.md`, `sandboxing.md`, `subagents.md` under pre | PASS (1.0) |
| C6 | What pages are in the 'Enterprise' section? List s | `managed-configuration,admin-setup,governance` | `admin-setup.md`, `governance.md`, `managed-configuration.md` under prefix `/cod | PASS (1.0) |
| C7 | What pages are in the 'Guides' section? List some  | `agents-sdk,build-ai-native-engineering-team,agents-md` | `build-ai-native-engineering-team.md`, `agents-md.md`, `agents-sdk.md` under pre | PASS (1.0) |
| C8 | What pages are in the 'Ide' section? List some slu | `ide,slash-commands,features` | `/codex/ide.md`, `/codex/ide/commands.md`, `/codex/ide/features.md`, `/codex/ide | PASS (1.0) |

### Structure

| ID | Query | Expected | Got | Score |
|----|-------|----------|-----|-------|
| A1 | How many total pages are listed in this document? | `71` | 71 | PASS (1.0) |
| A2 | How many sections are listed in this document? | `40` | 40 | PASS (1.0) |
| A3 | How many pages does the 'Documentation sets' secti | `1` | 1 | PASS (1.0) |
| A4 | How many pages does the 'Agent Approvals Security' | `1` | 1 | PASS (1.0) |
| A5 | How many pages does the 'App' section have? | `10` | 10 | PASS (1.0) |
| A6 | How many pages does the 'App Server' section have? | `1` | 1 | PASS (1.0) |
| A7 | How many pages does the 'Auth' section have? | `1` | 1 | PASS (1.0) |
| A8 | How many pages does the 'Cli' section have? | `4` | 4 | PASS (1.0) |
