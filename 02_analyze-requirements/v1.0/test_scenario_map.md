# Test Scenario Map — v1.0

## Tổng quan
- Tổng số scenarios: 62 (NEW: 62, MODIFIED: 0, CARRIED: 0)
- Phân bổ priority: P1: 20 | P2: 30 | P3: 12
- Tổng số màn hình (Screen): 21 | Tổng số block: 36
- **Cập nhật 2026-07-24 (bổ sung):** +4 scenario (SC-DLV-012/013/014, SC-GIFT-004) từ ma trận nhãn nút quan sát thực tế app STG (QA GiangDC2) — xem block "Theo dõi đơn — Ma trận nhãn nút theo trạng thái" trong mục DLV.
- **Cập nhật 2026-07-24 (bổ sung #2):** thêm nguồn DOC-v1.0-04 (82 ảnh Figma "Fox Eco Doc") — bổ sung verbatim text/button chính xác cao cho các Screen: Đăng tin thành công (+ phát hiện mâu thuẫn "Mã tin", xem C-ORD-05), Thông báo (+1 block nội dung thực tế), Cá nhân (badge tier), Tặng quà (popup "Đã gửi lời cảm ơn!"), Theo dõi đơn — Ma trận nhãn nút (xác nhận verbatim + popup xác nhận), Huỷ đơn (form lý do + màn "Đơn đã huỷ"). Không phát sinh scenario mới trong đợt này — chỉ tăng độ chính xác text cho scenario đã có.

## Block Definitions (Screen → Block → Fields/Rules)

### USR — Tài khoản & Hồ sơ

#### Screen: Cá nhân

##### Block: Thông tin định danh

| # | Field/Cột/Action | Rule ngắn |
|---|-------------------|------------|
| 1 | Tên | Tự động điền theo tài khoản SSO |
| 2 | Phòng ban | Tự động điền theo tài khoản SSO |
| 3 | Khu vực/tỉnh | Tự động điền, dùng cho ghép địa lý (NT-06) |

**Source Quote:**
> "USR-04 Hiển thị phòng ban + khu vực/tỉnh (tin cậy + ghép địa lý)"

**Source Location:** `DOC-v1.0-01 §A6 "Actors & Hồ sơ (chung)" · row USR-04`

**Scenarios liên quan:** SC-USR-003

##### Block: Chỉ số đóng góp

| # | Field/Cột/Action | Rule ngắn |
|---|-------------------|------------|
| 1 | Badge tier | "🏆 Hạng Đồng hành" — text pill dưới tên, xác nhận CÓ tồn tại trên UI thực tế (xem C-USR-01) |
| 2 | Tổng đơn đã giúp | "[N] đơn đã giúp" — đếm số đơn COMPLETED mà user là Carrier |
| 3 | Tổng quà ảo đã nhận | "[N] quà đã nhận" — đếm quà nhận được, đếm theo loại |
| 4 | (Không hiện) Điểm ECO / điểm uy tín dạng số / CO₂ | KHÔNG xuất hiện trên UI thực tế lẫn BRD v3.1 — xem C-USR-01 |

**Source Quote:**
> "USR-05 Hiển thị tổng số đơn đã giúp + tổng số quà ảo đã nhận (không tính điểm/CO₂)" — **verbatim xác nhận từ ảnh Figma (DOC-v1.0-04, đã zoom 4x)**: Header cam có avatar + tên + "Phòng [ban] · MNV: [mã NV]" + badge pill "🏆 Hạng Đồng hành"; card trắng bên dưới 2 số liệu "[N] đơn đã giúp" / "[N] quà đã nhận"; menu "Đơn của tôi" / "Quà đã nhận". Không có điểm ECO/điểm uy tín dạng số nào.

**Source Location:** `DOC-v1.0-01 §A6 "Actors & Hồ sơ (chung)" · row USR-05` + `DOC-v1.0-04 — images/570ad9d32e3dbdf44c72d6140826f0e6f9a3393e, e5764b10a94b0d51fab023c1a92b6f25732cb402`

**Scenarios liên quan:** SC-USR-004

##### Block: Kênh liên hệ

| # | Field/Cột/Action | Rule ngắn |
|---|-------------------|------------|
| 1 | SĐT | Bắt buộc, luôn lộ sau khi ghép |
| 2 | Workplace/email | Tuỳ chọn, user tự cấu hình có lộ hay không |

**Source Quote:**
> "USR-07 Cấu hình kênh liên hệ sẽ lộ: SĐT (bắt buộc), Workplace/email (tùy chọn)"

**Source Location:** `DOC-v1.0-01 §A6 "Actors & Hồ sơ (chung)" · row USR-07`

**⚠ GAP xác nhận (C-USR-02):** Chỉ có nguồn BRD text, KHÔNG có bằng chứng UI nào (ảnh Figma DOC-v1.0-04 của màn Cá nhân không có mục này; QA xác nhận không thấy trên app STG thật). Theo `Project_rule.md §10.1`, KHÔNG viết TC khẳng định vị trí/hành vi UI cho block này tới khi BA/PO xác nhận — xem `MEMORY.md §6.1 C-USR-02`.

**Scenarios liên quan:** SC-USR-005 (⚠ blocked bởi C-USR-02 — xem ghi chú GAP)

### ORD — Đăng tin

#### Screen: Trang chủ

##### Block: "Đơn của tôi"

| # | Field/Cột/Action | Rule ngắn |
|---|-------------------|------------|
| 1 | Nhãn hướng | "Gửi:" (Sender) / "Nhận:" (Receiver) |
| 2 | Loại hàng \| giá trị | Hiển thị tóm tắt |
| 3 | Badge trạng thái | Chờ ghép/Đã ghép/Đang giao/Đã giao/Hoàn thành |
| 4 | Từ:/Đến: | Điểm lấy → điểm giao rút gọn |
| 5 | Thanh progress 5 bước | Khớp 5 mốc trạng thái |
| 6 | "Chạm để theo dõi đơn" | Mở màn Theo dõi đơn |

**Source Quote:**
> "Đơn của tôi | Chỉ hiện khi có đơn đang hoạt động. Nhãn 'Gửi:' + loại hàng | giá trị; badge trạng thái (Chờ ghép/Đã ghép/Đang giao/Đã giao/Hoàn thành); 'Từ:' / 'Đến:'; thanh progress 5 bước; 'Chạm để theo dõi đơn của bạn'"

**Source Location:** `DOC-v1.0-02 §3.1 "Màn hình Trang chủ" · Table 3`

**Scenarios liên quan:** SC-ORD-003, SC-ORD-004

##### Block: "Tin mới"

| # | Field/Cột/Action | Rule ngắn |
|---|-------------------|------------|
| 1 | Rút gọn 1 tin mới nhất | Của cả cộng đồng, không riêng Sender |
| 2 | Bấm vào | Mở Chi tiết tin |

**Source Quote:**
> "Tin mới | Rút gọn 1 tin mới nhất của CẢ CỘNG ĐỒNG (không riêng của Người gửi); bấm vào mở Chi tiết tin"

**Source Location:** `DOC-v1.0-02 §3.1 "Màn hình Trang chủ" · Table 3`

**Scenarios liên quan:** SC-ASN-005 (liên quan)

#### Screen: Chi tiết tin

##### Block: Thông tin hàng

| # | Field/Cột/Action | Rule ngắn |
|---|-------------------|------------|
| 1 | Ảnh sản phẩm | Ảnh minh hoạ hoặc ảnh mặc định |
| 2 | Loại hàng, Giá trị | 2 cột |
| 3 | Ghi chú | Text tự do |

**Source Quote:**
> "Ảnh sản phẩm | Ảnh minh hoạ hàng hoá (hoặc ảnh mặc định nếu người đăng không tải ảnh) — Thông tin hàng | Loại hàng, Giá trị (2 cột), Ghi chú"

**Source Location:** `DOC-v1.0-02 §3.4 "Màn hình Chi tiết tin" · Table 5`

**Scenarios liên quan:** SC-ORD-001

##### Block: Lộ trình & liên hệ

| # | Field/Cột/Action | Rule ngắn |
|---|-------------------|------------|
| 1 | Lộ trình | Điểm lấy, điểm giao, khung bản đồ ~X km (placeholder tĩnh) |
| 2 | Khung giờ | Khung giờ mong muốn giao nhận |
| 3 | Người gửi | Tên, SĐT + nút Gọi |
| 4 | Nút "Tôi mang giúp được" | CTA chính vai trò Carrier |

**Source Quote:**
> "Lộ trình | Điểm Lấy hàng, điểm Giao hàng, khung 'Bản đồ · ~X km' (placeholder tĩnh, không phải bản đồ thật) — Khung giờ | Khung giờ mong muốn giao nhận — Người gửi | Tên, SĐT + nút 'Gọi' — Nút 'Tôi mang giúp được' | CTA chính — hành động của vai trò Người vận chuyển"

**Source Location:** `DOC-v1.0-02 §3.4 "Màn hình Chi tiết tin" · Table 5`

**Scenarios liên quan:** SC-ASN-001, SC-ASN-003, C-ASN-01

#### Screen: Đăng tin mới (chọn vai trò)

##### Block: 2 lựa chọn

| # | Field/Cột/Action | Rule ngắn |
|---|-------------------|------------|
| 1 | "Tôi cần gửi hàng" | → Wizard NEED (Bước 1/3) |
| 2 | "Tôi nhận giao hàng" | → Form OFFER (1 bước) |

**Source Quote:**
> "'Tôi cần gửi hàng' — Bạn có hàng cần gửi, tìm đồng nghiệp đi thuận đường mang hộ. — 'Tôi nhận giao hàng' — dành cho vai trò vận chuyển"

**Source Location:** `DOC-v1.0-02 §3.5 "Màn hình Đăng tin mới"`

**Scenarios liên quan:** SC-ORD-001, SC-ORD-002

#### Screen: Wizard đăng tin — Bước 1/3 (Thông tin hàng)

##### Block: Form thông tin hàng

| # | Field/Cột/Action | Rule ngắn |
|---|-------------------|------------|
| 1 | Loại hàng | Chip chọn 1: Tài liệu (mặc định) · Đồ điện tử · Thực phẩm · Hàng nhỏ · Đồ dễ vỡ · Quần áo · Thuốc/Y tế · Khác |
| 2 | Ghi chú | Textarea, gợi ý ví dụ |
| 3 | Giá trị hàng (ước tính) | Chip chọn 1: thấp/vừa/cao |
| 4 | Ảnh hàng | Chụp/chọn thư viện, khuyến nghị, không bắt buộc |

**Source Quote:**
> "Loại hàng | Chip chọn 1: Tài liệu (mặc định) · Đồ điện tử · Thực phẩm · Hàng nhỏ · Đồ dễ vỡ · Quần áo · Thuốc/Y tế · Khác — Ghi chú | Textarea... — Giá trị hàng (ước tính) | Chip chọn 1: Giá trị thấp / vừa / cao — Ảnh hàng (khuyến nghị) | Chụp ảnh hoặc chọn từ thư viện — không bắt buộc"

**Source Location:** `DOC-v1.0-02 §3.5.1 "Wizard đăng tin ... Bước 1/3" · Table 6`

**Scenarios liên quan:** SC-ORD-001, SC-ORD-007, SC-ORD-010(gián tiếp), SC-ORD-014, C-ORD-01, C-ORD-04

#### Screen: Wizard đăng tin — Bước 2/3 (Địa điểm & Thời gian)

##### Block: Người gửi

| # | Field/Cột/Action | Rule ngắn |
|---|-------------------|------------|
| 1 | Tên, SĐT, Địa chỉ | Tự động điền theo tài khoản |

**Source Quote:**
> "Người gửi | Tự động điền theo tài khoản: Tên, SĐT, Địa chỉ (điểm lấy hàng)"

**Source Location:** `DOC-v1.0-02 §3.5.2 "Bước 2/3: Địa điểm & Thời gian" · Table 7`

**Scenarios liên quan:** SC-ORD-001

##### Block: Người nhận

| # | Field/Cột/Action | Rule ngắn |
|---|-------------------|------------|
| 1 | Email công ty người nhận | Đầu mục; nhập → tra danh bạ nội bộ |
| 2 | Tên, SĐT, Địa chỉ giao hàng | Nhập tay hoặc auto-fill từ email |

**Source Quote:**
> "Người nhận | Nhập tay: Tên người nhận, Số điện thoại, Địa chỉ giao hàng" (DOC-v1.0-02 Table 7) — bổ sung — "Ô 'Email công ty người nhận' nằm đầu mục Người nhận; nhập email có trong hệ thống → tự điền tên/SĐT/địa chỉ + báo 'Đã tìm thấy trong hệ thống nội bộ'; không có → báo 'Không tìm thấy · nhập thủ công'" (DOC-v1.0-01 US-D18)

**Source Location:** `DOC-v1.0-02 §3.5.2 Table 7` + `DOC-v1.0-01 §D1b US-D18`

**Scenarios liên quan:** SC-ORD-007, SC-ORD-011, SC-ORD-012

##### Block: Thời gian

| # | Field/Cột/Action | Rule ngắn |
|---|-------------------|------------|
| 1 | Khoảng thời gian (ngày) | Từ ngày/Đến ngày, mặc định = hôm nay |
| 2 | Khung giờ mong muốn | Từ/Đến, mặc định 05:00 PM–06:30 PM |

**Source Quote:**
> "Khoảng thời gian (ngày) | Từ ngày / Đến ngày — mặc định = hôm nay — Khung giờ mong muốn | Từ / Đến — mặc định 05:00 PM–06:30 PM"

**Source Location:** `DOC-v1.0-02 §3.5.2 "Bước 2/3" · Table 7`

**Scenarios liên quan:** SC-ORD-001

#### Screen: Wizard đăng tin — Bước 3/3 (Xác nhận & Đăng tin)

##### Block: Tóm tắt & điều khoản

| # | Field/Cột/Action | Rule ngắn |
|---|-------------------|------------|
| 1 | Tóm tắt đơn | Loại hàng+giá trị, khung giờ, người gửi/nhận, ghi chú |
| 2 | Banner cảnh báo hàng cấm | Tĩnh: thuốc/vũ khí/chất nguy hiểm/hàng phi pháp |
| 3 | Checkbox điều khoản | Mặc định tick sẵn |
| 4 | Nút "Đăng tin ngay" | Xác nhận đăng |

**Source Quote:**
> "Tóm tắt đơn gửi hàng | ... — Banner cảnh báo | 'Không được gửi: thuốc, vũ khí, chất nguy hiểm, hàng phi pháp...' — Checkbox điều khoản | Mặc định đã tick sẵn — 'Tôi tự chịu trách nhiệm về hàng hoá và thoả thuận với người mang giúp' — Nút 'Đăng tin ngay' | Xác nhận đăng tin"

**Source Location:** `DOC-v1.0-02 §3.5.3 "Bước 3/3: Xác nhận & Đăng tin" · Table 8`

**Scenarios liên quan:** SC-ORD-006, SC-ORD-014

#### Screen: Đăng tin thành công

##### Block: Popup kết quả (title + nội dung + 2 nút)

| # | Field/Cột/Action | Rule ngắn (verbatim, xem C-ORD-05) |
|---|-------------------|------------|
| 1 | Icon | Check tròn xanh lá (thành công) |
| 2 | Title | "Đăng tin thành công!" |
| 3 | Nội dung | "Tin của bạn đã được đăng lên bảng tin. Chúng tôi sẽ thông báo ngay khi có người quan tâm." |
| 4 | "Mã tin" (⚠ chỉ 1 trong 2 biến thể thiết kế — xem C-ORD-05) | Vd: "#ECO-2026-0451" |
| 5 | Nút "Theo dõi đơn" | Nút cam, primary → Screen Theo dõi đơn |
| 6 | Nút "Về trang chủ" | Nút viền, secondary → Trang chủ |

**Source Quote:**
> "Đăng tin thành công — 2 lựa chọn: Theo dõi đơn / Về trang chủ" (DOC-v1.0-02 §3.5.4) — bổ sung — "Sau khi bấm 'Đăng tin ngay' → màn 'Đăng tin thành công' (KHÔNG hiển thị mã đơn — mã kỹ thuật vô nghĩa với người dùng); tin xuất hiện ở 'Đơn của tôi' trên trang chủ" (US-D02) — **verbatim xác nhận từ ảnh Figma (DOC-v1.0-04, đã zoom 4x)**: Title "Đăng tin thành công!" — Nội dung "Tin của bạn đã được đăng lên bảng tin. Chúng tôi sẽ thông báo ngay khi có người quan tâm." — Nút "Theo dõi đơn" / "Về trang chủ". ⚠ 2/4 ảnh nguồn (`53410b9a9962e145550cf91680a13bbabaf9b47c`, `c8a72f19d00292f5776ea53759535937bc8f9b9e`) có THÊM dòng "Mã tin: #ECO-2026-0451" trước 2 nút — mâu thuẫn với US-D02 và với 2/4 ảnh còn lại (`1cc41f87de9f6f9aa41e31eb1e783234771fa554`, `b2807d958cc82bbe871a43566a8b1c54ff02c462`) không có dòng này. Xem **C-ORD-05**.

**Source Location:** `DOC-v1.0-02 §3.5.4` + `DOC-v1.0-01 §D1b US-D02` + `DOC-v1.0-04 — images/1cc41f87de9f6f9aa41e31eb1e783234771fa554, b2807d958cc82bbe871a43566a8b1c54ff02c462, 53410b9a9962e145550cf91680a13bbabaf9b47c, c8a72f19d00292f5776ea53759535937bc8f9b9e`

**Analyst Note:** generate-tc nên viết Expected Result CHÍNH theo biến thể KHÔNG có "Mã tin" (khớp US-D02 + đa số nguồn), và thêm 1 TC riêng/note kiểm tra "Mã tin" nếu vibe-test trên app thật thấy dòng này xuất hiện — không assert cứng nhắc 1 trong 2 khả năng khi chưa có xác nhận BA (C-ORD-05).

**Scenarios liên quan:** SC-ORD-003

#### Screen: Chỉnh sửa tin

##### Block: Form điền sẵn

| # | Field/Cột/Action | Rule ngắn |
|---|-------------------|------------|
| 1 | Toàn bộ field như tạo đơn | Điền sẵn data hiện có |
| 2 | Nút "Cập nhật" | Lưu thay đổi |
| 3 | Nút "Huỷ chỉnh sửa" | Bỏ thay đổi |

**Source Quote:**
> "Nút 'Chỉnh sửa' chỉ hiện ở trạng thái Chờ ghép (POSTED); mở màn giống tạo đơn nhưng đã điền sẵn; có nút 'Cập nhật' & 'Huỷ chỉnh sửa'; sau IN_TRANSIT không cho sửa"

**Source Location:** `DOC-v1.0-01 §D1b "User Story — Gửi Hàng" · US-D19`

**Scenarios liên quan:** SC-ORD-008, SC-ORD-009

### ASN — Ghép nối

#### Screen: Chi tiết tin (nút hành động vận chuyển)

##### Block: Nút hành động vận chuyển

| # | Field/Cột/Action | Rule ngắn |
|---|-------------------|------------|
| 1 | Nút "Tôi mang giúp được" | Ẩn nếu người xem = chủ tin/Người nhận của đơn (xem C-ASN-02) |

**Source Quote:**
> "Bấm 'Tôi mang giúp được' → hiện modal xác nhận" (DOC-v1.0-02 §4.2) — "OPR-05 Không tự khớp với chính mình — Không gợi ý tin do chính người đó đăng; người gửi ≠ người vận chuyển của cùng một đơn" (DOC-v1.0-01 §D7)

**Source Location:** `DOC-v1.0-02 §4.2 "Màn hình Chi tiết tin — hành động chính"` + `DOC-v1.0-01 §D7 row OPR-05`

**Scenarios liên quan:** SC-ASN-001, SC-ASN-011

#### Screen: Modal xác nhận mang giúp

##### Block: Xác nhận 2 nút

| # | Field/Cột/Action | Rule ngắn |
|---|-------------------|------------|
| 1 | Nội dung cảnh báo | SĐT 2 bên sẽ lộ sau khi xác nhận |
| 2 | Nút Huỷ / Xác nhận | Xác nhận → MATCHED |

**Source Quote:**
> "Modal 'Xác nhận mang giúp' — SĐT hai bên sẽ được lộ sau khi xác nhận" và "Bấm Xác nhận → đơn chuyển trạng thái 'Đã ghép'; CẢ 3 khung (Người gửi / Người vận chuyển / Người nhận) đổi trạng thái tức thời"

**Source Location:** `DOC-v1.0-02 §4.2 "Màn hình Chi tiết tin — hành động chính"`

**Scenarios liên quan:** SC-ASN-002, SC-ASN-004, SC-ASN-005

#### Screen: Đăng tin → "Tôi nhận giao hàng" (đăng ký chuyến đi)

##### Block: Form đăng ký tuyến

| # | Field/Cột/Action | Rule ngắn |
|---|-------------------|------------|
| 1 | Thông tin của tôi | Tên, SĐT — tự động điền |
| 2 | Điểm xuất phát (A) | Tự động điền theo địa chỉ mặc định |
| 3 | Điểm đến (B) | Nhập tay |
| 4 | Khoảng thời gian, Thời gian di chuyển | Từ/đến ngày, khởi hành/đến nơi |
| 5 | Checkbox điều khoản | Đồng ý điều khoản FoxEco |

**Source Quote:**
> "Thông tin của tôi | Tên, SĐT — tự động điền theo tài khoản — Điểm xuất phát (A) | Tự động điền theo địa chỉ mặc định — Điểm đến (B) | Nhập tay, placeholder 'Bạn sẽ đến đâu?' — Khoảng thời gian (ngày) | Từ ngày / Đến ngày — Thời gian di chuyển | Khởi hành / Đến nơi — Checkbox điều khoản | Đồng ý Điều khoản sử dụng FoxEco"

**Source Location:** `DOC-v1.0-02 §4.4 "Màn hình Đăng tin → 'Tôi nhận giao hàng'" · Table 13`

**Scenarios liên quan:** SC-ORD-002, SC-ASN-006

#### Screen: Đã ghi nhận tuyến đường

##### Block: Thông báo kết quả

| # | Field/Cột/Action | Rule ngắn |
|---|-------------------|------------|
| 1 | Giải thích | Tuyến được lưu (không công khai); hệ thống tự tìm người gửi phù hợp |

**Source Quote:**
> "Sau khi đăng → màn 'Đã ghi nhận tuyến đường' giải thích: tuyến được lưu (không công khai), khi có người cần gửi trùng điểm lấy & điểm giao hệ thống sẽ gửi thông báo để bạn xem xét"

**Source Location:** `DOC-v1.0-01 §D1b "User Story — Gửi Hàng" · US-D11`

**Scenarios liên quan:** SC-ASN-006, SC-ASN-007

### DLV — Thực hiện giao hàng

#### Screen: Theo dõi đơn (Sender)

##### Block: Trạng thái & lộ trình

| # | Field/Cột/Action | Rule ngắn |
|---|-------------------|------------|
| 1 | Thanh 5 bước trạng thái | Chờ ghép → Lấy hàng → Đang giao → Đã giao → Hoàn thành |
| 2 | Lộ trình | Điểm lấy/giao + bản đồ ~X km |
| 3 | Liên hệ Người vận chuyển | Chỉ hiện sau khi ghép |
| 4 | Lịch sử | Timeline: Đăng tin→Ghép→Lấy hàng→Đã giao→Hoàn thành |
| 5 | Trạng thái ở đáy màn | Chỉ là nhãn, Sender thụ động ở bước này |

**Source Quote:**
> "Thanh 5 bước trạng thái | Chờ ghép → Lấy hàng → Đang giao → Đã giao → Hoàn thành — Liên hệ Người vận chuyển | Chỉ hiện sau khi ghép: tên + SĐT + nút Gọi — Lịch sử | Timeline mốc sự kiện — Trạng thái ở đáy màn | Chỉ là NHÃN thông tin, không phải nút hành động — Người gửi thụ động ở bước này"

**Source Location:** `DOC-v1.0-02 §3.6 "Màn hình Theo dõi đơn (nhãn phụ 'Tôi gửi hàng')" · Table 9`

**Scenarios liên quan:** SC-DLV-005, SC-DLV-006, SC-ORD-004

#### Screen: Theo dõi đơn (Carrier)

##### Block: Liên hệ 2 phía

| # | Field/Cột/Action | Rule ngắn |
|---|-------------------|------------|
| 1 | NGƯỜI GỬI + NGƯỜI NHẬN | Tên + SĐT + nút Gọi cho cả 2 |

**Source Quote:**
> "Liên hệ 2 phía | Hiển thị cả 'NGƯỜI GỬI' và 'NGƯỜI NHẬN' (tên + SĐT + nút Gọi) — vai trò trung gian cần liên hệ cả 2 đầu"

**Source Location:** `DOC-v1.0-02 §4.3 "Màn hình Theo dõi đơn (nhãn phụ 'Tôi giao hàng')" · Table 11`

**Scenarios liên quan:** SC-DLV-001, SC-DLV-003

##### Block: Nút hành động theo trạng thái

| # | Field/Cột/Action | Rule ngắn |
|---|-------------------|------------|
| 1 | Trạng thái "Lấy hàng" | Nút "✓ Tôi đã lấy hàng" → modal xác nhận |
| 2 | Trạng thái "Đang giao" | Nút "✓ Đã giao cho người nhận" → modal xác nhận |
| 3 | Trạng thái "Đã giao" | Nhãn không bấm được — chờ Receiver xác nhận |

**Source Quote:**
> "Trạng thái 'Lấy hàng' | Nút '✓ Tôi đã lấy hàng' → modal xác nhận — Trạng thái 'Đang giao' | Nút '✓ Đã giao cho người nhận' → modal xác nhận — Trạng thái 'Đã giao' | Nút chuyển thành NHÃN không bấm được: 'Đã giao · chờ người nhận xác nhận' — quyền chốt đơn chuyển sang Người nhận"

**Source Location:** `DOC-v1.0-02 §4.3 "Màn hình Theo dõi đơn" · Table 12`

**Scenarios liên quan:** SC-DLV-006, SC-DLV-010

#### Screen: Theo dõi đơn (Receiver)

##### Block: Liên hệ & nút xác nhận

| # | Field/Cột/Action | Rule ngắn |
|---|-------------------|------------|
| 1 | Liên hệ | Sau khi ghép: chỉ "NGƯỜI GIAO HÀNG" (tên carrier + SĐT + Gọi) |
| 2 | Nút CTA | Bị động ở Chờ ghép/Lấy hàng/Đang giao; active (cam) khi = "Đã giao": "✓ Xác nhận đã nhận hàng" |
| 3 | Sau khi xác nhận | Đơn → "Hoàn thành" ngay, lịch sử ghi "Hoàn thành & đã đánh giá" |

**Source Quote:**
> "Liên hệ | Sau khi ghép: chỉ hiện 'NGƯỜI GIAO HÀNG' (tên carrier + SĐT + Gọi) — không hiện lại thông tin Người gửi — Nút CTA | Bị động (không hành động) ở Chờ ghép/Lấy hàng/Đang giao; CHỈ kích hoạt (cam, bấm được) khi = 'Đã giao': '✓ Xác nhận đã nhận hàng' — Sau khi xác nhận | Đơn chuyển 'Hoàn thành' NGAY LẬP TỨC, lịch sử ghi 'Hoàn thành & đã đánh giá'"

**Source Location:** `DOC-v1.0-02 §5.2 "Màn hình Theo dõi đơn (nhãn phụ 'Tôi nhận hàng')" · Table 14`

**Scenarios liên quan:** SC-DLV-005, SC-DLV-011, C-DLV-01

#### Screen: Xác nhận đã nhận hàng (đầy đủ)

##### Block: Form chi tiết

| # | Field/Cột/Action | Rule ngắn |
|---|-------------------|------------|
| 1 | Thông tin Carrier | Tên + đơn vị/phòng ban + điểm uy tín |
| 2 | Điểm lấy hàng | Địa chỉ carrier đã lấy hàng |
| 3 | Ảnh bằng chứng | Khuyến nghị, không bắt buộc |

**Source Quote:**
> "Thông tin Carrier | Tên + đơn vị/phòng ban + điểm uy tín (vd: Trần Thị Lan, Marketing, ★4.9) — Điểm lấy hàng | Địa chỉ nơi carrier đã lấy hàng — Ảnh bằng chứng (khuyến nghị) | 'Chụp ảnh hàng khi nhận — làm bằng chứng khi có tranh chấp'"

**Source Location:** `DOC-v1.0-02 §5.3 "Xác nhận đã nhận hàng (phiên bản chi tiết)" · Table 15`

**Scenarios liên quan:** SC-DLV-011, C-DLV-03

#### Screen: Theo dõi đơn — Ma trận nhãn nút theo trạng thái (3 vai trò)

##### Block: Nhãn nút hành động x trạng thái x vai trò

| # | Trạng thái | Người gửi | Người vận chuyển | Người nhận |
|---|---|---|---|---|
| 1 | Chờ ghép | "Đang chờ người vận chuyển nhận đơn" — disable, + "Chỉnh sửa"/"Huỷ đơn" | "Tôi mang giúp được" — enable (ở Chi tiết tin) | "Đang chờ người vận chuyển nhận đơn" — disable, + "Huỷ đơn" |
| 2 | Đã ghép (label stepper: "Lấy hàng") | "Đã ghép · chờ shipper lấy hàng" — disable, + "Huỷ đơn" | "✓ Tôi đã lấy hàng" — enable → popup "Xác nhận" "Bạn xác nhận đã lấy hàng từ người gửi và bắt đầu giao?"; + "✕ Huỷ nhận đơn" (→ popup lý do bắt buộc) | "Đã có người vận chuyển · chờ lấy hàng" — disable, + "Huỷ đơn" |
| 3 | Đang giao | "Đang giao đến người nhận" — disable | "Đã giao cho người nhận" — enable → popup "Xác nhận" "Bạn xác nhận đã giao hàng tận tay người nhận?" | "✓ Đơn đang trên đường đến bạn" — disable |
| 4 | Đã giao | "✓ Đã giao · chờ người nhận xác nhận" — disable | "✓ Đã giao · chờ người nhận xác nhận" — disable | "Xác nhận đã nhận hàng" — enable → popup "Xác nhận" "Bạn xác nhận đã nhận được hàng từ người vận chuyển?" |
| 5 | Hoàn thành | "✓ Cảm ơn người vận chuyển" — enable → sau khi gửi quà thành công đổi thành "Bạn đã đánh giá" (disable) | "✓ Đơn đã hoàn thành ✓" — disable | "Đơn đã hoàn thành ✓" — disable |

**Source Quote:**
> "Quan sát thực tế app STG (không có trong BRD/PRD/docx demo — bổ sung từ testing trực tiếp): nhãn nút + trạng thái enable/disable của cả 3 vai trò tại màn Theo dõi đơn, cho từng bước Chờ ghép/Đã ghép/Đang giao/Đã giao/Hoàn thành, do QA cung cấp." (nguyên văn nhãn giữ đúng theo bảng trên) — **Cập nhật 2026-07-24, đối chiếu & tinh chỉnh verbatim theo ảnh Figma (DOC-v1.0-04)**, xác nhận độc lập cả 15 ô của ma trận qua nhiều ảnh khác nhau (mỗi trạng thái × vai trò có ít nhất 1-3 ảnh xác nhận, xem danh sách image hash ở Source Location). Phát hiện thêm: mỗi hành động "enable" của Carrier/Receiver đều dẫn qua 1 popup "Xác nhận" (title cố định "Xác nhận", nội dung câu hỏi khác nhau theo bước) trước khi đổi trạng thái thật — không chuyển ngay khi bấm nút nền.

**Source Location:** `Quan sát thực tế app STG — QA GiangDC2, xác nhận 2026-07-24` + `DOC-v1.0-04 — images/dc8cf987bf06207a762b814a21eefbe13c40aca3 (Sender/Chờ ghép), 8d3e169fecbbf44a701ef4080c13f30fa4f05568+61ef919488e2c5815b678641d455fe7562ede721 (popup Tôi mang giúp được), 2e2ff7bce0854f5cf86fb8144cfc5b13ee294a02+974b5c529e419b4aa202f084b73bf0b23fac4af5 (Carrier/Lấy hàng), aab3cde0770e9df708be03761ed79208345f380d (Receiver/Lấy hàng), c8cae4c3b2760927a0d1534f7973c7fdcf342a0f+e1699c4f6f52bd9bf1c1277d4db122fb3d0aa978+ca5e7239037e6d21a5fc337235100d6abfb31e6a (Đang giao, cả 3 vai trò), af5416b71dc0e94d97215c8da8c97b77ad1a6003 (Receiver/Đang giao), 8563adc10d2b0697bff7c2f68c4839008ffa5f16+91b08fb10c09ab34d0943d1999b891b029a96526+7d8b4a8cf5c78355a0977f13fa8f1ae3d3b96091+5dc3ce81c38a42c96f6bf3f6bab751e90dcfa3fe+82d9aace478ba585169b74e5bdedec3053e96bbe (Đã giao, cả 3 vai trò), 19490aa9d28bbca1d95f1ccf12e90a09819395a2+2658b17b3798886bf5b50803e13c3538e1037d63+76e115a2e4ff6e73d9e414accebf2d2f6026d341 (Hoàn thành, cả 3 vai trò)`

**Analyst Note:** Nhãn này áp dụng cho màn **Theo dõi đơn** (role-aware, đúng vai trò đang đăng nhập) — KHÔNG áp dụng cho màn **Chi tiết tin** public, nơi đang có bug chưa ẩn đúng nút "Tôi mang giúp được" theo vai trò thực (xem `C-ASN-02`, `SC-ASN-011`). Nhãn "Đã ghép" ở đây (Theo dõi đơn) hiển thị dưới label stepper "Lấy hàng" — cùng 1 trạng thái backend MATCHED nhưng progress-bar dùng chữ "Lấy hàng" cho bước này (khớp §3.6 Table 9 VÀ ảnh Figma); generate-tc dùng "Lấy hàng" làm tên bước trong Given/Expected, "Đã ghép" chỉ dùng khi nói về trạng thái backend/badge. Luồng "Cảm ơn người vận chuyển → Bạn đã đánh giá" ở bước Hoàn thành là **phát hiện mới**, chưa từng ghi nhận ở BRD/PRD/docx demo — bổ sung `REQ-GIFT-003` trong `MEMORY.md`. Xác nhận thêm qua ảnh Figma: đây chính là bằng chứng giải quyết **C-DLV-01** (Receiver-only) — xem `MEMORY.md §6.1`.

**Scenarios liên quan:** SC-DLV-012, SC-DLV-013, SC-DLV-014, SC-GIFT-004 (tham chiếu thêm: SC-DLV-005, SC-DLV-006, SC-DLV-010, SC-DLV-011, SC-ASN-001, SC-ASN-005 đã cover phần logic ai-được-làm-gì; block này chỉ bổ sung ĐÚNG TEXT nhãn hiển thị)

### GIFT — Đánh giá & Quà cảm ơn

#### Screen: Tặng quà

##### Block: 4 lựa chọn quà

| # | Field/Cột/Action | Rule ngắn |
|---|-------------------|------------|
| 1 | Title | "Tặng quà" |
| 2 | Nội dung mở đầu | "Hành trình hoàn thành!" / "Gửi một món quà cảm ơn người vận chuyển" |
| 3 | Label | "Chọn một món quà gửi tặng người vận chuyển" |
| 4 | 🌷 Bông hoa · ☕ Ly cà phê · 🧸 Gấu bông · 👑 Vương miện | Chọn 1 (chip có viền cam khi selected) |
| 5 | Nút "✓ Xác nhận tặng quà" | Gửi ngay không cần xác nhận thêm → popup kết quả |
| 6 | Popup kết quả — Title | "Đã gửi lời cảm ơn!" |
| 7 | Popup kết quả — Nội dung | "Món quà và lời cảm ơn của bạn đã được gửi đến người vận chuyển." |
| 8 | Popup kết quả — Nút | "Về trang chủ" |

**Source Quote:**
> "4 lựa chọn quà: 🌷 Bông hoa · ☕ Ly cà phê · 🧸 Gấu bông · 👑 Vương miện. Xác nhận → modal 'Đã gửi lời cảm ơn!' — tính năng tương tác xã hội, không bắt buộc." — **verbatim xác nhận từ ảnh Figma (DOC-v1.0-04)**: "Tặng quà" / "Hành trình hoàn thành!" / "Gửi một món quà cảm ơn người vận chuyển" / "Chọn một món quà gửi tặng người vận chuyển" / nút "✓ Xác nhận tặng quà" → popup "Đã gửi lời cảm ơn!" — "Món quà và lời cảm ơn của bạn đã được gửi đến người vận chuyển." — nút "Về trang chủ". KHÔNG có UI sao 1-5 ở màn này (xem C-GIFT-01).

**Source Location:** `DOC-v1.0-02 §3.8 "Màn hình Tặng quà"` + `DOC-v1.0-04 — images/5d29d0821b4abe7e831646cdad7fa6cdbea69118, 165aaa39e070e12b4fe61084d05b47959a3111ba, 808c25763c360700f941f055a2c2e9923ee53a31, 851d2b9f636f0e6682ccbf1093f8929028b7cb92`

**Scenarios liên quan:** SC-GIFT-001, SC-GIFT-002

#### Screen: Cá nhân (mục Quà đã nhận)

##### Block: Quà đã nhận

| # | Field/Cột/Action | Rule ngắn |
|---|-------------------|------------|
| 1 | Card đếm số | Theo từng loại quà (bông hoa/ly cà phê/gấu bông/vương miện) |
| 2 | Danh sách lịch sử | Lịch sử nhận quà |

**Source Quote:**
> "Là Carrier, tôi muốn xem tổng hợp 'Quà đã nhận' (đếm theo loại + lịch sử) và 'Đơn đã giúp' trong Trang cá nhân... Trang cá nhân có mục 'Đơn đã giúp' & 'Quà đã nhận'; màn Quà đã nhận hiển thị 1 card đếm số bông hoa/ly cà phê/gấu bông/vương miện + danh sách lịch sử nhận quà"

**Source Location:** `DOC-v1.0-01 §D1b "User Story — Gửi Hàng" · US-D20`

**Scenarios liên quan:** SC-GIFT-003

### CNL — Huỷ đơn

#### Screen: Huỷ đơn (popup)

##### Block: Form lý do bắt buộc

| # | Field/Cột/Action | Rule ngắn |
|---|-------------------|------------|
| 1 | Title (Carrier huỷ nhận) | "Huỷ nhận đơn" |
| 2 | Nội dung | "Bạn chắc chắn muốn huỷ nhận giao đơn này? Đơn sẽ được trả lại bảng tin để người khác nhận." |
| 3 | Label lý do | "Lý do huỷ *" — placeholder "Nhập lý do bạn muốn huỷ nhận đơn (VD: đổi lịch, không cần gửi nữa...)" |
| 4 | Nút Huỷ / Xác nhận | "Xác nhận" disable (xám) tới khi có lý do nhập |
| 5 | Trạng thái cuối (nếu huỷ trước MATCHED) | Screen "Đơn đã huỷ" — nút disabled "Đơn đã huỷ", toàn bộ stepper 5 bước chuyển xám |

**Source Quote:**
> "Huỷ được ở POSTED/MATCHED; popup huỷ bắt buộc nhập lý do (nút Xác nhận khoá tới khi có lý do); đơn huỷ ghi rõ ai huỷ (Người gửi/Người vận chuyển/Người nhận) + lý do, đồng bộ realtime cho cả 3 bên; Carrier huỷ nhận → đơn trả lại bảng tin (về 'Chờ ghép'); sau IN_TRANSIT phải tạo báo cáo sự cố" — **verbatim xác nhận từ ảnh Figma (DOC-v1.0-04)**, biến thể Carrier huỷ đơn đã nhận: Title "Huỷ nhận đơn" — Nội dung "Bạn chắc chắn muốn huỷ nhận giao đơn này? Đơn sẽ được trả lại bảng tin để người khác nhận." — Label "Lý do huỷ *" placeholder "Nhập lý do bạn muốn huỷ nhận đơn (VD: đổi lịch, không cần gửi nữa...)" — nút "Xác nhận" disable tới khi nhập lý do. Sender/Receiver dùng nút "Huỷ đơn" (không kèm form lý do trong ảnh quan sát được — cần đối chiếu thêm nếu Sender/Receiver cũng có form lý do tương tự).

**Source Location:** `DOC-v1.0-01 §D1b "User Story — Gửi Hàng" · US-D16` + `DOC-v1.0-04 — images/6fa300d11fd95aba462b559a90af74e8b7f9b2c9 (form có lý do), 5f681a4a1f4801b2cd32e235e9d72c349f00e618+9e26752d4eaa057f9bc1bb32fea479d5c98b8331+e48b0ea09a90a03dfc2d767eb4578d00c3aa1af7 (biến thể popup Carrier), c2191d9527bd8969f009e572df0c379a4a332a07+d6feddb389f396042f6535d13f5525789960837d (màn "Đơn đã huỷ")`

**Scenarios liên quan:** SC-CNL-001, SC-CNL-002, SC-CNL-003, SC-CNL-004

### NTF — Thông báo

#### Screen: Thông báo

##### Block: Nhóm theo thời gian

| # | Field/Cột/Action | Rule ngắn |
|---|-------------------|------------|
| 1 | Nhóm Hôm nay/Hôm qua/Tuần này | Sắp xếp theo mốc thời gian |

**Source Quote:**
> "Thông báo — nhóm theo Hôm nay / Hôm qua / Tuần này"

**Source Location:** `DOC-v1.0-02 §3.2 "Màn hình Thông báo (chuông ở Header)"`

**Scenarios liên quan:** SC-NTF-001..006 (chung)

##### Block: Nội dung theo sự kiện (baseline BA, draft)

| # | Field/Cột/Action | Rule ngắn |
|---|-------------------|------------|
| 1-9 | NTF-01..09 | Xem MEMORY.md §4.1 REQ-NTF-001 Source Quote #1 |

**Source Quote:** see `MEMORY.md §4.1 REQ-NTF-001` (verbatim bảng D6).

**Source Location:** `DOC-v1.0-01 §D6 "Thông báo (Notifications)"`

**Scenarios liên quan:** SC-NTF-001, SC-NTF-002, SC-NTF-003, SC-NTF-004, SC-NTF-005

##### Block: Nội dung thực tế trên UI (DOC-v1.0-04 — ưu tiên dùng cho copy verbatim trong TC)

| # | Icon | Title | Nội dung | Thời gian mẫu |
|---|------|-------|----------|----------------|
| 1 | 🎁 | "Bạn nhận được một món quà cảm ơn 🎁" | "Đồng Công Chí Linh đã gửi tặng bạn một món quà vì đã giúp giao hàng. Mở trang cá nhân để xem." | Vừa xong |
| 2 | 🤝 | "Tìm thấy đơn hàng phù hợp tuyến của bạn" | "Có người cần gửi "Đồ điện tử · Lô B3 → Q.3" trùng tuyến bạn đã đăng. Xem chi tiết để nhận giao." | 5 phút trước |
| 3 | 📞 | "Ghép thành công — SĐT đã được lộ" | "Bạn và Trần Thị Lan đã được kết nối. Liên hệ để sắp xếp lấy hàng.ép giao nhận." (⚠ nghi lỗi chữ trong thiết kế gốc — verify với design trước khi đưa vào TC) | 48 phút trước |
| 4 | ❌ | "Đơn của bạn đã bị người vận chuyển huỷ" | "Lý do: "[lý do free-text]". Đơn đang chờ người vận chuyển mới nhận giúp." | 35 phút trước |
| 5 | 🕐 | "Sắp đến khung giờ hẹn giao" | "Đơn của bạn hẹn giao trong khung [khung giờ] hôm nay." | 1 giờ trước |
| 6 | ✅ | "Đơn đã hoàn thành — đánh giá ngay" | ""[Tên tin]" đã giao xong. Hãy đánh giá [Tên Carrier] để giúp cộng đồng tin cậy hơn." | Hôm qua · 18:20 |
| 7 | ⭐ | "Bạn nhận được đánh giá 5 sao" | "[Tên người đánh giá]: "[nhận xét]"" | Hôm qua · 09:40 |
| 8 | 🔀 | "Có chuyến đi mới hợp tuyến của bạn" | "[Tên] vừa đăng chuyến [tuyến]..." (bị cắt trong ảnh nguồn, chưa đọc được hết) | — |
| — | — | Header "Thông báo", nút "Đánh dấu đã đọc" (góc phải), nhóm theo "HÔM NAY"/"HÔM QUA", chấm đỏ = chưa đọc | | |

**Source Quote:** xem `MEMORY.md §4.1 REQ-NTF-001` Source Quote #2 (verbatim đầy đủ + trích dẫn ảnh).

**Source Location:** `DOC-v1.0-04 — images/db4dfb7e4f07138be5712aff5cb7dea61d983353, 1c6c57c1a6356fee121b59007f85478d244d43d2` (đã zoom 4x xác nhận)

**Analyst Note:** Danh sách này KHÔNG khớp hoàn toàn NTF-01..09 (baseline BA ở block trên) — thiếu tương đương NTF-05/06 (mốc giao/nhận riêng biệt), thừa 3 loại mới (nhắc giờ giao, đánh giá x2). Dùng bảng này làm nguồn verbatim ưu tiên khi viết Expected Result trong TC (đúng yêu cầu "text+button chính xác" của dự án); dùng bảng NTF-01..09 phía trên làm baseline logic sự kiện/actor cho các trường hợp chưa có ảnh xác nhận trực tiếp (đặc biệt NTF-06 hoàn tất đơn). Xem **C-NTF-01** (MEMORY.md §6).

**Scenarios liên quan:** SC-NTF-001, SC-NTF-002, SC-NTF-003, SC-NTF-004, SC-NTF-005

### TS — Trust & Safety / Admin

> Không có Screen/Block UI cụ thể — TS-01/02/03 là backend/log + Admin Web Portal chưa có đặc tả UI trong tài liệu hiện có (xem **C-TS-01** ở `MEMORY.md §6`). Scenario TS test ở mức hệ quả quan sát được từ phía end-user (timeline hiển thị đúng, đơn chuyển "admin hỗ trợ" khi quá hạn) thay vì thao tác trực tiếp UI Admin.

## Scenarios — NEW & MODIFIED (chi tiết đầy đủ)

### USR — Tài khoản & Hồ sơ

| Scenario ID | Feature | Screen | Block | Req ID | DOC Source | Given | When | Then | Priority | Test Type | Lifecycle |
|-------------|---------|--------|-------|--------|-----------|-------|------|------|----------|-----------|-----------|
| SC-USR-001 | Đăng nhập SSO | — | — | REQ-USR-001 | DOC-v1.0-01 | User có tài khoản FPT hợp lệ, mở app FoxPro | Đăng nhập qua SSO nội bộ | Nhận JWT, role, profile → vào app FoxEco thành công | P1 | Functional | NEW |
| SC-USR-002 | Xem hồ sơ cá nhân (view-only) | Cá nhân | Thông tin định danh | REQ-USR-002 | DOC-v1.0-01 | Đã đăng nhập, ở màn Cá nhân | Xem hồ sơ (tên, SĐT, avatar, phòng ban, khu vực, kênh liên hệ) — ⚠ KHÔNG có chức năng cập nhật, xác nhận view-only trên app STG thật (C-USR-03, Resolved) | Hồ sơ hiển thị đúng dữ liệu cho cả 6 trường; không có UI/nút chỉnh sửa nào | P2 | Functional | NEW |
| SC-USR-003 | Hiển thị phòng ban + khu vực | Cá nhân | Thông tin định danh | REQ-USR-003 | DOC-v1.0-01 | Đã đăng nhập | Mở màn Cá nhân/header tin đăng | Hiển thị đúng phòng ban + khu vực/tỉnh của user | P2 | UI | NEW |
| SC-USR-004 | Chỉ số cá nhân đúng theo BRD (2 chỉ số) | Cá nhân | Chỉ số đóng góp | REQ-USR-004 | DOC-v1.0-01, DOC-v1.0-02 | Đã đăng nhập, có lịch sử đơn/quà | Mở màn Cá nhân | Hiển thị đúng "Tổng đơn đã giúp" + "Tổng quà đã nhận"; KHÔNG hiện điểm ECO/hạng thành viên/CO₂ (⚠ chờ C-USR-01) | P2 | Business Rule | NEW |
| SC-USR-005 | Cấu hình kênh liên hệ sẽ lộ (⚠ GAP — chưa có UI, xem C-USR-02) | Cá nhân | Kênh liên hệ | REQ-USR-005 | DOC-v1.0-01 | Đã đăng nhập | Bật/tắt hiển thị Workplace/email | SĐT luôn lộ (bắt buộc); email lộ theo cấu hình (⚠ generate-tc: viết TC dạng "GAP finding" thay vì test hành vi tới khi BA xác nhận — Project_rule.md §10.1) | P3 | Functional | NEW |

#### Source Detail per Scenario

##### SC-USR-001..005 — Đăng nhập, hồ sơ, chỉ số cá nhân
**Source Quote:** see `MEMORY.md §4.1 REQ-USR-001..005`.
**Analyst Note:** SC-USR-004 là scenario nhạy cảm nhất module — expected result phụ thuộc trực tiếp kết quả resolve **C-USR-01 (BLOCKER)**; hiện viết theo BRD (2 chỉ số, không tier/điểm) làm baseline. SC-USR-002 đã xác nhận **view-only** trên app STG thật (không có chức năng cập nhật hồ sơ) — xem **C-USR-03 (Resolved)**; generate-tc chỉ viết TC display/verification, không viết TC hành vi cập nhật/lưu cho scenario này.

### ORD — Đăng tin

| Scenario ID | Feature | Screen | Block | Req ID | DOC Source | Given | When | Then | Priority | Test Type | Lifecycle |
|-------------|---------|--------|-------|--------|-----------|-------|------|------|----------|-----------|-----------|
| SC-ORD-001 | Đăng tin NEED qua wizard | Wizard đăng tin — Bước 1/3, 2/3, 3/3 | Form thông tin hàng, Người gửi, Người nhận, Thời gian, Tóm tắt & điều khoản | REQ-ORD-001, REQ-ORD-002 | DOC-v1.0-01, DOC-v1.0-02 | User chọn "Tôi cần gửi hàng" | Điền đủ B1→B2→B3, tick điều khoản, bấm "Đăng tin ngay" | Tin tạo thành công, trạng thái POSTED | P1 | Functional | NEW |
| SC-ORD-002 | Đăng tin OFFER (form 1 bước) | Đăng tin → Tôi nhận giao hàng | Form đăng ký tuyến | REQ-ORD-001, REQ-ORD-002 | DOC-v1.0-01, DOC-v1.0-02 | User chọn "Tôi nhận giao hàng" | Điền điểm A/B, khung giờ, tick điều khoản, gửi | Tuyến ghi nhận (KHÔNG công khai bảng tin), chờ hệ thống tự khớp | P2 | Functional | NEW |
| SC-ORD-003 | Tin xuất hiện ngay ở "Đơn của tôi", không hiện mã đơn | Đăng tin thành công, Trang chủ | Popup kết quả (title + nội dung + 2 nút), "Đơn của tôi" | REQ-ORD-001 | DOC-v1.0-02, DOC-v1.0-04 | Vừa đăng tin NEED thành công | Xem màn "Đăng tin thành công!" rồi về Trang chủ | Title "Đăng tin thành công!", nội dung "Tin của bạn đã được đăng lên bảng tin. Chúng tôi sẽ thông báo ngay khi có người quan tâm.", nút "Theo dõi đơn"/"Về trang chủ"; KHÔNG hiện mã đơn kỹ thuật (⚠ 1 biến thể thiết kế có "Mã tin" — xem C-ORD-05, không assert cứng tới khi BA xác nhận); tin xuất hiện ở "Đơn của tôi" | P2 | UI | NEW |
| SC-ORD-004 | Timeline tin ghi đầy đủ mốc | Theo dõi đơn (Sender) | Trạng thái & lộ trình | REQ-ORD-003 | DOC-v1.0-01, DOC-v1.0-02 | Tin đã qua ≥2 trạng thái | Mở Theo dõi đơn, xem mục Lịch sử | Timeline hiện đủ mốc kèm timestamp | P1 | Functional | NEW |
| SC-ORD-005 | Tin tự động "Hết hạn" khi quá thời gian | Trang chủ, Hoạt động | "Đơn của tôi" | REQ-ORD-004 | DOC-v1.0-01 | Tin POSTED quá thời gian cấu hình mà chưa MATCHED | Hệ thống quét định kỳ | Tin tự chuyển EXPIRED, badge "Hết hạn" + lý do "Không có ai nhận mang giúp trong thời gian đăng" | P1 | Business Rule | NEW |
| SC-ORD-006 | Không tick điều khoản → chặn đăng | Wizard — Bước 3/3 | Tóm tắt & điều khoản | REQ-ORD-005 | DOC-v1.0-01, DOC-v1.0-02 | Ở Bước 3/3, đã bỏ tick checkbox điều khoản | Bấm "Đăng tin ngay" | Chặn đăng, không tạo tin | P2 | Business Rule | NEW |
| SC-ORD-007 | [Gap] Bỏ trống Loại hàng/Giá trị vẫn qua Bước 2 | Wizard — Bước 1/3 | Form thông tin hàng | REQ-ORD-002 | DOC-v1.0-02 | Ở Bước 1/3, không chọn Loại hàng/Giá trị | Bấm "Tiếp theo" | Hành vi hiện tại: cho qua Bước 2 (⚠ xem C-ORD-01, cần BA xác nhận có nên bắt buộc) | P3 | Business Rule | NEW |
| SC-ORD-008 | Chỉnh sửa tin khi "Chờ ghép" | Chỉnh sửa tin | Form điền sẵn | REQ-ORD-006 | DOC-v1.0-01, DOC-v1.0-02 | Tin ở trạng thái POSTED | Bấm "Chỉnh sửa", sửa thông tin, bấm "Cập nhật" | Nút Chỉnh sửa hiện; form điền sẵn; lưu thành công | P2 | Functional | NEW |
| SC-ORD-009 | Khoá chỉnh sửa từ "Đã ghép" trở đi | Theo dõi đơn | — | REQ-ORD-006 | DOC-v1.0-01, DOC-v1.0-02 | Tin đã MATCHED | Tìm nút "Chỉnh sửa" | Không còn nút Chỉnh sửa (khoá hoàn toàn) | P1 | Business Rule | NEW |
| SC-ORD-010 | Chọn nhanh văn phòng FPT preset | Wizard — Bước 2/3 | Người gửi (địa điểm) | REQ-ORD-007 | DOC-v1.0-01 | Ở bước nhập địa điểm | Mở quick-select văn phòng | Hiện 6 preset văn phòng FPT (+ mở rộng theo tỉnh) | P3 | UI | NEW |
| SC-ORD-011 | Email công ty người nhận có trong hệ thống | Wizard — Bước 2/3 | Người nhận | REQ-ORD-008 | DOC-v1.0-01 | Ở Bước 2/3, nhập Email công ty người nhận | Email khớp danh bạ nội bộ | Tự điền tên/SĐT/địa chỉ + báo "Đã tìm thấy trong hệ thống nội bộ" | P2 | Functional | NEW |
| SC-ORD-012 | Email công ty người nhận không tồn tại | Wizard — Bước 2/3 | Người nhận | REQ-ORD-008 | DOC-v1.0-01 | Ở Bước 2/3, nhập Email công ty người nhận | Email không khớp danh bạ | Báo "Không tìm thấy · nhập thủ công", cho phép nhập tay | P2 | Business Rule | NEW |
| SC-ORD-013 | Giá trị hàng vượt ngưỡng → cảnh báo bảo hiểm | Wizard — Bước 1/3 | Form thông tin hàng | REQ-ORD-009 | DOC-v1.0-01 | Nhập Giá trị hàng vượt ngưỡng cấu hình (⚠ ngưỡng chưa xác định — C-ORD-02) | Tiếp tục nhập/submit | Hiện cảnh báo nên mua bảo hiểm bên thứ 3 | P2 | Business Rule | NEW |
| SC-ORD-014 | Đăng tin chứa hàng cấm bị chặn | Wizard — Bước 1/3, Bước 3/3 | Form thông tin hàng, Tóm tắt & điều khoản | REQ-ORD-010 | DOC-v1.0-01, DOC-v1.0-02 | Chọn Loại hàng thuộc danh mục cấm (thuốc/vũ khí/chất nguy hiểm/phi pháp) | Cố gắng đăng tin | Hệ thống chặn/cảnh báo rõ ràng (⚠ cơ chế banner tĩnh hiện tại — xem C-ORD-04) | P1 | Business Rule | NEW |

#### Source Detail per Scenario

##### SC-ORD-001..003 — Đăng tin NEED/OFFER, kết quả đăng thành công
**Source Quote:** see `MEMORY.md §4.1 REQ-ORD-001/002`.
**Analyst Note:** NEED dùng wizard 3 bước; OFFER dùng form 1 bước riêng (US-D10). Kết quả thành công không hiện mã đơn (US-D02).

##### SC-ORD-004..005 — Timeline & tự động hết hạn
**Source Quote:** see `MEMORY.md §4.1 REQ-ORD-003/004`.
**Analyst Note:** SC-ORD-005 cần môi trường/mock để test đúng thời điểm chuyển EXPIRED (giá trị "quá hạn cấu hình" chưa có số cụ thể — C-ORD-03).

##### SC-ORD-006..007 — Điều khoản & validate wizard
**Source Quote:** see `MEMORY.md §4.1 REQ-ORD-005`; SC-ORD-007 xem clarification **C-ORD-01**.
**Analyst Note:** SC-ORD-006 test theo rule chính thức (ORD-09 bắt buộc); SC-ORD-007 ghi nhận GAP hiện tại của demo (không bắt buộc field khác), cần BA xác nhận trước generate-tc coi đây là bug hay hành vi đúng.

##### SC-ORD-008..009 — Chỉnh sửa tin
**Source Quote:** see `MEMORY.md §4.1 REQ-ORD-006`.
**Analyst Note:** Mốc khoá là MATCHED (khớp 3/3 nguồn BR-EDIT-01/OPR-10/ORD-10), không phải IN_TRANSIT như US-D19 AC có thể gây hiểu lầm — xem Analyst Note tại REQ-ORD-006.

##### SC-ORD-010..012 — Địa điểm & auto-fill người nhận
**Source Quote:** see `MEMORY.md §4.1 REQ-ORD-007/008`.
**Analyst Note:** SC-ORD-010 (LOC-03) không có bằng chứng UI trong demo — chỉ có trong BRD, generate-tc cần thận trọng khi chưa vibe-test xác nhận UI thật có quick-select hay không.

##### SC-ORD-013..014 — Ngưỡng giá trị & hàng cấm
**Source Quote:** see `MEMORY.md §4.1 REQ-ORD-009/010`.
**Analyst Note:** SC-ORD-013 blocked bởi **C-ORD-02** (chưa có ngưỡng số). SC-ORD-014 cần làm rõ cơ chế chặn thật (validate vs banner tĩnh) — **C-ORD-04**.

### ASN — Ghép nối

| Scenario ID | Feature | Screen | Block | Req ID | DOC Source | Given | When | Then | Priority | Test Type | Lifecycle |
|-------------|---------|--------|-------|--------|-----------|-------|------|------|----------|-----------|-----------|
| SC-ASN-001 | Carrier bấm "Tôi mang giúp được" | Chi tiết tin | Nút hành động vận chuyển | REQ-ASN-001 | DOC-v1.0-01, DOC-v1.0-02 | Tin đang ở "Chờ ghép", Carrier xem Chi tiết tin (không phải chủ tin) | Bấm "Tôi mang giúp được" | Gửi đề nghị push + in-app tới Sender | P1 | Functional | NEW |
| SC-ASN-002 | Ghép ngay khi Carrier xác nhận | Modal xác nhận mang giúp | Xác nhận 2 nút | REQ-ASN-002 | DOC-v1.0-01, DOC-v1.0-02 | Modal "Xác nhận mang giúp" đang mở | Bấm Xác nhận | Đơn chuyển MATCHED ngay (không cần Sender duyệt riêng), lộ SĐT 2 bên, cả 3 khung đổi trạng thái tức thời | P1 | Business Rule | NEW |
| SC-ASN-003 | SĐT không lộ trước khi ghép | Chi tiết tin | Lộ trình & liên hệ | REQ-ASN-002 | DOC-v1.0-01 | Tin đang "Chờ ghép", chưa có ai xác nhận mang giúp | Người khác xem Chi tiết tin | SĐT Người gửi KHÔNG hiển thị (⚠ xem C-ASN-01 — hành vi demo hiện tại có gap) | P1 | Business Rule | NEW |
| SC-ASN-004 | Chống double-accept | Chi tiết tin | Nút hành động vận chuyển | REQ-ASN-003 | DOC-v1.0-01 | 2 Carrier khác nhau cùng mở Chi tiết tin 1 tin "Chờ ghép" | Cả 2 bấm "Tôi mang giúp được" gần như đồng thời | Chỉ 1 người ghép thành công (transaction lock); người còn lại nhận thông báo tin đã có người nhận | P1 | Business Rule | NEW |
| SC-ASN-005 | Tin ẩn khỏi Bảng tin sau khi ghép | Bảng tin | — | REQ-ASN-003, REQ-ASN-009 | DOC-v1.0-01 | Tin vừa chuyển MATCHED | Carrier khác mở Bảng tin | Tin không còn xuất hiện; không ai bấm "Tôi mang giúp được" được nữa | P1 | Business Rule | NEW |
| SC-ASN-006 | Tự động khớp tuyến OFFER↔NEED | — | — | REQ-ASN-004 | DOC-v1.0-01, DOC-v1.0-02 | Carrier đã đăng tuyến OFFER, có tin NEED mới trùng điểm lấy & điểm giao | Hệ thống quét khớp | Đẩy thông báo "Tìm thấy đơn hàng phù hợp tuyến của bạn" cho Carrier | P1 | Functional | NEW |
| SC-ASN-007 | Carrier "Nhận giao" từ thông báo khớp tuyến | Chi tiết tin | Nút hành động vận chuyển | REQ-ASN-004 | DOC-v1.0-01, DOC-v1.0-02 | Carrier bấm thông báo khớp tuyến, mở Chi tiết tin NEED phù hợp | Bấm "Nhận giao" | Ghép (MATCHED) + lộ liên hệ 2 bên + vào Theo dõi đơn | P2 | Functional | NEW |
| SC-ASN-008 | Trần 5 tin gợi ý | Trang chủ | — | REQ-ASN-005 | DOC-v1.0-01 | Có >5 tin NEED phù hợp tuyến/khu vực Carrier | Carrier mở Trang chủ | Chỉ hiện tối đa 5 tin (mới & gần tuyến nhất) | P3 | Business Rule | NEW |
| SC-ASN-009 | Tin không trùng điểm/khung giờ → không gợi ý | — | — | REQ-ASN-006 | DOC-v1.0-01 | Tin NEED có điểm lấy/giao khác khu vực HOẶC khung giờ không giao nhau với tuyến Carrier | Hệ thống quét khớp | Tin KHÔNG được gợi ý cho Carrier đó | P2 | Business Rule | NEW |
| SC-ASN-010 | Ưu tiên gợi ý theo độ gần rồi thời gian đăng | Trang chủ, Bảng tin | — | REQ-ASN-007 | DOC-v1.0-01 | Có nhiều tin cùng phù hợp tuyến Carrier | Xem danh sách gợi ý | Sắp xếp: gần tuyến nhất trước, cùng độ gần → tin mới đăng trước | P2 | Business Rule | NEW |
| SC-ASN-011 | Không tự khớp với chính mình | Chi tiết tin | Nút hành động vận chuyển | REQ-ASN-008 | DOC-v1.0-01 | Tin do chính user đăng (Sender) hoặc user là Người nhận của đơn | User đó mở Chi tiết tin của đơn đó | Nút "Tôi mang giúp được" ẨN/disable (⚠ xem C-ASN-02 — demo hiện tại chưa ẩn đúng) | P1 | Business Rule | NEW |
| SC-ASN-012 | Tin huỷ bởi Carrier quay lại "Chờ ghép" và khớp lại | Bảng tin | — | REQ-ASN-009 | DOC-v1.0-01 | Carrier huỷ đơn ở trạng thái MATCHED (chưa lấy hàng) | Xác nhận huỷ | Đơn về POSTED, hiện lại Bảng tin, được đưa lại vào luồng khớp | P2 | Business Rule | NEW |

#### Source Detail per Scenario

##### SC-ASN-001..005 — Ghép nối thủ công (bấm "Tôi mang giúp được")
**Source Quote:** see `MEMORY.md §4.1 REQ-ASN-001/002/003`.
**Analyst Note:** SC-ASN-003 test theo rule đúng (BRD BR-CON-02), lưu ý khi vibe-test trên bản hiện tại có thể fail do gap ghi ở C-ASN-01. SC-ASN-004 là test integrity quan trọng nhất module (race condition).

##### SC-ASN-006..007 — Tự động khớp tuyến OFFER
**Source Quote:** see `MEMORY.md §4.1 REQ-ASN-004`.
**Analyst Note:** Chiều bị động (hệ thống chủ động tìm & đẩy thông báo) khác hẳn chiều NEED (Carrier chủ động duyệt Bảng tin).

##### SC-ASN-008..010 — Trần số + điều kiện + ưu tiên gợi ý
**Source Quote:** see `MEMORY.md §4.1 REQ-ASN-005/006/007`.
**Analyst Note:** SC-ASN-009 phụ thuộc định nghĩa "cùng khu vực/tuyến" chưa chốt (C-NTF-02) — test với case rõ ràng (khác tỉnh hẳn) để tránh vùng xám.

##### SC-ASN-011..012 — Chống tự khớp + vòng đời tin khi huỷ
**Source Quote:** see `MEMORY.md §4.1 REQ-ASN-008/009`.
**Analyst Note:** SC-ASN-011 là regression quan trọng — bằng chứng thực tế (docx Table 17 #9) cho thấy bản hiện tại VI PHẠM rule này (xem **C-ASN-02**).

### DLV — Thực hiện giao hàng

| Scenario ID | Feature | Screen | Block | Req ID | DOC Source | Given | When | Then | Priority | Test Type | Lifecycle |
|-------------|---------|--------|-------|--------|-----------|-------|------|------|----------|-----------|-----------|
| SC-DLV-001 | Chụp ảnh hàng lúc nhận | Theo dõi đơn (Carrier) | Liên hệ 2 phía | REQ-DLV-001 | DOC-v1.0-01 | Đơn ở trạng thái MATCHED, Carrier chuẩn bị bấm "Tôi đã lấy hàng" | Chụp ảnh hàng (tuỳ chọn) rồi xác nhận lấy hàng | Ảnh lưu, gắn vào timeline làm bằng chứng | P2 | Functional | NEW |
| SC-DLV-002 | Bỏ qua chụp ảnh vẫn chuyển trạng thái | Theo dõi đơn (Carrier) | Nút hành động theo trạng thái | REQ-DLV-001 | DOC-v1.0-01 | Đơn ở MATCHED | Bấm "Tôi đã lấy hàng" không chụp ảnh | Chuyển IN_TRANSIT bình thường (ảnh không bắt buộc) | P3 | Business Rule | NEW |
| SC-DLV-003 | Bật chia sẻ vị trí khi đang giao | Theo dõi đơn (Carrier) | — | REQ-DLV-002 | DOC-v1.0-01 | Đơn IN_TRANSIT | Carrier bật chia sẻ vị trí | Sender/Receiver xem được vị trí tạm thời | P3 | Functional | NEW |
| SC-DLV-004 | Vị trí tự xoá sau khi đơn đóng | Theo dõi đơn | — | REQ-DLV-002 | DOC-v1.0-01 | Đã bật chia sẻ vị trí, đơn chuyển COMPLETED hoặc CANCELLED | Đơn đóng | Dữ liệu vị trí bị xoá, không còn hiển thị | P3 | Business Rule | NEW |
| SC-DLV-005 | Nút "Xác nhận đã nhận hàng" chỉ active khi Đã giao | Theo dõi đơn (Receiver) | Liên hệ & nút xác nhận | REQ-DLV-003 | DOC-v1.0-01, DOC-v1.0-02 | Đơn ở trạng thái Chờ ghép/Lấy hàng/Đang giao (chưa Đã giao) | Receiver mở Theo dõi đơn | Nút CTA bị động, không bấm được | P1 | Business Rule | NEW |
| SC-DLV-006 | Nút hành động Carrier bị động trước "Đã giao" | Theo dõi đơn (Carrier) | Nút hành động theo trạng thái | REQ-DLV-003 | DOC-v1.0-02 | Đơn đã ở "Đã giao" (DELIVERED) | Carrier xem lại màn Theo dõi đơn | Nút chuyển thành nhãn "Đã giao · chờ người nhận xác nhận", không bấm được | P1 | Business Rule | NEW |
| SC-DLV-007 | Escalate khi quá N giờ chưa xác nhận | Theo dõi đơn (Receiver) | — | REQ-DLV-003 | DOC-v1.0-01 | Đơn ở "Đã giao" quá 2 giờ, Receiver chưa xác nhận | Hệ thống quét định kỳ | Gửi nhắc; quá thêm 2 giờ → chuyển admin hỗ trợ | P2 | Business Rule | NEW |
| SC-DLV-008 | Ghi nhận chi phí đối soát offline | — | — | REQ-DLV-004 | DOC-v1.0-01 | Đơn đã hoàn tất, 2 bên muốn ghi số tiền tham khảo | Nhập số tiền vào field ghi nhận chi phí | Lưu bản ghi tham khảo, KHÔNG kích hoạt thanh toán qua app | P3 | Functional | NEW |
| SC-DLV-009 | Chặn huỷ thường sau IN_TRANSIT | Theo dõi đơn | — | REQ-DLV-005 | DOC-v1.0-01 | Đơn đã IN_TRANSIT (Carrier đã lấy hàng) | User cố huỷ đơn theo đường thường | Bị chặn; chỉ còn lựa chọn "Báo sự cố" | P2 | Business Rule | NEW |
| SC-DLV-010 | Không thể "Đã giao" trước "Tôi đã lấy hàng" | Theo dõi đơn (Carrier) | Nút hành động theo trạng thái | REQ-DLV-006 | DOC-v1.0-01 | Đơn ở MATCHED (chưa bấm "Tôi đã lấy hàng") | Carrier cố bấm "Đã giao cho người nhận" | Nút chưa xuất hiện/disable; phải bấm "Tôi đã lấy hàng" trước | P1 | Business Rule | NEW |
| SC-DLV-011 | Xác nhận đã nhận → Hoàn thành ngay lập tức | Theo dõi đơn (Receiver), Xác nhận đã nhận hàng | Liên hệ & nút xác nhận, Form chi tiết | REQ-DLV-003, REQ-DLV-006 | DOC-v1.0-01, DOC-v1.0-02 | Đơn ở "Đã giao", Receiver mở màn xác nhận | Bấm "✓ Xác nhận đã nhận hàng" | Đơn chuyển COMPLETED ngay lập tức, lịch sử ghi "Hoàn thành & đã đánh giá" (⚠ actor xem C-DLV-01, UI variant xem C-DLV-03) | P1 | Functional | NEW |
| SC-DLV-012 | Nhãn nút Sender/Receiver đúng theo trạng thái Đã ghép/Đang giao | Theo dõi đơn — Ma trận nhãn nút theo trạng thái | Nhãn nút hành động x trạng thái x vai trò | REQ-DLV-003, REQ-DLV-006 | Quan sát thực tế app | Đơn lần lượt ở "Đã ghép" rồi "Đang giao" | Sender và Receiver mở Theo dõi đơn ở từng trạng thái | Sender thấy "Đã ghép. Chờ shipper lấy hàng" rồi "Đang giao đến người nhận" (disable); Receiver thấy "Đã có người vận chuyển" rồi "Đơn đang trên đường đến bạn" (disable) | P2 | UI | NEW |
| SC-DLV-013 | Tại "Đã giao": Sender/Carrier cùng nhãn disable, chỉ Receiver enable | Theo dõi đơn — Ma trận nhãn nút theo trạng thái | Nhãn nút hành động x trạng thái x vai trò | REQ-DLV-003 | Quan sát thực tế app | Đơn ở "Đã giao" (DELIVERED) | Cả 3 vai trò mở Theo dõi đơn | Sender & Carrier cùng thấy nhãn "Đã giao. Chờ người nhận xác nhận" (disable); Receiver thấy "Xác nhận đã nhận hàng" (enable, duy nhất) | P1 | Business Rule | NEW |
| SC-DLV-014 | Carrier/Receiver thấy nhãn "Đơn đã hoàn thành" sau Hoàn thành | Theo dõi đơn — Ma trận nhãn nút theo trạng thái | Nhãn nút hành động x trạng thái x vai trò | REQ-DLV-003 | Quan sát thực tế app | Đơn vừa chuyển COMPLETED | Carrier và Receiver mở lại Theo dõi đơn | Cả 2 thấy nhãn "Đơn đã hoàn thành" (disable) — không còn hành động nào khác | P3 | UI | NEW |

#### Source Detail per Scenario

##### SC-DLV-001..002 — Chụp ảnh lúc nhận (tuỳ chọn)
**Source Quote:** see `MEMORY.md §4.1 REQ-DLV-001`.
**Analyst Note:** Ảnh optional nhưng khuyến nghị mạnh làm bằng chứng tranh chấp — cả 2 nhánh (có/không ảnh) đều phải cho qua được trạng thái tiếp theo.

##### SC-DLV-003..004 — Chia sẻ vị trí
**Source Quote:** see `MEMORY.md §4.1 REQ-DLV-002`.
**Analyst Note:** Mặc định bật/tắt chưa xác định (**C-DLV-02**) — Given của SC-DLV-003 giả định user chủ động bật.

##### SC-DLV-005..007 — Xác nhận đã nhận + escalate
**Source Quote:** see `MEMORY.md §4.1 REQ-DLV-003`.
**Analyst Note:** Actor được quyền xác nhận (Receiver-only hay Receiver/Sender) là **C-DLV-01 (BLOCKER)** — viết Given theo Receiver (đa số nguồn), cần BA xác nhận trước automate.

##### SC-DLV-008 — Ghi nhận chi phí
**Source Quote:** see `MEMORY.md §4.1 REQ-DLV-004`.
**Analyst Note:** Không có UI minh hoạ cụ thể — test ở mức field-level khi có UI thật.

##### SC-DLV-009 — Chặn huỷ sau IN_TRANSIT
**Source Quote:** see `MEMORY.md §4.1 REQ-DLV-005`.
**Analyst Note:** Màn "Báo sự cố" chưa có đặc tả field (**C-CNL-01**) — SC chỉ verify đường huỷ thường bị khoá + tồn tại lối thoát thay thế.

##### SC-DLV-010..011 — Thứ tự bắt buộc & hoàn tất
**Source Quote:** see `MEMORY.md §4.1 REQ-DLV-006, REQ-DLV-003`.
**Analyst Note:** SC-DLV-011 là scenario "chốt đơn" quan trọng nhất module DLV, gắn với 2 clarification (C-DLV-01 actor, C-DLV-03 UI variant) — generate-tc nên tách 2 biến thể UI thành TC riêng nếu BA chốt cả 2 cùng tồn tại theo điều kiện khác nhau.

##### SC-DLV-012..014 — Ma trận nhãn nút theo trạng thái (quan sát thực tế app)
**Source Quote:** see block "Theo dõi đơn — Ma trận nhãn nút theo trạng thái" ở trên (Quan sát thực tế app STG, QA GiangDC2, 2026-07-24).
**Analyst Note:** Nguồn từ testing trực tiếp app thật, không có trong BRD/PRD gốc — ưu tiên dùng làm text chuẩn cho cột Expected Result khi generate-tc (chính xác hơn paraphrase docx "chỉ là nhãn thông tin"). SC-DLV-013 priority P1 vì đây là rule nghiệp vụ cốt lõi (chỉ Receiver được chốt Hoàn thành — liên hệ C-DLV-01); SC-DLV-012/014 priority thấp hơn vì thuần UI-label, không phải business rule.

### GIFT — Đánh giá & Quà cảm ơn

| Scenario ID | Feature | Screen | Block | Req ID | DOC Source | Given | When | Then | Priority | Test Type | Lifecycle |
|-------------|---------|--------|-------|--------|-----------|-------|------|------|----------|-----------|-----------|
| SC-GIFT-001 | Chọn 1/4 loại quà tặng Carrier | Tặng quà | 4 lựa chọn quà | REQ-GIFT-001 | DOC-v1.0-01, DOC-v1.0-02 | Đơn vừa chuyển COMPLETED, Sender xem màn Tặng quà | Chọn 1 trong 4 loại quà (bông hoa/ly cà phê/gấu bông/vương miện) | Chọn được, sẵn sàng gửi | P2 | Functional | NEW |
| SC-GIFT-002 | Gửi quà không cần Carrier xác nhận | Tặng quà | 4 lựa chọn quà | REQ-GIFT-001 | DOC-v1.0-01, DOC-v1.0-02 | Đã chọn 1 loại quà | Xác nhận gửi | Gửi ngay, không chờ Carrier xác nhận; hiện popup "Đã gửi lời cảm ơn!" | P3 | Functional | NEW |
| SC-GIFT-003 | Xem lịch sử/số lượng quà đã nhận | Cá nhân | Quà đã nhận | REQ-GIFT-001 | DOC-v1.0-01, DOC-v1.0-02 | Carrier đã nhận ≥1 quà | Mở mục "Quà đã nhận" ở Trang cá nhân | Hiện card đếm số theo từng loại quà + danh sách lịch sử | P3 | UI | NEW |
| SC-GIFT-004 | Nút "Cảm ơn người vận chuyển" đổi thành "Bạn đã đánh giá" sau khi gửi quà | Theo dõi đơn — Ma trận nhãn nút theo trạng thái, Tặng quà | Nhãn nút hành động x trạng thái x vai trò, 4 lựa chọn quà | REQ-GIFT-003 | Quan sát thực tế app | Đơn COMPLETED, Sender thấy nút "Cảm ơn người vận chuyển" (enable) | Bấm nút, chọn 1 loại quà, gửi thành công | Quay lại Theo dõi đơn/Chi tiết đơn, nút đổi thành nhãn "Bạn đã đánh giá" (disable, không gửi lại được) | P2 | Functional | NEW |

> **REQ-GIFT-002 (RAT-01/02 — đánh giá 1-5 sao) không có scenario** — Testability Blocked, xem **C-GIFT-01** ở `MEMORY.md §6`. Không derive Given/When/Then cho tính năng mâu thuẫn nguồn.

#### Source Detail per Scenario

##### SC-GIFT-001..003 — Quà cảm ơn
**Source Quote:** see `MEMORY.md §4.1 REQ-GIFT-001`.
**Analyst Note:** Đây là module NHẤT QUÁN giữa BRD và demo (không mâu thuẫn) — priority thấp vì tính năng phi-critical (social/gamification nhẹ), nhưng vẫn cần test để đảm bảo luồng hoàn tất đơn không bị chặn bởi bước tặng quà (optional).

##### SC-GIFT-004 — Đổi nhãn nút sau khi gửi quà
**Source Quote:** see `MEMORY.md §4.1 REQ-GIFT-003` (Quan sát thực tế app STG, QA GiangDC2, 2026-07-24).
**Analyst Note:** Phát hiện mới trong quá trình QA trả lời trước generate-tc — REQ-GIFT-001 gốc chỉ mô tả hành động gửi quà, không mô tả việc nút đổi nhãn/khoá lại sau khi gửi. Bổ sung `REQ-GIFT-003` riêng để tránh gán nhầm vào REQ-GIFT-001 (giữ nguyên tắc 1 quote = 1 requirement).

### CNL — Huỷ đơn

| Scenario ID | Feature | Screen | Block | Req ID | DOC Source | Given | When | Then | Priority | Test Type | Lifecycle |
|-------------|---------|--------|-------|--------|-----------|-------|------|------|----------|-----------|-----------|
| SC-CNL-001 | Huỷ đơn — popup bắt buộc lý do | Huỷ đơn (popup) | Form lý do bắt buộc | REQ-CNL-001 | DOC-v1.0-01, DOC-v1.0-02 | Đơn ở POSTED hoặc MATCHED | User bấm "Huỷ đơn" nhưng không nhập lý do | Nút Xác nhận huỷ bị khoá (disable) tới khi có lý do | P1 | Business Rule | NEW |
| SC-CNL-002 | Chặn huỷ khi đã "Đang giao" | Theo dõi đơn | — | REQ-CNL-003 | DOC-v1.0-01 | Đơn đã IN_TRANSIT | User cố tìm/bấm "Huỷ đơn" | Không có lựa chọn huỷ thường (theo OPR-11) | P1 | Business Rule | NEW |
| SC-CNL-003 | Đơn huỷ ghi rõ actor + đồng bộ realtime | Huỷ đơn (popup) | Form lý do bắt buộc | REQ-CNL-001 | DOC-v1.0-01, DOC-v1.0-02 | Đơn ở MATCHED (3 bên đang xem) | 1 bên huỷ kèm lý do hợp lệ | Đơn huỷ ghi rõ vai trò người huỷ + lý do; cả 3 màn đồng bộ trạng thái tức thời | P2 | Business Rule | NEW |
| SC-CNL-004 | Carrier huỷ khi chưa lấy hàng → về "Chờ ghép" | Theo dõi đơn (Carrier) | — | REQ-CNL-002 | DOC-v1.0-01 | Đơn ở MATCHED, Carrier chưa bấm "Tôi đã lấy hàng" | Carrier huỷ nhận | Đơn tự động về POSTED, hiển thị lại Bảng tin | P2 | Business Rule | NEW |

#### Source Detail per Scenario

##### SC-CNL-001..004 — Huỷ đơn
**Source Quote:** see `MEMORY.md §4.1 REQ-CNL-001/002/003`.
**Analyst Note:** SC-CNL-002 là mặt "negative" bổ sung cho REQ-DLV-005 (đường thay thế Báo sự cố) — 2 SC bổ trợ nhau, không trùng lặp (DLV-009 test "có lối thoát Báo sự cố", CNL-002 test "đường huỷ thường bị khoá hoàn toàn").

### NTF — Thông báo

| Scenario ID | Feature | Screen | Block | Req ID | DOC Source | Given | When | Then | Priority | Test Type | Lifecycle |
|-------------|---------|--------|-------|--------|-----------|-------|------|------|----------|-----------|-----------|
| SC-NTF-001 | Thông báo khi ghép ngay | Thông báo | Nội dung theo sự kiện | REQ-NTF-001 | DOC-v1.0-01 | Carrier vừa bấm "Tôi mang giúp được" và hệ thống ghép | Kiểm tra thông báo | Sender nhận NTF-01 ("SĐT đã lộ"); Receiver nhận NTF-02 ("có người vận chuyển nhận giao") | P2 | Functional | NEW |
| SC-NTF-002 | Thông báo khi khớp tuyến OFFER | Thông báo | Nội dung theo sự kiện | REQ-NTF-001 | DOC-v1.0-01 | Hệ thống vừa khớp 1 tuyến OFFER với 1 tin NEED | Kiểm tra thông báo | Carrier nhận NTF-03 ("Tìm thấy đơn hàng phù hợp tuyến của bạn") | P2 | Functional | NEW |
| SC-NTF-003 | Thông báo theo mốc vận chuyển | Thông báo | Nội dung theo sự kiện | REQ-NTF-001 | DOC-v1.0-01 | Carrier lần lượt bấm "Tôi đã lấy hàng" → "Đã giao" → Receiver "Xác nhận đã nhận" | Kiểm tra thông báo mỗi bước | NTF-04 (lấy hàng) → NTF-05 (đã giao) → NTF-06 (hoàn tất) gửi đúng người nhận | P2 | Functional | NEW |
| SC-NTF-004 | Thông báo khi nhận quà cảm ơn | Thông báo | Nội dung theo sự kiện | REQ-NTF-001 | DOC-v1.0-01 | Sender vừa gửi quà cảm ơn | Kiểm tra thông báo | Carrier nhận NTF-07 ("Bạn nhận được một món quà cảm ơn 🎁") | P3 | Functional | NEW |
| SC-NTF-005 | Thông báo khi huỷ đơn / tin quá hạn | Thông báo | Nội dung theo sự kiện | REQ-NTF-001 | DOC-v1.0-01 | (a) Đơn bị huỷ kèm lý do, hoặc (b) tin quá hạn chưa ghép | Kiểm tra thông báo | (a) Các bên còn lại nhận NTF-08 kèm lý do + vai trò người huỷ; (b) Người đăng tin nhận NTF-09 | P2 | Functional | NEW |
| SC-NTF-006 | Trần thông báo khớp/ngày | Thông báo | — | REQ-NTF-002 | DOC-v1.0-01 | Carrier đã nhận số lượng thông báo khớp = ngưỡng cấu hình trong ngày | Có thêm 1 tin mới khớp | Không bắn thêm thông báo (đã đạt trần) — ⚠ ngưỡng cụ thể chưa chốt (C-NTF-02) | P3 | Business Rule | NEW |

#### Source Detail per Scenario

##### SC-NTF-001..006 — Thông báo theo sự kiện vòng đời
**Source Quote:** see `MEMORY.md §4.1 REQ-NTF-001/002`.
**Analyst Note:** Toàn bộ nội dung message trong bảng D6 được doc tự đánh dấu "Nháp — chờ BA review & bổ sung" — SC hiện tại dùng làm baseline, generate-tc cần re-sync nếu nội dung đổi sau khi BA duyệt. SC-NTF-006 ngưỡng cụ thể phụ thuộc C-NTF-02.

### TS — Trust & Safety / Admin

| Scenario ID | Feature | Screen | Block | Req ID | DOC Source | Given | When | Then | Priority | Test Type | Lifecycle |
|-------------|---------|--------|-------|--------|-----------|-------|------|------|----------|-----------|-----------|
| SC-TS-001 | Log ghi đầy đủ mốc tương tác | — | — | REQ-TS-001 | DOC-v1.0-01 | Có sự kiện đăng/ghép/đổi trạng thái/huỷ xảy ra | Kiểm tra timeline/log (qua hệ quả hiển thị ở Theo dõi đơn) | Ghi đủ: ai đăng, ai nhận, mốc thời gian, đổi trạng thái, huỷ (lý do+actor) | P2 | Functional | NEW |
| SC-TS-002 | Log không sửa được sau khi ghi | — | — | REQ-TS-001 | DOC-v1.0-01 | Log/timeline đã ghi 1 sự kiện | Cố gắng chỉnh sửa log (mức API/data, ngoài phạm vi UI thường) | Log bất biến, không cho sửa | P2 | Business Rule | NEW |
| SC-TS-003 | Admin can thiệp hỗ trợ dựa trên log | — | — | REQ-TS-002 | DOC-v1.0-01 | Đơn bị vướng (vd quá hạn xác nhận nhận hàng) | Hệ thống escalate cho Admin (theo BR-CNF-04) | Admin có thể can thiệp hỗ trợ dựa trên log (⚠ UI Admin Portal chưa có đặc tả — C-TS-01) | P3 | Functional | NEW |

#### Source Detail per Scenario

##### SC-TS-001..003 — Log & Admin intervention
**Source Quote:** see `MEMORY.md §4.1 REQ-TS-001/002`.
**Analyst Note:** Test scope v1.0 giới hạn ở hệ quả quan sát được từ phía end-user; SC-TS-002/003 cần API-level hoặc Admin Portal thật để test đầy đủ — hiện ghi nhận ở mức kỳ vọng nghiệp vụ.

## Scenarios — CARRIED (reference only)

| Scenario ID | Tên ngắn | Module | Screen | Block | Origin Version | Priority | Reference |
|-------------|----------|--------|--------|-------|---------------|----------|-----------|

## Scenarios — DEPRECATED

| Scenario ID | Tên ngắn | Module | Deprecated ở | Lý do |
|-------------|----------|--------|-------------|-------|
