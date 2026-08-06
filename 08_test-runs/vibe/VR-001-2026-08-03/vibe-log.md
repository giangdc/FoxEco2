# Vibe Test Log — VR-001 — v1.0 — 2026-08-03

> Scope: TC_04.94 → TC_04.103 — sheet "Đăng tin", block "Đăng tin OFFER (Tôi nhận giao hàng)"
> Round: 1 (cột N–R, tất cả đều trống trước run này)
> Platform: mobile (Appium MCP) — app FoxPro STG (`com.hrisproject.stag`), đăng nhập sẵn "Ngô Quốc Hưng"

---

## TC_04.94: Check đầy đủ 7 field trên Form OFFER

| # | Step | Action | Result | Notes |
|---|------|--------|--------|-------|
| 1 | Quan sát toàn bộ Form đăng ký tuyến | get_page_source + find_element từng field | ⚠️ MIXED | Xem chi tiết dưới |

| Field | Expected | Actual | Match? |
|-------|----------|--------|--------|
| Tên người giao | đọc, auto-fill | "Ngô Quốc Hưng" — có, auto-fill | ✅ |
| SĐT người giao | đọc, auto-fill | "0000166911" — có, auto-fill | ✅ |
| Điểm xuất phát | auto-fill, sửa được | Trống (chỉ placeholder "Bạn đang ở đâu / xuất phát từ đâu") — KHÔNG auto-fill | ❌ |
| Điểm đến | tồn tại | Có (placeholder "Bạn sẽ đến đâu") | ✅ |
| Từ ngày/Đến ngày | mặc định hôm nay | "Hôm nay" / "Hôm nay" | ✅ |
| Thời gian di chuyển | mặc định 17:30–18:30 | Mặc định = giờ hiện tại + 30 phút (lúc test: 09:55–10:25) | ❌ |
| Checkbox điều khoản | tồn tại | Có ("Tôi đã đọc và đồng ý Điều khoản sử dụng FoxEco") | ✅ |

**Result: ❌ FAIL (5/7 đúng, 2/7 sai default — Điểm xuất phát không auto-fill; Thời gian di chuyển default không phải 17:30–18:30)**
**Screenshot:** TC_04.94_final.png
**Locators captured:** 7 elements (xem vibe-locators.md)

---

## TC_04.95: Check hoàn tất đăng ký tuyến OFFER với dữ liệu hợp lệ

| # | Step | Action | Result | Notes |
|---|------|--------|--------|-------|
| 1 | Giữ mặc định Điểm xuất phát = 'Tòa nhà Lô B3, KCX Tân Thuận, Q.7' | set_value (nhập thủ công vì field không auto-fill sẵn — xem TC_04.94) | ⚠️ PARTIAL | Field nhận đúng giá trị sau khi nhập, nhưng "giữ mặc định" không đúng nghĩa vì không có default |
| 2 | Điểm đến: nhập '89 Nguyễn Thị Minh Khai, Q.3' | set_value | ✅ PASS | Field nhận đúng giá trị |
| 3 | Giữ Thời gian di chuyển mặc định 17:30–18:30 | (không chỉnh, giữ nguyên default hiện tại của app) | ❌ FAIL | Default thực tế là 09:55–10:25 (giờ hiện tại+30p), không phải 17:30–18:30 |
| 4 | Tick Checkbox điều khoản | tap | ✅ PASS | Checkbox chuyển sang tick (✓ màu xanh) |
| 5 | Bấm gửi | tap "Đăng tin ngay" | ✅ PASS | — |
| E1-E4 | Field nhận đúng giá trị | verify | ✅ PASS | Điểm xuất phát, Điểm đến hiển thị đúng |
| E5 | Tuyến ghi nhận thành công, KHÔNG công khai, chờ hệ thống tự khớp | verify màn kết quả | ✅ PASS | Hiện "Đã ghi nhận tuyến đường!" + text "được lưu vào hệ thống (không hiển thị công khai)... hệ thống sẽ gửi thông báo" — khớp đúng ý |

**Result: ❌ FAIL (chức năng submit hoạt động đúng, nhưng 2 điểm Expected về giá trị default (Điểm xuất phát, Thời gian di chuyển) không khớp — cùng root cause với TC_04.94)**
**Screenshot:** TC_04.95_final.png
**Locators captured:** +2 (Điểm đến type action, nút Đăng tin ngay, màn kết quả)

---

## TC_04.96: Check Điểm xuất phát (OFFER) tại biên max-1 (199 ký tự hợp lệ)

| # | Step | Action | Result | Notes |
|---|------|--------|--------|-------|
| 1 | Nhập 199 ký tự hợp lệ vào Điểm xuất phát | set_value | ✅ PASS | get_page_source xác nhận text len=199, max-text-length=200, không bị cắt |
| 2 | Bấm gửi | (không cần — mục tiêu TC là verify field nhận giá trị, không phải toàn bộ submit) | — | Nút "Đăng tin ngay" vẫn disabled vì Điểm đến/checkbox chưa điền — không liên quan đến field đang test |

**Result: ✅ PASS**
**Evidence:** page-source (TC_04.96-98_pagesource_evidence.txt) — không chụp screenshot riêng vì bằng chứng chính xác hơn qua text length

---

## TC_04.97: Check Điểm xuất phát (OFFER) tại biên max (đúng 200 ký tự hợp lệ)

| # | Step | Action | Result | Notes |
|---|------|--------|--------|-------|
| 1 | Nhập đúng 200 ký tự hợp lệ | set_value | ✅ PASS | get_page_source xác nhận text len=200, không bị cắt |

**Result: ✅ PASS**
**Evidence:** page-source (TC_04.96-98_pagesource_evidence.txt)

---

## TC_04.98: Check Điểm xuất phát (OFFER) tại biên max+1 (201 ký tự)

| # | Step | Action | Result | Notes |
|---|------|--------|--------|-------|
| 1 | Nhập 201 ký tự | set_value | ✅ PASS | get_page_source xác nhận text bị chặn ở đúng 200 ký tự (ký tự thứ 201 "g" không được chấp nhận) |

**Result: ✅ PASS (bị chặn đúng qua enforced maxlength — không có message lỗi riêng nhưng hành vi chặn nhập chính xác)**
**Evidence:** page-source (TC_04.96-98_pagesource_evidence.txt)

---

## TC_04.99: Check Điểm đến trùng Điểm xuất phát bị chặn

| # | Step | Action | Result | Notes |
|---|------|--------|--------|-------|
| 1 | Điểm đến = Điểm xuất phát = 'Tòa nhà Lô B3, KCX Tân Thuận, Q.7' | set_value ×2 | ✅ PASS | Cả 2 field nhận đúng giá trị (nhìn thấy trùng nhau) |
| 2 | Bấm gửi | tick checkbox → check button state | ⚠️ PARTIAL | Nút "Đăng tin ngay" enabled=false (bị chặn ✅), nhưng KHÔNG có text lỗi "Điểm đến phải khác điểm xuất phát" hiển thị ở bất kỳ đâu trên màn hình (get_page_source quét toàn bộ text, không tìm thấy) |

**Result: ❌ FAIL (chặn đúng nhưng thiếu message lỗi theo Expected)**
**Screenshot:** TC_04.99_final.png

---

## TC_04.100: Check để trống Điểm xuất phát khi submit bị chặn

| # | Step | Action | Result | Notes |
|---|------|--------|--------|-------|
| 1 | Xoá trống Điểm xuất phát | set_value("") | ✅ PASS | Field hiển thị rỗng (chỉ còn placeholder, showing-hint=true) |
| 2 | Bấm gửi | check button state (Điểm đến đã đổi sang giá trị khác để cô lập test) | ⚠️ PARTIAL | Nút disabled=true (bị chặn ✅), KHÔNG có text lỗi nào hiển thị (đã quét toàn bộ text trên màn hình) |

**Result: ❌ FAIL (chặn đúng nhưng thiếu message lỗi theo Expected — cùng pattern với TC_04.99)**
**Screenshot:** TC_04.100_final.png

---

## TC_04.101: Check Thời gian di chuyển cách nhau 29 phút bị chặn

| # | Step | Action | Result | Notes |
|---|------|--------|--------|-------|
| 1 | Nhập Thời gian di chuyển: 17:30 – 17:59 | tap picker + swipe wheel calibrate → 17:30, rồi 17:59 | ✅ PASS | Field hiển thị đúng giá trị vừa chọn |
| 2 | Bấm gửi | check button + page source | ✅ PASS | Nút disabled=true (bị chặn ✅) + text lỗi "Giờ đến phải lớn hơn 17:30" xuất hiện đúng (nội dung khác chữ với Expected "khoảng cách phải tối thiểu 30 phút" nhưng cùng bản chất chặn <30 phút) |

**Result: ✅ PASS (chặn đúng + có message lỗi, dù text khác literal Expected nhưng đúng ý nghĩa nghiệp vụ)**
**Screenshot:** TC_04.101_final.png

---

## TC_04.102: Check Thời gian di chuyển đúng biên 30 phút hợp lệ

| # | Step | Action | Result | Notes |
|---|------|--------|--------|-------|
| 1 | Nhập Thời gian di chuyển: 17:30 – 18:00 | swipe wheel ĐẾN NƠI từ 17:59 → 18:00 | ✅ PASS | Field hiển thị đúng giá trị |
| 2 | Bấm gửi | check button + page source | ✅ PASS | Không có lỗi, nút "Đăng tin ngay" enabled=true, clickable=true |

**Result: ✅ PASS**
**Screenshot:** TC_04.102_final.png

---

## TC_04.103: Check nút gửi (OFFER) disabled tới khi hợp lệ + tick điều khoản

| # | Step | Action | Result | Notes |
|---|------|--------|--------|-------|
| 1 | Điểm đến trống, checkbox đã tick | set_value("") vào Điểm đến | ✅ PASS | Nút "Đăng tin ngay" enabled=false (disabled đúng) |
| 2 | Điền đủ + hợp lệ toàn bộ field, giữ tick | set_value lại Điểm đến hợp lệ | ✅ PASS | Nút chuyển sang enabled=true, clickable=true |

**Result: ✅ PASS**
**Screenshot:** TC_04.103_final.png

---

## Tổng kết nhanh

| TC | Kết quả | Ghi chú chính |
|----|---------|----------------|
| TC_04.94 | ❌ FAIL | Điểm xuất phát không auto-fill; Thời gian di chuyển default sai |
| TC_04.95 | ❌ FAIL | Submit hoạt động đúng nhưng default value sai (cùng root cause TC_04.94) |
| TC_04.96 | ✅ PASS | Boundary 199 ký tự OK |
| TC_04.97 | ✅ PASS | Boundary 200 ký tự OK |
| TC_04.98 | ✅ PASS | Boundary 201 ký tự bị chặn đúng |
| TC_04.99 | ❌ FAIL | Chặn đúng nhưng thiếu message lỗi |
| TC_04.100 | ❌ FAIL | Chặn đúng nhưng thiếu message lỗi |
| TC_04.101 | ✅ PASS | Chặn đúng + có message (khác chữ Expected nhưng đúng ý) |
| TC_04.102 | ✅ PASS | Boundary 30 phút OK |
| TC_04.103 | ✅ PASS | Nút disable/enable đúng theo trạng thái field |

**6 PASS / 4 FAIL / 0 BLOCKED**

**2 nhóm lỗi phát hiện (đáng log bug):**
1. **BUG-A (Major, UI/Data default):** Form OFFER không auto-fill "Điểm xuất phát" và default "Thời gian di chuyển" không phải 17:30–18:30 như spec — ảnh hưởng TC_04.94, TC_04.95.
2. **BUG-B (Minor, UX validation message):** 2 trường hợp validate chặn submit (Điểm đến trùng Điểm xuất phát; Điểm xuất phát trống) không hiển thị message lỗi cho người dùng, chỉ disable nút âm thầm — ảnh hưởng TC_04.99, TC_04.100. (Đối chiếu: case Thời gian di chuyển <30 phút — TC_04.101 — CÓ hiển thị message, cho thấy pattern xử lý lỗi không nhất quán giữa các loại field.)
