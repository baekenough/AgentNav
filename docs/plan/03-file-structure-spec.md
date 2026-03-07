# File Structure Specification

## 4.1 전체 디렉터리 구조

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

## 4.2 루트 매니페스트 (`.well-known/agents.json`)

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
    { "path": "/", "ref": "/agents/pages/index.json" },
    { "path": "/blog", "ref": "/agents/pages/blog.json" },
    { "path": "/projects", "ref": "/agents/pages/projects.json" }
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

## 4.3 페이지별 안내 (`agents/pages/*.json`)

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
  "required_headers": { "Accept": "application/json" },
  "notes": "content_md 필드는 마크다운 원문을 반환하므로 HTML 파싱 불필요"
}
```

## 4.4 에이전트별 가이드 (`agents/guides/*.md`)

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
