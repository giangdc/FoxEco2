---
name: review-src-tc
description: So sánh TC-MASTER Excel vs source code Java bằng independent reviewer agent. Phát hiện mismatch steps/expected/data, missing implementations, orphan methods. Use when user mentions 'review source vs TC', 'compare TC và code', 'check mismatch', 'verify implementation', 'TC coverage check', 'review code của member', or runs /review-src-tc command.
license: Proprietary — FPT QA Toolkit v1.0 (qc-claude-v1)
compatibility: Designed for Claude Code QA projects with 00_..11_ folder structure (qc-claude-v1). Requires Claude Code or compatible agent runtime.
metadata:
  toolkit: qc-claude-v1
  pipeline-position: "9"
  status-section: MASTER-MEMORY-section-8
  owner: QC Team
  version: "1.1"
  released: "2026-06-05"
  updated: "2026-07-21 — migrated TC column mapping sang template ISC (42-cột, xem generate-tc/references/consolidate.md); bỏ Assigned To (--member dùng git author thay thế)"
---

# Review Source vs Test Case

TC-MASTER ↔ source code comparison bằng **independent reviewer agent** (Anthropic API).

## Command

| Command | Mode | Mô tả |
|---------|------|-------|
| `/review-src-tc` | FULL | So sánh toàn bộ |
| `/review-src-tc --module Login` | SCOPE | 1 module |
| `/review-src-tc --member member_A` | SCOPE | Code của member |
| `/review-src-tc --recheck` | RECHECK | Verify đã fix findings |
| `/review-src-tc --status` | STATUS | Xem tổng quan |
| `/review-src-tc --direct` | FULL (no agent) | Skip agent |

## Prerequisites

| Cần có | Check |
|--------|-------|
| TC-MASTER-v[X].xlsx (alias của file ISC chính thức — 42 cột, 1 sheet/module) | generate-tc ≥ PARTIAL |
| Test classes | implement-automation ≥ PARTIAL |

## Pipeline

`generate-tc` + `implement-automation` → **★ review-src-tc ★** → (user/implement-automation fix)

**Folder sở hữu:** `11_tc-review/`

## Mode Routing

| Condition | → Load |
|-----------|--------|
| `--status` | `references/status.md` |
| `--recheck` | `references/recheck.md` |
| `--module` hoặc `--member` | `references/scope.md` |
| Default (Java) | `references/full.md` |
| Default (TypeScript) | `references/full-typescript.md` — **stack-aware routing**, xem dưới |

## Stack-Aware Mode Routing (added 2026-05-31)

> Skill detect stack từ MEMORY §2 Tech Stack `Language` field. Route to variant tương ứng. Backward-compat fallback Java.

### Detection logic

```python
def detect_stack(memory_path):
    """Parse §2 Tech Stack Language field."""
    if not memory_path.exists():
        return "java"  # No MEMORY → Java default
    in_section_2 = False
    for line in memory_path.read_text().splitlines():
        if line.startswith("## 2. Tech Stack"):
            in_section_2 = True
            continue
        if in_section_2 and line.startswith("##") and not line.startswith("## 2"):
            break
        if in_section_2 and "| Language" in line:
            parts = [p.strip() for p in line.split("|")]
            if len(parts) >= 3 and parts[2] in ("TypeScript", "JavaScript"):
                return "typescript"
    return "java"
```

### Route table

| Detected stack | Default mode | --recheck | --module | --status |
|---|---|---|---|---|
| `typescript` | `references/full-typescript.md` | `references/recheck.md` (generic) | `references/scope.md` (generic — adapts via §2 detection) | `references/status.md` (generic) |
| `java` (default) | `references/full.md` (existing) | `references/recheck.md` | `references/scope.md` | `references/status.md` |

### Override flag

`/review-src-tc --stack typescript` HOẶC `/review-src-tc --stack java` cho explicit override.

### Backward-compat

1. Legacy MEMORY §2 free-form text → fallback Java + INFO warning
2. Existing Java projects: no change (continues load `full.md`)
3. TS projects (Language=TypeScript trong §2): auto-load `full-typescript.md`

### File pattern differences (key takeaway)

| Aspect | Java variant | TypeScript variant |
|---|---|---|
| File extension | `.java` | `.ts` |
| TC ID location | `@Test(description = "[TC ID] / [Req ID]: ...")` annotation | Test name string: `test('[TC ID]: ... / [Req ID]', ...)` |
| Parameterized | `@DataProvider` + `@Test(dataProvider="...")` | `for (const data of [...]) { test(\`${data.tcId}\`, ...) }` |
| Page Object usage | `loginPage().enterEmail(...)` | `await loginPage.enterEmail(...)` |
| Assertions | `assertEquals`, `assertTrue` (TestNG) | `await expect(locator).toHaveText(...)` (Playwright) |

## Agent Protocol

> Xem `review-agent/AGENT.md` §3b cho system prompt.

**Flow:**
```
Main Claude                          Reviewer Agent (API)
  │                                        │
  ├─ Parse TC-MASTER → TC steps/expected   │
  ├─ Read .java files → code content       │
  ├─ Pair TC ↔ test method                 │
  ├─ Serialize → JSON ──────────────→ Receive paired data
  │                                  ├─ Apply M1-M4 checks
  │                                  └─ Return findings JSON
  ├─ Receive JSON ←─────────────────┘
  ├─ Format report
  └─ Present to user
```

**Agent used when:** implement-automation §8 ≥ PARTIAL (code do AI tạo).
**Skip agent:** `--direct` flag hoặc code do human viết (implement-automation NOT_STARTED).

## Nguyên tắc

- **TC Excel là contract.** Code match TC, không ngược lại.
- **So sánh TỪNG step, TỪNG expected.** Không "tổng thể giống nhau".
- **KHÔNG sửa code.** Chỉ report.

## Status Protocol

§8 = COMPLETED. Output: `11_tc-review/src-tc-review-v[X].md`

## Examples

### Example 1: Full review
**Input:** `/review-src-tc`
**Behavior:**
1. Đọc TC-MASTER + scan all test classes
2. Pair TC ↔ test method via `// TC_01.1` comments (TC ID = giá trị cột A đã resolve, không tự đặt)
3. Call independent reviewer agent (M1-M4 checks)
4. Output `11_tc-review/src-tc-review-v[X].md` + Excel

**Output:** Match rate score (0-100), mismatch findings.

### Example 2: Module review
**Input:** `/review-src-tc --module Login`
**Behavior:** Filter Login TCs + LoginTest class only.

### Example 3: Per-member review (Team mode)
**Input:** `/review-src-tc --member member_A`
**Behavior:** Review TCs assigned to member_A only.

### Example 4: Recheck after fix
**Input:** `/review-src-tc --recheck`
**Behavior:** Re-run on previous Major findings, verify resolved.

## Common Edge Cases

| Scenario | Handling |
|----------|----------|
| No test classes | Block, suggest `/implement-automation` |
| TC count >> test method count | Report "not implemented" gap |
| Test method count > TC count | Report "orphan methods" (extra tests không trong TC) |
| **Test method count < TC count (comprehensive mode + parameterized)** | **(NEW 2026-05-29)** Verify `@DataProvider` size = derived TC count. Pattern OK — see `references/full.md` §"Comprehensive mode awareness" cho details. KHÔNG raise CRITICAL nếu §13 Implementation Log log TC ID range (e.g., `testFooBoundary` covers `TC_03.14..TC_03.20`). |
| **Filter `--member` không còn cột "Assigned To"** | **(2026-07-21)** Template ISC bỏ cột Assigned To. Dùng git author của file test làm fallback — xem `references/scope.md`. |
| TC comment format không chuẩn | Try fuzzy match (TC ID pattern), warn |
| Mixed Java + Python tests | Filter Java only (Python = vibe-test scope) |
| @Disabled / @Ignore tests | Skip, report as "Disabled" |
| Manual verify steps | Mark as `// MANUAL`, không required assertion |
| Independent reviewer API fail | Fallback direct review with disclaimer, score cap 85 |

