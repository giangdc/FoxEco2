# Test Report — Mode CROSS-VERSION

> `/test-report --cross-version v1.0 v2.0`
> `/test-report --cross-version v1.0 v1.1 v2.0`

## Workflow

### Step 1: Đọc data cho MỖI version chỉ định
Với mỗi version → đọc: MASTER-MEMORY §1 (version info), Version MEMORY §3-§4, TC-MASTER của version đó (mỗi version có file ISC riêng — `ISC_[Project]_[Version]_TC_...xlsx`, alias `TC-MASTER-v[Version].xlsx`), §15, §16, bug-index (+ Bug Data sheet), review reports.

**TC coverage / Pass rate / Automation coverage per version:** đọc trực tiếp từ `Dashboard` sheet (tổng cột "Coverage %"/"Pass %"/"Auto") của TC-MASTER version đó — xem `release.md` §"Calculate metrics" cho mapping đầy đủ, KHÔNG tự parse lại row Test Cases cho từng version.

### Step 2: Build comparison matrix

```markdown
## Version Progression

| Metric | v1.0 | v1.1 | v2.0 | Trend |
|--------|------|------|------|-------|
| Total scenarios | 42 | 47 | 58 | ↑ Growing |
| NEW scenarios | 42 | 5 | 12 | — |
| MODIFIED scenarios | — | 2 | 3 | — |
| CARRIED scenarios | — | 40 | 43 | ↑ |
| DEPRECATED | — | 0 | 7 | ↑ |
| Total TCs | 50 | 58 | 68 | ↑ |
| TC coverage | 98% | 100% | 93% | ⚠️ Drop |
| Pass rate (latest run) | 88% | 92% | 85% | ⚠️ Drop |
| Open bugs | 0 | 0 | 2 | ⚠️ |
| P1 bugs | 0 | 0 | 1 | ⛔ |
| TC Review score | 82 | 85 | 75 | ↓ |
| SRC-TC Match score | 85 | 90 | 78 | ↓ |
| Automation coverage | 30% | 45% | 28% | ↓ |
```

### Step 3: Regression analysis (latest vs parent)

```markdown
## Regression Analysis — v2.0 vs v1.1

| Category | Count | Executed | Pass | Fail | Notes |
|----------|-------|----------|------|------|-------|
| NEW scenarios | 12 | 10 | 8 | 2 | 2 bugs logged |
| MODIFIED scenarios | 3 | 3 | 3 | 0 | — |
| CARRIED (high risk) | 8 | 8 | 7 | 1 | 1 locator stale |
| CARRIED (low risk) | 35 | 10 | 10 | 0 | Sample regression |
| DEPRECATED | 7 | — | — | — | Removed from scope |

**Regression pass rate:** 28/31 = 90.3% ✅
**NEW feature pass rate:** 8/10 = 80% ⚠️ Below target
```

### Step 4: Bug trend across versions

```markdown
## Bug Trend

| Version | New Bugs | Closed | Net Open | P1 | P2 | P3 |
|---------|----------|--------|----------|----|----|-----|
| v1.0 | 3 | 3 | 0 | 0 | 2 | 1 |
| v1.1 | 1 | 1 | 0 | 0 | 1 | 0 |
| v2.0 | 3 | 1 | 2 | 1 | 1 | 1 |

**Trend:** Bug density increasing in v2.0. P1 bug present — release risk.
```

### Step 5: Quality trend

```markdown
## Quality Trend

| Gate | v1.0 | v1.1 | v2.0 |
|------|------|------|------|
| G1 TC Review | 82 ✅ | 85 ✅ | 75 ✅ |
| G2 P1 Pass | 100% ✅ | 100% ✅ | 90% ❌ |
| G3 Overall Pass | 88% ❌ | 92% ✅ | 85% ❌ |
| G4 P1 Bugs | 0 ✅ | 0 ✅ | 1 ❌ |
| G5 Bug Fix | 100% ✅ | 100% ✅ | 33% ❌ |
| G6 Blocked | 0 ✅ | 0 ✅ | 0 ✅ |
| G7 SRC-TC | 85 ✅ | 90 ✅ | 78 ✅ |
| **Overall** | **CONDITIONAL** | **GO** | **NO-GO** |
```

### Step 6: Generate report
**File:** `09_reports/REPORT-CROSSVER-v[X]-v[Y]-[date].md`

### Step 7: Recommendations
- Version trajectory: improving / declining / stable
- Risk areas: modules with declining quality
- Action items: fix P1 bugs, improve automation coverage, etc.
