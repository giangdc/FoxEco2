# Vibe Test Log — VR-002 — v1.0 — 2026-08-03 (module Hoạt động)

> Platform: mobile (Android, Appium MCP, UiAutomator2) — app FoxEco SDK trong FoxPro STG.
> Tiếp tục phiên vibe-test cùng ngày (emulator + app đã mở sẵn theo yêu cầu user).
> Dữ liệu đơn hàng trong tài khoản test là **mock ngẫu nhiên hoá mỗi lần load lại màn Hoạt động**
> (badge/thứ tự card đổi khác nhau giữa các lần điều hướng) — ghi chú riêng cho từng TC nếu ảnh hưởng.

---

## TC_01.1: Check bottom nav đủ 5 tab và "Hoạt động" highlight đúng khi đang ở màn này

| # | Step | Action | Result | Notes |
|---|------|--------|--------|-------|
| 1 | Mở app FoxEco | (app đã mở sẵn) | ✅ PASS | — |
| 2 | Bấm "Hoạt động" tại bottom nav | (đã ở màn Hoạt động sẵn) | ✅ PASS | — |
| 3 | Quan sát thanh bottom nav | find_element × 5 tab | ✅ PASS | Cả 5 tab tồn tại: Trang chủ, Bảng tin, Đăng tin (nút +), Hoạt động, Cá nhân |
| E1 | Đủ 5 tab, "Hoạt động" highlight cam, 4 tab khác không highlight | Screenshot xác nhận màu cam trên tab "Hoạt động" | ✅ PASS | `selected` attribute = false cho cả 2 elem kiểm tra (Compose không expose qua attribute), verify bằng màu sắc screenshot |

**Result: ✅ PASS (3 steps, 1 expected)**
**Screenshot:** `screenshots/TC_01.1_final.png` (đã có từ phiên trước, vẫn hợp lệ)

---

## TC_01.2: Check hiển thị đủ 2 tab "Đang diễn ra"/"Đã hoàn thành" tại màn Hoạt động

| # | Step | Action | Result | Notes |
|---|------|--------|--------|-------|
| 1-2 | Mở app, bấm Hoạt động | (đã ở màn) | ✅ PASS | — |
| 3 | Quan sát khu vực tab switcher | find_element × 2 | ✅ PASS | "Đang diễn ra" + "Đã hoàn thành" đều tồn tại đúng label |

**Result: ✅ PASS**
**Screenshot:** `screenshots/TC_01.2_TC_01.3_TC_01.6_TC_01.7_TC_01.12_final.png`

---

## TC_01.3: Check tab mặc định khi mới vào màn Hoạt động là "Đang diễn ra" (state PRISTINE)

| # | Step | Action | Result | Notes |
|---|------|--------|--------|-------|
| 1 | Mở app FoxEco | tap "Trang chủ" (rời màn Hoạt động để tạo lại điều kiện pristine) | ✅ PASS | — |
| 2 | Bấm "Hoạt động" tại bottom nav lần đầu | tap elem "Hoạt động" | ✅ PASS | — |
| 3 | Quan sát tab đang chọn | Screenshot | ✅ PASS | Tab "Đang diễn ra" có nền trắng (active), "Đã hoàn thành" nền cam nhạt (inactive) — đúng mặc định |

**Result: ✅ PASS**
**Screenshot:** `screenshots/TC_01.2_TC_01.3_TC_01.6_TC_01.7_TC_01.12_final.png`

---

## TC_01.4: Check dữ liệu đúng tại tab "Đang diễn ra"

| # | Step | Action | Result | Notes |
|---|------|--------|--------|-------|
| 1-3 | Mở app, vào Hoạt động, tab Đang diễn ra | (đã active) | ✅ PASS | — |
| 4 | Quan sát toàn bộ danh sách (scroll hết) | get_page_source + scroll × 2 | ❌ FAIL | Danh sách gồm: nhiều card "Chờ ghép", "Đã ghép", "Đang giao" (đúng theo spec) **+ 1 card badge "Đã giao"** ở cuối danh sách — "Đã giao" KHÔNG nằm trong set trạng thái hợp lệ mà TC quy định cho tab này (Chờ ghép/Đã ghép/Đang giao/Đã huỷ) |

**Result: ❌ FAIL**
**Expected:** Danh sách CHỈ chứa đơn Chờ ghép/Đã ghép/Đang giao/Đã huỷ
**Actual:** Có thêm 1 card trạng thái "Đã giao" (không thuộc set trên)
**Note quan trọng:** Stepper ở màn "Theo dõi đơn" cho thấy flow thực tế có 5 bước: Chờ ghép → Lấy hàng → Đang giao → **Đã giao** → Hoàn thành. "Đã giao" (delivered, chờ xác nhận hoàn tất) có thể là trạng thái hợp lệ trung gian mà TC-MASTER chưa liệt kê — **cần BA/PO xác nhận** đây là gap của TC (thêm "Đã giao" vào set hợp lệ của tab "Đang diễn ra") hay là bug phân loại sai tab. KHÔNG tự log bug — xem khuyến nghị trong vibe-report.
**Screenshot:** `screenshots/TC_01.4_dagiao_in_dangdienra_FAIL.png`

---

## TC_01.5: Check dữ liệu đúng tại tab "Đã hoàn thành"

| # | Step | Action | Result | Notes |
|---|------|--------|--------|-------|
| 1-3 | Mở app, vào Hoạt động, tab Đã hoàn thành | tap tab | 🚫 BLOCKED | Tab hoàn toàn rỗng (0 đơn) — tài khoản test hiện không có đơn Hoàn thành/Hết hạn nào để verify data-filter |
| 4 | Quan sát danh sách | — | 🚫 BLOCKED | Không có dữ liệu để kiểm tra "CHỈ chứa Hoàn thành/Hết hạn" |

**Result: 🚫 BLOCKED — thiếu test data (tab Đã hoàn thành rỗng)**
**Screenshot:** `screenshots/TC_01.20_empty_final.png` (cùng bằng chứng với TC_01.20)

---

## TC_01.6: Check đơn trạng thái "Đã ghép" hiển thị tại tab "Đang diễn ra"

| # | Step | Action | Result | Notes |
|---|------|--------|--------|-------|
| 1-4 | Mở app, vào Hoạt động, tab Đang diễn ra, tìm card "Đã ghép" | find_element descriptionContains("Đã ghép") | ✅ PASS | Card tồn tại, badge hiển thị đúng "Đã ghép" (màu tím) |

**Result: ✅ PASS**
**Screenshot:** `screenshots/TC_01.2_TC_01.3_TC_01.6_TC_01.7_TC_01.12_final.png`

---

## TC_01.7: Check đơn trạng thái "Đang giao" hiển thị tại tab "Đang diễn ra"

| # | Step | Action | Result | Notes |
|---|------|--------|--------|-------|
| 1-4 | Tương tự TC_01.6, tìm card "Đang giao" | find_element descriptionContains("Đang giao") | ✅ PASS | Card tồn tại, badge đúng "Đang giao" (màu cam nhạt) |

**Result: ✅ PASS**
**Screenshot:** `screenshots/TC_01.2_TC_01.3_TC_01.6_TC_01.7_TC_01.12_final.png`

---

## TC_01.8: Check đầy đủ + đúng 5 trường hiển thị trên 1 card đơn tại màn Hoạt động

| # | Step | Action | Result | Notes |
|---|------|--------|--------|-------|
| 1-2 | Mở app, vào Hoạt động | (đã ở màn) | ✅ PASS | — |
| 3 | Quan sát 1 card bất kỳ | get_page_source, đọc content-desc đầy đủ | ❌ FAIL | Card chỉ có 4/5 trường: (1) icon trạng thái — có (SVG, thể hiện qua màu badge), (2) tên tin — có ("Nhận: ..."), (3) tuyến Từ→Đến — có, (5) badge trạng thái — có. **(4) ngày — HOÀN TOÀN KHÔNG CÓ**, đã kiểm tra content-desc gộp đầy đủ của nhiều card khác nhau, không có bất kỳ chuỗi ngày/tháng nào |

**Result: ❌ FAIL**
**Expected:** Card hiển thị đủ 5 trường gồm cả (4) ngày
**Actual:** Card chỉ có 4 trường, thiếu hẳn trường ngày
**Screenshot:** `screenshots/TC_01.2_TC_01.3_TC_01.6_TC_01.7_TC_01.12_final.png` (card mẫu, không có ngày ở đâu cả)

---

## TC_01.9: Check tin tự động chuyển "Hết hạn" khi quá "Đến ngày"

🚫 **BLOCKED** — cần đăng tin NEED mới với "Đến ngày" set rất gần rồi chờ hệ thống tự chuyển trạng thái (cron/scheduled job phía backend). Không khả thi trong phạm vi 1 phiên vibe-test UI-only (không có quyền chỉnh giờ hệ thống backend hoặc tạo dữ liệu với "Đến ngày" đã quá hạn ngay từ đầu). Đề xuất: cần a) tài khoản/API riêng để seed dữ liệu tin đã hết hạn sẵn, hoặc b) test thủ công có chờ thời gian thực.

---

## TC_01.10: Check tin CHƯA tự động chuyển "Hết hạn" (boundary ngay trước hạn)

🚫 **BLOCKED** — cùng lý do TC_01.9, cần dàn dựng dữ liệu boundary chính xác tới phút, không khả thi qua UI thông thường trong phạm vi run này.

---

## TC_01.11: Check card trạng thái "Hoàn thành" hiển thị đúng tại tab "Đã hoàn thành"

🚫 **BLOCKED** — tab "Đã hoàn thành" rỗng, không có đơn COMPLETED nào trong tài khoản test (xem TC_01.5/TC_01.20).

---

## TC_01.12: Check card trạng thái "Chờ ghép" hiển thị đúng tại tab "Đang diễn ra"

| # | Step | Action | Result | Notes |
|---|------|--------|--------|-------|
| 1-2 | Mở app, vào Hoạt động, tab Đang diễn ra | find_element descriptionContains("Chờ ghép") | ✅ PASS | Card tồn tại, badge đúng "Chờ ghép" (màu xanh dương nhạt) |

**Result: ✅ PASS**
**Screenshot:** `screenshots/TC_01.2_TC_01.3_TC_01.6_TC_01.7_TC_01.12_final.png`

---

## TC_01.13: Check bấm vào card trạng thái "Chờ ghép" mở đúng màn Chi tiết tin

| # | Step | Action | Result | Notes |
|---|------|--------|--------|-------|
| 1 | Mở app, bấm Hoạt động | (đã ở màn) | ✅ PASS | — |
| 2 | Bấm vào card đơn "Chờ ghép" | tap elem descriptionContains("Chờ ghép") | ❌ FAIL | Điều hướng sang màn **"Theo dõi đơn"**, KHÔNG phải "Chi tiết tin" như TC yêu cầu |

**Result: ❌ FAIL (nghi ngờ TC-MASTER ghi sai expected result, không phải app bug)**
**Expected (TC hiện tại):** Điều hướng sang màn "Chi tiết tin"
**Actual:** Điều hướng sang màn "Theo dõi đơn"
**Bằng chứng ủng hộ đây là hành vi ĐÚNG theo thiết kế:** chính card đó có dòng chữ UI "Chạm để theo dõi đơn của bạn" — tức app tự mô tả hành vi tap là "theo dõi đơn", khớp với đích điều hướng thực tế quan sát được.
**Screenshot:** `screenshots/TC_01.13_theodoi_notchitiettin.png`

---

## TC_01.14: Check bấm vào card trạng thái "Đã ghép" mở đúng màn Chi tiết tin

| # | Step | Action | Result | Notes |
|---|------|--------|--------|-------|
| 1-2 | Bấm Hoạt động, bấm card "Đã ghép" | tap elem descriptionContains("Đã ghép") | ❌ FAIL | Cùng pattern TC_01.13 — vào "Theo dõi đơn" |

**Result: ❌ FAIL (cùng nguyên nhân TC_01.13)**
**Screenshot:** `screenshots/TC_01.14_theodoi_notchitiettin.png`

---

## TC_01.15: Check bấm vào card trạng thái "Đang giao" mở đúng màn Chi tiết tin

| # | Step | Action | Result | Notes |
|---|------|--------|--------|-------|
| 1-2 | Bấm Hoạt động, bấm card "Đang giao" | tap elem descriptionContains("Đang giao") | ❌ FAIL | Cùng pattern — vào "Theo dõi đơn" |

**Result: ❌ FAIL (cùng nguyên nhân TC_01.13)**
**Screenshot:** `screenshots/TC_01.15_theodoi_notchitiettin.png`

---

## TC_01.16: Check bấm vào card trạng thái "Hoàn thành" mở đúng màn Chi tiết tin

🚫 **BLOCKED** — không có card "Hoàn thành" trong tài khoản test (tab Đã hoàn thành rỗng).

---

## TC_01.17: Check bấm vào card trạng thái "Đã huỷ" mở đúng màn Chi tiết tin/Theo dõi đơn

🚫 **BLOCKED** — không có đơn "Đã huỷ" sẵn có. Đã thử tìm nút "Huỷ đơn" trên màn Theo dõi đơn (đơn Chờ ghép) để tự tạo dữ liệu nhưng KHÔNG thấy nút huỷ ở màn này trong phạm vi khảo sát (có thể do role tài khoản test hiện tại, hoặc luồng huỷ nằm ở màn khác — xem module Huỷ đơn CNL). Không đủ thời gian truy thêm trong run này.

---

## TC_01.18: Check bấm vào card "Hết hạn" không cho thao tác

🚫 **BLOCKED** — không có card "Hết hạn" trong dữ liệu hiện có.

---

## TC_01.19: Check empty state hiển thị khi tab "Đang diễn ra" rỗng

🚫 **BLOCKED** — tab "Đang diễn ra" của tài khoản test luôn có dữ liệu (nhiều đơn), không rỗng, không thể verify empty state cho tab này trong run.

---

## TC_01.20: Check empty state hiển thị khi tab "Đã hoàn thành" rỗng

| # | Step | Action | Result | Notes |
|---|------|--------|--------|-------|
| 1 | Mở app, bấm Hoạt động | (đã ở màn) | ✅ PASS | — |
| 2 | Mở tab "Đã hoàn thành" (không có đơn nào) | tap tab | ✅ PASS | Icon nhịp tim/pulse (SVG) + text "Chưa có đơn nào" hiển thị đúng — khớp 100% expected |

**Result: ✅ PASS**
**Screenshot:** `screenshots/TC_01.20_empty_final.png`

---

## TC_01.21: Check đơn trạng thái "Đã huỷ" hiển thị đúng dạng card tại tab "Đang diễn ra"

🚫 **BLOCKED** — cùng lý do TC_01.17, không tạo được đơn "Đã huỷ" trong phạm vi run (không tìm thấy nút huỷ đơn khả dụng từ tài khoản/role test hiện tại).

---

## Tổng kết run (module Hoạt động)

| Kết quả | Số lượng | TC |
|---------|----------|-----|
| ✅ PASS | 7 | TC_01.1, 2, 3, 6, 7, 12, 20 |
| ❌ FAIL | 5 | TC_01.4, 8, 13, 14, 15 |
| 🚫 BLOCKED | 9 | TC_01.5, 9, 10, 11, 16, 17, 18, 19, 21 |

**Tổng: 21 TC** (7 PASS · 5 FAIL · 9 BLOCKED)
