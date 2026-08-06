# Vibe Locators — v1.0 — Thongbao_VR-006-2026-08-05 (merged Round 1 + Round 2) — 2026-08-05

> Captured via Appium MCP (UiAutomator2) during 2 lần chạy.
> Mark legend: ✅ Verified (MCP find+action OK) · ⚠️ Inferred · 🚫 NOT FOUND · ⏳ Pending
> MCP session log: see mcp-session-log.md (audit trail, gồm cả Round 1 + Round 2)
> Platform: mobile (Android, package `com.hrisproject.stag`, emulator-5554)
> Scope: module Thông báo (TC_03) — flow Trang chủ → icon chuông → màn Thông báo
> Round 1 = gốc `VR-003-2026-08-04` (đã merge, folder gốc đã xoá) · Round 2 = `Thongbao_VR-006-2026-08-05`

## Page: Trang chủ (Home)

| Element | Action Used | Strategy | Value | Verified | MCP call ref | TC refs |
|---------|------------|----------|-------|----------|--------------|---------|
| Icon chuông (bell) | tap | accessibility id | `Thông báo` | ✅ (verified cả 2 round) | R1 mcp-log #6-7 · R2 mcp-log #6-7 | TC_03.17 (entry flow) |

## Page: Thông báo (Notification list)

| Element | Action Used | Strategy | Value | Verified | MCP call ref | TC refs |
|---------|------------|----------|-------|----------|--------------|---------|
| Header text | verify | text (a11y-important TextView) | `Thông báo` | ✅ | R1 mcp-log #9 | TC_03.17 |
| Icon back (header) | tap | xpath (no content-desc/id exposed) | `//*[@bounds="[42,149][137,244]"]` | ✅ | R1 mcp-log #48-49 | TC_03.18 |
| Nút "Đánh dấu đã đọc" (mark all read) | tap | accessibility id | `Đánh dấu đã đọc` | ✅ | R1 mcp-log #39-40 | TC_03.21, TC_03.23 |
| Group header "HÔM NAY" / "HÔM QUA" / "TUẦN NÀY" | verify | text (TextView) | `HÔM NAY` / `HÔM QUA` / `TUẦN NÀY` (nhóm mới xuất hiện Round 2) | ✅ | R1 mcp-log #9 · R2 mcp-log #38 | TC_03.17, TC_03.25 |
| Notification card (generic) | tap | id (uiautomator resourceId) | `notif-item-<uuid>` — each card has unique resource-id | ✅ | R1 mcp-log #29-30, #33-34, #43-44, #46-47 · R2 mcp-log #20-21, #28-29 | TC_03.20, 22, 33, 35, 36, 37, 39 |
| Card "Đơn đã bị huỷ" (loại mới, Round 2) | tap | id (uiautomator resourceId) | ví dụ đã capture: `notif-item-019fd040-c13d-70d7-ae3d-010e42304a79` | ✅ | R2 mcp-log #19-21 | TC_03.39 |
| Card "Đơn đã hoàn tất" (loại mới, Round 2) | tap | id (uiautomator resourceId) | ví dụ đã capture: `notif-item-019fcb8c-fc15-7ef0-80a6-3b9725c63a72` | ✅ | R2 mcp-log #27-29 | TC_03.37 |
| Unread-dot indicator (small ViewGroup next to title) | verify (presence/absence) | relative position | ViewGroup `bounds="[986,Y][1007,Y+21]"` inside each `notif-item-*` block, no content-desc/text | ✅ (inferred via page-source diff, not a tappable target) | R1 mcp-log #10, #31, #35, #41 | TC_03.20, 21, 22, 23 |
| 4 loại push còn lại (Đã có người nhận mang giúp, Ghép thành công, Tìm thấy đơn hàng phù hợp tuyến, quà cảm ơn) | — | — | (không tồn tại trong dữ liệu tài khoản test qua cả 2 round) | 🚫 NOT FOUND | R1 mcp-log #10,#13,#16 · R2 mcp-log #9,#11,#13,#38 (page source scans) | TC_03.31, 32, 34, 38 |

> Nay đã xác nhận **5/9 loại thông báo** (theo bảng 9 loại `MEMORY.md` §6.1) có mặt trong lịch sử tài
> khoản test: "Đơn đã được giao", "Đơn gửi tới bạn đã có người vận chuyển", "Người vận chuyển đã lấy
> hàng" (Round 1) + "Đơn đã bị huỷ", "Đơn đã hoàn tất" (Round 2, mới). Còn 4 loại chưa xuất hiện qua cả
> 2 round — vẫn cần multi-device/account khác để capture (xem TC_03.31/32/34/38).

## Page: Theo dõi đơn (destination after tapping a notification)

| Element | Action Used | Strategy | Value | Verified | MCP call ref | TC refs |
|---------|------------|----------|-------|----------|--------------|---------|
| Header text | verify | text (TextView) | `Theo dõi đơn` | ✅ | R1 mcp-log #30, #34, #44, #47 · R2 mcp-log #22 | TC_03.20, 33, 35, 36, 39 |
| Banner đỏ "Đơn hàng đã bị huỷ" | verify | text (TextView) | `Đơn hàng đã bị huỷ` | ✅ | R2 mcp-log #22 | TC_03.39 |
| Timeline step "Hoàn thành" (highlight) | verify | text (TextView) | `Hoàn thành` | ✅ | R2 mcp-log #30 | TC_03.37 |

## Navigation Flow (only MCP-traversed flows, cả 2 round)

| From | Trigger | To | MCP-verified |
|------|---------|-----|--------------|
| Trang chủ | MCP tap icon chuông (`Thông báo`) | Thông báo (list) | R1 pre-check screenshot · R2 mcp-log #7 |
| Thông báo | MCP tap card `notif-item-019fc905-...` ("Đơn đã được giao") | Theo dõi đơn | TC_03.20 / TC_03.36 |
| Thông báo | MCP tap card `notif-item-019fc8ad-...` ("Đơn gửi tới bạn đã có người vận chuyển") | Theo dõi đơn | TC_03.33 |
| Thông báo | MCP tap card `notif-item-019fc896-9f80-...` ("Người vận chuyển đã lấy hàng") | Theo dõi đơn | TC_03.35 |
| Thông báo | MCP tap card "Đơn đã bị huỷ" | Theo dõi đơn (banner đỏ "Đơn hàng đã bị huỷ") | TC_03.39 (Round 2) |
| Thông báo | MCP tap card "Đơn đã hoàn tất" | Theo dõi đơn (timeline "Hoàn thành") | TC_03.37 (Round 2) |
| Theo dõi đơn | MCP `back` gesture / press_key BACK | Thông báo (list, state preserved) | TC_03.20, 22, 33, 35, 37, 39 |
| Thông báo | MCP tap back-icon (xpath bounds) | Trang chủ | TC_03.18 |

## Ghi chú quan trọng cho implement-automation

- Locator ổn định nhất cho từng card thông báo: `resource-id` dạng `notif-item-<uuid>` (uiautomator `resourceId`, KHÔNG dùng strategy Appium "id" chuẩn — bị lỗi not-found, phải dùng `-android uiautomator` với `new UiSelector().resourceId("...")`).
- `content-desc` của card = tiêu đề thông báo (title) — **KHÔNG unique** khi có nhiều thông báo cùng loại → automation nên chọn theo `resource-id` hoặc theo vị trí (index) trong danh sách, không nên dùng content-desc để định vị 1 card cụ thể.
- Icon back ở header Thông báo **không có accessibility label** (`content-desc=""`) — gap nhỏ về a11y, hiện dùng xpath theo bounds tuyệt đối (dễ vỡ khi resize màn hình khác) — đề xuất BE/FE thêm accessibility label cho nút này.
- uuid trong `notif-item-<uuid>` đổi mỗi lần app re-fetch data → KHÔNG hardcode uuid cụ thể vào test code, chỉ dùng để trace lại đúng run này.
- Cơ chế load-more (scroll-to-bottom) xác nhận hoạt động đúng qua nhiều batch (HÔM NAY → HÔM QUA →
  TUẦN NÀY, Round 2), không trùng lặp item — an toàn để automate TC_03.25/26/27 bằng scroll lặp + so
  sánh số lượng `notif-item-*` trước/sau.
- KHÔNG có UI indicator "đã hết dữ liệu" — automation cho TC_03.26 nên assert theo "không tăng thêm
  item sau N lần scroll liên tiếp", KHÔNG assert theo text cụ thể (không tồn tại).
- Dữ liệu tài khoản "Phan Minh Tài" biến động mạnh giữa các ngày (tài khoản dùng chung nhiều tester)
  — automation cho các TC phụ thuộc loại thông báo cụ thể (TC_03.29-39) nên có bước discover/skip nếu
  loại thông báo cần thiết chưa xuất hiện, thay vì hardcode phải luôn có.
