# Vibe Locators — v1.0 — Profile_VR-007-2026-08-05 (merged) — 2026-08-05

> Captured via Appium MCP. Gộp **Round 1+2** (gốc `VR-004-2026-08-04`, đã xoá folder gốc sau merge) +
> **Round 3** (chạy trực tiếp trong folder này).
> Mark legend: ✅ Verified (MCP find+action OK) · ⚠️ Inferred · 🚫 NOT FOUND · ⏳ Pending
> MCP session log: see mcp-session-log.md (audit trail, có section riêng cho Round 1+2 và Round 3)
> Platform: mobile (Android, UiAutomator2)

---

## ROUND 1 + 2 (2026-08-04 — gốc VR-004)

### Page: Host App FoxPro — Login (Xác nhận OTP)

| Element | Action Used | Strategy | Value | Verified | MCP call ref | TC refs |
|---------|------------|----------|-------|----------|--------------|---------|
| Email đăng nhập field | type | xpath | `//*[@text='Nhập email đăng nhập']` | ✅ | mcp-log (R1+2) #17-24 | login flow (Round 2 setup) |
| Nút "NHẬN MÃ OTP" | tap | xpath | `//*[@text='NHẬN MÃ OTP']` | ✅ | mcp-log (R1+2) #17-24 | login flow |
| OTP input field | type | xpath | `//android.widget.EditText` | ✅ | mcp-log (R1+2) #17-24 | login flow |
| Nút "ĐĂNG NHẬP" | tap | xpath | `//*[@text='ĐĂNG NHẬP']` | ✅ | mcp-log (R1+2) #17-24 | login flow |

### Page: Host App FoxPro — Cá nhân (tab riêng của host app, KHÔNG phải FoxEco)

| Element | Action Used | Strategy | Value | Verified | MCP call ref | TC refs |
|---------|------------|----------|-------|----------|--------------|---------|
| Bottom-nav "Cá nhân" | tap | xpath | `//*[@text='Cá nhân']` | ✅ | mcp-log (R1+2) #16-17 | navigation |
| Menu "Đăng xuất" | scroll_to_element + tap | xpath | `//*[@text='Đăng xuất']` | ✅ | mcp-log (R1+2) #17-24 | logout flow |
| Dialog "Đồng ý" (confirm đăng xuất) | tap | xpath | `//*[@text='Đồng ý']` | ✅ | mcp-log (R1+2) #17-24 | logout flow |
| Bottom-nav "Chức năng" | tap | xpath | `//*[@text='Chức năng']` | ✅ | mcp-log (R1+2) #8 | navigation |
| Tile "FoxEco" (entry point SDK) | scroll_to_element + tap | xpath | `//*[@text='FoxEco']` | ✅ | mcp-log (R1+2) #8-9 | navigation — SDK entry |

⚠️ Lưu ý: tile "FoxGrowth" (`//*[@text='FoxGrowth']`) — thử tap NHẦM lúc đầu, dẫn vào module điểm thưởng khác (KHÔNG phải FoxEco). Không dùng locator này cho FoxEco automation.

### Page: FoxEco SDK — bottom nav (chung mọi màn trong SDK)

| Element | Action Used | Strategy | Value | Verified | MCP call ref | TC refs |
|---------|------------|----------|-------|----------|--------------|---------|
| Tab "Cá nhân" (trong SDK) | tap | xpath | `//*[@text='Cá nhân']` | ✅ | mcp-log (R1+2) #10 | tất cả TC_02.x |
| Header back "Quay lại" (SDK) | tap | accessibility id | `Quay lại` | ✅ | mcp-log (R1+2) #16 | TC_02.15 |

### Page: FoxEco — Cá nhân (màn chính)

| Element | Action Used | Strategy | Value | Verified | MCP call ref | TC refs |
|---------|------------|----------|-------|----------|--------------|---------|
| Menu "Đơn của tôi" | tap | accessibility id | `profile-menu-activity` | ✅ | mcp-log (R1+2) #12 | TC_02.8 |
| Menu "Quà đã nhận" | tap | accessibility id | `profile-menu-gifts` | ✅ | mcp-log (R1+2) #14 | TC_02.9 |
| Stat "quà đã nhận" (số, clickable) | (not exercised) | accessibility id | `profile-stat-gifts` | ⚠️ Inferred | mcp-log (R1+2) #11 (found via get_page_source, chưa gọi find_element/tap riêng) | — |
| Text tên user | verify | — (no resource-id/accessibility id, chỉ có text) | text dynamic theo user | ✅ | mcp-log (R1+2) #11 | TC_02.1-3 |
| Text phòng ban | verify | — (no resource-id) | text dynamic theo user | ✅ | mcp-log (R1+2) #11 | TC_02.1-3 |

### Page: FoxEco — Quà đã nhận

| Element | Action Used | Strategy | Value | Verified | MCP call ref | TC refs |
|---------|------------|----------|-------|----------|--------------|---------|
| Title "Quà đã nhận" | verify | id | `gifts-received-title` | ✅ | mcp-log (R1+2) #15 | TC_02.11, 16 |
| Header back "Quay lại" | tap | accessibility id | `Quay lại` | ✅ | mcp-log (R1+2) #16 | TC_02.15 |
| Empty state title | verify | — (no resource-id, text-based) | `"Hiện tại chưa có dữ liệu"` — xác nhận đúng hành vi thật (2026-08-05, không phải bug), Expected TC đã sửa lại khớp | ✅ | mcp-log (R1+2/R3) | TC_02.11 (PASS, xem Round 3) |
| Empty state subtitle | verify | — (no resource-id, text-based) | "Quà bạn nhận được từ đồng nghiệp sẽ hiện ở đây" | ✅ | mcp-log (R1+2) #15 | TC_02.11 |

### Page: FoxEco — Đơn của tôi (đích điều hướng của TC_02.8)

| Element | Action Used | Strategy | Value | Verified | MCP call ref | TC refs |
|---------|------------|----------|-------|----------|--------------|---------|
| Title "Đơn của tôi" | verify | — (text-based) | "Đơn của tôi" | ✅ | mcp-log (R1+2) #12 | TC_02.8 |
| Tab "Đang diễn ra" / "Đã hoàn thành" | (not exercised) | — (content-desc match text) | "Đang diễn ra" / "Đã hoàn thành" | ⚠️ Inferred | mcp-log (R1+2) #12, #Round2 step | — |

### Navigation Flow (Round 1+2)

| From | Trigger | To | MCP-verified |
|------|---------|-----|--------------|
| Host FoxPro "Chức năng" | tap tile "FoxEco" | FoxEco "Trang chủ" | mcp-log (R1+2) #9 |
| FoxEco (bất kỳ tab) | tap bottom-nav "Cá nhân" | FoxEco "Cá nhân" | mcp-log (R1+2) #10 |
| FoxEco "Cá nhân" | tap `profile-menu-activity` | FoxEco "Đơn của tôi" | TC_02.8, mcp-log (R1+2) #12 |
| FoxEco "Cá nhân" | tap `profile-menu-gifts` | FoxEco "Quà đã nhận" | TC_02.9, mcp-log (R1+2) #14 |
| FoxEco "Quà đã nhận" | tap "Quay lại" | FoxEco "Cá nhân" | TC_02.15, mcp-log (R1+2) #16 |
| FoxEco "Trang chủ" | tap header "Quay lại" | Host FoxPro "Chức năng"/"Chang" | mcp-log (R1+2) #7-8 (exit SDK) |
| Host FoxPro "Cá nhân" | tap "Đăng xuất" → confirm "Đồng ý" | Host FoxPro Login screen | mcp-log (R1+2) #17-24 |
| Host FoxPro Login | nhập email + OTP → "ĐĂNG NHẬP" | Host FoxPro "Trang chủ" (logged in) | mcp-log (R1+2) #17-24 |

---

## ROUND 3 (2026-08-05 — Profile_VR-007)

### Page: Cá nhân (SDK FoxEco — profile tab)

| Element | Action Used | Strategy | Value | Verified | MCP call ref | TC refs |
|---------|------------|----------|-------|----------|--------------|---------|
| Bottom nav "Cá nhân" tab | tap | accessibility id | `Cá nhân` | ✅ | mcp-log (R3) #6-7 | TC_02.1 |
| Nút "Chỉnh sửa"/"Cập nhật" (kỳ vọng KHÔNG tồn tại) | verify absence | (tried) -android uiautomator | `new UiSelector().textContains("Chỉnh sửa")` | 🚫 NOT FOUND (đúng kỳ vọng) | mcp-log (R3) #9 | TC_02.1 |
| Menu "Quà đã nhận" | tap | accessibility id | `profile-menu-gifts` | ✅ | mcp-log (R3) #12-13 | TC_02.9, TC_02.11, TC_02.13, TC_02.14, TC_02.17 |
| Menu "Quà đã nhận" — id sai (tham khảo, KHÔNG dùng) | — | (tried) id | `profile-menu-gifts` | 🚫 NOT FOUND | mcp-log (R3) #11 | — |
| Header phòng ban text (thiếu MNV) | verify | -android uiautomator (text node) | text="Ban Giám đốc" (Giang) / "Phòng Phát triển Phần mềm số 8" (TaiPM) | ✅ | mcp-log (R3) #4, #46-49 | TC_02.1, TC_02.2, TC_02.3 |
| Chỉ số "đơn đã giúp"/"quà đã nhận" | verify | -android uiautomator (text node) | text="0"/"5" tuỳ account | ✅ | mcp-log (R3) #4, #49 | TC_02.4, TC_02.5, TC_02.6 |

### Page: Quà đã nhận (SDK FoxEco)

| Element | Action Used | Strategy | Value | Verified | MCP call ref | TC refs |
|---------|------------|----------|-------|----------|--------------|---------|
| Icon "Quay lại" | tap | accessibility id | `Quay lại` | ✅ | mcp-log (R3) #16-17 | TC_02.15 |
| Title screen | verify | resource-id | `gifts-received-title` | ✅ | mcp-log (R3) #15 | TC_02.11 |
| Card tổng số theo loại quà (4 loại) | verify | -android uiautomator (text nodes) | "Bông hoa"/"Ly cà phê"/"Gấu bông"/"Vương miện" + số lượng | ✅ | mcp-log (R3) #14 | TC_02.12, TC_02.13, TC_02.14, TC_02.16 |
| Danh sách "LỊCH SỬ NHẬN QUÀ" | verify | -android uiautomator (list items) | tên quà + người tặng + "Hôm nay/Hôm qua" + giờ | ✅ | mcp-log (R3) #14 | TC_02.17 |
| Empty state title (data=0) | verify | -android uiautomator (text node) | text="Hiện tại chưa có dữ liệu" — **xác nhận đúng hành vi thật (2026-08-05), KHÔNG phải bug** | ✅ | mcp-log (R3) #52 | TC_02.11 (PASS) |
| Empty state icon + subtitle | verify | -android uiautomator | icon hộp quà (svg) + "Quà bạn nhận được từ đồng nghiệp sẽ hiện ở đây" | ✅ | mcp-log (R3) #52 | TC_02.11 |

### Page: Host app FoxPro — Cá nhân (profile, ngoài SDK — dùng để switch account)

| Element | Action Used | Strategy | Value | Verified | MCP call ref | TC refs |
|---------|------------|----------|-------|----------|--------------|---------|
| Bottom nav "Cá nhân" (host) | tap | -android uiautomator | `new UiSelector().text("Cá nhân")` | ✅ | mcp-log (R3) #22-23, #58-59 | (support, không phải TC Cá nhân SDK) |
| Menu "Đăng xuất" | tap | -android uiautomator | `new UiSelector().textContains("Đăng xuất")` | ✅ | mcp-log (R3) #26-27, #61-62 | (support) |
| Confirm dialog "Đồng ý" | tap | -android uiautomator | `new UiSelector().text("Đồng ý")` | ✅ | mcp-log (R3) #29-30, #63-64 | (support) |
| Login — email field | type | -android uiautomator | `new UiSelector().className("android.widget.EditText")` (1st EditText trên màn login) | ✅ | mcp-log (R3) #32-33, #65-66 | (support) |
| Login — nút "NHẬN MÃ OTP" | tap | -android uiautomator | `new UiSelector().textContains("NHẬN MÃ OTP")` | ✅ | mcp-log (R3) #34-35, #67-68 | (support) |
| OTP — input field | type | -android uiautomator | `new UiSelector().className("android.widget.EditText")` (màn Xác nhận OTP) | ✅ | mcp-log (R3) #37-38, #69-70 | (support) |
| OTP — nút "ĐĂNG NHẬP" | tap | -android uiautomator | `new UiSelector().text("ĐĂNG NHẬP")` | ✅ | mcp-log (R3) #39-40, #71-72 | (support) |
| Chức năng grid — tile "FoxEco" | tap | -android uiautomator | `new UiSelector().textContains("FoxEco")` | ✅ | mcp-log (R3) #44-45 | (support — entry point SDK) |

### Navigation Flow (Round 3)

| From | Trigger | To | MCP-verified |
|------|---------|-----|--------------|
| SDK Cá nhân | tap accessibility id "profile-menu-gifts" | SDK Quà đã nhận | TC_02.9 |
| SDK Quà đã nhận | tap accessibility id "Quay lại" | SDK Cá nhân | TC_02.15 |
| SDK Cá nhân | BACK ×2 | SDK Trang chủ → host app "Chức năng" | mcp-log (R3) #18, #20 |
| Host "Chức năng" | tap "Cá nhân" nav | Host profile | mcp-log (R3) #22-23 |
| Host profile | scroll + tap "Đăng xuất" → "Đồng ý" | Login screen FoxPro | mcp-log (R3) #25-30 |
| Login screen | nhập email + "NHẬN MÃ OTP" | Màn "Xác nhận OTP" | mcp-log (R3) #32-36 |
| Xác nhận OTP | nhập mã "123QWE" + "ĐĂNG NHẬP" | Host Trang chủ (account mới) | mcp-log (R3) #37-41 |
| Host Trang chủ | tap "Chức năng" → tap "FoxEco" | SDK Trang chủ (account mới) | mcp-log (R3) #42-46 |

---

## Notes (tích luỹ cả 3 round)

- Locators `profile-menu-activity`, `profile-menu-gifts`, `Quay lại`, `gifts-received-title` đều là `accessibility id`/`id` ổn định (Android resource-id/content-desc), ưu tiên dùng trực tiếp cho `@AndroidFindBy(accessibilityId=...)`. Các text thuần (tên, phòng ban, empty-state) không có resource-id — automation cần dùng xpath theo text hoặc theo vị trí tương đối, dễ vỡ khi đổi ngôn ngữ/nội dung động.
- 2 element KHÔNG match ở Round 3 (🚫 NOT FOUND) đều là kết quả ĐÚNG kỳ vọng/tự sửa lỗi strategy, không phải app bug.
- Empty-state "Quà đã nhận" dùng text "Hiện tại chưa có dữ liệu" — **user xác nhận 2026-08-05 đây là hành vi đúng, không phải bug**; Expected Result của TC_02.11 đã sửa lại khớp. Automation nên assert cố định theo text này.
- Account "Phan Minh Tài" (`stag_TaiPM@fpt.com`) dùng ở cả 3 round để lấy state "0 đơn/0 quà" (TC_02.5/TC_02.11); ở Round 3 đã đăng xuất và khôi phục lại `stag_giangdc2@fpt.com` trước khi kết thúc run (khác Round 1+2, kết thúc ở account Giang mà không revert).
- 2026-08-05: đã merge folder `VR-004-2026-08-04` (Round 1+2 gốc) vào folder này (`Profile_VR-007-2026-08-05`) theo yêu cầu user — gộp đủ 4 file (vibe-report/vibe-log/vibe-locators/mcp-session-log) + 5 screenshot Round 1+2 vào đây, sau đó đã xoá folder `VR-004-2026-08-04` gốc.
