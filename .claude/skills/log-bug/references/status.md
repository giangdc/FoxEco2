# Log Bug — Mode STATUS

> `/log-bug --status`

Đọc bug-index.md → trình bày: by version, by module, by severity, by status.

---

## Workflow

### Step 1: Parse `05_bug-reports/bug-index.md`

Build in-memory bug list với fields: ID, Version, Priority, Status, Reported date, Module, Owner.

### Step 2: Compute aggregations

- By Priority × Status (count matrix)
- By Version (rows per version)
- By Owner (workload distribution)

### Step 3: 🔥 Aging Report (NEW — added 2026-05-28)

> Bugs Open quá lâu mà chưa recheck = warning sign. Có thể stale (spec evolved) hoặc forgotten.
> Precedent: BUG-002 sat 17 days Open carry-over qua 4 sprints. Spec change Sprint 3 ("Camera KHÔNG track RM") rendered it FP, nhưng no review flagged it. Aging report would have surfaced this.

For each bug status = `Open` or `New`:

1. Compute `days_open = today - reported_date`
2. Severity escalation:

| Age | Severity tag | Action suggestion |
|-----|--------------|-------------------|
| ≤ 7 days | (no flag) | Normal triage cadence |
| **8-14 days** | 🟡 INFO `Stale — review trong sprint hiện tại` | Add to next standup |
| **15-30 days** | 🟠 WARNING `May be spec-obsolete — re-validate vs current DOC` | `/analyze-requirements --review` + `/execute-maintain --recheck BUG-NNN` |
| **> 30 days** | 🔴 CRITICAL `Likely obsolete — triage required before next release GO` | Block GO decision until manually closed or fixed |

3. Suggest specific skills to invoke:
   - **Spec evolution check:** `analyze-requirements --review` cho module affected
   - **Recheck:** `execute-maintain --recheck BUG-NNN` (will MANDATE Step 0 DOC re-validate per execute-maintain v4.1+)
   - **Manual close FP:** `log-bug --close BUG-NNN` nếu test obsolete

### Step 4: Output format

```
🐛 Bug Status — [date]

## Overall (from bug-index.md)
| Priority | Open | Partial | Fixed | False Pos | Total |

## Active Production Blockers
(list P1 + P2 Open with version + module + owner)

## 🔥 Aging Report
🟡 INFO (8-14 days):
  BUG-NNN · Module · X days Open · suggest: <skill>
🟠 WARNING (15-30 days):
  BUG-NNN · Module · X days · last reviewed [date] · suggest: re-validate vs DOC §X
🔴 CRITICAL (> 30 days):
  BUG-NNN · Module · X days · NO sprint touched · BLOCK GO until triaged

## By Version
(rows v1.0 → vX.Y count + status)

## Recommendations
1. [most urgent action]
2. [next]
```

### Step 5: Trigger downstream skill suggestions

If any 🟠/🔴 aging bugs surfaced:
- Prompt user: "Re-validate aging bugs? (Y/N)"
- If Y → suggest running `execute-maintain --recheck` cho each (will go through Step 0 DOC verify automatically)
- If N → log to MASTER-MEMORY §8 Notes: "log-bug --status surfaced N aging bugs, user deferred re-validate"

---

## Checklist

- [ ] Parsed bug-index.md complete
- [ ] Aggregations computed (by priority, version, owner)
- [ ] Aging report ran (compute days_open per Open bug)
- [ ] Severity tags applied (INFO 8-14d / WARNING 15-30d / CRITICAL >30d)
- [ ] Skill suggestions printed for each aged bug
- [ ] User prompted re-validate workflow if any 🟠/🔴 found
- [ ] §8 Pipeline Status Notes updated if user defers

---

## Example output

```
🐛 Bug Status — 2026-05-28

## Overall
| Priority | Open | Fixed | False Pos | Total |
| P1       | 0    | 1     | 3         | 4     |
| P2       | 0    | 0     | 1         | 1     |  (+ 1 Partial)
| P3       | 3    | 0     | 2         | 5     |

## Active Production Blockers
(none — all P1 cleared 2026-05-28)

## 🔥 Aging Report

🟡 INFO (8-14 days):
  BUG-007: 8 days Open · QA framework flake · suggest /execute-maintain --recheck
  BUG-008: 8 days Open · QA framework flake · suggest /execute-maintain --recheck

🟠 WARNING (15-30 days):
  BUG-001: 17 days partial Open · Backend region_16 · suggest /analyze-requirements --review + /execute-maintain --recheck

🔴 CRITICAL (> 30 days):
  (none)

## Recommendations
1. Backend team triage BUG-001 partial (17 days aging) — defensive deadline before next release
2. Schedule flake retry cycle for BUG-007/008 next sprint
```
