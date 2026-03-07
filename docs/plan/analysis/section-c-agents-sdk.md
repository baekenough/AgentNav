# Section C: Agents & Tools + Agent SDK — Verification Report

## Summary
- Total pages checked: 45
- Verified: 45 ✅
- Failed: 0 ❌
- New pages discovered: 68+

## Page Catalog

| # | Path | Status | Title | Type | Description |
|---|------|--------|-------|------|-------------|
| 1 | /docs/en/agents-and-tools/tool-use/overview | ✅ | Tool use with Claude | conceptual/guide | Claude의 도구/함수 호출 방식 개요. 가격, 벤치마크, 모델별 도구 지원 사양을 포함 |
| 2 | /docs/en/agents-and-tools/tool-use/implement-tool-use | ✅ | How to implement tool use | guide | 도구 사용 구현 종합 가이드. 모델 선택, 도구 정의, 병렬 실행, tool runner 베타 포함 |
| 3 | /docs/en/agents-and-tools/tool-use/web-search-tool | ✅ | Web search tool | reference/guide | 동적 필터링 기반 웹 검색 도구 (web_search_20260209). 도메인 필터링, 로컬라이제이션, 인용, 가격($10/1000건) |
| 4 | /docs/en/agents-and-tools/tool-use/web-fetch-tool | ✅ | Web fetch tool | reference/guide | 웹 페이지/PDF 전체 콘텐츠 검색 도구 (web_fetch_20260209). URL 유효성 검사, 인용, 추가 비용 없음 |
| 5 | /docs/en/agents-and-tools/tool-use/code-execution-tool | ✅ | Code execution tool | reference/guide | 샌드박스 코드 실행 도구 (code_execution_20250825). 웹 검색/fetch와 무료 번들, 파일 업/다운로드, 사전설치 패키지 |
| 6 | /docs/en/agents-and-tools/tool-use/bash-tool | ✅ | Bash tool | reference/guide | 영속 Bash 세션 도구 (bash_20250124). 셸 명령 실행, 245 입력 토큰 비용 |
| 7 | /docs/en/agents-and-tools/tool-use/computer-use-tool | ✅ | Computer use tool | reference/guide (beta) | 데스크톱 상호작용 도구 (computer_20251124). 스크린샷/마우스/키보드, 베타 헤더 필요 |
| 8 | /docs/en/agents-and-tools/tool-use/text-editor-tool | ✅ | Text editor tool | reference/guide | 파일 보기/편집 도구 (text_editor_20250728 for Claude 4, text_editor_20250124 for 3.7). view, str_replace, create, insert, undo_edit 명령 |
| 9 | /docs/en/agents-and-tools/tool-use/memory-tool | ✅ | Memory tool | reference/guide | 클라이언트 측 영속 메모리 도구 (memory_20250818). /memories 디렉토리 CRUD, 컨텍스트 편집 통합, 컴팩션 지원 |
| 10 | /docs/en/agents-and-tools/tool-use/tool-search-tool | ✅ | Tool search tool | reference/guide | 대규모 도구 세트를 위한 동적 도구 탐색. 컨텍스트 부풀림 85%+ 감소, 커스텀 구현 옵션 |
| 11 | /docs/en/agents-and-tools/tool-use/programmatic-tool-calling | ✅ | Programmatic tool calling | reference/guide | 실행 컨테이너 내 코드 기반 도구 호출 (code_execution_20260120). 지연시간 및 토큰 소비 감소 |
| 12 | /docs/en/agents-and-tools/tool-use/fine-grained-tool-streaming | ✅ | Fine-grained tool streaming | reference/guide | GA 기능. eager_input_streaming으로 더 빠른 도구 파라미터 스트리밍. 베타 헤더 불필요 |
| 13 | /docs/en/agents-and-tools/mcp-connector | ✅ | MCP connector | reference/guide (beta) | 직접 API MCP 통합 (beta: mcp-client-2025-11-20). 도구 호출, OAuth, 다중 서버, 마이그레이션 가이드 |
| 14 | /docs/en/agents-and-tools/remote-mcp-servers | ✅ | Remote MCP servers | reference | 서드파티 원격 MCP 서버 목록 및 연결 안내 |
| 15 | /docs/en/agents-and-tools/agent-skills/overview | ✅ | Agent Skills | conceptual/overview | 모듈식 기능 확장 (사전구축: pptx, xlsx, docx, pdf + 커스텀). 3단계 점진적 로딩, 파일시스템 기반 |
| 16 | /docs/en/agents-and-tools/agent-skills/quickstart | ✅ | Get started with Agent Skills in the API | tutorial | 사전구축 Skills(pptx, xlsx, docx, pdf) 단계별 사용 가이드. 베타 헤더 필요, 파일 다운로드 |
| 17 | /docs/en/agents-and-tools/agent-skills/best-practices | ✅ | Skill authoring best practices | guide | 간결한 작성, 점진적 공개 패턴, 워크플로우/피드백 루프, 평가 기반 개발, 안티패턴 |
| 18 | /docs/en/agents-and-tools/agent-skills/enterprise | ✅ | Skills for enterprise | guide | 거버넌스, 보안 검토 체크리스트, 리스크 티어, 라이프사이클 관리, 평가 요구사항, 버저닝 |
| 19 | /docs/en/agent-sdk/overview | ✅ | Agent SDK overview | conceptual/overview | Claude Code SDK에서 Claude Agent SDK로 명칭 변경. Python + TypeScript, 내장 도구, hooks, subagents, MCP, permissions, sessions, Skills |
| 20 | /docs/en/agent-sdk/quickstart | ✅ | Quickstart | tutorial | 버그 수정 에이전트 워크스루. 설정, query() API, 권한 모드, 도구 구성 |
| 21 | /docs/en/agent-sdk/typescript | ✅ | Agent SDK reference - TypeScript | reference | 전체 API: query(), tool(), Options, SDKMessage 타입, AgentDefinition |
| 22 | /docs/en/agent-sdk/typescript-v2-preview | ✅ | TypeScript SDK V2 interface (preview) | reference (unstable) | 간소화된 send()/stream() 패턴, createSession/resumeSession, unstable_v2_prompt |
| 23 | /docs/en/agent-sdk/python | ✅ | Agent SDK reference - Python | reference | 전체 API: query(), ClaudeSDKClient, ClaudeAgentOptions, 메시지 타입 |
| 24 | /docs/en/agent-sdk/agent-loop | ✅ | How the agent loop works | conceptual/guide | 메시지 라이프사이클, 턴, 도구 실행, 컨텍스트 윈도우, 자동 컴팩션, effort 레벨, 권한 모드 |
| 25 | /docs/en/agent-sdk/custom-tools | ✅ | Custom Tools | guide | 인프로세스 MCP 서버 via createSdkMcpServer/tool 헬퍼. Zod/Python 타입 안전성 |
| 26 | /docs/en/agent-sdk/mcp | ✅ | Connect to external tools with MCP | guide | stdio/HTTP/SSE 트랜스포트, 도구 검색, 인증, .mcp.json 설정, 예제 |
| 27 | /docs/en/agent-sdk/subagents | ✅ | Subagents in the SDK | guide | 프로그래밍/파일시스템 에이전트 정의, 컨텍스트 격리, 병렬 실행, 도구 제한, resume 기능 |
| 28 | /docs/en/agent-sdk/structured-outputs | ✅ | Get structured output from agents | guide | JSON Schema, Zod, Pydantic 지원. outputFormat 옵션, 오류 처리 |
| 29 | /docs/en/agent-sdk/streaming-output | ✅ | Stream responses in real-time | guide | 실시간 출력 스트리밍. include_partial_messages/includePartialMessages로 StreamEvent 수신, 텍스트/도구 호출 스트리밍, UI 구축 패턴 |
| 30 | /docs/en/agent-sdk/streaming-vs-single-mode | ✅ | Streaming Input | guide | 두 가지 입력 모드: 스트리밍(권장, 인터랙티브 세션) vs 단일 메시지(원샷 쿼리). 이미지 업로드, 큐잉, 인터럽트 지원 |
| 31 | /docs/en/agent-sdk/user-input | ✅ | Handle approvals and user input | guide | Claude의 승인 요청/명확화 질문 처리. canUseTool 콜백, AskUserQuestion 도구, 승인/거부/수정/대안 제안 패턴 |
| 32 | /docs/en/agent-sdk/permissions | ✅ | Configure permissions | guide | 권한 모드(default, dontAsk, acceptEdits, bypassPermissions, plan)와 allow/deny 규칙. 평가 흐름: hooks → deny → mode → allow → canUseTool |
| 33 | /docs/en/agent-sdk/hooks | ✅ | Intercept and control agent behavior with hooks | guide | 에이전트 실행 핵심 지점에서 콜백 실행. PreToolUse, PostToolUse, SubagentStart/Stop, Notification 등 18+ 이벤트. 매처, 입력/출력, 체이닝, 비동기 지원 |
| 34 | /docs/en/agent-sdk/modifying-system-prompts | ✅ | Modifying system prompts | guide | 시스템 프롬프트 커스터마이징 4가지 방법: CLAUDE.md, output styles, systemPrompt append, 커스텀 systemPrompt. 비교표 포함 |
| 35 | /docs/en/agent-sdk/sessions | ✅ | Work with sessions | guide | 세션 영속성, continue/resume/fork 패턴. ClaudeSDKClient(Python), continue:true(TypeScript), 세션 ID 캡처, 호스트 간 resume |
| 36 | /docs/en/agent-sdk/skills | ✅ | Agent Skills in the SDK | guide | SDK에서 Skills 사용. SKILL.md 파일 기반, settingSources 설정 필수, Skill 도구 활성화, 트러블슈팅 |
| 37 | /docs/en/agent-sdk/slash-commands | ✅ | Slash Commands in the SDK | guide | /compact, /clear, /help 등 빌트인 명령. 커스텀 슬래시 명령 생성(마크다운 파일), 인수/플레이스홀더, bash 실행, 파일 참조, 네임스페이싱 |
| 38 | /docs/en/agent-sdk/plugins | ✅ | Plugins in the SDK | guide | 로컬 디렉토리에서 플러그인 로드. 커맨드/에이전트/스킬/훅/MCP 서버 확장. 네임스페이스 명령, plugin.json 매니페스트 |
| 39 | /docs/en/agent-sdk/claude-code-features | ✅ | Use Claude Code features in the SDK | guide | settingSources로 CLAUDE.md, rules, skills, hooks 로드. 기능별 비교표(CLAUDE.md vs Skills vs Subagents vs Hooks vs MCP) |
| 40 | /docs/en/agent-sdk/todo-tracking | ✅ | Todo Lists | guide | SDK 내장 할일 추적. TodoWrite 도구로 진행률 표시, 복잡한 멀티스텝 작업 자동 생성, 실시간 진행률 UI 구축 |
| 41 | /docs/en/agent-sdk/file-checkpointing | ✅ | Rewind file changes with checkpointing | guide | Write/Edit/NotebookEdit 도구의 파일 변경 추적 및 되감기. 체크포인트 UUID 캡처, rewindFiles()/rewind_files() 호출, 다중 복원 지점 |
| 42 | /docs/en/agent-sdk/cost-tracking | ✅ | Track cost and usage | guide | 토큰 사용량 추적, 병렬 도구 호출 중복 제거, 비용 계산. total_cost_usd, 모델별 분석(TS만), 캐시 토큰 추적 |
| 43 | /docs/en/agent-sdk/hosting | ✅ | Hosting the Agent SDK | guide | 프로덕션 배포 아키텍처. 컨테이너 샌드박싱, 4가지 패턴(임시/장기/하이브리드/단일), 샌드박스 제공자 목록(Modal, Cloudflare, E2B 등) |
| 44 | /docs/en/agent-sdk/secure-deployment | ✅ | Securely deploying AI agents | guide | 보안 배포 가이드. 격리 기술(샌드박스/Docker/gVisor/VM), 프록시 패턴, 자격증명 관리, 파일시스템 구성, 네트워크 제어 |
| 45 | /docs/en/agent-sdk/migration-guide | ✅ | Migrate to Claude Agent SDK | guide | Claude Code SDK → Claude Agent SDK 마이그레이션. 패키지명 변경(TS: @anthropic-ai/claude-agent-sdk, Python: claude-agent-sdk), ClaudeCodeOptions→ClaudeAgentOptions, 시스템 프롬프트 기본값 변경, settingSources 미로드 기본값 |

## Discovered Pages (not in sitemap)

Below are internal `/docs/en/...` links discovered during page fetching that may not be in the master sitemap list. These represent pages that should be verified for inclusion.

### From Page 1: /docs/en/agents-and-tools/tool-use/overview
| Discovered Link | Notes |
|----------------|-------|
| /docs/en/build-with-claude/structured-outputs | Structured outputs |
| /docs/en/build-with-claude/prompt-caching | Prompt caching |
| /docs/en/about-claude/model-deprecations | Model deprecations |
| /docs/en/agents-and-tools/tool-use/implement-tool-use | Implement tool use (in sitemap) |

### From Page 2: /docs/en/agents-and-tools/tool-use/implement-tool-use
| Discovered Link | Notes |
|----------------|-------|
| /docs/en/build-with-claude/extended-thinking | Extended thinking |
| /docs/en/agents-and-tools/tool-use/tool-search-tool | Tool search tool (in sitemap) |
| /docs/en/build-with-claude/structured-outputs | Structured outputs |
| /docs/en/build-with-claude/prompt-caching | Prompt caching |
| /docs/en/about-claude/models/migration-guide | Migration guide |
| /docs/en/build-with-claude/context-editing | Context editing |

### From Page 3: /docs/en/agents-and-tools/tool-use/web-search-tool
| Discovered Link | Notes |
|----------------|-------|
| /docs/en/build-with-claude/zero-data-retention | Zero data retention |
| /docs/en/agents-and-tools/tool-use/code-execution-tool | Code execution tool (in sitemap) |
| /docs/en/build-with-claude/prompt-caching | Prompt caching |
| /docs/en/build-with-claude/batch-processing | Batch processing |
| /docs/en/about-claude/model-deprecations | Model deprecations |

### From Page 4: /docs/en/agents-and-tools/tool-use/web-fetch-tool
| Discovered Link | Notes |
|----------------|-------|
| /docs/en/build-with-claude/zero-data-retention | Zero data retention |
| /docs/en/agents-and-tools/tool-use/web-search-tool | Web search tool (in sitemap) |
| /docs/en/build-with-claude/prompt-caching | Prompt caching |
| /docs/en/build-with-claude/batch-processing | Batch processing |

### From Page 5: /docs/en/agents-and-tools/tool-use/code-execution-tool
| Discovered Link | Notes |
|----------------|-------|
| /docs/en/build-with-claude/zero-data-retention | Zero data retention |
| /docs/en/about-claude/model-deprecations | Model deprecations |
| /docs/en/api/files-api | Files API |

### From Page 6: /docs/en/agents-and-tools/tool-use/bash-tool
| Discovered Link | Notes |
|----------------|-------|
| /docs/en/agents-and-tools/tool-use/overview | Overview (in sitemap) |
| /docs/en/agents-and-tools/tool-use/text-editor-tool | Text editor tool (in sitemap) |
| /docs/en/agents-and-tools/tool-use/code-execution-tool | Code execution tool (in sitemap) |

### From Page 7: /docs/en/agents-and-tools/tool-use/computer-use-tool
| Discovered Link | Notes |
|----------------|-------|
| /docs/en/build-with-claude/zero-data-retention | Zero data retention |
| /docs/en/about-claude/model-deprecations | Model deprecations |
| /docs/en/api/beta-headers | Beta headers |

### From Page 8: /docs/en/agents-and-tools/tool-use/text-editor-tool
| Discovered Link | Notes |
|----------------|-------|
| /docs/en/agents-and-tools/tool-use/overview | Overview (in sitemap) |
| /docs/en/agents-and-tools/tool-use/bash-tool | Bash tool (in sitemap) |

### From Page 9: /docs/en/agents-and-tools/tool-use/memory-tool
| Discovered Link | Notes |
|----------------|-------|
| /docs/en/build-with-claude/zero-data-retention | Zero data retention |
| /docs/en/agents-and-tools/tool-use/text-editor-tool | Text editor tool (in sitemap) |
| /docs/en/build-with-claude/context-editing | Context editing |
| /docs/en/build-with-claude/compaction | Compaction |

### From Page 10: /docs/en/agents-and-tools/tool-use/tool-search-tool
| Discovered Link | Notes |
|----------------|-------|
| /docs/en/build-with-claude/zero-data-retention | Zero data retention |

### From Page 11: /docs/en/agents-and-tools/tool-use/programmatic-tool-calling
| Discovered Link | Notes |
|----------------|-------|
| /docs/en/agents-and-tools/tool-use/code-execution-tool | Code execution tool (in sitemap) |
| /docs/en/build-with-claude/zero-data-retention | Zero data retention |

### From Page 12: /docs/en/agents-and-tools/tool-use/fine-grained-tool-streaming
| Discovered Link | Notes |
|----------------|-------|
| /docs/en/build-with-claude/streaming | Streaming |
| /docs/en/build-with-claude/handling-stop-reasons | Handling stop reasons |

### From Page 13: /docs/en/agents-and-tools/mcp-connector
| Discovered Link | Notes |
|----------------|-------|
| /docs/en/build-with-claude/zero-data-retention | Zero data retention |
| /docs/en/agents-and-tools/tool-use/tool-search-tool | Tool search tool (in sitemap) |
| /docs/en/agents-and-tools/tool-use/implement-tool-use | Implement tool use (in sitemap) |
| /docs/en/agent-sdk/mcp | Agent SDK MCP (in sitemap) |

### From Page 14: /docs/en/agents-and-tools/remote-mcp-servers
| Discovered Link | Notes |
|----------------|-------|
| /docs/en/agents-and-tools/mcp-connector | MCP connector (in sitemap) |

### From Page 15: /docs/en/agents-and-tools/agent-skills/overview
| Discovered Link | Notes |
|----------------|-------|
| /docs/en/agents-and-tools/agent-skills/quickstart | Quickstart (in sitemap) |
| /docs/en/agents-and-tools/agent-skills/best-practices | Best practices (in sitemap) |
| /docs/en/agent-sdk/skills | Agent SDK skills (in sitemap) |
| /docs/en/agents-and-tools/tool-use/code-execution-tool | Code execution tool (in sitemap) |

### From Page 16: /docs/en/agents-and-tools/agent-skills/quickstart
| Discovered Link | Notes |
|----------------|-------|
| /docs/en/agents-and-tools/agent-skills/best-practices | Best practices (in sitemap) |
| /docs/en/agents-and-tools/tool-use/code-execution-tool | Code execution tool (in sitemap) |
| /docs/en/agent-sdk/skills | Agent SDK skills (in sitemap) |

### From Page 17: /docs/en/agents-and-tools/agent-skills/best-practices
| Discovered Link | Notes |
|----------------|-------|
| /docs/en/agents-and-tools/agent-skills/overview | Overview (in sitemap) |
| /docs/en/agents-and-tools/agent-skills/quickstart | Quickstart (in sitemap) |
| /docs/en/agent-sdk/skills | Agent SDK skills (in sitemap) |

### From Page 18: /docs/en/agents-and-tools/agent-skills/enterprise
| Discovered Link | Notes |
|----------------|-------|
| /docs/en/agents-and-tools/agent-skills/overview | Overview (in sitemap) |
| /docs/en/agents-and-tools/agent-skills/best-practices | Best practices (in sitemap) |
| /docs/en/agent-sdk/secure-deployment | Secure deployment (in sitemap) |

### From Page 19: /docs/en/agent-sdk/overview
| Discovered Link | Notes |
|----------------|-------|
| /docs/en/agent-sdk/quickstart | Quickstart (in sitemap) |
| /docs/en/agent-sdk/typescript | TypeScript ref (in sitemap) |
| /docs/en/agent-sdk/python | Python ref (in sitemap) |
| /docs/en/agent-sdk/migration-guide | Migration guide (in sitemap) |
| /docs/en/agent-sdk/hooks | Hooks (in sitemap) |
| /docs/en/agent-sdk/subagents | Subagents (in sitemap) |
| /docs/en/agent-sdk/mcp | MCP (in sitemap) |
| /docs/en/agent-sdk/permissions | Permissions (in sitemap) |
| /docs/en/agent-sdk/sessions | Sessions (in sitemap) |
| /docs/en/agent-sdk/skills | Skills (in sitemap) |
| /docs/en/agent-sdk/slash-commands | Slash commands (in sitemap) |
| /docs/en/agent-sdk/plugins | Plugins (in sitemap) |
| /docs/en/agent-sdk/claude-code-features | Claude Code features (in sitemap) |
| /docs/en/agent-sdk/user-input | User input (in sitemap) |
| /docs/en/agent-sdk/streaming-output | Streaming output (in sitemap) |

### From Page 20: /docs/en/agent-sdk/quickstart
| Discovered Link | Notes |
|----------------|-------|
| /docs/en/agent-sdk/python | Python ref (in sitemap) |
| /docs/en/agent-sdk/typescript | TypeScript ref (in sitemap) |
| /docs/en/agent-sdk/permissions | Permissions (in sitemap) |
| /docs/en/agent-sdk/hooks | Hooks (in sitemap) |
| /docs/en/agent-sdk/sessions | Sessions (in sitemap) |
| /docs/en/agent-sdk/mcp | MCP (in sitemap) |
| /docs/en/agent-sdk/hosting | Hosting (in sitemap) |
| /docs/en/agent-sdk/streaming-vs-single-mode | Streaming vs single mode (in sitemap) |

### From Page 21: /docs/en/agent-sdk/typescript
| Discovered Link | Notes |
|----------------|-------|
| /docs/en/agent-sdk/typescript-v2-preview | V2 preview (in sitemap) |
| /docs/en/agent-sdk/python | Python ref (in sitemap) |
| /docs/en/agent-sdk/overview | Overview (in sitemap) |
| /docs/en/agent-sdk/hooks | Hooks (in sitemap) |
| /docs/en/agent-sdk/permissions | Permissions (in sitemap) |
| /docs/en/agent-sdk/subagents | Subagents (in sitemap) |
| /docs/en/agent-sdk/mcp | MCP (in sitemap) |

### From Page 22: /docs/en/agent-sdk/typescript-v2-preview
| Discovered Link | Notes |
|----------------|-------|
| /docs/en/agent-sdk/typescript | TypeScript ref (in sitemap) |
| /docs/en/agent-sdk/overview | Overview (in sitemap) |

### From Page 23: /docs/en/agent-sdk/python
| Discovered Link | Notes |
|----------------|-------|
| /docs/en/agent-sdk/typescript | TypeScript ref (in sitemap) |
| /docs/en/agent-sdk/overview | Overview (in sitemap) |
| /docs/en/agent-sdk/hooks | Hooks (in sitemap) |
| /docs/en/agent-sdk/permissions | Permissions (in sitemap) |

### From Page 24: /docs/en/agent-sdk/agent-loop
| Discovered Link | Notes |
|----------------|-------|
| /docs/en/agent-sdk/hooks | Hooks (in sitemap) |
| /docs/en/agent-sdk/streaming-output | Streaming output (in sitemap) |
| /docs/en/agent-sdk/permissions | Permissions (in sitemap) |
| /docs/en/agent-sdk/subagents | Subagents (in sitemap) |
| /docs/en/agent-sdk/sessions | Sessions (in sitemap) |
| /docs/en/agent-sdk/mcp | MCP (in sitemap) |
| /docs/en/agent-sdk/claude-code-features | Claude Code features (in sitemap) |
| /docs/en/agent-sdk/quickstart | Quickstart (in sitemap) |
| /docs/en/agent-sdk/python | Python ref (in sitemap) |
| /docs/en/agent-sdk/typescript | TypeScript ref (in sitemap) |
| /docs/en/agent-sdk/cost-tracking | Cost tracking (in sitemap) |

### From Page 25: /docs/en/agent-sdk/custom-tools
| Discovered Link | Notes |
|----------------|-------|
| /docs/en/agent-sdk/typescript | TypeScript ref (in sitemap) |
| /docs/en/agent-sdk/python | Python ref (in sitemap) |
| /docs/en/agent-sdk/overview | Overview (in sitemap) |

### From Page 26: /docs/en/agent-sdk/mcp
| Discovered Link | Notes |
|----------------|-------|
| /docs/en/agent-sdk/custom-tools | Custom tools (in sitemap) |
| /docs/en/agent-sdk/permissions | Permissions (in sitemap) |
| /docs/en/agent-sdk/typescript | TypeScript ref (in sitemap) |
| /docs/en/agent-sdk/python | Python ref (in sitemap) |

### From Page 27: /docs/en/agent-sdk/subagents
| Discovered Link | Notes |
|----------------|-------|
| /docs/en/agent-sdk/typescript | TypeScript ref (in sitemap) |
| /docs/en/agent-sdk/python | Python ref (in sitemap) |
| /docs/en/agent-sdk/overview | Overview (in sitemap) |
| /docs/en/agent-sdk/permissions | Permissions (in sitemap) |

### From Page 28: /docs/en/agent-sdk/structured-outputs
| Discovered Link | Notes |
|----------------|-------|
| /docs/en/build-with-claude/structured-outputs | Structured outputs (API level) |
| /docs/en/agent-sdk/custom-tools | Custom tools (in sitemap) |

### From Page 29: /docs/en/agent-sdk/streaming-output
| Discovered Link | Notes |
|----------------|-------|
| /docs/en/agent-sdk/streaming-vs-single-mode | Streaming vs single mode (in sitemap) |
| /docs/en/agent-sdk/structured-outputs | Structured outputs (in sitemap) |
| /docs/en/agent-sdk/permissions | Permissions (in sitemap) |
| /docs/en/build-with-claude/streaming | Streaming (API level) |

### From Page 30: /docs/en/agent-sdk/streaming-vs-single-mode
| Discovered Link | Notes |
|----------------|-------|
| (No new external links discovered — self-contained page) | |

### From Page 31: /docs/en/agent-sdk/user-input
| Discovered Link | Notes |
|----------------|-------|
| /docs/en/agent-sdk/permissions | Permissions (in sitemap) |
| /docs/en/agent-sdk/hooks | Hooks (in sitemap) |
| /docs/en/agent-sdk/streaming-vs-single-mode | Streaming vs single mode (in sitemap) |
| /docs/en/agent-sdk/custom-tools | Custom tools (in sitemap) |
| /docs/en/agent-sdk/typescript | TypeScript ref (in sitemap) |
| /docs/en/agent-sdk/python | Python ref (in sitemap) |

### From Page 32: /docs/en/agent-sdk/permissions
| Discovered Link | Notes |
|----------------|-------|
| /docs/en/agent-sdk/user-input | User input (in sitemap) |
| /docs/en/agent-sdk/hooks | Hooks (in sitemap) |
| /docs/en/agent-sdk/typescript | TypeScript ref (in sitemap) |
| /docs/en/agent-sdk/python | Python ref (in sitemap) |

### From Page 33: /docs/en/agent-sdk/hooks
| Discovered Link | Notes |
|----------------|-------|
| /docs/en/agent-sdk/typescript | TypeScript ref (in sitemap) |
| /docs/en/agent-sdk/python | Python ref (in sitemap) |
| /docs/en/agent-sdk/permissions | Permissions (in sitemap) |
| /docs/en/agent-sdk/custom-tools | Custom tools (in sitemap) |

### From Page 34: /docs/en/agent-sdk/modifying-system-prompts
| Discovered Link | Notes |
|----------------|-------|
| /docs/en/agent-sdk/typescript | TypeScript ref (in sitemap) |

### From Page 35: /docs/en/agent-sdk/sessions
| Discovered Link | Notes |
|----------------|-------|
| /docs/en/agent-sdk/file-checkpointing | File checkpointing (in sitemap) |
| /docs/en/agent-sdk/user-input | User input (in sitemap) |
| /docs/en/agent-sdk/agent-loop | Agent loop (in sitemap) |
| /docs/en/agent-sdk/python | Python ref (in sitemap) |
| /docs/en/agent-sdk/typescript | TypeScript ref (in sitemap) |
| /docs/en/agent-sdk/typescript-v2-preview | V2 preview (in sitemap) |

### From Page 36: /docs/en/agent-sdk/skills
| Discovered Link | Notes |
|----------------|-------|
| /docs/en/agents-and-tools/agent-skills/overview | Agent Skills overview (in sitemap) |
| /docs/en/agents-and-tools/agent-skills/best-practices | Best practices (in sitemap) |
| /docs/en/agent-sdk/subagents | Subagents (in sitemap) |
| /docs/en/agent-sdk/slash-commands | Slash commands (in sitemap) |
| /docs/en/agent-sdk/overview | Overview (in sitemap) |
| /docs/en/agent-sdk/typescript | TypeScript ref (in sitemap) |
| /docs/en/agent-sdk/python | Python ref (in sitemap) |

### From Page 37: /docs/en/agent-sdk/slash-commands
| Discovered Link | Notes |
|----------------|-------|
| /docs/en/agent-sdk/subagents | Subagents (in sitemap) |
| /docs/en/agent-sdk/typescript | TypeScript ref (in sitemap) |
| /docs/en/agent-sdk/overview | Overview (in sitemap) |

### From Page 38: /docs/en/agent-sdk/plugins
| Discovered Link | Notes |
|----------------|-------|
| /docs/en/agent-sdk/slash-commands | Slash commands (in sitemap) |
| /docs/en/agent-sdk/subagents | Subagents (in sitemap) |
| /docs/en/agent-sdk/skills | Skills (in sitemap) |

### From Page 39: /docs/en/agent-sdk/claude-code-features
| Discovered Link | Notes |
|----------------|-------|
| /docs/en/agent-sdk/python | Python ref (in sitemap) |
| /docs/en/agent-sdk/typescript | TypeScript ref (in sitemap) |
| /docs/en/agent-sdk/skills | Skills (in sitemap) |
| /docs/en/agent-sdk/subagents | Subagents (in sitemap) |
| /docs/en/agent-sdk/hooks | Hooks (in sitemap) |
| /docs/en/agent-sdk/permissions | Permissions (in sitemap) |
| /docs/en/agent-sdk/modifying-system-prompts | System prompts (in sitemap) |
| /docs/en/agent-sdk/mcp | MCP (in sitemap) |

### From Page 40: /docs/en/agent-sdk/todo-tracking
| Discovered Link | Notes |
|----------------|-------|
| /docs/en/agent-sdk/typescript | TypeScript ref (in sitemap) |
| /docs/en/agent-sdk/python | Python ref (in sitemap) |
| /docs/en/agent-sdk/streaming-vs-single-mode | Streaming vs single mode (in sitemap) |
| /docs/en/agent-sdk/custom-tools | Custom tools (in sitemap) |

### From Page 41: /docs/en/agent-sdk/file-checkpointing
| Discovered Link | Notes |
|----------------|-------|
| /docs/en/agent-sdk/sessions | Sessions (in sitemap) |
| /docs/en/agent-sdk/permissions | Permissions (in sitemap) |
| /docs/en/agent-sdk/typescript | TypeScript ref (in sitemap) |
| /docs/en/agent-sdk/python | Python ref (in sitemap) |

### From Page 42: /docs/en/agent-sdk/cost-tracking
| Discovered Link | Notes |
|----------------|-------|
| /docs/en/agent-sdk/typescript | TypeScript ref (in sitemap) |
| /docs/en/agent-sdk/python | Python ref (in sitemap) |
| /docs/en/agent-sdk/overview | Overview (in sitemap) |
| /docs/en/agent-sdk/permissions | Permissions (in sitemap) |
| /docs/en/build-with-claude/prompt-caching | Prompt caching |

### From Page 43: /docs/en/agent-sdk/hosting
| Discovered Link | Notes |
|----------------|-------|
| /docs/en/agent-sdk/secure-deployment | Secure deployment (in sitemap) |
| /docs/en/agent-sdk/typescript | TypeScript ref (in sitemap) |
| /docs/en/agent-sdk/sessions | Sessions (in sitemap) |
| /docs/en/agent-sdk/permissions | Permissions (in sitemap) |
| /docs/en/agent-sdk/cost-tracking | Cost tracking (in sitemap) |
| /docs/en/agent-sdk/mcp | MCP (in sitemap) |

### From Page 44: /docs/en/agent-sdk/secure-deployment
| Discovered Link | Notes |
|----------------|-------|
| /docs/en/agent-sdk/hosting | Hosting (in sitemap) |
| /docs/en/agent-sdk/permissions | Permissions (in sitemap) |

### From Page 45: /docs/en/agent-sdk/migration-guide
| Discovered Link | Notes |
|----------------|-------|
| /docs/en/agent-sdk/overview | Overview (in sitemap) |
| /docs/en/agent-sdk/typescript | TypeScript ref (in sitemap) |
| /docs/en/agent-sdk/python | Python ref (in sitemap) |
| /docs/en/agent-sdk/custom-tools | Custom tools (in sitemap) |
| /docs/en/agent-sdk/mcp | MCP (in sitemap) |

## Unique External Page References (not in Section C)

The following unique pages referenced by Section C pages are NOT part of this section and should be verified in other sections:

| Path | Referenced By |
|------|--------------|
| /docs/en/build-with-claude/structured-outputs | Pages 1, 2, 28 |
| /docs/en/build-with-claude/prompt-caching | Pages 1, 2, 3, 4, 42 |
| /docs/en/about-claude/model-deprecations | Pages 1, 3, 5, 7 |
| /docs/en/build-with-claude/extended-thinking | Page 2 |
| /docs/en/build-with-claude/context-editing | Pages 2, 9 |
| /docs/en/build-with-claude/zero-data-retention | Pages 3, 4, 5, 7, 9, 10, 11, 13 |
| /docs/en/build-with-claude/batch-processing | Pages 3, 4 |
| /docs/en/api/files-api | Page 5 |
| /docs/en/api/beta-headers | Page 7 |
| /docs/en/build-with-claude/compaction | Page 9 |
| /docs/en/build-with-claude/streaming | Pages 12, 29 |
| /docs/en/build-with-claude/handling-stop-reasons | Page 12 |

## Key Findings

### Tool Versions Documented
| Tool | Version ID | Status |
|------|-----------|--------|
| web_search | web_search_20260209 | GA |
| web_fetch | web_fetch_20260209 | GA |
| code_execution | code_execution_20250825 | GA |
| bash | bash_20250124 | GA |
| computer_use | computer_20251124 | Beta |
| text_editor | text_editor_20250728 (Claude 4) / text_editor_20250124 (Claude 3.7) | GA |
| memory | memory_20250818 | GA |
| tool_search | (dynamic) | GA |
| programmatic_tool_calling | code_execution_20260120 | GA |
| fine_grained_tool_streaming | eager_input_streaming | GA |
| mcp_connector | mcp-client-2025-11-20 | Beta |

### Agent SDK Key Info
- **Renamed from**: Claude Code SDK → Claude Agent SDK
- **TypeScript package**: `@anthropic-ai/claude-agent-sdk`
- **Python package**: `claude-agent-sdk`
- **Breaking changes in v0.1.0**: System prompt no longer default, settingSources not loaded by default, ClaudeCodeOptions→ClaudeAgentOptions

### Notes
- All 45 pages successfully fetched and verified
- docs.anthropic.com redirects to platform.claude.com (301 Moved Permanently)
- Most internal cross-references within Section C are valid (link to pages within the same section)
- External references primarily point to build-with-claude and about-claude sections
- No broken or missing pages detected within this section
