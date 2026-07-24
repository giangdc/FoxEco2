# Vibe Test — Mode EXECUTE

> `/vibe-test` | `/vibe-test --web --module Login` | `/vibe-test --mobile --tc TC_01.1`
> **MCP MANDATORY** for locator capture — see SKILL.md §"🚨 MCP MANDATORY RULE"

## Workflow

### Step 1: Đọc context + guard

```
1. PIPELINE.md → check generate-tc ≥ PARTIAL
2. MASTER-MEMORY §8 → recommend review-tc COMPLETED
   - review-tc chưa chạy → ⚠️ "TC chưa review. Tiếp tục?"
3. Parse TC-MASTER (openpyxl, data_only=True cho giá trị formula đã resolve — cột A/AM/AN/AO) →
   danh sách TCs theo scope (--module, --tc, --priority)
   ⚠️ **Row label Screen/Block KHÔNG phải TC — BẮT BUỘC loại khỏi danh sách trước khi lọc scope.**
   Sheet Test Cases có thể chèn row label Screen/Block xen giữa row TC (`generate-tc/references/
   generate.md` Step 6.4 — Screen: merge A:I; Block: merge B:I). Nhận diện: cột A (Testcase ID) rỗng
   = row label, không phải TC → bỏ qua hoàn toàn (không execute, không ghi round data vào row đó).
   Lọc STATUS — nguồn thật là Excel (cột AM Vibe-test tổng + cột AO Status), Version MEMORY §4 chỉ
   là cache đọc nhanh, KHÔNG dùng làm nguồn quyết định:
     • Mặc định       → CHỈ TC pending (cột AO Status ≠ "Pass"); TC đã Pass ở round mới nhất = bỏ qua
     • `--all`        → GỒM CẢ TC đã Pass — chạy lại toàn bộ scope từ đầu (ghi vào round trống tiếp
                         theo, xem 3b — KHÔNG ghi đè round cũ, "chạy lại" = thêm 1 round mới)
     • (`--retest` là mode riêng cho FAIL/BLOCKED — xem references/retest.md, mặc định ghi đè round
        gần nhất thay vì mở round mới — xem lý do trong file đó)
3b. **Xác định round đích cho MỖI TC row** (block 5 cột N-R/S-W/X-AB/AC-AG/AH-AL trong Test Cases sheet):
   - Mặc định: quét round 1→5 của TC row đó, chọn round ĐẦU TIÊN có cột "Kết quả" còn trống. TC
     khác nhau trong cùng 1 run CÓ THỂ rơi vào round khác nhau (tuỳ TC đó đã được test bao nhiêu lần).
   - `--round N`: ép toàn bộ TC trong scope ghi vào round N (dùng khi cả team đồng bộ mở 1 round test
     mới) — nếu round N của 1 TC nào đó ĐÃ có dữ liệu, hỏi user xác nhận ghi đè trước khi tiếp tục.
   - Cả 5 round (N→AH) đã đầy cho 1 TC → KHÔNG ghi được nữa, báo lỗi rõ: "TC_[x] đã dùng hết 5 round
     — cần tăng Version TC (bump theo Guideline sheet mục 5) hoặc liên hệ QA lead", skip TC đó, tiếp
     tục các TC khác trong scope.
4. Detect platform: --web / --mobile / auto
5. Xác định Run ID: VR-[NNN] (auto-increment từ runs trước trong 08_test-runs/vibe/)
6. Tạo folder: 08_test-runs/vibe/VR-[NNN]-[date]/screenshots/
7. **Tạo mcp-session-log.md** (MCP audit trail file — write each MCP call)
8. Ghi §8 = IN_PROGRESS
```

### Step 1.5: 🚨 MCP PRE-FLIGHT (BẮT BUỘC — bỏ qua = run invalidated)

**Mobile:**
```
Call (in order, log each to mcp-session-log.md):
  1. mcp__appium__select_device         → verify device picker returns emulator/device
  2. mcp__appium__appium_session_management(action=create)
                                         → session_id captured, log in mcp-session-log
  3. mcp__appium__appium_get_page_source → first snapshot OK?
  4. mcp__appium__appium_get_window_size → confirm responsive

Pass criteria: ALL 4 calls return without error.

Fail → STOP run. Options for user:
  (a) Restart Appium MCP server, retry
  (b) Continue in DEGRADED mode (no ✅ Verified locators allowed)
  (c) Abort and run /health-check để diagnose
```

**Web:**
```
Call (in order):
  1. browser_navigate(base_url) → page loaded
  2. browser_snapshot() → accessibility tree retrieved

Fail → same options as mobile.
```

### Step 2: Khởi tạo platform adapter

**Web (MCP only):**
```
browser_navigate(base_url)
browser_take_screenshot() → verify trang load (this is evidence, not locator)
browser_snapshot() → accessibility tree (foundation cho locator capture)
```

**Mobile (MCP required, ADB lifecycle helper):**
```
✅ MCP (required for locator work):
   appium_app_lifecycle(action=launch, app_id=<package>)
   appium_get_page_source() → first UI tree snapshot
   
⚠️ ADB OK ONLY for lifecycle:
   adb shell am force-stop <package>  → cleanup between TCs
   adb shell am start -n ...           → if MCP launch fails (last resort)
   adb logcat -d                       → debug evidence
   adb screencap                       → snapshot file (evidence, NOT locator source)
   
❌ ADB NOT acceptable substitute for locator capture:
   adb input tap X Y                   → coordinate tap, NOT element find
   adb uiautomator dump                → static XML, không match MCP semantics
```

**Login nếu cần** (từ TC Precondition):
```
→ Thực hiện login steps
→ Screenshot after login
→ Ghi locator login elements vào vibe-locators.md
```

### Step 3: Thực thi từng TC — vòng lặp chính

```python
locator_registry = {}    # accumulate locators across TCs
tc_results = []          # accumulate results

for tc in tc_list:
    result = execute_single_tc(tc)
    tc_results.append(result)
```

#### execute_single_tc(tc):

```
Với MỖI STEP trong TC:

  1. ĐỌC step text: "Nhập 'user@test.com' vào field Email"
  
  2. 🚨 SNAPSHOT UI via MCP (BẮT BUỘC — log call):
     Web:    browser_snapshot()       → accessibility tree
     Mobile: appium_get_page_source() → UI tree XML
     → Append entry to mcp-session-log.md
  
  3. 🚨 TÌM ELEMENT qua MCP find_element (BẮT BUỘC):
     Web:    locate trong snapshot using accessibility selector
     Mobile: appium_find_element(strategy="accessibility id" | "id" | "xpath", value="<candidate>")
     
     Verify result:
       ├─ MCP returns matching element → ✅ locator candidate confirmed
       ├─ MCP returns empty → 🚫 mark NOT FOUND with exact strategy+value tried
       └─ MCP returns multiple matches → log ambiguity, prefer most specific
     
     ★ CAPTURE LOCATOR (only after MCP confirms):
     locator_registry[page][element_name] = {
         strategy: "<from MCP, exact>",
         value: "<from MCP, exact — no paraphrasing>",
         action: "<MCP method to be called next>",
         verified: True,
         mcp_call_ref: "<line number in mcp-session-log.md>",
         date: today
     }
     
     ❌ FORBIDDEN: Inferring locator from screenshot text
        e.g., screenshot shows "Tài chính" → ❌ do NOT assume accessibility id == "Tài chính"
        MUST call appium_find_element + verify before recording
  
  4. 🚨 THỰC HIỆN ACTION qua MCP (BẮT BUỘC):
     Web:    browser_click(ref) / browser_type(ref, "user@test.com")
     Mobile: appium_gesture(action=tap, element_id=<from step 3>)
             OR appium_set_value(element_id, "user@test.com")
     
     If MCP action succeeds AND step 3 found element → element fully ✅ Verified
     If MCP action fails → mark step BLOCKED, downgrade element to ⚠️ Inferred
     
     ❌ FORBIDDEN: Using `adb input tap X Y` as substitute
        - Coordinate tap proves nothing about element identity
        - Only OK for navigation (e.g., bottom nav lifecycle) — but then no ✅ locator recorded
     
  5. GHI KẾT QUẢ STEP + MCP audit:
     - PASS: action thành công, UI respond đúng + MCP call references logged
     - FAIL: action thành công nhưng kết quả sai expected
     - BLOCKED: MCP find_element returned no match → no ✅ Verified locator recorded

Với MỖI EXPECTED trong TC:

  1. ĐỌC expected: "Redirect về trang Dashboard"
  
  2. VERIFY:
     Web:    browser_snapshot() → check URL, check element visible
     Mobile: list_elements_on_screen() → check screen content
     
     ★ CAPTURE LOCATOR cho verify elements:
     locator_registry[page][element_name] = {
         strategy: "css",
         value: ".dashboard-header",
         action: "verify_visible",
         verified: True
     }
  
  3. GHI KẾT QUẢ:
     - PASS: actual match expected
     - FAIL: actual ≠ expected → ghi cả actual value

★ SCREENSHOT CUỐI TC (bắt buộc):
  browser_take_screenshot() / take_screenshot()
  → Save: screenshots/TC_01.1_final.png
```

#### Xử lý step results:

| Kết quả | Hành động | Tiếp tục? |
|---------|-----------|-----------|
| PASS | Ghi log, tiếp step tiếp | ✅ Tiếp |
| FAIL | Screenshot + ghi expected vs actual | ✅ Cố gắng tiếp (trừ khi step sau phụ thuộc) |
| BLOCKED | Screenshot + ghi lý do + capture "NOT FOUND" vào locator registry | ❌ Dừng TC, skip steps còn lại |

### Step 4: Ghi vibe-locators.md + mcp-session-log.md

Sau khi chạy xong TẤT CẢ TCs → aggregate locator_registry → ghi 3 files:

**File 1:** `08_test-runs/vibe/VR-[NNN]-[date]/vibe-locators.md` (locators của run này — strict ✅/⚠️/🚫/⏳)
**File 2:** `08_test-runs/vibe/VR-[NNN]-[date]/mcp-session-log.md` ★ NEW (MCP audit trail — proves capture method)
**File 3:** `08_test-runs/vibe/vibe-locators-latest.md` (merge/copy → implement-automation đọc file NÀY)

```markdown
# Vibe Locators — v[X] — VR-[NNN] — [date]

> Captured via [Playwright/Appium] MCP during this run.
> Mark legend: ✅ Verified (MCP find+action OK) · ⚠️ Inferred · 🚫 NOT FOUND · ⏳ Pending
> MCP session log: see mcp-session-log.md (audit trail)
> Platform: [web / mobile]

## Page: Login (/login)

| Element | Action Used | Strategy | Value | Verified | MCP call ref | TC refs |
|---------|------------|----------|-------|----------|--------------|---------|
| Email field | type | id | email-input | ✅ | mcp-log line 12 | TC_01.1, TC_01.2 |
| Password field | type | id | password-input | ✅ | mcp-log line 14 | TC_01.1, TC_01.2 |
| Login button | click | css | [data-testid='btn-login'] | ✅ | mcp-log line 16 | TC_01.1~005 |
| Error msg | verify | css | .error-message | ✅ | mcp-log line 21 | TC_01.2~005 |
| SSO button | click | (tried: accessibility id "google-sso") | (not present) | 🚫 NOT FOUND | mcp-log line 35 | TC_01.10 |

## Page: Dashboard (/dashboard)
...

## Navigation Flow (only MCP-traversed flows)

| From | Trigger | To | MCP-verified |
|------|---------|-----|--------------|
| /login | MCP click Login (valid) | /dashboard | TC_01.1 step 4 |
| /login | MCP click Login (invalid) | /login (stay) | TC_01.2 step 4 |
```

**mcp-session-log.md template:**

```markdown
# MCP Session Log — VR-[NNN] — [date]

## Session info
- Platform: mobile (Appium MCP)
- Device: emulator-5554
- Session ID: [from appium_session_management response]
- Created: HH:MM:SS
- Pre-flight: ✅ select_device + create + get_page_source all OK

## Call history

| # | Time | MCP method | Args (summary) | Result | Note |
|--:|------|-----------|----------------|--------|------|
| 1 | 10:00:01 | select_device | emulator-5554 | OK | Pre-flight |
| 2 | 10:00:02 | appium_session_management | action=create | OK sid=abc123 | Pre-flight |
| 3 | 10:00:05 | appium_get_page_source | — | OK 1842 bytes | Pre-flight |
| 4 | 10:00:08 | appium_get_window_size | — | 1280x2856 | Pre-flight |
| 5 | 10:00:15 | appium_get_page_source | — | OK 2103 bytes | TC_01.1 step 1 |
| 6 | 10:00:17 | appium_find_element | strategy=id, value=email-input | OK eid=xyz | TC_01.1 step 2 capture |
| 7 | 10:00:18 | appium_set_value | eid=xyz, text=user@test.com | OK | TC_01.1 step 2 action |
| ... | | | | | |
| N | 10:08:30 | appium_session_management | action=terminate | OK | Cleanup |

## Statistics
- Total MCP calls: [N]
- find_element calls: [N] (success: X, NOT FOUND: Y)
- get_page_source calls: [N]
- Action calls (click/type): [N]
- ⚠️ Any failures: list timestamps
```

**Required:** `vibe-locators.md` `MCP call ref` column MUST reference an entry in `mcp-session-log.md`. Locator entry without matching log entry → invalid, downgrade ✅ → ⚠️ Inferred.

**Giá trị cho implement-automation:**
- Locator ✅ → dùng trực tiếp: `@FindBy` (web Selenium-Java) · `@AndroidFindBy` (mobile Appium) · `page.locator()`/`getByTestId`/`getByRole` (web Playwright-TS — map từ Strategy: `id`→`#id`/testId, `css`→`locator()`, `text`/`role`→`getByText`/`getByRole`)
- Locator ❌ NOT FOUND → implement-automation skip, không tốn thời gian
- Navigation flow → biết page transitions, tạo đúng Page/Screen classes
- TC refs → biết locator dùng trong TC nào, phạm vi ảnh hưởng khi locator thay đổi

### Step 5: Ghi vibe-log chi tiết

Output: `08_test-runs/vibe/VR-[NNN]-[date]/vibe-log.md`

```markdown
# Vibe Test Log — VR-[NNN] — v[X] — [date]

## TC_01.1: Kiểm tra đăng nhập thành công

| # | Step | Action | Result | Notes |
|---|------|--------|--------|-------|
| 1 | Truy cập /login | navigate → OK | ✅ PASS | — |
| 2 | Nhập 'user@test.com' → Email | type(#email-input) | ✅ PASS | Locator: id=email-input |
| 3 | Nhập 'Test@123' → Password | type(#password-input) | ✅ PASS | Locator: id=password-input |
| 4 | Nhấn Đăng nhập | click([data-testid='btn-login']) | ✅ PASS | — |
| E1 | Redirect → Dashboard | URL = /dashboard ✓ | ✅ PASS | — |

**Result: ✅ PASS (4 steps, 1 expected)**
**Screenshot:** TC_01.1_final.png
**Locators captured:** 4 elements

---

## TC_01.3: Kiểm tra đăng nhập SSO

| # | Step | Action | Result | Notes |
|---|------|--------|--------|-------|
| 1 | Truy cập /login | navigate → OK | ✅ PASS | — |
| 2 | Nhấn "Đăng nhập Google" | ❌ element not found | 🚫 BLOCKED | snapshot: không có button SSO |
| 3-4 | — | — | ⏭ SKIPPED | blocked at step 2 |

**Result: 🚫 BLOCKED at Step 2**
**Reason:** SSO button không tồn tại trên STG
**Screenshot:** TC_01.3_step2_BLOCKED.png
**Impact:** KHÔNG automate TC này. Chờ SSO deploy.
```

### Step 6: Tổng hợp vibe-report

Output: `08_test-runs/vibe/VR-[NNN]-[date]/vibe-report.md`

```markdown
# Vibe Test Report — VR-[NNN] — v[X] — [date]

> Platform: [web / mobile]
> Environment: [URL / app package]
> Total TCs: [N]

## Summary

| Result | Count | % |
|--------|-------|---|
| ✅ PASS | [N] | [%] |
| ❌ FAIL | [N] | [%] |
| 🚫 BLOCKED | [N] | [%] |

## Locator Coverage

| Pages visited | Elements captured | Verified ✅ | Not found ❌ |
|--------------|------------------|------------|-------------|
| [N] | [N] | [N] | [N] |

→ implement-automation có thể bắt đầu với [N] locators đã verified.

## Blocked TCs — ⚠️ KHÔNG automate

| TC ID | Blocked at | Reason | Impact |
|-------|-----------|--------|--------|

## Failed TCs — Cần review TC hoặc fix app

| TC ID | Failed at | Expected | Actual |
|-------|----------|----------|--------|

## Passed TCs — Sẵn sàng implement automation

| TC ID | Steps | Locators captured | Screenshot |
|-------|-------|------------------|-----------|

## Recommendation

- **Automate now:** [N] TCs — locators ready trong vibe-locators.md
- **Fix TC first:** [N] TCs — sửa expected hoặc steps
- **Wait for app:** [N] TCs — feature chưa deploy / bug cần fix
```

### Step 7: Ghi kết quả vào TC-MASTER (Excel — nguồn thật) + MEMORY (cache)

**7a. Ghi trực tiếp vào round block xác định ở Step 3b, cho MỖI TC đã chạy trong round đó** (sheet
Test Cases/Test Case N tương ứng, đúng row của TC):

| Cột trong block round | Giá trị ghi |
|---|---|
| Vibe-test | `Yes` (TC này chạy qua vibe-test — LUÔN `Yes`, đây chính là cột đánh dấu AI-assisted exploratory testing) |
| KQ Script | **KHÔNG ghi** — cột này dành riêng cho kết quả chạy automation script (execute-maintain), vibe-test không đụng vào, để nguyên `Chưa chạy`/trống |
| Kết quả | `Pass` / `Fail` / `Block` — map trực tiếp từ PASS/FAIL/BLOCKED của vibe-test run |
| Executed By | Email PIC — đọc `Summary!C13` (PIC mặc định) hoặc `--executed-by <email>` nếu user chỉ định. KHÔNG ghi "AI"/"vibe-test" vào đây — Guideline sheet yêu cầu định dạng email; việc chạy qua AI đã được đánh dấu ở cột Vibe-test |
| ID Bugs | Nếu Kết quả = `Fail`: ghi Bug ID cục bộ (`BUG-[NNN]`) ngay sau khi `/log-bug` tạo xong. Khi `/log-bug --push-jira` chạy xong và có `jira_key`, log-bug cập nhật LẠI ô này thành `jira_key` (thay cho `BUG-NNN`) — xem `log-bug/references/sync-excel.md`. Nếu Block/Pass → để trống. |

Cột A (Testcase ID)/AM/AN/AO là formula — **KHÔNG ghi**, tự động rollup sau khi ghi 5 cột trên.

**7b. KHÔNG BAO GIỜ ghi vào round khác round đã xác định ở Step 3b** — mỗi round là 1 lần test độc
lập; ghi nhầm round sẽ làm rollup Status/Dashboard/RTM tính sai.

**7c. Version MEMORY §4 — Vibe Status column (cache, đồng bộ theo, KHÔNG phải nguồn chính):**

| SC ID | ... | TC Status | Vibe Status | Vibe Date |
|-------|-----|-----------|-------------|-----------|
| SC-LOGIN-001 | ... | ✅ | ✅ PASS (R2) | 2026-05-24 |
| SC-LOGIN-003 | ... | ✅ | 🚫 BLOCKED (R1) | 2026-05-24 |

> Ghi rõ round trong Vibe Status để tránh nhầm lẫn khi TC đã qua nhiều round. Nếu Excel và MEMORY
> lệch nhau (vd health-check phát hiện) → **Excel luôn thắng**, sửa lại MEMORY theo Excel.

**MASTER-MEMORY §8:**
```
| vibe-test | COMPLETED | 2026-05-24 | v2.0, VR-001, 15 TCs, Round 2 | 12P/1F/2B, 35 locators | web |
```

### Step 8: Present + handoff

```
✅ Vibe test VR-[NNN] hoàn tất (v[X]):

📊 Results: 12 PASS | 1 FAIL | 2 BLOCKED
🔍 Locators: 35 elements verified trên 4 pages
📁 Run folder: 08_test-runs/vibe/VR-[NNN]-[date]/
📎 Locators latest: 08_test-runs/vibe/vibe-locators-latest.md

Automate (12 TCs, locators ready):
  /implement-automation --module Login
  → implement-automation đọc vibe-locators-latest.md — KHÔNG cần mở Playwright lại

Fix first (1 TC):
  TC_01.5 → /analyze-requirements --update "Expected text tiếng Anh"

Wait (2 TCs):
  TC_01.3: SSO chưa deploy
  TC_02.8: API lỗi 500
```

---

## Checklist

- [ ] TC-MASTER parsed
- [ ] **MCP pre-flight passed** (Step 1.5 — 4 calls all OK for mobile, 2 for web)
- [ ] **mcp-session-log.md created** với session ID + timestamp
- [ ] Platform adapter initialized via MCP (NOT ADB-only)
- [ ] Run folder tạo: `08_test-runs/vibe/VR-[NNN]-[date]/`
- [ ] Mỗi TC: thực hiện từng step qua **MCP find_element + action**
- [ ] Mỗi TC: screenshot step cuối (BẮT BUỘC — via MCP `take_screenshot`)
- [ ] Mỗi FAIL/BLOCKED: screenshot tại step lỗi
- [ ] **Mỗi locator entry: MCP call ref column populated**
- [ ] Locator data → `VR-[NNN]/vibe-locators.md` với strict ✅/⚠️/🚫/⏳ marks
- [ ] **`vibe-locators.md` ✅ entries match `mcp-session-log.md` rows** (audit trail intact)
- [ ] vibe-locators-latest.md updated (merge, preserving verification marks)
- [ ] vibe-report + vibe-log tạo trong run folder
- [ ] **Round đích xác định đúng cho từng TC (Step 3b)** — round đầu tiên còn trống, hoặc round chỉ định qua `--round N`
- [ ] **TC-MASTER: cột Vibe-test=Yes + Kết quả + Executed By (+ ID Bugs nếu Fail) đã ghi đúng round** — KHÔNG đụng cột A/AM/AN/AO (formula) hay cột KQ Script (thuộc execute-maintain)
- [ ] Version MEMORY §4 Vibe Status cập nhật (cache, kèm số round) — khớp với Excel
- [ ] §8 = COMPLETED (Notes phải bao gồm số MCP calls và % ✅ Verified)
- [ ] KHÔNG tạo code / Page Object / Test class
- [ ] **❌ KHÔNG đoán locator từ screenshot text** (banned per SKILL.md)
- [ ] **❌ KHÔNG copy locator từ run cũ mà không re-verify qua MCP** (banned)
- [ ] **❌ KHÔNG dùng `adb input tap` thay thế cho `appium_gesture`** (banned ngoại trừ navigation lifecycle)
