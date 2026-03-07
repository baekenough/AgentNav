# NAVIGATOR.md Codex Test Report

- **Date**: 2026-03-07 20:52:02
- **Model**: default
- **Total Queries**: 100
- **Overall Score**: 97.7/100 (97.7%)
- **Elapsed**: 214.5s

## Category Summary

| Category | Name | Score | Pct |
|----------|------|-------|-----|
| A | Structure | 10.0/10 | 100% |
| B | Direct Lookup | 10.0/10 | 100% |
| C | API Navigation | 10.0/10 | 100% |
| D | SDK Endpoint Lookup | 10.0/10 | 100% |
| E | Natural Language Navigation | 10.0/10 | 100% |
| F | Section Enumeration | 9.7/10 | 97% |
| G | Page Type Classification | 10.0/10 | 100% |
| H | Full URL Construction | 10.0/10 | 100% |
| I | Cross-Section Navigation | 9.0/10 | 90% |
| J | Edge Cases | 9.0/10 | 90% |

## Detailed Results

### Cat A: Structure

| ID | Query | Expected | Got | Score |
|----|-------|----------|-----|-------|
| A1 | How many total pages are in agents.txt? | 651 | 651 | PASS (1.0) |
| A2 | How many sections are in agents.txt? | 9 | 9 | PASS (1.0) |
| A3 | How many pages does the API Reference section have | 546 | 546 | PASS (1.0) |
| A4 | How many pages does Build with Claude section have | 35 | 35 | PASS (1.0) |
| A5 | How many pages does the Agent SDK section have? | 27 | 27 | PASS (1.0) |
| A6 | How many pages does Agents & Tools section have? | 18 | 18 | PASS (1.0) |
| A7 | How many pages does About Claude section have? | 12 | 12 | PASS (1.0) |
| A8 | How many pages does Test & Evaluate section have? | 8 | 8 | PASS (1.0) |
| A9 | How many pages does Release Notes section have? | 2 | 2 | PASS (1.0) |
| A10 | How many pages does Resources section have? | 1 | 1 | PASS (1.0) |

### Cat B: Direct Lookup

| ID | Query | Expected | Got | Score |
|----|-------|----------|-----|-------|
| B1 | Find the path for prompt-caching. | /docs/en/build-with-claude/prompt-caching | /docs/en/build-with-claude/prompt-caching | PASS (1.0) |
| B2 | Find the path for glossary. | /docs/en/about-claude/glossary | /docs/en/about-claude/glossary | PASS (1.0) |
| B3 | Find the path for pricing. | /docs/en/about-claude/pricing | /docs/en/about-claude/pricing | PASS (1.0) |
| B4 | Find the path for extended-thinking. | /docs/en/build-with-claude/extended-thinking | /docs/en/build-with-claude/extended-thinking | PASS (1.0) |
| B5 | Find the path for mcp-connector. | /docs/en/agents-and-tools/mcp-connector | /docs/en/agents-and-tools/mcp-connector | PASS (1.0) |
| B6 | Find the path for bash-tool. | /docs/en/agents-and-tools/tool-use/bash-tool | /docs/en/agents-and-tools/tool-use/bash-tool | PASS (1.0) |
| B7 | Find the path for quickstart in Agent SDK. | /docs/en/agent-sdk/quickstart | /docs/en/agent-sdk/quickstart | PASS (1.0) |
| B8 | Find the path for subagents. | /docs/en/agent-sdk/subagents | /docs/en/agent-sdk/subagents | PASS (1.0) |
| B9 | Find the path for rate-limits. | /docs/en/api/rate-limits | /docs/en/api/rate-limits | PASS (1.0) |
| B10 | Find the path for reduce-hallucinations. | /docs/en/test-and-evaluate/strengthen-guardrails/reduce-hall | /docs/en/test-and-evaluate/strengthen-guardrails/reduce-hallucinations | PASS (1.0) |

### Cat C: API Navigation

| ID | Query | Expected | Got | Score |
|----|-------|----------|-----|-------|
| C1 | What is the API path for messages create endpoint? | messages/create | /docs/en/api/messages/create | PASS (1.0) |
| C2 | What is the API overview path? | api/overview | /docs/en/api/overview | PASS (1.0) |
| C3 | What is the API errors page path? | api/errors | /docs/en/api/errors | PASS (1.0) |
| C4 | What is the Admin API hub path? | api/admin | /docs/en/api/admin | PASS (1.0) |
| C5 | What is the workspace management path? | admin/workspaces | /docs/en/api/admin/workspaces | PASS (1.0) |
| C6 | What is the batch create endpoint path? | messages/batches/create | /docs/en/api/messages/batches/create | PASS (1.0) |
| C7 | What is the beta files hub path? | beta/files | /docs/en/api/beta/files | PASS (1.0) |
| C8 | What is the models list endpoint path? | models/list | /docs/en/api/models/list | PASS (1.0) |
| C9 | What is the completions API hub path? | completions | /docs/en/api/completions | PASS (1.0) |
| C10 | What is the API versioning page path? | api/versioning | /docs/en/api/versioning | PASS (1.0) |

### Cat D: SDK Endpoint Lookup

| ID | Query | Expected | Got | Score |
|----|-------|----------|-----|-------|
| D1 | What is the Python SDK path for messages/create? | api/python/messages/create | /docs/en/api/python/messages/create | PASS (1.0) |
| D2 | What is the TypeScript SDK path for models/list? | api/typescript/models/list | /docs/en/api/typescript/models/list | PASS (1.0) |
| D3 | What is the Go SDK path for beta/files/upload? | api/go/beta/files/upload | /docs/en/api/go/beta/files/upload | PASS (1.0) |
| D4 | What is the Java SDK path for messages/batches/cre | api/java/messages/batches/create | /docs/en/api/java/messages/batches/create | PASS (1.0) |
| D5 | What is the Kotlin SDK path for completions/create | api/kotlin/completions/create | /docs/en/api/kotlin/completions/create | PASS (1.0) |
| D6 | What is the Ruby SDK path for beta/models/retrieve | api/ruby/beta/models/retrieve | /docs/en/api/ruby/beta/models/retrieve | PASS (1.0) |
| D7 | What is the PHP SDK path for messages/count_tokens | api/php/messages/count_tokens | /docs/en/api/php/messages/count_tokens | PASS (1.0) |
| D8 | What is the C# SDK path for beta/skills/list? | api/csharp/beta/skills/list | /docs/en/api/csharp/beta/skills/list | PASS (1.0) |
| D9 | What is the Terraform SDK path for messages/batche | api/terraform/messages/batches/cancel | /docs/en/api/terraform/messages/batches/cancel | PASS (1.0) |
| D10 | What is the CLI SDK path for beta/files/delete? | api/cli/beta/files/delete | /docs/en/api/cli/beta/files/delete | PASS (1.0) |

### Cat E: Natural Language Navigation

| ID | Query | Expected | Got | Score |
|----|-------|----------|-----|-------|
| E1 | I want to send a message to the API. Which page? | messages/create | Messages create endpoint — https://platform.claude.com/docs/en/api/messages/crea | PASS (1.0) |
| E2 | Where can I see available models? | models/overview | Models overview — https://platform.claude.com/docs/en/about-claude/models/overvi | PASS (1.0) |
| E3 | How do I cache prompts? | prompt-caching | Prompt caching — https://platform.claude.com/docs/en/build-with-claude/prompt-ca | PASS (1.0) |
| E4 | Where is the web search tool documented? | web-search-tool | Web search tool — https://platform.claude.com/docs/en/agents-and-tools/tool-use/ | PASS (1.0) |
| E5 | How do I get started with the Agent SDK? | agent-sdk/quickstart | Agent SDK quickstart — https://platform.claude.com/docs/en/agent-sdk/quickstart | PASS (1.0) |
| E6 | How to reduce hallucinations? | reduce-hallucinations | Reduce hallucinations — https://platform.claude.com/docs/en/test-and-evaluate/st | PASS (1.0) |
| E7 | What are the rate limiting rules? | rate-limits | Rate limits — https://platform.claude.com/docs/en/api/rate-limits | PASS (1.0) |
| E8 | Where is computer use documented? | computer-use-tool | Computer use tool — https://platform.claude.com/docs/en/agents-and-tools/tool-us | PASS (1.0) |
| E9 | Where is the Python SDK guide? | python | Python SDK guide — https://platform.claude.com/docs/en/agent-sdk/python | PASS (1.0) |
| E10 | How to get structured output from Claude? | structured-outputs | Structured outputs — https://platform.claude.com/docs/en/build-with-claude/struc | PASS (1.0) |

### Cat F: Section Enumeration

| ID | Query | Expected | Got | Score |
|----|-------|----------|-----|-------|
| F1 | How many topics/pages are in Test & Evaluate? | 8 | 8 | PASS (1.0) |
| F2 | How many use case guides are listed under About Cl | 4 | 4 | PASS (1.0) |
| F3 | List all tools in the Agents & Tools section tool- | bash-tool,code-execution-tool,computer-use-tool,fine-grained | bash-tool, code-execution-tool, computer-use-tool, memory-tool, text-editor-tool | partial (0.67) |
| F4 | What Agent SDK configuration topics exist? | hooks,permissions,plugins | hooks, modifying-system-prompts, permissions, plugins | PASS (1.0) |
| F5 | Which cloud platform pages exist in Build with Cla | bedrock,vertex,foundry | claude-in-microsoft-foundry, claude-on-amazon-bedrock, claude-on-vertex-ai | PASS (1.0) |
| F6 | How many API infrastructure pages are there? | 10 | 10 | PASS (1.0) |
| F7 | How many SDK overview pages exist? | 7 | 7 | PASS (1.0) |
| F8 | How many Admin resource groups exist (organization | 5 | 5 | PASS (1.0) |
| F9 | How many Beta resource groups exist (files, messag | 4 | 4 | PASS (1.0) |
| F10 | How many Release Notes pages are there? | 2 | 2 | PASS (1.0) |

### Cat G: Page Type Classification

| ID | Query | Expected | Got | Score |
|----|-------|----------|-----|-------|
| G1 | What type is the quickstart page in Agent SDK? | tutorial | tutorial | PASS (1.0) |
| G2 | What type is the glossary page? | reference | reference | PASS (1.0) |
| G3 | What type is prompt-caching? | guide | guide | PASS (1.0) |
| G4 | What type is messages/create? | api-endpoint | api-endpoint | PASS (1.0) |
| G5 | What type is resources/overview? | overview | overview | PASS (1.0) |
| G6 | What type is web-search-tool? | tool-reference | tool-reference | PASS (1.0) |
| G7 | What type is reduce-hallucinations? | best-practices | best-practices | PASS (1.0) |
| G8 | What type is agent-sdk/python? | sdk-guide | sdk-guide | PASS (1.0) |
| G9 | What type is system-prompts in Release Notes? | changelog | changelog | PASS (1.0) |
| G10 | What type is the messages hub page? | api-hub | api-hub | PASS (1.0) |

### Cat H: Full URL Construction

| ID | Query | Expected | Got | Score |
|----|-------|----------|-----|-------|
| H1 | Full URL for prompt-caching? | https://platform.claude.com/docs/en/build-with-claude/prompt | https://platform.claude.com/docs/en/build-with-claude/prompt-caching | PASS (1.0) |
| H2 | Full URL for Python SDK messages/create? | https://platform.claude.com/docs/en/api/python/messages/crea | https://platform.claude.com/docs/en/api/python/messages/create | PASS (1.0) |
| H3 | Full URL for rate-limits? | https://platform.claude.com/docs/en/api/rate-limits | https://platform.claude.com/docs/en/api/rate-limits | PASS (1.0) |
| H4 | Full URL for mcp-connector? | https://platform.claude.com/docs/en/agents-and-tools/mcp-con | https://platform.claude.com/docs/en/agents-and-tools/mcp-connector | PASS (1.0) |
| H5 | Full URL for Agent SDK quickstart? | https://platform.claude.com/docs/en/agent-sdk/quickstart | https://platform.claude.com/docs/en/agent-sdk/quickstart | PASS (1.0) |
| H6 | Full URL for reduce-hallucinations? | https://platform.claude.com/docs/en/test-and-evaluate/streng | https://platform.claude.com/docs/en/test-and-evaluate/strengthen-guardrails/redu | PASS (1.0) |
| H7 | Full URL for models/overview in About Claude? | https://platform.claude.com/docs/en/about-claude/models/over | https://platform.claude.com/docs/en/about-claude/models/overview | PASS (1.0) |
| H8 | Full URL for the intro page? | https://platform.claude.com/docs/en/intro | https://platform.claude.com/docs/en/intro | PASS (1.0) |
| H9 | Full URL for admin/workspaces? | https://platform.claude.com/docs/en/api/admin/workspaces | https://platform.claude.com/docs/en/api/admin/workspaces | PASS (1.0) |
| H10 | Full URL for beta/skills/versions/create? | https://platform.claude.com/docs/en/api/beta/skills/versions | https://platform.claude.com/docs/en/api/beta/skills/versions/create | PASS (1.0) |

### Cat I: Cross-Section Navigation

| ID | Query | Expected | Got | Score |
|----|-------|----------|-----|-------|
| I1 | List all overview pages across all sections. | overview | type=overview: /docs/en/about-claude/models/overview; /docs/en/about-claude/use- | PASS (1.0) |
| I2 | List all tutorial pages. | intro,get-started,quickstart | /docs/en/intro; /docs/en/get-started; /docs/en/agent-sdk/quickstart | PASS (1.0) |
| I3 | Which sections contain model-related pages? | about-claude/models,api/models | About Claude; API Reference | FAIL (0.0) |
| I4 | Which pages relate to streaming? | streaming,streaming-output,fine-grained | /docs/en/build-with-claude/streaming; /docs/en/agents-and-tools/tool-use/fine-gr | PASS (1.0) |
| I5 | Which pages relate to security? | secure-deployment,mitigate-jailbreaks | /docs/en/build-with-claude/data-residency; /docs/en/build-with-claude/zero-data- | PASS (1.0) |
| I6 | Which pages relate to costs? | pricing,cost-tracking,usage-cost-api | /docs/en/about-claude/pricing; /docs/en/build-with-claude/usage-cost-api; /docs/ | PASS (1.0) |
| I7 | Which pages relate to batch processing? | batch-processing,messages/batches | /docs/en/build-with-claude/batch-processing; /docs/en/api/messages/batches{,/cre | PASS (1.0) |
| I8 | Which pages relate to MCP? | mcp-connector,remote-mcp,agent-sdk/mcp | /docs/en/agents-and-tools/mcp-connector; /docs/en/agents-and-tools/remote-mcp-se | PASS (1.0) |
| I9 | List all pages in the Test & Evaluate section. | test-and-evaluate | /docs/en/test-and-evaluate/develop-tests; /docs/en/test-and-evaluate/eval-tool;  | PASS (1.0) |
| I10 | Which pages relate to Python? | python | /docs/en/agent-sdk/python; /docs/en/api/sdks/python; /docs/en/api/python/{messag | PASS (1.0) |

### Cat J: Edge Cases

| ID | Query | Expected | Got | Score |
|----|-------|----------|-----|-------|
| J1 | Find prompt-cacheing page (note the typo). | prompt-caching | https://platform.claude.com/docs/en/build-with-claude/prompt-caching | PASS (1.0) |
| J2 | Find msg create endpoint (abbreviated). | messages/create | https://platform.claude.com/docs/en/api/messages/create | PASS (1.0) |
| J3 | Find k8s deployment page. | not found | No exact k8s page found; closest match is https://platform.claude.com/docs/en/ag | FAIL (0.0) |
| J4 | Find Claude 4.6 page. | whats-new-claude-4-6 | https://platform.claude.com/docs/en/about-claude/models/whats-new-claude-4-6 | PASS (1.0) |
| J5 | What does ZDR stand for? Find the page. | zero-data-retention | ZDR = Zero Data Retention; https://platform.claude.com/docs/en/build-with-claude | PASS (1.0) |
| J6 | Find stop reasons page. | handling-stop-reasons | https://platform.claude.com/docs/en/build-with-claude/handling-stop-reasons | PASS (1.0) |
| J7 | Find websearch page (no space/hyphen). | web-search-tool | https://platform.claude.com/docs/en/agents-and-tools/tool-use/web-search-tool | PASS (1.0) |
| J8 | Find embeddings page. | embeddings | https://platform.claude.com/docs/en/build-with-claude/embeddings | PASS (1.0) |
| J9 | Find agent-loop page. | agent-sdk/agent-loop | https://platform.claude.com/docs/en/agent-sdk/agent-loop | PASS (1.0) |
| J10 | Find content moderation page. | content-moderation | https://platform.claude.com/docs/en/about-claude/use-case-guides/content-moderat | PASS (1.0) |
