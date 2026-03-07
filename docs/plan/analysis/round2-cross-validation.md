# Round 2: Cross-Validation Report

> Generated: 2026-03-07
> Agent: arch-documenter (SW Architect)
> Source sitemap: /tmp/en-docs.txt (651 URLs)

---

## Scope Correction

### Original Estimate vs Actual

| Metric | Original | Actual | Delta |
|--------|----------|--------|-------|
| Total pages | 122 | 651 | +529 |
| Section A (Intro + About) | 14 | 12 | -2 (intro, get-started 누락) |
| Section B (Build with Claude) | 35 | 35 | 0 |
| Section C (Agents + SDK) | 45 | 45 | 0 |
| Section D-1 (API) | 17 sitemapped | 575 | +558 |
| Section D-2 (Test + Release + Resources) | 11 | 11 | 0 |
| **Covered by all reports** | **122** | **651** | **+529 미확인** |

### Root Cause of Discrepancy

원래 122페이지 추산은 가이드/개념/레퍼런스 페이지만 커버했다. 실제 사이트맵에는 다음이 추가로 포함된다:

- **SDK별 API 레퍼런스 페이지**: 동일한 엔드포인트가 Python, TypeScript, Java, Go, C#, Ruby, PHP, Kotlin, Terraform, CLI 총 10개 SDK별로 반복 — 각 SDK당 약 45페이지
- **Core API 엔드포인트 레퍼런스**: messages, models, completions, admin, beta 섹션의 세부 엔드포인트들
- **Admin API 서브엔드포인트**: 34개 admin 경로 (workspaces, users, invites, api_keys, organizations, usage_report, cost_report)
- **Beta API 서브엔드포인트**: files, messages/batches, models, skills + versions 총 30개

### Page Category Breakdown

| Category | Count | Analysis Status | Report |
|----------|-------|-----------------|--------|
| Intro + About Claude (conceptual) | 12 | 완료 ✅ | section-a |
| Build with Claude (guides + features) | 35 | 완료 ✅ | section-b |
| Agents & Tools + Agent SDK | 45 | 완료 ✅ | section-c |
| API Core (overview, sdks, config) | 17 | 완료 ✅ | section-d1 |
| API Core endpoints (messages, models, completions) | 9 | 부분 확인 (d1에서 일부) | section-d1 |
| Admin API 엔드포인트 | 34 | 미분석 ❌ | 없음 |
| Beta API 엔드포인트 | 30 | 미분석 ❌ | 없음 |
| SDK-specific API 레퍼런스 (10 SDKs × ~45) | ~450 | 미분석 ❌ | 없음 |
| Test & Evaluate + Guardrails | 8 | 완료 ✅ | section-d2 |
| Release Notes + Resources | 3 | 완료 ✅ | section-d2 |
| **총계** | **651** | **122 완료 / 529 미분석** | |

---

## Section Accuracy Audit

### Section A: Intro + About Claude

**Sitemap pages (12개):**

| Sitemap Path | In Report? |
|-------------|-----------|
| /docs/en/intro | ❌ 없음 (보고서 14개에 포함 안됨) |
| /docs/en/get-started | ❌ 없음 (보고서 14개에 포함 안됨) |
| /docs/en/about-claude/glossary | ✅ |
| /docs/en/about-claude/model-deprecations | ✅ |
| /docs/en/about-claude/models/choosing-a-model | ✅ |
| /docs/en/about-claude/models/migration-guide | ✅ |
| /docs/en/about-claude/models/overview | ✅ |
| /docs/en/about-claude/models/whats-new-claude-4-6 | ✅ |
| /docs/en/about-claude/pricing | ✅ |
| /docs/en/about-claude/use-case-guides/content-moderation | ✅ |
| /docs/en/about-claude/use-case-guides/customer-support-chat | ✅ |
| /docs/en/about-claude/use-case-guides/legal-summarization | ✅ |
| /docs/en/about-claude/use-case-guides/overview | ✅ |
| /docs/en/about-claude/use-case-guides/ticket-routing | ✅ |

**분석:**
- 사이트맵에는 12개 (intro, get-started 포함)
- Section A 보고서에는 14개 (intro, get-started 검증 포함 — 보고서는 실제로 이 두 페이지를 검증했으나 사이트맵 기준 집계에서는 intro와 get-started를 "about-claude" 섹션이 아닌 루트 레벨로 별도 분류)
- 사이트맵에서 `/docs/en/intro`와 `/docs/en/get-started`는 about-claude 하위가 아닌 루트 레벨에 위치
- **결론**: 보고서는 실제로 사이트맵 12개 + 루트 2개 = 14개를 모두 검증. 내용 정확도: ✅ 양호

### Section B: Build with Claude

**Sitemap pages (35개):**

| Sitemap Path | In Report? |
|-------------|-----------|
| /docs/en/build-with-claude/adaptive-thinking | ✅ |
| /docs/en/build-with-claude/administration-api | ✅ |
| /docs/en/build-with-claude/batch-processing | ✅ |
| /docs/en/build-with-claude/citations | ✅ |
| /docs/en/build-with-claude/claude-code-analytics-api | ✅ |
| /docs/en/build-with-claude/claude-in-microsoft-foundry | ✅ |
| /docs/en/build-with-claude/claude-on-amazon-bedrock | ✅ |
| /docs/en/build-with-claude/claude-on-vertex-ai | ✅ |
| /docs/en/build-with-claude/compaction | ✅ |
| /docs/en/build-with-claude/context-editing | ✅ |
| /docs/en/build-with-claude/context-windows | ✅ |
| /docs/en/build-with-claude/data-residency | ✅ |
| /docs/en/build-with-claude/effort | ✅ |
| /docs/en/build-with-claude/embeddings | ✅ |
| /docs/en/build-with-claude/extended-thinking | ✅ |
| /docs/en/build-with-claude/fast-mode | ✅ |
| /docs/en/build-with-claude/files | ✅ |
| /docs/en/build-with-claude/handling-stop-reasons | ✅ |
| /docs/en/build-with-claude/multilingual-support | ✅ |
| /docs/en/build-with-claude/overview | ✅ |
| /docs/en/build-with-claude/pdf-support | ✅ |
| /docs/en/build-with-claude/prompt-caching | ✅ |
| /docs/en/build-with-claude/prompt-engineering/claude-prompting-best-practices | ✅ |
| /docs/en/build-with-claude/prompt-engineering/overview | ✅ |
| /docs/en/build-with-claude/prompt-engineering/prompting-tools | ✅ |
| /docs/en/build-with-claude/search-results | ✅ |
| /docs/en/build-with-claude/skills-guide | ✅ |
| /docs/en/build-with-claude/streaming | ✅ |
| /docs/en/build-with-claude/structured-outputs | ✅ |
| /docs/en/build-with-claude/token-counting | ✅ |
| /docs/en/build-with-claude/usage-cost-api | ✅ |
| /docs/en/build-with-claude/vision | ✅ |
| /docs/en/build-with-claude/working-with-messages | ✅ |
| /docs/en/build-with-claude/workspaces | ✅ |
| /docs/en/build-with-claude/zero-data-retention | ✅ |

**결론**: 35/35 완벽 일치. ✅ 100% 정확

### Section C: Agents & Tools + Agent SDK

**Sitemap pages (45개):**

**agents-and-tools 하위 (18개):**

| Sitemap Path | In Report? |
|-------------|-----------|
| /docs/en/agents-and-tools/agent-skills/best-practices | ✅ |
| /docs/en/agents-and-tools/agent-skills/enterprise | ✅ |
| /docs/en/agents-and-tools/agent-skills/overview | ✅ |
| /docs/en/agents-and-tools/agent-skills/quickstart | ✅ |
| /docs/en/agents-and-tools/mcp-connector | ✅ |
| /docs/en/agents-and-tools/remote-mcp-servers | ✅ |
| /docs/en/agents-and-tools/tool-use/bash-tool | ✅ |
| /docs/en/agents-and-tools/tool-use/code-execution-tool | ✅ |
| /docs/en/agents-and-tools/tool-use/computer-use-tool | ✅ |
| /docs/en/agents-and-tools/tool-use/fine-grained-tool-streaming | ✅ |
| /docs/en/agents-and-tools/tool-use/implement-tool-use | ✅ |
| /docs/en/agents-and-tools/tool-use/memory-tool | ✅ |
| /docs/en/agents-and-tools/tool-use/overview | ✅ |
| /docs/en/agents-and-tools/tool-use/programmatic-tool-calling | ✅ |
| /docs/en/agents-and-tools/tool-use/text-editor-tool | ✅ |
| /docs/en/agents-and-tools/tool-use/tool-search-tool | ✅ |
| /docs/en/agents-and-tools/tool-use/web-fetch-tool | ✅ |
| /docs/en/agents-and-tools/tool-use/web-search-tool | ✅ |

**agent-sdk 하위 (27개):**

| Sitemap Path | In Report? |
|-------------|-----------|
| /docs/en/agent-sdk/agent-loop | ✅ |
| /docs/en/agent-sdk/claude-code-features | ✅ |
| /docs/en/agent-sdk/cost-tracking | ✅ |
| /docs/en/agent-sdk/custom-tools | ✅ |
| /docs/en/agent-sdk/file-checkpointing | ✅ |
| /docs/en/agent-sdk/hooks | ✅ |
| /docs/en/agent-sdk/hosting | ✅ |
| /docs/en/agent-sdk/mcp | ✅ |
| /docs/en/agent-sdk/migration-guide | ✅ |
| /docs/en/agent-sdk/modifying-system-prompts | ✅ |
| /docs/en/agent-sdk/overview | ✅ |
| /docs/en/agent-sdk/permissions | ✅ |
| /docs/en/agent-sdk/plugins | ✅ |
| /docs/en/agent-sdk/python | ✅ |
| /docs/en/agent-sdk/quickstart | ✅ |
| /docs/en/agent-sdk/secure-deployment | ✅ |
| /docs/en/agent-sdk/sessions | ✅ |
| /docs/en/agent-sdk/skills | ✅ |
| /docs/en/agent-sdk/slash-commands | ✅ |
| /docs/en/agent-sdk/streaming-output | ✅ |
| /docs/en/agent-sdk/streaming-vs-single-mode | ✅ |
| /docs/en/agent-sdk/structured-outputs | ✅ |
| /docs/en/agent-sdk/subagents | ✅ |
| /docs/en/agent-sdk/todo-tracking | ✅ |
| /docs/en/agent-sdk/typescript | ✅ |
| /docs/en/agent-sdk/typescript-v2-preview | ✅ |
| /docs/en/agent-sdk/user-input | ✅ |

**결론**: 45/45 완벽 일치. ✅ 100% 정확

### Section D-1: API (CORRECTED)

**원래 분석 범위 (17개 사이트맵 + 1 보너스 = 18개):**

| Sitemap Path | In D-1 Report? |
|-------------|---------------|
| /docs/en/api/overview | ✅ |
| /docs/en/api/client-sdks | ✅ |
| /docs/en/api/rate-limits | ✅ |
| /docs/en/api/errors | ✅ |
| /docs/en/api/versioning | ✅ |
| /docs/en/api/beta-headers | ✅ |
| /docs/en/api/service-tiers | ✅ |
| /docs/en/api/supported-regions | ✅ |
| /docs/en/api/ip-addresses | ✅ |
| /docs/en/api/openai-sdk | ✅ |
| /docs/en/api/sdks/python | ✅ |
| /docs/en/api/sdks/typescript | ✅ |
| /docs/en/api/sdks/java | ✅ |
| /docs/en/api/sdks/go | ✅ |
| /docs/en/api/sdks/csharp | ✅ |
| /docs/en/api/sdks/ruby | ✅ |
| /docs/en/api/sdks/php | ✅ |
| /docs/en/api/messages | ✅ (보너스 발견) |

**실제 사이트맵 API 섹션 전체 규모:**

원래 D-1 보고서에서 검증된 18개는 전체 API 섹션의 약 3.1%에 불과. 실제 사이트맵의 API 관련 페이지 수:

| API 하위 섹션 | 사이트맵 페이지 수 | D-1 보고서 커버 |
|-------------|----------------|--------------|
| api/ (루트 레벨 + sdks) | 17 + /api/messages 등 | ✅ 17개 완료 |
| /api/messages/* (core) | 9개 | 부분 (messages 허브만) |
| /api/admin/* | 34개 | ❌ 미분석 |
| /api/beta/* | 30개 | ❌ 미분석 |
| /api/completions/* | 2개 | ❌ 미분석 |
| /api/models/* | 3개 | ❌ 미분석 |
| /api/python/* | 45개 | ❌ 미분석 |
| /api/typescript/* | 45개 | ❌ 미분석 |
| /api/java/* | 45개 | ❌ 미분석 |
| /api/go/* | 45개 | ❌ 미분석 |
| /api/csharp/* | 45개 | ❌ 미분석 |
| /api/ruby/* | 45개 | ❌ 미분석 |
| /api/php/* | 45개 | ❌ 미분석 |
| /api/kotlin/* | 45개 | ❌ 미분석 |
| /api/terraform/* | 45개 | ❌ 미분석 |
| /api/cli/* | 45개 | ❌ 미분석 |
| **총계** | **~590개** | **17개 완료** |

**핵심 미분석 페이지 목록 (사이트맵 확인):**

Core API 엔드포인트 (분류: `api/` 직접 하위):
- /docs/en/api/admin (섹션 허브)
- /docs/en/api/admin/api_keys
- /docs/en/api/admin/api_keys/list
- /docs/en/api/admin/api_keys/retrieve
- /docs/en/api/admin/api_keys/update
- /docs/en/api/admin/cost_report
- /docs/en/api/admin/cost_report/retrieve
- /docs/en/api/admin/invites
- /docs/en/api/admin/invites/create
- /docs/en/api/admin/invites/delete
- /docs/en/api/admin/invites/list
- /docs/en/api/admin/invites/retrieve
- /docs/en/api/admin/organizations
- /docs/en/api/admin/organizations/me
- /docs/en/api/admin/usage_report
- /docs/en/api/admin/usage_report/retrieve_claude_code
- /docs/en/api/admin/usage_report/retrieve_messages
- /docs/en/api/admin/users
- /docs/en/api/admin/users/delete
- /docs/en/api/admin/users/list
- /docs/en/api/admin/users/retrieve
- /docs/en/api/admin/users/update
- /docs/en/api/admin/workspaces
- /docs/en/api/admin/workspaces/archive
- /docs/en/api/admin/workspaces/create
- /docs/en/api/admin/workspaces/list
- /docs/en/api/admin/workspaces/members
- /docs/en/api/admin/workspaces/members/create
- /docs/en/api/admin/workspaces/members/delete
- /docs/en/api/admin/workspaces/members/list
- /docs/en/api/admin/workspaces/members/retrieve
- /docs/en/api/admin/workspaces/members/update
- /docs/en/api/admin/workspaces/retrieve
- /docs/en/api/admin/workspaces/update
- /docs/en/api/beta (섹션 허브)
- /docs/en/api/beta/files
- /docs/en/api/beta/files/delete
- /docs/en/api/beta/files/download
- /docs/en/api/beta/files/list
- /docs/en/api/beta/files/retrieve_metadata
- /docs/en/api/beta/files/upload
- /docs/en/api/beta/messages
- /docs/en/api/beta/messages/batches
- /docs/en/api/beta/messages/batches/cancel
- /docs/en/api/beta/messages/batches/create
- /docs/en/api/beta/messages/batches/delete
- /docs/en/api/beta/messages/batches/list
- /docs/en/api/beta/messages/batches/results
- /docs/en/api/beta/messages/batches/retrieve
- /docs/en/api/beta/messages/count_tokens
- /docs/en/api/beta/messages/create
- /docs/en/api/beta/models
- /docs/en/api/beta/models/list
- /docs/en/api/beta/models/retrieve
- /docs/en/api/beta/skills
- /docs/en/api/beta/skills/create
- /docs/en/api/beta/skills/delete
- /docs/en/api/beta/skills/list
- /docs/en/api/beta/skills/retrieve
- /docs/en/api/beta/skills/versions
- /docs/en/api/beta/skills/versions/create
- /docs/en/api/beta/skills/versions/delete
- /docs/en/api/beta/skills/versions/list
- /docs/en/api/beta/skills/versions/retrieve
- /docs/en/api/completions
- /docs/en/api/completions/create
- /docs/en/api/messages/batches
- /docs/en/api/messages/batches/cancel
- /docs/en/api/messages/batches/create
- /docs/en/api/messages/batches/delete
- /docs/en/api/messages/batches/list
- /docs/en/api/messages/batches/results
- /docs/en/api/messages/batches/retrieve
- /docs/en/api/messages/count_tokens
- /docs/en/api/messages/create
- /docs/en/api/models
- /docs/en/api/models/list
- /docs/en/api/models/retrieve

SDK-별 레퍼런스 페이지 (10 SDKs × ~45 페이지 = ~450페이지):
- /api/python/*, /api/typescript/*, /api/java/*, /api/go/*
- /api/csharp/*, /api/ruby/*, /api/php/*, /api/kotlin/*
- /api/terraform/*, /api/cli/*
- 각 SDK당: messages/*, messages/batches/*, models/*, completions/*, beta/*

**D-1 미분석 페이지에서 발견된 D-1 보고서 경로 불일치:**

D-1 보고서가 참조한 일부 경로가 실제 사이트맵과 다름:
| D-1 보고서 발견 경로 | 실제 사이트맵 경로 | 비고 |
|-------------------|-----------------|------|
| /docs/en/api/admin-api/workspaces/get-workspace | /docs/en/api/admin/workspaces/retrieve | 경로 구조 불일치 |
| /docs/en/api/admin-api/users/get-user | /docs/en/api/admin/users/retrieve | 경로 구조 불일치 |
| /docs/en/api/admin-api/apikeys/get-api-key | /docs/en/api/admin/api_keys/retrieve | 경로 구조 불일치 |
| /docs/en/api/admin-api/organization/get-me | /docs/en/api/admin/organizations/me | 경로 구조 불일치 |
| /docs/en/api/admin-api/usage-cost/get-messages-usage-report | /docs/en/api/admin/usage_report/retrieve_messages | 경로 구조 불일치 |
| /docs/en/api/skills/create-skill | /docs/en/api/beta/skills/create | 경로 구조 불일치 |
| /docs/en/api/files-create | /docs/en/api/beta/files/upload | 경로 구조 불일치 |

> 참고: D-1 보고서가 발견한 경로들은 실제 페이지에서 수집한 링크이므로 redirect나 별칭 경로일 수 있음. 사이트맵의 경로가 canonical 경로.

### Section D-2: Test & Evaluate + Release Notes + Resources

**Sitemap pages (11개):**

| Sitemap Path | In Report? |
|-------------|-----------|
| /docs/en/test-and-evaluate/develop-tests | ✅ |
| /docs/en/test-and-evaluate/eval-tool | ✅ |
| /docs/en/test-and-evaluate/strengthen-guardrails/handle-streaming-refusals | ✅ |
| /docs/en/test-and-evaluate/strengthen-guardrails/increase-consistency | ✅ |
| /docs/en/test-and-evaluate/strengthen-guardrails/mitigate-jailbreaks | ✅ |
| /docs/en/test-and-evaluate/strengthen-guardrails/reduce-hallucinations | ✅ |
| /docs/en/test-and-evaluate/strengthen-guardrails/reduce-latency | ✅ |
| /docs/en/test-and-evaluate/strengthen-guardrails/reduce-prompt-leak | ✅ |
| /docs/en/release-notes/overview | ✅ |
| /docs/en/release-notes/system-prompts | ✅ |
| /docs/en/resources/overview | ✅ |

**결론**: 11/11 완벽 일치. ✅ 100% 정확

---

## Cross-Reference Validation

### Pages Discovered by Section Reports but NOT in Sitemap

섹션 보고서들이 "discovered"로 표시했으나 실제 사이트맵(/tmp/en-docs.txt)에 없는 경로:

| Discovered Path | Discovered By | 비고 |
|----------------|--------------|------|
| /docs/en/api/admin-api/workspaces/get-workspace | Section B | 경로 형식 불일치 — 실제: /api/admin/workspaces/retrieve |
| /docs/en/api/admin-api/workspace_members/get-workspace-member | Section B | 경로 형식 불일치 — 실제: /api/admin/workspaces/members/retrieve |
| /docs/en/api/admin-api/workspaces/list-workspaces | Section B | 경로 형식 불일치 — 실제: /api/admin/workspaces/list |
| /docs/en/api/admin-api/users/get-user | Section B | 경로 형식 불일치 — 실제: /api/admin/users/retrieve |
| /docs/en/api/admin-api/invites/get-invite | Section B | 경로 형식 불일치 — 실제: /api/admin/invites/retrieve |
| /docs/en/api/admin-api/apikeys/get-api-key | Section B | 경로 형식 불일치 — 실제: /api/admin/api_keys/retrieve |
| /docs/en/api/admin-api/organization/get-me | Section B, D-2 | 경로 형식 불일치 — 실제: /api/admin/organizations/me |
| /docs/en/api/admin-api/usage-cost/get-messages-usage-report | Section B | 경로 형식 불일치 — 실제: /api/admin/usage_report/retrieve_messages |
| /docs/en/api/admin-api/usage-cost/get-cost-report | Section B | 경로 형식 불일치 — 실제: /api/admin/cost_report/retrieve |
| /docs/en/api/admin-api/apikeys/list-api-keys | Section B | 경로 형식 불일치 — 실제: /api/admin/api_keys/list |
| /docs/en/api/admin-api/claude-code/get-claude-code-usage-report | Section B | 경로 형식 불일치 — 실제: /api/admin/usage_report/retrieve_claude_code |
| /docs/en/api/admin | Section D-1 | ✅ 사이트맵 존재 (58번 줄) |
| /docs/en/api/beta | Section D-1 | ✅ 사이트맵 존재 (92번 줄) |
| /docs/en/api/creating-message-batches | Section B, D-1 | ❌ 사이트맵에 없음 — 구 경로, redirect 가능성 |
| /docs/en/api/messages-count-tokens | Section D-1 | ❌ 사이트맵에 없음 — 구 경로, 실제: /api/messages/count_tokens |
| /docs/en/api/models-list | Section D-1, D-2 | ❌ 사이트맵에 없음 — 구 경로, 실제: /api/models/list |
| /docs/en/api/files-api | Section C | ❌ 사이트맵에 없음 — 구 경로, 실제: /api/beta/files |
| /docs/en/api/files-create | Section B, C | ❌ 사이트맵에 없음 — 구 경로, 실제: /api/beta/files/upload |
| /docs/en/api/files-content | Section B | ❌ 사이트맵에 없음 — 구 경로, 실제: /api/beta/files/download |
| /docs/en/api/skills/list-skills | Section B | ❌ 사이트맵에 없음 — 구 경로, 실제: /api/beta/skills/list |
| /docs/en/api/skills/list-skill-versions | Section B | ❌ 사이트맵에 없음 — 구 경로, 실제: /api/beta/skills/versions/list |
| /docs/en/api/skills/create-skill | Section B, D-2 | ❌ 사이트맵에 없음 — 구 경로, 실제: /api/beta/skills/create |
| /docs/en/api/deleting-message-batches | Section D-2 | ❌ 사이트맵에 없음 — 구 경로, 실제: /api/messages/batches/delete |
| /docs/en/agents-and-tools/mcp | Section D-1 | ❌ 사이트맵에 없음 |
| /docs/en/api/beta/skills/list | (sitemap) | ❌ D-1이 잘못된 경로로 참조함 |
| /docs/en/mcp | Section A | ❌ 사이트맵에 없음 — 별도 섹션 또는 외부 |
| /docs/en/home | Section D-1 | ❌ 사이트맵에 없음 — 루트/홈 리다이렉트 |
| /docs/en/claude_api_primer | Section D-2 | ❌ 사이트맵에 없음 — 별도 문서 |
| /docs/en/api/admin-api/* (모든 -api- 형식) | Section B | ❌ 일괄 불일치 — 실제 경로: /api/admin/* |

**핵심 발견**: 섹션 보고서들이 참조한 `/api/admin-api/` 경로들은 실제 사이트맵에서 `/api/admin/` 경로로 존재. 이는 페이지 내 링크가 canonical 경로와 다른 별칭을 사용하거나, 분석 시점과 사이트맵 생성 시점 사이에 URL 구조가 변경되었을 가능성을 시사함.

### Pages in Sitemap but NOT Covered by ANY Section Report

이 목록은 사이트맵의 651개 URL 중 5개 섹션 보고서 어디에도 등장하지 않는 페이지들:

**API Core endpoints (미커버):**
- /docs/en/api/messages/batches (배치 섹션 허브 — messages는 커버되었으나 batches 허브는 별도)
- /docs/en/api/messages/batches/cancel
- /docs/en/api/messages/batches/create
- /docs/en/api/messages/batches/delete
- /docs/en/api/messages/batches/list
- /docs/en/api/messages/batches/results
- /docs/en/api/messages/batches/retrieve
- /docs/en/api/messages/count_tokens
- /docs/en/api/messages/create
- /docs/en/api/models
- /docs/en/api/models/list
- /docs/en/api/models/retrieve
- /docs/en/api/completions
- /docs/en/api/completions/create

**Admin API 섹션 전체 (34개 미커버):**
- /docs/en/api/admin/api_keys
- /docs/en/api/admin/api_keys/list
- /docs/en/api/admin/api_keys/retrieve
- /docs/en/api/admin/api_keys/update
- /docs/en/api/admin/cost_report
- /docs/en/api/admin/cost_report/retrieve
- /docs/en/api/admin/invites
- /docs/en/api/admin/invites/create
- /docs/en/api/admin/invites/delete
- /docs/en/api/admin/invites/list
- /docs/en/api/admin/invites/retrieve
- /docs/en/api/admin/organizations
- /docs/en/api/admin/organizations/me
- /docs/en/api/admin/usage_report
- /docs/en/api/admin/usage_report/retrieve_claude_code
- /docs/en/api/admin/usage_report/retrieve_messages
- /docs/en/api/admin/users
- /docs/en/api/admin/users/delete
- /docs/en/api/admin/users/list
- /docs/en/api/admin/users/retrieve
- /docs/en/api/admin/users/update
- /docs/en/api/admin/workspaces
- /docs/en/api/admin/workspaces/archive
- /docs/en/api/admin/workspaces/create
- /docs/en/api/admin/workspaces/list
- /docs/en/api/admin/workspaces/members
- /docs/en/api/admin/workspaces/members/create
- /docs/en/api/admin/workspaces/members/delete
- /docs/en/api/admin/workspaces/members/list
- /docs/en/api/admin/workspaces/members/retrieve
- /docs/en/api/admin/workspaces/members/update
- /docs/en/api/admin/workspaces/retrieve
- /docs/en/api/admin/workspaces/update

**Beta API 섹션 전체 (30개 미커버):**
- /docs/en/api/beta/files (및 하위 5개)
- /docs/en/api/beta/messages (및 batches 하위 7개, count_tokens, create)
- /docs/en/api/beta/models (및 list, retrieve)
- /docs/en/api/beta/skills (및 create, delete, list, retrieve)
- /docs/en/api/beta/skills/versions (및 create, delete, list, retrieve)

**SDK-specific 레퍼런스 (약 450개 전체 미커버):**
- /docs/en/api/python/* (45개)
- /docs/en/api/typescript/* (45개)
- /docs/en/api/java/* (45개)
- /docs/en/api/go/* (45개)
- /docs/en/api/csharp/* (45개)
- /docs/en/api/ruby/* (45개)
- /docs/en/api/php/* (45개)
- /docs/en/api/kotlin/* (45개)
- /docs/en/api/terraform/* (45개)
- /docs/en/api/cli/* (45개)

---

## Accuracy Summary

| Section | Sitemap Pages | Reported Pages | Coverage | Accuracy |
|---------|--------------|----------------|----------|----------|
| A: Intro + About | 12 (+2 루트) | 14 | 100% | ✅ 정확 |
| B: Build with Claude | 35 | 35 | 100% | ✅ 정확 |
| C: Agents + SDK | 45 | 45 | 100% | ✅ 정확 |
| D-1: API Core | 17 | 17 (+1 bonus) | 3.1% of total API | ✅ 범위 내 정확 / ⚠️ 범위 부족 |
| D-2: Test + Release + Resources | 11 | 11 | 100% | ✅ 정확 |
| **API SDK-specific (미분석)** | **~530** | **0** | **0%** | ❌ 미커버 |
| **전체** | **651** | **122** | **18.7%** | **✅ 커버 내 정확 / ❌ 529 미커버** |

### Coverage Breakdown by Section (사이트맵 기준)

| 사이트맵 섹션 | 페이지 수 | 분석 완료 | 미분석 |
|------------|---------|---------|-------|
| about-claude | 12 | 12 | 0 |
| agent-sdk | 27 | 27 | 0 |
| agents-and-tools | 18 | 18 | 0 |
| api (core: overview~versioning) | 17 | 17 | 0 |
| api/messages/* | 9 | 1 (허브) | 8 |
| api/models/* | 3 | 0 | 3 |
| api/completions/* | 2 | 0 | 2 |
| api/admin/* | 34 | 0 | 34 |
| api/beta/* | 30 | 0 | 30 |
| api/python/* | 45 | 0 | 45 |
| api/typescript/* | 45 | 0 | 45 |
| api/java/* | 45 | 0 | 45 |
| api/go/* | 45 | 0 | 45 |
| api/csharp/* | 45 | 0 | 45 |
| api/ruby/* | 45 | 0 | 45 |
| api/php/* | 45 | 0 | 45 |
| api/kotlin/* | 45 | 0 | 45 |
| api/terraform/* | 45 | 0 | 45 |
| api/cli/* | 45 | 0 | 45 |
| build-with-claude | 35 | 35 | 0 |
| get-started + intro | 2 | 2 | 0 |
| release-notes | 2 | 2 | 0 |
| resources | 1 | 1 | 0 |
| test-and-evaluate | 8 | 8 | 0 |
| **총계** | **651** | **122** | **529** |

---

## Recommendations

### Priority 1: Section D-1 범위 정정 (즉시)

Section D-1 보고서에 Scope Correction 섹션 추가가 필요함. 실제 API 섹션은 590개 이상의 페이지를 포함하며, 현재 보고서는 그중 핵심 구성/설정 페이지 17개만 커버.

### Priority 2: API 엔드포인트 레퍼런스 분석 (Round 3)

다음 섹션에 대한 추가 분석 보고서 생성이 필요:

1. **Section D-3: Core API Endpoints** — api/messages/*, api/models/*, api/completions/*, api/admin/*, api/beta/* (약 90개)
2. **Section D-4: SDK-specific References** — 10개 SDK별 레퍼런스 페이지 (약 450개)
   - SDK별 페이지 구조는 반복적이므로 한 SDK를 완전 분석 후 패턴 문서화 권장
   - 우선순위: python → typescript → java → go → 나머지

### Priority 3: URL 경로 불일치 해소

섹션 보고서들이 참조한 `/api/admin-api/` 형식 경로들이 사이트맵의 `/api/admin/` 형식과 다름. 해당 경로들의 실제 상태(redirect vs 404)를 직접 확인 권장.

### Priority 4: 누락 sitemap 항목 확인

다음 경로들이 페이지 내 링크에서 발견되었으나 사이트맵에 없음 — 실제 404 여부 확인 필요:
- /docs/en/mcp (MCP 문서 루트)
- /docs/en/agents-and-tools/mcp (TypeScript SDK에서 발견)
- /docs/en/home (최상위 홈)
- /docs/en/api/creating-message-batches (구 경로)

### Priority 5: 보고서 정확도 유지

기존 5개 섹션 보고서 (A, B, C, D-1 core, D-2)는 내용 정확도 높음. 현재 보고서들이 커버한 범위 내에서는 신뢰할 수 있음. 단, D-1 보고서의 "discovered pages" 섹션에 있는 /api/admin-api/* 경로들은 실제 사이트맵 경로와 불일치하므로 주석 처리 권장.

---

## Appendix: Sitemap URL Count by Prefix

사이트맵 651개 URL의 prefix별 분포 (분석 기준):

| URL Prefix | Count |
|-----------|-------|
| /docs/en/api/python/ | 45 |
| /docs/en/api/typescript/ | 45 |
| /docs/en/api/java/ | 45 |
| /docs/en/api/go/ | 45 |
| /docs/en/api/csharp/ | 45 |
| /docs/en/api/ruby/ | 45 |
| /docs/en/api/php/ | 45 |
| /docs/en/api/kotlin/ | 45 |
| /docs/en/api/terraform/ | 45 |
| /docs/en/api/cli/ | 45 |
| /docs/en/api/beta/ | 30 |
| /docs/en/api/admin/ | 34 |
| /docs/en/api/ (루트 + sdks + 기타) | 22 |
| /docs/en/build-with-claude/ | 35 |
| /docs/en/agent-sdk/ | 27 |
| /docs/en/agents-and-tools/ | 18 |
| /docs/en/about-claude/ | 12 |
| /docs/en/test-and-evaluate/ | 8 |
| /docs/en/ (루트: intro, get-started) | 2 |
| /docs/en/release-notes/ | 2 |
| /docs/en/resources/ | 1 |
| **총계** | **651** |

*Note: 10개 SDK별 레퍼런스는 동일한 엔드포인트 구조를 반복하므로 content 고유성 측면에서는 `api/beta/` + `api/admin/` + core endpoints (~90개)가 실질적 신규 정보를 담고 있음.*
