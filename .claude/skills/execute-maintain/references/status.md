# Execute — Mode STATUS

> `/execute-maintain --status` | `/execute-maintain --status --version v2.0`

## Workflow

### Step 1: Đọc §15 + §16

### Step 2: Present execution overview

```
📊 Execution Status — v[X]

## Run History (latest 5)
| Run | Date | Scope | Total | Pass | Fail | Skip | Rate |
|-----|------|-------|-------|------|------|------|------|
| RUN-004 | 05-25 | All | 30 | 28 | 1 | 1 | 93% |
| RUN-003 | 05-22 | LoginTest | 5 | 4 | 1 | 0 | 80% |
| ...

## Open Failures
| Fail ID | Type | Method | Status | Bug ID |
|---------|------|--------|--------|--------|
| FAIL-001 | ASSERTION | testLoginInvalidEmail | Open | — |
| FAIL-003 | LOCATOR | testDashboardFilter | Open | — |

## Failure Breakdown
| Type | Count | % |
|------|-------|---|
| ASSERTION_FAIL | 1 | 50% |
| LOCATOR_STALE | 1 | 50% |
| ENV_ERROR | 0 | 0% |

## Pass Rate Trend
RUN-001: 70% → RUN-002: 80% → RUN-003: 80% → RUN-004: 93% ↑

## Recommendations
- FAIL-001: suggest /log-bug (ASSERTION)
- FAIL-003: suggest /execute-maintain --recheck FAIL-003 (LOCATOR)
```

KHÔNG sửa file.
