# TXT Format Verification Summary

**Verification Date**: 2026-04-17
**Framework**: tests/nav-agent-test.py
**Format**: agents.txt (all sources)
**Max Queries per Source**: 40

> **(v2: 실측 완료)** — 2026-04-17 파서 버그 수정 후 재측정 완료.
> v1 결과는 버그 상태(섹션 1개 파싱), v2는 `_expand_flat_sections()` 수정 후 실측값.

## Results Matrix

### v1 — 파서 버그 상태 (참고용)

| Source | Pages | Sections | Queries Run | Score | Grade | Duration |
|--------|-------|----------|-------------|-------|-------|----------|
| claude-code | 111 | 1 (parsed) | 10 | 9.7/10 (96.7%) | A | 16.8s |
| claude-api | 1,035 | 1 (parsed) | 10 | 8.0/10 (80.1%) | B | 24.9s |
| gpt-codex | 71 | 40 | 40 | 40.0/40 (100.0%) | A | 17.2s |
| gemini-cli | 90 | 14 | 33 | 31.2/33 (94.5%) | A | 18.8s |

### v2 — 파서 수정 후 실측값 (2026-04-17)

| Source | Pages | Sections | Queries Run | Score | Grade | Duration |
|--------|-------|----------|-------------|-------|-------|----------|
| claude-code | 111 | **80** | **35** | **32.0/35 (91.4%)** | **A** | 25.7s |
| claude-api | 1,035 | **82** | **40** | **20.4/40 (51.0%)** | **F** | 58.8s |
| gpt-codex | 71 | 40 | 40 | 40.0/40 (100.0%) | A | 17.2s |
| gemini-cli | 90 | 14 | 33 | 31.2/33 (94.5%) | A | 18.8s |

## Category Performance (v2 실측값)

> claude-code/claude-api는 v2(파서 수정 후) 실측값. gpt-codex/gemini-cli는 이전 측정값 유지.

| Category | claude-code (v2) | claude-api (v2) | gpt-codex | gemini-cli |
|----------|-----------------|-----------------|-----------|------------|
| Direct Lookup | 100% (12/12) | 42% (5.1/12) | 100% | 85% |
| Full URL Construction | 100% (8/8) | 100% (8/8) | 100% | 100% |
| Page Type | 100% (4/4) | 100% (4/4) | 100% | 100% |
| Section Enumeration | 33% (1/3) | 29% (2.3/8) | 100% | 100% |
| Structure | 88% (7/8) | 12% (1/8) | 100% | 100% |

## Key Findings (v2 실측 기반)

- **Full URL Construction, Page Type**: claude-code/claude-api 모두 100% — TXT 포맷이 URL 구성과 페이지 타입 분류를 완벽하게 전달
- **claude-code v2 (Grade A, 91.4%)**: 섹션 80개로 확장 후 쿼리 35개 실행. Section Enumeration(33%)과 Structure(88%) 일부 실패. 섹션 카운트 질의(A2: expected 80, got 1)와 하위 섹션 슬러그 열거(C1, C2) 실패 — LLM이 flat TXT에서 섹션 수를 직접 세지 못함
- **claude-api v2 (Grade F, 51.0%)**: 섹션 82개로 확장 후 쿼리 40개 실행. Direct Lookup(42%), Section Enumeration(29%), Structure(12%) 크게 저조. 59,872 chars의 대용량 TXT에서 sdk 언어별 섹션(cli, csharp, go 등)을 LLM이 인식 못하고, 경로에 `.md` suffix 포함 반환으로 partial credit만 획득
- **v1 → v2 개선**: 쿼리 수 10→35(claude-code), 10→40(claude-api) 확장으로 통계 신뢰도 크게 향상. claude-code는 Grade 유지(A), claude-api는 Grade B(80%)→F(51%)로 드러난 실제 약점이 v1에서 숨겨져 있었음
- **근본 원인 (claude-api 저조)**: TXT 포맷의 flat 구조가 대규모 SDK 문서(1,035p, 10 SDKs)에서 섹션 경계를 명확히 표현하지 못함 — LLM이 섹션명을 인식하려면 명시적 헤더가 필요

## Failed Query Patterns

### 주요 실패 패턴 요약

| 패턴 | 발생 소스 | 원인 |
|------|----------|------|
| `.md` 확장자 포함 경로 반환 | claude-api (B2) | TXT 포맷이 `.md` suffix 포함, grader는 strip된 경로 기대 |
| 경로 prefix 누락 | claude-api (B1, B2) | LLM이 `/docs/en/` prefix 생략, partial match로 0.25~0.43점 |
| 슬러그 목록 불일치 | claude-code (C2), claude-api (C2) | LLM이 샘플 슬러그 대신 예시 파일명 제시 |
| 최상위 경로 인식 실패 | gemini-cli (B1) | `/docs/` 경로가 너무 짧아 특정 LLM이 `/`로 단축 반환 |
| 경로명 변형 | gemini-cli (B8) | `cli-reference` vs `commands` — TXT 내 경로와 JSON ground truth 불일치 가능성 |

## Structural Issue: Single-Section Sources (FIXED in v2)

agents.json에서 sections가 1개로 파싱된 소스(claude-code, claude-api)는 쿼리 생성 다양성이 크게 제한됩니다:

- claude-code: 실제 10개 섹션이지만 TXT→JSON 파싱 시 1개 섹션으로 집계됨
- claude-api: 실제 20개 섹션이지만 동일 현상

결과적으로 두 소스의 max-queries 40 설정에도 불구하고 실제 10개만 실행되어, Grade 신뢰도가 gpt-codex/gemini-cli 대비 낮음.

### 수정 내용 (2026-04-17)

`tests/nav-agent-test.py`에 `_expand_flat_sections()` 함수 추가:
- 단일 flat 섹션(20 pages 초과)을 path_prefix 이후 경로 세그먼트 기준으로 논리 섹션으로 분리
- 지배 섹션(80% 초과)이 있으면 2-level 경로 grouping 적용 (claude-api의 `api/` → `api/python`, `api/go` 등)
- gpt-codex/gemini-cli처럼 이미 세분화된 소스는 영향 없음 (backward-compatible)

## Conclusion

### 전체 판정 (v2 실측)

| 메트릭 | v1 (버그) | v2 (실측) |
|--------|-----------|-----------|
| Grade A 달성 소스 | 3/4 | **3/4** (claude-code, gpt-codex, gemini-cli) |
| Grade F 달성 소스 | 0/4 | **1/4** (claude-api) |
| 전체 평균 점수 | ~93% (10+10+40+33 = 93 queries) | **79.4%** (35+40+40+33 = 148 queries) |
| 최고 성능 | gpt-codex 100% | gpt-codex 100% |
| 최저 성능 | claude-api 80.1% (10 queries) | **claude-api 51.0% (40 queries)** |

### TXT 포맷 판정 (v2 실측 기반 최종)

v2 실측 결과, TXT 포맷의 실제 성능 격차가 드러났습니다:

- **강점**: Full URL Construction, Page Type — 모든 소스 100% 달성. TXT가 URL 구성과 타입 분류를 완벽하게 전달
- **약점**: 대용량 SDK 문서(claude-api, 60KB, 82섹션)에서 Section Enumeration(29%), Structure(12%), Direct Lookup(42%) 모두 저조 — flat TXT 구조가 섹션 경계 표현에 한계
- **v1에서 숨겨진 문제**: 섹션 1개 파싱으로 쿼리 10개만 실행하여 claude-api가 Grade B(80%)처럼 보였으나, 실제는 Grade F(51%)
- **MD 포맷 대비**: MD는 모든 소스 Grade A(100%) — TXT 대비 뚜렷한 우위

**권장**:
- 소형 문서 세트(~100p, ~10 섹션): TXT 충분 (claude-code Grade A 91.4% 확인)
- 대형 문서 세트(1000p+, 다수 섹션): MD 필수 (claude-api TXT는 Grade F — 실용 불가)

## Individual Reports

- `/Users/sangyi/workspace/projects/AgentNav/tests/reports/claude-code-txt-report.md`
- `/Users/sangyi/workspace/projects/AgentNav/tests/reports/claude-api-txt-report.md`
- `/Users/sangyi/workspace/projects/AgentNav/tests/reports/gpt-codex-txt-report.md`
- `/Users/sangyi/workspace/projects/AgentNav/tests/reports/gemini-cli-txt-report.md`
