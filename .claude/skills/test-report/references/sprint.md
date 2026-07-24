# Test Report — Mode SPRINT

> `/test-report --sprint S05` | `/test-report --sprint S05 --version v2.0`

## Input
Giống RELEASE nhưng scope = 1 sprint (filter by date range hoặc sprint label).

## Workflow

### Step 1: Xác định sprint scope
- Sprint label: S05
- Date range: [start] → [end] (hỏi user nếu không rõ)
- Version: active version (hoặc `--version`)

### Step 2: Filter data theo sprint
- §15 Execution Log: runs trong date range
- §16 Fail Registry: fails trong date range
- bug-index.md + `Bug Data` sheet: bugs created trong date range — `Bug Data` cột Sprint (K)/Round (U) map trực tiếp `R[N]` ↔ sprint hiện tại (xem `log-bug/references/sync-excel.md`)
- TC-MASTER: `Summary!C9` (Sprint field) xác nhận đúng sprint đang report; TC theo round tương ứng đọc qua block round (N-AL) trong sheet Test Cases, hoặc tổng hợp nhanh qua `Dashboard` cột "R[N] Executed/Pass/Fail/Block/N/A"

### Step 3: Calculate sprint metrics

| Metric | Formula |
|--------|---------|
| Sprint TC planned | Tổng TC trong scope version (Dashboard tổng "Tổng TC") |
| Sprint TC executed | **Đọc `Dashboard` cột "R[N] Executed"** ứng với round ánh xạ sprint hiện tại (khớp `Bug Data` cột Sprint/Round convention) |
| Execution rate | Executed / Planned × 100% |
| Pass rate | **Đọc `Dashboard` cột "R[N] Pass"** / "R[N] Executed" × 100% |
| New bugs | Bugs created trong sprint (Bug Data cột Sprint = R[N] hiện tại) |
| Bugs closed | Bugs closed trong sprint |
| Net open | Open bugs cuối sprint |
| Velocity | TCs executed per day |

### Step 4: Generate sprint report

**File:** `09_reports/REPORT-SPRINT-S[N]-v[X]-[date].md`

```markdown
# Sprint Report — S[N] — v[X]

## Sprint Overview
| Field | Value |
|-------|-------|
| Sprint | S[N] |
| Version | v[X] |
| Period | [start] → [end] |
| Environment | [URL] |

## Execution Summary
| Metric | Value |
|--------|-------|
| TC Planned | [N] |
| TC Executed | [N] ([%] of planned) |
| Passed | [N] ([%]) |
| Failed | [N] ([%]) |
| Blocked | [N] |
| New bugs | [N] |
| Bugs closed | [N] |
| Velocity | [N] TCs/day |

## Quality Gates (snapshot cuối sprint)
| # | Gate | Criteria | Result | Status |
|---|------|----------|--------|--------|
(G1-G7 table)

## Failed TCs
| TC ID | Module | Fail Type | Bug ID | Status |
|-------|--------|----------|--------|--------|

## Bugs Created This Sprint
| Bug ID | TC ID | Severity | Module | Status |
|--------|-------|----------|--------|--------|

## Blocked Items
| TC ID | Reason | Impact | Action Required |
|-------|--------|--------|----------------|

## Sprint Burndown (nếu có data nhiều ngày)
| Date | Planned | Executed | Remaining |
|------|---------|----------|-----------|

## Next Sprint Recommendation
- Carry-over TCs: [N] (chưa executed)
- Open bugs: [N] (cần fix trước sprint tiếp)
- Blocked items: [N] (cần resolve)
```

### Step 5: Update
- `08_test-runs/TR-S[N]-v[X]-[date].md` (test run log)
- §8 = COMPLETED
