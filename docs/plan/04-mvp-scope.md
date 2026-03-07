# MVP Scope (v0.1)

## 5.1 목표

- 개인 도메인(`agentnav.baekenough.com`)에 정적 agents 파일 + 페이지별 안내 + 에이전트 가이드를 호스팅
- Claude Code와 GPT Codex가 각각 **네이티브하게** 이 파일을 읽고 사이트를 활용하는 시나리오 검증
- **4가지 포맷(XML, TXT, MD, JSON)을 동시에 제공**하여 에이전트별 포맷 소화 효율을 비교 측정
- 인증/세션/토큰 관리는 스코프 밖 (정적 파일만)

## 5.2 확정된 결정 사항

### Decision 1: 멀티 포맷 실험

PoC는 아래 4가지 파일 포맷을 동시에 운영하여 에이전트가 가장 효율적으로 소화하는 포맷을 측정한다.

| 포맷 | 파일명 | 특징 |
|------|--------|------|
| XML | agents.xml | 구조적, 스키마 검증 가능, 장황함 |
| TXT | agents.txt | 단순, 최소 토큰, 파싱 자유도 높음 |
| MD | agents.md | 사람 친화적, 계층 구조 표현 용이 |
| JSON | agents.json | 기계 파싱 최적, 엄격한 구조 |

측정 지표:
- 토큰 소비량 (같은 정보를 각 포맷으로 인코딩했을 때의 토큰 수)
- 파싱 정확도 (에이전트가 의도한 액션을 올바르게 추출하는 비율)
- 액션 추출 성공률 (에이전트가 첫 시도에 올바른 엔드포인트를 호출하는 비율)

### Decision 2: 호스팅

- 도메인: `agentnav.baekenough.com`
- 4가지 포맷 모두 동일 도메인에서 서빙
- 각 포맷은 독립 경로로 접근 가능
  - `/.well-known/agents.json`
  - `/.well-known/agents.xml`
  - `/.well-known/agents.txt`
  - `/.well-known/agents.md`

### Decision 3: 타깃 소스

- 대상 문서: `https://platform.claude.com/docs/en/home`
- 범위: "Get Started > Quickstart"부터 "Operate > Model Migration"까지의 모든 유의미한 페이지
- agents 파일들은 이 문서 사이트를 탐색하고 활용하는 방법을 기술
- 실제 다수의 페이지와 다양한 콘텐츠 유형이 포함된 실질적인 테스트 케이스를 제공

## 5.3 검증 시나리오

### 기본 시나리오

| 시나리오 | 기대 결과 |
|----------|-----------|
| 에이전트에게 "이 사이트의 agents.json을 읽어봐" 지시 | 사이트 구조와 가능한 액션을 파악 |
| "이 사이트의 블로그 글 목록을 가져와" 지시 | HTML 파싱 없이 API로 직접 접근 |
| "이 사이트에서 뭘 할 수 있어?" 질문 | agents 파일 기반으로 기능 목록 응답 |

### 포맷 비교 실험 시나리오

| 실험 | 방법 | 측정 지표 |
|------|------|-----------|
| 포맷별 토큰 효율 | 동일 에이전트, 동일 태스크, 포맷만 변경 | 입력 토큰 수, 응답 정확도 |
| 포맷별 액션 추출 | "Claude Docs에서 Quickstart 찾아줘" 지시 | 첫 시도 성공률 (TTFA) |
| 에이전트 타입별 선호 포맷 | Claude Code vs GPT Codex 각각 4포맷 테스트 | 포맷별 성공률 분포 |
| 복잡도별 포맷 적합성 | 단순 조회 vs 다단계 탐색 | 태스크 완료율, 오류율 |

## 5.4 사전 조사 필요 항목

### 1. Claude Code의 외부 리소스 접근 방식

- fetch / curl / MCP 중 어떤 경로로 웹 리소스를 읽는가
- `.well-known` 경로의 파일을 자동으로 탐색하는 기능이 있는가
- 자연어 가이드(.md) vs 구조화된 데이터(.json) 중 어떤 것을 더 잘 소화하는가

### 2. GPT Codex의 외부 리소스 접근 방식

- 동일한 질문들을 Codex 관점에서 조사
- Codex의 tool calling / function calling 패턴과 agents 포맷의 호환성

### 3. 포맷 효율 테스트 방법론

- 4가지 포맷(XML, TXT, MD, JSON) 중 에이전트 파싱 효율 + 사람 가독성 균형 측정
- 포맷 효율 테스트 기준 정의: 같은 정보를 인코딩했을 때의 토큰 수 비교
- 에이전트 타입별 선호 포맷 발견 프로세스 설계
- `platform.claude.com/docs` 사이트 구조 크롤링 및 대표 페이지 선별 기준

### 4. 타깃 소스 분석

- `platform.claude.com/docs/en/home`의 전체 페이지 목록 및 계층 구조 파악
- "Get Started > Quickstart"부터 "Operate > Model Migration"까지 포함되는 페이지 수
- 콘텐츠 유형 분류 (개념 설명, API 레퍼런스, 튜토리얼, 예제 등)
