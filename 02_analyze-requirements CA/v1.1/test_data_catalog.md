# Test Data Catalog — v1.1

> Tạo bởi: analyze-requirements (mode DELTA từ v1.0). Chỉ liệt kê field có dữ liệu MỚI hoặc THAY ĐỔI so với v1.0 — phần không đổi xem `02_analyze-requirements/v1.0/test_data_catalog.md`.
>
> **Structure-lock:** giữ nguyên 5 cột `| Field | Valid | Invalid | Boundary | Nguồn |` cho mọi module. KHÔNG đổi cột.

## Module SENDER — Wizard đăng tin (DOC-v1.1-01 §D8.1, §D8.3)

| Field | Valid | Invalid | Boundary | Nguồn |
|-------|-------|---------|----------|-------|
| Loại hàng | "Tài liệu" (mặc định, chip chọn 1 trong **8 mục theo UI**: Tài liệu/Đồ điện tử/Thực phẩm/Hàng nhỏ/Đồ dễ vỡ/Quần áo/Thuốc·Y tế/Khác — resolved, BRD 5-mục KHÔNG áp dụng) | *(không có invalid — chip select cố định, không cho để trống theo BRD)* | 8-way EP, không có boundary số. **"Thuốc/Y tế" xác nhận KHÔNG phải hàng cấm (C-SENDER-3 resolved)** — không cần P1 risk-flag | §D8.1, C-SENDER-3 |
| Ghi chú | text tự do, vd "Laptop trong túi, nhẹ tay" (≤300 ký tự) | *(không bắt buộc — không có invalid ngoài vượt boundary)* | **300 ký tự (hợp lệ), 301 ký tự (chặn — chưa verify UI enforce thế nào, spec-only)** | §D8.1 |
| Giá trị hàng | "Giá trị thấp" / "vừa" / "cao" (chọn 1, bắt buộc) | rỗng/chưa chọn (→ inline error "Vui lòng chọn giá trị hàng", **đã verify UI thật**) | *(3-way chip, không có boundary số)* | §D8.1, §D8.3 VAL-01/02 |
| Ảnh sản phẩm | 1 ảnh JPG/PNG (không bắt buộc) | *(sai định dạng/quá dung lượng — spec-only, chưa verify UI thật)* | **≤5MB (hợp lệ), >5MB (chặn — spec-only, chưa verify)**; chỉ 1 ảnh duy nhất (không multi-upload) | §D8.1 |
| Email công ty người nhận | email nội bộ hợp lệ, có trong hệ thống (→ tự điền tên/SĐT/địa chỉ, spec-only chưa verify UI thật vì thiếu data demo) | định dạng email sai, hoặc email không thuộc tên miền nội bộ (spec-only) | *(không có boundary ký tự nêu rõ)* | §D1b US-D18, §D8.1 |
| Tên người nhận | 2-60 ký tự, không rỗng | rỗng (→ bắt buộc nhập) | **2 ký tự (hợp lệ, chặn dưới), 60 ký tự (hợp lệ, chặn trên), 1/61 ký tự (chặn) — spec-only, chưa verify UI enforce** | §D8.1 |
| Số điện thoại (người nhận) | SĐT VN hợp lệ, 10 số, bắt đầu bằng 0 (vd 0987654321) | không đủ 10 số, không bắt đầu bằng 0, chứa ký tự chữ (spec-only, chưa verify UI enforce) | **10 số (hợp lệ), 9/11 số (chặn) — spec-only** | §D8.1 |
| Địa chỉ giao hàng | **dropdown/select** (target theo user 2026-07-29, override BRD §D8.1 "text tự do ≤200 ký tự" — xem C-SENDER-4), chọn 1 địa điểm PHẢI khác Địa chỉ lấy hàng | chưa chọn (dropdown ở trạng thái mặc định), hoặc chọn trùng Địa chỉ lấy hàng | *(không có boundary ký tự — không còn áp dụng, đổi sang dropdown)* | §D8.1 (free-text, lỗi thời); C-SENDER-4 (dropdown, target) |
| Địa chỉ lấy hàng (Người gửi) | **dropdown/select** (target theo user 2026-07-29 — xem C-SENDER-4), mặc định chọn sẵn nơi làm việc của user, cho phép đổi | *(không có invalid — luôn có 1 giá trị mặc định)* | *(không áp dụng — dropdown, không phải free-text)* | §D8.1 (free-text ≤200 ký tự, lỗi thời); C-SENDER-4 (dropdown, target) |
| Khung giờ (từ – đến) | vd 17:00–18:30, khoảng cách ≥30 phút | đến ≤ từ, hoặc khoảng cách <30 phút (spec-only, chưa verify UI enforce) | **đúng 30 phút (hợp lệ, chặn dưới), 29 phút (chặn) — spec-only** | §D8.1 |
| *(mọi field text)* | *(auto-trim khoảng trắng đầu/cuối, chuẩn hoá SĐT bỏ khoảng trắng/dấu chấm trước khi lưu — VAL-03, spec-only chưa verify UI thật)* | | | §D8.3 VAL-03 |

## Module ORDER — Ngưỡng EXPIRED (DOC-v1.1-01 §D8.1, §D8.2 — C-ORDER-2 resolved)

| Field | Valid | Invalid | Boundary | Nguồn |
|-------|-------|---------|----------|-------|
| Từ ngày / Đến ngày | Đến ngày ≥ Từ ngày; không chọn ngày quá khứ | Đến ngày < Từ ngày, hoặc Từ ngày trong quá khứ | **Ngưỡng EXPIRED = "Đến ngày" (resolved 2026-07-28, đảo ngược resolution v1.0 "Từ ngày"). Boundary: current date = Đến ngày (hợp lệ, chưa expired), current date = Đến ngày + 1 (chặn, expired) — viết được khi có UI/worker backend thật, hiện vẫn 🚫 Blocked** | §D8.1, §D8.2, C-ORDER-2 |

## Module CANCEL — Lý do huỷ (DOC-v1.1-01 §D8.3 VAL-04 — C-CANCEL-1 resolved)

| Field | Valid | Invalid | Boundary | Nguồn |
|-------|-------|---------|----------|-------|
| Lý do huỷ | text ≥5 ký tự (theo BRD VAL-04, target/rule chính thức đã resolve) | rỗng (→ nút "Xác nhận" bị khoá, đã verify UI thật); **1-4 ký tự (theo BRD PHẢI bị chặn — nhưng UI hiện tại KHÔNG chặn, đã verify "ab" 2 ký tự vẫn enable nút → gap cần dev fix)** | **5 ký tự (hợp lệ, chặn dưới theo BRD), 4 ký tự (PHẢI chặn theo BRD nhưng UI hiện tại KHÔNG chặn — viết TC theo BRD, dự kiến FAIL trên UI hiện tại, khuyến nghị log-bug)** | §D8.3 VAL-04, C-CANCEL-1 |

## Ghi chú chung
- Giá trị "master data" (danh mục từ hệ thống nguồn) phụ thuộc môi trường — xác nhận giá trị thực khi vibe-test/automation.
- Boundary values (in **đậm**) là ứng viên chính cho BVA ở generate-tc.
- **Phần lớn boundary mới ở bảng SENDER trên (Ghi chú 300 ký tự, Ảnh 5MB, Tên 2-60 ký tự, SĐT 10 số, Khung giờ 30 phút) là "spec-only" — lấy từ BRD v3.2 §D8, CHƯA tự verify qua UI thật (không nhập dữ liệu biên thật trong phiên verify này).** generate-tc có thể viết TC dựa trên các con số này (khác với "chưa xác định" hoàn toàn của v1.0), nhưng nên gắn cờ "cần vibe-test xác nhận thực tế UI có enforce đúng hay không" trước khi coi PASS/FAIL là chuẩn — nhất quán với phát hiện đã verify chắc chắn ở CANCEL (BRD ghi 1 rule nhưng UI hiện tại không enforce đúng như vậy — user đã quyết định viết TC theo BRD làm target).
- **2026-07-28 (lần 2):** user đã resolve cả 4 điểm còn Open ở lần phân tích đầu (C-ORDER-2, C-SENDER-3, C-CANCEL-1, C-GENERAL-4) — bảng ORDER và CANCEL ở trên đã cập nhật theo resolution mới nhất.

### Quy ước cell (giữ nhất quán)
- **Valid:** `value (mô tả)` — vd `10 số (10 ký tự)`, `hôm nay (default)`.
- **Invalid:** `value (→ hệ quả/MSG)` — dự án không có mã MSG → ghi mô tả hệ quả.
- **Boundary:** **bold** giá trị biên + (hợp lệ/chặn).
- **Nguồn:** `DOC-v1.1-01 §section` (req_notation: none — dùng §section, kèm mã BRD gốc như VAL-04/US-D18 trong ref).
