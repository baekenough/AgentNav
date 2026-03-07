# Section D-1: API — Verification Report

---

## Scope Correction (Round 2 교차 검증 결과)

> 업데이트: 2026-03-07 — round2-cross-validation.md 참조

### 원래 분석 범위 vs 실제 사이트맵 범위

| 항목 | 원래 D-1 범위 | 실제 사이트맵 전체 | 비고 |
|------|-------------|-----------------|------|
| 분석한 페이지 | 17개 (+ 1 보너스) | ~590개 | D-1은 전체의 3.1% |
| 커버한 섹션 | overview, client-sdks, sdks/*, rate-limits, errors, versioning, beta-headers, service-tiers, supported-regions, ip-addresses, openai-sdk, messages | 위 + admin/*, beta/*, messages/*, models/*, completions/*, python/*, typescript/*, java/*, go/*, csharp/*, ruby/*, php/*, kotlin/*, terraform/*, cli/* | |

### 미분석 API 페이지 (사이트맵 확인)

| 섹션 | 페이지 수 | 설명 |
|------|---------|------|
| /api/admin/* | 34 | 조직·워크스페이스·유저·API키·초대·사용량·비용 보고서 관리 엔드포인트 |
| /api/beta/* | 30 | Files, Messages/Batches, Models, Skills + Versions 베타 엔드포인트 |
| /api/messages/* | 8 | batches (CRUD 6개) + count_tokens + create |
| /api/models/* | 3 | 섹션 허브, list, retrieve |
| /api/completions/* | 2 | 섹션 허브, create (레거시) |
| /api/python/* | 45 | Python SDK별 레퍼런스 (동일 구조 반복) |
| /api/typescript/* | 45 | TypeScript SDK별 레퍼런스 |
| /api/java/* | 45 | Java SDK별 레퍼런스 |
| /api/go/* | 45 | Go SDK별 레퍼런스 |
| /api/csharp/* | 45 | C# SDK별 레퍼런스 |
| /api/ruby/* | 45 | Ruby SDK별 레퍼런스 |
| /api/php/* | 45 | PHP SDK별 레퍼런스 |
| /api/kotlin/* | 45 | Kotlin SDK별 레퍼런스 |
| /api/terraform/* | 45 | Terraform SDK별 레퍼런스 |
| /api/cli/* | 45 | CLI SDK별 레퍼런스 |

### "Discovered Pages"의 경로 불일치 주의

이 보고서의 "Discovered Pages" 섹션에서 수집한 `/api/admin-api/` 형식 경로들은 실제 사이트맵의 `/api/admin/` 형식 경로와 다름. 예:
- 보고서 발견: `/api/admin-api/workspaces/get-workspace` → 실제: `/api/admin/workspaces/retrieve`
- 보고서 발견: `/api/files-create` → 실제: `/api/beta/files/upload`
- 보고서 발견: `/api/models-list` → 실제: `/api/models/list`

이는 페이지가 링크에서 구 경로(별칭)를 사용하거나, URL 구조 변경 이전 링크일 가능성이 있음.

---

## Summary
- Total pages checked: 18 (17 sitemap + 1 cross-reference bonus)
- Verified: 18 ✅
- Failed: 0 ❌
- New pages discovered: 48

## Page Catalog

| # | Path | Status | Title | Type | Description |
|---|------|--------|-------|------|-------------|
| 1 | /docs/en/api/overview | ✅ | API Overview | overview | Claude API 전체 구조 소개 및 네비게이션 허브 (Messages, Files, Models, Admin, Skills, Completions 등 엔드포인트 그룹 안내) |
| 2 | /docs/en/api/client-sdks | ✅ | Client SDKs | reference | Python, TypeScript, Java, Go, Ruby, C#, PHP 공식 SDK 목록 및 각 SDK 페이지 링크 |
| 3 | /docs/en/api/rate-limits | ✅ | Rate limits | reference | API 남용 방지 및 용량 관리를 위한 조직별 사용 한도 설명 (RPM, TPM, 계층별 제한) |
| 4 | /docs/en/api/errors | ✅ | Errors | reference | Claude API 오류 유형 및 HTTP 상태 코드 설명 (4xx/5xx 오류, 재시도 전략, 스트리밍 오류 처리) |
| 5 | /docs/en/api/versioning | ✅ | Versions | reference | API 버전 관리 정책 (`anthropic-version` 헤더 필수, 현재 안정 버전 `2023-06-01`) |
| 6 | /docs/en/api/beta-headers | ✅ | Beta headers | reference | 베타 기능 활성화를 위한 `anthropic-beta` 헤더 사용법 및 현재 지원되는 베타 기능 목록 |
| 7 | /docs/en/api/service-tiers | ✅ | Service tiers | reference | 가용성·성능·비용 예측 가능성 기준으로 서비스 계층 선택 (Standard/Priority 티어, 1M+ 토큰 컨텍스트 제한 등) |
| 8 | /docs/en/api/supported-regions | ✅ | Supported regions | reference | Claude API 접근이 지원되는 국가·지역·영토 목록 |
| 9 | /docs/en/api/ip-addresses | ✅ | IP addresses | reference | 방화벽 규칙 설정을 위한 Anthropic 서비스 고정 IP 주소 목록 (인바운드/아웃바운드) |
| 10 | /docs/en/api/openai-sdk | ✅ | OpenAI SDK compatibility | guide | OpenAI SDK를 최소한의 코드 변경으로 Claude API 테스트에 활용하는 호환성 레이어 안내 |
| 11 | /docs/en/api/sdks/python | ✅ | Python SDK | reference | Anthropic Python SDK 설치 및 구성 가이드 (동기/비동기 클라이언트, 스트리밍, 도구 사용) |
| 12 | /docs/en/api/sdks/typescript | ✅ | TypeScript SDK | reference | Anthropic TypeScript SDK 설치 및 구성 가이드 (Node.js/Deno/Bun/브라우저 지원, MCP 통합) |
| 13 | /docs/en/api/sdks/java | ✅ | Java SDK | reference | Anthropic Java SDK 설치 및 구성 가이드 (빌더 패턴, 비동기 지원, 도구 사용) |
| 14 | /docs/en/api/sdks/go | ✅ | Go SDK | reference | Anthropic Go SDK 설치 및 구성 가이드 (컨텍스트 기반 취소, 함수형 옵션, 스트리밍) |
| 15 | /docs/en/api/sdks/csharp | ✅ | C# SDK | reference | Anthropic C# SDK 설치 및 구성 가이드 (.NET 애플리케이션 지원, IChatClient 통합) |
| 16 | /docs/en/api/sdks/ruby | ✅ | Ruby SDK | reference | Anthropic Ruby SDK 설치 및 구성 가이드 (Sorbet 타입, 스트리밍 헬퍼, 연결 풀링) |
| 17 | /docs/en/api/sdks/php | ✅ | PHP SDK | reference | Anthropic PHP SDK 설치 및 구성 가이드 (값 객체, 빌더 패턴, 스트리밍 응답) |
| 18 | /docs/en/api/messages | ✅ | Messages | reference | Messages API 엔드포인트 레퍼런스 (메시지 생성·토큰 카운팅·배치 CRUD 엔드포인트 목록) |

## Discovered Pages (not in sitemap)

Below are internal `/docs/en/...` links discovered during page fetching that are NOT in the 18 pages above.

### From Page 1: /docs/en/api/overview
| Discovered Link | Notes |
|----------------|-------|
| /docs/en/api/admin | Admin API 엔드포인트 섹션 |
| /docs/en/api/beta | Beta 엔드포인트 섹션 |
| /docs/en/api/completions | Completions API (레거시) |
| /docs/en/api/completions/create | Create a Text Completion |
| /docs/en/api/creating-message-batches | Message Batches 생성 |
| /docs/en/api/files-create | Files API 생성 |
| /docs/en/api/messages-count-tokens | 메시지 토큰 카운팅 (구 경로) |
| /docs/en/api/messages/count_tokens | 메시지 토큰 카운팅 (신 경로) |
| /docs/en/api/messages/create | 메시지 생성 엔드포인트 |
| /docs/en/api/models | Models API 섹션 |
| /docs/en/api/models-list | 모델 목록 (구 경로) |
| /docs/en/api/models/list | 모델 목록 (신 경로) |
| /docs/en/api/models/retrieve | 특정 모델 조회 |
| /docs/en/api/skills/create-skill | Skills 생성 엔드포인트 |
| /docs/en/build-with-claude/batch-processing | 배치 처리 가이드 |
| /docs/en/build-with-claude/claude-in-microsoft-foundry | Microsoft Foundry 통합 |
| /docs/en/build-with-claude/claude-on-amazon-bedrock | Amazon Bedrock 통합 |
| /docs/en/build-with-claude/claude-on-vertex-ai | Vertex AI 통합 |
| /docs/en/build-with-claude/data-residency | 데이터 레지던시 |
| /docs/en/build-with-claude/files | Files API 가이드 |
| /docs/en/build-with-claude/overview | 기능 개요 |
| /docs/en/build-with-claude/working-with-messages | Messages API 사용 가이드 |
| /docs/en/get-started | 시작하기 |
| /docs/en/home | 홈 |
| /docs/en/intro | 소개 |
| /docs/en/release-notes/overview | 릴리스 노트 |
| /docs/en/resources/overview | 리소스 개요 |

### From Page 3: /docs/en/api/rate-limits
| Discovered Link | Notes |
|----------------|-------|
| /docs/en/build-with-claude/fast-mode | Fast mode (속도 제한 연관) |
| /docs/en/build-with-claude/prompt-caching | 프롬프트 캐싱 (TPM 절감) |
| /docs/en/build-with-claude/workspaces | 워크스페이스 (한도 설정) |

### From Page 7: /docs/en/api/service-tiers
| Discovered Link | Notes |
|----------------|-------|
| /docs/en/about-claude/model-deprecations | 모델 수명 주기 관리 |
| /docs/en/about-claude/models/overview | 모델 개요 |
| /docs/en/build-with-claude/context-windows | 컨텍스트 윈도우 |

### From Page 10: /docs/en/api/openai-sdk
| Discovered Link | Notes |
|----------------|-------|
| /docs/en/build-with-claude/citations | 인용 기능 |
| /docs/en/build-with-claude/extended-thinking | 확장 사고 |
| /docs/en/build-with-claude/pdf-support | PDF 지원 |
| /docs/en/build-with-claude/prompt-caching | 프롬프트 캐싱 |
| /docs/en/build-with-claude/structured-outputs | 구조화 출력 |

### From Page 11: /docs/en/api/sdks/python
| Discovered Link | Notes |
|----------------|-------|
| /docs/en/agents-and-tools/tool-use/overview | 도구 사용 개요 |

### From Page 12: /docs/en/api/sdks/typescript
| Discovered Link | Notes |
|----------------|-------|
| /docs/en/agents-and-tools/mcp | MCP 문서 |
| /docs/en/agents-and-tools/mcp-connector | MCP 커넥터 |
| /docs/en/agents-and-tools/tool-use/overview | 도구 사용 개요 |

### From Page 16: /docs/en/api/sdks/ruby
| Discovered Link | Notes |
|----------------|-------|
| /docs/en/agents-and-tools/tool-use/implement-tool-use | 도구 사용 구현 |

### From Page 18: /docs/en/api/messages
| Discovered Link | Notes |
|----------------|-------|
| /docs/en/api/messages/batches/cancel | 배치 취소 |
| /docs/en/api/messages/batches/create | 배치 생성 |
| /docs/en/api/messages/batches/delete | 배치 삭제 |
| /docs/en/api/messages/batches/list | 배치 목록 |
| /docs/en/api/messages/batches/results | 배치 결과 조회 |
| /docs/en/api/messages/batches/retrieve | 배치 단건 조회 |

## Unique Discovered Pages (Deduplicated)

48개의 고유 내부 문서 페이지가 발견되었으며 D-1의 18개 페이지에 포함되지 않습니다. 마스터 사이트맵과 교차 검증이 필요합니다.

### api section (미확인 엔드포인트 레퍼런스)
1. /docs/en/api/admin
2. /docs/en/api/beta
3. /docs/en/api/completions
4. /docs/en/api/completions/create
5. /docs/en/api/creating-message-batches
6. /docs/en/api/files-create
7. /docs/en/api/messages-count-tokens
8. /docs/en/api/messages/batches/cancel
9. /docs/en/api/messages/batches/create
10. /docs/en/api/messages/batches/delete
11. /docs/en/api/messages/batches/list
12. /docs/en/api/messages/batches/results
13. /docs/en/api/messages/batches/retrieve
14. /docs/en/api/messages/count_tokens
15. /docs/en/api/messages/create
16. /docs/en/api/models
17. /docs/en/api/models-list
18. /docs/en/api/models/list
19. /docs/en/api/models/retrieve
20. /docs/en/api/skills/create-skill

### build-with-claude section
21. /docs/en/build-with-claude/batch-processing
22. /docs/en/build-with-claude/citations
23. /docs/en/build-with-claude/claude-in-microsoft-foundry
24. /docs/en/build-with-claude/claude-on-amazon-bedrock
25. /docs/en/build-with-claude/claude-on-vertex-ai
26. /docs/en/build-with-claude/context-windows
27. /docs/en/build-with-claude/data-residency
28. /docs/en/build-with-claude/extended-thinking
29. /docs/en/build-with-claude/fast-mode
30. /docs/en/build-with-claude/files
31. /docs/en/build-with-claude/overview
32. /docs/en/build-with-claude/pdf-support
33. /docs/en/build-with-claude/prompt-caching
34. /docs/en/build-with-claude/streaming
35. /docs/en/build-with-claude/structured-outputs
36. /docs/en/build-with-claude/working-with-messages
37. /docs/en/build-with-claude/workspaces

### agents-and-tools section
38. /docs/en/agents-and-tools/mcp
39. /docs/en/agents-and-tools/mcp-connector
40. /docs/en/agents-and-tools/tool-use/implement-tool-use
41. /docs/en/agents-and-tools/tool-use/overview

### about-claude section
42. /docs/en/about-claude/model-deprecations
43. /docs/en/about-claude/models/overview

### Top-level / navigation
44. /docs/en/get-started
45. /docs/en/home
46. /docs/en/intro
47. /docs/en/release-notes/overview
48. /docs/en/resources/overview

## Key Findings

1. **모든 18개 페이지 검증 완료** — 17개의 사이트맵 페이지 + 크로스 레퍼런스로 발견된 `api/messages` 보너스 페이지 모두 정상 로드 및 콘텐츠 확인.

2. **api/messages는 실제 존재하는 페이지** — 사이트맵에는 없지만 API Reference 섹션의 핵심 페이지로, 메시지 생성(`/create`), 토큰 카운팅(`/count_tokens`), 배치 관련 6개 서브엔드포인트(`/batches/*`)를 포함하는 허브 페이지.

3. **API Reference 섹션에 추가 미등록 페이지 다수 발견**:
   - `/docs/en/api/admin` — Admin API (조직/워크스페이스/API 키 관리)
   - `/docs/en/api/beta` — Beta 엔드포인트 목록
   - `/docs/en/api/completions` — 레거시 Completions API
   - `/docs/en/api/models*` — Models API 엔드포인트들
   - `/docs/en/api/skills/create-skill` — Skills 생성 엔드포인트
   - Message Batches 서브엔드포인트 6개 (`/cancel`, `/create`, `/delete`, `/list`, `/results`, `/retrieve`)

4. **SDK 페이지 구조 일관성** — 7개 SDK 페이지(Python, TypeScript, Java, Go, C#, Ruby, PHP) 모두 동일한 구조로 작성됨. TypeScript SDK만 유일하게 MCP 통합 문서(`/docs/en/agents-and-tools/mcp`) 링크를 포함.

5. **페이지 유형 분포** — 17개 중 16개가 `reference` 유형, 1개(`openai-sdk`)가 `guide` 유형. 이 섹션은 주로 API 레퍼런스와 구성 참조 정보로 구성됨.

6. **중복/리다이렉트 의심 경로** — `/docs/en/api/models-list`와 `/docs/en/api/models/list`, `/docs/en/api/messages-count-tokens`와 `/docs/en/api/messages/count_tokens`가 동시에 발견됨. 구 경로(하이픈 표기)가 신 경로(슬래시 표기)로 리다이렉트될 가능성 있음.

7. **`api/versioning` 실제 제목은 "Versions"** — URL은 `versioning`이나 H1 제목은 `Versions`로 약간의 불일치 있음. 사이트맵이나 네비게이션에서 혼용될 수 있으므로 주의 필요.
