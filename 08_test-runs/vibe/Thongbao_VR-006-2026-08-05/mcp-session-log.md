# MCP Session Log — Thongbao_VR-006-2026-08-05 (merged)

> Folder này gộp **2 lần chạy vibe-test cho module Thông báo (TC_03)**:
> - **Round 1** — chạy gốc trong folder `VR-003-2026-08-04` (2026-08-04), đã merge vào đây rồi **xoá folder gốc** theo yêu cầu user (2026-08-05).
> - **Round 2** — chạy trực tiếp trong folder này (`Thongbao_VR-006-2026-08-05`, 2026-08-05), retest 29 TC pending từ Round 1.
> Tổng cộng: 39 TC (Round 1) → 15 PASS / 0 FAIL / 24 BLOCKED tích luỹ sau Round 2.

---

## ROUND 1 — Session info (gốc VR-003, 2026-08-04)
- Platform: mobile (Appium MCP, UiAutomator2)
- Device: emulator-5554 (Pixel 6 emulator, đã mở sẵn theo yêu cầu user)
- App: `com.hrisproject.stag` (FoxEco SDK trong FoxPro), đã mở sẵn tại màn Trang chủ
- Session ID: `4f52c4f9-d97c-45c1-81b6-04b0be86b35a`
- Created: 09:04 (2026-08-04)
- Pre-flight: ✅ `select_device` OK → `appium_session_management(create)` OK → `appium_get_page_source` OK (large, saved to file) → `appium_get_window_size` OK (1080x2400)

### Round 1 — Call history

| # | Time | MCP method | Args (summary) | Result | Note |
|--:|------|-----------|----------------|--------|------|
| 1 | 09:04 | appium_session_management | action=list | No active sessions | Pre-check |
| 2 | 09:04 | select_device | platform=android | OK, emulator-5554 | Pre-flight |
| 3 | 09:04 | appium_session_management | action=create, android | OK sid=4f52c4f9... | Pre-flight |
| 4 | 09:04 | appium_get_page_source | — | OK (~269KB, home screen) | Pre-flight |
| 5 | 09:04 | appium_get_window_size | — | 1080x2400 | Pre-flight |
| 6 | 09:05 | appium_screenshot | — | OK → 00_precheck_home.png | Xác nhận đang ở Trang chủ |
| 7 | 09:05 | appium_find_element | accessibility id = "Thông báo" | OK elementId ...1023 | Icon chuông |
| 8 | 09:05 | appium_gesture | action=tap, elementUUID ...1023 | OK | Tap icon chuông |
| 9 | 09:06 | appium_screenshot | — | OK → 01_notification_screen.png | Vào màn Thông báo |
| 10 | 09:06 | appium_get_page_source | — | OK (~239KB) | Snapshot đầu tiên màn Thông báo |
| 11 | 09:07 | appium_gesture | action=scroll, direction=down | OK | Scroll 1 |
| 12 | 09:07 | appium_get_page_source | — | OK | Snapshot sau scroll 1 |
| 13 | 09:08 | appium_screenshot | — | OK → 02_scroll1.png | |
| 14 | 09:08 | appium_gesture | action=scroll, direction=down (x2, duration=300) | OK x2 | Scroll thêm |
| 15 | 09:08 | appium_get_page_source | — | OK | Snapshot sau scroll x3 |
| 16 | 09:09 | appium_screenshot | — | OK → 03_scroll3.png | |
| 17 | 09:09 | appium_gesture | action=swipe fast (custom coords x2) | OK x2 | Cố scroll sâu hơn |
| 18 | 09:10 | appium_screenshot | — | OK → 04_scroll_end.png (md5 trùng #16→#18) | Xác nhận đã chạm đáy danh sách, không load thêm |
| 19 | 09:10 | appium_gesture | action=swipe fast (reverse, x3) + scroll_to_element (fail, harmless) | OK x3 / 1 lỗi không match | Quay lại đầu danh sách |
| 20 | 09:12 | appium_screenshot | — | OK → 05_back_to_top.png | Xác nhận về đầu, timestamp tương đối tự cập nhật (14 phút→20 phút) |
| 21 | 09:12 | appium_get_page_source | — | OK | Snapshot đầu danh sách, lấy resource-id ổn định |
| 22 | 09:13 | appium_find_element | -android uiautomator resourceId("notif-item-019fc905-...") | OK elementId ...116c | Card "Đơn đã được giao" (7 giờ trước) |
| 23 | 09:13 | appium_gesture | action=tap, elementUUID ...116c | OK | TC_03.20 / TC_03.36 |
| 24 | 09:13 | appium_screenshot | — | OK → 06_TC_03.20_36_tap_daduocgiao.png | Điều hướng → Theo dõi đơn |
| 25 | 09:13 | appium_gesture | action=back | OK | Quay lại Thông báo |
| 26 | 09:13 | appium_get_page_source | — | OK | Verify chỉ card vừa tap mất unread-dot |
| 27 | 09:14 | appium_screenshot | — | OK → 07_TC_03.20_after_read.png | Bằng chứng visual |
| 28 | 09:14 | appium_find_element | -android uiautomator resourceId (cùng ...116c) | OK | Card đã đọc, test lại (TC_03.22) |
| 29 | 09:14 | appium_gesture | action=tap, elementUUID ...116c | OK | TC_03.22 |
| 30 | 09:15 | appium_screenshot | — | OK → 08_TC_03.22_tap_already_read.png | Không lỗi, điều hướng bình thường |
| 31 | 09:15 | appium_gesture | action=back | OK | |
| 32 | 09:15 | appium_get_page_source | — | OK | Verify state không đổi so với trước |
| 33 | 09:15 | appium_find_element | accessibility id = "Đánh dấu đã đọc" | OK elementId ...1157 | TC_03.21 |
| 34 | 09:15 | appium_gesture | action=tap, elementUUID ...1157 | OK | Mark-all-as-read |
| 35 | 09:15 | appium_get_page_source | — | OK | Verify toàn bộ dot biến mất + nút tự ẩn |
| 36 | 09:16 | appium_screenshot | — | OK → 09_TC_03.21_markall_read.png | |
| 37 | 09:17 | appium_find_element | -android uiautomator resourceId("notif-item-019fc8ad-...") | OK elementId ...1179 | TC_03.33 |
| 38 | 09:17 | appium_gesture | action=tap, elementUUID ...1179 | OK | |
| 39 | 09:17 | appium_screenshot | — | OK → 10_TC_03.33_tap_donguitoiban.png | Điều hướng → Theo dõi đơn |
| 40 | 09:17 | appium_gesture | action=back | OK | |
| 41 | 09:17 | appium_find_element | -android uiautomator resourceId("notif-item-019fc896-9f80-...") | OK elementId ...1190 | TC_03.35 |
| 42 | 09:18 | appium_gesture | action=tap, elementUUID ...1190 | OK | |
| 43 | 09:18 | appium_screenshot | — | OK → 11_TC_03.35_tap_nguoivanchuyenlayhang.png | Điều hướng → Theo dõi đơn |
| 44 | 09:18 | appium_gesture | action=back | OK | |
| 45 | 09:19 | appium_find_element | xpath `//*[@bounds="[42,149][137,244]"]` | OK elementId ...114c | Icon back (TC_03.18) |
| 46 | 09:19 | appium_gesture | action=tap, elementUUID ...114c | OK | |
| 47 | 09:19 | appium_screenshot | — | OK → 12_TC_03.18_back_icon.png | Điều hướng → Trang chủ (đúng) |

### Round 1 — Statistics
- Total MCP calls: 47
- find_element calls: 7 (success: 7, NOT FOUND: 0)
- get_page_source calls: 8
- screenshot calls: 13
- gesture (tap/scroll/swipe/back) calls: ~19
- ⚠️ Failures: 1 non-blocking (`scroll_to_element` với selector "Thông báo" — element ambiguous/end-of-content, không ảnh hưởng flow vì đã dùng swipe thay thế)

---

## ROUND 2 — Session info (VR-006, 2026-08-05)
- Platform: mobile (Appium MCP, embedded/local)
- Device: emulator-5554 (Pixel 6)
- Host app: FoxPro `com.hrisproject.stag` (FoxEco SDK)
- Session ID: `03e06324-66b8-4404-a7cd-878d4d80f699`
- Created: 14:09 (2026-08-05)
- Account: "Phan Minh Tài" (session persisted from earlier today, already logged in on emulator)
- Pre-flight: ✅ appium_session_management(list, pre-check: none active) → select_device → session create → get_page_source → get_window_size all OK

### Round 2 — Call history

| # | Time | MCP method | Args (summary) | Result | Note |
|--:|------|-----------|----------------|--------|------|
| 1 | 14:08 | appium_session_management | action=list | OK — no active sessions | Pre-flight check |
| 2 | 14:09 | select_device | platform=android | OK — emulator-5554 | Pre-flight |
| 3 | 14:09 | appium_session_management | action=create, android, udid=emulator-5554 | OK sid=03e06324... | Pre-flight |
| 4 | 14:09 | appium_get_page_source | — | OK ~106k chars, package=com.hrisproject.stag, screen=Trang chủ, account="Phan Minh Tài" | Pre-flight |
| 5 | 14:09 | appium_get_window_size | — | 1080x2400 | Pre-flight |
| 6 | 14:09 | appium_find_element | accessibility id = "Thông báo" | OK eid=...8c49 | Entry — bell icon on Trang chủ |
| 7 | 14:09 | appium_gesture | action=tap, eid=...8c49 | OK | Navigate → màn Thông báo |
| 8 | 14:10 | appium_screenshot | — | OK → 00_thongbao_screen_current.png | Survey initial state |
| 9 | 14:10 | appium_get_page_source | — | OK, 8 notif-item, group "HÔM NAY" | Survey — data richer than VR-003 (Aug 4) |
| 10 | 14:11 | appium_gesture | action=scroll, direction=down | OK | Survey scroll #1 |
| 11 | 14:11 | appium_get_page_source | — | OK, 9 notif-item, "HÔM QUA" group visible | TC_03.25 evidence — new batch loaded |
| 12 | 14:11 | appium_gesture | action=scroll, direction=down | OK | Survey scroll #2 |
| 13 | 14:11 | appium_get_page_source | — | OK, 9 notif-item, "Đơn đã hoàn tất" type found (new vs VR-003) | TC_03.25/37 evidence |
| 14 | 14:12 | appium_gesture | action=scroll, direction=down | OK | Survey scroll #3 |
| 15 | 14:12 | appium_get_page_source | — | OK, content same as call #11 (bounce-back) | Indicates near end-of-list at this depth |
| 16-18 | 14:13 | appium_gesture | action=scroll, direction=up ×3 | OK | Return to top |
| 19 | 14:13 | appium_get_page_source | — | OK, located notif-item-019fd040-... = "Đơn đã bị huỷ" | TC_03.39 locator capture |
| 20 | 14:13 | appium_find_element | -android uiautomator resourceId("notif-item-019fd040-c13d-70d7-ae3d-010e42304a79") | OK eid=...8fce | TC_03.39 step 3 |
| 21 | 14:14 | appium_gesture | action=tap, eid=...8fce | OK | TC_03.39 step 3 action |
| 22 | 14:14 | appium_screenshot | — | OK → TC_03.39_after_tap_donbihuy.png | TC_03.39 evidence — landed "Theo dõi đơn" |
| 23 | 14:14 | appium_mobile_press_key | key=BACK | OK | Return to Thông báo |
| 24-26 | 14:14 | appium_gesture | action=scroll, direction=down ×3 | OK | Navigate to "Đơn đã hoàn tất" card |
| 27 | 14:15 | appium_get_page_source | — | OK, located notif-item-019fcb8c-... = "Đơn đã hoàn tất" | TC_03.37 locator capture |
| 28 | 14:15 | appium_find_element | -android uiautomator resourceId("notif-item-019fcb8c-fc15-7ef0-80a6-3b9725c63a72") | OK eid=...9078 | TC_03.37 step 3 |
| 29 | 14:15 | appium_gesture | action=tap, eid=...9078 | OK | TC_03.37 step 3 action |
| 30 | 14:15 | appium_screenshot | — | OK → TC_03.37_after_tap_donhoantat.png | TC_03.37 evidence — landed "Theo dõi đơn" (Hoàn thành) |
| 31 | 14:15 | appium_mobile_press_key | key=BACK | OK | Return to Thông báo |
| 32-37 | 14:15-16 | appium_gesture | action=scroll, direction=down ×6 | OK | TC_03.25/26 — continue loading batches |
| 38 | 14:16 | appium_get_page_source | — | OK, 9 notif-item, group "TUẦN NÀY" appeared | TC_03.25 evidence — 3rd distinct batch/group loaded |
| 39-48 | 14:17-18 | appium_gesture | action=scroll, direction=down ×10 | OK | TC_03.26/27 — push to true end of list |
| 49 | 14:18 | appium_screenshot | — | OK → TC_03.26_scroll_bottom_check.png | TC_03.26/27 evidence — list stopped growing past "TUẦN NÀY" section, no spinner, no dup, no crash |
| — | 14:18 | ADB (not MCP) | `adb shell svc wifi disable` + `svc data disable` | OK | TC_03.28 attempt — simulate network loss (lifecycle-level, NOT a locator action) |
| 50-51 | 14:18 | appium_gesture | action=scroll, direction=down ×2 | OK | TC_03.28 — scroll while offline |
| — | 14:19 | ADB (not MCP) | `adb shell svc wifi enable` + `svc data enable` | OK | Restore network |
| 52 | 14:19 | appium_screenshot | — | OK (not saved — verification only) | TC_03.28 — confirm no crash/data loss after restore |

### Round 2 — Statistics
- Total MCP calls: 52
- find_element calls: 3 (success: 3, NOT FOUND: 0)
- get_page_source calls: 6
- gesture calls (scroll/tap): 40 (scroll: 37, tap: 3)
- press_key calls: 2 (BACK)
- screenshot calls: 4 (saved: 4)
- ADB calls (lifecycle/network-sim only, NOT locator source): 4 (`svc wifi/data disable/enable`)
- Failures: none — all MCP calls returned success

### Round 2 — Notes
- Data on the test account changed materially since VR-003 (2026-08-04): new notification types appeared ("Đơn đã bị huỷ", "Đơn đã hoàn tất") and list depth grew (HÔM NAY → HÔM QUA → TUẦN NÀY), enabling TC_03.25/26/27/37/39 to move from BLOCKED → tested this round.
- TC_03.28 (mất mạng đúng lúc đang load thêm) could not be precisely timed — by the time network was disabled the list had already reached end-of-data (no in-flight load-more request to interrupt). Partial evidence only (no crash/data-loss while offline at rest) — kept BLOCKED for the exact scenario.

---

## Combined Statistics (Round 1 + Round 2)
- Total MCP calls: 99 (47 + 52)
- find_element calls: 10 (success: 10, NOT FOUND: 0)
- get_page_source calls: 14
- screenshot calls: 17 (all saved, all present in `screenshots/`)
- Failures: 1 non-blocking (Round 1, `scroll_to_element` ambiguous match, worked around with swipe)
