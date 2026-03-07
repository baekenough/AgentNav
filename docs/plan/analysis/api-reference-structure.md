# API Reference Structure — Complete Catalog

## Overview

- Total API reference pages: 546
- Core endpoints (non-SDK): 23
- Admin endpoints: 34 (1 root + 33 sub-pages)
- Beta endpoints: 30 (1 root + 29 sub-pages)
- CLI SDK pages: 45
- Language/Tool SDK pages: 9 SDKs × 45 = 405 (TypeScript, Python, Go, Java, Kotlin, Ruby, PHP, C#, Terraform)
- SDK overview pages: 7 (under /docs/en/api/sdks/)
- Infrastructure/reference: 8 standalone pages
- Beta headers page: 1
- Client SDKs page: 1
- OpenAI SDK compat page: 1

### SDK Count Note

10 SDKs are documented with API reference pages:
- 9 language/tool SDKs × 45 pages = 405 pages (TypeScript, Python, Go, Java, Kotlin, Ruby, PHP, C#, Terraform)
- 1 CLI SDK × 45 pages = 45 pages
- 7 SDK overview landing pages (C#, Go, Java, PHP, Python, Ruby, TypeScript) — note: CLI, Kotlin, Terraform have no /sdks/ overview page

---

## Core API Endpoints (Non-SDK)

### Infrastructure & Reference

| Path | Description |
|------|-------------|
| /docs/en/api/overview | API 개요 — 인증, 기본 사용법, 시작 가이드 |
| /docs/en/api/versioning | API 버전 정책 및 호환성 안내 |
| /docs/en/api/errors | HTTP 오류 코드 레퍼런스 (4xx/5xx 상태 코드) |
| /docs/en/api/rate-limits | API 요청 속도 제한 및 토큰 사용량 한도 |
| /docs/en/api/ip-addresses | Anthropic 서버 IP 주소 목록 (방화벽 설정용) |
| /docs/en/api/supported-regions | API 사용 가능 지역 목록 |
| /docs/en/api/service-tiers | 서비스 티어 구분 (빌드/프로덕션 등) |
| /docs/en/api/client-sdks | 공식 클라이언트 SDK 목록 및 링크 |
| /docs/en/api/openai-sdk | OpenAI SDK 호환성 안내 (마이그레이션 가이드) |
| /docs/en/api/beta-headers | 베타 기능 활성화용 HTTP 헤더 레퍼런스 |

### Messages API

| Path | Description |
|------|-------------|
| /docs/en/api/messages | Messages API 허브 — 개요 및 기능 설명 |
| /docs/en/api/messages/create | POST /v1/messages — 메시지 생성 엔드포인트 |
| /docs/en/api/messages/count_tokens | POST /v1/messages/count_tokens — 토큰 수 계산 |
| /docs/en/api/messages/batches | Messages Batches API 허브 |
| /docs/en/api/messages/batches/create | POST /v1/messages/batches — 배치 작업 생성 |
| /docs/en/api/messages/batches/retrieve | GET /v1/messages/batches/{id} — 배치 조회 |
| /docs/en/api/messages/batches/list | GET /v1/messages/batches — 배치 목록 조회 |
| /docs/en/api/messages/batches/cancel | POST /v1/messages/batches/{id}/cancel — 배치 취소 |
| /docs/en/api/messages/batches/results | GET /v1/messages/batches/{id}/results — 배치 결과 조회 |
| /docs/en/api/messages/batches/delete | DELETE /v1/messages/batches/{id} — 배치 삭제 |

### Models API

| Path | Description |
|------|-------------|
| /docs/en/api/models | Models API 허브 — 사용 가능한 모델 목록 |
| /docs/en/api/models/list | GET /v1/models — 전체 모델 목록 조회 |
| /docs/en/api/models/retrieve | GET /v1/models/{model_id} — 특정 모델 정보 조회 |

### Completions API (Legacy)

| Path | Description |
|------|-------------|
| /docs/en/api/completions | Completions API 허브 — 구형 텍스트 완성 API |
| /docs/en/api/completions/create | POST /v1/complete — 텍스트 완성 생성 (deprecated) |

---

## Admin API Endpoints

관리자 API — 조직, 사용자, 워크스페이스, 비용/사용량 리포트 관리

| Path | Description |
|------|-------------|
| /docs/en/api/admin | Admin API 허브 — 조직 관리 API 개요 |

### Organizations

| Path | Description |
|------|-------------|
| /docs/en/api/admin/organizations | Organizations API 허브 |
| /docs/en/api/admin/organizations/me | GET /v1/organizations/me — 현재 조직 정보 조회 |

### Users

| Path | Description |
|------|-------------|
| /docs/en/api/admin/users | Users API 허브 |
| /docs/en/api/admin/users/list | GET /v1/users — 조직 내 사용자 목록 조회 |
| /docs/en/api/admin/users/retrieve | GET /v1/users/{user_id} — 사용자 정보 조회 |
| /docs/en/api/admin/users/update | PATCH /v1/users/{user_id} — 사용자 정보 수정 |
| /docs/en/api/admin/users/delete | DELETE /v1/users/{user_id} — 사용자 삭제 |

### Invites

| Path | Description |
|------|-------------|
| /docs/en/api/admin/invites | Invites API 허브 |
| /docs/en/api/admin/invites/create | POST /v1/invites — 사용자 초대 생성 |
| /docs/en/api/admin/invites/retrieve | GET /v1/invites/{invite_id} — 초대 정보 조회 |
| /docs/en/api/admin/invites/list | GET /v1/invites — 초대 목록 조회 |
| /docs/en/api/admin/invites/delete | DELETE /v1/invites/{invite_id} — 초대 취소/삭제 |

### API Keys

| Path | Description |
|------|-------------|
| /docs/en/api/admin/api_keys | API Keys API 허브 |
| /docs/en/api/admin/api_keys/list | GET /v1/api_keys — API 키 목록 조회 |
| /docs/en/api/admin/api_keys/retrieve | GET /v1/api_keys/{api_key_id} — API 키 정보 조회 |
| /docs/en/api/admin/api_keys/update | PATCH /v1/api_keys/{api_key_id} — API 키 수정 |

### Workspaces

| Path | Description |
|------|-------------|
| /docs/en/api/admin/workspaces | Workspaces API 허브 |
| /docs/en/api/admin/workspaces/create | POST /v1/workspaces — 워크스페이스 생성 |
| /docs/en/api/admin/workspaces/retrieve | GET /v1/workspaces/{workspace_id} — 워크스페이스 조회 |
| /docs/en/api/admin/workspaces/list | GET /v1/workspaces — 워크스페이스 목록 조회 |
| /docs/en/api/admin/workspaces/update | PATCH /v1/workspaces/{workspace_id} — 워크스페이스 수정 |
| /docs/en/api/admin/workspaces/archive | POST /v1/workspaces/{workspace_id}/archive — 워크스페이스 아카이브 |

### Workspace Members

| Path | Description |
|------|-------------|
| /docs/en/api/admin/workspaces/members | Workspace Members API 허브 |
| /docs/en/api/admin/workspaces/members/create | POST /v1/workspaces/{id}/members — 멤버 추가 |
| /docs/en/api/admin/workspaces/members/retrieve | GET /v1/workspaces/{id}/members/{user_id} — 멤버 조회 |
| /docs/en/api/admin/workspaces/members/list | GET /v1/workspaces/{id}/members — 멤버 목록 조회 |
| /docs/en/api/admin/workspaces/members/update | PATCH /v1/workspaces/{id}/members/{user_id} — 멤버 역할 수정 |
| /docs/en/api/admin/workspaces/members/delete | DELETE /v1/workspaces/{id}/members/{user_id} — 멤버 제거 |

### Cost & Usage Reports

| Path | Description |
|------|-------------|
| /docs/en/api/admin/cost_report | Cost Report API 허브 |
| /docs/en/api/admin/cost_report/retrieve | GET /v1/cost_report — 비용 리포트 조회 |
| /docs/en/api/admin/usage_report | Usage Report API 허브 |
| /docs/en/api/admin/usage_report/retrieve_messages | GET /v1/usage_report/messages — Messages API 사용량 조회 |
| /docs/en/api/admin/usage_report/retrieve_claude_code | GET /v1/usage_report/claude_code — Claude Code 사용량 조회 |

---

## Beta API Endpoints

베타 API — 정식 릴리스 전 기능, `anthropic-beta` 헤더로 활성화

| Path | Description |
|------|-------------|
| /docs/en/api/beta | Beta API 허브 — 베타 기능 개요 |

### Beta Files API

| Path | Description |
|------|-------------|
| /docs/en/api/beta/files | Files API 허브 — 파일 업로드/관리 |
| /docs/en/api/beta/files/upload | POST /v1/files — 파일 업로드 |
| /docs/en/api/beta/files/list | GET /v1/files — 업로드된 파일 목록 조회 |
| /docs/en/api/beta/files/retrieve_metadata | GET /v1/files/{file_id} — 파일 메타데이터 조회 |
| /docs/en/api/beta/files/download | GET /v1/files/{file_id}/content — 파일 다운로드 |
| /docs/en/api/beta/files/delete | DELETE /v1/files/{file_id} — 파일 삭제 |

### Beta Messages API

| Path | Description |
|------|-------------|
| /docs/en/api/beta/messages | Beta Messages API 허브 |
| /docs/en/api/beta/messages/create | POST /v1/messages (beta) — 베타 기능 포함 메시지 생성 |
| /docs/en/api/beta/messages/count_tokens | POST /v1/messages/count_tokens (beta) — 베타 토큰 카운트 |
| /docs/en/api/beta/messages/batches | Beta Message Batches API 허브 |
| /docs/en/api/beta/messages/batches/create | POST /v1/messages/batches (beta) — 베타 배치 생성 |
| /docs/en/api/beta/messages/batches/retrieve | GET /v1/messages/batches/{id} (beta) — 베타 배치 조회 |
| /docs/en/api/beta/messages/batches/list | GET /v1/messages/batches (beta) — 베타 배치 목록 |
| /docs/en/api/beta/messages/batches/cancel | POST /v1/messages/batches/{id}/cancel (beta) — 베타 배치 취소 |
| /docs/en/api/beta/messages/batches/results | GET /v1/messages/batches/{id}/results (beta) — 베타 배치 결과 |
| /docs/en/api/beta/messages/batches/delete | DELETE /v1/messages/batches/{id} (beta) — 베타 배치 삭제 |

### Beta Models API

| Path | Description |
|------|-------------|
| /docs/en/api/beta/models | Beta Models API 허브 |
| /docs/en/api/beta/models/list | GET /v1/models (beta) — 베타 모델 목록 |
| /docs/en/api/beta/models/retrieve | GET /v1/models/{id} (beta) — 베타 모델 조회 |

### Beta Skills API

| Path | Description |
|------|-------------|
| /docs/en/api/beta/skills | Skills API 허브 — 에이전트 스킬 관리 |
| /docs/en/api/beta/skills/create | POST /v1/skills — 스킬 생성 |
| /docs/en/api/beta/skills/retrieve | GET /v1/skills/{skill_id} — 스킬 조회 |
| /docs/en/api/beta/skills/list | GET /v1/skills — 스킬 목록 조회 |
| /docs/en/api/beta/skills/delete | DELETE /v1/skills/{skill_id} — 스킬 삭제 |
| /docs/en/api/beta/skills/versions | Skill Versions API 허브 |
| /docs/en/api/beta/skills/versions/create | POST /v1/skills/{id}/versions — 스킬 버전 생성 |
| /docs/en/api/beta/skills/versions/retrieve | GET /v1/skills/{id}/versions/{version_id} — 버전 조회 |
| /docs/en/api/beta/skills/versions/list | GET /v1/skills/{id}/versions — 버전 목록 조회 |
| /docs/en/api/beta/skills/versions/delete | DELETE /v1/skills/{id}/versions/{version_id} — 버전 삭제 |

---

## SDK-Specific References

각 SDK는 동일한 45페이지 구조를 공유합니다. SDK별 차이는 언어 고유 코드 예시와 타입 시스템뿐입니다.

| SDK | Pages | Base Path |
|-----|-------|-----------|
| TypeScript | 45 | /docs/en/api/typescript/ |
| Python | 45 | /docs/en/api/python/ |
| Go | 45 | /docs/en/api/go/ |
| Java | 45 | /docs/en/api/java/ |
| Kotlin | 45 | /docs/en/api/kotlin/ |
| Ruby | 45 | /docs/en/api/ruby/ |
| PHP | 45 | /docs/en/api/php/ |
| C# | 45 | /docs/en/api/csharp/ |
| Terraform | 45 | /docs/en/api/terraform/ |
| CLI | 45 | /docs/en/api/cli/ |

### Common Structure (45 pages — same for all 10 SDKs)

아래는 TypeScript SDK를 기준으로 한 45페이지 전체 구조입니다. 나머지 9개 SDK도 동일한 경로 패턴을 따릅니다.

#### TypeScript SDK — Complete Page List

| Path | Description |
|------|-------------|
| /docs/en/api/typescript/beta | TypeScript Beta API 허브 |
| /docs/en/api/typescript/beta/files | TS Beta Files API 허브 |
| /docs/en/api/typescript/beta/files/delete | TS — 파일 삭제 |
| /docs/en/api/typescript/beta/files/download | TS — 파일 다운로드 |
| /docs/en/api/typescript/beta/files/list | TS — 파일 목록 조회 |
| /docs/en/api/typescript/beta/files/retrieve_metadata | TS — 파일 메타데이터 조회 |
| /docs/en/api/typescript/beta/files/upload | TS — 파일 업로드 |
| /docs/en/api/typescript/beta/messages | TS Beta Messages API 허브 |
| /docs/en/api/typescript/beta/messages/batches | TS Beta Message Batches 허브 |
| /docs/en/api/typescript/beta/messages/batches/cancel | TS — 배치 취소 |
| /docs/en/api/typescript/beta/messages/batches/create | TS — 배치 생성 |
| /docs/en/api/typescript/beta/messages/batches/delete | TS — 배치 삭제 |
| /docs/en/api/typescript/beta/messages/batches/list | TS — 배치 목록 |
| /docs/en/api/typescript/beta/messages/batches/results | TS — 배치 결과 |
| /docs/en/api/typescript/beta/messages/batches/retrieve | TS — 배치 조회 |
| /docs/en/api/typescript/beta/messages/count_tokens | TS Beta — 토큰 카운트 |
| /docs/en/api/typescript/beta/messages/create | TS Beta — 메시지 생성 |
| /docs/en/api/typescript/beta/models | TS Beta Models API 허브 |
| /docs/en/api/typescript/beta/models/list | TS Beta — 모델 목록 |
| /docs/en/api/typescript/beta/models/retrieve | TS Beta — 모델 조회 |
| /docs/en/api/typescript/beta/skills | TS Beta Skills API 허브 |
| /docs/en/api/typescript/beta/skills/create | TS — 스킬 생성 |
| /docs/en/api/typescript/beta/skills/delete | TS — 스킬 삭제 |
| /docs/en/api/typescript/beta/skills/list | TS — 스킬 목록 |
| /docs/en/api/typescript/beta/skills/retrieve | TS — 스킬 조회 |
| /docs/en/api/typescript/beta/skills/versions | TS Skill Versions 허브 |
| /docs/en/api/typescript/beta/skills/versions/create | TS — 스킬 버전 생성 |
| /docs/en/api/typescript/beta/skills/versions/delete | TS — 스킬 버전 삭제 |
| /docs/en/api/typescript/beta/skills/versions/list | TS — 스킬 버전 목록 |
| /docs/en/api/typescript/beta/skills/versions/retrieve | TS — 스킬 버전 조회 |
| /docs/en/api/typescript/completions | TS Completions API 허브 |
| /docs/en/api/typescript/completions/create | TS — 텍스트 완성 생성 |
| /docs/en/api/typescript/messages | TS Messages API 허브 |
| /docs/en/api/typescript/messages/batches | TS Message Batches 허브 |
| /docs/en/api/typescript/messages/batches/cancel | TS — 배치 취소 |
| /docs/en/api/typescript/messages/batches/create | TS — 배치 생성 |
| /docs/en/api/typescript/messages/batches/delete | TS — 배치 삭제 |
| /docs/en/api/typescript/messages/batches/list | TS — 배치 목록 |
| /docs/en/api/typescript/messages/batches/results | TS — 배치 결과 |
| /docs/en/api/typescript/messages/batches/retrieve | TS — 배치 조회 |
| /docs/en/api/typescript/messages/count_tokens | TS — 토큰 카운트 |
| /docs/en/api/typescript/messages/create | TS — 메시지 생성 |
| /docs/en/api/typescript/models | TS Models API 허브 |
| /docs/en/api/typescript/models/list | TS — 모델 목록 |
| /docs/en/api/typescript/models/retrieve | TS — 모델 조회 |

#### 45페이지 구조 분석

| 섹션 | 페이지 수 | 포함 내용 |
|------|-----------|-----------|
| beta (30) | 30 | files(6), messages(10), models(3), skills(11) |
| completions (2) | 2 | completions hub + create |
| messages (10) | 10 | messages hub, batches(8), count_tokens, create |
| models (3) | 3 | models hub, list, retrieve |
| **합계** | **45** | |

---

## SDK Overview Pages

SDK 랜딩 페이지 (`/docs/en/api/sdks/` 하위) — 7개 SDK만 존재 (CLI, Kotlin, Terraform은 없음)

| Path | SDK | Description |
|------|-----|-------------|
| /docs/en/api/sdks/csharp | C# | C# SDK 개요 및 시작 가이드 |
| /docs/en/api/sdks/go | Go | Go SDK 개요 및 시작 가이드 |
| /docs/en/api/sdks/java | Java | Java SDK 개요 및 시작 가이드 |
| /docs/en/api/sdks/php | PHP | PHP SDK 개요 및 시작 가이드 |
| /docs/en/api/sdks/python | Python | Python SDK 개요 및 시작 가이드 |
| /docs/en/api/sdks/ruby | Ruby | Ruby SDK 개요 및 시작 가이드 |
| /docs/en/api/sdks/typescript | TypeScript | TypeScript SDK 개요 및 시작 가이드 |

---

## Complete URL Count Verification

| Category | Count |
|----------|-------|
| Core infrastructure & reference | 10 |
| Messages API (core) | 10 |
| Models API (core) | 3 |
| Completions API (core, legacy) | 2 |
| Admin API | 34 |
| Beta API | 30 |
| TypeScript SDK | 45 |
| Python SDK | 45 |
| Go SDK | 45 |
| Java SDK | 45 |
| Kotlin SDK | 45 |
| Ruby SDK | 45 |
| PHP SDK | 45 |
| C# SDK | 45 |
| Terraform SDK | 45 |
| CLI SDK | 45 |
| SDK overview pages (/sdks/) | 7 |
| **Total** | **546** |

---

## AgentNav Implications

### agents.txt에서 546개 API 레퍼런스 페이지 처리 방안

#### 핵심 문제

546개 페이지를 개별 항목으로 나열하면 agents.txt가 불필요하게 비대해집니다. SDK별 45페이지는 구조가 동일하므로 패턴 기반 그룹화가 필수입니다.

#### 권장 전략

**1. 패턴 기반 그룹화 (SDK pages)**

```
# API Reference — SDK Pages (450 pages)
# Pattern: /docs/en/api/{sdk}/{section}/...
# SDKs: typescript, python, go, java, kotlin, ruby, php, csharp, terraform, cli
# Each SDK: 45 pages (completions/2, messages/10, models/3, beta/30)
Allow: /docs/en/api/typescript/*
Allow: /docs/en/api/python/*
# ... (각 SDK별 단일 와일드카드 규칙)
```

**2. 고유 콘텐츠 개별 등록 (Core + Admin + Beta)**

- Core (23개): 각 엔드포인트별 고유 기능 설명 존재 → 개별 등록 권장
- Admin (34개): 조직 관리 기능으로 고유 콘텐츠 → 개별 등록 권장
- Beta (30개): 베타 기능으로 고유 콘텐츠 → 개별 등록 권장

**3. 콘텐츠 유형 분류**

| 콘텐츠 유형 | 페이지 수 | AgentNav 처리 방식 |
|-------------|-----------|-------------------|
| 고유 콘텐츠 (Core + Admin + Beta) | 87 | 개별 URL 등록, 상세 description |
| SDK 반복 콘텐츠 (10 SDKs × 45) | 450 | 패턴 와일드카드 + 1개 SDK 샘플 상세 등록 |
| SDK 개요 페이지 | 7 | 개별 URL 등록 |
| **합계** | **544** | |

> Note: /docs/en/api/client-sdks (1) + /docs/en/api/openai-sdk (1) = 2페이지 인프라 항목 별도

#### SDK 페이지 우선순위

agents.txt에 SDK 상세 페이지를 포함할 경우, TypeScript와 Python을 우선 등록합니다. 두 SDK가 가장 많이 사용되며, 나머지 SDK는 동일 구조를 따르므로 참조 예시로 충분합니다.

#### Skills API 주목

`/docs/en/api/beta/skills/*` 경로는 AgentNav 프로젝트와 직접 관련된 Skills API입니다. 스킬 생성, 버전 관리, 조회/삭제 엔드포인트를 포함하므로 개별 등록 및 높은 우선순위 부여를 권장합니다.
