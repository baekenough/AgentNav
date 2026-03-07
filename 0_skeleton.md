# agents.txt — AI 에이전트를 위한 웹사이트 안내 표준

> **Status**: Idea / Draft v0.1
> **Author**: SangYi Baek (백상이)
> **Created**: 2026-03-07

---

## 1. 한 줄 요약

`robots.txt`가 크롤러에게 "여기는 오지 마"를 알려줬다면,
`agents.txt`는 AI 에이전트에게 **"여기는 이렇게 쓰면 돼"**를 알려주는 표준 파일이다.

---

## 2. 문제 인식

### 2.1 현재 AI 에이전트의 웹 상호작용 방식

AI 에이전트(Claude Code, GPT Codex 등)가 웹사이트와 상호작용할 때, 기본적으로 HTML 전체를 파싱하거나 브라우저를 자동화(Playwright MCP 등)해서 DOM을 탐색한다.

이 방식의 핵심 문제:

- **토큰 낭비**: 페이지 하나의 DOM을 파싱하면 수천~수만 토큰을 소비한다. Playwright MCP의 경우 버튼 클릭 한 번에 12,891자의 accessibility tree가 반환된다.
- **시행착오 비용**: 에이전트가 사이트 구조를 스스로 파악해야 하므로, 네비게이션/인증/API 호출 방식을 시행착오로 알아내는 과정에서 토큰과 시간이 낭비된다.
- **비표준적 접근**: 사이트마다 에이전트의 접근 방식이 달라, 범용적인 에이전트 사용이 어렵다.

### 2.2 영감: Vercel agent-browser의 교훈

Vercel의 agent-browser가 보여준 핵심 인사이트:

- DOM 전체 대신 accessibility tree의 의미만 전달하면 93% 토큰 절감
- 도구를 17개에서 2개로 줄이자 성공률 80% → 100%, 토큰 37% 절감
- **"AI를 위한 도구는 처음부터 AI에 맞게 설계해야 한다"**

이 철학을 사이트 레벨로 확장한 것이 agents.txt이다.

### 2.3 기존 표준과의 관계

| 표준 | 역할 | agents.txt와의 차이 |
|------|------|---------------------|
| `robots.txt` | 크롤러 접근 제어 (allow/disallow) | 제한이 아닌 **안내** |
| `sitemap.xml` | 크롤링 대상 URL 나열 | URL만 나열 vs **행동 가능한 액션** 기술 |
| OpenAPI spec | 백엔드 API 엔드포인트 기술 | API 전용 vs **페이지 + API 통합 안내** |
| `llms.txt` | LLM에게 사이트 정보 제공 | 정보 제공 vs **행동 가이드** |
| MCP | 에이전트-서비스 간 도구 프로토콜 | 런타임 프로토콜 vs **정적 선언** |

agents.txt는 이들을 대체하는 것이 아니라, **에이전트가 사이트에 도착했을 때 가장 먼저 읽는 안내문** 역할을 한다. 필요하면 OpenAPI spec이나 MCP 서버로 연결해주는 진입점이다.

---

## 3. 핵심 컨셉

### 3.1 설계 원칙

1. **정적 선언(Static Declaration)**: 서버 로직 없이 정적 파일만으로 동작한다
2. **페이지 단위 분리**: 사이트 전체가 아닌 개별 페이지 수준의 안내를 제공한다
3. **에이전트 중립**: 특정 에이전트에 종속되지 않는 공통 구조 + 에이전트별 힌트
4. **점진적 도입**: 최소한의 필드만으로 시작 가능하고, 필요에 따라 확장한다
5. **토큰 효율 우선**: 에이전트의 컨텍스트 윈도우를 최소한으로 사용하는 것이 목표다

### 3.2 디스커버리 (에이전트가 이 파일을 찾는 방법)

```
https://example.com/.well-known/agents.json    ← 1순위: 표준 경로
https://example.com/agents.json                 ← 2순위: 루트 fallback
<meta name="agents" content="/agents.json">     ← 3순위: HTML 임베딩
```

1차 구현에서는 고정 경로(`/.well-known/agents.json`)만 사용한다.

---

## 4. 파일 구조

### 4.1 전체 디렉터리 구조

```
mysite.com/
├── .well-known/
│   └── agents.json              # 진입점: 사이트 메타 + 페이지 인덱스
├── agents/
│   ├── pages/
│   │   ├── index.json           # 홈페이지 안내
│   │   ├── blog.json            # 블로그 섹션 안내
│   │   └── projects.json        # 프로젝트 섹션 안내
│   └── guides/
│       ├── claude-code.md       # Claude Code 에이전트 전용 가이드
│       └── codex.md             # GPT Codex 에이전트 전용 가이드
```

### 4.2 루트 매니페스트 (`.well-known/agents.json`)

```json
{
  "$schema": "https://agents-txt.org/schema/v0.1.json",
  "version": "0.1",
  "site": {
    "name": "SangYi's Site",
    "description": "개인 기술 블로그 및 프로젝트 포트폴리오",
    "base_url": "https://example.com",
    "language": "ko"
  },
  "auth": null,
  "pages": [
    {
      "path": "/",
      "ref": "/agents/pages/index.json"
    },
    {
      "path": "/blog",
      "ref": "/agents/pages/blog.json"
    },
    {
      "path": "/projects",
      "ref": "/agents/pages/projects.json"
    }
  ],
  "agent_guides": {
    "claude-code": "/agents/guides/claude-code.md",
    "codex": "/agents/guides/codex.md"
  },
  "policies": {
    "allow_scraping": true,
    "allow_automated_actions": false,
    "preferred_interaction": "api"
  }
}
```

### 4.3 페이지별 안내 (`agents/pages/*.json`)

```json
{
  "path": "/blog",
  "purpose": "기술 블로그 글 목록 조회 및 개별 글 읽기",
  "available_actions": [
    {
      "action": "list_posts",
      "description": "블로그 글 목록 조회",
      "method": "GET",
      "endpoint": "/api/posts",
      "params": {
        "tag": "(optional) 태그 필터",
        "page": "(optional) 페이지 번호, default 1",
        "limit": "(optional) 한 페이지당 글 수, default 10"
      },
      "response_summary": "{ posts: [{ id, title, date, tags, excerpt }], total, page }"
    },
    {
      "action": "read_post",
      "description": "개별 블로그 글 조회",
      "method": "GET",
      "endpoint": "/api/posts/:id",
      "response_summary": "{ id, title, date, tags, content_md, author }"
    }
  ],
  "navigates_to": [
    { "path": "/blog/:id", "trigger": "개별 글 선택 시" },
    { "path": "/", "trigger": "홈으로 돌아가기" }
  ],
  "required_headers": {
    "Accept": "application/json"
  },
  "notes": "content_md 필드는 마크다운 원문을 반환하므로 HTML 파싱 불필요"
}
```

### 4.4 에이전트별 가이드 (`agents/guides/*.md`)

자연어로 작성되며, 해당 에이전트의 특성에 맞는 사용법을 안내한다.

```markdown
# Claude Code Guide for example.com

## Quick Start
이 사이트의 데이터에 접근하려면 HTML 파싱 대신 JSON API를 사용하세요.

## API 사용법
- 블로그 글 목록: `curl https://example.com/api/posts`
- 개별 글 조회: `curl https://example.com/api/posts/{id}`

## 주의사항
- 자동 글 작성/수정은 허용되지 않습니다
- rate limit: 60 requests/min
```

---

## 5. 1차 구현 범위 (MVP)

### 5.1 목표

- 개인 도메인에 정적 agents.json + 페이지별 안내 + 에이전트 가이드를 호스팅
- Claude Code와 GPT Codex가 각각 **네이티브하게** 이 파일을 읽고 사이트를 활용하는 시나리오 검증
- 인증/세션/토큰 관리는 스코프 밖 (정적 파일만)

### 5.2 검증 시나리오

| 시나리오 | 기대 결과 |
|----------|-----------|
| 에이전트에게 "이 사이트의 agents.json을 읽어봐" 지시 | 사이트 구조와 가능한 액션을 파악 |
| "이 사이트의 블로그 글 목록을 가져와" 지시 | HTML 파싱 없이 API로 직접 접근 |
| "이 사이트에서 뭘 할 수 있어?" 질문 | agents.json 기반으로 기능 목록 응답 |

### 5.3 사전 조사 필요 항목

1. **Claude Code의 외부 리소스 접근 방식**
   - fetch / curl / MCP 중 어떤 경로로 웹 리소스를 읽는가
   - `.well-known` 경로의 파일을 자동으로 탐색하는 기능이 있는가
   - 자연어 가이드(.md) vs 구조화된 데이터(.json) 중 어떤 것을 더 잘 소화하는가

2. **GPT Codex의 외부 리소스 접근 방식**
   - 동일한 질문들을 Codex 관점에서 조사
   - Codex의 tool calling / function calling 패턴과 agents.json의 호환성

3. **포맷 결정**
   - JSON vs YAML vs Markdown: 에이전트 파싱 효율 + 사람 가독성 균형
   - 1차에서는 JSON(구조 데이터) + MD(가이드) 조합으로 시작

---

## 6. 향후 확장 방향 (v0.2+)

1차 MVP 검증 후 고려할 확장:

- **인증 레이어**: API 키/OAuth 기반 에이전트 인증 지원
- **rate limit 선언**: 에이전트별 요청 제한 명시
- **MCP 서버 연동**: `mcp_server` 필드로 MCP 엔드포인트 안내
- **에이전트 식별**: `User-Agent` 또는 커스텀 헤더로 에이전트 유형 식별
- **동적 페이지 안내**: SPA/동적 페이지의 상태 기반 액션 기술
- **커뮤니티 표준화**: 스펙을 공개하고 다른 사이트/에이전트의 채택 유도
- **`requires_human_confirmation` 패턴**: 결제/삭제 등 위험 액션에 대한 인간 확인 정책

---

## 7. 핵심 가설

이 프로젝트가 검증하려는 가설:

> **"사이트 소유자가 에이전트용 안내 파일을 제공하면,
> 에이전트가 DOM 파싱 대비 현저히 적은 토큰으로
> 동일하거나 더 나은 작업 수행을 할 수 있다."**

측정 지표:
- agents.json 유무에 따른 토큰 사용량 비교
- 작업 성공률 비교
- 에이전트의 첫 유의미한 액션까지 걸리는 시간(time-to-first-action)

---

## 8. 참고 자료

- [AI에게 Playwright MCP를 주면 안되는 이유 (PEC)](https://www.productengineer.info/community/articles/10d24bff-1a0d-43d3-bf99-c4c4f3f72bd2) — Vercel agent-browser 분석, 이 아이디어의 직접적 영감
- [RFC 8615 - Well-Known URIs](https://tools.ietf.org/html/rfc8615) — `.well-known` 경로 표준
- [robots.txt (RFC 9309)](https://www.rfc-editor.org/rfc/rfc9309) — 웹 크롤러 접근 제어 표준
- [llms.txt](https://llmstxt.org/) — LLM을 위한 사이트 정보 제공 시도
- [Model Context Protocol (MCP)](https://modelcontextprotocol.io/) — AI 에이전트-서비스 간 도구 프로토콜
