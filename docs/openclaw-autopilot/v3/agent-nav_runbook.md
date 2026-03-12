# AgentNav Automation Runbook

## 1. CI failure loop
1. Inspect failing check.
2. Compare with previous failure signature.
3. If repeated twice, stop automation.
4. Move issue to human review.
5. Persist logs and benchmark artifacts.

## 2. Staging deploy failure
1. Mark deployment failed.
2. Collect staging logs.
3. Stop additional promotions.
4. Roll back to last stable artifact.
5. Re-open or create follow-up issue.

## 3. Production canary failure
1. Freeze rollout.
2. Drain canary.
3. Roll back to previous stable version.
4. Notify approver and incident channel.
5. Generate postmortem issue template.

## 4. Benchmark regression failure
1. Compare current report to baseline.
2. If success-rate drop > threshold, block merge/deploy.
3. If cost/latency exceed warning band, escalate to approval queue.
4. Store diff summary in issue timeline.

## 5. Emergency manual stop
- Pause issue automation.
- Disable deploy workflow or revoke promotion.
- Mark issue as paused with reason.
- Preserve branch, PR, artifacts, and logs.

## 6. Required evidence before closure
- linked issue
- linked PR
- green checks
- benchmark artifact
- staging deployment evidence
- rollback readiness note
- approval record for prod if applicable
