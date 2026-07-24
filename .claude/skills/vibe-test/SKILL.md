---
name: vibe-test
description: Thực thi TC-MASTER qua MCP (Playwright web / Appium mobile) — AI thay manual tester. Validate TC thực tế trên app, screenshot evidence per TC, capture locator data cho implement-automation tái sử dụng. Use when user mentions 'vibe test', 'chạy TC bằng browser', 'test TC trên web', 'test TC trên mobile', 'kiểm tra TC trước automate', 'manual test bằng AI', or runs /vibe-test, /vibe-web, /vibe-mobile commands.
license: Proprietary — FPT QA Toolkit v1.0 (qc-claude-v1)
compatibility: Designed for Claude Code QA projects with 00_..11_ folder structure (qc-claude-v1). Requires Claude Code or compatible agent runtime.
metadata:
  toolkit: qc-claude-v1
  pipeline-position: "7"
  status-section: MASTER-MEMORY-section-8
  owner: QC Team
  version: "1.1"
  released: "2026-06-05"
  updated: "2026-07-21 — align với template ISC: ghi kết quả trực tiếp vào cột Vibe-test/Kết quả/Executed By/ID Bugs theo round (N-AL) trong TC-MASTER thay vì chỉ MEMORY §4; round tự xác định theo block trống đầu tiên của mỗi TC row. Trước đó (2026-05-26): MCP-mandatory enforcement."
---

# Vibe Test

Đọc TC-MASTER → drive app qua **MCP (bắt buộc)** → thực hiện từng step → ghi pass/fail/blocked → chụp screenshot → **capture locator data** cho implement-automation.

**1 skill, 2 platforms:** web (Playwright MCP) + mobile (Appium MCP).

---

## 🚨 MCP MANDATORY RULE (NEW — added 2026-05-26)

> **Locator capture MUST go through MCP.** KHÔNG đoán, KHÔNG suy luận từ screenshot text, KHÔNG copy-paste từ memory cũ.

### Banned practices (sẽ làm sai locator + ảnh hưởng implement-automation)

| ❌ Không được làm | Lý do |
|------------------|-------|
| Suy đoán accessibility id từ text trong screenshot (e.g., thấy "Tài chính" → đoán `accessibility id "Tài chính"`) | Element thực có thể có content-desc khác, hoặc cùng text nhưng nhiều elements |
| Copy locator từ vibe-locators của run cũ mà không re-verify | Build mới có thể đã đổi accessibility id / xpath |
| Dùng coordinate tap (`adb input tap X Y`) để verify element exists | Coordinates không phải locator — dùng cho navigation lifecycle thôi |
| Đánh dấu `✅ Verified` nếu chưa gọi MCP extract page source | "Verified" implies MCP-confirmed; sai sẽ misleading implement-automation |
| Skip MCP session create vì "đã có ADB" | ADB không expose accessibility tree — không thay thế được MCP |

### Required for EVERY locator entry trong `vibe-locators.md`

| Field | Required source |
|-------|-----------------|
| Locator strategy | From MCP `appium_get_page_source` / `appium_find_element` / `browser_snapshot` |
| Locator value | EXACT string from MCP response (no paraphrasing) |
| Verified mark | ✅ **only if** MCP call succeeded for that specific element in this run |
| Action used | The MCP method called (`tap_element`, `browser_click`, `type_text`, etc.) |

### Verification mark legend (strict)

| Mark | Meaning |
|------|---------|
| ✅ Verified | MCP `find_element` succeeded + action executed successfully in this run |
| ⚠️ Inferred | Visible in screenshot but NOT MCP-confirmed (must be re-verified before implement-automation uses) |
| 🚫 NOT FOUND | MCP `find_element` returned no match (locator candidate doesn't exist on app) |
| ⏳ Pending | Listed in TC but not yet attempted this run |

### When MCP unavailable

```
Mobile MCP not connected → DO NOT proceed with locator capture.
Options (in order):
  1. Try MCP restart: appium_session_management(action=create)
  2. If still fail → mark run as MCP_UNAVAILABLE, capture only lifecycle (screenshots + logcat) via ADB
  3. ALL locator entries in this run marked ⚠️ Inferred (not ✅ Verified)
  4. Add disclaimer banner trong vibe-report.md + vibe-locators.md
```

---

## Command

| Command | Mode | Mô tả |
|---------|------|-------|
| `/vibe-test` | EXECUTE | Thực thi TC **pending** (⏳ chưa vibe-test / chưa PASS) — auto-detect platform. TC đã ✅ PASS run trước = bỏ qua |
| `/vibe-test --all` | EXECUTE | **Chạy lại TOÀN BỘ** TC trong scope, KỂ CẢ TC đã ✅ PASS (override mặc định pending; overwrite kết quả cũ). Kết hợp được với `--module`/`--priority`/`--web`/`--mobile` |
| `/vibe-test --web` | EXECUTE | Force web (Playwright MCP) |
| `/vibe-test --mobile` | EXECUTE | Force mobile (Appium MCP) |
| `/vibe-test --module Login` | EXECUTE | Filter module |
| `/vibe-test --tc TC_01.1,TC_01.2` | EXECUTE | TCs cụ thể — dùng đúng giá trị cột A đã resolve, không tự đặt |
| `/vibe-test --priority High` | EXECUTE | Chỉ Priority=High |
| `/vibe-test --retest TC_01.3` | RETEST | Test lại FAIL/BLOCKED (mặc định ghi đè round gần nhất — xem `references/retest.md`) |
| `/vibe-test --round N` | EXECUTE | Ép ghi vào round N cụ thể thay vì auto-detect round trống đầu tiên (dùng khi cả team đồng bộ bắt đầu 1 round test mới) |
| `/vibe-test --status` | STATUS | Xem tổng quan kết quả |

Aliases: `/vibe-web` = `/vibe-test --web`, `/vibe-mobile` = `/vibe-test --mobile`

## Vị trí trong Pipeline

```
generate-tc → review-tc → ★ vibe-test ★ → implement-automation
                           (validate TC)    (đọc locator data từ vibe-test)
                           (capture locators via MCP)
```

**Vai trò kép:**
1. **Validate TC** — TC có thực thi được trên app thật không?
2. **Capture locators via MCP** — byproduct cho implement-automation, tránh re-discover

## Prerequisites

| Cần có | Check |
|--------|-------|
| TC-MASTER-v[X].xlsx (alias file ISC chính thức — 42 cột, block Round 1-5) | generate-tc §8 ≥ PARTIAL |
| review-tc (khuyến nghị) | review-tc §8 = COMPLETED |
| **Web:** Playwright MCP **connected + verified responsive** | `--web` hoặc auto-detect · MUST call `browser_navigate` first |
| **Mobile:** Emulator/device online **+ Appium MCP session created** | `--mobile` hoặc auto-detect · MUST call `appium_session_management(action=create)` first |

**Pre-flight MCP check (BẮT BUỘC):**

```
Before executing any TC, verify MCP responsive:

Mobile:
  ├─ mcp__appium__select_device         → device picker OK?
  ├─ mcp__appium__appium_session_management(action=create) → session created?
  ├─ mcp__appium__appium_get_page_source → first page source dumped OK?
  └─ If ANY fails → abort, request user fix MCP before retry

Web:
  ├─ browser_navigate(base_url)          → load OK?
  ├─ browser_snapshot()                  → accessibility tree dumped OK?
  └─ If fails → abort or fallback to documented degraded mode
```

**Platform auto-detect:**
```
1. CLAUDE.md có env URL (https://...) → web
2. CLAUDE.md có appPackage → mobile
3. Cả hai → hỏi user
4. User chỉ định --web / --mobile → force
```

## Input / Output

| Input (ĐỌC) | Output (GHI) |
|-------------|-------------|
| TC-MASTER-v[X].xlsx | `08_test-runs/vibe/VR-[NNN]-[date]/vibe-report.md` |
| Version MEMORY (env URL) | `08_test-runs/vibe/VR-[NNN]-[date]/vibe-log.md` |
| CLAUDE.md (credentials) | `08_test-runs/vibe/VR-[NNN]-[date]/screenshots/*.png` |
| | `08_test-runs/vibe/VR-[NNN]-[date]/vibe-locators.md` |
| | `08_test-runs/vibe/VR-[NNN]-[date]/mcp-session-log.md` ★ NEW — proves MCP was used |
| | **`08_test-runs/vibe/vibe-locators-latest.md`** ★ merged/copied file cho implement-automation |
| | **TC-MASTER Excel — cột Vibe-test/Kết quả/Executed By/ID Bugs của round đang chạy (N-AL), per TC row** ★ nguồn thật, xem `references/execute.md` Step 7 |
| | Version MEMORY §4 (Vibe Status — cache đồng bộ từ Excel, KHÔNG còn là nguồn chính) |

**`mcp-session-log.md` requirement (NEW):** Mỗi run phải có file này, ghi lại:
- Session ID + create timestamp
- List of MCP calls made (e.g., `appium_get_page_source called 12x`)
- Pre-flight check result
- If MCP failed mid-run, exactly when

→ Implement-auto + reviewers có thể audit xem locators có thực sự MCP-verified hay không.

**Cấu trúc output:**
```
08_test-runs/
└── vibe/
    ├── vibe-locators-latest.md         ★ implement-automation reads THIS file
    ├── VR-001-2026-05-24/
    │   ├── vibe-report.md
    │   ├── vibe-log.md
    │   ├── vibe-locators.md            ← strict ✅/⚠️/🚫/⏳ marks
    │   ├── mcp-session-log.md          ★ NEW — proof of MCP usage
    │   └── screenshots/
    └── ...
```

**Run ID:** `VR-[NNN]` — auto-increment, never reuse.

**Folder sở hữu:** `08_test-runs/vibe/` (CHỈ folder này)

## Mode Routing

| Condition | → Load |
|-----------|--------|
| `--status` | `references/status.md` |
| `--retest` | `references/retest.md` |
| Default | `references/execute.md` |

## Locator Capture Workflow — MCP-MANDATORY

> Đây là điểm khác biệt lớn nhất so với manual test truyền thống.
> Locator capture **PHẢI** đi qua MCP — không có shortcut.

**File output:** `vibe-locators.md` — strict per-element verification mark.

### Per-element capture protocol

For EVERY element you interact with in a TC step:

```
STEP 1: Snapshot UI via MCP
  Mobile: appium_get_page_source() → full accessibility XML
  Web:    browser_snapshot() → accessibility tree
  
STEP 2: Find candidate element
  Mobile: appium_find_element(strategy="accessibility id", value="<from step text>")
  Web:    browser locator candidates from snapshot

STEP 3: Verify candidate
  Try the action (tap/type/get_text) — if MCP succeeds → ✅
  If element not found → mark 🚫 NOT FOUND with the strategy+value tried
  If multiple matches → log ambiguity, prefer most specific (id > accessibility id > xpath)

STEP 4: Record in locator registry with EXACT MCP-returned strings
  - No paraphrasing of locator value
  - No screenshot-based inference
  - Verified mark ✅ requires both find + action success in same TC
```

### `vibe-locators.md` template (strict format)

```markdown
# Vibe Locators — v[X] — VR-[NNN] — [date]

> Captured via [Playwright/Appium] MCP during this run.
> Mark legend: ✅ Verified · ⚠️ Inferred · 🚫 NOT FOUND · ⏳ Pending
> MCP session log: see mcp-session-log.md (audit trail)

## Page: Login (/login)

| Element | Action Used | Locator Strategy | Locator Value | Verified | MCP call ref |
|---------|------------|-----------------|---------------|----------|--------------|
| Email field | type | id | email-input | ✅ | appium_find_element #3 (success) |
| Password field | type | id | password-input | ✅ | appium_find_element #4 (success) |
| Login button | click | css | [data-testid='btn-login'] | ✅ | browser_click #5 (success) |
| SSO Google button | click | (tried: accessibility id "google-sso") | (not present) | 🚫 NOT FOUND | appium_find_element #7 (no match) |
| Tooltip overlay | hover | (tried: xpath //div[@role='tooltip']) | (not present) | 🚫 NOT FOUND | browser_locator #9 (timeout) |

## Page: Dashboard (/dashboard)

| Element | Action | Strategy | Value | Verified | MCP call ref |
|---------|--------|----------|-------|----------|--------------|

## Navigation Flow (only flows actually traversed via MCP)

| From | Trigger | To | Verified by |
|------|---------|-----|------------|
| /login | MCP click Login (success) | /dashboard | TC_01.1 step 4 |
| /login | MCP click Login (invalid) | /login (stay) | TC_01.2 step 4 |
```

**Banned in this file:**
- Bulk-imported locators from previous runs without re-verify
- Coordinate-based "locators" (X,Y tap is navigation, not locator capture)
- Elements marked ✅ Verified without corresponding `mcp-session-log.md` entry

## Nguyên tắc

- **TC-MASTER là script.** Thực hiện ĐÚNG từng step.
- **App thật = truth — but only through MCP.** Screenshot is evidence, not locator source.
- **MCP MANDATORY for locator capture.** ADB allowed for lifecycle (force-stop, am start, logcat) only.
- **Kết quả trung thực.** PASS / FAIL / BLOCKED — không bào chữa.
- **Screenshot bắt buộc** step cuối mỗi TC + tại step FAIL/BLOCKED.
- **Locator capture qua MCP** — không tự động magic, làm thủ công per element.
- **KHÔNG tạo code.** KHÔNG tạo Page Object / Test class / Screen class.

## Platform Action Reference

| Action | Web (Playwright MCP) | Mobile (Appium MCP) | ADB (lifecycle ONLY — NOT locator) |
|--------|----------------------|---------------------|-----------------------------------|
| Launch app | `browser_navigate(url)` | `appium_app_lifecycle(launch)` | `adb shell am start` ✓ |
| Force-stop | (browser close) | `appium_app_lifecycle(terminate)` | `adb shell am force-stop` ✓ |
| **Snapshot accessibility tree** | `browser_snapshot()` | `appium_get_page_source()` | ❌ NOT EQUIVALENT — `uiautomator dump` is read-only static |
| **Find element** | accessibility tree match | `appium_find_element(strategy, value)` | ❌ NOT EQUIVALENT |
| **Click/tap** | `browser_click(ref)` | `appium_gesture(action=tap, element_id)` | ⚠️ `adb input tap X Y` — works but doesn't validate element |
| **Type** | `browser_type(ref, text)` | `appium_set_value(element_id, text)` | ⚠️ `adb input text` — bypasses element validation |
| Screenshot | `browser_take_screenshot()` | `appium_screenshot()` | ✓ `adb screencap` (evidence only) |
| Logcat / network | (browser console) | (via Appium driver settings) | ✓ `adb logcat` (debug only) |

**Rule:** Use Appium/Playwright MCP for ANY action that involves a UI element. Use ADB only for app lifecycle (start/stop) + non-element-specific evidence capture (screenshot, logcat). If you need to know an element exists/works, call MCP.

## Status Protocol

§8 = PARTIAL (đang chạy) → COMPLETED (tất cả TC scope đã vibe-test).
Notes example: "12P/1F/2B, MCP locators verified: 35 elements, MCP calls: 87"

## Examples

### Example 1: Execute all TCs (proper MCP-mandatory flow)

**Input:** `/vibe-test --mobile --module HR`

**Behavior:**
1. Pre-flight: `select_device` → `appium_session_management(action=create)` → `appium_get_page_source` (verify responsive)
2. If pre-flight fails → abort with clear error; offer ADB-degraded mode as opt-in
3. Filter HR sheet, drive emulator via Appium MCP
4. For each TC step → snapshot → find_element → action → screenshot
5. Locators captured strictly per protocol with ✅/🚫 marks
6. `mcp-session-log.md` records every MCP call
7. Output: `08_test-runs/vibe/VR-001-[date]/` với 4 files + screenshots

### Example 2: Specific TCs

**Input:** `/vibe-test --tc TC_01.1,TC_01.2`
**Behavior:** Pre-flight MCP check → run 2 TCs only with strict MCP capture.

### Example 3: Retest blocked TC

**Input:** `/vibe-test --retest TC_01.3`
**Behavior:** Same pre-flight + MCP requirements as full run. Cannot retest in degraded mode.

### Example 4: Status overview (no MCP needed)

**Input:** `/vibe-test --status`
**Behavior:** Inline summary from latest run logs — MCP not invoked.

### Example 5: MCP unavailable → degraded run (explicit user opt-in)

**Input:** User asks to continue after pre-flight MCP fail

**Behavior:**
- Banner in report: "⚠️ MCP UNAVAILABLE — locators all marked ⚠️ Inferred"
- Lifecycle screenshots + logcat captured via ADB
- No ✅ Verified marks allowed in `vibe-locators.md`
- Implement-auto WILL need to re-verify all locators before using

### Example 6: Re-run toàn bộ (kể cả TC đã PASS)

**Input:** `/vibe-test --all --module Login`
**Behavior:** Bỏ qua filter pending → chạy lại MỌI TC của module Login (cả TC đã ✅ PASS), vẫn pre-flight MCP + capture lại locator như run thường, **overwrite** Vibe Status §4. Dùng khi app deploy lại / muốn refresh toàn bộ locator. (Không kèm `--module` → chạy lại toàn bộ TC-MASTER.)

## Common Edge Cases

| Scenario | Handling |
|----------|----------|
| MCP server disconnected pre-flight | Abort, instruct user restart MCP. **Do NOT silently fallback to ADB-only.** |
| MCP works pre-flight but fails mid-run | Save partial results, mark remaining TCs as MCP_INTERRUPTED, log timestamp in mcp-session-log.md |
| Platform auto-detect ambiguous | Hỏi user `--web` hoặc `--mobile` |
| TC steps không match app reality | Mark FAIL, MCP snapshot to evidence, suggest TC update |
| Element NOT FOUND (MCP returns empty) | Mark 🚫 + record exact strategy+value tried in vibe-locators |
| App crashed mid-test | Restart app via MCP, retry current TC, log warning + new MCP session if needed |
| Login required nhưng credentials thiếu | Ask user run `! source <env-file>` in session (e.g. `! source ~/.dashboard-report/credentials.env`). KHÔNG echo password, KHÔNG inline `SSO_PASSWORD="..."` vào command, KHÔNG read & copy file content vào context. |
| Network timeout (slow app load) | Extend MCP wait, retry once, fail if persistent |
| Visual-only test (no element assertion) | Screenshot + mark "manual verify required" — but still snapshot accessibility tree if any text needs verify |
| Test data dynamic (e.g., current date) | Use real-time data, document in vibe-log |
| Multi-step navigation broken | Skip subsequent steps, mark BLOCKED at step N, capture last MCP snapshot |
| User asks "đoán locator nhanh cho tôi" / "skip MCP cho run này" | Politely refuse — explain banned practices section + offer degraded mode with ⚠️ marks |
| TC đã dùng hết 5 round (N-AL đều có dữ liệu) | KHÔNG tự mở round 6 — báo lỗi, suggest bump Version TC hoặc liên hệ QA lead, skip TC đó, tiếp tục TC khác |
| TC-MASTER thiếu sheet/không đúng format template ISC (file build từ schema cũ) | DỪNG, suggest `/generate-tc --consolidate` từ template gốc trước khi vibe-test |
| Nhiều TC trong cùng run rơi vào round khác nhau (TC đã test nhiều lần trước, TC khác chưa) | Bình thường — round xác định per-TC-row, không đồng bộ toàn run trừ khi dùng `--round N` |
| Bug vừa log nhưng chưa `--push-jira` (chưa có jira_key) | Ghi `BUG-NNN` tạm vào cột ID Bugs, log-bug sẽ tự cập nhật thành jira_key sau khi push |
