---
agents_txt_version: "0.2"
format: markdown
schema:
  sections: "## heading = section name"
  subsections: "### heading = subsection grouping"
  pages: "- [title](path) {type}"
  page_types: [overview, tutorial, guide, reference, tool-reference, best-practices, changelog]
  navigation: "See ## Navigation Guide section"
---

# Gemini CLI Documentation

- **URL**: https://geminicli.com
- **Standard**: agents.txt v0.2 (AgentNav PoC)
- **Total Pages**: 90
- **Last Updated**: 2026-03-30

## Site Overview

| # | Section | Pages | Base Path |
|---|---------|-------|-----------|
| 1 | Get Started | 5 | /docs/ |
| 2 | Tutorials | 10 | /docs/cli/tutorials/ |
| 3 | CLI Features | 16 | /docs/cli/ |
| 4 | Configuration | 10 | /docs/cli/ |
| 5 | Core | 4 | /docs/core/ |
| 6 | Extensions | 5 | /docs/extensions/ |
| 7 | Hooks | 4 | /docs/hooks/ |
| 8 | IDE Integration | 2 | /docs/ide-integration/ |
| 9 | Tools | 12 | /docs/tools/ |
| 10 | Reference | 5 | /docs/reference/ |
| 11 | Resources | 5 | /docs/resources/ |
| 12 | Admin | 1 | /docs/admin/ |
| 13 | Development | 7 | /docs/ |
| 14 | Releases | 4 | /docs/changelogs/ |

---

## Get Started (5 pages)

- [Get started with Gemini CLI](/docs/get-started/) {tutorial}
- [Installation](/docs/get-started/installation/) {tutorial}
- [Authentication](/docs/get-started/authentication/) {tutorial}
- [Gemini 3 on Gemini CLI](/docs/get-started/gemini-3/) {overview}

- [Gemini CLI Documentation](/docs/) {overview}

## Tutorials (10 pages)

- [File Management](/docs/cli/tutorials/file-management/) {tutorial}
- [Get Started with Agent Skills](/docs/cli/tutorials/skills-getting-started/) {tutorial}
- [Manage Context and Memory](/docs/cli/tutorials/memory-management/) {tutorial}
- [Execute Shell Commands](/docs/cli/tutorials/shell-commands/) {tutorial}
- [Manage Sessions and History](/docs/cli/tutorials/session-management/) {tutorial}
- [Plan Tasks with Todos](/docs/cli/tutorials/task-planning/) {tutorial}
- [Web Search and Fetch](/docs/cli/tutorials/web-tools/) {tutorial}
- [Set Up an MCP Server](/docs/cli/tutorials/mcp-setup/) {tutorial}
- [Automate Tasks](/docs/cli/tutorials/automation/) {tutorial}
- [Plan Mode with Model Steering](/docs/cli/tutorials/plan-mode-steering/) {tutorial}

## CLI Features (16 pages)

- [Agent Skills](/docs/cli/skills/) {guide}
- [Creating Agent Skills](/docs/cli/creating-skills/) {guide}
- [ACP Mode](/docs/cli/acp-mode/) {guide}
- [Checkpointing](/docs/cli/checkpointing/) {guide}
- [Git Worktrees](/docs/cli/git-worktrees/) {guide}
- [Headless Mode](/docs/cli/headless/) {guide}
- [Model Selection](/docs/cli/model/) {guide}
- [Model Routing](/docs/cli/model-routing/) {guide}
- [Model Steering](/docs/cli/model-steering/) {guide}
- [Notifications](/docs/cli/notifications/) {guide}
- [Plan Mode](/docs/cli/plan-mode/) {guide}
- [Rewind](/docs/cli/rewind/) {guide}
- [Sandboxing](/docs/cli/sandbox/) {guide}
- [Session Management](/docs/cli/session-management/) {guide}
- [Observability with OpenTelemetry](/docs/cli/telemetry/) {reference}
- [Token Caching](/docs/cli/token-caching/) {guide}

## Configuration (10 pages)

- [Custom Commands](/docs/cli/custom-commands/) {guide}
- [Enterprise Configuration](/docs/cli/enterprise/) {guide}
- [Ignore Files (.geminiignore)](/docs/cli/gemini-ignore/) {reference}
- [Advanced Model Configuration](/docs/cli/generation-settings/) {reference}
- [Project Context (GEMINI.md)](/docs/cli/gemini-md/) {guide}
- [System Prompt Override](/docs/cli/system-prompt/) {guide}
- [Themes](/docs/cli/themes/) {guide}
- [Trusted Folders](/docs/cli/trusted-folders/) {guide}

- [CLI Cheatsheet](/docs/cli/cli-reference/) {reference}
- [Settings](/docs/cli/settings/) {reference}

## Core (4 pages)

- [Gemini CLI Core](/docs/core/) {overview}
- [Subagents](/docs/core/subagents/) {guide}
- [Remote Subagents](/docs/core/remote-agents/) {guide}
- [Local Model Routing](/docs/core/local-model-routing/) {guide}

## Extensions (5 pages)

- [Extensions](/docs/extensions/) {guide}
- [Extension Best Practices](/docs/extensions/best-practices/) {best-practices}
- [Extension Reference](/docs/extensions/reference/) {reference}
- [Release Extensions](/docs/extensions/releasing/) {guide}
- [Build Extensions](/docs/extensions/writing-extensions/) {guide}

## Hooks (4 pages)

- [Hooks Overview](/docs/hooks/) {guide}
- [Hooks Best Practices](/docs/hooks/best-practices/) {best-practices}
- [Hooks Reference](/docs/hooks/reference/) {reference}
- [Writing Hooks](/docs/hooks/writing-hooks/) {guide}

## IDE Integration (2 pages)

- [IDE Integration](/docs/ide-integration/) {guide}
- [IDE Companion Plugin Spec](/docs/ide-integration/ide-companion-spec/) {reference}

## Tools (12 pages)

- [Tools Reference](/docs/reference/tools/) {tool-reference}
- [Activate Skill Tool](/docs/tools/activate-skill/) {tool-reference}
- [Ask User Tool](/docs/tools/ask-user/) {tool-reference}
- [File System Tools](/docs/tools/file-system/) {tool-reference}
- [Internal Docs Tool](/docs/tools/internal-docs/) {tool-reference}
- [MCP Servers](/docs/tools/mcp-server/) {tool-reference}
- [Memory Tool](/docs/tools/memory/) {tool-reference}
- [Planning Tools](/docs/tools/planning/) {tool-reference}
- [Shell Tool](/docs/tools/shell/) {tool-reference}
- [Todo Tool](/docs/tools/todos/) {tool-reference}
- [Web Fetch Tool](/docs/tools/web-fetch/) {tool-reference}
- [Web Search Tool](/docs/tools/web-search/) {tool-reference}

## Reference (5 pages)

- [CLI Commands](/docs/reference/commands/) {reference}
- [Configuration Reference](/docs/reference/configuration/) {reference}
- [Keyboard Shortcuts](/docs/reference/keyboard-shortcuts/) {reference}
- [Memory Import Processor](/docs/reference/memport/) {tool-reference}
- [Policy Engine](/docs/reference/policy-engine/) {reference}

## Resources (5 pages)

- [FAQ](/docs/resources/faq/) {reference}
- [Quota and Pricing](/docs/resources/quota-and-pricing/) {reference}
- [Terms and Privacy](/docs/resources/tos-privacy/) {reference}
- [Troubleshooting](/docs/resources/troubleshooting/) {guide}
- [Uninstall](/docs/resources/uninstall/) {guide}

## Admin (1 page)

- [Enterprise Admin Controls](/docs/admin/enterprise-controls/) {guide}

## Development (7 pages)

- [Contribution Guide](/docs/contributing/) {guide}
- [Integration Testing](/docs/integration-tests/) {guide}
- [Local Development](/docs/local-development/) {guide}
- [NPM Package Structure](/docs/npm/) {reference}

- [Issue and PR Automation](/docs/issue-and-pr-automation/) {guide}
- [Release Confidence Strategy](/docs/release-confidence/) {guide}
- [Example Proxy Script](/docs/examples/proxy-script/) {tutorial}

## Releases (4 pages)

- [Release Notes](/docs/changelogs/) {changelog}
- [Stable Release (v0.35.2)](/docs/changelogs/latest/) {changelog}
- [Preview Release (v0.36.0-preview.5)](/docs/changelogs/preview/) {changelog}

- [Gemini CLI Releases](/docs/releases/) {changelog}

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
