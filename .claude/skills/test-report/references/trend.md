# Test Report — Mode TREND

> `/test-report --trend` | `/test-report --trend --version v2.0`

## Workflow

### Step 1: Aggregate data across runs
Đọc §15 Execution Log → tất cả runs (filter version nếu chỉ định).

### Step 2: Build trend data

**Pass rate over time:**
```
| Run | Date | Total | Pass | Fail | Rate | Delta |
|-----|------|-------|------|------|------|-------|
| RUN-001 | 04-15 | 20 | 14 | 6 | 70% | — |
| RUN-002 | 04-18 | 25 | 20 | 5 | 80% | +10% |
| RUN-003 | 04-22 | 30 | 27 | 3 | 90% | +10% |
| RUN-004 | 04-25 | 30 | 28 | 2 | 93% | +3% |
```

**Bug open/close over time:**
```
| Date | New | Closed | Net Open | Trend |
|------|-----|--------|----------|-------|
| 04-15 | 3 | 0 | 3 | ↑ |
| 04-18 | 1 | 2 | 2 | ↓ |
| 04-22 | 0 | 1 | 1 | ↓ |
| 04-25 | 0 | 0 | 1 | → |
```

**Failure classification trend:**
```
| Run | LOCATOR | ASSERTION | ENV | UNKNOWN |
|-----|---------|-----------|-----|---------|
| RUN-001 | 3 | 2 | 1 | 0 |
| RUN-002 | 1 | 3 | 1 | 0 |
| RUN-003 | 0 | 2 | 1 | 0 |
| RUN-004 | 0 | 1 | 1 | 0 |
```

### Step 3: Insights
- Pass rate trajectory: improving / declining / plateauing
- Bug convergence: closing faster than opening? When zero-bug?
- Failure pattern: LOCATOR issues decreasing (locators stabilizing)?
- Bottleneck: ENV_ERROR consistent → env instability

### Step 4: Present inline hoặc tạo file
- Short trend → inline
- Detailed trend → `09_reports/REPORT-TREND-v[X]-[date].md`
