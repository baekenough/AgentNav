# AgentNav

**agents.txt 표준의 오픈소스 레퍼런스 구현**

[![Spec](https://img.shields.io/badge/Spec-v0.2-blue)](docs/spec/agents-txt-v0.2.md)
[![Formats](https://img.shields.io/badge/Formats-TXT%20%7C%20MD%20%7C%20JSON%20%7C%20XML-green)](https://agentnav.baekenough.com)
[![NAV--AGENT Grade](https://img.shields.io/badge/NAV--AGENT-Grade%20A%20(95%25%2B)-brightgreen)](NAV-AGENT.md)
[![Cross-LLM](https://img.shields.io/badge/Cross--LLM%20Test-97.7%2F100-brightgreen)](tests/navigator-codex-report.md)
[![License](https://img.shields.io/badge/License-MIT-lightgrey)](LICENSE)

라이브 데모: **https://agentnav.baekenough.com**

---

## 목차

- [agents.txt란?](#agentsxt란)
- [왜 agents.txt인가?](#왜-agentsxt인가)
- [포맷 비교](#포맷-비교)
- [제공 중인 문서 셋](#제공-중인-문서-셋)
- [아키텍처](#아키텍처)
- [에이전트 스펙](#에이전트-스펙)
- [테스트 결과](#테스트-결과)
- [빠른 시작](#빠른-시작)
- [문서 추가 방법](#문서-추가-방법)
- [프로젝트 구조](#프로젝트-구조)
- [기여](#기여)
- [라이선스](#라이선스)

---

## agents.txt란?

agents.txt는 LLM 및 AI 에이전트 소비에 최적화된 **머신 리더블 문서 사이트맵 포맷**입니다.

**핵심 개념**: AI 에이전트가 실제 페이지를 하나씩 fetch하지 않고도 문서 사이트의 전체 구조를 발견하고 탐색할 수 있게 합니다.

```
"프롬프트 캐싱 문서가 어디 있지?"
  → 페이지 하나 fetch로 전체 사이트 구조 파악
  → 즉시 올바른 페이지 경로 반환
```

**비유**:
- `robots.txt` — 웹 크롤러가 사이트 크롤링 규칙을 파악
- `sitemap.xml` — 검색 엔진이 페이지 목록을 인덱싱
- `agents.txt` — AI 에이전트가 문서 구조를 이해하고 탐색

robots.txt와 sitemap.xml에서 영감을 받았지만, AI 에이전트를 위해 설계되었습니다. LLM 토큰 효율과 시맨틱 네비게이션에 최적화되어 있습니다.

스펙 버전: **v0.2** (초안) — 상세 사항은 [docs/spec/agents-txt-v0.2.md](docs/spec/agents-txt-v0.2.md) 참조

---

## 왜 agents.txt인가?

### 기존 방식의 문제

AI 에이전트가 문서 사이트를 탐색할 때, 두 가지 극단적인 선택지가 있습니다:

1. **모든 페이지를 fetch**: 651개 페이지 × 수천 토큰 = 수백만 토큰 소비
2. **사이트맵(XML)을 파싱**: URL 목록만 있고, 페이지 설명/유형/관계 정보 없음

### agents.txt의 해결책

단일 fetch로 다음을 제공합니다:

- 전체 사이트 구조 (섹션, 페이지 수, URL 패턴)
- 각 페이지의 제목, 설명, 콘텐츠 유형
- SDK 패턴 압축 (10개 SDK × 45개 엔드포인트 = 450 페이지를 템플릿 하나로 표현)
- 네비게이션 힌트 (어떤 쿼리 → 어떤 섹션)

### SDK 패턴 압축 (핵심 기능)

여러 SDK가 같은 엔드포인트 구조를 공유하는 사이트에서 agents.txt는 모든 페이지를 나열하는 대신 템플릿 패턴을 사용합니다.

예시: Claude 문서의 API 참조 섹션 (10개 SDK × 45개 엔드포인트)

```
# 기존 방식: 450개 항목 나열
/api/python/messages/create
/api/python/messages/batches/create
...
/api/typescript/messages/create
/api/typescript/messages/batches/create
...
(450줄 계속)

# agents.txt 방식: 템플릿 + 목록
TEMPLATE: /api/{sdk}/{endpoint}
SDKS: python, typescript, java, go, csharp, ruby, php, kotlin, terraform, cli
PAGES_PER_SDK: messages/create, messages/batches/create, ...
```

토큰 비용 절감: **약 90%**

---

## 포맷 비교

4가지 포맷이 지원됩니다. 같은 데이터를 다른 직렬화 방식으로 제공합니다.

| 포맷 | 토큰 (651 페이지) | MIME 타입 | 머신 파싱 | 사람 가독성 | 권장 용도 |
|------|-------------------|-----------|----------|-----------|----------|
| TXT | ~3,200 | `text/plain` | 양호 | 양호 | 토큰 제한 에이전트 |
| MD | ~5,400 | `text/markdown` | 양호 | 최고 | LLM 자연어 처리 |
| JSON | ~9,600 | `application/json` | 최고 | 보통 | 프로그래매틱 API 통합 |
| XML | ~7,000 | `application/xml` | 최고 | 보통 | 엔터프라이즈 XML 도구 |

토큰 수는 Claude 문서(651 페이지) 기준 근사값(4자/토큰 추정)입니다. 실제 값은 사이트 크기와 패턴 압축 사용 여부에 따라 다릅니다.

### 포맷 선택 가이드

- **토큰 예산이 제한적**: TXT (최소 토큰)
- **LLM 자연어 처리**: MD (자연스러운 구조, 균형 잡힌 토큰 비용)
- **프로그래매틱 파싱**: JSON (최고의 구조화, 스키마 검증 가능)
- **엔터프라이즈 XML 도구**: XML (XPath/DOM 파싱)

---

## 제공 중인 문서 셋

| 프로바이더 | 페이지 | 섹션 | 경로 |
|-----------|-------|------|------|
| Claude Code (Anthropic) | 651 | 9 | `/claude-code/` |
| GPT Codex (OpenAI) | 69 | 14 | `/gpt-codex/` |

### 엔드포인트

```
# Claude Code 문서
https://agentnav.baekenough.com/claude-code/.well-known/agents.txt
https://agentnav.baekenough.com/claude-code/.well-known/agents.md
https://agentnav.baekenough.com/claude-code/.well-known/agents.json
https://agentnav.baekenough.com/claude-code/.well-known/agents.xml

# GPT Codex 문서
https://agentnav.baekenough.com/gpt-codex/.well-known/agents.txt
https://agentnav.baekenough.com/gpt-codex/.well-known/agents.md
https://agentnav.baekenough.com/gpt-codex/.well-known/agents.json
https://agentnav.baekenough.com/gpt-codex/.well-known/agents.xml

# 기본 (Claude Code primary, RFC 8615)
https://agentnav.baekenough.com/.well-known/agents.json
```

---

## 아키텍처

AgentNav는 백엔드가 없는 순수 정적 파일 서버입니다.

```
[Client / AI Agent]
        |
        | HTTPS
        v
[Cloudflare Tunnel]
        |
        v
[Docker Container]
  nginx:alpine
  - /usr/share/nginx/html/ (정적 파일)
  - .well-known URL 리다이렉트 처리
```

**구성 요소:**
- **nginx:alpine** — 정적 파일 서빙, `.well-known` URL 라우팅
- **Cloudflare Tunnel** — HTTPS 종단, 도메인 연결
- **Docker** — 컨테이너 격리 및 배포

**Dockerfile:**

```dockerfile
FROM nginx:alpine
COPY nginx.conf /etc/nginx/conf.d/default.conf
COPY public/ /usr/share/nginx/html/
EXPOSE 80
```

---

## 에이전트 스펙

AgentNav는 두 가지 에이전트 명세를 포함합니다.

### NAVIGATOR.md — 소비자 에이전트

어떤 LLM이든 이 스펙을 구현하여 agents.txt를 파싱하고 네비게이션 쿼리에 답할 수 있습니다.

**워크플로우:**

```
Step 1: Discovery
  /.well-known/agents.json → /.well-known/agents.md → /.well-known/agents.xml → /.well-known/agents.txt
  (HTTP 200 첫 번째 응답에서 멈춤)

Step 2: Parse
  포맷별 파싱 전략 적용
  (JSON: 객체 구조 / MD: 헤더+링크 / XML: DOM / TXT: 키-값 + 섹션 블록)

Step 3: Build Site Map
  내부 사이트맵 구축 (섹션별 페이지 목록, SDK 패턴 확장)

Step 4: Answer Queries
  사용자 쿼리 → 가장 관련 있는 페이지 경로 반환
```

**특징:**
- 포맷 무관: 4가지 포맷 모두 처리
- LLM 무관: Claude, GPT, Gemini 등 모두 지원
- 외부 의존성 없음: HTTP fetch 하나로 동작

상세 스펙: [NAVIGATOR.md](NAVIGATOR.md)

---

### NAV-AGENT.md — 검증 에이전트

각 포맷이 문서 구조를 얼마나 효과적으로 전달하는지 정량적으로 테스트합니다.

**5가지 가중 메트릭:**

| 메트릭 | 가중치 | 설명 |
|--------|--------|------|
| Section Discovery (섹션 발견율) | 20% | 9개 최상위 섹션 중 몇 개를 식별할 수 있는가 |
| Page Coverage (페이지 커버리지) | 25% | 651개 페이지 중 몇 개의 존재를 파악할 수 있는가 |
| Navigation Accuracy (네비게이션 정확도) | 30% | 사용자 질문에 대해 올바른 페이지로 안내할 수 있는가 |
| Pattern Recognition (패턴 인식) | 15% | SDK별 반복 패턴을 인식하고 활용할 수 있는가 |
| Content Classification (콘텐츠 분류) | 10% | 페이지 유형을 올바르게 분류할 수 있는가 |

**등급:**

| 등급 | 점수 | 의미 |
|------|------|------|
| A | 90%+ | 포맷이 사이트 구조를 효과적으로 전달함 |
| B | 70-89% | 대부분 효과적, 일부 격차 있음 |
| C | 50-69% | 부분적으로 효과적, 주요 격차 있음 |
| F | 50% 미만 | 포맷이 구조 전달에 실패함 |

상세 스펙: [NAV-AGENT.md](NAV-AGENT.md)

---

### 콘텐츠 유형 분류 체계 (12가지 타입)

| 타입 | 설명 | 예시 |
|------|------|------|
| `tutorial` | 시작 가이드, 빠른 시작 | quickstart, get-started |
| `reference` | 정적 참조 정보 | glossary, pricing, deprecations |
| `guide` | 기능별 사용 가이드 | prompt-caching, vision, streaming |
| `overview` | 섹션 진입점/개요 페이지 | models/overview, features overview |
| `use-case` | 유스케이스별 가이드 | content-moderation, ticket-routing |
| `tool-reference` | 도구 사용 문서 | bash-tool, web-search-tool |
| `sdk-guide` | SDK별 가이드 (Agent SDK) | python, typescript |
| `api-reference` | API 인프라 문서 | rate-limits, errors, versioning |
| `api-endpoint` | 개별 API 엔드포인트 | messages/create, models/list |
| `api-hub` | API 섹션 허브/랜딩 | messages, admin, beta |
| `best-practices` | 모범 사례/평가 문서 | reduce-hallucinations, reduce-latency |
| `changelog` | 변경 로그 | release-notes/system-prompts |

---

## 테스트 결과

### NAV-AGENT 검증 (Claude)

4개 포맷 모두 **Grade A (95%+)** 달성. v0.2 taxonomy 정규화 후 Content Classification 100%.

### 크로스-LLM 검증 (GPT Codex CLI)

NAVIGATOR.md 스펙이 다른 LLM 환경에서도 동작하는지 검증한 독립 테스트.

- 테스트 도구: Codex CLI (OpenAI GPT)
- 규모: 10개 카테고리, 100개 쿼리
- 결과: **97.7/100 (Grade A)**

| 카테고리 | 점수 |
|---------|------|
| A — 구조 발견 | 10/10 (100%) |
| B — 직접 페이지 조회 | 10/10 (100%) |
| C — API 네비게이션 | 10/10 (100%) |
| D — SDK 엔드포인트 조회 | 10/10 (100%) |
| E — 자연어 네비게이션 | 10/10 (100%) |
| F — 섹션 열거 | 9.7/10 (97%) |
| G — 타입 분류 | 10/10 (100%) |
| H — URL 구성 | 10/10 (100%) |
| I — 크로스-섹션 | 9/10 (90%) |
| J — 엣지 케이스 | 9/10 (90%) |

7/10 카테고리 100% 달성. 상세 결과: [tests/navigator-codex-report.md](tests/navigator-codex-report.md)

---

## 빠른 시작

### AI 에이전트용 — agents.txt 가져오기

```bash
# 원하는 포맷으로 문서 인덱스 가져오기
curl https://agentnav.baekenough.com/claude-code/.well-known/agents.txt
curl https://agentnav.baekenough.com/claude-code/.well-known/agents.json
curl https://agentnav.baekenough.com/claude-code/.well-known/agents.md
curl https://agentnav.baekenough.com/claude-code/.well-known/agents.xml
```

응답 하나로 651개 페이지의 전체 구조를 파악할 수 있습니다.

### NAVIGATOR 에이전트 사용

NAVIGATOR.md 스펙을 구현한 에이전트를 사용해 대화형으로 탐색합니다:

```
User: "Analyze the agents.txt at agentnav.baekenough.com/claude-code"

Navigator:
  Site: Claude Code Documentation
  URL: https://platform.claude.com/docs
  Total Pages: 651 across 9 sections

  Sections:
    1. Introduction (2 pages)
    2. About Claude (12 pages)
    3. Build with Claude (35 pages)
    4. Agents & Tools (18 pages)
    5. Agent SDK (27 pages)
    6. API Reference (546 pages — 10 SDKs x 45 endpoints + 96 core)
    7. Test & Evaluate (8 pages)
    8. Release Notes (2 pages)
    9. Resources (1 page)

User: "Where is the page about prompt caching?"

Navigator:
  Found in "Build with Claude" section:
  → https://platform.claude.com/docs/en/build-with-claude/prompt-caching
```

### 사이트 운영자용 — agents.txt 추가하기

자신의 문서 사이트에 agents.txt를 추가하는 방법:

1. 4가지 포맷 중 하나 이상으로 문서 인덱스 생성 (v0.2 스펙 준수)
2. `/.well-known/agents.{format}` 엔드포인트에서 서빙 (RFC 8615)
3. 페이지 분류에 12가지 콘텐츠 유형 taxonomy 사용
4. 멀티 SDK 문서의 경우 SDK Pattern Compression 활용 (토큰 90% 절감)

스펙 상세: [docs/spec/agents-txt-v0.2.md](docs/spec/agents-txt-v0.2.md)

### 셀프 호스팅

```bash
git clone <repo>
cd AgentNav
docker build -t agentnav .
docker run -p 8080:80 agentnav
# http://localhost:8080 접속
```

---

## 문서 추가 방법

새 문서 프로바이더를 AgentNav에 추가하는 절차입니다.

1. `public/` 아래 새 디렉토리 생성

```bash
mkdir public/your-docs
```

2. v0.2 스펙에 따라 4가지 포맷 파일 생성

```
public/your-docs/
├── agents.json   # JSON 포맷
├── agents.md     # Markdown 포맷
├── agents.xml    # XML 포맷
└── agents.txt    # Plain text 포맷
```

3. 포맷 선택 페이지 생성

```bash
cp public/claude-code/index.html public/your-docs/index.html
# index.html 내 참조 수정
```

4. `public/index.html`에 카드 추가

5. 빌드 및 배포

```bash
docker build -t agentnav .
docker run -p 8080:80 agentnav
```

6. NAV-AGENT로 검증 (Grade B 이상 권장)

---

## 프로젝트 구조

```
AgentNav/
├── README.md                       # 영문 README
├── README_ko.md                    # 한국어 README (이 파일)
├── Dockerfile                      # nginx:alpine 컨테이너 정의
├── nginx.conf                      # .well-known URL 리다이렉트 설정
├── NAVIGATOR.md                    # 소비자 에이전트 스펙 (파싱 & 네비게이션)
├── NAV-AGENT.md                    # 검증 에이전트 스펙 (테스트 & 등급)
├── public/
│   ├── index.html                  # 랜딩 페이지 (프로바이더 목록)
│   ├── claude-code/
│   │   ├── index.html              # 포맷 선택 페이지
│   │   ├── agents.json             # JSON 포맷 (~9,600 토큰)
│   │   ├── agents.md               # Markdown 포맷 (~5,400 토큰)
│   │   ├── agents.xml              # XML 포맷 (~7,000 토큰)
│   │   └── agents.txt              # Plain text 포맷 (~3,200 토큰)
│   └── gpt-codex/
│       ├── index.html
│       ├── agents.json
│       ├── agents.md
│       ├── agents.xml
│       └── agents.txt
├── docs/
│   └── spec/
│       └── agents-txt-v0.2.md      # 공식 스펙 문서
└── tests/
    ├── navigator-codex-test.py     # 크로스-LLM 검증 스크립트 (100개 쿼리)
    └── navigator-codex-report.md   # Codex CLI 테스트 결과 (97.7/100)
```

---

## 기여

### 스펙 준수

- `docs/spec/agents-txt-v0.2.md`의 v0.2 스펙을 따릅니다
- 콘텐츠 유형 분류에 12가지 taxonomy를 사용합니다
- 새 타입 추가 시 스펙 문서도 함께 업데이트합니다

### 검증

새 agents.txt 파일을 추가하거나 기존 파일을 수정한 경우:

1. NAV-AGENT로 포맷 효과성 검증 (Grade B 이상 권장)

```
"NAV-AGENT로 /your-docs/의 agents.md 포맷을 검증해줘"
```

2. NAVIGATOR로 파싱 가능성 테스트

```
"NAVIGATOR로 http://localhost:8080/your-docs/를 파싱해줘"
```

### Pull Request

- 새 문서 셋 추가: `public/{vendor}-{product}/` 디렉토리 구조 준수
- 스펙 변경: `docs/spec/` 업데이트 + 예시 파일 동기화
- 버그 수정: 관련 NAV-AGENT 테스트 케이스 포함

---

## 라이선스

MIT

---

## 링크

| 리소스 | URL |
|--------|-----|
| 라이브 데모 | https://agentnav.baekenough.com |
| 공식 스펙 | [docs/spec/agents-txt-v0.2.md](docs/spec/agents-txt-v0.2.md) |
| 검증 에이전트 | [NAV-AGENT.md](NAV-AGENT.md) |
| 소비자 에이전트 | [NAVIGATOR.md](NAVIGATOR.md) |
| 크로스-LLM 테스트 | [tests/navigator-codex-report.md](tests/navigator-codex-report.md) |
