# AgentNav Auto-Pilot MVP Pack

OpenClaw를 control plane으로 두고 AgentNav 저장소를 자동 운영하기 위한 **즉시 적용 가능한 초안 묶음**입니다.

## 포함 파일

- `db/001_init_schema.sql`  
  OpenClaw 이슈/실행/PR/배포/벤치마크 기본 스키마
- `db/002_state_machine.sql`  
  상태 전이 테이블 + 가드 코드 + 전이 로그
- `.github/workflows/ci.yml`  
  lint/typecheck/unit/smoke/nav benchmark 게이트
- `.github/workflows/pr-summary.yml`  
  CI 완료 시 PR에 결과 요약 코멘트
- `.github/workflows/deploy-staging.yml`  
  main 머지 후 staging 자동 배포
- `.github/workflows/deploy-prod.yml`  
  수동 트리거 + GitHub Environment 승인 기반 prod 배포
- `docs/backlog-2weeks.md`  
  2주 실행용 GitHub 이슈 백로그

## 빠른 적용 순서

1. DB에 `001_init_schema.sql` 실행
2. DB에 `002_state_machine.sql` 실행
3. AgentNav repo에 `.github/workflows/*.yml` 복사
4. `scripts/` 배포/헬스체크 스크립트 구현
5. GitHub Environments(`staging`, `production`) 및 보호 브랜치 설정

## 전제

- PostgreSQL 14+ (권장)
- `gen_random_uuid()` 사용을 위해 `pgcrypto` 확장 사용
- GitHub App 또는 동급 machine identity 구성
