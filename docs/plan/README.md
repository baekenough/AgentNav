# agents.txt — AI Agent Website Navigation Standard

| 항목 | 내용 |
|------|------|
| **상태** | Idea / Draft v0.1 |
| **저자** | SangYi Baek (백상이) |
| **작성일** | 2026-03-07 |

---

## 한 줄 요약

`robots.txt`가 크롤러에게 "여기는 오지 마"를 알려줬다면, `agents.txt`는 AI 에이전트에게 **"여기는 이렇게 쓰면 돼"**를 알려주는 표준 파일이다.

---

## 목차

| 문서 | 제목 | 설명 |
|------|------|------|
| [01-problem-statement.md](./01-problem-statement.md) | 문제 인식 | 현재 AI 에이전트의 웹 상호작용 방식의 한계, Vercel agent-browser의 교훈, 기존 표준(`robots.txt`, `sitemap.xml`, OpenAPI 등)과의 관계 |
| [02-concept.md](./02-concept.md) | 개념 및 설계 원칙 | `agents.txt`가 무엇인지, 어떤 원칙으로 설계되는지, 핵심 철학 |
| [03-spec.md](./03-spec.md) | 파일 명세 | `agents.txt` 파일 포맷, 필드 정의, 문법 규칙, 예시 |
| [04-use-cases.md](./04-use-cases.md) | 활용 시나리오 | 실제 웹사이트 유형별 적용 사례 (SaaS, 쇼핑몰, 문서 사이트 등) |
| [05-ecosystem.md](./05-ecosystem.md) | 생태계 및 통합 | MCP, OpenAPI, `llms.txt` 등 기존 표준과의 통합 방식, 에이전트 프레임워크 연동 |
| [06-adoption-strategy.md](./06-adoption-strategy.md) | 채택 전략 | 표준 확산을 위한 로드맵, 커뮤니티 구성, 선례(robots.txt 확산 과정) 분석 |
| [07-open-questions.md](./07-open-questions.md) | 열린 질문 | 아직 해결되지 않은 설계 이슈, 논쟁 지점, 향후 연구 과제 |

---

## 이 문서 모음에 대해

이 폴더는 `agents.txt` 표준 아이디어의 초기 기획 문서를 담고 있다. 각 문서는 독립적으로 읽을 수 있지만, 순서대로 읽으면 문제 인식 → 개념 설계 → 명세 → 생태계 → 확산 전략의 흐름으로 이해할 수 있다.

현재 상태는 **Draft v0.1**로, 아이디어 검토 단계이다. 피드백과 논의를 통해 지속적으로 발전시킬 예정이다.
