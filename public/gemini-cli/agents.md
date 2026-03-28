---
agents_txt_version: "0.2"
format: markdown
schema:
  sections: "## heading = section name"
  subsections: "### heading = subsection grouping"
  pages: "- [title](path) {type}"
  page_types: [overview, tutorial, guide, reference, tool-reference, changelog]
  navigation: "See ## Navigation Guide section"
---

# Gemini CLI Documentation

- **URL**: https://geminicli.com
- **Standard**: agents.txt v0.2 (AgentNav PoC)
- **Total Pages**: 57
- **Last Updated**: 2026-03-28

## Site Overview

| # | Section | Pages | Base Path |
|---|---------|-------|-----------|
| 1 | Get Started | 5 | /docs/ |
| 2 | Use Gemini CLI | 9 | /docs/cli/tutorials/ |
| 3 | Features | 17 | /docs/ |
| 4 | Configuration | 8 | /docs/cli/ |
| 5 | Reference | 6 | /docs/reference/ |
| 6 | Resources | 5 | /docs/resources/ |
| 7 | Development | 4 | /docs/ |
| 8 | Releases | 3 | /docs/changelogs/ |

---

## Get Started (5 pages)

- [Quickstart](/docs/get-started/) {tutorial}
- [Installation](/docs/get-started/installation/) {tutorial}
- [Authentication](/docs/get-started/authentication/) {tutorial}
- [CLI Cheatsheet](/docs/cli/cli-reference/) {reference}
- [Gemini 3 on Gemini CLI](/docs/get-started/gemini-3/) {overview}

## Use Gemini CLI (9 pages)

- [File Management](/docs/cli/tutorials/file-management/) {tutorial}
- [Get Started with Agent Skills](/docs/cli/tutorials/skills-getting-started/) {tutorial}
- [Manage Context and Memory](/docs/cli/tutorials/memory-management/) {tutorial}
- [Execute Shell Commands](/docs/cli/tutorials/shell-commands/) {tutorial}
- [Manage Sessions and History](/docs/cli/tutorials/session-management/) {tutorial}
- [Plan Tasks with Todos](/docs/cli/tutorials/task-planning/) {tutorial}
- [Web Search and Fetch](/docs/cli/tutorials/web-tools/) {tutorial}
- [Set Up an MCP Server](/docs/cli/tutorials/mcp-setup/) {tutorial}
- [Automate Tasks](/docs/cli/tutorials/automation/) {tutorial}

## Features (17 pages)

- [Agent Skills](/docs/cli/skills/) {guide}
- [Checkpointing](/docs/cli/checkpointing/) {guide}
- [Headless Mode](/docs/cli/headless/) {guide}
- [Hooks Overview](/docs/hooks/) {guide}
- [IDE Integration](/docs/ide-integration/) {guide}
- [MCP Servers](/docs/tools/mcp-server/) {guide}
- [Model Routing](/docs/cli/model-routing/) {guide}
- [Model Selection](/docs/cli/model/) {guide}
- [Plan Mode](/docs/cli/plan-mode/) {guide}
- [Subagents](/docs/core/subagents/) {guide}
- [Remote Subagents](/docs/core/remote-agents/) {guide}
- [Rewind](/docs/cli/rewind/) {guide}
- [Sandboxing](/docs/cli/sandbox/) {guide}
- [Settings](/docs/cli/settings/) {reference}
- [Telemetry](/docs/cli/telemetry/) {reference}
- [Token Caching](/docs/cli/token-caching/) {guide}

- [Extensions](/docs/extensions/) {guide}

## Configuration (8 pages)

- [Custom Commands](/docs/cli/custom-commands/) {guide}
- [Enterprise Configuration](/docs/cli/enterprise/) {guide}
- [Ignore Files (.geminiignore)](/docs/cli/gemini-ignore/) {reference}
- [Model Configuration](/docs/cli/generation-settings/) {reference}
- [Project Context (GEMINI.md)](/docs/cli/gemini-md/) {guide}
- [System Prompt Override](/docs/cli/system-prompt/) {guide}
- [Themes](/docs/cli/themes/) {guide}
- [Trusted Folders](/docs/cli/trusted-folders/) {guide}

## Reference (6 pages)

- [Command Reference](/docs/reference/commands/) {reference}
- [Configuration Reference](/docs/reference/configuration/) {reference}
- [Keyboard Shortcuts](/docs/reference/keyboard-shortcuts/) {reference}
- [Memory Import Processor](/docs/reference/memport/) {tool-reference}
- [Policy Engine](/docs/reference/policy-engine/) {reference}
- [Tools Reference](/docs/reference/tools/) {tool-reference}

## Resources (5 pages)

- [FAQ](/docs/resources/faq/) {reference}
- [Quota and Pricing](/docs/resources/quota-and-pricing/) {reference}
- [Terms and Privacy](/docs/resources/tos-privacy/) {reference}
- [Troubleshooting](/docs/resources/troubleshooting/) {guide}
- [Uninstall](/docs/resources/uninstall/) {guide}

## Development (4 pages)

- [Contribution Guide](/docs/contributing/) {guide}
- [Integration Testing](/docs/integration-tests/) {guide}
- [Local Development](/docs/local-development/) {guide}
- [NPM Package Structure](/docs/npm/) {reference}

## Releases (3 pages)

- [Release Notes](/docs/changelogs/) {changelog}
- [Stable Release](/docs/changelogs/latest/) {changelog}
- [Preview Release](/docs/changelogs/preview/) {changelog}

---

## Navigation Guide

### Quick Navigation

| Intent | Best Section | Key Pages |
|--------|-------------|-----------|
| Getting started | Getting Started | Quickstart, Explore |
| How to prompt | Concepts | Prompting |
| Desktop app usage | App | Codex app, Codex app features, Codex app commands |
| VS Code integration | IDE Extension | Codex IDE extension, Codex IDE extension features |
| Terminal usage | CLI | Codex CLI, Codex CLI features, Command line options |
| Cloud/web usage | Web | Codex web, Cloud environments |
| Connect to GitHub/Slack | Integrations | Use Codex in GitHub, Use Codex in Slack, Use Codex in Linear |
| Security setup | Codex Security | Codex Security, Codex Security setup |
| Configure Codex | Configuration | Config basics, Configuration Reference |
| Enterprise setup | Administration | Admin Setup, Governance |
| CI/CD automation | Automation | Non-interactive mode, Codex GitHub Action |
| SDK integration | Automation | Codex SDK, Use Codex with the Agents SDK |
| Release notes | Releases | Codex changelog |

### Search Priority

1. Getting Started — overview, quickstart
2. Concepts — prompting, workflows, models
3. Configuration — config, rules, agents-md, mcp, skills
4. App / CLI — platform-specific features
5. Automation — SDK, non-interactive, github-action
