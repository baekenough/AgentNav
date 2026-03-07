# AgentNav

**AI 에이전트를 위한 웹 표준 — `agents.txt`**

[![Spec](https://img.shields.io/badge/Spec-v0.2-blue)](docs/spec/agents-txt-v0.2.md)
[![Formats](https://img.shields.io/badge/Formats-TXT%20%7C%20MD%20%7C%20JSON%20%7C%20XML-green)](https://agentnav.baekenough.com)
[![NAV--AGENT Grade](https://img.shields.io/badge/NAV--AGENT-Grade%20A%20(95%25%2B)-brightgreen)](NAV-AGENT.md)
[![Cross-LLM](https://img.shields.io/badge/Cross--LLM%20Test-97.7%2F100-brightgreen)](tests/navigator-codex-report.md)
[![License](https://img.shields.io/badge/License-MIT-lightgrey)](LICENSE)

레퍼런스 구현: **https://agentnav.baekenough.com**

---

## 목차

- [문제: AI 에이전트의 문서 탐색](#문제-ai-에이전트의-문서-탐색)
- [해결책: agents.txt](#해결책-agentsxt)
- [작동 방식](#작동-방식)
- [사이트 운영자 가이드: 내 사이트에 agents.txt 추가하기](#사이트-운영자-가이드-내-사이트에-agentsxt-추가하기)
- [스펙 개요 (v0.2)](#스펙-개요-v02)
- [레퍼런스 구현](#레퍼런스-구현)
- [검증 및 테스트 결과](#검증-및-테스트-결과)
- [프로젝트 구조](#프로젝트-구조)
- [기여](#기여)
- [라이선스](#라이선스)

---

## 문제: AI 에이전트의 문서 탐색

Vercel이 발견한 사실이 있습니다. AI 에이전트가 Playwright MCP로 웹을 탐색하면 **버튼 클릭 하나에 12,891자의 컨텍스트가 소비**됩니다. agent-browser로 전환하자 **93% 토큰 절감**이 가능했습니다. 이유는 단순합니다. 인간용 인터페이스를 AI에게 강제하는 대신, AI 전용 인터페이스를 제공했기 때문입니다.

문서 탐색도 같은 문제입니다.

AI 에이전트가 문서 사이트를 탐색할 때, 선택지는 두 가지뿐입니다:

| 방식 | 비용 | 문제 |
|------|------|------|
| 모든 페이지를 직접 fetch | 651페이지 × 수천 토큰 = **수백만 토큰** | 현실적으로 불가능 |
| sitemap.xml 파싱 | 적음 | URL 목록만 있고, 설명/유형/관계 정보 없음 |

인간을 위해 설계된 HTML 문서를 AI에게 강제하는 것은 근본적으로 잘못된 접근입니다.

---

## 해결책: agents.txt

새로운 웹 표준을 제안합니다 — `agents.txt`.

각 사이트가 `/.well-known/agents.txt`에서 이 파일을 서빙하는 것이 목표입니다. 마치 크롤러를 위한 `robots.txt`, 검색 엔진을 위한 `sitemap.xml`처럼.

```
robots.txt   — 웹 크롤러에게 사이트 크롤링 규칙을 알려줌
sitemap.xml  — 검색 엔진에게 페이지 목록을 알려줌
agents.txt   — AI 에이전트에게 문서 구조를 알려줌
```

agents.txt는 **단일 fetch**로 다음을 전달합니다:

- 전체 사이트 구조 (섹션, 페이지 수, URL 패턴)
- 각 페이지의 제목, 설명, 콘텐츠 유형
- SDK 패턴 압축 (10개 SDK × 45개 엔드포인트 = 450페이지를 템플릿 하나로 표현)
- 네비게이션 힌트 (어떤 쿼리가 어떤 섹션으로 가야 하는지)

결과: Claude 문서 651페이지 전체를 **~3,200 토큰**으로 파악.

---

## 작동 방식

### AI 에이전트 입장에서

```
# 기존 방식 (HTML 크롤링)
에이전트 → 651개 페이지 순차 fetch → 수백만 토큰 소비 → 느리고 비쌈

# agents.txt 방식
에이전트 → /.well-known/agents.txt 단일 fetch → ~3,200 토큰 →
  전체 사이트 구조 파악 → 올바른 페이지 즉시 반환
```

### 포맷 비교

4가지 포맷이 지원됩니다. 모두 동일한 정보를 다른 직렬화 방식으로 제공합니다.

| 포맷 | 토큰 (651페이지) | MIME 타입 | 권장 용도 |
|------|-----------------|-----------|----------|
| TXT | ~3,200 | `text/plain` | 토큰 예산이 제한적인 에이전트 |
| MD | ~5,400 | `text/markdown` | LLM 자연어 처리, 균형 잡힌 선택 |
| JSON | ~9,600 | `application/json` | 프로그래매틱 파싱, API 통합 |
| XML | ~7,000 | `application/xml` | 엔터프라이즈 XML 도구 |

토큰 수는 Claude 문서 기준 근사값(4자/토큰 추정)입니다.

### SDK 패턴 압축

여러 SDK가 같은 엔드포인트 구조를 공유하는 사이트에서 핵심 기능입니다.

```
# 기존 방식: 450개 항목 나열 (토큰 낭비)
/api/python/messages/create
/api/python/messages/batches/create
...
/api/typescript/messages/create
/api/typescript/messages/batches/create
...(450줄 계속)

# agents.txt 방식: 템플릿 + 목록 (토큰 90% 절감)
TEMPLATE: /api/{sdk}/{endpoint}
SDKS: python, typescript, java, go, csharp, ruby, php, kotlin, terraform, cli
PAGES_PER_SDK: messages/create, messages/batches/create, ...
```

---

## 사이트 운영자 가이드: 내 사이트에 agents.txt 추가하기

> **이 섹션이 핵심입니다.** agents.txt의 가치는 각 사이트가 직접 제공할 때 실현됩니다.

### 1단계: 스펙 확인

[docs/spec/agents-txt-v0.2.md](docs/spec/agents-txt-v0.2.md)에서 v0.2 스펙을 확인하세요.

### 2단계: agents.txt 파일 작성

최소한 TXT 포맷 하나로 시작하세요. 아래 구조를 따릅니다:

**TXT 포맷 예시 (최소 구조):**

```
SITE: My Documentation
URL: https://docs.example.com
TOTAL_PAGES: 120
GENERATED: 2026-03-07

SECTION: Getting Started
PAGES: 8
  quickstart | Quick Start Guide | tutorial | /docs/quickstart
  installation | Installation | tutorial | /docs/installation

SECTION: API Reference
PAGES: 50
  messages-create | Create Message | api-endpoint | /api/messages/create
  ...
```

**12가지 콘텐츠 유형 taxonomy:**

| 타입 | 설명 |
|------|------|
| `tutorial` | 시작 가이드, 빠른 시작 |
| `reference` | 정적 참조 정보 (용어집, 가격 등) |
| `guide` | 기능별 사용 가이드 |
| `overview` | 섹션 진입점/개요 페이지 |
| `use-case` | 유스케이스별 가이드 |
| `tool-reference` | 도구 사용 문서 |
| `sdk-guide` | SDK별 가이드 |
| `api-reference` | API 인프라 문서 |
| `api-endpoint` | 개별 API 엔드포인트 |
| `api-hub` | API 섹션 허브/랜딩 |
| `best-practices` | 모범 사례/평가 문서 |
| `changelog` | 변경 로그 |

### 3단계: Well-Known URL에서 서빙

RFC 8615 규약에 따라 `/.well-known/` 경로에서 서빙합니다:

```
https://docs.example.com/.well-known/agents.txt   # 필수 (기본)
https://docs.example.com/.well-known/agents.md    # 선택
https://docs.example.com/.well-known/agents.json  # 선택
https://docs.example.com/.well-known/agents.xml   # 선택
```

nginx 설정 예시:

```nginx
location /.well-known/agents.txt {
    alias /srv/agents/agents.txt;
    add_header Content-Type text/plain;
    add_header Access-Control-Allow-Origin *;
}
```

### 4단계: 검증

NAV-AGENT로 파일이 올바르게 동작하는지 검증합니다 (Grade B 이상 권장):

```
"NAV-AGENT로 https://docs.example.com/.well-known/agents.txt를 검증해줘"
```

상세 검증 기준은 [NAV-AGENT.md](NAV-AGENT.md)를 참조하세요.

---

## 스펙 개요 (v0.2)

공식 스펙: [docs/spec/agents-txt-v0.2.md](docs/spec/agents-txt-v0.2.md)

### 핵심 설계 원칙

| 원칙 | 설명 |
|------|------|
| 토큰 효율 | 최소 토큰으로 최대 구조 정보 전달 |
| 머신 파싱 가능 | 프로그래매틱 추출에 충분한 구조 |
| 사람 가독성 | 도구 없이도 개발자가 이해 가능 |
| 네비게이션 유틸리티 | 어떤 쿼리도 실제 fetch 없이 올바른 페이지로 안내 |
| 패턴 압축 | 반복 구조(SDK별 API 참조 등)를 열거하지 않고 표현 |

### Well-Known URL 규약 (RFC 8615)

```
https://{domain}/.well-known/agents.txt     # Plain text (기본 권장)
https://{domain}/.well-known/agents.md      # Markdown
https://{domain}/.well-known/agents.json    # JSON
https://{domain}/.well-known/agents.xml     # XML
```

멀티 프로바이더 호스팅 시:

```
https://{domain}/.well-known/agents.json              # 기본 (첫 번째 프로바이더)
https://{domain}/{vendor}-{product}/.well-known/agents.json  # 프로바이더별
```

### 버전 이력

| 버전 | 상태 | 비고 |
|------|------|------|
| v0.1 | 비공식 | 초기 개념 증명, 스키마 미공개 |
| v0.2 | 현재 (초안) | 타입 taxonomy, URL 규약, 스키마, 멀티 프로바이더 지원 공식화 |

---

## 레퍼런스 구현

AgentNav는 agents.txt 스펙의 레퍼런스 구현입니다. 실제 문서 사이트들의 agents.txt를 예시로 제공합니다.

라이브 주소: **https://agentnav.baekenough.com**

### 제공 중인 예시

| 사이트 | 페이지 | 섹션 | 경로 |
|--------|-------|------|------|
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

# 기본 엔드포인트 (RFC 8615)
https://agentnav.baekenough.com/.well-known/agents.json
```

### 아키텍처

AgentNav 레퍼런스 구현은 백엔드가 없는 순수 정적 파일 서버입니다.

```
[AI Agent / Client]
      |
      | HTTPS
      v
[Cloudflare Tunnel]
      |
      v
[Docker Container]
  nginx:alpine
  - /usr/share/nginx/html/ (정적 파일)
  - .well-known URL 라우팅
```

### 셀프 호스팅

자신의 서버에서 레퍼런스 구현을 실행할 수 있습니다:

```bash
git clone <repo>
cd AgentNav
docker build -t agentnav .
docker run -p 8080:80 agentnav
# http://localhost:8080 접속
```

새 문서 셋을 추가하려면:

```bash
# 1. 디렉토리 생성
mkdir public/your-docs

# 2. v0.2 스펙에 따라 파일 생성
public/your-docs/
├── agents.json
├── agents.md
├── agents.xml
└── agents.txt

# 3. 포맷 선택 페이지 추가
cp public/claude-code/index.html public/your-docs/index.html
# index.html 내 참조 수정

# 4. 빌드 및 배포
docker build -t agentnav .
docker run -p 8080:80 agentnav
```

---

## 검증 및 테스트 결과

### 검증 에이전트

AgentNav는 두 가지 에이전트 명세를 포함합니다.

**NAVIGATOR.md** — 소비자 에이전트 스펙. 어떤 LLM이든 이 스펙을 구현하여 agents.txt를 파싱하고 네비게이션 쿼리에 답할 수 있습니다.

```
Step 1: Discovery   /.well-known/agents.json → agents.md → agents.xml → agents.txt
Step 2: Parse       포맷별 파싱 전략 적용
Step 3: Build       내부 사이트맵 구축 (섹션별 페이지 목록, SDK 패턴 확장)
Step 4: Answer      사용자 쿼리 → 올바른 페이지 경로 반환
```

**NAV-AGENT.md** — 검증 에이전트 스펙. 각 포맷이 문서 구조를 얼마나 효과적으로 전달하는지 정량적으로 테스트합니다.

| 메트릭 | 가중치 |
|--------|--------|
| Section Discovery (섹션 발견율) | 20% |
| Page Coverage (페이지 커버리지) | 25% |
| Navigation Accuracy (네비게이션 정확도) | 30% |
| Pattern Recognition (패턴 인식) | 15% |
| Content Classification (콘텐츠 분류) | 10% |

### NAV-AGENT 검증 결과 (Claude)

4개 포맷 모두 **Grade A (95%+)** 달성. v0.2 taxonomy 정규화 후 Content Classification 100%.

| 등급 | 점수 | 의미 |
|------|------|------|
| A | 90%+ | 포맷이 사이트 구조를 효과적으로 전달 |
| B | 70-89% | 대부분 효과적, 일부 격차 있음 |
| C | 50-69% | 부분적으로 효과적, 주요 격차 있음 |
| F | 50% 미만 | 구조 전달 실패 |

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

## 프로젝트 구조

```
AgentNav/
├── README.md                       # 영문 README
├── README_ko.md                    # 한국어 README (이 파일)
├── Dockerfile                      # nginx:alpine 컨테이너 정의
├── nginx.conf                      # .well-known URL 라우팅 설정
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

### 내 사이트의 agents.txt를 레퍼런스 구현에 추가

PR 환영합니다. `public/{vendor}-{product}/` 디렉토리 구조를 따르세요.

### 스펙 기여

- `docs/spec/agents-txt-v0.2.md`의 v0.2 스펙을 따릅니다
- 콘텐츠 유형 taxonomy에 새 타입 추가 시 스펙 문서도 함께 업데이트합니다

### 검증 절차

새 agents.txt 파일을 추가하거나 기존 파일을 수정한 경우:

1. NAV-AGENT로 포맷 효과성 검증 (Grade B 이상 권장)
2. NAVIGATOR로 파싱 가능성 테스트

```
"NAV-AGENT로 /your-docs/의 agents.txt를 검증해줘"
"NAVIGATOR로 http://localhost:8080/your-docs/를 파싱해줘"
```

---

## 라이선스

MIT

---

## 링크

| 리소스 | URL |
|--------|-----|
| 레퍼런스 구현 | https://agentnav.baekenough.com |
| 공식 스펙 v0.2 | [docs/spec/agents-txt-v0.2.md](docs/spec/agents-txt-v0.2.md) |
| 검증 에이전트 | [NAV-AGENT.md](NAV-AGENT.md) |
| 소비자 에이전트 | [NAVIGATOR.md](NAVIGATOR.md) |
| 크로스-LLM 테스트 결과 | [tests/navigator-codex-report.md](tests/navigator-codex-report.md) |
| 영문 README | [README.md](README.md) |
