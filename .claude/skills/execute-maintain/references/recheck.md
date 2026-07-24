# Execute — Mode RECHECK

> `/execute-maintain --recheck FAIL-001` hoặc `/execute-maintain --recheck BUG-NNN`
> Playwright/Appium verify UI hiện tại so với locator trong code.

## Workflow

---

## 🚨 Step 0: DOC Re-validate (BẮT BUỘC — added 2026-05-28)

> **Trước khi chạy recheck trên bug/fail cũ, PHẢI verify current DOC còn support test assumption gốc.**
> Precedent: BUG-002 case 2026-05-28 — spec change Sprint 3 "Camera KHÔNG track RM" rendered original test obsolete, nhưng recheck copy-paste old repro vẫn ran for 17 days. Skill này should refuse that shortcut.

### Required steps before any actual test run:

For each bug/fail being rechecked:

1. **Read bug/fail context fully:**
   - Open `05_bug-reports/BUG-NNN-*.md` (if bug) hoặc Source MEMORY §16 entry (if FAIL)
   - Identify: Module · Endpoint · Entities tested (services, params, fields, screen_key)
   - Note: bug logged date · current date · days elapsed

2. **Read CURRENT active version DOC §relevant_section:**
   - Find DOC ID from `02_analyze-requirements/MASTER-MEMORY.md §2 Document Registry` for active version
   - Locate section covering the tested entities (e.g., §4.3 for cust_lost, §8 for Insight)
   - Read carefully — esp. "Notes", "Exclusions", "Backend fan-out", error catalogs

3. **Cross-check assumptions:**

   | Question | If YES | If NO |
   |----------|--------|-------|
   | Are tested entities still listed as valid in DOC whitelist? | proceed Step 1 below | ⚠️ Possible spec evolution — flag |
   | Has DOC added exclusion rules (e.g., "X KHÔNG do Y", "feature dropped")? | ⚠️ Test may be obsolete | proceed |
   | Has DOC marked feature DEPRECATED or moved to Coming Soon? | ⚠️ Stop, close as obsolete | proceed |
   | Did spec change date > bug logged date? | ⚠️ Triage needed | proceed |

4. **Decision matrix:**

   | DOC state vs bug | Action |
   |------------------|--------|
   | DOC fully supports test assumption | ✅ Proceed Step 1+ (actual recheck) |
   | DOC contradicts test assumption | ❌ **Close bug as FP (Spec Evolution)** — do NOT run test. Document closure reason citing DOC §section. |
   | DOC ambiguous / unclear | ⏸️ Ask user before running. List specific contradictions. |
   | DOC missing for that module | ⚠️ Log gap to clarifications. Proceed conservatively. |

### 🚫 BANNED behaviors:

| ❌ Don't | ✅ Do instead |
|----------|---------------|
| Copy-paste old bug repro steps and run blindly | Read current DOC §section FIRST, verify entities still valid |
| Trust bug status (Open, P1) as authoritative | Trust DOC as authoritative; bug status may be stale |
| Report "BUG STILL REPRODUCES" without checking spec | Report "Bug repro tested. DOC §X §Y verified. Verdict: [reproduces / FP / blocked]" |
| Suggest fix (mobile/backend change) based on bug repro alone | Suggest fix only after confirming DOC actually expects different behavior |

### Output format for Step 0 (mandatory in recheck report):

```markdown
## Step 0: DOC Re-validate (BUG-NNN)

| Check | Result |
|-------|--------|
| Bug logged date | 2026-MM-DD ([N] days ago) |
| Bug repro entities | screen_key=X, service=Y, ... |
| Active DOC | DOC-vX.Y.Z-NN (read date 2026-MM-DD) |
| DOC §relevant section | §X.Y "..." |
| Entities still valid per DOC? | ✅ Yes / ⚠️ Partial / ❌ No |
| Exclusion rules added since bug? | ✅ None / ⚠️ Found: "..." |
| Spec change since bug logged | None / Found in DOC-vX.Y.Z (added YYYY-MM-DD) |
| **Decision** | PROCEED RECHECK / CLOSE FP / ASK USER |
```

→ Only after Step 0 PROCEED outcome may proceed to Step 1+ below.

---

### Step 1: Đọc failure context
§16 → FAIL-001: page URL, element, locator strategy + value.

### Step 2: Playwright navigate + snapshot
```
browser_navigate(URL)    → page load
browser_snapshot()       → accessibility tree
browser_take_screenshot() → visual evidence
```

### Step 3: So sánh locator vs UI

| Scenario | Kết quả | Suggest |
|----------|---------|---------|
| Element found + locator match | "Locator valid. Lỗi có thể do timing/env." | Add explicit wait hoặc re-run |
| Element found + locator KHÁC | "Element đổi locator: cũ=[X], mới=[Y]" | `/implement-automation --update "locator [element] đổi thành [Y]"` |
| Element NOT found | "Element không tồn tại trên page" | UI thay đổi → check design |
| Page not loading | "Page timeout / redirect" | Env issue |

### Step 4: Present + evidence
```
🔄 Recheck — FAIL-001 (testLoginSSO)

URL: https://stg.example.com/login
Locator: @FindBy(id = "sso-google")

Result: ❌ Element NOT FOUND
Screenshot: [attached]
Accessibility tree: [no element matching 'sso-google']

Suggest: SSO button không có trên STG. Possible: feature chưa deploy.
→ /implement-automation --update "skip TC-LOGIN-010 (SSO not deployed)"
```

### Constraints
- Playwright CHỈ observe: navigate + snapshot + screenshot
- KHÔNG interact (click/type)
- KHÔNG sửa code
- KHÔNG suggest locator mới — chỉ report thực tế
