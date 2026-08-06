# Vibe Locators — v1.0 — VR-001 — 2026-08-03

> Captured via Appium MCP (UiAutomator2) during run này.
> Mark legend: ✅ Verified · ⚠️ Inferred · 🚫 NOT FOUND · ⏳ Pending
> MCP session log: xem `mcp-session-log.md`
> Platform: mobile (Android) — App: FoxEco SDK trong FoxPro STG, package `com.hrisproject.stag`
> ⚠️ App này gần như KHÔNG dùng `resource-id` (Compose UI) — locator thực tế chủ yếu dựa vào
> `-android uiautomator textContains/text(...)` hoặc `content-desc` (accessibility id), xpath là fallback cuối.

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
