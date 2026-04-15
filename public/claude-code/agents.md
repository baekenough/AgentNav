---
agents_txt_version: "0.2"
format: markdown
schema:
  sections: "## heading = section name"
  subsections: "### heading = subsection grouping"
  pages: "- [title](path) {type}"
  page_types: [overview, tutorial, guide, reference, tool-reference, sdk-guide, best-practices, changelog]
---

# Claude Code Documentation

- **URL**: https://code.claude.com
- **Standard**: agents.txt v0.2 (AgentNav PoC)
- **Total Pages**: 111
- **Last Updated**: 2026-04-15

## Site Overview

| # | Section | Pages | Base Path |
|---|---------|-------|-----------|
| 1 | Docs | 111 | /docs/en/ |

---

## Docs (111 pages)

- [How the agent loop works](/docs/en/agent-sdk/agent-loop.md) {sdk-guide}
- [Use Claude Code features in the SDK](/docs/en/agent-sdk/claude-code-features.md) {sdk-guide}
- [Track cost and usage](/docs/en/agent-sdk/cost-tracking.md) {sdk-guide}
- [Give Claude custom tools](/docs/en/agent-sdk/custom-tools.md) {sdk-guide}
- [Rewind file changes with checkpointing](/docs/en/agent-sdk/file-checkpointing.md) {sdk-guide}
- [Intercept and control agent behavior with hooks](/docs/en/agent-sdk/hooks.md) {sdk-guide}
- [Hosting the Agent SDK](/docs/en/agent-sdk/hosting.md) {sdk-guide}
- [Connect to external tools with MCP](/docs/en/agent-sdk/mcp.md) {sdk-guide}
- [Migrate to Claude Agent SDK](/docs/en/agent-sdk/migration-guide.md) {sdk-guide}
- [Modifying system prompts](/docs/en/agent-sdk/modifying-system-prompts.md) {sdk-guide}
- [Observability with OpenTelemetry](/docs/en/agent-sdk/observability.md) {sdk-guide}
- [Agent SDK overview](/docs/en/agent-sdk/overview.md) {overview}
- [Configure permissions](/docs/en/agent-sdk/permissions.md) {sdk-guide}
- [Plugins in the SDK](/docs/en/agent-sdk/plugins.md) {sdk-guide}
- [Agent SDK reference - Python](/docs/en/agent-sdk/python.md) {sdk-guide}
- [Quickstart](/docs/en/agent-sdk/quickstart.md) {tutorial}
- [Securely deploying AI agents](/docs/en/agent-sdk/secure-deployment.md) {sdk-guide}
- [Work with sessions](/docs/en/agent-sdk/sessions.md) {sdk-guide}
- [Agent Skills in the SDK](/docs/en/agent-sdk/skills.md) {sdk-guide}
- [Slash Commands in the SDK](/docs/en/agent-sdk/slash-commands.md) {tool-reference}
- [Stream responses in real-time](/docs/en/agent-sdk/streaming-output.md) {sdk-guide}
- [Streaming Input](/docs/en/agent-sdk/streaming-vs-single-mode.md) {sdk-guide}
- [Get structured output from agents](/docs/en/agent-sdk/structured-outputs.md) {sdk-guide}
- [Subagents in the SDK](/docs/en/agent-sdk/subagents.md) {sdk-guide}
- [Todo Lists](/docs/en/agent-sdk/todo-tracking.md) {sdk-guide}
- [Scale to many tools with tool search](/docs/en/agent-sdk/tool-search.md) {sdk-guide}
- [Agent SDK reference - TypeScript](/docs/en/agent-sdk/typescript.md) {sdk-guide}
- [TypeScript SDK V2 interface (preview)](/docs/en/agent-sdk/typescript-v2-preview.md) {sdk-guide}
- [Handle approvals and user input](/docs/en/agent-sdk/user-input.md) {sdk-guide}
- [Orchestrate teams of Claude Code sessions](/docs/en/agent-teams.md) {guide}
- [Claude Code on Amazon Bedrock](/docs/en/amazon-bedrock.md) {guide}
- [Track team usage with analytics](/docs/en/analytics.md) {guide}
- [Authentication](/docs/en/authentication.md) {guide}
- [Best Practices for Claude Code](/docs/en/best-practices.md) {best-practices}
- [Changelog](/docs/en/changelog.md) {changelog}
- [Push events into a running session with channels](/docs/en/channels.md) {guide}
- [Channels reference](/docs/en/channels-reference.md) {guide}
- [Checkpointing](/docs/en/checkpointing.md) {guide}
- [Use Claude Code with Chrome (beta)](/docs/en/chrome.md) {guide}
- [Use Claude Code on the web](/docs/en/claude-code-on-the-web.md) {guide}
- [Explore the .claude directory](/docs/en/claude-directory.md) {guide}
- [CLI reference](/docs/en/cli-reference.md) {tool-reference}
- [Code Review](/docs/en/code-review.md) {guide}
- [Commands](/docs/en/commands.md) {tool-reference}
- [Common workflows](/docs/en/common-workflows.md) {guide}
- [Let Claude use your computer from the CLI](/docs/en/computer-use.md) {guide}
- [Explore the context window](/docs/en/context-window.md) {guide}
- [Manage costs effectively](/docs/en/costs.md) {guide}
- [Data usage](/docs/en/data-usage.md) {guide}
- [Use Claude Code Desktop](/docs/en/desktop.md) {guide}
- [Get started with the desktop app](/docs/en/desktop-quickstart.md) {tutorial}
- [Schedule recurring tasks in Claude Code Desktop](/docs/en/desktop-scheduled-tasks.md) {guide}
- [Development containers](/docs/en/devcontainer.md) {guide}
- [Discover and install prebuilt plugins through marketplaces](/docs/en/discover-plugins.md) {guide}
- [Environment variables](/docs/en/env-vars.md) {guide}
- [Speed up responses with fast mode](/docs/en/fast-mode.md) {guide}
- [Extend Claude Code](/docs/en/features-overview.md) {overview}
- [Fullscreen rendering](/docs/en/fullscreen.md) {guide}
- [Claude Code GitHub Actions](/docs/en/github-actions.md) {guide}
- [Claude Code with GitHub Enterprise Server](/docs/en/github-enterprise-server.md) {guide}
- [Claude Code GitLab CI/CD](/docs/en/gitlab-ci-cd.md) {guide}
- [Claude Code on Google Vertex AI](/docs/en/google-vertex-ai.md) {guide}
- [Run Claude Code programmatically](/docs/en/headless.md) {guide}
- [Hooks reference](/docs/en/hooks.md) {guide}
- [Automate workflows with hooks](/docs/en/hooks-guide.md) {guide}
- [How Claude Code works](/docs/en/how-claude-code-works.md) {guide}
- [Interactive mode](/docs/en/interactive-mode.md) {guide}
- [JetBrains IDEs](/docs/en/jetbrains.md) {guide}
- [Customize keyboard shortcuts](/docs/en/keybindings.md) {guide}
- [Legal and compliance](/docs/en/legal-and-compliance.md) {guide}
- [LLM gateway configuration](/docs/en/llm-gateway.md) {reference}
- [Connect Claude Code to tools via MCP](/docs/en/mcp.md) {guide}
- [How Claude remembers your project](/docs/en/memory.md) {guide}
- [Claude Code on Microsoft Foundry](/docs/en/microsoft-foundry.md) {guide}
- [Model configuration](/docs/en/model-config.md) {reference}
- [Monitoring](/docs/en/monitoring-usage.md) {guide}
- [Enterprise network configuration](/docs/en/network-config.md) {reference}
- [Output styles](/docs/en/output-styles.md) {guide}
- [Claude Code overview](/docs/en/overview.md) {overview}
- [Choose a permission mode](/docs/en/permission-modes.md) {guide}
- [Configure permissions](/docs/en/permissions.md) {guide}
- [Platforms and integrations](/docs/en/platforms.md) {guide}
- [Create and distribute a plugin marketplace](/docs/en/plugin-marketplaces.md) {guide}
- [Create plugins](/docs/en/plugins.md) {guide}
- [Plugins reference](/docs/en/plugins-reference.md) {guide}
- [Quickstart](/docs/en/quickstart.md) {tutorial}
- [Continue local sessions from any device with Remote Control](/docs/en/remote-control.md) {guide}
- [Sandboxing](/docs/en/sandboxing.md) {guide}
- [Run prompts on a schedule](/docs/en/scheduled-tasks.md) {guide}
- [Security](/docs/en/security.md) {guide}
- [Configure server-managed settings](/docs/en/server-managed-settings.md) {reference}
- [Claude Code settings](/docs/en/settings.md) {reference}
- [Advanced setup](/docs/en/setup.md) {guide}
- [Extend Claude with skills](/docs/en/skills.md) {guide}
- [Claude Code in Slack](/docs/en/slack.md) {guide}
- [Customize your status line](/docs/en/statusline.md) {guide}
- [Create custom subagents](/docs/en/sub-agents.md) {guide}
- [Optimize your terminal setup](/docs/en/terminal-config.md) {reference}
- [Enterprise deployment overview](/docs/en/third-party-integrations.md) {overview}
- [Tools reference](/docs/en/tools-reference.md) {guide}
- [Troubleshooting](/docs/en/troubleshooting.md) {guide}
- [Plan in the cloud with ultraplan](/docs/en/ultraplan.md) {guide}
- [Voice dictation](/docs/en/voice-dictation.md) {guide}
- [Use Claude Code in VS Code](/docs/en/vs-code.md) {guide}
- [Get started with Claude Code on the web](/docs/en/web-quickstart.md) {tutorial}
- [Week 13 · March 23–27, 2026](/docs/en/whats-new/2026-w13.md) {changelog}
- [Week 14 · March 30 – April 3, 2026](/docs/en/whats-new/2026-w14.md) {changelog}
- [Week 15 · April 6–10, 2026](/docs/en/whats-new/2026-w15.md) {changelog}
- [What's new](/docs/en/whats-new/index.md) {changelog}
- [Zero data retention](/docs/en/zero-data-retention.md) {guide}
- [Automate work with routines](/docs/en/routines.md) {guide}

