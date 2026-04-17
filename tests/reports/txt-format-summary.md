# TXT Format Verification Summary

**Verification Date**: 2026-04-17
**Framework**: tests/nav-agent-test.py
**Format**: agents.txt (all sources)
**Max Queries per Source**: 40

## Results Matrix

| Source | Pages | Sections | Queries Run | Score | Grade | Duration |
|--------|-------|----------|-------------|-------|-------|----------|
| claude-code | 111 | 1 (parsed) | 10 | 9.7/10 (96.7%) | A | 16.8s |
| claude-api | 1,035 | 1 (parsed) | 10 | 8.0/10 (80.1%) | B | 24.9s |
| gpt-codex | 71 | 40 | 40 | 40.0/40 (100.0%) | A | 17.2s |
| gemini-cli | 90 | 14 | 33 | 31.2/33 (94.5%) | A | 18.8s |

> **Note on query count**: claude-code and claude-api have only 1 parsed section (all pages under a single root), limiting the diversity of auto-generated queries to 10. gpt-codex/gemini-cli with many sections reach the full 40-query budget.

## Category Performance (averaged across sources)

| Category | claude-code | claude-api | gpt-codex | gemini-cli | Avg |
|----------|------------|------------|-----------|------------|-----|
| A: Structure | 100% | 100% | 100% | 100% | **100%** |
| B: Direct Lookup | 100% | 34% | 100% | 85% | **80%** |
| C: Section Enumeration | 84% | 66% | 100% | 100% | **88%** |
| D: Full URL Construction | 100% | 100% | 100% | 100% | **100%** |
| E: Page Type | 100% | 100% | 100% | 100% | **100%** |

## Key Findings

- **Structure (A) and Full URL (D) and Page Type (E) 카테고리**: 4개 소스 모두 100% 달성 — TXT 포맷이 메타데이터, URL 구성, 페이지 타입 분류를 완벽하게 전달
- **claude-api Direct Lookup 저조 (34%)**: agents.txt가 59,872 chars(최대 파일)로 LLM 컨텍스트 내 경로 추적이 어려움; 특히 `.md` 확장자 포함 여부 불일치로 partial credit만 획득
- **gemini-cli Direct Lookup 부분 실패 (85%)**: `/docs/` 최상위 경로와 `/docs/cli/cli-reference/` vs `/docs/reference/commands/` 경로명 불일치 — agents.json 내 경로와 실제 TXT 표현 간 gap
- **Section Enumeration (C) 전반적 양호**: 평균 88%; claude-api의 대용량 TXT에서 슬러그 목록 추출 시 일부 오답 발생
- **쿼리 다양성 제한**: agents.json의 sections 구조가 1개인 소스(claude-code, claude-api)는 자동 생성 쿼리가 10개로 제한되어 통계적 신뢰도가 낮음

## Failed Query Patterns

### 주요 실패 패턴 요약

| 패턴 | 발생 소스 | 원인 |
|------|----------|------|
| `.md` 확장자 포함 경로 반환 | claude-api (B2) | TXT 포맷이 `.md` suffix 포함, grader는 strip된 경로 기대 |
| 경로 prefix 누락 | claude-api (B1, B2) | LLM이 `/docs/en/` prefix 생략, partial match로 0.25~0.43점 |
| 슬러그 목록 불일치 | claude-code (C2), claude-api (C2) | LLM이 샘플 슬러그 대신 예시 파일명 제시 |
| 최상위 경로 인식 실패 | gemini-cli (B1) | `/docs/` 경로가 너무 짧아 특정 LLM이 `/`로 단축 반환 |
| 경로명 변형 | gemini-cli (B8) | `cli-reference` vs `commands` — TXT 내 경로와 JSON ground truth 불일치 가능성 |

## Structural Issue: Single-Section Sources

agents.json에서 sections가 1개로 파싱된 소스(claude-code, claude-api)는 쿼리 생성 다양성이 크게 제한됩니다:

- claude-code: 실제 10개 섹션이지만 TXT→JSON 파싱 시 1개 섹션으로 집계됨
- claude-api: 실제 20개 섹션이지만 동일 현상

결과적으로 두 소스의 max-queries 40 설정에도 불구하고 실제 10개만 실행되어, Grade 신뢰도가 gpt-codex/gemini-cli 대비 낮음.

## Conclusion

### 전체 판정

| 메트릭 | 값 |
|--------|-----|
| Grade A 달성 소스 | **3/4** (claude-code, gpt-codex, gemini-cli) |
| Grade B 달성 소스 | 1/4 (claude-api) |
| 전체 평균 점수 | **~93%** (weighted by query count: 89.8/93) |
| 최고 성능 | gpt-codex — 40/40 (100%) 완벽 |
| 최저 성능 | claude-api — 8.0/10 (80.1%) |

### TXT 포맷 판정

TXT 포맷은 전반적으로 **충분히 우수**하다고 판정합니다:

- **강점**: 구조적 메타데이터(총 페이지, 섹션 수), 전체 URL 구성, 페이지 타입 분류에서 100% 달성
- **약점**: 대용량 파일(claude-api, 60KB)에서 특정 경로 직접 검색 시 LLM 정확도 저하
- **MD 포맷 대비**: 이전 MD 검증에서 모든 소스 Grade A(100%) 대비, TXT는 3/4 Grade A — MD가 여전히 우위이나 TXT도 실용적 수준

**권장**: 소형 문서 세트(~100p)에는 TXT 충분, 대형 문서 세트(1000p+)는 MD 우선 권장.

## Individual Reports

- `/Users/sangyi/workspace/projects/AgentNav/tests/reports/claude-code-txt-report.md`
- `/Users/sangyi/workspace/projects/AgentNav/tests/reports/claude-api-txt-report.md`
- `/Users/sangyi/workspace/projects/AgentNav/tests/reports/gpt-codex-txt-report.md`
- `/Users/sangyi/workspace/projects/AgentNav/tests/reports/gemini-cli-txt-report.md`
