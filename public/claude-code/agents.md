---
agents_txt_version: "0.2"
format: markdown
schema:
  sections: "## heading = section name"
  subsections: "### heading = subsection grouping"
  pages: "- [title](path) — description {type}"
  page_types: [overview, tutorial, guide, reference, use-case, tool-reference, sdk-guide, api-reference, api-endpoint, api-hub, best-practices, changelog]
  sdk_pattern: "/docs/en/api/{sdk}/{endpoint-path}"
  navigation: "See ## Navigation Guide section"
---

# Anthropic Claude API Documentation

- **URL**: https://platform.claude.com/docs
- **Standard**: agents.txt v0.2 (AgentNav PoC)
- **Total Pages**: 651
- **Last Updated**: 2026-03-22

## Site Overview

| # | Section | Pages | Base Path |
|---|---------|-------|-----------|
| 1 | Introduction | 2 | /docs/en/ |
| 2 | About Claude | 12 | /docs/en/about-claude/ |
| 3 | Build with Claude | 35 | /docs/en/build-with-claude/ |
| 4 | Agents & Tools | 18 | /docs/en/agents-and-tools/ |
| 5 | Agent SDK | 27 | /docs/en/agent-sdk/ |
| 6 | API Reference | 546 | /docs/en/api/ |
| 7 | Test & Evaluate | 8 | /docs/en/test-and-evaluate/ |
| 8 | Release Notes | 2 | /docs/en/release-notes/ |
| 9 | Resources | 1 | /docs/en/resources/ |

---

## Introduction (2 pages)

- [Intro to Claude](/docs/en/intro) {tutorial}
- [Get started with Claude](/docs/en/get-started) {tutorial}

## About Claude (12 pages)

### General

- [Glossary](/docs/en/about-claude/glossary) {reference}
- [Model deprecations](/docs/en/about-claude/model-deprecations) {reference}
- [Pricing](/docs/en/about-claude/pricing) {reference}

### Models

- [Models overview](/docs/en/about-claude/models/overview) {overview}
- [Choosing the right model](/docs/en/about-claude/models/choosing-a-model) {guide}
- [Migration guide](/docs/en/about-claude/models/migration-guide) {guide}
- [What's new in Claude 4.6](/docs/en/about-claude/models/whats-new-claude-4-6) {reference}

### Use Case Guides

- [Guides to common use cases](/docs/en/about-claude/use-case-guides/overview) {overview}
- [Content moderation](/docs/en/about-claude/use-case-guides/content-moderation) {use-case}
- [Customer support agent](/docs/en/about-claude/use-case-guides/customer-support-chat) {use-case}
- [Legal summarization](/docs/en/about-claude/use-case-guides/legal-summarization) {use-case}
- [Ticket routing](/docs/en/about-claude/use-case-guides/ticket-routing) {use-case}

## Build with Claude (35 pages)

### Overview

- [Features overview](/docs/en/build-with-claude/overview) {overview}

### Prompt Engineering

- [Prompt engineering overview](/docs/en/build-with-claude/prompt-engineering/overview) {overview}
- [Prompting best practices](/docs/en/build-with-claude/prompt-engineering/claude-prompting-best-practices) {guide}
- [Console prompting tools](/docs/en/build-with-claude/prompt-engineering/prompting-tools) {guide}

### Input & Output

- [Using the Messages API](/docs/en/build-with-claude/working-with-messages) {guide}
- [Structured outputs](/docs/en/build-with-claude/structured-outputs) {guide}
- [Streaming Messages](/docs/en/build-with-claude/streaming) {guide}
- [Handling stop reasons](/docs/en/build-with-claude/handling-stop-reasons) {guide}
- [Citations](/docs/en/build-with-claude/citations) {guide}
- [Search results](/docs/en/build-with-claude/search-results) {guide}

### Content Types

- [Vision](/docs/en/build-with-claude/vision) {guide}
- [PDF support](/docs/en/build-with-claude/pdf-support) {guide}
- [Files API](/docs/en/build-with-claude/files) {guide}
- [Embeddings](/docs/en/build-with-claude/embeddings) {guide}

### Context & Thinking

- [Context windows](/docs/en/build-with-claude/context-windows) {guide}
- [Context editing](/docs/en/build-with-claude/context-editing) {guide}
- [Compaction](/docs/en/build-with-claude/compaction) {guide}
- [Building with extended thinking](/docs/en/build-with-claude/extended-thinking) {guide}
- [Adaptive thinking](/docs/en/build-with-claude/adaptive-thinking) {guide}
- [Effort](/docs/en/build-with-claude/effort) {guide}

### Performance & Cost

- [Token counting](/docs/en/build-with-claude/token-counting) {guide}
- [Prompt caching](/docs/en/build-with-claude/prompt-caching) {guide}
- [Batch processing](/docs/en/build-with-claude/batch-processing) {guide}
- [Fast mode (research preview)](/docs/en/build-with-claude/fast-mode) {guide}
- [Usage and Cost API](/docs/en/build-with-claude/usage-cost-api) {guide}
- [Multilingual support](/docs/en/build-with-claude/multilingual-support) {guide}

### Platform & Deployment

- [Using Agent Skills with the API](/docs/en/build-with-claude/skills-guide) {guide}
- [Zero Data Retention (ZDR)](/docs/en/build-with-claude/zero-data-retention) {guide}
- [Data residency](/docs/en/build-with-claude/data-residency) {guide}
- [Workspaces](/docs/en/build-with-claude/workspaces) {guide}
- [Admin API overview](/docs/en/build-with-claude/administration-api) {guide}
- [Claude Code Analytics API](/docs/en/build-with-claude/claude-code-analytics-api) {guide}

### Cloud Providers

- [Claude on Amazon Bedrock](/docs/en/build-with-claude/claude-on-amazon-bedrock) {guide}
- [Claude on Vertex AI](/docs/en/build-with-claude/claude-on-vertex-ai) {guide}
- [Claude in Microsoft Foundry](/docs/en/build-with-claude/claude-in-microsoft-foundry) {guide}

## Agents & Tools (18 pages)

### Agent Skills

- [Agent Skills](/docs/en/agents-and-tools/agent-skills/overview) {overview}
- [Get started with Agent Skills in the API](/docs/en/agents-and-tools/agent-skills/quickstart) {tool-reference}
- [Skill authoring best practices](/docs/en/agents-and-tools/agent-skills/best-practices) {tool-reference}
- [Skills for enterprise](/docs/en/agents-and-tools/agent-skills/enterprise) {tool-reference}

### MCP (Model Context Protocol)

- [MCP connector](/docs/en/agents-and-tools/mcp-connector) {tool-reference}
- [Remote MCP servers](/docs/en/agents-and-tools/remote-mcp-servers) {tool-reference}

### Tool Use

- [Tool use with Claude](/docs/en/agents-and-tools/tool-use/overview) {overview}
- [How to implement tool use](/docs/en/agents-and-tools/tool-use/implement-tool-use) {tool-reference}
- [Programmatic tool calling](/docs/en/agents-and-tools/tool-use/programmatic-tool-calling) {tool-reference}
- [Fine-grained tool streaming](/docs/en/agents-and-tools/tool-use/fine-grained-tool-streaming) {tool-reference}
- [Bash tool](/docs/en/agents-and-tools/tool-use/bash-tool) {tool-reference}
- [Code execution tool](/docs/en/agents-and-tools/tool-use/code-execution-tool) {tool-reference}
- [Computer use tool](/docs/en/agents-and-tools/tool-use/computer-use-tool) {tool-reference}
- [Memory tool](/docs/en/agents-and-tools/tool-use/memory-tool) {tool-reference}
- [Text editor tool](/docs/en/agents-and-tools/tool-use/text-editor-tool) {tool-reference}
- [Tool search tool](/docs/en/agents-and-tools/tool-use/tool-search-tool) {tool-reference}
- [Web fetch tool](/docs/en/agents-and-tools/tool-use/web-fetch-tool) {tool-reference}
- [Web search tool](/docs/en/agents-and-tools/tool-use/web-search-tool) {tool-reference}

## Agent SDK (27 pages)

### Getting Started

- [Agent SDK Overview](/docs/en/agent-sdk/overview) {overview}
- [Quickstart](/docs/en/agent-sdk/quickstart) {tutorial}
- [Migration Guide](/docs/en/agent-sdk/migration-guide) {guide}

### SDK Languages

- [Python SDK](/docs/en/agent-sdk/python) {sdk-guide}
- [TypeScript SDK](/docs/en/agent-sdk/typescript) {sdk-guide}
- [TypeScript V2 Preview](/docs/en/agent-sdk/typescript-v2-preview) {sdk-guide}

### Core Concepts

- [Agent Loop](/docs/en/agent-sdk/agent-loop) {guide}
- [Sessions](/docs/en/agent-sdk/sessions) {guide}
- [Subagents](/docs/en/agent-sdk/subagents) {guide}
- [Custom Tools](/docs/en/agent-sdk/custom-tools) {guide}
- [MCP](/docs/en/agent-sdk/mcp) {guide}
- [Permissions](/docs/en/agent-sdk/permissions) {guide}
- [Structured Outputs](/docs/en/agent-sdk/structured-outputs) {guide}
- [User Input](/docs/en/agent-sdk/user-input) {guide}

### Features

- [Claude Code Features](/docs/en/agent-sdk/claude-code-features) {guide}
- [Skills](/docs/en/agent-sdk/skills) {guide}
- [Slash Commands](/docs/en/agent-sdk/slash-commands) {guide}
- [Plugins](/docs/en/agent-sdk/plugins) {guide}
- [Hooks](/docs/en/agent-sdk/hooks) {guide}
- [Modifying System Prompts](/docs/en/agent-sdk/modifying-system-prompts) {guide}
- [Todo Tracking](/docs/en/agent-sdk/todo-tracking) {guide}
- [File Checkpointing](/docs/en/agent-sdk/file-checkpointing) {guide}

### Output & Streaming

- [Streaming Output](/docs/en/agent-sdk/streaming-output) {guide}
- [Streaming vs Single Mode](/docs/en/agent-sdk/streaming-vs-single-mode) {guide}

### Operations

- [Cost Tracking](/docs/en/agent-sdk/cost-tracking) {guide}
- [Hosting](/docs/en/agent-sdk/hosting) {guide}
- [Secure Deployment](/docs/en/agent-sdk/secure-deployment) {guide}

## API Reference (546 pages)

### Infrastructure (10 pages)

- [API Overview](/docs/en/api/overview) {overview}
- [Versions](/docs/en/api/versioning) {api-reference}
- [Errors](/docs/en/api/errors) {api-reference}
- [Rate limits](/docs/en/api/rate-limits) {api-reference}
- [IP addresses](/docs/en/api/ip-addresses) {api-reference}
- [Supported regions](/docs/en/api/supported-regions) {api-reference}
- [Service tiers](/docs/en/api/service-tiers) {api-reference}
- [Client SDKs](/docs/en/api/client-sdks) {api-reference}
- [OpenAI SDK compatibility](/docs/en/api/openai-sdk) {api-reference}
- [Beta headers](/docs/en/api/beta-headers) {api-reference}

### SDK Overviews (7 pages)

- [Python SDK](/docs/en/api/sdks/python) {sdk-guide}
- [TypeScript SDK](/docs/en/api/sdks/typescript) {sdk-guide}
- [Java SDK](/docs/en/api/sdks/java) {sdk-guide}
- [Go SDK](/docs/en/api/sdks/go) {sdk-guide}
- [C# SDK](/docs/en/api/sdks/csharp) {sdk-guide}
- [Ruby SDK](/docs/en/api/sdks/ruby) {sdk-guide}
- [PHP SDK](/docs/en/api/sdks/php) {sdk-guide}

### Messages API (10 pages)

- [Messages](/docs/en/api/messages) — hub {api-hub}
- [Create](/docs/en/api/messages/create) {api-endpoint}
- [Count Tokens](/docs/en/api/messages/count_tokens) {api-endpoint}
- [Batches](/docs/en/api/messages/batches) — hub {api-hub}
- [Create](/docs/en/api/messages/batches/create) {api-endpoint}
- [Retrieve](/docs/en/api/messages/batches/retrieve) {api-endpoint}
- [List](/docs/en/api/messages/batches/list) {api-endpoint}
- [Cancel](/docs/en/api/messages/batches/cancel) {api-endpoint}
- [Results](/docs/en/api/messages/batches/results) {api-endpoint}
- [Delete](/docs/en/api/messages/batches/delete) {api-endpoint}

### Models API (3 pages)

- [Models](/docs/en/api/models) — hub {api-hub}
- [List](/docs/en/api/models/list) {api-endpoint}
- [Retrieve](/docs/en/api/models/retrieve) {api-endpoint}

### Completions API (2 pages, legacy)

- [Completions](/docs/en/api/completions) — hub (legacy) {api-hub}
- [Create](/docs/en/api/completions/create) {api-endpoint}

### Admin API (34 pages)

#### Organizations

- [Admin](/docs/en/api/admin) — hub {api-hub}
- [Organizations](/docs/en/api/admin/organizations) {api-hub}
- [Me](/docs/en/api/admin/organizations/me) {api-endpoint}

#### Users

- [Users](/docs/en/api/admin/users) {api-hub}
- [List](/docs/en/api/admin/users/list) {api-endpoint}
- [Retrieve](/docs/en/api/admin/users/retrieve) {api-endpoint}
- [Update](/docs/en/api/admin/users/update) {api-endpoint}
- [Delete](/docs/en/api/admin/users/delete) {api-endpoint}

#### Invites

- [Invites](/docs/en/api/admin/invites) {api-hub}
- [Create](/docs/en/api/admin/invites/create) {api-endpoint}
- [Retrieve](/docs/en/api/admin/invites/retrieve) {api-endpoint}
- [List](/docs/en/api/admin/invites/list) {api-endpoint}
- [Delete](/docs/en/api/admin/invites/delete) {api-endpoint}

#### API Keys

- [API Keys](/docs/en/api/admin/api_keys) {api-hub}
- [List](/docs/en/api/admin/api_keys/list) {api-endpoint}
- [Retrieve](/docs/en/api/admin/api_keys/retrieve) {api-endpoint}
- [Update](/docs/en/api/admin/api_keys/update) {api-endpoint}

#### Workspaces

- [Workspaces](/docs/en/api/admin/workspaces) {api-hub}
- [Create](/docs/en/api/admin/workspaces/create) {api-endpoint}
- [Retrieve](/docs/en/api/admin/workspaces/retrieve) {api-endpoint}
- [List](/docs/en/api/admin/workspaces/list) {api-endpoint}
- [Update](/docs/en/api/admin/workspaces/update) {api-endpoint}
- [Archive](/docs/en/api/admin/workspaces/archive) {api-endpoint}

#### Workspace Members

- [Members](/docs/en/api/admin/workspaces/members) {api-hub}
- [Create](/docs/en/api/admin/workspaces/members/create) {api-endpoint}
- [Retrieve](/docs/en/api/admin/workspaces/members/retrieve) {api-endpoint}
- [List](/docs/en/api/admin/workspaces/members/list) {api-endpoint}
- [Update](/docs/en/api/admin/workspaces/members/update) {api-endpoint}
- [Delete](/docs/en/api/admin/workspaces/members/delete) {api-endpoint}

#### Reports

- [Cost Report](/docs/en/api/admin/cost_report) {api-hub}
- [Retrieve](/docs/en/api/admin/cost_report/retrieve) {api-endpoint}
- [Usage Report](/docs/en/api/admin/usage_report) {api-hub}
- [Retrieve Messages](/docs/en/api/admin/usage_report/retrieve_messages) {api-endpoint}
- [Retrieve Claude Code](/docs/en/api/admin/usage_report/retrieve_claude_code) {api-endpoint}

### Beta API (30 pages)

- [Beta](/docs/en/api/beta) — hub {api-hub}

#### Beta Files (6 pages)

- [Files](/docs/en/api/beta/files) {api-hub}
- [Upload](/docs/en/api/beta/files/upload) {api-endpoint}
- [List](/docs/en/api/beta/files/list) {api-endpoint}
- [Retrieve Metadata](/docs/en/api/beta/files/retrieve_metadata) {api-endpoint}
- [Download](/docs/en/api/beta/files/download) {api-endpoint}
- [Delete](/docs/en/api/beta/files/delete) {api-endpoint}

#### Beta Messages (10 pages)

- [Messages](/docs/en/api/beta/messages) {api-hub}
- [Create](/docs/en/api/beta/messages/create) {api-endpoint}
- [Count Tokens](/docs/en/api/beta/messages/count_tokens) {api-endpoint}
- [Batches](/docs/en/api/beta/messages/batches) {api-hub}
- [Create](/docs/en/api/beta/messages/batches/create) {api-endpoint}
- [Retrieve](/docs/en/api/beta/messages/batches/retrieve) {api-endpoint}
- [List](/docs/en/api/beta/messages/batches/list) {api-endpoint}
- [Cancel](/docs/en/api/beta/messages/batches/cancel) {api-endpoint}
- [Results](/docs/en/api/beta/messages/batches/results) {api-endpoint}
- [Delete](/docs/en/api/beta/messages/batches/delete) {api-endpoint}

#### Beta Models (3 pages)

- [Models](/docs/en/api/beta/models) {api-hub}
- [List](/docs/en/api/beta/models/list) {api-endpoint}
- [Retrieve](/docs/en/api/beta/models/retrieve) {api-endpoint}

#### Beta Skills (10 pages)

- [Skills](/docs/en/api/beta/skills) {api-hub}
- [Create](/docs/en/api/beta/skills/create) {api-endpoint}
- [Retrieve](/docs/en/api/beta/skills/retrieve) {api-endpoint}
- [List](/docs/en/api/beta/skills/list) {api-endpoint}
- [Delete](/docs/en/api/beta/skills/delete) {api-endpoint}
- [Versions](/docs/en/api/beta/skills/versions) {api-hub}
- [Create](/docs/en/api/beta/skills/versions/create) {api-endpoint}
- [Retrieve](/docs/en/api/beta/skills/versions/retrieve) {api-endpoint}
- [List](/docs/en/api/beta/skills/versions/list) {api-endpoint}
- [Delete](/docs/en/api/beta/skills/versions/delete) {api-endpoint}

### SDK-Specific API References (450 pages)

Each of the 10 SDKs below has 45 pages mirroring the core API structure (messages, models, completions, beta/files, beta/messages, beta/models, beta/skills).

| SDK | Base Path |
|-----|-----------|
| TypeScript | /docs/en/api/typescript/ |
| Python | /docs/en/api/python/ |
| Java | /docs/en/api/java/ |
| Go | /docs/en/api/go/ |
| Kotlin | /docs/en/api/kotlin/ |
| Ruby | /docs/en/api/ruby/ |
| PHP | /docs/en/api/php/ |
| C# | /docs/en/api/csharp/ |
| Terraform | /docs/en/api/terraform/ |
| CLI | /docs/en/api/cli/ |

**URL pattern**: `/docs/en/api/{sdk}/{endpoint-path}`

**Example**: The Python SDK's "Create Message" page is at `/docs/en/api/python/messages/create`.

Each SDK contains these 45 endpoint pages:

| Endpoint Group | Pages | Paths under /docs/en/api/{sdk}/ |
|----------------|-------|--------------------------------|
| Messages | 2 | messages/create, messages/count_tokens |
| Message Batches | 6 | messages/batches/create, .../retrieve, .../list, .../cancel, .../results, .../delete |
| Models | 2 | models/list, models/retrieve |
| Completions | 1 | completions/create |
| Beta Files | 5 | beta/files/upload, .../list, .../retrieve_metadata, .../download, .../delete |
| Beta Messages | 2 | beta/messages/create, beta/messages/count_tokens |
| Beta Message Batches | 6 | beta/messages/batches/create, .../retrieve, .../list, .../cancel, .../results, .../delete |
| Beta Models | 2 | beta/models/list, beta/models/retrieve |
| Beta Skills | 5 | beta/skills/create, .../retrieve, .../list, .../delete, .../versions |
| Beta Skill Versions | 4 | beta/skills/versions/create, .../retrieve, .../list, .../delete |
| Hub/Index Pages | 10 | messages, messages/batches, models, completions, beta/files, beta/messages, beta/messages/batches, beta/models, beta/skills, beta/skills/versions |

**Endpoint types**: Hub/index pages are `{api-hub}`, all action pages (create, list, retrieve, etc.) are `{api-endpoint}`.

## Test & Evaluate (8 pages)

- [Define success criteria and build evaluations](/docs/en/test-and-evaluate/develop-tests) {best-practices}
- [Using the Evaluation Tool](/docs/en/test-and-evaluate/eval-tool) {best-practices}

### Strengthen Guardrails

- [Streaming refusals](/docs/en/test-and-evaluate/strengthen-guardrails/handle-streaming-refusals) {best-practices}
- [Increase output consistency](/docs/en/test-and-evaluate/strengthen-guardrails/increase-consistency) {best-practices}
- [Mitigate jailbreaks and prompt injections](/docs/en/test-and-evaluate/strengthen-guardrails/mitigate-jailbreaks) {best-practices}
- [Reduce hallucinations](/docs/en/test-and-evaluate/strengthen-guardrails/reduce-hallucinations) {best-practices}
- [Reducing latency](/docs/en/test-and-evaluate/strengthen-guardrails/reduce-latency) {best-practices}
- [Reduce prompt leak](/docs/en/test-and-evaluate/strengthen-guardrails/reduce-prompt-leak) {best-practices}

## Release Notes (2 pages)

- [Claude Developer Platform](/docs/en/release-notes/overview) {overview}
- [System Prompts](/docs/en/release-notes/system-prompts) {changelog}

## Resources (1 page)

- [Resources](/docs/en/resources/overview) {overview}

---

## Navigation Guide

### Section Selection by Intent

Use this flowchart to find the right section:

```
What do you need?
|
+-- "What is Claude? What models exist?"
|   -> About Claude (/docs/en/about-claude/)
|
+-- "How do I start using Claude?"
|   -> Introduction (/docs/en/get-started)
|
+-- "How do I build with the API?"
|   +-- Concepts (caching, streaming, tokens, vision)
|   |   -> Build with Claude (/docs/en/build-with-claude/)
|   +-- API endpoints & parameters
|   |   -> API Reference (/docs/en/api/)
|   +-- SDK-specific code examples
|       -> API Reference > SDK pages (/docs/en/api/{sdk}/)
|
+-- "How do I give Claude tools?"
|   -> Agents & Tools (/docs/en/agents-and-tools/)
|
+-- "How do I build an agent with Claude Code SDK?"
|   -> Agent SDK (/docs/en/agent-sdk/)
|
+-- "How do I test or evaluate Claude?"
|   -> Test & Evaluate (/docs/en/test-and-evaluate/)
|
+-- "What's new? What changed?"
|   -> Release Notes (/docs/en/release-notes/)
|
+-- "Pricing, rate limits, regions?"
|   +-- Pricing -> /docs/en/about-claude/pricing
|   +-- Rate limits -> /docs/en/api/rate-limits
|   +-- Regions -> /docs/en/api/supported-regions
|
+-- "Admin, workspaces, organization management?"
|   -> Admin API (/docs/en/api/admin/)
```

### URL Construction Rules

**Static pages**: Use the exact paths listed in the sections above.

**SDK-specific API pages**: Combine the SDK name with the endpoint path.

```
Pattern: /docs/en/api/{sdk}/{endpoint-path}

SDKs: typescript | python | java | go | kotlin | ruby | php | csharp | terraform | cli

Examples:
  /docs/en/api/python/messages/create          — Python: Create Message
  /docs/en/api/typescript/models/list           — TypeScript: List Models
  /docs/en/api/go/beta/files/upload             — Go: Upload File (Beta)
  /docs/en/api/java/beta/skills/versions/create — Java: Create Skill Version (Beta)
```

### Common Task Shortcuts

| Task | Page |
|------|------|
| Send first API request | [Get started with Claude](/docs/en/get-started) |
| Choose the right model | [Choosing the right model](/docs/en/about-claude/models/choosing-a-model) |
| Check pricing | [Pricing](/docs/en/about-claude/pricing) |
| Use tools/function calling | [How to implement tool use](/docs/en/agents-and-tools/tool-use/implement-tool-use) |
| Build an agent | [Agent SDK Overview](/docs/en/agent-sdk/overview) |
| Stream responses | [Streaming Messages](/docs/en/build-with-claude/streaming) |
| Process images | [Vision](/docs/en/build-with-claude/vision) |
| Process PDFs | [PDF support](/docs/en/build-with-claude/pdf-support) |
| Reduce costs | [Prompt caching](/docs/en/build-with-claude/prompt-caching) |
| Batch many requests | [Batch processing](/docs/en/build-with-claude/batch-processing) |
| Handle errors | [Errors](/docs/en/api/errors) |
| Reduce hallucinations | [Reduce hallucinations](/docs/en/test-and-evaluate/strengthen-guardrails/reduce-hallucinations) |
| Manage organization | [Admin](/docs/en/api/admin) |
| Use MCP servers | [MCP connector](/docs/en/agents-and-tools/mcp-connector) |
| Computer use | [Computer use tool](/docs/en/agents-and-tools/tool-use/computer-use-tool) |
| Extended thinking | [Building with extended thinking](/docs/en/build-with-claude/extended-thinking) |
