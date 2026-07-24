# Test Data Catalog — v1.0

> Tạo bởi: analyze-requirements. Dữ liệu test (valid / invalid / boundary) per module, trích từ DOC-v1.0-01/02 theo đúng ID gốc của dự án (`req_notation`: doc-native module-prefixed IDs — xem `Project_rule.md §9`). Input cho generate-tc (BVA/EP/...).
>
> **Structure-lock:** giữ nguyên 5 cột `| Field | Valid | Invalid | Boundary | Nguồn |` cho mọi module. Module không có input field UI cụ thể (NTF, TS — chỉ nội dung hiển thị/backend) không có bảng riêng, xem `MEMORY.md §4.1` tương ứng.

## Module USR — Tài khoản & Hồ sơ (DOC-v1.0-01 §A6)

| Field | Valid | Invalid | Boundary | Nguồn |
|-------|-------|---------|----------|-------|
| Tên | `Đồng Công Chí Linh` (auto-fill từ SSO) | — (readonly, không sửa qua form) | — | USR-02 |
| SĐT (hồ sơ) | SĐT nội bộ hợp lệ, auto-fill từ SSO | — (readonly, view-only — xác nhận KHÔNG có chức năng cập nhật trên app STG thật, xem C-USR-03) | — | USR-02 |
| Phòng ban + khu vực/tỉnh | `Phòng Kỹ thuật · MNV: FTEL2291` (mẫu demo) | — (readonly, không sửa qua form) | — | USR-04 |
| Kênh liên hệ lộ | SĐT (bắt buộc, luôn bật) + Workplace/email (tuỳ chọn bật) | tắt SĐT (→ chặn, vì SĐT bắt buộc lộ) | — | USR-07 |
| Chỉ số cá nhân | Tổng đơn đã giúp (số nguyên ≥0) + Tổng quà đã nhận (đếm theo loại) | — | ⚠ **Không hiện điểm ECO/hạng thành viên/CO₂ (chờ C-USR-01 chốt)** | USR-05 |

## Module ORD — Đăng tin (DOC-v1.0-01 §D3, DOC-v1.0-02 §3.5)

| Field | Valid | Invalid | Boundary | Nguồn |
|-------|-------|---------|----------|-------|
| Loại hàng | 1 trong 8 chip: `Tài liệu` (mặc định) · `Đồ điện tử` · `Thực phẩm` · `Hàng nhỏ` · `Đồ dễ vỡ` · `Quần áo` · `Thuốc/Y tế` · `Khác` | không chọn (⚠ hành vi hiện tại vẫn cho qua — xem C-ORD-01) | — | Table 6 (§3.5.1) |
| Giá trị hàng (ước tính) | 1 trong 3 chip: `thấp` / `vừa` / `cao` | không chọn (⚠ hành vi hiện tại vẫn cho qua — C-ORD-01) | **ngưỡng cấu hình BR-ORD-03 (→ cảnh báo bảo hiểm) — giá trị số CHƯA xác định, xem C-ORD-02** | BR-ORD-03, Table 6 |
| Ghi chú | text tự do (vd "gọi trước khi tới") | — (optional, không có rule chặn) | — | Table 6 |
| Ảnh hàng | ảnh hợp lệ (jpg/png) | — (optional, không bắt buộc) | — (dung lượng/định dạng tối đa chưa nêu trong doc) | Table 6 |
| Email công ty người nhận | email nội bộ có trong hệ thống → auto-fill (→ "Đã tìm thấy trong hệ thống nội bộ") | email không có trong hệ thống (→ "Không tìm thấy · nhập thủ công") | — | US-D18 |
| Tên/SĐT/Địa chỉ người nhận (nhập tay) | đầy đủ 3 trường hợp lệ | để trống hoàn toàn (⚠ hành vi hiện tại vẫn cho qua Bước 3 — C-ORD-01) | — | Table 7 (§3.5.2) |
| Khung giờ mong muốn | Từ < Đến hợp lệ (mặc định `05:00 PM–06:30 PM`) | Đến ≤ Từ (chưa có rule validate rõ trong doc) | — | Table 7 |
| Checkbox điều khoản | đã tick (mặc định tick sẵn theo demo) | chưa tick (→ chặn đăng, ORD-09) | — | ORD-09, Table 8 |

## Module ASN — Ghép nối (DOC-v1.0-02 §4.4 Table 13)

| Field | Valid | Invalid | Boundary | Nguồn |
|-------|-------|---------|----------|-------|
| Điểm xuất phát (A) / Điểm đến (B) (OFFER) | địa chỉ hợp lệ, khác nhau | để trống (chưa có rule validate rõ) | — | Table 13 |
| Khung giờ di chuyển (OFFER) | Khởi hành < Đến nơi | Đến nơi ≤ Khởi hành | — | Table 13 |

## Module DLV — Thực hiện giao hàng (DOC-v1.0-01 §D3, §D4)

| Field | Valid | Invalid | Boundary | Nguồn |
|-------|-------|---------|----------|-------|
| Ảnh bằng chứng lúc nhận | ảnh hợp lệ (tuỳ chọn) | — (optional, không bắt buộc) | — | PUP-03, BR-CNF-01 |
| Chia sẻ vị trí (GPS) | bật khi đơn = IN_TRANSIT | bật ngoài IN_TRANSIT (theo rule chỉ active khi đang giao) | mặc định bật/tắt **chưa xác định (C-DLV-02)** | GPS-01 |
| Thời hạn xác nhận đã nhận | xác nhận trong 2 giờ kể từ "Đã giao" | quá 2 giờ chưa xác nhận (→ nhắc) | **2 giờ (mốc nhắc), 4 giờ tổng (mốc escalate admin)** | BR-CNF-04 |
| Chi phí đối soát (tuỳ chọn) | số tiền hợp lệ (2 bên tự khai) | — (optional, không có validate cụ thể) | — | COST-01, BR-COST-01 |

## Module GIFT — Đánh giá & Quà cảm ơn (DOC-v1.0-01 §A7, DOC-v1.0-02 §3.8)

| Field | Valid | Invalid | Boundary | Nguồn |
|-------|-------|---------|----------|-------|
| Loại quà | 1 trong 4: `🌷 Bông hoa` · `☕ Ly cà phê` · `🧸 Gấu bông` · `👑 Vương miện` | không chọn loại nào rồi gửi (chưa có rule validate rõ — suy đoán phải chọn 1 mới gửi được) | — | A7, §3.8 |

## Module CNL — Huỷ đơn (DOC-v1.0-01 §D1b US-D16)

| Field | Valid | Invalid | Boundary | Nguồn |
|-------|-------|---------|----------|-------|
| Lý do huỷ | text bất kỳ không rỗng | rỗng (→ nút Xác nhận huỷ bị khoá/disable) | — | US-D16, BR-CNL-01 |

## Ghi chú chung
- Giá trị "master data" (6 văn phòng preset FPT — LOC-03; danh mục Loại hàng 8 chip; danh sách tỉnh/thành ghép địa lý) phụ thuộc environment thật — xác nhận giá trị thực khi vibe-test/automation.
- Boundary values (in **đậm**) là ứng viên chính cho BVA ở generate-tc — lưu ý 2 boundary quan trọng CHƯA có giá trị số cụ thể (ngưỡng giá trị hàng BR-ORD-03 · hạn tin mặc định ORD-06), xem C-ORD-02/C-ORD-03 ở `MEMORY.md §6`.

### Quy ước cell (giữ nhất quán)
- **Valid:** `value (mô tả)` — vd `bông hoa (1 trong 4 loại)`.
- **Invalid:** `value (→ hệ quả/MSG)` — dự án không có mã MSG → ghi mô tả hệ quả (vd `rỗng (→ nút Xác nhận huỷ bị khoá)`).
- **Boundary:** **bold** giá trị biên + (hợp lệ/chặn) — vd `**2 giờ (mốc nhắc), 4 giờ (mốc escalate)**`.
- **Nguồn:** dùng ID gốc của DOC dự án (vd `USR-05`, `BR-ORD-03`, `US-D18`) hoặc `Table N (§section)` khi trích từ DOC-v1.0-02 (docx không có ID riêng cho field-level, chỉ có table/section).
- `→` = hệ quả; `[…]` = ID pattern.
