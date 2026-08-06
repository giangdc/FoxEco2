# Vibe Locators — v1.0 — VR-002 — 2026-08-03

> Captured via Appium MCP (UiAutomator2) during run này.
> Mark legend: ✅ Verified · ⚠️ Inferred · 🚫 NOT FOUND · ⏳ Pending
> MCP session log: xem `mcp-session-log.md`
> Platform: mobile (Android) — App: FoxEco SDK trong FoxPro STG, package `com.hrisproject.stag`
> Session này gồm 2 phần: (A) module Hoạt động [continued/finished trong lần chạy này],
> (B) module Đăng tin — Form OFFER [đã chạy steps + ghi Excel ở phiên trước, screenshots step_form*.png
> + step_post_menu.png tồn tại nhưng KHÔNG có mcp-session-log của phần đó → locator phần (B) đã có
> trong `vibe-locators-latest.md` (từ VR-001) nên KHÔNG lặp lại ở đây, chỉ bổ sung phần (A).
> ⚠️ App này gần như KHÔNG dùng `resource-id` (Compose UI) — locator thực tế chủ yếu dựa vào
> `-android uiautomator text/descriptionContains(...)`.

## Page: Bottom Navigation (toàn app)

| Element | Action Used | Locator Strategy | Locator Value | Verified | MCP call ref | TC refs |
|---------|------------|-------------------|----------------|----------|---------------|---------|
| Tab "Trang chủ" | tap / verify | -android uiautomator | `new UiSelector().text("Trang chủ")` | ✅ | mcp-log #3 | TC_01.1, TC_01.3 |
| Tab "Bảng tin" | verify | -android uiautomator | `new UiSelector().text("Bảng tin")` | ✅ | mcp-log #5 | TC_01.1 |
| Tab "Đăng tin" (+ nút giữa) | verify | -android uiautomator | `new UiSelector().text("Đăng tin")` | ✅ | mcp-log #7 | TC_01.1 |
| Tab "Hoạt động" | tap / verify | -android uiautomator | `new UiSelector().text("Hoạt động")` | ✅ | mcp-log #1, #4 | TC_01.1, TC_01.3 |
| Tab "Cá nhân" | verify | -android uiautomator | `new UiSelector().text("Cá nhân")` | ✅ | mcp-log #6 | TC_01.1 |

## Page: Hoạt động — Đơn của tôi (/activity)

| Element | Action Used | Locator Strategy | Locator Value | Verified | MCP call ref | TC refs |
|---------|------------|-------------------|----------------|----------|---------------|---------|
| Tab switcher "Đang diễn ra" | tap / verify | -android uiautomator | `new UiSelector().text("Đang diễn ra")` | ✅ | mcp-log #8, #16, #27 | TC_01.2, TC_01.3, TC_01.4 |
| Tab switcher "Đã hoàn thành" | tap / verify | -android uiautomator | `new UiSelector().text("Đã hoàn thành")` | ✅ | mcp-log #9, #20 | TC_01.2, TC_01.5, TC_01.20 |
| Order card (bất kỳ trạng thái) | tap / verify | -android uiautomator | `new UiSelector().descriptionContains("<Badge trạng thái>")` — vd `descriptionContains("Chờ ghép")`, `descriptionContains("Đã ghép")`, `descriptionContains("Đang giao")`. Toàn bộ card là 1 accessibility node, content-desc gộp: `"Nhận: <tên tin>, <badge trạng thái>, Từ: <điểm đi>, Đến: <điểm đến>, Chạm để theo dõi đơn của bạn"` | ✅ | mcp-log #22, #24, #29, #33, #35, #37 | TC_01.4, 6, 7, 8, 12, 13, 14, 15 |
| Empty state icon (pulse/nhịp tim, SVG) | verify (visual only) | (SVG `com.horcrux.svg.SvgView`, không có accessibility name riêng) | không có locator text — chỉ verify qua screenshot | ⚠️ Inferred (không có id/content-desc để MCP find riêng icon) | mcp-log #19 (screenshot) | TC_01.20 |
| Empty state text "Chưa có đơn nào" | verify | -android uiautomator | `new UiSelector().text("Chưa có đơn nào")` | ✅ | mcp-log #19 | TC_01.20 |

## Page: Theo dõi đơn (đích điều hướng khi tap order card)

| Element | Action Used | Locator Strategy | Locator Value | Verified | MCP call ref | TC refs |
|---------|------------|-------------------|----------------|----------|---------------|---------|
| Header "Theo dõi đơn" | verify | -android uiautomator | `new UiSelector().text("Theo dõi đơn")` | ✅ | mcp-log #23, #30, #34, #36 | TC_01.13, 14, 15 |
| Stepper 5 bước | verify (text list) | -android uiautomator | text nodes: "Chờ ghép", "Lấy hàng", "Đang giao", "Đã giao", "Hoàn thành" | ✅ | mcp-log #23 | TC_01.13 |
| Nút back (mũi tên) | tap | (không tìm bằng accessibility id text — dùng `appium_mobile_press_key(BACK)` thay vì locator) | — | ✅ (qua hardware back, không phải element locator) | mcp-log #26, #31 | TC_01.14, 15 (cleanup) |

## Navigation Flow (chỉ flow đã MCP-traverse trong run này)

| From | Trigger | To | MCP-verified |
|------|---------|-----|--------------|
| (any tab) | tap "Trang chủ" rồi tap "Hoạt động" | Hoạt động — tab "Đang diễn ra" (default) | TC_01.3 |
| Hoạt động / tab "Đang diễn ra" | tap card "Chờ ghép" | Theo dõi đơn (KHÔNG phải "Chi tiết tin") | TC_01.13 |
| Hoạt động / tab "Đang diễn ra" | tap card "Đã ghép" | Theo dõi đơn (KHÔNG phải "Chi tiết tin") | TC_01.14 |
| Hoạt động / tab "Đang diễn ra" | tap card "Đang giao" | Theo dõi đơn (KHÔNG phải "Chi tiết tin") | TC_01.15 |
| Hoạt động / tab "Đang diễn ra" | tap tab "Đã hoàn thành" | Empty state "Chưa có đơn nào" (tài khoản test này không có đơn Hoàn thành/Hết hạn) | TC_01.20 |

**Giá trị cho implement-automation:**
- Card đơn ở Hoạt động là 1 accessibility node duy nhất (không có sub-element riêng cho từng field)
  → automation chỉ có thể click nguyên card, KHÔNG click riêng được vào badge/tên tin/tuyến.
- Card content-desc KHÔNG chứa trường ngày/thời gian nào — xem finding TC_01.8 trong vibe-report.
- Tap card → LUÔN điều hướng "Theo dõi đơn", không phải "Chi tiết tin" — TC-MASTER hiện ghi sai
  expected result cho TC_01.13/14/15 (xem vibe-report §Findings), automation nên assert đích
  "Theo dõi đơn" khi implement, KHÔNG assert "Chi tiết tin".
- Dữ liệu test là mock ngẫu nhiên hoá mỗi lần load lại màn (badge/thứ tự card đổi giữa các lần
  điều hướng) — automation cần assert theo badge/content-desc pattern, KHÔNG hardcode index cố định.
