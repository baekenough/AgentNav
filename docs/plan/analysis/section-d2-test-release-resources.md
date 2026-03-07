# Section D-2: Test & Evaluate + Release Notes + Resources — Verification Report

## Summary
- Total pages checked: 11
- Verified: 11 ✅
- Failed: 0 ❌
- New pages discovered: 52 (unique /docs/en/* paths not in the 11 target pages)

---

## Page Catalog

| # | Path | Status | Title | Type | Description |
|---|------|--------|-------|------|-------------|
| 1 | /docs/en/test-and-evaluate/develop-tests | ✅ | Define success criteria and build evaluations | guide | 성공 기준 정의와 평가(eval) 설계 방법을 다루며, 측정 가능한 지표 설정, 테스트 케이스 작성, 그리고 반복적 프롬프트 개선 사이클을 설명한다. |
| 2 | /docs/en/test-and-evaluate/eval-tool | ✅ | Using the Evaluation Tool | tutorial | Claude Console의 Evaluation 도구 사용법을 단계별로 안내하며, 프롬프트 생성, 테스트 케이스 작성, CSV 임포트 등의 기능을 설명한다. |
| 3 | /docs/en/test-and-evaluate/strengthen-guardrails/reduce-hallucinations | ✅ | Reduce hallucinations | guide | LLM 환각(hallucination) 현상을 최소화하기 위한 기법들을 제시하며, 불확실성 인정 허용, 직접 인용 활용, 출처 기반 검증, 사고 연쇄 검증 등의 전략을 다룬다. |
| 4 | /docs/en/test-and-evaluate/strengthen-guardrails/increase-consistency | ✅ | Increase output consistency | guide | Claude 응답의 일관성을 높이기 위한 방법을 설명하며, 출력 포맷 지정, 구조화된 출력, 예시 제공, 검색 기반 컨텍스트 고정, 역할 유지 등의 기법을 다룬다. |
| 5 | /docs/en/test-and-evaluate/strengthen-guardrails/reduce-latency | ✅ | Reducing latency | guide | 모델 응답 지연(latency)을 줄이기 위한 전략을 다루며, 적합한 모델 선택, 프롬프트 최적화, 스트리밍 활용, 병렬 처리, 캐싱 등의 기법을 설명한다. |
| 6 | /docs/en/test-and-evaluate/strengthen-guardrails/reduce-prompt-leak | ✅ | Reduce prompt leak | guide | 시스템 프롬프트의 민감한 정보가 노출되는 프롬프트 누수(leak)를 방지하기 위한 전략을 설명하며, 컨텍스트 분리, 후처리 필터링, 정기 감사 등의 방법을 제시한다. |
| 7 | /docs/en/test-and-evaluate/strengthen-guardrails/handle-streaming-refusals | ✅ | Streaming refusals | reference | Claude 4 모델부터 도입된 스트리밍 거절(refusal) 처리를 설명하며, `stop_reason: "refusal"` API 응답 형식, 컨텍스트 리셋 방법, 언어별 구현 예시를 다룬다. |
| 8 | /docs/en/test-and-evaluate/strengthen-guardrails/mitigate-jailbreaks | ✅ | Mitigate jailbreaks and prompt injections | guide | 탈옥(jailbreak) 및 프롬프트 인젝션 공격을 완화하기 위한 다층 방어 전략을 설명하며, 무해성 스크린, 입력 검증, 프롬프트 엔지니어링, 지속적 모니터링, 체인 방어 패턴을 다룬다. |
| 9 | /docs/en/release-notes/overview | ✅ | Claude Developer Platform | reference | Claude API, 클라이언트 SDK, Claude Console의 업데이트 이력을 날짜순으로 정리한 공식 릴리스 노트로, 신규 모델 출시, 기능 추가, 모델 지원 종료 정보를 포함한다. |
| 10 | /docs/en/release-notes/system-prompts | ✅ | System Prompts | reference | claude.ai 웹 인터페이스와 모바일 앱에서 사용되는 공식 시스템 프롬프트의 버전별 전문을 제공하며, 제품 정보, 거절 처리, 톤/포맷, 사용자 복지 등의 섹션으로 구성된다. |
| 11 | /docs/en/resources/overview | ✅ | Resources (Overview) | overview | 모델 카드(System Card), 학습 리소스(Quickstarts, Courses, Cookbook), 그리고 LLM 인제스천용 문서(llms.txt, API primer) 등 Anthropic의 외부 참조 자료 허브를 제공한다. |

---

## Discovered Pages (not in sitemap, per page)

### Page 1: /docs/en/test-and-evaluate/develop-tests
내부 /docs/en/* 링크 없음

### Page 2: /docs/en/test-and-evaluate/eval-tool
- /docs/en/build-with-claude/prompt-engineering/prompting-tools

### Page 3: /docs/en/test-and-evaluate/strengthen-guardrails/reduce-hallucinations
내부 /docs/en/* 링크 없음

### Page 4: /docs/en/test-and-evaluate/strengthen-guardrails/increase-consistency
- /docs/en/build-with-claude/prompt-engineering/claude-prompting-best-practices
- /docs/en/build-with-claude/structured-outputs

### Page 5: /docs/en/test-and-evaluate/strengthen-guardrails/reduce-latency
- /docs/en/about-claude/glossary
- /docs/en/about-claude/models/overview
- /docs/en/api/messages
- /docs/en/build-with-claude/prompt-engineering/claude-prompting-best-practices
- /docs/en/build-with-claude/streaming

### Page 6: /docs/en/test-and-evaluate/strengthen-guardrails/reduce-prompt-leak
- /docs/en/build-with-claude/prompt-engineering/claude-prompting-best-practices

### Page 7: /docs/en/test-and-evaluate/strengthen-guardrails/handle-streaming-refusals
내부 /docs/en/* 링크 없음

### Page 8: /docs/en/test-and-evaluate/strengthen-guardrails/mitigate-jailbreaks
- /docs/en/build-with-claude/structured-outputs

### Page 9: /docs/en/release-notes/overview
- /docs/en/about-claude/model-deprecations
- /docs/en/about-claude/models
- /docs/en/about-claude/models/overview
- /docs/en/about-claude/models/whats-new-claude-4-6
- /docs/en/about-claude/pricing
- /docs/en/agents-and-tools/agent-skills/overview
- /docs/en/agents-and-tools/mcp-connector
- /docs/en/agents-and-tools/tool-use/code-execution-tool
- /docs/en/agents-and-tools/tool-use/computer-use-tool
- /docs/en/agents-and-tools/tool-use/fine-grained-tool-streaming
- /docs/en/agents-and-tools/tool-use/implement-tool-use
- /docs/en/agents-and-tools/tool-use/memory-tool
- /docs/en/agents-and-tools/tool-use/overview
- /docs/en/agents-and-tools/tool-use/programmatic-tool-calling
- /docs/en/agents-and-tools/tool-use/tool-search-tool
- /docs/en/agents-and-tools/tool-use/web-fetch-tool
- /docs/en/agents-and-tools/tool-use/web-search-tool
- /docs/en/api/admin-api/organization/get-me
- /docs/en/api/beta-headers
- /docs/en/api/deleting-message-batches
- /docs/en/api/errors
- /docs/en/api/models-list
- /docs/en/api/openai-sdk
- /docs/en/api/rate-limits
- /docs/en/api/skills/create-skill
- /docs/en/build-with-claude/adaptive-thinking
- /docs/en/build-with-claude/administration-api
- /docs/en/build-with-claude/batch-processing
- /docs/en/build-with-claude/citations
- /docs/en/build-with-claude/claude-code-analytics-api
- /docs/en/build-with-claude/claude-in-microsoft-foundry
- /docs/en/build-with-claude/claude-on-vertex-ai
- /docs/en/build-with-claude/compaction
- /docs/en/build-with-claude/context-editing
- /docs/en/build-with-claude/context-windows
- /docs/en/build-with-claude/data-residency
- /docs/en/build-with-claude/effort
- /docs/en/build-with-claude/extended-thinking
- /docs/en/build-with-claude/fast-mode
- /docs/en/build-with-claude/files
- /docs/en/build-with-claude/handling-stop-reasons
- /docs/en/build-with-claude/pdf-support
- /docs/en/build-with-claude/prompt-caching
- /docs/en/build-with-claude/search-results
- /docs/en/build-with-claude/structured-outputs
- /docs/en/build-with-claude/token-counting
- /docs/en/build-with-claude/usage-cost-api
- /docs/en/build-with-claude/vision

### Page 10: /docs/en/release-notes/system-prompts
내부 /docs/en/* 링크 없음

### Page 11: /docs/en/resources/overview
- /docs/en/about-claude/glossary
- /docs/en/about-claude/use-case-guides/overview
- /docs/en/claude_api_primer

---

## Unique Discovered Pages (Deduplicated)

Links not already in the 11 target pages:

### about-claude section
- /docs/en/about-claude/glossary
- /docs/en/about-claude/model-deprecations
- /docs/en/about-claude/models
- /docs/en/about-claude/models/overview
- /docs/en/about-claude/models/whats-new-claude-4-6
- /docs/en/about-claude/pricing
- /docs/en/about-claude/use-case-guides/overview

### agents-and-tools section
- /docs/en/agents-and-tools/agent-skills/overview
- /docs/en/agents-and-tools/mcp-connector
- /docs/en/agents-and-tools/tool-use/code-execution-tool
- /docs/en/agents-and-tools/tool-use/computer-use-tool
- /docs/en/agents-and-tools/tool-use/fine-grained-tool-streaming
- /docs/en/agents-and-tools/tool-use/implement-tool-use
- /docs/en/agents-and-tools/tool-use/memory-tool
- /docs/en/agents-and-tools/tool-use/overview
- /docs/en/agents-and-tools/tool-use/programmatic-tool-calling
- /docs/en/agents-and-tools/tool-use/tool-search-tool
- /docs/en/agents-and-tools/tool-use/web-fetch-tool
- /docs/en/agents-and-tools/tool-use/web-search-tool

### api section
- /docs/en/api/admin-api/organization/get-me
- /docs/en/api/beta-headers
- /docs/en/api/deleting-message-batches
- /docs/en/api/errors
- /docs/en/api/messages
- /docs/en/api/models-list
- /docs/en/api/openai-sdk
- /docs/en/api/rate-limits
- /docs/en/api/skills/create-skill

### build-with-claude section
- /docs/en/build-with-claude/adaptive-thinking
- /docs/en/build-with-claude/administration-api
- /docs/en/build-with-claude/batch-processing
- /docs/en/build-with-claude/citations
- /docs/en/build-with-claude/claude-code-analytics-api
- /docs/en/build-with-claude/claude-in-microsoft-foundry
- /docs/en/build-with-claude/claude-on-vertex-ai
- /docs/en/build-with-claude/compaction
- /docs/en/build-with-claude/context-editing
- /docs/en/build-with-claude/context-windows
- /docs/en/build-with-claude/data-residency
- /docs/en/build-with-claude/effort
- /docs/en/build-with-claude/extended-thinking
- /docs/en/build-with-claude/fast-mode
- /docs/en/build-with-claude/files
- /docs/en/build-with-claude/handling-stop-reasons
- /docs/en/build-with-claude/pdf-support
- /docs/en/build-with-claude/prompt-caching
- /docs/en/build-with-claude/prompt-engineering/claude-prompting-best-practices
- /docs/en/build-with-claude/prompt-engineering/prompting-tools
- /docs/en/build-with-claude/search-results
- /docs/en/build-with-claude/streaming
- /docs/en/build-with-claude/structured-outputs
- /docs/en/build-with-claude/token-counting
- /docs/en/build-with-claude/usage-cost-api
- /docs/en/build-with-claude/vision

### other
- /docs/en/claude_api_primer

**Total unique discovered paths: 55**

---

## Key Findings

### 1. 전체 페이지 접근 가능
11개 페이지 모두 `.md` 확장자 직접 접근 방식(`platform.claude.com/docs/en/[path].md`)으로 성공적으로 fetch되었다. 사이트는 JavaScript 렌더링 기반이지만 서버가 마크다운 원문을 별도로 서빙한다.

### 2. 섹션별 특성
- **test-and-evaluate/develop-tests**: 가장 긴 콘텐츠. 성공 기준 정의, 테스트 케이스 유형, 자동화 방법론을 포괄적으로 다루는 핵심 가이드다.
- **strengthen-guardrails 하위 6페이지**: 실용적인 안전/성능 강화 기법을 개별 주제로 분리해 제공. 각 페이지는 독립적으로 읽을 수 있다.
- **handle-streaming-refusals**: Claude 4 모델 이후 신규 도입된 기능. `stop_reason: "refusal"` 처리는 스트리밍 통합 시 필수적인 참조 페이지다.
- **release-notes/overview**: 단일 페이지에서 가장 많은 내부 링크(48개)를 보유. 신규 기능 발견의 허브 역할을 한다.
- **release-notes/system-prompts**: Claude 4.6 Sonnet의 전체 시스템 프롬프트 원문을 포함. 내부 링크는 없지만 모델 행동 이해에 핵심 자료다.

### 3. 주목할 신규 발견 페이지 (release-notes/overview 경유)
다음 페이지들은 AgentNav 사이트맵에 포함될 가능성이 높은 미확인 페이지들이다:
- `/docs/en/build-with-claude/compaction` — 서버 사이드 컨텍스트 요약 (Opus 4.6 전용)
- `/docs/en/build-with-claude/fast-mode` — 빠른 출력 토큰 생성 (연구 프리뷰)
- `/docs/en/build-with-claude/adaptive-thinking` — Opus 4.6 권장 사고 방식
- `/docs/en/build-with-claude/data-residency` — 데이터 거주 지역 제어
- `/docs/en/agents-and-tools/tool-use/programmatic-tool-calling` — 코드 실행 내 도구 호출
- `/docs/en/agents-and-tools/tool-use/tool-search-tool` — 온디맨드 도구 검색
- `/docs/en/agents-and-tools/mcp-connector` — MCP 커넥터

### 4. 콘텐츠 유형 분포
| 유형 | 수량 | 페이지 |
|------|------|--------|
| guide | 6 | develop-tests, reduce-hallucinations, increase-consistency, reduce-latency, reduce-prompt-leak, mitigate-jailbreaks |
| reference | 3 | handle-streaming-refusals, release-notes/overview, release-notes/system-prompts |
| tutorial | 1 | eval-tool |
| overview | 1 | resources/overview |

### 5. 최신 모델 정보 (system-prompts 페이지 기준, 2026-02-17)
- 현재 최신 모델: Claude Opus 4.6, Claude Sonnet 4.6, Claude Haiku 4.5
- API 모델 ID: `claude-opus-4-6`, `claude-sonnet-4-6`, `claude-haiku-4-5-20251001`
- Prefill은 Claude Opus 4.6, Sonnet 4.6, Sonnet 4.5에서 deprecated

---

*Report generated: 2026-03-07*
*Agent: arch-documenter (SW Architect)*
*Source: platform.claude.com/docs/en/*
