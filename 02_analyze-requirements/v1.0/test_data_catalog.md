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
| Kênh liên hệ lộ | SĐT (bắt buộc, luôn bật) + Workplace/email (tuỳ chọn bật) | tắt SĐT (→ chặn, vì SĐT bắt buộc lộ) | ⚠ **Tính năng "Cấu hình kênh liên hệ" xác nhận Out of scope v1.0 — phase sau (C-USR-02, Resolved — Deferred 2026-07-27). Không viết TC hành vi bật/tắt.** | USR-07 |
| Chỉ số cá nhân | Tổng đơn đã giúp (số nguyên ≥0) + Tổng quà đã nhận (đếm theo loại) | — | Không hiện điểm ECO/hạng thành viên/CO₂ dạng số ở v1.0; cơ chế phân hạng "Hạng Đồng hành" xác nhận Out of scope v1.0 — phase sau (C-USR-01, Resolved — Deferred 2026-07-27) | USR-05 |

## Module ORD — Đăng tin (DOC-v1.0-01 §D3, DOC-v1.0-02 §3.5)

| Field | Valid | Invalid | Boundary | Nguồn |
|-------|-------|---------|----------|-------|
| Loại hàng | 1 trong 8 chip: `Tài liệu` (mặc định) · `Đồ điện tử` · `Thực phẩm` · `Hàng nhỏ` · `Đồ dễ vỡ` · `Quần áo` · `Thuốc/Y tế` · `Khác` (kể cả "Thuốc/Y tế" — v1.0 không chặn, C-ORD-04 Resolved) | không chọn (→ chặn, không cho qua Bước 2 — validate bắt buộc, C-ORD-01 Resolved 2026-07-27) | — | Table 6 (§3.5.1) |
| Giá trị hàng (ước tính) | 1 trong 3 chip: `thấp` / `vừa` / `cao` — chọn **`cao`** → hiện cảnh báo trách nhiệm tự thoả thuận (BRD v3.2 §D8.1, 2026-07-28) | không chọn (→ chặn, không cho qua Bước 2 — validate bắt buộc, C-ORD-01 Resolved 2026-07-27) | Ngưỡng cấu hình BR-ORD-03 (→ cảnh báo bảo hiểm theo SỐ TIỀN) **KHÔNG áp dụng ở v1.0** — BA/PO xác nhận phase này chưa làm, out of scope v1.0 (C-ORD-02, Resolved — Deferred 2026-07-27); không viết BVA cho ngưỡng SỐ TIỀN này. Cảnh báo khi chọn chip "cao" là cơ chế categorical KHÁC, ĐANG CÓ ở v1.0 (không cần BVA số) | BR-ORD-03, Table 6, BRD v3.2 §D8.1 |
| Ghi chú | text tự do (vd "gọi trước khi tới"), ≤300 ký tự | >300 ký tự (→ chặn/báo lỗi) | **300 ký tự (hợp lệ), 301 ký tự (chặn)** (BRD v3.2 §D8.1) | Table 6, BRD v3.2 §D8.1 |
| Ảnh hàng | ảnh hợp lệ (jpg/png), ≤5MB, chỉ 1 ảnh | sai định dạng (không phải JPG/PNG), >5MB, chọn nhiều ảnh | **5MB (hợp lệ), >5MB (chặn)** (BRD v3.2 §D8.1) | Table 6, BRD v3.2 §D8.1 |
| Email công ty người nhận | email nội bộ có trong hệ thống → auto-fill (→ "Đã tìm thấy trong hệ thống nội bộ") | email không có trong hệ thống (→ "Không tìm thấy · nhập thủ công"); sai định dạng email | — | US-D18, BRD v3.2 §D8.1 |
| Tên người nhận | 2–60 ký tự hợp lệ | để trống (→ chặn — C-ORD-01), 1 ký tự, 61 ký tự | **2 ký tự (hợp lệ), 1 ký tự (chặn), 60 ký tự (hợp lệ), 61 ký tự (chặn)** (BRD v3.2 §D8.1) | Table 7, BRD v3.2 §D8.1 |
| SĐT người nhận | SĐT VN hợp lệ (10 số, đầu 0) | sai định dạng, có khoảng trắng/dấu chấm (tự động chuẩn hoá trước khi lưu — VAL-03) | — | Table 7, BRD v3.2 §D8.1/§D8.3 |
| Địa chỉ lấy hàng / Địa chỉ giao hàng | text hợp lệ, ≤200 ký tự, 2 địa chỉ KHÁC nhau | để trống (→ chặn — C-ORD-01), >200 ký tự, Địa chỉ giao hàng TRÙNG địa chỉ lấy hàng (→ chặn, rule mới BRD v3.2) | **200 ký tự (hợp lệ), 201 ký tự (chặn)** (BRD v3.2 §D8.1) | Table 7, BRD v3.2 §D8.1 |
| Khung giờ mong muốn | Từ < Đến, cách nhau ≥30 phút (mặc định `05:00 PM–06:30 PM`) | Đến ≤ Từ, cách nhau <30 phút (BRD v3.2 §D8.1) | **30 phút (hợp lệ), 29 phút (chặn)** (BRD v3.2 §D8.1) | Table 7, BRD v3.2 §D8.1 |
| Checkbox điều khoản | đã tick (mặc định tick sẵn theo demo) | chưa tick (→ chặn đăng, ORD-09; nút submit disabled tới khi hợp lệ — VAL-01) | — | ORD-09, Table 8, BRD v3.2 §D8.3 |
| Điểm xuất phát / Điểm đến (OFFER, D8.2) | text hợp lệ, ≤200 ký tự (Điểm xuất phát), 2 điểm KHÁC nhau | để trống khi submit, >200 ký tự (Điểm xuất phát), Điểm đến TRÙNG điểm xuất phát | **200 ký tự (hợp lệ Điểm xuất phát), 201 ký tự (chặn)** (BRD v3.2 §D8.2) | BRD v3.2 §D8.2 |
| Thời gian di chuyển (OFFER, D8.2) | Từ < Đến, cách nhau ≥30 phút (mặc định `17:30–18:30`) | Đến ≤ Từ, cách nhau <30 phút | **30 phút (hợp lệ), 29 phút (chặn)** (BRD v3.2 §D8.2) | BRD v3.2 §D8.2 |

## Module ASN — Ghép nối (DOC-v1.0-02 §4.4 Table 13)

| Field | Valid | Invalid | Boundary | Nguồn |
|-------|-------|---------|----------|-------|
| Điểm xuất phát (A) / Điểm đến (B) (OFFER) | địa chỉ hợp lệ, khác nhau | để trống (chưa có rule validate rõ) | — | Table 13 |
| Khung giờ di chuyển (OFFER) | Khởi hành < Đến nơi | Đến nơi ≤ Khởi hành | — | Table 13 |

## Module DLV — Thực hiện giao hàng (DOC-v1.0-01 §D3, §D4)

| Field | Valid | Invalid | Boundary | Nguồn |
|-------|-------|---------|----------|-------|
| Ảnh bằng chứng lúc nhận | ảnh hợp lệ (tuỳ chọn) | — (optional, không bắt buộc) | — | PUP-03, BR-CNF-01 |
| Chia sẻ vị trí (GPS) | bật khi đơn = IN_TRANSIT | bật ngoài IN_TRANSIT (theo rule chỉ active khi đang giao) | mặc định bật/tắt **là phase sau, chưa có giá trị (C-DLV-02, Open — deferred)** | GPS-01 |
| Thời hạn xác nhận đã nhận | xác nhận trong 2 giờ kể từ "Đã giao" | quá 2 giờ chưa xác nhận (→ nhắc) | **2 giờ (mốc nhắc), 4 giờ tổng (mốc escalate admin)** | BR-CNF-04 |
| Chi phí đối soát (tuỳ chọn) | số tiền hợp lệ (2 bên tự khai) | — (optional, không có validate cụ thể) | — | COST-01, BR-COST-01 |

## Module GIFT — Đánh giá & Quà cảm ơn (DOC-v1.0-01 §A7, DOC-v1.0-02 §3.8)

| Field | Valid | Invalid | Boundary | Nguồn |
|-------|-------|---------|----------|-------|
| Loại quà | 1 trong 4: `🌷 Bông hoa` · `☕ Ly cà phê` · `🧸 Gấu bông` · `👑 Vương miện` | không chọn loại nào rồi gửi (chưa có rule validate rõ — suy đoán phải chọn 1 mới gửi được) | — | A7, §3.8 |

## Module CNL — Huỷ đơn (DOC-v1.0-01 §D1b US-D16)

| Field | Valid | Invalid | Boundary | Nguồn |
|-------|-------|---------|----------|-------|
| Lý do huỷ | text bất kỳ không rỗng, ≥5 ký tự | rỗng, 1-4 ký tự (→ nút Xác nhận huỷ bị khoá/disable — VAL-04) | **5 ký tự (hợp lệ, bật nút), 4 ký tự (chặn, disable)** (BRD v3.2 §D8.3) | US-D16, BR-CNL-01, BRD v3.2 §D8.3 |

## Fixture — Tài khoản & Đơn hàng mẫu (cross-module, ⚠ NEW 2026-07-29)

> **Vì sao có mục này:** review pre-consolidate 2026-07-29 phát hiện **44 TC** (8 TC ở 4 fragment cũ + 36 TC ở 5 fragment mới) có Pre-condition dạng *"đơn đang ở trạng thái X"* / *"tài khoản là Carrier của đơn"* nhưng catalog chỉ có giá trị **field-level** (nội dung ô nhập), KHÔNG có bộ **tài khoản/đơn hàng mẫu**. Tester/automation không biết dùng account nào, đơn nào để chạy. Mục này liệt kê đúng những fixture các TC hiện tại đang cần.
>
> **Lưu ý cấu trúc:** 3 bảng dưới đây (F1/F2/F3) KHÔNG áp structure-lock 5 cột `| Field | Valid | Invalid | Boundary | Nguồn |` của các bảng per-module ở trên — đây là bảng fixture (dữ liệu môi trường), không phải bảng giá trị field.
>
> Mọi giá trị cụ thể để `[TBD]` — **phải điền khi setup môi trường STG** (`07_environments/environments.md`), KHÔNG bịa giá trị trong tài liệu phân tích.

### F1. Tài khoản theo vai trò

| ID fixture | Vai trò | Dùng cho | Giá trị |
|---|---|---|---|
| `ACC-SENDER` | Người gửi (Sender) | 59 TC | `[TBD: MNV/email SSO]` |
| `ACC-CARRIER` | Người vận chuyển (Carrier) | 82 TC | `[TBD: MNV/email SSO]` |
| `ACC-RECEIVER` | Người nhận (Receiver) | 37 TC | `[TBD: MNV/email SSO]` |
| `ACC-CARRIER-2` | Carrier thứ hai | Chống double-accept (`TC_06.31`), tin ẩn sau ghép (`TC_06.6`), khớp lại sau huỷ (`TC_06.9`) | `[TBD]` |
| `ACC-NEW` | Tài khoản mới, 0 đơn đã giúp / 0 quà | `TC_05.9` (BVA-min card Đóng góp), `TC_05.9` (card Đóng góp = 0) | `[TBD]` |
| `ACC-HEAVY` | Tài khoản ≥100 đơn đã giúp | `TC_05.11` (BVA-large, không tràn layout) | `[TBD]` |

> 3 tài khoản đầu phải thuộc **cùng 1 đơn** để chạy được các TC đồng bộ realtime 3 bên (`TC_06.30`, `TC_07.21`, `TC_08.20`, `TC_08.23`) — khuyến nghị dùng `/vibe-multi` (đa-device).

### F2. Đơn hàng theo trạng thái

| ID fixture | Trạng thái | Số TC cần | Ghi chú dựng dữ liệu |
|---|---|---|---|
| `ORD-POSTED` | Chờ ghép (POSTED) | 32 | Chưa ai nhận; cần cho cả nhánh Bảng tin lẫn huỷ trước ghép |
| `ORD-MATCHED` | Đã ghép (MATCHED, stepper hiện "Lấy hàng") | 40 | Carrier CHƯA bấm "Tôi đã lấy hàng" |
| `ORD-IN-TRANSIT` | Đang giao (IN_TRANSIT) | 15 | Dùng cho nhóm TC chặn huỷ sau khi lấy hàng |
| `ORD-DELIVERED` | Đã giao (DELIVERED) | 15 | Dùng cho ma trận nhãn nút + escalate quá hạn |
| `ORD-COMPLETED` | Hoàn thành (COMPLETED) | 22 | Chưa tặng quà — cần cho `TC_09.1` (nút "Cảm ơn người vận chuyển" còn enable) |
| `ORD-COMPLETED-GIFTED` | Hoàn thành + đã tặng quà | 2 | `TC_09.15/16` (nhãn "Bạn đã đánh giá", không gửi lại được) |
| `ORD-CANCELLED` | Đã huỷ | — | Sinh ra trong lúc chạy TC huỷ, không cần dựng sẵn |
| `ORD-EXPIRED` | Hết hạn | 1 | `TC_01.17` (card "Hết hạn" không cho thao tác) |
| `ORD-WITH-PHOTO` | Bất kỳ, có kèm 1 ảnh hàng | 2 | `TC_06.13` — cần **file ảnh gốc** để đối chiếu trực quan: `[TBD: tên file, định dạng, dung lượng]` |
| `ORD-NO-PHOTO` | Bất kỳ, KHÔNG kèm ảnh | 1 | `TC_06.14` (hiển thị ảnh mặc định) |

### F3. Bộ dữ liệu danh sách (cho BVA/DT sắp xếp & trần hiển thị)

| ID fixture | Nội dung | Dùng cho |
|---|---|---|
| `FEED-4` / `FEED-5` / `FEED-6` | 4 / 5 / 6 tin NEED phù hợp tuyến của `ACC-CARRIER` | `TC_05.27/28/29` (BVA trần 5 tin section "Tin mới") |
| `FEED-DIST` | 3 tin khác độ gần tuyến, **cùng** thời điểm đăng | `TC_05.30`, `TC_06.10` (DT-rule1 sắp theo độ gần) |
| `FEED-TIME` | 2 tin **cùng** độ gần tuyến, khác thời điểm đăng | `TC_05.31`, `TC_06.11` (DT-rule2 sắp theo thời gian) |
| `TIME-ESCALATE` | Đơn ở "Đã giao" mock được mốc 1h55' / >2h / >4h | `TC_07.35/36/37` (BVA ngưỡng escalate) — cần cơ chế mock thời gian hệ thống, `[TBD: cách mock trên STG]` |

**Chưa giải quyết được ở tầng tài liệu:** `TIME-ESCALATE` phụ thuộc khả năng mock thời gian của môi trường STG — nếu STG không mock được, 3 TC này phải chuyển sang kiểm thử ở tầng backend/log thay vì UI. Cần xác nhận với Dev/DevOps.

## Ghi chú chung
- **Cập nhật 2026-07-29 (review pre-consolidate):** bổ sung mục **Fixture** ở trên (F1 tài khoản · F2 đơn theo trạng thái · F3 bộ dữ liệu danh sách) — đóng finding INFO "catalog thiếu fixture đơn hàng/tài khoản" ảnh hưởng 44 TC. Giá trị cụ thể để `[TBD]`, phải điền khi setup môi trường STG.
- Giá trị "master data" (6 văn phòng preset FPT — LOC-03; danh mục Loại hàng 8 chip; danh sách tỉnh/thành ghép địa lý) phụ thuộc environment thật — xác nhận giá trị thực khi vibe-test/automation.
- Boundary values (in **đậm**) là ứng viên chính cho BVA ở generate-tc. **Cập nhật 2026-07-27:** ngưỡng giá trị hàng BR-ORD-03 xác nhận **Out of scope v1.0** (C-ORD-02, Resolved — Deferred) — KHÔNG viết BVA cho ngưỡng này ở v1.0. Hạn tin (ORD-06) KHÔNG còn là boundary thiếu số — BA/PO xác nhận hạn tin = giá trị "Đến ngày" mà user tự chọn lúc đăng tin (C-ORD-03, Resolved); BVA cho hạn tin nên test theo giá trị ngày user nhập (vd ngày gần nhất/xa nhất hệ thống cho phép chọn), không phải theo 1 hằng số hệ thống. Chi tiết xem `MEMORY.md §6`.
- **Cập nhật 2026-07-28 (BRD v3.2 §D8):** bổ sung toàn bộ maxlength/min-length/BVA còn thiếu cho module ORD (Ghi chú, Địa chỉ, Tên người nhận, khung giờ NEED+OFFER, ảnh sản phẩm) và CNL (lý do huỷ) — trước đây các field này ghi "chưa có số cụ thể"/TBD, nay đã có giá trị chính thức từ BA. Xem `MEMORY.md §6.1 C-ORD-01` (đầy đủ) và `C-ORD-02` (phân biệt cảnh báo categorical "Giá trị hàng = Cao" — đang có ở v1.0 — với ngưỡng số tiền BR-ORD-03 — vẫn deferred).

### Quy ước cell (giữ nhất quán)
- **Valid:** `value (mô tả)` — vd `bông hoa (1 trong 4 loại)`.
- **Invalid:** `value (→ hệ quả/MSG)` — dự án không có mã MSG → ghi mô tả hệ quả (vd `rỗng (→ nút Xác nhận huỷ bị khoá)`).
- **Boundary:** **bold** giá trị biên + (hợp lệ/chặn) — vd `**2 giờ (mốc nhắc), 4 giờ (mốc escalate)**`.
- **Nguồn:** dùng ID gốc của DOC dự án (vd `USR-05`, `BR-ORD-03`, `US-D18`) hoặc `Table N (§section)` khi trích từ DOC-v1.0-02 (docx không có ID riêng cho field-level, chỉ có table/section).
- `→` = hệ quả; `[…]` = ID pattern.
