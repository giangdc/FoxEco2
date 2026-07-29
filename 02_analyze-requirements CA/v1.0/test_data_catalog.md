# Test Data Catalog — v1.0

> Tạo bởi: analyze-requirements. Dữ liệu test (valid / invalid / boundary) per module, trích từ tài liệu gốc **theo đúng ký hiệu của DOC dự án** (`req_notation: none` → dùng `§section`). Input cho generate-tc (BVA/EP/...).
>
> **Structure-lock:** giữ nguyên 5 cột `| Field | Valid | Invalid | Boundary | Nguồn |` cho mọi module. KHÔNG đổi cột.

## Module SENDER — Wizard đăng tin (DOC-v1.0-01)

| Field | Valid | Invalid | Boundary | Nguồn |
|-------|-------|---------|----------|-------|
| Loại hàng (chip) | 1 trong 8 chip: Tài liệu / Đồ điện tử / Thực phẩm / Hàng nhỏ / Đồ dễ vỡ / Quần áo / Thuốc·Y tế / Khác (mô tả: chọn "Đồ điện tử") | N/A (chip select, không có free input để nhập sai) | N/A | §1.2 |
| Giá trị hàng (chip) | 1 trong 3 chip: Giá trị thấp / Giá trị vừa / Giá trị cao (mô tả: chọn "Giá trị vừa") | N/A (chip select) | N/A | §1.2 |
| Ghi chú | text tự do (mô tả: "Gói hàng dễ vỡ, vui lòng nhẹ tay") | chưa rõ (→ cần verify: có giới hạn độ dài hay bắt buộc nhập không — xem C-SENDER-2 test-scope note) | chưa rõ (→ cần verify max length) | §1.2 |
| Tên người nhận | text không rỗng (mô tả: "Phan Văn Hưng") | chưa rõ (→ cần verify: bỏ trống có chặn "Tiếp theo" không) | chưa rõ | §1.3 |
| SĐT người nhận | số điện thoại VN 10 chữ số (mô tả: "0987654321") | chưa rõ (→ cần verify: có validate format/độ dài không) | chưa rõ (→ cần verify min/max digits) | §1.3 |
| Địa chỉ giao hàng | text địa chỉ (mô tả: "89 Nguyễn Thị Minh Khai, Q.3, TP.HCM") | chưa rõ (→ cần verify bỏ trống) | N/A | §1.3 |
| Checkbox điều khoản sử dụng | đã tick (→ enable nút "Đăng tin ngay") | chưa tick (→ nút "Đăng tin ngay" disabled/không phản hồi — đã verify) | N/A | §1.4 |
| Email công ty người nhận (🚫 Blocked — DOC-v1.0-02, chưa có UI) | email có trong hệ thống nội bộ (→ tự điền tên/SĐT/địa chỉ + "Đã tìm thấy trong hệ thống nội bộ") | email không có trong hệ thống (→ "Không tìm thấy · nhập thủ công"); format email sai (→ chưa xác định hệ quả) | chưa xác định | DOC-v1.0-02 §D1b US-D18 |

## Module OFFER — Đăng tin "Tôi nhận giao hàng" (🔓 Unblocked 2026-07-27 — UI xác nhận DOC-v1.0-03)

| Field | Valid | Invalid | Boundary | Nguồn |
|-------|-------|---------|----------|-------|
| Thông tin của tôi (tên/SĐT) | tự điền sẵn (vd "Nguyễn Anh Tuấn" / "0903 555 271") — quan sát UI không cho sửa trực tiếp, chưa xác định có field nhập tay khi user mới chưa có info | chưa xác định | N/A | DOC-v1.0-02 §D1b US-D10; UI DOC-v1.0-03 |
| Điểm xuất phát (A) | tự điền sẵn từ profile (vd "Tòa nhà Lô B3, KCX Tân Thuận, Q.7") | chưa xác định | chưa xác định | DOC-v1.0-02 §D1b US-D10; UI DOC-v1.0-03 |
| Điểm đến (B) | text địa chỉ, nhập tay (placeholder "Bạn sẽ đến đâu") | rỗng (→ nút "Đăng tin ngay" disabled — đã quan sát) | chưa xác định | DOC-v1.0-02 §D1b US-D10; UI DOC-v1.0-03 |
| Khoảng thời gian (Từ ngày/Đến ngày) | date picker, mặc định = ngày hiện tại | chưa xác định | chưa xác định | UI DOC-v1.0-03 (BRD viết gọn "Khung giờ", UI thật tách 2 field ngày) |
| Thời gian di chuyển (Khởi hành/Đến nơi) | time picker, mặc định 05:30 PM–06:30 PM (quan sát) | chưa xác định | chưa xác định | UI DOC-v1.0-03 |
| Checkbox điều khoản | đã tick (bắt buộc, cùng pattern SENDER — text "Tôi đã đọc và đồng ý Điều khoản sử dụng FoxEco") | chưa tick (→ nút "Đăng tin ngay" disabled — đã quan sát cùng lúc với Điểm đến rỗng, chưa tách riêng 2 case) | N/A | DOC-v1.0-02 §D1b US-D10; UI DOC-v1.0-03 |

## Module CANCEL — Huỷ đơn (🔓 Unblocked 2026-07-27 — UI xác nhận DOC-v1.0-03)

| Field | Valid | Invalid | Boundary | Nguồn |
|-------|-------|---------|----------|-------|
| Lý do huỷ | text tự do không rỗng (placeholder quan sát được: "VD: đổi lịch, không cần gửi nữa...") | rỗng (→ nút "Xác nhận" khoá, không huỷ được — đã quan sát UI thật, khớp US-D16) | chưa xác định max length | DOC-v1.0-02 §D1b US-D16; UI DOC-v1.0-03 |

## Module GIFT — Tặng quà cảm ơn (🔓 Unblocked 2026-07-27 — UI xác nhận DOC-v1.0-03)

| Field | Valid | Invalid | Boundary | Nguồn |
|-------|-------|---------|----------|-------|
| Loại quà (chip) | 1 trong 4: Bông hoa 🌷 / Ly cà phê ☕ / Gấu bông 🧸 / Vương miện 👑 (đúng nhãn quan sát được, có emoji icon) | N/A (chip select cố định, không free input) | N/A | DOC-v1.0-02 §A7; UI DOC-v1.0-03 |
| Nút xác nhận | bấm "Xác nhận tặng quà" sau khi chọn 1 quà (⚠️ khác BRD "gửi ngay không cần xác nhận" — UI thật có bước xác nhận) | chưa chọn quà (→ chưa xác định nút có disabled hay không, cần verify) | N/A | UI DOC-v1.0-03 (không có trong BRD gốc) |

## Ghi chú chung
- Giá trị "master data" (danh mục từ hệ thống nguồn) phụ thuộc môi trường — xác nhận giá trị thực khi vibe-test/automation. Trong bản demo, 8 loại hàng + 3 mức giá trị là danh mục **cố định** trong client code (không gọi API), có thể coi là stable.
- Boundary values (in **đậm**) là ứng viên chính cho BVA ở generate-tc. **Trong bản demo v1.0, phần lớn field text (Ghi chú/Tên/SĐT/Địa chỉ) CHƯA xác định được rõ ràng buộc validate/boundary thật** vì đã quan sát hành vi "nút Tiếp theo luôn khả dụng kể cả khi chưa điền" ở bước 1 (xem `MEMORY.md` REQ-SENDER-002) — nghi ngờ bản demo KHÔNG có validate input thật (chỉ là prototype UI). generate-tc nên ưu tiên P2/P3 cho các trường hợp "invalid/boundary chưa rõ" này, và đánh dấu rõ trong TC "kết quả mong đợi cần verify thực tế trước khi coi là PASS/FAIL".
- **(2026-07-24)** Data catalog của các module 🚫 Blocked (Email công ty người nhận, OFFER, CANCEL, GIFT) trích từ BRD v3.1 (DOC-v1.0-02) — chưa có UI thật để verify hành vi validate, phần lớn cell "Invalid"/"Boundary" ghi "chưa xác định" thay vì đoán.
- **(2026-07-27) UNBLOCK OFFER/CANCEL/GIFT:** verify qua Chrome MCP trên DOC-v1.0-03 xác nhận CÓ UI thật cho cả 3 module — đã cập nhật cell Valid với giá trị/placeholder quan sát được trực tiếp. Nhiều cell Invalid/Boundary vẫn "chưa xác định" vì chỉ mới verify happy-path/1 case validation (chưa chạy đủ Error Guessing như đã làm cho SENDER) — generate-tc nên áp dụng lại kỹ thuật B6 Error Guessing cho field text mới (Điểm đến OFFER, Lý do huỷ CANCEL) tương tự SENDER. **Email công ty người nhận vẫn 🚫 Blocked thật** (chưa thấy field này trong DOC-v1.0-03).

### Quy ước cell (giữ nhất quán)
- **Valid:** `value (mô tả)` — vd `ABC1234567 (10 ký tự)`, `hôm nay (default)`.
- **Invalid:** `value (→ hệ quả/MSG)` — vd `rỗng (→MSG-001)`, `"abc" (→MSG-E-002)`. Dự án không có mã MSG → ghi mô tả hệ quả (vd `rỗng (→ báo lỗi bắt buộc nhập)`).
- **Boundary:** **bold** giá trị biên + (hợp lệ/chặn) — vd `**500 ký tự (hợp lệ), 501 (chặn)**`.
- **Nguồn:** dùng **đúng ký hiệu của DOC dự án** theo `req_notation` trong block `## DOC Notation` của `Project_rule.md` — dự án này `req_notation: none` → dùng `DOC-ID §section` (rút gọn `§section` vì cùng 1 DOC-v1.0-01 cho toàn bảng).
- Set literal `{0=…, 1=…}`; `→` = hệ quả; `⟷` = quan hệ 2 chiều; `[…]` = ID pattern.
