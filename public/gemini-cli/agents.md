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
- **Total Pages**: 69
- **Last Updated**: 2026-03-22

## Site Overview

| # | Section | Pages | Base Path |
|---|---------|-------|-----------|
| 1 | Get Started | 7 | /docs/ |
| 2 | Tutorials | 10 | /docs/cli/tutorials/ |
| 3 | Extensions | 5 | /docs/extensions/ |
| 4 | Features | 20 | /docs/ |
| 5 | Configuration | 8 | /docs/cli/ |
| 6 | Reference | 6 | /docs/reference/ |
| 7 | Resources | 5 | /docs/resources/ |
| 8 | Development | 5 | /docs/ |
| 9 | Releases | 3 | /docs/changelogs/ |

---

## Get Started (7 pages)

- [Overview](/docs/) {overview}
- [Quickstart](/docs/get-started/) {tutorial}
- [Installation](/docs/get-started/installation/) {tutorial}
- [Authentication](/docs/get-started/authentication/) {tutorial}
- [Examples](/docs/get-started/examples/) {tutorial}
- [CLI Cheatsheet](/docs/cli/cli-reference/) {reference}
- [Gemini 3 on Gemini CLI](/docs/get-started/gemini-3/) {overview}

## Tutorials (10 pages)

- [File Management](/docs/cli/tutorials/file-management/) {tutorial}
- [Get Started with Agent Skills](/docs/cli/tutorials/skills-getting-started/) {tutorial}
- [Manage Context and Memory](/docs/cli/tutorials/memory-management/) {tutorial}
- [Execute Shell Commands](/docs/cli/tutorials/shell-commands/) {tutorial}
- [Manage Sessions and History](/docs/cli/tutorials/session-management/) {tutorial}
- [Plan Tasks with Todos](/docs/cli/tutorials/task-planning/) {tutorial}
- [Use Plan Mode with Model Steering](/docs/cli/tutorials/plan-mode-steering/) {tutorial}
- [Web Search and Fetch](/docs/cli/tutorials/web-tools/) {tutorial}
- [Set Up an MCP Server](/docs/cli/tutorials/mcp-setup/) {tutorial}
- [Automate Tasks](/docs/cli/tutorials/automation/) {tutorial}

## Extensions (5 pages)

- [Extensions Overview](/docs/extensions/) {overview}
- [Developer Guide: Build Extensions](/docs/extensions/writing-extensions/) {guide}
- [Developer Guide: Best Practices](/docs/extensions/best-practices/) {best-practices}
- [Developer Guide: Releasing](/docs/extensions/releasing/) {guide}
- [Developer Guide: Reference](/docs/extensions/reference/) {reference}

## Features (20 pages)

- [Agent Skills](/docs/cli/skills/) {guide}
- [Checkpointing](/docs/cli/checkpointing/) {guide}
- [Headless Mode](/docs/cli/headless/) {guide}
- [Git Worktrees](/docs/cli/git-worktrees/) {guide}
- [Hooks Overview](/docs/hooks/) {guide}
- [Hooks Reference](/docs/hooks/reference/) {reference}
- [IDE Integration](/docs/ide-integration/) {guide}
- [MCP Servers](/docs/tools/mcp-server/) {guide}
- [Model Routing](/docs/cli/model-routing/) {guide}
- [Model Selection](/docs/cli/model/) {guide}
- [Model Steering](/docs/cli/model-steering/) {guide}
- [Notifications](/docs/cli/notifications/) {guide}
- [Plan Mode](/docs/cli/plan-mode/) {guide}
- [Subagents](/docs/core/subagents/) {guide}
- [Remote Subagents](/docs/core/remote-agents/) {guide}
- [Rewind](/docs/cli/rewind/) {guide}
- [Sandboxing](/docs/cli/sandbox/) {guide}
- [Settings](/docs/cli/settings/) {reference}
- [Telemetry](/docs/cli/telemetry/) {reference}
- [Token Caching](/docs/cli/token-caching/) {guide}

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

## Development (5 pages)

- [Contribution Guide](/docs/contributing/) {guide}
- [Integration Testing](/docs/integration-tests/) {guide}
- [Issue and PR Automation](/docs/issue-and-pr-automation/) {guide}
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
| Getting started | Get Started | Overview, Quickstart, Installation |
| Step-by-step guides | Tutorials | File Management, Shell Commands, MCP Setup |
| Build plugins | Extensions | Extensions Overview, Build Extensions, Best Practices |
| Core features | Features | Agent Skills, Hooks, Subagents, MCP Servers |
| IDE integration | Features | IDE Integration |
| Model options | Features | Model Selection, Model Routing, Model Steering |
| Project setup | Configuration | Project Context (GEMINI.md), Enterprise Configuration |
| Commands and tools | Reference | Command Reference, Tools Reference |
| Troubleshooting | Resources | Troubleshooting, FAQ |
| Contributing | Development | Contribution Guide, Local Development |
| Release history | Releases | Release Notes, Stable Release |

### Search Priority

1. Get Started — overview, quickstart, installation
2. Tutorials — step-by-step guides for common tasks
3. Features — agent skills, hooks, model routing, subagents
4. Configuration — GEMINI.md, enterprise, themes, ignore files
5. Reference — commands, tools, keyboard shortcuts
6. Extensions — build and publish plugins
