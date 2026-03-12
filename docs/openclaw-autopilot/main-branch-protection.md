# Main 브랜치 보호 가이드

`main` 브랜치는 직접 push를 막고, PR 리뷰 기반으로만 변경되게 운영하는 것을 권장합니다.

## 권장 기본 정책

- Direct push 금지
- Force push 금지
- Branch delete 금지
- PR 리뷰 최소 1명 승인
- stale review dismiss
- conversation resolution required
- admins 포함 동일 정책 적용

## 적용 방법 (GitHub CLI)

- 예시 payload: `docs/openclaw-autopilot/main-branch-protection.example.json`
- 자동 적용 스크립트:

```bash
./scripts/setup_main_branch_protection.sh
```

옵션:

```bash
# 특정 저장소 지정
./scripts/setup_main_branch_protection.sh --repo owner/repo

# PR 승인 수 변경 (기본 1)
./scripts/setup_main_branch_protection.sh --approvals 2

# CI required status check context 지정
./scripts/setup_main_branch_protection.sh --contexts "agentnav-ci / validate"
```

## 사전 조건

- `gh` 설치
- `gh auth login` 완료
- 저장소 admin 권한

## 주의

- required contexts를 지정하면 해당 체크가 green이 아니면 merge가 막힙니다.
- 현재 repo에 실제 CI workflow가 준비되지 않았다면 `--contexts`는 비워두는 것을 권장합니다.
