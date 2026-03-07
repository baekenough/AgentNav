# 07. 참고 자료 및 선행 연구

---

## 한 줄 요약

`agents.txt` 아이디어의 직접적 영감, 관련 웹 표준, 그리고 유사한 시도들을 정리한다.

---

## 8.1 직접적 영감 (Direct Inspirations)

이 프로젝트의 아이디어를 직접적으로 촉발한 자료들이다.

### AI에게 Playwright MCP를 주면 안되는 이유 (PEC)

- **링크**: [productengineer.info](https://www.productengineer.info/community/articles/10d24bff-1a0d-43d3-bf99-c4c4f3f72bd2)
- **핵심 내용**: Vercel의 agent-browser 분석. DOM 전체 파싱 대신 의미 정보만 전달하면 93% 토큰 절감, 도구 수를 줄이면 성공률이 80% → 100%로 상승한다는 실증 데이터를 제시한다.
- **이 프로젝트와의 관계**: "AI를 위한 도구는 처음부터 AI에 맞게 설계해야 한다"는 철학을 사이트 레벨로 확장한 것이 `agents.txt`의 출발점이다. 에이전트가 사이트 구조를 스스로 파악하게 두지 않고, 사이트 소유자가 먼저 안내 파일을 제공하는 패러다임을 제안한다.

---

## 8.2 웹 표준 (Web Standards)

`agents.txt`가 따르거나 참조하는 기존 웹 표준들이다.

### RFC 8615 — Well-Known URIs

- **링크**: [tools.ietf.org/html/rfc8615](https://tools.ietf.org/html/rfc8615)
- **핵심 내용**: `/.well-known/` 경로를 표준화한 RFC. 특정 목적의 파일을 사이트 루트의 예측 가능한 경로에 배치하는 규약이다.
- **이 프로젝트와의 관계**: `agents.txt`의 배치 경로로 `/.well-known/agents.txt` 또는 루트의 `/agents.txt`를 검토하는 근거가 된다. 에이전트가 예측 가능한 경로에서 안내 파일을 탐색할 수 있도록 한다.

### robots.txt — RFC 9309

- **링크**: [rfc-editor.org/rfc/rfc9309](https://www.rfc-editor.org/rfc/rfc9309)
- **핵심 내용**: 웹 크롤러의 접근을 제어하는 표준. 1994년부터 사용되어 현재까지 가장 보편적인 크롤러 제어 메커니즘이다.
- **이 프로젝트와의 관계**: `agents.txt`의 직접적인 명명 영감. `robots.txt`가 "오지 마"를 알려준다면, `agents.txt`는 "이렇게 써"를 알려준다. 표준이 단순한 텍스트 파일로 시작해 광범위하게 채택된 역사적 선례이기도 하다.

---

## 8.3 유사한 시도들 (Related Initiatives)

`agents.txt`와 유사한 문제를 다른 방식으로 접근한 이니셔티브들이다.

### llms.txt

- **링크**: [llmstxt.org](https://llmstxt.org/)
- **핵심 내용**: LLM이 사이트 정보를 효율적으로 소화할 수 있도록 마크다운 형식으로 사이트 정보를 제공하는 비공식 제안이다.
- **이 프로젝트와의 관계**: 목적은 유사하지만 접근 방식이 다르다. `llms.txt`는 정보 제공(정보성)에 초점을 맞추고, `agents.txt`는 에이전트가 실제로 수행할 수 있는 액션 안내(행동성)에 초점을 맞춘다. `llms.txt`가 "사이트가 무엇인지" 설명한다면, `agents.txt`는 "에이전트가 여기서 무엇을 어떻게 할 수 있는지"를 기술한다.

### Model Context Protocol (MCP)

- **링크**: [modelcontextprotocol.io](https://modelcontextprotocol.io/)
- **핵심 내용**: Anthropic이 제안한 AI 에이전트와 외부 서비스 간의 표준 도구 프로토콜. 에이전트가 외부 시스템과 상호작용할 때 사용할 수 있는 도구를 동적으로 정의한다.
- **이 프로젝트와의 관계**: MCP는 런타임 프로토콜(에이전트가 서비스와 실시간으로 협상)이고, `agents.txt`는 정적 선언(사이트가 미리 안내 파일을 준비)이다. 두 접근은 상호 보완적이다. `agents.txt`가 진입점 역할을 하고, 필요 시 MCP 서버로 연결해주는 포인터를 포함할 수 있다.

---

## 8.4 추가 참고 자료

| 자료 | 설명 |
|------|------|
| [sitemap.xml (sitemaps.org)](https://www.sitemaps.org/) | 크롤링 대상 URL을 나열하는 표준. `agents.txt`가 URL 목록을 넘어 액션 안내를 제공한다는 점에서 차별화된다. |
| [OpenAPI Specification](https://swagger.io/specification/) | 백엔드 API 엔드포인트를 기술하는 표준. API 전용이라는 한계가 있으며, `agents.txt`는 API와 페이지 네비게이션을 통합하여 안내한다. |
| [Web Accessibility Initiative (WAI)](https://www.w3.org/WAI/) | 웹 접근성 표준. 에이전트의 웹 상호작용이 결국 "접근성"의 새로운 차원임을 시사한다. |
