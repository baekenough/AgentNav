---
agents_txt_version: "0.2"
format: markdown
type: site-index
---

# AgentNav — Documentation Sets

- **URL**: https://agentnav.baekenough.com
- **Standard**: agents.txt v0.2
- **Documentation Sets**: 3
- **Total Pages**: 200
- **Last Updated**: 2026-03-28

## Available Documentation Sets

### Claude Code
- **Source**: [code.claude.com](https://code.claude.com)
- **Pages**: 72 | **Sections**: 12
- **Formats**:
  - [agents.json](/claude-code/agents.json)
  - [agents.md](/claude-code/agents.md)
  - [agents.xml](/claude-code/agents.xml)
  - [agents.txt](/claude-code/agents.txt)

### GPT Codex
- **Source**: [developers.openai.com](https://developers.openai.com)
- **Pages**: 71 | **Sections**: 14
- **Formats**:
  - [agents.json](/gpt-codex/agents.json)
  - [agents.md](/gpt-codex/agents.md)
  - [agents.xml](/gpt-codex/agents.xml)
  - [agents.txt](/gpt-codex/agents.txt)

### Gemini CLI
- **Source**: [geminicli.com](https://geminicli.com)
- **Pages**: 57 | **Sections**: 8
- **Formats**:
  - [agents.json](/gemini-cli/agents.json)
  - [agents.md](/gemini-cli/agents.md)
  - [agents.xml](/gemini-cli/agents.xml)
  - [agents.txt](/gemini-cli/agents.txt)

## Navigation Guide

1. Each documentation set provides structured page inventories in 4 formats
2. Use JSON for structured parsing, Markdown for LLM consumption, TXT for minimal tokens
3. Access via `/{set-name}/agents.{format}` (e.g., `/claude-code/agents.json`)
4. Query parameter shortcut: `/?docs={set-name}` redirects to the set's index
