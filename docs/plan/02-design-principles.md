# Design Principles & Core Concepts

## 3.1 설계 원칙

1. **정적 선언(Static Declaration)**: 서버 로직 없이 정적 파일만으로 동작한다
2. **페이지 단위 분리**: 사이트 전체가 아닌 개별 페이지 수준의 안내를 제공한다
3. **에이전트 중립**: 특정 에이전트에 종속되지 않는 공통 구조 + 에이전트별 힌트
4. **점진적 도입**: 최소한의 필드만으로 시작 가능하고, 필요에 따라 확장한다
5. **토큰 효율 우선**: 에이전트의 컨텍스트 윈도우를 최소한으로 사용하는 것이 목표다

## 3.2 디스커버리 (에이전트가 이 파일을 찾는 방법)

```
https://example.com/.well-known/agents.json    ← 1순위: 표준 경로
https://example.com/agents.json                 ← 2순위: 루트 fallback
<meta name="agents" content="/agents.json">     ← 3순위: HTML 임베딩
```

1차 구현에서는 고정 경로(`/.well-known/agents.json`)만 사용한다.
