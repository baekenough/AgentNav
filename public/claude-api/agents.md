---
agents_txt_version: "0.2"
format: markdown
schema:
  sections: "## heading = section name"
  subsections: "### heading = subsection grouping"
  pages: "- [title](path) {type}"
  page_types: [overview, tutorial, guide, reference, use-case, sdk-guide, api-endpoint, api-hub, best-practices, changelog]
---

# Anthropic Claude API Documentation

- **URL**: https://platform.claude.com
- **Standard**: agents.txt v0.2 (AgentNav PoC)
- **Total Pages**: 620
- **Last Updated**: 2026-03-28

## Site Overview

| # | Section | Pages | Base Path |
|---|---------|-------|-----------|
| 1 | Getting Started | 2 | /docs/en/ |
| 2 | About Claude | 6 | /docs/en/about-claude/ |
| 3 | Build with Claude | 35 | /docs/en/build-with-claude/ |
| 4 | Agent SDK | 28 | /docs/en/agent-sdk/ |
| 5 | Agents & Tools | 31 | /docs/en/agents-and-tools/ |
| 6 | Test & Evaluate | 8 | /docs/en/test-and-evaluate/ |
| 7 | API Overview & SDKs | 18 | /docs/en/api/ |
| 8 | Messages API | 100 | /docs/en/api/ |
| 9 | Messages API (Beta) | 100 | /docs/en/api/ |
| 10 | Models API | 30 | /docs/en/api/ |
| 11 | Models API (Beta) | 30 | /docs/en/api/ |
| 12 | Completions API | 20 | /docs/en/api/ |
| 13 | Admin API | 33 | /docs/en/api/admin/ |
| 14 | Files API (Beta) | 60 | /docs/en/api/ |
| 15 | Skills API (Beta) | 100 | /docs/en/api/ |
| 16 | Beta API Overview | 10 | /docs/en/api/ |
| 17 | Resources | 8 | /docs/en/ |
| 18 | Release Notes | 1 | /docs/en/release-notes/ |

---

## Getting Started (2 pages)

- [Quickstart](/docs/en/get-started) {tutorial}
- [Intro to Claude](/docs/en/intro) {guide}

## About Claude (6 pages)

- [Models overview](/docs/en/about-claude/models/overview) {overview}
- [Choosing a model](/docs/en/about-claude/models/choosing-a-model) {guide}
- [Migration guide](/docs/en/about-claude/models/migration-guide) {guide}
- [Model deprecations](/docs/en/about-claude/model-deprecations) {guide}
- [Pricing](/docs/en/about-claude/pricing) {guide}
- [What's new in Claude 4.6](/docs/en/about-claude/models/whats-new-claude-4-6) {guide}

## Build with Claude (35 pages)

- [Features overview](/docs/en/build-with-claude/overview) {overview}
- [Overview](/docs/en/build-with-claude/prompt-engineering/overview) {overview}
- [Adaptive thinking](/docs/en/build-with-claude/adaptive-thinking) {guide}
- [Admin API overview](/docs/en/build-with-claude/administration-api) {overview}
- [API and data retention](/docs/en/build-with-claude/api-and-data-retention) {guide}
- [Batch processing](/docs/en/build-with-claude/batch-processing) {guide}
- [Extended thinking](/docs/en/build-with-claude/extended-thinking) {guide}
- [Citations](/docs/en/build-with-claude/citations) {guide}
- [Claude Code Analytics API](/docs/en/build-with-claude/claude-code-analytics-api) {guide}
- [Microsoft Foundry](/docs/en/build-with-claude/claude-in-microsoft-foundry) {guide}
- [Amazon Bedrock](/docs/en/build-with-claude/claude-on-amazon-bedrock) {guide}
- [Vertex AI](/docs/en/build-with-claude/claude-on-vertex-ai) {guide}
- [Compaction](/docs/en/build-with-claude/compaction) {guide}
- [Console prompting tools](/docs/en/build-with-claude/prompt-engineering/prompting-tools) {guide}
- [Context editing](/docs/en/build-with-claude/context-editing) {guide}
- [Context windows](/docs/en/build-with-claude/context-windows) {guide}
- [Data residency](/docs/en/build-with-claude/data-residency) {guide}
- [Effort](/docs/en/build-with-claude/effort) {guide}
- [Embeddings](/docs/en/build-with-claude/embeddings) {guide}
- [Fast mode (beta: research preview)](/docs/en/build-with-claude/fast-mode) {guide}
- [Files API](/docs/en/build-with-claude/files) {guide}
- [Handling stop reasons](/docs/en/build-with-claude/handling-stop-reasons) {guide}
- [Multilingual support](/docs/en/build-with-claude/multilingual-support) {guide}
- [PDF support](/docs/en/build-with-claude/pdf-support) {guide}
- [Prompt caching](/docs/en/build-with-claude/prompt-caching) {guide}
- [Prompting best practices](/docs/en/build-with-claude/prompt-engineering/claude-prompting-best-practices) {best-practices}
- [Search results](/docs/en/build-with-claude/search-results) {guide}
- [Streaming Messages](/docs/en/build-with-claude/streaming) {guide}
- [Structured outputs](/docs/en/build-with-claude/structured-outputs) {guide}
- [Token counting](/docs/en/build-with-claude/token-counting) {guide}
- [Usage and Cost API](/docs/en/build-with-claude/usage-cost-api) {guide}
- [Using Skills with the API](/docs/en/build-with-claude/skills-guide) {guide}
- [Using the Messages API](/docs/en/build-with-claude/working-with-messages) {guide}
- [Vision](/docs/en/build-with-claude/vision) {guide}
- [Workspaces](/docs/en/build-with-claude/workspaces) {guide}

## Agent SDK (28 pages)

- [Overview](/docs/en/agent-sdk/overview) {overview}
- [Quickstart](/docs/en/agent-sdk/quickstart) {tutorial}
- [Python SDK](/docs/en/agent-sdk/python) {guide}
- [TypeScript SDK](/docs/en/agent-sdk/typescript) {guide}
- [Agent Skills in the SDK](/docs/en/agent-sdk/skills) {guide}
- [Handling Permissions](/docs/en/agent-sdk/permissions) {guide}
- [MCP Integration](/docs/en/agent-sdk/mcp) {guide}
- [Structured outputs in the SDK](/docs/en/agent-sdk/structured-outputs) {guide}
- [Define custom tools](/docs/en/agent-sdk/custom-tools) {guide}
- [User approvals and input](/docs/en/agent-sdk/user-input) {guide}
- [Hosting the Agent SDK](/docs/en/agent-sdk/hosting) {guide}
- [How the agent loop works](/docs/en/agent-sdk/agent-loop) {guide}
- [Control execution with hooks](/docs/en/agent-sdk/hooks) {guide}
- [Migration Guide](/docs/en/agent-sdk/migration-guide) {guide}
- [Modifying system prompts](/docs/en/agent-sdk/modifying-system-prompts) {guide}
- [Plugins in the SDK](/docs/en/agent-sdk/plugins) {guide}
- [File checkpointing](/docs/en/agent-sdk/file-checkpointing) {guide}
- [Tool search](/docs/en/agent-sdk/tool-search) {guide}
- [Securely deploying AI agents](/docs/en/agent-sdk/secure-deployment) {guide}
- [Slash Commands in the SDK](/docs/en/agent-sdk/slash-commands) {guide}
- [Stream responses in real-time](/docs/en/agent-sdk/streaming-output) {guide}
- [Streaming Input](/docs/en/agent-sdk/streaming-vs-single-mode) {guide}
- [Subagents in the SDK](/docs/en/agent-sdk/subagents) {guide}
- [Todo Lists](/docs/en/agent-sdk/todo-tracking) {guide}
- [Track cost and usage](/docs/en/agent-sdk/cost-tracking) {guide}
- [TypeScript v2 Preview](/docs/en/agent-sdk/typescript-v2-preview) {guide}
- [Use Claude Code features](/docs/en/agent-sdk/claude-code-features) {guide}
- [Work with sessions](/docs/en/agent-sdk/sessions) {guide}

## Agents & Tools (31 pages)

- [Overview](/docs/en/agents-and-tools/agent-skills/overview) {overview}
- [Quickstart](/docs/en/agents-and-tools/agent-skills/quickstart) {tutorial}
- [Overview](/docs/en/agents-and-tools/tool-use/overview) {overview}
- [Bash tool](/docs/en/agents-and-tools/tool-use/bash-tool) {guide}
- [Claude API skill](/docs/en/agents-and-tools/agent-skills/claude-api-skill) {guide}
- [Code execution tool](/docs/en/agents-and-tools/tool-use/code-execution-tool) {guide}
- [Computer use tool](/docs/en/agents-and-tools/tool-use/computer-use-tool) {guide}
- [Define tools](/docs/en/agents-and-tools/tool-use/define-tools) {guide}
- [Fine-grained tool streaming](/docs/en/agents-and-tools/tool-use/fine-grained-tool-streaming) {guide}
- [Handle tool calls](/docs/en/agents-and-tools/tool-use/handle-tool-calls) {guide}
- [How tool use works](/docs/en/agents-and-tools/tool-use/how-tool-use-works) {guide}
- [Manage tool context](/docs/en/agents-and-tools/tool-use/manage-tool-context) {guide}
- [MCP connector](/docs/en/agents-and-tools/mcp-connector) {guide}
- [Memory tool](/docs/en/agents-and-tools/tool-use/memory-tool) {guide}
- [Parallel tool use](/docs/en/agents-and-tools/tool-use/parallel-tool-use) {guide}
- [Programmatic tool calling](/docs/en/agents-and-tools/tool-use/programmatic-tool-calling) {guide}
- [Remote MCP servers](/docs/en/agents-and-tools/remote-mcp-servers) {guide}
- [Server tools](/docs/en/agents-and-tools/tool-use/server-tools) {guide}
- [Best practices](/docs/en/agents-and-tools/agent-skills/best-practices) {best-practices}
- [Skills for enterprise](/docs/en/agents-and-tools/agent-skills/enterprise) {guide}
- [Strict tool use](/docs/en/agents-and-tools/tool-use/strict-tool-use) {guide}
- [Text editor tool](/docs/en/agents-and-tools/tool-use/text-editor-tool) {guide}
- [Tool combinations](/docs/en/agents-and-tools/tool-use/tool-combinations) {guide}
- [Tool reference](/docs/en/agents-and-tools/tool-use/tool-reference) {reference}
- [Tool Runner (SDK)](/docs/en/agents-and-tools/tool-use/tool-runner) {guide}
- [Tool search](/docs/en/agents-and-tools/tool-use/tool-search-tool) {guide}
- [Tool use with prompt caching](/docs/en/agents-and-tools/tool-use/tool-use-with-prompt-caching) {guide}
- [Troubleshooting](/docs/en/agents-and-tools/tool-use/troubleshooting-tool-use) {guide}
- [Tutorial: Build a tool-using agent](/docs/en/agents-and-tools/tool-use/build-a-tool-using-agent) {guide}
- [Web fetch tool](/docs/en/agents-and-tools/tool-use/web-fetch-tool) {guide}
- [Web search tool](/docs/en/agents-and-tools/tool-use/web-search-tool) {guide}

## Test & Evaluate (8 pages)

- [Define success and build evaluations](/docs/en/test-and-evaluate/develop-tests) {guide}
- [Increase output consistency](/docs/en/test-and-evaluate/strengthen-guardrails/increase-consistency) {guide}
- [Mitigate jailbreaks](/docs/en/test-and-evaluate/strengthen-guardrails/mitigate-jailbreaks) {guide}
- [Reduce hallucinations](/docs/en/test-and-evaluate/strengthen-guardrails/reduce-hallucinations) {guide}
- [Reduce prompt leak](/docs/en/test-and-evaluate/strengthen-guardrails/reduce-prompt-leak) {guide}
- [Reducing latency](/docs/en/test-and-evaluate/strengthen-guardrails/reduce-latency) {guide}
- [Streaming refusals](/docs/en/test-and-evaluate/strengthen-guardrails/handle-streaming-refusals) {guide}
- [Using the Evaluation Tool](/docs/en/test-and-evaluate/eval-tool) {guide}

## API Overview & SDKs (18 pages)

- [API overview](/docs/en/api/overview) {overview}
- [Admin](/docs/en/api/admin) — hub {guide}
- [Beta headers](/docs/en/api/beta-headers) {guide}
- [C# SDK](/docs/en/api/sdks/csharp) {sdk-guide}
- [Overview](/docs/en/api/client-sdks) {sdk-guide}
- [Errors](/docs/en/api/errors) {guide}
- [Go SDK](/docs/en/api/sdks/go) {sdk-guide}
- [IP addresses](/docs/en/api/ip-addresses) {guide}
- [Java SDK](/docs/en/api/sdks/java) {sdk-guide}
- [OpenAI SDK compatibility](/docs/en/api/openai-sdk) {guide}
- [PHP SDK](/docs/en/api/sdks/php) {sdk-guide}
- [Python SDK](/docs/en/api/sdks/python) {sdk-guide}
- [Rate limits](/docs/en/api/rate-limits) {guide}
- [Ruby SDK](/docs/en/api/sdks/ruby) {sdk-guide}
- [Service tiers](/docs/en/api/service-tiers) {guide}
- [Supported regions](/docs/en/api/supported-regions) {guide}
- [TypeScript SDK](/docs/en/api/sdks/typescript) {sdk-guide}
- [Versions](/docs/en/api/versioning) {guide}

## Messages API (100 pages)

- [Batches](/docs/en/api/messages/batches) — hub {api-hub}
- [Batches (cli)](/docs/en/api/cli/messages/batches) {guide}
- [Batches (csharp)](/docs/en/api/csharp/messages/batches) {guide}
- [Batches (Go)](/docs/en/api/go/messages/batches) {guide}
- [Batches (Java)](/docs/en/api/java/messages/batches) {guide}
- [Batches (php)](/docs/en/api/php/messages/batches) {guide}
- [Batches (Python)](/docs/en/api/python/messages/batches) {guide}
- [Batches (Ruby)](/docs/en/api/ruby/messages/batches) {guide}
- [Batches (terraform)](/docs/en/api/terraform/messages/batches) {guide}
- [Batches (TypeScript)](/docs/en/api/typescript/messages/batches) {guide}
- [Cancel a Message Batch](/docs/en/api/messages/batches/cancel) {api-endpoint}
- [Cancel a Message Batch (cli)](/docs/en/api/cli/messages/batches/cancel) {api-endpoint}
- [Cancel a Message Batch (csharp)](/docs/en/api/csharp/messages/batches/cancel) {api-endpoint}
- [Cancel a Message Batch (Go)](/docs/en/api/go/messages/batches/cancel) {api-endpoint}
- [Cancel a Message Batch (Java)](/docs/en/api/java/messages/batches/cancel) {api-endpoint}
- [Cancel a Message Batch (php)](/docs/en/api/php/messages/batches/cancel) {api-endpoint}
- [Cancel a Message Batch (Python)](/docs/en/api/python/messages/batches/cancel) {api-endpoint}
- [Cancel a Message Batch (Ruby)](/docs/en/api/ruby/messages/batches/cancel) {api-endpoint}
- [Cancel a Message Batch (terraform)](/docs/en/api/terraform/messages/batches/cancel) {api-endpoint}
- [Cancel a Message Batch (TypeScript)](/docs/en/api/typescript/messages/batches/cancel) {api-endpoint}
- [Count tokens in a Message](/docs/en/api/messages/count_tokens) {api-endpoint}
- [Count tokens in a Message (cli)](/docs/en/api/cli/messages/count_tokens) {api-endpoint}
- [Count tokens in a Message (csharp)](/docs/en/api/csharp/messages/count_tokens) {api-endpoint}
- [Count tokens in a Message (Go)](/docs/en/api/go/messages/count_tokens) {api-endpoint}
- [Count tokens in a Message (Java)](/docs/en/api/java/messages/count_tokens) {api-endpoint}
- [Count tokens in a Message (php)](/docs/en/api/php/messages/count_tokens) {api-endpoint}
- [Count tokens in a Message (Python)](/docs/en/api/python/messages/count_tokens) {api-endpoint}
- [Count tokens in a Message (Ruby)](/docs/en/api/ruby/messages/count_tokens) {api-endpoint}
- [Count tokens in a Message (terraform)](/docs/en/api/terraform/messages/count_tokens) {api-endpoint}
- [Count tokens in a Message (TypeScript)](/docs/en/api/typescript/messages/count_tokens) {api-endpoint}
- [Create a Message](/docs/en/api/messages/create) {api-endpoint}
- [Create a Message (cli)](/docs/en/api/cli/messages/create) {api-endpoint}
- [Create a Message (csharp)](/docs/en/api/csharp/messages/create) {api-endpoint}
- [Create a Message (Go)](/docs/en/api/go/messages/create) {api-endpoint}
- [Create a Message (Java)](/docs/en/api/java/messages/create) {api-endpoint}
- [Create a Message (php)](/docs/en/api/php/messages/create) {api-endpoint}
- [Create a Message (Python)](/docs/en/api/python/messages/create) {api-endpoint}
- [Create a Message (Ruby)](/docs/en/api/ruby/messages/create) {api-endpoint}
- [Create a Message (terraform)](/docs/en/api/terraform/messages/create) {api-endpoint}
- [Create a Message (TypeScript)](/docs/en/api/typescript/messages/create) {api-endpoint}
- [Create a Message Batch](/docs/en/api/messages/batches/create) {api-endpoint}
- [Create a Message Batch (cli)](/docs/en/api/cli/messages/batches/create) {api-endpoint}
- [Create a Message Batch (csharp)](/docs/en/api/csharp/messages/batches/create) {api-endpoint}
- [Create a Message Batch (Go)](/docs/en/api/go/messages/batches/create) {api-endpoint}
- [Create a Message Batch (Java)](/docs/en/api/java/messages/batches/create) {api-endpoint}
- [Create a Message Batch (php)](/docs/en/api/php/messages/batches/create) {api-endpoint}
- [Create a Message Batch (Python)](/docs/en/api/python/messages/batches/create) {api-endpoint}
- [Create a Message Batch (Ruby)](/docs/en/api/ruby/messages/batches/create) {api-endpoint}
- [Create a Message Batch (terraform)](/docs/en/api/terraform/messages/batches/create) {api-endpoint}
- [Create a Message Batch (TypeScript)](/docs/en/api/typescript/messages/batches/create) {api-endpoint}
- [Delete a Message Batch](/docs/en/api/messages/batches/delete) {api-endpoint}
- [Delete a Message Batch (cli)](/docs/en/api/cli/messages/batches/delete) {api-endpoint}
- [Delete a Message Batch (csharp)](/docs/en/api/csharp/messages/batches/delete) {api-endpoint}
- [Delete a Message Batch (Go)](/docs/en/api/go/messages/batches/delete) {api-endpoint}
- [Delete a Message Batch (Java)](/docs/en/api/java/messages/batches/delete) {api-endpoint}
- [Delete a Message Batch (php)](/docs/en/api/php/messages/batches/delete) {api-endpoint}
- [Delete a Message Batch (Python)](/docs/en/api/python/messages/batches/delete) {api-endpoint}
- [Delete a Message Batch (Ruby)](/docs/en/api/ruby/messages/batches/delete) {api-endpoint}
- [Delete a Message Batch (terraform)](/docs/en/api/terraform/messages/batches/delete) {api-endpoint}
- [Delete a Message Batch (TypeScript)](/docs/en/api/typescript/messages/batches/delete) {api-endpoint}
- [List Message Batches](/docs/en/api/messages/batches/list) {api-endpoint}
- [List Message Batches (cli)](/docs/en/api/cli/messages/batches/list) {api-endpoint}
- [List Message Batches (csharp)](/docs/en/api/csharp/messages/batches/list) {api-endpoint}
- [List Message Batches (Go)](/docs/en/api/go/messages/batches/list) {api-endpoint}
- [List Message Batches (Java)](/docs/en/api/java/messages/batches/list) {api-endpoint}
- [List Message Batches (php)](/docs/en/api/php/messages/batches/list) {api-endpoint}
- [List Message Batches (Python)](/docs/en/api/python/messages/batches/list) {api-endpoint}
- [List Message Batches (Ruby)](/docs/en/api/ruby/messages/batches/list) {api-endpoint}
- [List Message Batches (terraform)](/docs/en/api/terraform/messages/batches/list) {api-endpoint}
- [List Message Batches (TypeScript)](/docs/en/api/typescript/messages/batches/list) {api-endpoint}
- [Messages](/docs/en/api/messages) — hub {api-hub}
- [Messages (cli)](/docs/en/api/cli/messages) {api-hub}
- [Messages (csharp)](/docs/en/api/csharp/messages) {api-hub}
- [Messages (Go)](/docs/en/api/go/messages) {api-hub}
- [Messages (Java)](/docs/en/api/java/messages) {api-hub}
- [Messages (php)](/docs/en/api/php/messages) {api-hub}
- [Messages (Python)](/docs/en/api/python/messages) {api-hub}
- [Messages (Ruby)](/docs/en/api/ruby/messages) {api-hub}
- [Messages (terraform)](/docs/en/api/terraform/messages) {api-hub}
- [Messages (TypeScript)](/docs/en/api/typescript/messages) {api-hub}
- [Retrieve a Message Batch](/docs/en/api/messages/batches/retrieve) {api-endpoint}
- [Retrieve a Message Batch (cli)](/docs/en/api/cli/messages/batches/retrieve) {api-endpoint}
- [Retrieve a Message Batch (csharp)](/docs/en/api/csharp/messages/batches/retrieve) {api-endpoint}
- [Retrieve a Message Batch (Go)](/docs/en/api/go/messages/batches/retrieve) {api-endpoint}
- [Retrieve a Message Batch (Java)](/docs/en/api/java/messages/batches/retrieve) {api-endpoint}
- [Retrieve a Message Batch (php)](/docs/en/api/php/messages/batches/retrieve) {api-endpoint}
- [Retrieve a Message Batch (Python)](/docs/en/api/python/messages/batches/retrieve) {api-endpoint}
- [Retrieve a Message Batch (Ruby)](/docs/en/api/ruby/messages/batches/retrieve) {api-endpoint}
- [Retrieve a Message Batch (terraform)](/docs/en/api/terraform/messages/batches/retrieve) {api-endpoint}
- [Retrieve a Message Batch (TypeScript)](/docs/en/api/typescript/messages/batches/retrieve) {api-endpoint}
- [Retrieve Message Batch results](/docs/en/api/messages/batches/results) {api-endpoint}
- [Retrieve Message Batch results (cli)](/docs/en/api/cli/messages/batches/results) {api-endpoint}
- [Retrieve Message Batch results (csharp)](/docs/en/api/csharp/messages/batches/results) {api-endpoint}
- [Retrieve Message Batch results (Go)](/docs/en/api/go/messages/batches/results) {api-endpoint}
- [Retrieve Message Batch results (Java)](/docs/en/api/java/messages/batches/results) {api-endpoint}
- [Retrieve Message Batch results (php)](/docs/en/api/php/messages/batches/results) {api-endpoint}
- [Retrieve Message Batch results (Python)](/docs/en/api/python/messages/batches/results) {api-endpoint}
- [Retrieve Message Batch results (Ruby)](/docs/en/api/ruby/messages/batches/results) {api-endpoint}
- [Retrieve Message Batch results (terraform)](/docs/en/api/terraform/messages/batches/results) {api-endpoint}
- [Retrieve Message Batch results (TypeScript)](/docs/en/api/typescript/messages/batches/results) {api-endpoint}

## Messages API (Beta) (100 pages)

- [Batches (Beta)](/docs/en/api/beta/messages/batches) {guide}
- [Batches (Beta) (cli)](/docs/en/api/cli/beta/messages/batches) {guide}
- [Batches (Beta) (csharp)](/docs/en/api/csharp/beta/messages/batches) {guide}
- [Batches (Beta) (Go)](/docs/en/api/go/beta/messages/batches) {guide}
- [Batches (Beta) (Java)](/docs/en/api/java/beta/messages/batches) {guide}
- [Batches (Beta) (php)](/docs/en/api/php/beta/messages/batches) {guide}
- [Batches (Beta) (Python)](/docs/en/api/python/beta/messages/batches) {guide}
- [Batches (Beta) (Ruby)](/docs/en/api/ruby/beta/messages/batches) {guide}
- [Batches (Beta) (terraform)](/docs/en/api/terraform/beta/messages/batches) {guide}
- [Batches (Beta) (TypeScript)](/docs/en/api/typescript/beta/messages/batches) {guide}
- [Cancel a Message Batch (Beta)](/docs/en/api/beta/messages/batches/cancel) {api-endpoint}
- [Cancel a Message Batch (Beta) (cli)](/docs/en/api/cli/beta/messages/batches/cancel) {api-endpoint}
- [Cancel a Message Batch (Beta) (csharp)](/docs/en/api/csharp/beta/messages/batches/cancel) {api-endpoint}
- [Cancel a Message Batch (Beta) (Go)](/docs/en/api/go/beta/messages/batches/cancel) {api-endpoint}
- [Cancel a Message Batch (Beta) (Java)](/docs/en/api/java/beta/messages/batches/cancel) {api-endpoint}
- [Cancel a Message Batch (Beta) (php)](/docs/en/api/php/beta/messages/batches/cancel) {api-endpoint}
- [Cancel a Message Batch (Beta) (Python)](/docs/en/api/python/beta/messages/batches/cancel) {api-endpoint}
- [Cancel a Message Batch (Beta) (Ruby)](/docs/en/api/ruby/beta/messages/batches/cancel) {api-endpoint}
- [Cancel a Message Batch (Beta) (terraform)](/docs/en/api/terraform/beta/messages/batches/cancel) {api-endpoint}
- [Cancel a Message Batch (Beta) (TypeScript)](/docs/en/api/typescript/beta/messages/batches/cancel) {api-endpoint}
- [Count tokens in a Message (Beta)](/docs/en/api/beta/messages/count_tokens) {api-endpoint}
- [Count tokens in a Message (Beta) (cli)](/docs/en/api/cli/beta/messages/count_tokens) {api-endpoint}
- [Count tokens in a Message (Beta) (csharp)](/docs/en/api/csharp/beta/messages/count_tokens) {api-endpoint}
- [Count tokens in a Message (Beta) (Go)](/docs/en/api/go/beta/messages/count_tokens) {api-endpoint}
- [Count tokens in a Message (Beta) (Java)](/docs/en/api/java/beta/messages/count_tokens) {api-endpoint}
- [Count tokens in a Message (Beta) (php)](/docs/en/api/php/beta/messages/count_tokens) {api-endpoint}
- [Count tokens in a Message (Beta) (Python)](/docs/en/api/python/beta/messages/count_tokens) {api-endpoint}
- [Count tokens in a Message (Beta) (Ruby)](/docs/en/api/ruby/beta/messages/count_tokens) {api-endpoint}
- [Count tokens in a Message (Beta) (terraform)](/docs/en/api/terraform/beta/messages/count_tokens) {api-endpoint}
- [Count tokens in a Message (Beta) (TypeScript)](/docs/en/api/typescript/beta/messages/count_tokens) {api-endpoint}
- [Create a Message (Beta)](/docs/en/api/beta/messages/create) {api-endpoint}
- [Create a Message (Beta) (cli)](/docs/en/api/cli/beta/messages/create) {api-endpoint}
- [Create a Message (Beta) (csharp)](/docs/en/api/csharp/beta/messages/create) {api-endpoint}
- [Create a Message (Beta) (Go)](/docs/en/api/go/beta/messages/create) {api-endpoint}
- [Create a Message (Beta) (Java)](/docs/en/api/java/beta/messages/create) {api-endpoint}
- [Create a Message (Beta) (php)](/docs/en/api/php/beta/messages/create) {api-endpoint}
- [Create a Message (Beta) (Python)](/docs/en/api/python/beta/messages/create) {api-endpoint}
- [Create a Message (Beta) (Ruby)](/docs/en/api/ruby/beta/messages/create) {api-endpoint}
- [Create a Message (Beta) (terraform)](/docs/en/api/terraform/beta/messages/create) {api-endpoint}
- [Create a Message (Beta) (TypeScript)](/docs/en/api/typescript/beta/messages/create) {api-endpoint}
- [Create a Message Batch (Beta)](/docs/en/api/beta/messages/batches/create) {api-endpoint}
- [Create a Message Batch (Beta) (cli)](/docs/en/api/cli/beta/messages/batches/create) {api-endpoint}
- [Create a Message Batch (Beta) (csharp)](/docs/en/api/csharp/beta/messages/batches/create) {api-endpoint}
- [Create a Message Batch (Beta) (Go)](/docs/en/api/go/beta/messages/batches/create) {api-endpoint}
- [Create a Message Batch (Beta) (Java)](/docs/en/api/java/beta/messages/batches/create) {api-endpoint}
- [Create a Message Batch (Beta) (php)](/docs/en/api/php/beta/messages/batches/create) {api-endpoint}
- [Create a Message Batch (Beta) (Python)](/docs/en/api/python/beta/messages/batches/create) {api-endpoint}
- [Create a Message Batch (Beta) (Ruby)](/docs/en/api/ruby/beta/messages/batches/create) {api-endpoint}
- [Create a Message Batch (Beta) (terraform)](/docs/en/api/terraform/beta/messages/batches/create) {api-endpoint}
- [Create a Message Batch (Beta) (TypeScript)](/docs/en/api/typescript/beta/messages/batches/create) {api-endpoint}
- [Delete a Message Batch (Beta)](/docs/en/api/beta/messages/batches/delete) {api-endpoint}
- [Delete a Message Batch (Beta) (cli)](/docs/en/api/cli/beta/messages/batches/delete) {api-endpoint}
- [Delete a Message Batch (Beta) (csharp)](/docs/en/api/csharp/beta/messages/batches/delete) {api-endpoint}
- [Delete a Message Batch (Beta) (Go)](/docs/en/api/go/beta/messages/batches/delete) {api-endpoint}
- [Delete a Message Batch (Beta) (Java)](/docs/en/api/java/beta/messages/batches/delete) {api-endpoint}
- [Delete a Message Batch (Beta) (php)](/docs/en/api/php/beta/messages/batches/delete) {api-endpoint}
- [Delete a Message Batch (Beta) (Python)](/docs/en/api/python/beta/messages/batches/delete) {api-endpoint}
- [Delete a Message Batch (Beta) (Ruby)](/docs/en/api/ruby/beta/messages/batches/delete) {api-endpoint}
- [Delete a Message Batch (Beta) (terraform)](/docs/en/api/terraform/beta/messages/batches/delete) {api-endpoint}
- [Delete a Message Batch (Beta) (TypeScript)](/docs/en/api/typescript/beta/messages/batches/delete) {api-endpoint}
- [List Message Batches (Beta)](/docs/en/api/beta/messages/batches/list) {api-endpoint}
- [List Message Batches (Beta) (cli)](/docs/en/api/cli/beta/messages/batches/list) {api-endpoint}
- [List Message Batches (Beta) (csharp)](/docs/en/api/csharp/beta/messages/batches/list) {api-endpoint}
- [List Message Batches (Beta) (Go)](/docs/en/api/go/beta/messages/batches/list) {api-endpoint}
- [List Message Batches (Beta) (Java)](/docs/en/api/java/beta/messages/batches/list) {api-endpoint}
- [List Message Batches (Beta) (php)](/docs/en/api/php/beta/messages/batches/list) {api-endpoint}
- [List Message Batches (Beta) (Python)](/docs/en/api/python/beta/messages/batches/list) {api-endpoint}
- [List Message Batches (Beta) (Ruby)](/docs/en/api/ruby/beta/messages/batches/list) {api-endpoint}
- [List Message Batches (Beta) (terraform)](/docs/en/api/terraform/beta/messages/batches/list) {api-endpoint}
- [List Message Batches (Beta) (TypeScript)](/docs/en/api/typescript/beta/messages/batches/list) {api-endpoint}
- [Messages (Beta)](/docs/en/api/beta/messages) {api-hub}
- [Messages (Beta) (cli)](/docs/en/api/cli/beta/messages) {api-hub}
- [Messages (Beta) (csharp)](/docs/en/api/csharp/beta/messages) {api-hub}
- [Messages (Beta) (Go)](/docs/en/api/go/beta/messages) {api-hub}
- [Messages (Beta) (Java)](/docs/en/api/java/beta/messages) {api-hub}
- [Messages (Beta) (php)](/docs/en/api/php/beta/messages) {api-hub}
- [Messages (Beta) (Python)](/docs/en/api/python/beta/messages) {api-hub}
- [Messages (Beta) (Ruby)](/docs/en/api/ruby/beta/messages) {api-hub}
- [Messages (Beta) (terraform)](/docs/en/api/terraform/beta/messages) {api-hub}
- [Messages (Beta) (TypeScript)](/docs/en/api/typescript/beta/messages) {api-hub}
- [Retrieve a Message Batch (Beta)](/docs/en/api/beta/messages/batches/retrieve) {api-endpoint}
- [Retrieve a Message Batch (Beta) (cli)](/docs/en/api/cli/beta/messages/batches/retrieve) {api-endpoint}
- [Retrieve a Message Batch (Beta) (csharp)](/docs/en/api/csharp/beta/messages/batches/retrieve) {api-endpoint}
- [Retrieve a Message Batch (Beta) (Go)](/docs/en/api/go/beta/messages/batches/retrieve) {api-endpoint}
- [Retrieve a Message Batch (Beta) (Java)](/docs/en/api/java/beta/messages/batches/retrieve) {api-endpoint}
- [Retrieve a Message Batch (Beta) (php)](/docs/en/api/php/beta/messages/batches/retrieve) {api-endpoint}
- [Retrieve a Message Batch (Beta) (Python)](/docs/en/api/python/beta/messages/batches/retrieve) {api-endpoint}
- [Retrieve a Message Batch (Beta) (Ruby)](/docs/en/api/ruby/beta/messages/batches/retrieve) {api-endpoint}
- [Retrieve a Message Batch (Beta) (terraform)](/docs/en/api/terraform/beta/messages/batches/retrieve) {api-endpoint}
- [Retrieve a Message Batch (Beta) (TypeScript)](/docs/en/api/typescript/beta/messages/batches/retrieve) {api-endpoint}
- [Retrieve Message Batch results (Beta)](/docs/en/api/beta/messages/batches/results) {api-endpoint}
- [Retrieve Message Batch results (Beta) (cli)](/docs/en/api/cli/beta/messages/batches/results) {api-endpoint}
- [Retrieve Message Batch results (Beta) (csharp)](/docs/en/api/csharp/beta/messages/batches/results) {api-endpoint}
- [Retrieve Message Batch results (Beta) (Go)](/docs/en/api/go/beta/messages/batches/results) {api-endpoint}
- [Retrieve Message Batch results (Beta) (Java)](/docs/en/api/java/beta/messages/batches/results) {api-endpoint}
- [Retrieve Message Batch results (Beta) (php)](/docs/en/api/php/beta/messages/batches/results) {api-endpoint}
- [Retrieve Message Batch results (Beta) (Python)](/docs/en/api/python/beta/messages/batches/results) {api-endpoint}
- [Retrieve Message Batch results (Beta) (Ruby)](/docs/en/api/ruby/beta/messages/batches/results) {api-endpoint}
- [Retrieve Message Batch results (Beta) (terraform)](/docs/en/api/terraform/beta/messages/batches/results) {api-endpoint}
- [Retrieve Message Batch results (Beta) (TypeScript)](/docs/en/api/typescript/beta/messages/batches/results) {api-endpoint}

## Models API (30 pages)

- [Get a Model](/docs/en/api/models/retrieve) {api-endpoint}
- [Get a Model (cli)](/docs/en/api/cli/models/retrieve) {api-endpoint}
- [Get a Model (csharp)](/docs/en/api/csharp/models/retrieve) {api-endpoint}
- [Get a Model (Go)](/docs/en/api/go/models/retrieve) {api-endpoint}
- [Get a Model (Java)](/docs/en/api/java/models/retrieve) {api-endpoint}
- [Get a Model (php)](/docs/en/api/php/models/retrieve) {api-endpoint}
- [Get a Model (Python)](/docs/en/api/python/models/retrieve) {api-endpoint}
- [Get a Model (Ruby)](/docs/en/api/ruby/models/retrieve) {api-endpoint}
- [Get a Model (terraform)](/docs/en/api/terraform/models/retrieve) {api-endpoint}
- [Get a Model (TypeScript)](/docs/en/api/typescript/models/retrieve) {api-endpoint}
- [List Models](/docs/en/api/models/list) {api-endpoint}
- [List Models (cli)](/docs/en/api/cli/models/list) {api-endpoint}
- [List Models (csharp)](/docs/en/api/csharp/models/list) {api-endpoint}
- [List Models (Go)](/docs/en/api/go/models/list) {api-endpoint}
- [List Models (Java)](/docs/en/api/java/models/list) {api-endpoint}
- [List Models (php)](/docs/en/api/php/models/list) {api-endpoint}
- [List Models (Python)](/docs/en/api/python/models/list) {api-endpoint}
- [List Models (Ruby)](/docs/en/api/ruby/models/list) {api-endpoint}
- [List Models (terraform)](/docs/en/api/terraform/models/list) {api-endpoint}
- [List Models (TypeScript)](/docs/en/api/typescript/models/list) {api-endpoint}
- [Models](/docs/en/api/models) — hub {api-hub}
- [Models (cli)](/docs/en/api/cli/models) {api-hub}
- [Models (csharp)](/docs/en/api/csharp/models) {api-hub}
- [Models (Go)](/docs/en/api/go/models) {api-hub}
- [Models (Java)](/docs/en/api/java/models) {api-hub}
- [Models (php)](/docs/en/api/php/models) {api-hub}
- [Models (Python)](/docs/en/api/python/models) {api-hub}
- [Models (Ruby)](/docs/en/api/ruby/models) {api-hub}
- [Models (terraform)](/docs/en/api/terraform/models) {api-hub}
- [Models (TypeScript)](/docs/en/api/typescript/models) {api-hub}

## Models API (Beta) (30 pages)

- [Get a Model (Beta)](/docs/en/api/beta/models/retrieve) {api-endpoint}
- [Get a Model (Beta) (cli)](/docs/en/api/cli/beta/models/retrieve) {api-endpoint}
- [Get a Model (Beta) (csharp)](/docs/en/api/csharp/beta/models/retrieve) {api-endpoint}
- [Get a Model (Beta) (Go)](/docs/en/api/go/beta/models/retrieve) {api-endpoint}
- [Get a Model (Beta) (Java)](/docs/en/api/java/beta/models/retrieve) {api-endpoint}
- [Get a Model (Beta) (php)](/docs/en/api/php/beta/models/retrieve) {api-endpoint}
- [Get a Model (Beta) (Python)](/docs/en/api/python/beta/models/retrieve) {api-endpoint}
- [Get a Model (Beta) (Ruby)](/docs/en/api/ruby/beta/models/retrieve) {api-endpoint}
- [Get a Model (Beta) (terraform)](/docs/en/api/terraform/beta/models/retrieve) {api-endpoint}
- [Get a Model (Beta) (TypeScript)](/docs/en/api/typescript/beta/models/retrieve) {api-endpoint}
- [List Models (Beta)](/docs/en/api/beta/models/list) {api-endpoint}
- [List Models (Beta) (cli)](/docs/en/api/cli/beta/models/list) {api-endpoint}
- [List Models (Beta) (csharp)](/docs/en/api/csharp/beta/models/list) {api-endpoint}
- [List Models (Beta) (Go)](/docs/en/api/go/beta/models/list) {api-endpoint}
- [List Models (Beta) (Java)](/docs/en/api/java/beta/models/list) {api-endpoint}
- [List Models (Beta) (php)](/docs/en/api/php/beta/models/list) {api-endpoint}
- [List Models (Beta) (Python)](/docs/en/api/python/beta/models/list) {api-endpoint}
- [List Models (Beta) (Ruby)](/docs/en/api/ruby/beta/models/list) {api-endpoint}
- [List Models (Beta) (terraform)](/docs/en/api/terraform/beta/models/list) {api-endpoint}
- [List Models (Beta) (TypeScript)](/docs/en/api/typescript/beta/models/list) {api-endpoint}
- [Models (Beta)](/docs/en/api/beta/models) {api-hub}
- [Models (Beta) (cli)](/docs/en/api/cli/beta/models) {api-hub}
- [Models (Beta) (csharp)](/docs/en/api/csharp/beta/models) {api-hub}
- [Models (Beta) (Go)](/docs/en/api/go/beta/models) {api-hub}
- [Models (Beta) (Java)](/docs/en/api/java/beta/models) {api-hub}
- [Models (Beta) (php)](/docs/en/api/php/beta/models) {api-hub}
- [Models (Beta) (Python)](/docs/en/api/python/beta/models) {api-hub}
- [Models (Beta) (Ruby)](/docs/en/api/ruby/beta/models) {api-hub}
- [Models (Beta) (terraform)](/docs/en/api/terraform/beta/models) {api-hub}
- [Models (Beta) (TypeScript)](/docs/en/api/typescript/beta/models) {api-hub}

## Completions API (20 pages)

- [Completions](/docs/en/api/completions) — hub (legacy) {api-hub}
- [Completions (cli)](/docs/en/api/cli/completions) {api-hub}
- [Completions (csharp)](/docs/en/api/csharp/completions) {api-hub}
- [Completions (Go)](/docs/en/api/go/completions) {api-hub}
- [Completions (Java)](/docs/en/api/java/completions) {api-hub}
- [Completions (php)](/docs/en/api/php/completions) {api-hub}
- [Completions (Python)](/docs/en/api/python/completions) {api-hub}
- [Completions (Ruby)](/docs/en/api/ruby/completions) {api-hub}
- [Completions (terraform)](/docs/en/api/terraform/completions) {api-hub}
- [Completions (TypeScript)](/docs/en/api/typescript/completions) {api-hub}
- [Create a Text Completion](/docs/en/api/completions/create) {api-endpoint}
- [Create a Text Completion (cli)](/docs/en/api/cli/completions/create) {api-endpoint}
- [Create a Text Completion (csharp)](/docs/en/api/csharp/completions/create) {api-endpoint}
- [Create a Text Completion (Go)](/docs/en/api/go/completions/create) {api-endpoint}
- [Create a Text Completion (Java)](/docs/en/api/java/completions/create) {api-endpoint}
- [Create a Text Completion (php)](/docs/en/api/php/completions/create) {api-endpoint}
- [Create a Text Completion (Python)](/docs/en/api/python/completions/create) {api-endpoint}
- [Create a Text Completion (Ruby)](/docs/en/api/ruby/completions/create) {api-endpoint}
- [Create a Text Completion (terraform)](/docs/en/api/terraform/completions/create) {api-endpoint}
- [Create a Text Completion (TypeScript)](/docs/en/api/typescript/completions/create) {api-endpoint}

## Admin API (33 pages)

- [API Keys](/docs/en/api/admin/api_keys) {guide}
- [Archive Workspace](/docs/en/api/admin/workspaces/archive) {api-endpoint}
- [Cost Report](/docs/en/api/admin/cost_report) {guide}
- [Create Invite](/docs/en/api/admin/invites/create) {api-endpoint}
- [Create Workspace](/docs/en/api/admin/workspaces/create) {api-endpoint}
- [Create Workspace Member](/docs/en/api/admin/workspaces/members/create) {api-endpoint}
- [Delete Invite](/docs/en/api/admin/invites/delete) {api-endpoint}
- [Delete Workspace Member](/docs/en/api/admin/workspaces/members/delete) {api-endpoint}
- [Get API Key](/docs/en/api/admin/api_keys/retrieve) {api-endpoint}
- [Get Claude Code Usage Report](/docs/en/api/admin/usage_report/retrieve_claude_code) {api-endpoint}
- [Get Cost Report](/docs/en/api/admin/cost_report/retrieve) {api-endpoint}
- [Get Current Organization](/docs/en/api/admin/organizations/me) {api-endpoint}
- [Get Invite](/docs/en/api/admin/invites/retrieve) {api-endpoint}
- [Get Messages Usage Report](/docs/en/api/admin/usage_report/retrieve_messages) {api-endpoint}
- [Get User](/docs/en/api/admin/users/retrieve) {api-endpoint}
- [Get Workspace](/docs/en/api/admin/workspaces/retrieve) {api-endpoint}
- [Get Workspace Member](/docs/en/api/admin/workspaces/members/retrieve) {api-endpoint}
- [Invites](/docs/en/api/admin/invites) {guide}
- [List API Keys](/docs/en/api/admin/api_keys/list) {api-endpoint}
- [List Invites](/docs/en/api/admin/invites/list) {api-endpoint}
- [List Users](/docs/en/api/admin/users/list) {api-endpoint}
- [List Workspace Members](/docs/en/api/admin/workspaces/members/list) {api-endpoint}
- [List Workspaces](/docs/en/api/admin/workspaces/list) {api-endpoint}
- [Members](/docs/en/api/admin/workspaces/members) {guide}
- [Organizations](/docs/en/api/admin/organizations) {guide}
- [Remove User](/docs/en/api/admin/users/delete) {api-endpoint}
- [Update API Key](/docs/en/api/admin/api_keys/update) {api-endpoint}
- [Update User](/docs/en/api/admin/users/update) {api-endpoint}
- [Update Workspace](/docs/en/api/admin/workspaces/update) {api-endpoint}
- [Update Workspace Member](/docs/en/api/admin/workspaces/members/update) {api-endpoint}
- [Usage Report](/docs/en/api/admin/usage_report) {guide}
- [Users](/docs/en/api/admin/users) {guide}
- [Workspaces](/docs/en/api/admin/workspaces) {guide}

## Files API (Beta) (60 pages)

- [Delete File (Beta)](/docs/en/api/beta/files/delete) {api-endpoint}
- [Delete File (Beta) (cli)](/docs/en/api/cli/beta/files/delete) {api-endpoint}
- [Delete File (Beta) (csharp)](/docs/en/api/csharp/beta/files/delete) {api-endpoint}
- [Delete File (Beta) (Go)](/docs/en/api/go/beta/files/delete) {api-endpoint}
- [Delete File (Beta) (Java)](/docs/en/api/java/beta/files/delete) {api-endpoint}
- [Delete File (Beta) (php)](/docs/en/api/php/beta/files/delete) {api-endpoint}
- [Delete File (Beta) (Python)](/docs/en/api/python/beta/files/delete) {api-endpoint}
- [Delete File (Beta) (Ruby)](/docs/en/api/ruby/beta/files/delete) {api-endpoint}
- [Delete File (Beta) (terraform)](/docs/en/api/terraform/beta/files/delete) {api-endpoint}
- [Delete File (Beta) (TypeScript)](/docs/en/api/typescript/beta/files/delete) {api-endpoint}
- [Download File (Beta)](/docs/en/api/beta/files/download) {api-endpoint}
- [Download File (Beta) (cli)](/docs/en/api/cli/beta/files/download) {api-endpoint}
- [Download File (Beta) (csharp)](/docs/en/api/csharp/beta/files/download) {api-endpoint}
- [Download File (Beta) (Go)](/docs/en/api/go/beta/files/download) {api-endpoint}
- [Download File (Beta) (Java)](/docs/en/api/java/beta/files/download) {api-endpoint}
- [Download File (Beta) (php)](/docs/en/api/php/beta/files/download) {api-endpoint}
- [Download File (Beta) (Python)](/docs/en/api/python/beta/files/download) {api-endpoint}
- [Download File (Beta) (Ruby)](/docs/en/api/ruby/beta/files/download) {api-endpoint}
- [Download File (Beta) (terraform)](/docs/en/api/terraform/beta/files/download) {api-endpoint}
- [Download File (Beta) (TypeScript)](/docs/en/api/typescript/beta/files/download) {api-endpoint}
- [Files (Beta)](/docs/en/api/beta/files) {api-hub}
- [Files (Beta) (cli)](/docs/en/api/cli/beta/files) {api-hub}
- [Files (Beta) (csharp)](/docs/en/api/csharp/beta/files) {api-hub}
- [Files (Beta) (Go)](/docs/en/api/go/beta/files) {api-hub}
- [Files (Beta) (Java)](/docs/en/api/java/beta/files) {api-hub}
- [Files (Beta) (php)](/docs/en/api/php/beta/files) {api-hub}
- [Files (Beta) (Python)](/docs/en/api/python/beta/files) {api-hub}
- [Files (Beta) (Ruby)](/docs/en/api/ruby/beta/files) {api-hub}
- [Files (Beta) (terraform)](/docs/en/api/terraform/beta/files) {api-hub}
- [Files (Beta) (TypeScript)](/docs/en/api/typescript/beta/files) {api-hub}
- [Get File Metadata (Beta)](/docs/en/api/beta/files/retrieve_metadata) {api-endpoint}
- [Get File Metadata (Beta) (cli)](/docs/en/api/cli/beta/files/retrieve_metadata) {api-endpoint}
- [Get File Metadata (Beta) (csharp)](/docs/en/api/csharp/beta/files/retrieve_metadata) {api-endpoint}
- [Get File Metadata (Beta) (Go)](/docs/en/api/go/beta/files/retrieve_metadata) {api-endpoint}
- [Get File Metadata (Beta) (Java)](/docs/en/api/java/beta/files/retrieve_metadata) {api-endpoint}
- [Get File Metadata (Beta) (php)](/docs/en/api/php/beta/files/retrieve_metadata) {api-endpoint}
- [Get File Metadata (Beta) (Python)](/docs/en/api/python/beta/files/retrieve_metadata) {api-endpoint}
- [Get File Metadata (Beta) (Ruby)](/docs/en/api/ruby/beta/files/retrieve_metadata) {api-endpoint}
- [Get File Metadata (Beta) (terraform)](/docs/en/api/terraform/beta/files/retrieve_metadata) {api-endpoint}
- [Get File Metadata (Beta) (TypeScript)](/docs/en/api/typescript/beta/files/retrieve_metadata) {api-endpoint}
- [List Files (Beta)](/docs/en/api/beta/files/list) {api-endpoint}
- [List Files (Beta) (cli)](/docs/en/api/cli/beta/files/list) {api-endpoint}
- [List Files (Beta) (csharp)](/docs/en/api/csharp/beta/files/list) {api-endpoint}
- [List Files (Beta) (Go)](/docs/en/api/go/beta/files/list) {api-endpoint}
- [List Files (Beta) (Java)](/docs/en/api/java/beta/files/list) {api-endpoint}
- [List Files (Beta) (php)](/docs/en/api/php/beta/files/list) {api-endpoint}
- [List Files (Beta) (Python)](/docs/en/api/python/beta/files/list) {api-endpoint}
- [List Files (Beta) (Ruby)](/docs/en/api/ruby/beta/files/list) {api-endpoint}
- [List Files (Beta) (terraform)](/docs/en/api/terraform/beta/files/list) {api-endpoint}
- [List Files (Beta) (TypeScript)](/docs/en/api/typescript/beta/files/list) {api-endpoint}
- [Upload File (Beta)](/docs/en/api/beta/files/upload) {api-endpoint}
- [Upload File (Beta) (cli)](/docs/en/api/cli/beta/files/upload) {api-endpoint}
- [Upload File (Beta) (csharp)](/docs/en/api/csharp/beta/files/upload) {api-endpoint}
- [Upload File (Beta) (Go)](/docs/en/api/go/beta/files/upload) {api-endpoint}
- [Upload File (Beta) (Java)](/docs/en/api/java/beta/files/upload) {api-endpoint}
- [Upload File (Beta) (php)](/docs/en/api/php/beta/files/upload) {api-endpoint}
- [Upload File (Beta) (Python)](/docs/en/api/python/beta/files/upload) {api-endpoint}
- [Upload File (Beta) (Ruby)](/docs/en/api/ruby/beta/files/upload) {api-endpoint}
- [Upload File (Beta) (terraform)](/docs/en/api/terraform/beta/files/upload) {api-endpoint}
- [Upload File (Beta) (TypeScript)](/docs/en/api/typescript/beta/files/upload) {api-endpoint}

## Skills API (Beta) (100 pages)

- [Create Skill (Beta)](/docs/en/api/beta/skills/create) {api-endpoint}
- [Create Skill (Beta) (cli)](/docs/en/api/cli/beta/skills/create) {api-endpoint}
- [Create Skill (Beta) (csharp)](/docs/en/api/csharp/beta/skills/create) {api-endpoint}
- [Create Skill (Beta) (Go)](/docs/en/api/go/beta/skills/create) {api-endpoint}
- [Create Skill (Beta) (Java)](/docs/en/api/java/beta/skills/create) {api-endpoint}
- [Create Skill (Beta) (php)](/docs/en/api/php/beta/skills/create) {api-endpoint}
- [Create Skill (Beta) (Python)](/docs/en/api/python/beta/skills/create) {api-endpoint}
- [Create Skill (Beta) (Ruby)](/docs/en/api/ruby/beta/skills/create) {api-endpoint}
- [Create Skill (Beta) (terraform)](/docs/en/api/terraform/beta/skills/create) {api-endpoint}
- [Create Skill (Beta) (TypeScript)](/docs/en/api/typescript/beta/skills/create) {api-endpoint}
- [Create Skill Version (Beta)](/docs/en/api/beta/skills/versions/create) {api-endpoint}
- [Create Skill Version (Beta) (cli)](/docs/en/api/cli/beta/skills/versions/create) {api-endpoint}
- [Create Skill Version (Beta) (csharp)](/docs/en/api/csharp/beta/skills/versions/create) {api-endpoint}
- [Create Skill Version (Beta) (Go)](/docs/en/api/go/beta/skills/versions/create) {api-endpoint}
- [Create Skill Version (Beta) (Java)](/docs/en/api/java/beta/skills/versions/create) {api-endpoint}
- [Create Skill Version (Beta) (php)](/docs/en/api/php/beta/skills/versions/create) {api-endpoint}
- [Create Skill Version (Beta) (Python)](/docs/en/api/python/beta/skills/versions/create) {api-endpoint}
- [Create Skill Version (Beta) (Ruby)](/docs/en/api/ruby/beta/skills/versions/create) {api-endpoint}
- [Create Skill Version (Beta) (terraform)](/docs/en/api/terraform/beta/skills/versions/create) {api-endpoint}
- [Create Skill Version (Beta) (TypeScript)](/docs/en/api/typescript/beta/skills/versions/create) {api-endpoint}
- [Delete Skill (Beta)](/docs/en/api/beta/skills/delete) {api-endpoint}
- [Delete Skill (Beta) (cli)](/docs/en/api/cli/beta/skills/delete) {api-endpoint}
- [Delete Skill (Beta) (csharp)](/docs/en/api/csharp/beta/skills/delete) {api-endpoint}
- [Delete Skill (Beta) (Go)](/docs/en/api/go/beta/skills/delete) {api-endpoint}
- [Delete Skill (Beta) (Java)](/docs/en/api/java/beta/skills/delete) {api-endpoint}
- [Delete Skill (Beta) (php)](/docs/en/api/php/beta/skills/delete) {api-endpoint}
- [Delete Skill (Beta) (Python)](/docs/en/api/python/beta/skills/delete) {api-endpoint}
- [Delete Skill (Beta) (Ruby)](/docs/en/api/ruby/beta/skills/delete) {api-endpoint}
- [Delete Skill (Beta) (terraform)](/docs/en/api/terraform/beta/skills/delete) {api-endpoint}
- [Delete Skill (Beta) (TypeScript)](/docs/en/api/typescript/beta/skills/delete) {api-endpoint}
- [Delete Skill Version (Beta)](/docs/en/api/beta/skills/versions/delete) {api-endpoint}
- [Delete Skill Version (Beta) (cli)](/docs/en/api/cli/beta/skills/versions/delete) {api-endpoint}
- [Delete Skill Version (Beta) (csharp)](/docs/en/api/csharp/beta/skills/versions/delete) {api-endpoint}
- [Delete Skill Version (Beta) (Go)](/docs/en/api/go/beta/skills/versions/delete) {api-endpoint}
- [Delete Skill Version (Beta) (Java)](/docs/en/api/java/beta/skills/versions/delete) {api-endpoint}
- [Delete Skill Version (Beta) (php)](/docs/en/api/php/beta/skills/versions/delete) {api-endpoint}
- [Delete Skill Version (Beta) (Python)](/docs/en/api/python/beta/skills/versions/delete) {api-endpoint}
- [Delete Skill Version (Beta) (Ruby)](/docs/en/api/ruby/beta/skills/versions/delete) {api-endpoint}
- [Delete Skill Version (Beta) (terraform)](/docs/en/api/terraform/beta/skills/versions/delete) {api-endpoint}
- [Delete Skill Version (Beta) (TypeScript)](/docs/en/api/typescript/beta/skills/versions/delete) {api-endpoint}
- [Get Skill (Beta)](/docs/en/api/beta/skills/retrieve) {api-endpoint}
- [Get Skill (Beta) (cli)](/docs/en/api/cli/beta/skills/retrieve) {api-endpoint}
- [Get Skill (Beta) (csharp)](/docs/en/api/csharp/beta/skills/retrieve) {api-endpoint}
- [Get Skill (Beta) (Go)](/docs/en/api/go/beta/skills/retrieve) {api-endpoint}
- [Get Skill (Beta) (Java)](/docs/en/api/java/beta/skills/retrieve) {api-endpoint}
- [Get Skill (Beta) (php)](/docs/en/api/php/beta/skills/retrieve) {api-endpoint}
- [Get Skill (Beta) (Python)](/docs/en/api/python/beta/skills/retrieve) {api-endpoint}
- [Get Skill (Beta) (Ruby)](/docs/en/api/ruby/beta/skills/retrieve) {api-endpoint}
- [Get Skill (Beta) (terraform)](/docs/en/api/terraform/beta/skills/retrieve) {api-endpoint}
- [Get Skill (Beta) (TypeScript)](/docs/en/api/typescript/beta/skills/retrieve) {api-endpoint}
- [Get Skill Version (Beta)](/docs/en/api/beta/skills/versions/retrieve) {api-endpoint}
- [Get Skill Version (Beta) (cli)](/docs/en/api/cli/beta/skills/versions/retrieve) {api-endpoint}
- [Get Skill Version (Beta) (csharp)](/docs/en/api/csharp/beta/skills/versions/retrieve) {api-endpoint}
- [Get Skill Version (Beta) (Go)](/docs/en/api/go/beta/skills/versions/retrieve) {api-endpoint}
- [Get Skill Version (Beta) (Java)](/docs/en/api/java/beta/skills/versions/retrieve) {api-endpoint}
- [Get Skill Version (Beta) (php)](/docs/en/api/php/beta/skills/versions/retrieve) {api-endpoint}
- [Get Skill Version (Beta) (Python)](/docs/en/api/python/beta/skills/versions/retrieve) {api-endpoint}
- [Get Skill Version (Beta) (Ruby)](/docs/en/api/ruby/beta/skills/versions/retrieve) {api-endpoint}
- [Get Skill Version (Beta) (terraform)](/docs/en/api/terraform/beta/skills/versions/retrieve) {api-endpoint}
- [Get Skill Version (Beta) (TypeScript)](/docs/en/api/typescript/beta/skills/versions/retrieve) {api-endpoint}
- [List Skill Versions (Beta)](/docs/en/api/beta/skills/versions/list) {api-endpoint}
- [List Skill Versions (Beta) (cli)](/docs/en/api/cli/beta/skills/versions/list) {api-endpoint}
- [List Skill Versions (Beta) (csharp)](/docs/en/api/csharp/beta/skills/versions/list) {api-endpoint}
- [List Skill Versions (Beta) (Go)](/docs/en/api/go/beta/skills/versions/list) {api-endpoint}
- [List Skill Versions (Beta) (Java)](/docs/en/api/java/beta/skills/versions/list) {api-endpoint}
- [List Skill Versions (Beta) (php)](/docs/en/api/php/beta/skills/versions/list) {api-endpoint}
- [List Skill Versions (Beta) (Python)](/docs/en/api/python/beta/skills/versions/list) {api-endpoint}
- [List Skill Versions (Beta) (Ruby)](/docs/en/api/ruby/beta/skills/versions/list) {api-endpoint}
- [List Skill Versions (Beta) (terraform)](/docs/en/api/terraform/beta/skills/versions/list) {api-endpoint}
- [List Skill Versions (Beta) (TypeScript)](/docs/en/api/typescript/beta/skills/versions/list) {api-endpoint}
- [List Skills (Beta)](/docs/en/api/beta/skills/list) {api-endpoint}
- [List Skills (Beta) (cli)](/docs/en/api/cli/beta/skills/list) {api-endpoint}
- [List Skills (Beta) (csharp)](/docs/en/api/csharp/beta/skills/list) {api-endpoint}
- [List Skills (Beta) (Go)](/docs/en/api/go/beta/skills/list) {api-endpoint}
- [List Skills (Beta) (Java)](/docs/en/api/java/beta/skills/list) {api-endpoint}
- [List Skills (Beta) (php)](/docs/en/api/php/beta/skills/list) {api-endpoint}
- [List Skills (Beta) (Python)](/docs/en/api/python/beta/skills/list) {api-endpoint}
- [List Skills (Beta) (Ruby)](/docs/en/api/ruby/beta/skills/list) {api-endpoint}
- [List Skills (Beta) (terraform)](/docs/en/api/terraform/beta/skills/list) {api-endpoint}
- [List Skills (Beta) (TypeScript)](/docs/en/api/typescript/beta/skills/list) {api-endpoint}
- [Skills (Beta)](/docs/en/api/beta/skills) {api-hub}
- [Skills (Beta) (cli)](/docs/en/api/cli/beta/skills) {api-hub}
- [Skills (Beta) (csharp)](/docs/en/api/csharp/beta/skills) {api-hub}
- [Skills (Beta) (Go)](/docs/en/api/go/beta/skills) {api-hub}
- [Skills (Beta) (Java)](/docs/en/api/java/beta/skills) {api-hub}
- [Skills (Beta) (php)](/docs/en/api/php/beta/skills) {api-hub}
- [Skills (Beta) (Python)](/docs/en/api/python/beta/skills) {api-hub}
- [Skills (Beta) (Ruby)](/docs/en/api/ruby/beta/skills) {api-hub}
- [Skills (Beta) (terraform)](/docs/en/api/terraform/beta/skills) {api-hub}
- [Skills (Beta) (TypeScript)](/docs/en/api/typescript/beta/skills) {api-hub}
- [Versions (Beta)](/docs/en/api/beta/skills/versions) {guide}
- [Versions (Beta) (cli)](/docs/en/api/cli/beta/skills/versions) {guide}
- [Versions (Beta) (csharp)](/docs/en/api/csharp/beta/skills/versions) {guide}
- [Versions (Beta) (Go)](/docs/en/api/go/beta/skills/versions) {guide}
- [Versions (Beta) (Java)](/docs/en/api/java/beta/skills/versions) {guide}
- [Versions (Beta) (php)](/docs/en/api/php/beta/skills/versions) {guide}
- [Versions (Beta) (Python)](/docs/en/api/python/beta/skills/versions) {guide}
- [Versions (Beta) (Ruby)](/docs/en/api/ruby/beta/skills/versions) {guide}
- [Versions (Beta) (terraform)](/docs/en/api/terraform/beta/skills/versions) {guide}
- [Versions (Beta) (TypeScript)](/docs/en/api/typescript/beta/skills/versions) {guide}

## Beta API Overview (10 pages)

- [Beta (Beta)](/docs/en/api/beta) — hub {guide}
- [Beta (Beta) (cli)](/docs/en/api/cli/beta) {guide}
- [Beta (Beta) (csharp)](/docs/en/api/csharp/beta) {guide}
- [Beta (Beta) (Go)](/docs/en/api/go/beta) {guide}
- [Beta (Beta) (Java)](/docs/en/api/java/beta) {guide}
- [Beta (Beta) (php)](/docs/en/api/php/beta) {guide}
- [Beta (Beta) (Python)](/docs/en/api/python/beta) {guide}
- [Beta (Beta) (Ruby)](/docs/en/api/ruby/beta) {guide}
- [Beta (Beta) (terraform)](/docs/en/api/terraform/beta) {guide}
- [Beta (Beta) (TypeScript)](/docs/en/api/typescript/beta) {guide}

## Resources (8 pages)

- [Overview](/docs/en/about-claude/use-case-guides/overview) {overview}
- [Overview](/docs/en/resources/overview) {overview}
- [Content moderation](/docs/en/about-claude/use-case-guides/content-moderation) {use-case}
- [Customer support agent](/docs/en/about-claude/use-case-guides/customer-support-chat) {use-case}
- [Glossary](/docs/en/about-claude/glossary) {guide}
- [Legal summarization](/docs/en/about-claude/use-case-guides/legal-summarization) {use-case}
- [System Prompts](/docs/en/release-notes/system-prompts) {changelog}
- [Ticket routing](/docs/en/about-claude/use-case-guides/ticket-routing) {use-case}

## Release Notes (1 page)

- [Claude Platform](/docs/en/release-notes/overview) {overview}

