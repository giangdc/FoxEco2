# Vibe Locators — v1.0 — merged (VR-001 + VR-002 + Profile_VR-007 [Round 1+2+3] + Thongbao_VR-006 [Round 1+2]) — 2026-08-05

> Captured via Appium MCP (UiAutomator2) during các run này.
> Mark legend: ✅ Verified · ⚠️ Inferred · 🚫 NOT FOUND · ⏳ Pending
> MCP session log: xem `VR-001-2026-08-03/mcp-session-log.md` + `VR-002-2026-08-03/mcp-session-log.md`
> + `Profile_VR-007-2026-08-05/mcp-session-log.md` + `Thongbao_VR-006-2026-08-05/mcp-session-log.md`
> (2 folder sau chứa nhiều round gộp — folder gốc `VR-003-2026-08-04` đã merge vào `Thongbao_VR-006`
> và `VR-004-2026-08-04` đã merge vào `Profile_VR-007`, cả 2 đều đã xoá sau merge, 2026-08-05)
> Platform: mobile (Android) — App: FoxEco SDK trong FoxPro STG, package `com.hrisproject.stag`
> ⚠️ Phần lớn màn hình app KHÔNG dùng `resource-id` (Compose UI) — locator chủ yếu dựa vào
> `-android uiautomator textContains/text(...)` hoặc `content-desc` (accessibility id), xpath là fallback cuối.
> **Ngoại lệ:** màn Thông báo (module TC_03, xem `Thongbao_VR-006-2026-08-05`, gộp Round 1+2) render qua
> React Native (`com.horcrux.svg` cho icon) và MỖI card thông báo CÓ `resource-id` riêng dạng
> `notif-item-<uuid>` — dùng `-android uiautomator new UiSelector().resourceId("...")` (strategy Appium
> chuẩn `id` KHÔNG match được).
> Màn "Cá nhân" (module TC_02, xem VR-004) cũng CÓ `resource-id`/accessibility id thật cho các
> element tương tác chính (`profile-menu-activity`, `profile-menu-gifts`, `gifts-received-title`).
> Nguồn: VR-001 (module Đăng tin — Form OFFER) + VR-002 (module Hoạt động)
> + `Thongbao_VR-006-2026-08-05` (module Thông báo, Round 1+2 gộp)
> + VR-004 (module Cá nhân, 2 account).

## Page: Trang chủ (/home)

| Element | Action Used | Locator Strategy | Locator Value | Verified | MCP call ref | TC refs |
|---------|------------|-------------------|----------------|----------|---------------|---------|
| Tab "Đăng tin" (bottom nav) | tap | accessibility id | `Đăng tin` | ✅ | mcp-log #5-6 | TC_04.94–103 (entry) |

## Page: Đăng tin mới (chọn vai trò)

| Element | Action Used | Locator Strategy | Locator Value | Verified | MCP call ref | TC refs |
|---------|------------|-------------------|----------------|----------|---------------|---------|
| Card "Tôi nhận giao hàng" | tap | accessibility id | `Tôi nhận giao hàng` | 🚫 NOT FOUND | mcp-log #7 | — |
| Card "Tôi nhận giao hàng" | tap | -android uiautomator | `new UiSelector().textContains("Tôi nhận giao hàng")` | ✅ | mcp-log #8-9 | TC_04.94–103 (entry) |

## Page: Form OFFER — "Tôi nhận giao hàng" (đăng ký tuyến)

| Element | Action Used | Locator Strategy | Locator Value | Verified | MCP call ref | TC refs |
|---------|------------|-------------------|----------------|----------|---------------|---------|
| Tên người giao (EditText #0) | verify | -android uiautomator | `new UiSelector().textContains("Ngô Quốc Hưng")` (hoặc `hint("Họ tên")`) | ✅ | mcp-log #10 | TC_04.94 |
| SĐT người giao (EditText #1) | verify | -android uiautomator | `new UiSelector().textContains("0000166911")` (hoặc `hint("Số điện thoại")`) | ✅ | mcp-log #11 | TC_04.94 |
| Điểm xuất phát (A) (EditText #2) | type | -android uiautomator | `new UiSelector().className("android.widget.EditText").instance(2)` (hint=`"Bạn đang ở đâu / xuất phát từ đâu"`, maxLength=200) | ✅ | mcp-log #12-13, #30-35 | TC_04.94, 95, 96, 97, 98, 99, 100, 101, 102 |
| Điểm đến (B) (EditText #3) | type | -android uiautomator | `new UiSelector().className("android.widget.EditText").instance(3)` (hint=`"Bạn sẽ đến đâu"`, maxLength=200) | ✅ | mcp-log #14, #20 | TC_04.94, 95, 99, 100, 103 |
| Từ ngày (mặc định "Hôm nay") | verify | -android uiautomator | `new UiSelector().text("Hôm nay").instance(0)` | ✅ | mcp-log #16 | TC_04.94 |
| Đến ngày (mặc định "Hôm nay") | verify | -android uiautomator | `new UiSelector().text("Hôm nay").instance(1)` | ✅ | mcp-log #17 | TC_04.94 |
| KHỞI HÀNH (time picker trigger) | tap | -android uiautomator | `new UiSelector().textContains("<current HH:mm>")` — text đổi theo giá trị hiện tại, KHÔNG cố định | ✅ | mcp-log #45 | TC_04.101, 102 |
| ĐẾN NƠI (time picker trigger) | tap | -android uiautomator | `new UiSelector().textContains("<current HH:mm>")` — text đổi theo giá trị hiện tại | ✅ | mcp-log #60, #72 | TC_04.101, 102 |
| Checkbox "Tôi đã đọc và đồng ý Điều khoản..." | tap | -android uiautomator | `new UiSelector().textContains("Điều khoản sử dụng FoxEco")` | ✅ | mcp-log #15, #21, #37 | TC_04.94, 95, 99 |
| Button "Đăng tin ngay" | tap / verify enabled | -android uiautomator (hoặc accessibility id qua content-desc) | `new UiSelector().textContains("Đăng tin ngay")` — content-desc="Đăng tin ngay", `enabled` attribute phản ánh trạng thái validate | ✅ | mcp-log #22-23, #38, #42, #78, #81, #83 | TC_04.95, 99, 100, 102, 103 |

## Dialog: Time Picker "Chọn giờ"

| Element | Action Used | Locator Strategy | Locator Value | Verified | MCP call ref | TC refs |
|---------|------------|-------------------|----------------|----------|---------------|---------|
| Nút "Huỷ" | (không dùng trong run này) | -android uiautomator | `new UiSelector().description("Huỷ")` | ⚠️ Inferred (thấy trong page source, chưa tap) | mcp-log #46 (page source) | — |
| Nút "Xong" | tap | -android uiautomator | `new UiSelector().description("Xong")` | ✅ | mcp-log #59, #69, #77 | TC_04.101, 102 |
| Wheel Giờ (hour ScrollView) | swipe (coordinate-based) | KHÔNG có id — chỉ dùng bounds/coordinate swipe hoặc `new UiSelector().text("<HH>")` để tap trực tiếp số hiển thị | ⚠️ Inferred — hoạt động qua coordinate swipe, KHÔNG phải true "locator", cần lưu ý khi implement-automation (native NumberPicker `sendKeys`/`setValue` có thể không áp dụng cho Compose wheel này) | mcp-log #46-58 | TC_04.101, 102 |
| Wheel Phút (minute ScrollView) | swipe (coordinate-based) | tương tự — không id | ⚠️ Inferred (coordinate-based) | mcp-log #46-58, #61-68, #73-76 | TC_04.101, 102 |

## Inline validation message

| Element | Context | Locator Strategy | Locator Value | Verified | MCP call ref | TC refs |
|---------|---------|-------------------|----------------|----------|---------------|---------|
| Error text "Giờ đến phải lớn hơn 17:30" | Hiện khi ĐẾN NƠI ≤ KHỞI HÀNH+29min | -android uiautomator | `new UiSelector().textContains("Giờ đến phải lớn hơn")` | ✅ | mcp-log #70 | TC_04.101 |
| ⚠️ KHÔNG có error text tương ứng cho case Điểm đến trùng Điểm xuất phát (TC_04.99) | — | — | (không tồn tại) | 🚫 NOT FOUND | mcp-log #38 | TC_04.99 |
| ⚠️ KHÔNG có error text tương ứng cho case Điểm xuất phát để trống (TC_04.100) | — | — | (không tồn tại) | 🚫 NOT FOUND | mcp-log #42 | TC_04.100 |

## Navigation Flow (chỉ flow đã MCP-traverse trong run này)

| From | Trigger | To | MCP-verified |
|------|---------|-----|--------------|
| Trang chủ | tap "Đăng tin" | Đăng tin mới (chọn vai trò) | TC_04.94 setup |
| Đăng tin mới | tap "Tôi nhận giao hàng" | Form OFFER (1 bước, không qua wizard) | TC_04.94 setup |
| Form OFFER | tap "Đăng tin ngay" (data hợp lệ) | Màn "Đã ghi nhận tuyến đường!" | TC_04.95 step 5 |
| Màn "Đã ghi nhận tuyến đường!" | tap "Về trang chủ" | Trang chủ | TC_04.95 cleanup |

**Giá trị cho implement-automation:**
- App dùng Jetpack Compose UI, hầu như không có `resource-id` → automation nên ưu tiên
  `content-desc` (accessibility id) khi có, fallback `-android uiautomator textContains/text`.
- Time picker "Chọn giờ" là custom wheel Compose — KHÔNG hỗ trợ native NumberPicker API tốt;
  automation cần dùng coordinate swipe (như đã làm ở đây) hoặc tap trực tiếp lên số hiển thị trong
  phạm vi ±2 vị trí quanh tâm — cực kỳ giòn (brittle), nên cân nhắc đề xuất QA lead thêm testID/
  content-desc cho các số trên wheel để automation ổn định hơn.
- 2 case validate (Điểm đến trùng, Điểm xuất phát trống) KHÔNG có locator lỗi để assert vì app
  không hiển thị message — automation script chỉ assert được qua `enabled` attribute của nút
  "Đăng tin ngay", không assert được nội dung lỗi cụ thể.

---

# Bổ sung từ VR-002 (module Hoạt động)

## Page: Bottom Navigation (toàn app)

| Element | Action Used | Locator Strategy | Locator Value | Verified | MCP call ref | TC refs |
|---------|------------|-------------------|----------------|----------|---------------|---------|
| Tab "Trang chủ" | tap / verify | -android uiautomator | `new UiSelector().text("Trang chủ")` | ✅ | VR-002 mcp-log #3 | TC_01.1, TC_01.3 |
| Tab "Bảng tin" | verify | -android uiautomator | `new UiSelector().text("Bảng tin")` | ✅ | VR-002 mcp-log #5 | TC_01.1 |
| Tab "Đăng tin" (+ nút giữa) | verify | -android uiautomator | `new UiSelector().text("Đăng tin")` | ✅ | VR-002 mcp-log #7 | TC_01.1 |
| Tab "Hoạt động" | tap / verify | -android uiautomator | `new UiSelector().text("Hoạt động")` | ✅ | VR-002 mcp-log #1, #4 | TC_01.1, TC_01.3 |
| Tab "Cá nhân" | verify | -android uiautomator | `new UiSelector().text("Cá nhân")` | ✅ | VR-002 mcp-log #6 | TC_01.1 |

## Page: Hoạt động — Đơn của tôi (/activity)

| Element | Action Used | Locator Strategy | Locator Value | Verified | MCP call ref | TC refs |
|---------|------------|-------------------|----------------|----------|---------------|---------|
| Tab switcher "Đang diễn ra" | tap / verify | -android uiautomator | `new UiSelector().text("Đang diễn ra")` | ✅ | VR-002 mcp-log #8, #16, #27 | TC_01.2, TC_01.3, TC_01.4 |
| Tab switcher "Đã hoàn thành" | tap / verify | -android uiautomator | `new UiSelector().text("Đã hoàn thành")` | ✅ | VR-002 mcp-log #9, #20 | TC_01.2, TC_01.5, TC_01.20 |
| Order card (bất kỳ trạng thái) | tap / verify | -android uiautomator | `new UiSelector().descriptionContains("<Badge trạng thái>")` — vd `descriptionContains("Chờ ghép")`. Toàn bộ card là 1 accessibility node, content-desc gộp: `"Nhận: <tên tin>, <badge trạng thái>, Từ: <điểm đi>, Đến: <điểm đến>, Chạm để theo dõi đơn của bạn"` | ✅ | VR-002 mcp-log #22, #24, #29, #33, #35, #37 | TC_01.4, 6, 7, 8, 12, 13, 14, 15 |
| Empty state icon (pulse/nhịp tim, SVG) | verify (visual only) | (SVG, không có accessibility name riêng) | không có locator text | ⚠️ Inferred | VR-002 mcp-log #19 | TC_01.20 |
| Empty state text "Chưa có đơn nào" | verify | -android uiautomator | `new UiSelector().text("Chưa có đơn nào")` | ✅ | VR-002 mcp-log #19 | TC_01.20 |

## Page: Theo dõi đơn (đích điều hướng khi tap order card từ Hoạt động)

| Element | Action Used | Locator Strategy | Locator Value | Verified | MCP call ref | TC refs |
|---------|------------|-------------------|----------------|----------|---------------|---------|
| Header "Theo dõi đơn" | verify | -android uiautomator | `new UiSelector().text("Theo dõi đơn")` | ✅ | VR-002 mcp-log #23, #30, #34, #36 | TC_01.13, 14, 15 |
| Stepper 5 bước | verify (text list) | -android uiautomator | text nodes: "Chờ ghép", "Lấy hàng", "Đang giao", "Đã giao", "Hoàn thành" | ✅ | VR-002 mcp-log #23 | TC_01.13 |

## Navigation Flow bổ sung (VR-002)

| From | Trigger | To | MCP-verified |
|------|---------|-----|--------------|
| (any tab) | tap "Trang chủ" rồi tap "Hoạt động" | Hoạt động — tab "Đang diễn ra" (default) | TC_01.3 |
| Hoạt động / tab "Đang diễn ra" | tap card "Chờ ghép"/"Đã ghép"/"Đang giao" | **Theo dõi đơn** (KHÔNG phải "Chi tiết tin") | TC_01.13, 14, 15 |
| Hoạt động / tab "Đang diễn ra" | tap tab "Đã hoàn thành" | Empty state "Chưa có đơn nào" (data account test hiện tại) | TC_01.20 |

**Giá trị bổ sung cho implement-automation (module Hoạt động):**
- Card đơn là 1 accessibility node duy nhất — chỉ click nguyên card được, KHÔNG click riêng
  từng field con.
- Card content-desc KHÔNG có trường ngày/thời gian nào (xem TC_01.8 FAIL trong vibe-report VR-002).
- Tap card LUÔN vào "Theo dõi đơn", KHÔNG phải "Chi tiết tin" — automation nên assert đích
  "Theo dõi đơn"; TC-MASTER TC_01.13/14/15 cần review lại expected result.
- Dữ liệu đơn là mock ngẫu nhiên hoá mỗi lần load lại màn — automation cần assert theo
  badge/content-desc pattern, KHÔNG hardcode index cố định.

---

# Bổ sung từ Thongbao_VR-006 — Round 1 (module Thông báo, gốc VR-003-2026-08-04, đã merge + xoá folder gốc)

## Page: Trang chủ → icon chuông

| Element | Action Used | Locator Strategy | Locator Value | Verified | MCP call ref | TC refs |
|---------|------------|-------------------|----------------|----------|---------------|---------|
| Icon chuông (bell, có badge đỏ khi có unread) | tap | accessibility id | `Thông báo` | ✅ | VR-003 mcp-log #7-8 | entry flow |

## Page: Thông báo (danh sách)

| Element | Action Used | Locator Strategy | Locator Value | Verified | MCP call ref | TC refs |
|---------|------------|-------------------|----------------|----------|---------------|---------|
| Header text | verify | text (TextView) | `Thông báo` | ✅ | VR-003 mcp-log #10 | TC_03.17 |
| Icon quay lại (header) | tap | xpath (KHÔNG có content-desc/id) | `//*[@bounds="[42,149][137,244]"]` | ✅ | VR-003 mcp-log #45-46 | TC_03.18 |
| Nút "Đánh dấu đã đọc" (mark-all-read, **tự ẩn khi 0 unread**) | tap | accessibility id | `Đánh dấu đã đọc` | ✅ | VR-003 mcp-log #33-34 | TC_03.21, 23 |
| Group header thời gian | verify | text (TextView) | `HÔM NAY` / `HÔM QUA` | ✅ | VR-003 mcp-log #10 | TC_03.17 |
| Card thông báo (mỗi card unique) | tap | **id (uiautomator resourceId)** | `notif-item-<uuid>` (uuid đổi mỗi lần fetch, KHÔNG hardcode) | ✅ | VR-003 mcp-log #22-23, #37-38, #41-42 | TC_03.20, 22, 33, 35, 36 |
| Unread-dot (chỉ báo chưa đọc) | verify (page-source diff, không tap) | relative ViewGroup, `bounds="[986,Y][1007,Y+21]"` bên trong block `notif-item-*` | ✅ (gián tiếp) | VR-003 mcp-log #10, #26, #32, #35 | TC_03.20, 21, 22, 23 |

## Page: Theo dõi đơn (đích điều hướng từ card thông báo)

| Element | Action Used | Locator Strategy | Locator Value | Verified | MCP call ref | TC refs |
|---------|------------|-------------------|----------------|----------|---------------|---------|
| Header "Theo dõi đơn" | verify | text (TextView) | `Theo dõi đơn` | ✅ | VR-003 mcp-log #24, #39, #43 | TC_03.20, 33, 35, 36 |

## Navigation Flow bổ sung (Round 1, gốc VR-003)

| From | Trigger | To | MCP-verified |
|------|---------|-----|--------------|
| Trang chủ | tap icon chuông | Thông báo | entry flow |
| Thông báo | tap card "Đơn đã được giao" | Theo dõi đơn | TC_03.20, 36 |
| Thông báo | tap card "Đơn gửi tới bạn đã có người vận chuyển" | Theo dõi đơn | TC_03.33 |
| Thông báo | tap card "Người vận chuyển đã lấy hàng" | Theo dõi đơn | TC_03.35 |
| Theo dõi đơn | MCP back | Thông báo (state giữ nguyên) | TC_03.20, 22, 33, 35 |
| Thông báo | tap icon quay lại | Trang chủ | TC_03.18 |

**Giá trị bổ sung cho implement-automation (module Thông báo):**
- Đây là màn HIẾM HOI có `resource-id` thật — ưu tiên dùng thay vì content-desc.
- `content-desc` của card = tiêu đề thông báo, **trùng lặp** giữa nhiều card cùng loại (tài khoản
  test hiện có nhiều bản ghi lặp lại) → KHÔNG dùng content-desc để định vị 1 card cụ thể.
- Chỉ 3/9 loại thông báo (theo `test_scenario_map.md` / `MEMORY.md` §6.1 danh sách 9 loại) có mặt
  trong tài khoản test hiện tại: "Đơn đã được giao", "Đơn gửi tới bạn đã có người vận chuyển",
  "Người vận chuyển đã lấy hàng" — 6 loại còn lại cần tài khoản/orchestration khác để capture locator.
- Nút "Đánh dấu đã đọc" là **conditional element** — biến mất hoàn toàn khỏi DOM khi không còn
  thông báo chưa đọc, automation cần xử lý `try/catch` hoặc check tồn tại trước khi thao tác.

---

# Bổ sung từ VR-004 (module Cá nhân, 2 account: stag_TaiPM@fpt.com + stag_giangdc2@fpt.com)

## Page: Host App FoxPro — Login (Xác nhận OTP) + Cá nhân (Đăng xuất)

| Element | Action Used | Locator Strategy | Locator Value | Verified | MCP call ref | TC refs |
|---------|------------|-------------------|----------------|----------|---------------|---------|
| Email đăng nhập field | type | xpath | `//*[@text='Nhập email đăng nhập']` | ✅ | VR-004 mcp-log #17-24 | login flow |
| Nút "NHẬN MÃ OTP" | tap | xpath | `//*[@text='NHẬN MÃ OTP']` | ✅ | VR-004 mcp-log #17-24 | login flow |
| OTP input field | type | xpath | `//android.widget.EditText` | ✅ | VR-004 mcp-log #17-24 | login flow |
| Nút "ĐĂNG NHẬP" | tap | xpath | `//*[@text='ĐĂNG NHẬP']` | ✅ | VR-004 mcp-log #17-24 | login flow |
| Menu "Đăng xuất" (host app, cần scroll) | scroll_to_element + tap | xpath | `//*[@text='Đăng xuất']` | ✅ | VR-004 mcp-log #17-24 | logout flow |
| Dialog "Đồng ý" (confirm đăng xuất) | tap | xpath | `//*[@text='Đồng ý']` | ✅ | VR-004 mcp-log #17-24 | logout flow |
| Tile "FoxEco" (entry point SDK, trong tab "Chức năng", cần scroll) | scroll_to_element + tap | xpath | `//*[@text='FoxEco']` | ✅ | VR-004 mcp-log #8-9 | navigation — SDK entry |

⚠️ Tile "FoxGrowth" (`//*[@text='FoxGrowth']`) nằm gần "FoxEco" trong list host app — module điểm thưởng KHÁC, dễ tap nhầm. KHÔNG dùng cho FoxEco automation.

## Page: FoxEco — Cá nhân (màn chính)

| Element | Action Used | Locator Strategy | Locator Value | Verified | MCP call ref | TC refs |
|---------|------------|-------------------|----------------|----------|---------------|---------|
| Menu "Đơn của tôi" | tap | accessibility id | `profile-menu-activity` | ✅ | VR-004 mcp-log #12, #28 | TC_02.8 |
| Menu "Quà đã nhận" | tap | accessibility id | `profile-menu-gifts` | ✅ | VR-004 mcp-log #14, #25 | TC_02.9 |
| Header back "Quay lại" (chung mọi sub-page FoxEco) | tap | accessibility id | `Quay lại` | ✅ | VR-004 mcp-log #16, #27 | TC_02.15 |
| Stat "quà đã nhận" (số, clickable — dẫn tới cùng đích với menu) | (chưa exercise action riêng) | accessibility id | `profile-stat-gifts` | ⚠️ Inferred | VR-004 mcp-log #11 | — |
| Text tên user / phòng ban | verify | — (KHÔNG có resource-id, text thuần) | dynamic theo user | ✅ | VR-004 mcp-log #11 | TC_02.1, 2, 3 |

## Page: FoxEco — Quà đã nhận

| Element | Action Used | Locator Strategy | Locator Value | Verified | MCP call ref | TC refs |
|---------|------------|-------------------|----------------|----------|---------------|---------|
| Title header | verify | id | `gifts-received-title` | ✅ | VR-004 mcp-log #15 | TC_02.11, 16 |
| Empty state title | verify | — (text thuần, không id) | `"Hiện tại chưa có dữ liệu"` — xác nhận đúng hành vi thật (2026-08-05, không phải bug), Expected TC đã sửa lại khớp | ✅ | VR-004/VR-007 mcp-log | TC_02.11 (PASS) |
| Empty state subtitle | verify | — (text thuần) | `"Quà bạn nhận được từ đồng nghiệp sẽ hiện ở đây"` | ✅ | VR-004 mcp-log #15 | TC_02.11 |
| Card đếm số theo loại quà | verify | — (text thuần, mỗi loại 1 block) | vd `"☕ Ly cà phê — 1"` | ✅ | VR-004 mcp-log #26 | TC_02.12, 13, 16 |
| Danh sách "LỊCH SỬ NHẬN QUÀ" (mỗi item) | verify | — (text thuần, không id) | `"<loại quà> · <người tặng> · <thời điểm>"` | ✅ | VR-004 mcp-log #26 | TC_02.12, 17 |

## Page: FoxEco — Đơn của tôi

| Element | Action Used | Locator Strategy | Locator Value | Verified | MCP call ref | TC refs |
|---------|------------|-------------------|----------------|----------|---------------|---------|
| Title "Đơn của tôi" | verify | — (text thuần) | `"Đơn của tôi"` | ✅ | VR-004 mcp-log #12, #29 | TC_02.8 |
| Tab "Đang diễn ra" / "Đã hoàn thành" | (chưa exercise) | — (content-desc = text) | `"Đang diễn ra"` / `"Đã hoàn thành"` | ⚠️ Inferred | VR-004 mcp-log #12 | — |

## Navigation Flow bổ sung (VR-004)

| From | Trigger | To | MCP-verified |
|------|---------|-----|--------------|
| Host FoxPro "Chức năng" | tap tile "FoxEco" | FoxEco "Trang chủ" | VR-004 mcp-log #9 |
| FoxEco (bất kỳ tab) | tap bottom-nav "Cá nhân" | FoxEco "Cá nhân" | VR-004 mcp-log #10 |
| FoxEco "Cá nhân" | tap `profile-menu-activity` | FoxEco "Đơn của tôi" | TC_02.8 |
| FoxEco "Cá nhân" | tap `profile-menu-gifts` | FoxEco "Quà đã nhận" | TC_02.9 |
| FoxEco "Quà đã nhận" | tap "Quay lại" | FoxEco "Cá nhân" | TC_02.15 |
| Host FoxPro "Cá nhân" | tap "Đăng xuất" → confirm "Đồng ý" | Host FoxPro Login screen | logout flow |
| Host FoxPro Login | nhập email + OTP → "ĐĂNG NHẬP" | Host FoxPro "Trang chủ" (logged in) | login flow |

**Giá trị bổ sung cho implement-automation (module Cá nhân):**
- Khác với các module khác (Compose, hầu như không id), màn Cá nhân + Quà đã nhận CÓ
  `accessibility id`/`resource-id` thật cho element tương tác chính (`profile-menu-activity`,
  `profile-menu-gifts`, `profile-stat-gifts`, `gifts-received-title`) — ưu tiên dùng trực tiếp,
  ổn định hơn hẳn text-based locator.
- Các trường text thuần (tên, phòng ban, empty-state, card quà, lịch sử) KHÔNG có resource-id —
  automation cần xpath theo text hoặc theo vị trí tương đối.
- Entry point SDK đổi tuỳ context: từ host app phải qua tab "Chức năng" → tile "FoxEco" (không phải
  từ tab "Cá nhân" của host app — tab đó chỉ có menu riêng của host app, bao gồm "FoxGrowth" dễ
  nhầm lẫn).
- Empty-state title màn "Quà đã nhận" = text "Hiện tại chưa có dữ liệu" — **xác nhận 2026-08-05:
  đây là hành vi ĐÚNG, KHÔNG phải bug** (khác với ghi nhận tạm thời trước đó dựa trên ảnh chụp
  2026-07-31 ghi "Chưa có quà nào"). Automation cho TC_02.11 nên assert cố định theo text
  "Hiện tại chưa có dữ liệu".

---

# Bổ sung từ Thongbao_VR-006 — Round 2 (module Thông báo — TC_03, retest, account "Phan Minh Tài")

## Page: Trang chủ → icon chuông

| Element | Action Used | Locator Strategy | Locator Value | Verified | MCP call ref | TC refs |
|---------|------------|-------------------|----------------|----------|---------------|---------|
| Icon chuông (bell) | tap | accessibility id | `Thông báo` | ✅ (re-verify) | VR-006 mcp-log #6-7 | entry flow |

## Page: Thông báo (danh sách) — 2 locator mới (loại thông báo mới xuất hiện so với VR-003)

| Element | Action Used | Locator Strategy | Locator Value | Verified | MCP call ref | TC refs |
|---------|------------|-------------------|----------------|----------|---------------|---------|
| Card "Đơn đã bị huỷ" | tap | id (uiautomator resourceId) | `notif-item-<uuid>` (uuid đổi mỗi lần fetch, KHÔNG hardcode — ví dụ đã capture: `019fd040-c13d-70d7-ae3d-010e42304a79`) | ✅ | VR-006 mcp-log #19-21 | TC_03.39 |
| Card "Đơn đã hoàn tất" | tap | id (uiautomator resourceId) | `notif-item-<uuid>` (ví dụ đã capture: `019fcb8c-fc15-7ef0-80a6-3b9725c63a72`) | ✅ | VR-006 mcp-log #27-29 | TC_03.37 |

> Nay đã xác nhận **5/9 loại thông báo** (theo bảng 9 loại `MEMORY.md` §6.1) có mặt trong lịch sử tài
> khoản test: "Đơn đã được giao", "Đơn gửi tới bạn đã có người vận chuyển", "Người vận chuyển đã lấy
> hàng" (VR-003) + "Đơn đã bị huỷ", "Đơn đã hoàn tất" (VR-006, mới). Còn 4 loại chưa xuất hiện: "Đã có
> người nhận mang giúp", "Ghép thành công", "Tìm thấy đơn hàng phù hợp tuyến đường", "Bạn nhận được 1
> món quà cảm ơn" — vẫn cần multi-device/account khác để capture (xem TC_03.31/32/34/38).

## Navigation Flow bổ sung (VR-006)

| From | Trigger | To | MCP-verified |
|------|---------|-----|--------------|
| Thông báo | tap card "Đơn đã bị huỷ" | Theo dõi đơn (banner đỏ "Đơn hàng đã bị huỷ") | TC_03.39 |
| Thông báo | tap card "Đơn đã hoàn tất" | Theo dõi đơn (timeline "Hoàn thành") | TC_03.37 |

**Giá trị bổ sung cho implement-automation:**
- Cơ chế load-more (scroll-to-bottom) xác nhận hoạt động đúng qua nhiều batch (HÔM NAY → HÔM QUA →
  TUẦN NÀY), không trùng lặp item — an toàn để automate TC_03.25/26/27 bằng scroll lặp + so sánh số
  lượng `notif-item-*` trước/sau.
- KHÔNG có UI indicator "đã hết dữ liệu" — automation cho TC_03.26 nên assert theo "không tăng thêm
  item sau N lần scroll liên tiếp", KHÔNG assert theo text cụ thể (không tồn tại).
- Dữ liệu tài khoản "Phan Minh Tài" biến động mạnh giữa các ngày (tài khoản dùng chung nhiều tester)
  — automation cho các TC phụ thuộc loại thông báo cụ thể (TC_03.29-39) nên có bước discover/skip nếu
  loại thông báo cần thiết chưa xuất hiện, thay vì hardcode phải luôn có.

---

## Module: Cá nhân (TC_02) — Profile_VR-007-2026-08-05 (merged Round 1+2+3, 17/17 TC)

> Folder này gộp Round 1+2 (gốc `VR-004-2026-08-04`, đã xoá sau merge) + Round 3 (chạy trực tiếp trong
> folder này). Account chính: `stag_giangdc2@fpt.com` (5 đơn/5 quà, Round 3). Account phụ dùng để phủ
> precondition "0 đơn/0 quà": `stag_TaiPM@fpt.com` (dùng cả Round 1 và Round 3). Chi tiết đầy đủ +
> audit trail: xem `08_test-runs/vibe/Profile_VR-007-2026-08-05/vibe-locators.md` + `mcp-session-log.md`.
> Kết quả tích luỹ: 12 PASS / 3 FAIL (BUG-003/FE-148) / 2 BLOCKED (thiếu test data).

### Page: Cá nhân (SDK FoxEco — profile tab)

| Element | Action Used | Locator Strategy | Locator Value | Verified | MCP call ref | TC refs |
|---------|------------|-------------------|----------------|----------|---------------|---------|
| Bottom nav "Cá nhân" tab | tap | accessibility id | `Cá nhân` | ✅ | VR-007 mcp-log #6-7 | TC_02.1 |
| Menu "Quà đã nhận" | tap | accessibility id | `profile-menu-gifts` | ✅ | VR-007 mcp-log #12-13 | TC_02.9, TC_02.11, TC_02.13, TC_02.14, TC_02.17 |
| Nút "Chỉnh sửa" (không tồn tại — đúng kỳ vọng) | verify absence | -android uiautomator | `new UiSelector().textContains("Chỉnh sửa")` | 🚫 NOT FOUND (expected) | VR-007 mcp-log #9 | TC_02.1 |

### Page: Quà đã nhận (SDK FoxEco)

| Element | Action Used | Locator Strategy | Locator Value | Verified | MCP call ref | TC refs |
|---------|------------|-------------------|----------------|----------|---------------|---------|
| Icon "Quay lại" | tap | accessibility id | `Quay lại` | ✅ | VR-007 mcp-log #16-17 | TC_02.15 |
| Title screen | verify | resource-id | `gifts-received-title` | ✅ | VR-007 mcp-log #15 | TC_02.11 |

### Navigation Flow

| From | Trigger | To | MCP-verified |
|------|---------|-----|--------------|
| SDK Cá nhân | tap accessibility id "profile-menu-gifts" | SDK Quà đã nhận | TC_02.9 |
| SDK Quà đã nhận | tap accessibility id "Quay lại" | SDK Cá nhân | TC_02.15 |

**Giá trị bổ sung cho implement-automation:**
- `profile-menu-gifts` là accessibility id ổn định (content-desc), KHÔNG dùng strategy `id` (resource-id không set trên element này, chỉ set content-desc).
- Header "phòng ban" hiện KHÔNG chứa MNV ở bất kỳ account nào test được (Giang lẫn TaiPM) — automation cho TC_02.2/02.3 nên assert THEO BUG-003/FE-148 hiện trạng (Fail expected) cho tới khi dev fix, tránh false-negative liên tục.
- Empty-state "Quà đã nhận" dùng text "Hiện tại chưa có dữ liệu" — **user xác nhận 2026-08-05 đây là hành vi đúng, không phải bug**; Expected Result của TC_02.11 đã sửa lại khớp. Automation nên assert cố định theo text này.
