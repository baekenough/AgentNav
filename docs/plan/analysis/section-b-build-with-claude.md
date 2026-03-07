# Section B: Build with Claude — Verification Report

## Summary
- Total pages checked: 35
- Verified: 35
- Failed: 0
- New pages discovered: 38

## Page Catalog

| # | Path | Status | Title | Type | Description |
|---|------|--------|-------|------|-------------|
| 1 | /docs/en/build-with-claude/overview | ✅ | Features overview | overview | Claude API 기능 총정리 (모델 기능, 도구, 인프라, 컨텍스트 관리, 파일/자산) |
| 2 | /docs/en/build-with-claude/working-with-messages | ✅ | Using the Messages API | guide | Messages API 실용 패턴 (기본 요청, 멀티턴, 프리필, 비전) |
| 3 | /docs/en/build-with-claude/handling-stop-reasons | ✅ | Handling stop reasons | reference | stop_reason 필드 값 (end_turn, max_tokens, tool_use, pause_turn, refusal 등) 처리 방법 |
| 4 | /docs/en/build-with-claude/prompt-engineering/overview | ✅ | Prompt engineering overview | overview | 프롬프트 엔지니어링 시작점, 성공 기준 정의 후 개선 가이드 |
| 5 | /docs/en/build-with-claude/prompt-engineering/claude-prompting-best-practices | ✅ | Prompting best practices | guide | Claude 4.6 모델용 포괄적 프롬프팅 기법 (명확성, 예제, XML, 도구, 에이전트 시스템) |
| 6 | /docs/en/build-with-claude/prompt-engineering/prompting-tools | ✅ | Console prompting tools | guide | Console 프롬프트 도구 (생성기, 템플릿/변수, 개선기) |
| 7 | /docs/en/build-with-claude/extended-thinking | ✅ | Building with extended thinking | feature-doc | 확장 사고 기능 (설정, 스트리밍, 도구 사용, 프롬프트 캐싱 연동) |
| 8 | /docs/en/build-with-claude/adaptive-thinking | ✅ | Adaptive thinking | feature-doc | 적응형 사고 모드 (Claude가 동적으로 사고 깊이 결정, Opus 4.6/Sonnet 4.6 지원) |
| 9 | /docs/en/build-with-claude/effort | ✅ | Effort | feature-doc | effort 파라미터로 응답 토큰 사용량 제어 (max/high/medium/low) |
| 10 | /docs/en/build-with-claude/fast-mode | ✅ | Fast mode (research preview) | feature-doc | Opus 4.6 빠른 추론 모드 (2.5배 빠른 출력, 6배 프리미엄 가격) |
| 11 | /docs/en/build-with-claude/structured-outputs | ✅ | Structured outputs | feature-doc | JSON 스키마 준수 출력 보장 (JSON outputs + strict tool use) |
| 12 | /docs/en/build-with-claude/citations | ✅ | Citations | feature-doc | 문서 기반 인용 기능 (PDF, 텍스트, 커스텀 콘텐츠 지원) |
| 13 | /docs/en/build-with-claude/streaming | ✅ | Streaming Messages | reference | SSE 기반 스트리밍 응답 (이벤트 타입, SDK 사용법) |
| 14 | /docs/en/build-with-claude/batch-processing | ✅ | Batch processing | feature-doc | 비동기 대량 요청 처리 (50% 비용 절감, Message Batches API) |
| 15 | /docs/en/build-with-claude/pdf-support | ✅ | PDF support | feature-doc | PDF 텍스트/차트/이미지 분석 (32MB/100페이지 제한, URL/base64/Files API) |
| 16 | /docs/en/build-with-claude/search-results | ✅ | Search results | feature-doc | RAG 앱용 자연스러운 인용 (검색 결과 블록으로 소스 귀속) |
| 17 | /docs/en/build-with-claude/multilingual-support | ✅ | Multilingual support | feature-doc | 다국어 성능 데이터 (15개 언어 MMLU 벤치마크, 영어 대비 상대 성능) |
| 18 | /docs/en/build-with-claude/embeddings | ✅ | Embeddings | guide | 텍스트 임베딩 가이드 (Anthropic 자체 모델 없음, Voyage AI 권장) |
| 19 | /docs/en/build-with-claude/vision | ✅ | Vision | feature-doc | 이미지 이해 기능 (JPEG/PNG/GIF/WebP, base64/URL/Files API, 제한사항) |
| 20 | /docs/en/build-with-claude/prompt-caching | ✅ | Prompt caching | feature-doc | 프롬프트 캐싱으로 비용/지연 최적화 (자동 캐싱, 1시간 캐시) |
| 21 | /docs/en/build-with-claude/context-windows | ✅ | Context windows | feature-doc | 컨텍스트 윈도우 관리 (200K/1M 토큰, 확장사고 연동, 컨텍스트 인식) |
| 22 | /docs/en/build-with-claude/compaction | ✅ | Compaction | feature-doc | 서버 사이드 컨텍스트 압축 (긴 대화 관리, Opus 4.6/Sonnet 4.6) |
| 23 | /docs/en/build-with-claude/context-editing | ✅ | Context editing | feature-doc | 대화 컨텍스트 세밀 관리 (도구 결과 클리어, 사고 블록 클리어) |
| 24 | /docs/en/build-with-claude/files | ✅ | Files API | feature-doc | 파일 업로드/관리 API (PDF/이미지/텍스트, 500MB 제한, 베타) |
| 25 | /docs/en/build-with-claude/token-counting | ✅ | Token counting | feature-doc | 전송 전 토큰 수 추정 (무료, 이미지/PDF/도구/사고 지원) |
| 26 | /docs/en/build-with-claude/data-residency | ✅ | Data residency | feature-doc | 데이터 레지던시 제어 (inference_geo: us/global, 워크스페이스 지역) |
| 27 | /docs/en/build-with-claude/claude-on-amazon-bedrock | ✅ | Claude on Amazon Bedrock | guide | Bedrock에서 Claude 사용 (SDK 설정, 모델 ID, 글로벌/리전 엔드포인트) |
| 28 | /docs/en/build-with-claude/claude-on-vertex-ai | ✅ | Claude on Vertex AI | guide | Vertex AI에서 Claude 사용 (SDK 설정, 모델 ID, 글로벌/리전 엔드포인트) |
| 29 | /docs/en/build-with-claude/claude-in-microsoft-foundry | ✅ | Claude in Microsoft Foundry | guide | Microsoft Foundry에서 Claude 사용 (Azure 인증, SDK 설정, 배포 관리) |
| 30 | /docs/en/build-with-claude/skills-guide | ✅ | Using Agent Skills with the API | guide | Agent Skills API 가이드 (사전 구축 + 커스텀 스킬, Messages API 통합, 파일 다운로드) |
| 31 | /docs/en/build-with-claude/workspaces | ✅ | Workspaces | feature-doc | 워크스페이스로 API 키/팀 접근/비용 관리 (역할, 리소스 스코핑, 제한 설정) |
| 32 | /docs/en/build-with-claude/zero-data-retention | ✅ | Zero Data Retention (ZDR) | reference | ZDR 정책 상세 (적용 가능 엔드포인트, 비적용 항목, 특수 사례) |
| 33 | /docs/en/build-with-claude/administration-api | ✅ | Admin API overview | guide | Admin API 개요 (조직 멤버, 워크스페이스, API 키 프로그래밍 관리) |
| 34 | /docs/en/build-with-claude/usage-cost-api | ✅ | Usage and Cost API | reference | 사용량/비용 데이터 프로그래밍 접근 (토큰 추적, 비용 분석, 파트너 통합) |
| 35 | /docs/en/build-with-claude/claude-code-analytics-api | ✅ | Claude Code Analytics API | reference | Claude Code 사용 분석 API (개발자 생산성, 도구 사용률, 비용 분석) |

## Discovered Pages (not in sitemap)

Below are internal `/docs/en/...` links discovered during page fetching that may not be in the master sitemap list. These represent pages that should be verified for inclusion.

### From Page 1: /docs/en/build-with-claude/overview
| Discovered Link | Notes |
|----------------|-------|
| /docs/en/agents-and-tools/tool-use/code-execution-tool | Code execution tool |
| /docs/en/agents-and-tools/tool-use/web-fetch-tool | Web fetch tool |
| /docs/en/agents-and-tools/tool-use/web-search-tool | Web search tool |
| /docs/en/agents-and-tools/tool-use/bash-tool | Bash tool |
| /docs/en/agents-and-tools/tool-use/computer-use-tool | Computer use tool |
| /docs/en/agents-and-tools/tool-use/memory-tool | Memory tool |
| /docs/en/agents-and-tools/tool-use/text-editor-tool | Text editor tool |
| /docs/en/agents-and-tools/agent-skills/overview | Agent skills overview |
| /docs/en/agents-and-tools/tool-use/fine-grained-tool-streaming | Fine-grained tool streaming |
| /docs/en/agents-and-tools/mcp-connector | MCP connector |

### From Page 2: /docs/en/build-with-claude/working-with-messages
| Discovered Link | Notes |
|----------------|-------|
| /docs/en/api/messages | Messages API reference |

### From Page 7: /docs/en/build-with-claude/extended-thinking
| Discovered Link | Notes |
|----------------|-------|
| /docs/en/agents-and-tools/tool-use/programmatic-tool-calling | Programmatic tool calling |

### From Page 8: /docs/en/build-with-claude/adaptive-thinking
| Discovered Link | Notes |
|----------------|-------|
| /docs/en/about-claude/models/whats-new-claude-4-6 | What's new in Claude 4.6 |

### From Page 11: /docs/en/build-with-claude/structured-outputs
| Discovered Link | Notes |
|----------------|-------|
| /docs/en/agents-and-tools/tool-use/implement-tool-use | Implement tool use |

### From Page 14: /docs/en/build-with-claude/batch-processing
| Discovered Link | Notes |
|----------------|-------|
| /docs/en/api/creating-message-batches | Creating message batches API ref |

### From Page 15: /docs/en/build-with-claude/pdf-support
| Discovered Link | Notes |
|----------------|-------|
| /docs/en/api/files-create | Files create API ref |

### From Page 21: /docs/en/build-with-claude/context-windows
| Discovered Link | Notes |
|----------------|-------|
| /docs/en/about-claude/models/migration-guide | Migration guide |

### From Page 24: /docs/en/build-with-claude/files
| Discovered Link | Notes |
|----------------|-------|
| /docs/en/api/files-create | Files create API ref (also from pdf-support) |

### From Page 29: /docs/en/build-with-claude/claude-in-microsoft-foundry
| Discovered Link | Notes |
|----------------|-------|
| /docs/en/api/client-sdks | Client SDKs |
| /docs/en/about-claude/pricing | Pricing (third-party platform pricing) |

### From Page 30: /docs/en/build-with-claude/skills-guide
| Discovered Link | Notes |
|----------------|-------|
| /docs/en/api/skills/list-skills | Skills list API ref |
| /docs/en/api/skills/list-skill-versions | Skill versions API ref |
| /docs/en/agents-and-tools/agent-skills/quickstart | Agent skills quickstart |
| /docs/en/agents-and-tools/agent-skills/best-practices | Agent skills best practices |
| /docs/en/api/skills/create-skill | Create skill API ref |
| /docs/en/api/files-content | Files content API ref |

### From Page 31: /docs/en/build-with-claude/workspaces
| Discovered Link | Notes |
|----------------|-------|
| /docs/en/api/admin-api/workspaces/get-workspace | Workspaces API ref |
| /docs/en/api/admin-api/workspace_members/get-workspace-member | Workspace members API ref |
| /docs/en/api/admin-api/workspaces/list-workspaces | List workspaces API ref |
| /docs/en/api/rate-limits | Rate limits |

### From Page 32: /docs/en/build-with-claude/zero-data-retention
| Discovered Link | Notes |
|----------------|-------|
| /docs/en/agents-and-tools/tool-use/web-search-tool | Web search tool (also from overview) |
| /docs/en/agents-and-tools/tool-use/web-fetch-tool | Web fetch tool (also from overview) |
| /docs/en/agents-and-tools/tool-use/tool-search-tool | Tool search tool |
| /docs/en/api/files-create | Files create API ref (also from pdf-support, files) |
| /docs/en/agent-sdk/sessions | Agent SDK sessions |

### From Page 33: /docs/en/build-with-claude/administration-api
| Discovered Link | Notes |
|----------------|-------|
| /docs/en/api/admin | Admin API reference |
| /docs/en/api/admin-api/users/get-user | Get user API ref |
| /docs/en/api/admin-api/invites/get-invite | Get invite API ref |
| /docs/en/api/admin-api/apikeys/get-api-key | Get API key API ref |
| /docs/en/api/admin-api/organization/get-me | Get organization info API ref |

### From Page 34: /docs/en/build-with-claude/usage-cost-api
| Discovered Link | Notes |
|----------------|-------|
| /docs/en/api/admin-api/usage-cost/get-messages-usage-report | Usage report API ref |
| /docs/en/api/admin-api/usage-cost/get-cost-report | Cost report API ref |
| /docs/en/api/admin-api/apikeys/list-api-keys | List API keys API ref |
| /docs/en/api/service-tiers | Service tiers |

### From Page 35: /docs/en/build-with-claude/claude-code-analytics-api
| Discovered Link | Notes |
|----------------|-------|
| /docs/en/api/admin-api/claude-code/get-claude-code-usage-report | Claude Code usage report API ref |

## Unique Discovered Pages (Deduplicated)

The following 38 unique internal doc pages were discovered from Section B pages that are NOT part of the 35-page Section B list itself. These should be cross-referenced with the full 122-page sitemap:

### agents-and-tools section
1. /docs/en/agents-and-tools/tool-use/code-execution-tool
2. /docs/en/agents-and-tools/tool-use/web-fetch-tool
3. /docs/en/agents-and-tools/tool-use/web-search-tool
4. /docs/en/agents-and-tools/tool-use/bash-tool
5. /docs/en/agents-and-tools/tool-use/computer-use-tool
6. /docs/en/agents-and-tools/tool-use/memory-tool
7. /docs/en/agents-and-tools/tool-use/text-editor-tool
8. /docs/en/agents-and-tools/agent-skills/overview
9. /docs/en/agents-and-tools/tool-use/fine-grained-tool-streaming
10. /docs/en/agents-and-tools/mcp-connector
11. /docs/en/agents-and-tools/tool-use/programmatic-tool-calling
12. /docs/en/agents-and-tools/tool-use/implement-tool-use
13. /docs/en/agents-and-tools/tool-use/tool-search-tool
14. /docs/en/agents-and-tools/agent-skills/quickstart
15. /docs/en/agents-and-tools/agent-skills/best-practices

### api section
16. /docs/en/api/messages
17. /docs/en/api/creating-message-batches
18. /docs/en/api/files-create
19. /docs/en/api/client-sdks
20. /docs/en/api/skills/list-skills
21. /docs/en/api/skills/list-skill-versions
22. /docs/en/api/skills/create-skill
23. /docs/en/api/files-content
24. /docs/en/api/admin-api/workspaces/get-workspace
25. /docs/en/api/admin-api/workspace_members/get-workspace-member
26. /docs/en/api/admin-api/workspaces/list-workspaces
27. /docs/en/api/rate-limits
28. /docs/en/api/admin
29. /docs/en/api/admin-api/users/get-user
30. /docs/en/api/admin-api/invites/get-invite
31. /docs/en/api/admin-api/apikeys/get-api-key
32. /docs/en/api/admin-api/organization/get-me
33. /docs/en/api/admin-api/usage-cost/get-messages-usage-report
34. /docs/en/api/admin-api/usage-cost/get-cost-report
35. /docs/en/api/admin-api/apikeys/list-api-keys
36. /docs/en/api/service-tiers
37. /docs/en/api/admin-api/claude-code/get-claude-code-usage-report

### agent-sdk section
38. /docs/en/agent-sdk/sessions

### about-claude section (already in Section A sitemap)
- /docs/en/about-claude/models/whats-new-claude-4-6 (in Section A)
- /docs/en/about-claude/models/migration-guide (in Section A)
- /docs/en/about-claude/pricing (in Section A)

## Cross-Reference Map

Below shows which pages link to which other pages within Section B (35 verified pages only):

```
/docs/en/build-with-claude/overview
  -> /docs/en/build-with-claude/working-with-messages
  -> /docs/en/build-with-claude/extended-thinking
  -> /docs/en/build-with-claude/adaptive-thinking
  -> /docs/en/build-with-claude/effort
  -> /docs/en/build-with-claude/fast-mode
  -> /docs/en/build-with-claude/structured-outputs
  -> /docs/en/build-with-claude/citations
  -> /docs/en/build-with-claude/streaming
  -> /docs/en/build-with-claude/batch-processing
  -> /docs/en/build-with-claude/vision
  -> /docs/en/build-with-claude/pdf-support
  -> /docs/en/build-with-claude/search-results
  -> /docs/en/build-with-claude/multilingual-support
  -> /docs/en/build-with-claude/embeddings
  -> /docs/en/build-with-claude/prompt-caching
  -> /docs/en/build-with-claude/context-windows
  -> /docs/en/build-with-claude/compaction
  -> /docs/en/build-with-claude/context-editing
  -> /docs/en/build-with-claude/files
  -> /docs/en/build-with-claude/token-counting
  -> /docs/en/build-with-claude/data-residency
  -> /docs/en/build-with-claude/prompt-engineering/overview
  -> /docs/en/build-with-claude/claude-on-amazon-bedrock
  -> /docs/en/build-with-claude/claude-on-vertex-ai
  -> /docs/en/build-with-claude/claude-in-microsoft-foundry
  -> /docs/en/build-with-claude/skills-guide
  -> /docs/en/build-with-claude/workspaces
  -> /docs/en/build-with-claude/handling-stop-reasons

/docs/en/build-with-claude/extended-thinking
  -> /docs/en/build-with-claude/adaptive-thinking
  -> /docs/en/build-with-claude/effort
  -> /docs/en/build-with-claude/streaming
  -> /docs/en/build-with-claude/prompt-caching
  -> /docs/en/build-with-claude/context-windows

/docs/en/build-with-claude/adaptive-thinking
  -> /docs/en/build-with-claude/extended-thinking
  -> /docs/en/build-with-claude/effort

/docs/en/build-with-claude/effort
  -> /docs/en/build-with-claude/extended-thinking
  -> /docs/en/build-with-claude/adaptive-thinking

/docs/en/build-with-claude/fast-mode
  -> /docs/en/build-with-claude/effort
  -> /docs/en/build-with-claude/streaming

/docs/en/build-with-claude/structured-outputs
  -> /docs/en/build-with-claude/streaming

/docs/en/build-with-claude/citations
  -> /docs/en/build-with-claude/pdf-support
  -> /docs/en/build-with-claude/search-results

/docs/en/build-with-claude/batch-processing
  -> /docs/en/build-with-claude/prompt-caching

/docs/en/build-with-claude/pdf-support
  -> /docs/en/build-with-claude/vision
  -> /docs/en/build-with-claude/files
  -> /docs/en/build-with-claude/citations

/docs/en/build-with-claude/search-results
  -> /docs/en/build-with-claude/citations

/docs/en/build-with-claude/prompt-caching
  -> /docs/en/build-with-claude/batch-processing
  -> /docs/en/build-with-claude/context-windows

/docs/en/build-with-claude/context-windows
  -> /docs/en/build-with-claude/extended-thinking
  -> /docs/en/build-with-claude/compaction
  -> /docs/en/build-with-claude/context-editing
  -> /docs/en/build-with-claude/prompt-caching
  -> /docs/en/build-with-claude/token-counting

/docs/en/build-with-claude/compaction
  -> /docs/en/build-with-claude/context-windows
  -> /docs/en/build-with-claude/context-editing
  -> /docs/en/build-with-claude/token-counting

/docs/en/build-with-claude/context-editing
  -> /docs/en/build-with-claude/compaction
  -> /docs/en/build-with-claude/context-windows

/docs/en/build-with-claude/files
  -> /docs/en/build-with-claude/pdf-support
  -> /docs/en/build-with-claude/vision
  -> /docs/en/build-with-claude/batch-processing

/docs/en/build-with-claude/token-counting
  -> /docs/en/build-with-claude/context-windows
  -> /docs/en/build-with-claude/vision
  -> /docs/en/build-with-claude/pdf-support

/docs/en/build-with-claude/data-residency
  -> /docs/en/build-with-claude/usage-cost-api

/docs/en/build-with-claude/claude-on-amazon-bedrock
  -> /docs/en/build-with-claude/claude-on-vertex-ai
  -> /docs/en/build-with-claude/claude-in-microsoft-foundry

/docs/en/build-with-claude/claude-on-vertex-ai
  -> /docs/en/build-with-claude/claude-on-amazon-bedrock
  -> /docs/en/build-with-claude/claude-in-microsoft-foundry

/docs/en/build-with-claude/claude-in-microsoft-foundry
  -> /docs/en/build-with-claude/overview
  -> /docs/en/build-with-claude/zero-data-retention

/docs/en/build-with-claude/workspaces
  -> /docs/en/build-with-claude/administration-api
  -> /docs/en/build-with-claude/files
  -> /docs/en/build-with-claude/batch-processing
  -> /docs/en/build-with-claude/skills-guide
  -> /docs/en/build-with-claude/prompt-caching
  -> /docs/en/build-with-claude/usage-cost-api

/docs/en/build-with-claude/zero-data-retention
  -> /docs/en/build-with-claude/prompt-caching
  -> /docs/en/build-with-claude/batch-processing
  -> /docs/en/build-with-claude/fast-mode

/docs/en/build-with-claude/administration-api
  -> /docs/en/build-with-claude/workspaces
  -> /docs/en/build-with-claude/usage-cost-api
  -> /docs/en/build-with-claude/claude-code-analytics-api

/docs/en/build-with-claude/usage-cost-api
  -> /docs/en/build-with-claude/administration-api
  -> /docs/en/build-with-claude/prompt-caching
  -> /docs/en/build-with-claude/batch-processing
  -> /docs/en/build-with-claude/data-residency
  -> /docs/en/build-with-claude/fast-mode
  -> /docs/en/build-with-claude/claude-code-analytics-api

/docs/en/build-with-claude/claude-code-analytics-api
  -> /docs/en/build-with-claude/administration-api
  -> /docs/en/build-with-claude/usage-cost-api

/docs/en/build-with-claude/prompt-engineering/overview
  -> /docs/en/build-with-claude/prompt-engineering/claude-prompting-best-practices
  -> /docs/en/build-with-claude/prompt-engineering/prompting-tools

/docs/en/build-with-claude/prompt-engineering/claude-prompting-best-practices
  -> /docs/en/build-with-claude/prompt-engineering/overview
  -> /docs/en/build-with-claude/extended-thinking
  -> /docs/en/build-with-claude/structured-outputs

/docs/en/build-with-claude/prompt-engineering/prompting-tools
  -> /docs/en/build-with-claude/prompt-engineering/overview
```

## Key Findings

1. **All 35 pages verified successfully** -- every page exists, loads correctly, and contains substantive content.

2. **38 unique cross-referenced pages discovered** -- these span across `agents-and-tools`, `api` (including admin-api sub-paths), and `agent-sdk` sections. The majority are API reference endpoints that likely exist in the sitemap under the API section.

3. **Content type distribution:**
   - feature-doc: 19 pages (54%) -- the dominant type, covering individual Claude capabilities
   - guide: 9 pages (26%) -- practical implementation guides including platform integrations
   - reference: 4 pages (11%) -- stop reasons, streaming, ZDR, usage/cost API
   - overview: 2 pages (6%) -- section entry points
   - use-case: 0 pages -- use cases are in Section A

4. **Key architectural patterns observed:**
   - The overview page (Page 1) serves as a comprehensive hub linking to nearly all other pages in Section B
   - Platform integration pages (Bedrock, Vertex AI, Foundry) cross-link to each other
   - Context management pages (context-windows, compaction, context-editing) form a tight cluster
   - Admin pages (administration-api, usage-cost-api, claude-code-analytics-api, workspaces) form another cluster
   - Thinking/effort pages (extended-thinking, adaptive-thinking, effort) are tightly interconnected

5. **Potential missing sitemap pages to check:**
   - `/docs/en/agents-and-tools/agent-skills/quickstart` (agent skills quickstart, referenced from skills-guide)
   - `/docs/en/agents-and-tools/agent-skills/best-practices` (agent skills best practices)
   - `/docs/en/agent-sdk/sessions` (Agent SDK sessions, referenced from ZDR page)
   - `/docs/en/api/skills/*` (Skills API endpoints -- list-skills, create-skill, list-skill-versions)
   - `/docs/en/api/files-content` (Files content API endpoint)
   - Multiple `/docs/en/api/admin-api/*` sub-paths (workspaces, members, users, invites, apikeys, usage-cost, claude-code)

6. **Model references are current** -- all pages reference Claude Opus 4.6, Sonnet 4.6, and Haiku 4.5 as the latest models.

7. **Notable new features documented:**
   - Agent Skills API (skills-guide) -- a relatively new addition for extending Claude with pre-built and custom skills
   - Claude Code Analytics API -- provides developer productivity metrics (sessions, LOC, commits, PRs, tool acceptance rates)
   - Microsoft Foundry integration -- newest platform integration with Azure-native authentication
   - Fast mode -- research preview with 2.5x faster output at 6x premium pricing
   - Adaptive thinking -- dynamic thinking depth (Opus 4.6/Sonnet 4.6 only)
