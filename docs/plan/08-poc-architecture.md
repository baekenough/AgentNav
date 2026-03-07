# PoC Architecture

## 개요

AgentNav PoC는 `agentnav.baekenough.com` 도메인에서 4가지 포맷의 agents 파일을 동시에 서빙하고, 각 포맷이 AI 에이전트에게 얼마나 효율적으로 소화되는지를 측정하는 실험 인프라다.

타깃 소스는 `platform.claude.com/docs`로, "Get Started > Quickstart"부터 "Operate > Model Migration"까지 실제 문서 사이트를 대상으로 한다.

---

## 1. 호스팅 설정

### 도메인

```
agentnav.baekenough.com
```

- 정적 파일 호스팅 (동적 서버 불필요)
- 모든 포맷을 단일 도메인에서 서빙
- HTTPS 필수 (에이전트 도구의 보안 정책 충족)

### 호스팅 방식

정적 사이트 호스팅으로 운영한다. 초기에는 빠른 세팅을 위해 GitHub Pages 또는 Vercel을 고려하되, `.well-known/` 경로 서빙이 지원되는지 확인 후 결정한다.

| 옵션 | 장점 | 단점 |
|------|------|------|
| GitHub Pages | 무료, 간단, 버전 관리 통합 | `.well-known` 경로 지원 확인 필요 |
| Vercel | 빠른 CDN, 쉬운 설정 | 무료 플랜 제한 |
| Cloudflare Pages | 글로벌 CDN, `.well-known` 지원 확실 | 설정 약간 복잡 |

---

## 2. 포맷 매트릭스

4가지 포맷을 동시에 운영하여 에이전트별 소화 효율을 비교 측정한다.

### XML (`agents.xml`)

```xml
<?xml version="1.0" encoding="UTF-8"?>
<agents>
  <site name="Claude Documentation" url="https://platform.claude.com/docs/en/home" />
  <navigation>
    <section name="Get Started">
      <page title="Quickstart" path="/docs/en/home/quickstart" />
    </section>
  </navigation>
  <actions>
    <action id="find-page" description="Find a documentation page by topic" />
  </actions>
</agents>
```

| 항목 | 평가 |
|------|------|
| 구조 명확성 | 높음 (스키마 검증 가능) |
| 토큰 효율 | 낮음 (태그 오버헤드 큼) |
| 사람 가독성 | 중간 |
| 에이전트 친화성 | 중간 (XML 파싱 경험 필요) |

### TXT (`agents.txt`)

```
SITE: Claude Documentation
URL: https://platform.claude.com/docs/en/home

SECTIONS:
- Get Started > Quickstart: /docs/en/home/quickstart
- Get Started > Models: /docs/en/home/models

ACTIONS:
- find-page: Find a documentation page by topic
- list-sections: List all available documentation sections
```

| 항목 | 평가 |
|------|------|
| 구조 명확성 | 낮음 (컨벤션 의존) |
| 토큰 효율 | 높음 (최소 오버헤드) |
| 사람 가독성 | 높음 |
| 에이전트 친화성 | 미지수 (파싱 자유도 높으나 오해 가능성) |

### MD (`agents.md`)

```markdown
# Claude Documentation Agent Guide

**Site**: [Claude Documentation](https://platform.claude.com/docs/en/home)

## Navigation Structure

### Get Started
- [Quickstart](/docs/en/home/quickstart) - Get up and running quickly
- [Models](/docs/en/home/models) - Available Claude models

## Available Actions

| Action | Description |
|--------|-------------|
| `find-page` | Find a documentation page by topic |
| `list-sections` | List all available documentation sections |
```

| 항목 | 평가 |
|------|------|
| 구조 명확성 | 높음 (헤딩 계층 구조) |
| 토큰 효율 | 중간 |
| 사람 가독성 | 매우 높음 |
| 에이전트 친화성 | 높음 (LLM 훈련 데이터와 유사) |

### JSON (`agents.json`)

```json
{
  "site": {
    "name": "Claude Documentation",
    "url": "https://platform.claude.com/docs/en/home"
  },
  "navigation": {
    "sections": [
      {
        "name": "Get Started",
        "pages": [
          { "title": "Quickstart", "path": "/docs/en/home/quickstart" }
        ]
      }
    ]
  },
  "actions": [
    {
      "id": "find-page",
      "description": "Find a documentation page by topic"
    }
  ]
}
```

| 항목 | 평가 |
|------|------|
| 구조 명확성 | 매우 높음 (엄격한 스키마) |
| 토큰 효율 | 중간 (키 이름 오버헤드) |
| 사람 가독성 | 중간 |
| 에이전트 친화성 | 높음 (함수 호출 패턴과 친화적) |

---

## 3. URL 구조

```
agentnav.baekenough.com/
├── .well-known/
│   ├── agents.json          # JSON 포맷 진입점
│   ├── agents.xml           # XML 포맷 진입점
│   ├── agents.txt           # TXT 포맷 진입점
│   └── agents.md            # MD 포맷 진입점
├── agents/
│   ├── json/
│   │   └── pages/
│   │       ├── quickstart.json
│   │       ├── models.json
│   │       └── *.json
│   ├── xml/
│   │   └── pages/
│   │       ├── quickstart.xml
│   │       ├── models.xml
│   │       └── *.xml
│   ├── txt/
│   │   └── pages/
│   │       ├── quickstart.txt
│   │       ├── models.txt
│   │       └── *.txt
│   └── md/
│       └── pages/
│           ├── quickstart.md
│           ├── models.md
│           └── *.md
└── index.html               # 실험 결과 대시보드 (선택)
```

### 경로 설계 원칙

- `.well-known/` 경로는 각 포맷의 **진입점(root manifest)**만 위치시킨다
- 개별 페이지 상세 정보는 `agents/{format}/pages/` 하위에 위치시킨다
- 진입점 파일에는 개별 페이지 파일의 URL 목록이 포함되어 에이전트가 필요한 페이지만 선택적으로 가져올 수 있도록 한다

---

## 4. 타깃 소스: platform.claude.com/docs

### 대상 범위

- 시작: `Get Started > Quickstart`
- 종료: `Operate > Model Migration`
- 포함 섹션 (추정):

```
Get Started
├── Quickstart
├── Models
└── Claude.ai

Build with Claude
├── Define your use case
├── Prompt engineering
│   ├── Overview
│   ├── Prompt templates
│   └── ...
├── Tool use (function calling)
├── Vision
├── Extended thinking
└── ...

Operate
├── Deployment
├── Cost management
├── Rate limits
└── Model Migration
```

### 콘텐츠 유형 분류

| 유형 | 예시 | agents 파일 표현 방식 |
|------|------|----------------------|
| 개념 설명 | Models 페이지 | 요약 + 링크 |
| 튜토리얼 | Quickstart | 단계별 액션 목록 |
| API 레퍼런스 | Tool use | 엔드포인트 + 파라미터 |
| 예제 코드 | Prompt engineering | 코드 스니펫 위치 안내 |

### 크롤링 전략

1. `platform.claude.com/docs/en/home`의 사이드바 네비게이션을 기준으로 페이지 목록 추출
2. 각 페이지의 제목, URL, 섹션 정보를 수집
3. 4가지 포맷으로 동일한 정보를 인코딩하여 파일 생성
4. 콘텐츠 변경 시 재생성이 용이하도록 생성 스크립트 작성

---

## 5. 실험 설계

### 핵심 실험: 포맷별 효율 비교

**동일 에이전트 + 동일 태스크 + 포맷만 변경**으로 순수 포맷 효과를 측정한다.

```
실험 단위:
  에이전트: Claude Code (또는 GPT Codex)
  태스크: "Claude Docs에서 Tool use 섹션의 내용을 요약해줘"
  변수: 제공하는 agents 파일 포맷 (JSON / XML / TXT / MD)
  측정: 입력 토큰 수, 응답 정확도, 첫 시도 성공 여부
```

### 측정 지표

| 지표 | 약자 | 정의 | 측정 방법 |
|------|------|------|-----------|
| 입력 토큰 수 | - | agents 파일을 읽는 데 소비된 토큰 | 포맷별 파일 크기 + 토큰 카운터 |
| 파싱 정확도 | PA | 에이전트가 의도한 액션을 올바르게 추출한 비율 | 수동 평가 (n=10 태스크) |
| 첫 시도 성공률 | TTFA | 첫 번째 시도에 올바른 페이지 URL을 호출한 비율 | 에이전트 로그 분석 |
| 태스크 완료율 | TCR | 다단계 탐색 태스크의 최종 완료 비율 | 수동 평가 |

### 실험 시나리오

| # | 태스크 | 난이도 | 측정 포인트 |
|---|--------|--------|-------------|
| 1 | "Quickstart 페이지 링크를 알려줘" | 쉬움 | TTFA - 단순 조회 |
| 2 | "Tool use를 시작하려면 뭘 읽어야 해?" | 중간 | PA - 다중 페이지 추천 |
| 3 | "Vision 기능과 Extended thinking의 차이를 설명해줘" | 어려움 | TCR - 다단계 탐색 |
| 4 | "Model Migration 관련 페이지를 모두 찾아줘" | 어려움 | PA + TCR |

### 에이전트 타입별 선호 포맷 발견

```
단계 1: 각 에이전트 타입에서 4가지 포맷 모두 실험
단계 2: 포맷별 TTFA / PA / TCR 수집
단계 3: 에이전트 타입별 최적 포맷 식별
단계 4: 교차 검증 (다른 태스크로 동일 포맷 재테스트)
```

---

## 6. 성공 기준

### 포맷별 성공 기준

| 포맷 | 최소 기준 | 목표 기준 |
|------|-----------|-----------|
| JSON | TTFA >= 70%, 에이전트가 구조를 올바르게 파싱 | TTFA >= 90%, TCR >= 80% |
| XML | TTFA >= 60%, 태그 구조가 올바르게 해석됨 | TTFA >= 80%, TCR >= 70% |
| MD | TTFA >= 70%, 헤딩 계층이 네비게이션으로 활용됨 | TTFA >= 85%, TCR >= 75% |
| TXT | TTFA >= 50%, 컨벤션이 일관성 있게 해석됨 | TTFA >= 70%, TCR >= 65% |

### PoC 전체 성공 기준

- [ ] 4가지 포맷 모두 `agentnav.baekenough.com`에서 정상 서빙
- [ ] Claude Code와 GPT Codex가 각각 최소 1가지 포맷으로 태스크 성공
- [ ] 포맷별 효율 차이에 대한 정량적 데이터 수집 완료
- [ ] 에이전트 타입별 권장 포맷 초안 도출

---

## 7. 다음 단계

1. `platform.claude.com/docs` 크롤링 및 페이지 목록 추출 스크립트 작성
2. 4가지 포맷의 진입점 파일 초안 작성
3. 호스팅 플랫폼 결정 및 도메인 연결
4. 실험 태스크 10개 정의 및 평가 기준 세부화
5. 포맷별 파일 생성 및 배포
