---
agents_txt_version: "0.2"
format: markdown
schema:
  sections: "## heading = section name"
  subsections: "### heading = subsection grouping"
  pages: "- [title](path) {type}"
  page_types: [overview, tutorial, guide, reference, tool-reference, sdk-guide, best-practices]
---

# GPT Codex Documentation

- **URL**: https://developers.openai.com/codex
- **Standard**: agents.txt v0.2 (AgentNav PoC)
- **Total Pages**: 71
- **Last Updated**: 2026-04-15

## Site Overview

| # | Section | Pages | Base Path |
|---|---------|-------|-----------|
| 1 | Documentation sets | 1 | /codex/ |
| 2 | Agent Approvals Security | 1 | /codex/ |
| 3 | App | 10 | /codex/ |
| 4 | App Server | 1 | /codex/ |
| 5 | Auth | 1 | /codex/ |
| 6 | Cli | 4 | /codex/ |
| 7 | Cloud | 3 | /codex/ |
| 8 | Community | 1 | /codex/community/ |
| 9 | Concepts | 4 | /codex/concepts/ |
| 10 | Config Advanced | 1 | /codex/ |
| 11 | Config Basic | 1 | /codex/ |
| 12 | Config Reference | 1 | /codex/ |
| 13 | Config Sample | 1 | /codex/ |
| 14 | Custom Prompts | 1 | /codex/ |
| 15 | Enterprise | 3 | /codex/enterprise/ |
| 16 | Feature Maturity | 1 | /codex/ |
| 17 | Github Action | 1 | /codex/ |
| 18 | Guides | 3 | /codex/guides/ |
| 19 | Hooks | 1 | /codex/ |
| 20 | Ide | 5 | /codex/ |
| 21 | Integrations | 3 | /codex/integrations/ |
| 22 | Learn | 1 | /codex/learn/ |
| 23 | Mcp | 1 | /codex/ |
| 24 | Models | 1 | /codex/ |
| 25 | Noninteractive | 1 | /codex/ |
| 26 | Open Source | 1 | /codex/ |
| 27 | Overview | 1 | /codex/ |
| 28 | Plugins | 2 | /codex/ |
| 29 | Pricing | 1 | /codex/ |
| 30 | Prompting | 1 | /codex/ |
| 31 | Quickstart | 1 | /codex/ |
| 32 | Rules | 1 | /codex/ |
| 33 | Sdk | 1 | /codex/ |
| 34 | Security | 4 | /codex/ |
| 35 | Skills | 1 | /codex/ |
| 36 | Speed | 1 | /codex/ |
| 37 | Subagents | 1 | /codex/ |
| 38 | Videos | 1 | /codex/ |
| 39 | Windows | 1 | /codex/ |
| 40 | Workflows | 1 | /codex/ |

---

## Documentation sets (1 page)

- [Combined Codex docs](/codex/llms-full.txt) {guide}

## Agent Approvals Security (1 page)

- [Agent approvals & security](/codex/agent-approvals-security.md) {guide}

## App (10 pages)

- [Codex app](/codex/app.md) {guide}
- [Automations](/codex/app/automations.md) {guide}
- [Codex app commands](/codex/app/commands.md) {tool-reference}
- [Codex app features](/codex/app/features.md) {guide}
- [Codex app settings](/codex/app/settings.md) {reference}
- [Local environments](/codex/app/local-environments.md) {guide}
- [Review](/codex/app/review.md) {guide}
- [Troubleshooting](/codex/app/troubleshooting.md) {guide}
- [Windows](/codex/app/windows.md) {guide}
- [Worktrees](/codex/app/worktrees.md) {guide}

## App Server (1 page)

- [Codex App Server](/codex/app-server.md) {guide}

## Auth (1 page)

- [Authentication](/codex/auth.md) {guide}

## Cli (4 pages)

- [Codex CLI](/codex/cli.md) {tool-reference}
- [Codex CLI features](/codex/cli/features.md) {tool-reference}
- [Command line options](/codex/cli/reference.md) {tool-reference}
- [Slash commands in Codex CLI](/codex/cli/slash-commands.md) {tool-reference}

## Cloud (3 pages)

- [Codex web](/codex/cloud.md) {guide}
- [Agent internet access](/codex/cloud/internet-access.md) {guide}
- [Cloud environments](/codex/cloud/environments.md) {guide}

## Community (1 page)

- [Codex for Open Source](/codex/community/codex-for-oss.md) {guide}

## Concepts (4 pages)

- [Customization](/codex/concepts/customization.md) {guide}
- [Cyber Safety](/codex/concepts/cyber-safety.md) {guide}
- [Sandbox](/codex/concepts/sandboxing.md) {guide}
- [Subagents](/codex/concepts/subagents.md) {guide}

## Config Advanced (1 page)

- [Advanced Configuration](/codex/config-advanced.md) {reference}

## Config Basic (1 page)

- [Config basics](/codex/config-basic.md) {reference}

## Config Reference (1 page)

- [Configuration Reference](/codex/config-reference.md) {reference}

## Config Sample (1 page)

- [Sample Configuration](/codex/config-sample.md) {reference}

## Custom Prompts (1 page)

- [Custom Prompts](/codex/custom-prompts.md) {guide}

## Enterprise (3 pages)

- [Admin Setup](/codex/enterprise/admin-setup.md) {guide}
- [Governance](/codex/enterprise/governance.md) {guide}
- [Managed configuration](/codex/enterprise/managed-configuration.md) {reference}

## Feature Maturity (1 page)

- [Feature Maturity](/codex/feature-maturity.md) {guide}

## Github Action (1 page)

- [Codex GitHub Action](/codex/github-action.md) {guide}

## Guides (3 pages)

- [Building an AI-Native Engineering Team](/codex/guides/build-ai-native-engineering-team.md) {guide}
- [Custom instructions with AGENTS.md](/codex/guides/agents-md.md) {guide}
- [Use Codex with the Agents SDK](/codex/guides/agents-sdk.md) {sdk-guide}

## Hooks (1 page)

- [Hooks](/codex/hooks.md) {guide}

## Ide (5 pages)

- [Codex IDE extension](/codex/ide.md) {guide}
- [Codex IDE extension commands](/codex/ide/commands.md) {tool-reference}
- [Codex IDE extension features](/codex/ide/features.md) {guide}
- [Codex IDE extension settings](/codex/ide/settings.md) {reference}
- [Codex IDE extension slash commands](/codex/ide/slash-commands.md) {tool-reference}

## Integrations (3 pages)

- [Use Codex in GitHub](/codex/integrations/github.md) {guide}
- [Use Codex in Linear](/codex/integrations/linear.md) {guide}
- [Use Codex in Slack](/codex/integrations/slack.md) {guide}

## Learn (1 page)

### External Resources

- [Best practices](/codex/learn/best-practices.md) {best-practices}

## Mcp (1 page)

- [Model Context Protocol](/codex/mcp.md) {guide}

## Models (1 page)

- [Codex Models](/codex/models.md) {guide}

## Noninteractive (1 page)

- [Non-interactive mode](/codex/noninteractive.md) {guide}

## Open Source (1 page)

- [Open Source](/codex/open-source.md) {guide}

## Overview (1 page)

- [Codex](/codex/overview.md) {overview}

## Plugins (2 pages)

- [Plugins](/codex/plugins.md) {guide}
- [Build plugins](/codex/plugins/build.md) {guide}

## Pricing (1 page)

- [Codex Pricing](/codex/pricing.md) {reference}

## Prompting (1 page)

- [Prompting](/codex/prompting.md) {guide}

## Quickstart (1 page)

- [Quickstart](/codex/quickstart.md) {tutorial}

## Rules (1 page)

- [Rules](/codex/rules.md) {guide}

## Sdk (1 page)

- [Codex SDK](/codex/sdk.md) {sdk-guide}

## Security (4 pages)

- [Codex Security](/codex/security.md) {guide}
- [Codex Security setup](/codex/security/setup.md) {guide}
- [FAQ](/codex/security/faq.md) {guide}
- [Improving the threat model](/codex/security/threat-model.md) {guide}

## Skills (1 page)

- [Agent Skills](/codex/skills.md) {guide}

## Speed (1 page)

- [Speed](/codex/speed.md) {guide}

## Subagents (1 page)

- [Subagents](/codex/subagents.md) {guide}

## Videos (1 page)

- [Videos](/codex/videos.md) {guide}

## Windows (1 page)

- [Windows](/codex/windows.md) {guide}

## Workflows (1 page)

- [Workflows](/codex/workflows.md) {guide}

