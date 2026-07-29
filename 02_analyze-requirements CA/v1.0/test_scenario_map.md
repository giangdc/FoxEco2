# Test Scenario Map — v1.0

## Tổng quan
- Tổng số scenarios: 51 (NEW: 51, MODIFIED: 0, CARRIED: 0)
- Phân bổ priority: P1: 22 | P2: 18 | P3: 11
- **Cập nhật 2026-07-24 (tích hợp BRD v3.1 — DOC-v1.0-02):** +20 scenario mới trong 6 module mới (OFFER, CANCEL, GIFT, NOTIFICATION, ADMIN, MEDIA) + 2 module mở rộng (SENDER +2, ORDER +3). **Toàn bộ 20 scenario mới đều 🚫 Blocked cho TC/vibe-test** (tại thời điểm đó) — BRD đặc tả nhưng bản HTML prototype hiện tại chưa có UI tương ứng. 24 scenario gốc (v1.0 ban đầu) không đổi, vẫn testable như cũ.
- **Cập nhật 2026-07-27 (tích hợp DOC-v1.0-03 — bản prototype cập nhật):** +3 scenario mới (SC-GENERAL-002, SC-GIFT-004, SC-NOTIFICATION-002). **🔓 UNBLOCK OFFER, CANCEL, GIFT, NOTIFICATION** — verify qua Chrome MCP xác nhận cả 4 module đã có UI thật, không còn Blocked vì thiếu implementation. Chỉ còn ADMIN, MEDIA, và SC-ORDER-007 (1 phần) thật sự Blocked. Xem chi tiết từng module bên dưới.
- **Cập nhật 2026-07-27 (lần 2 — field-level Trang chủ + Bảng tin):** +4 scenario mới (SC-GENERAL-003/004, SC-CARRIER-008/009) theo yêu cầu user viết chi tiết field-level cho 2 màn này trước khi generate-tc theo sheet-by-tab. 2/4 có Expected Result "chưa xác định" (SC-GENERAL-004 empty state, SC-CARRIER-009 ảnh vắng mặt) vì chưa quan sát được trong demo — không đoán, cần vibe-test.

## Scenarios — NEW & MODIFIED (chi tiết đầy đủ)

### SENDER

| Scenario ID | Feature | Req ID | DOC Source | Given | When | Then | Priority | Test Type | Lifecycle |
|-------------|---------|--------|-----------|-------|------|------|----------|-----------|-----------|
| SC-SENDER-001 | Chọn vai trò | REQ-SENDER-001 | DOC-v1.0-01 §1.1 | Đang ở trang chủ Sender | Bấm nút "+" (Đăng tin) ở bottom nav | Hiển thị màn "Bạn muốn làm gì?" với đủ 2 lựa chọn "Tôi cần gửi hàng" / "Tôi nhận giao hàng" kèm mô tả | P2 | UI | NEW |
| SC-SENDER-002 | Chọn vai trò | REQ-SENDER-001 | DOC-v1.0-01 §1.1 | Đang ở màn "Bạn muốn làm gì?" | Chọn "Tôi cần gửi hàng" | Chuyển sang wizard đăng tin bước 1 (Loại hàng) | P1 | Functional | NEW |
| SC-SENDER-003 | Wizard bước 1 | REQ-SENDER-002 | DOC-v1.0-01 §1.2 | Đang ở wizard bước 1 | Chọn loại hàng "Đồ điện tử", nhập ghi chú, chọn "Giá trị vừa", bấm "Tiếp theo" | Chuyển sang wizard bước 2, dữ liệu vừa nhập không bị mất khi quay lại | P1 | Functional | NEW |
| SC-SENDER-004 | Wizard bước 2 | REQ-SENDER-003 | DOC-v1.0-01 §1.3 | Đang ở wizard bước 2, đã có sẵn thông tin Người gửi | Điền Tên/SĐT/Địa chỉ Người nhận, chọn khoảng thời gian + khung giờ, bấm "Tiếp theo" | Chuyển sang bước 3 "Tóm tắt đơn gửi hàng" hiển thị đúng dữ liệu vừa nhập | P1 | Functional | NEW |
| SC-SENDER-005 | Đăng tin — validation | REQ-SENDER-004 | DOC-v1.0-01 §1.4 | Đang ở bước 3 tóm tắt, checkbox điều khoản CHƯA tick | Bấm nút "Đăng tin ngay" | Nút không phản hồi / vẫn ở trạng thái disabled, KHÔNG submit đơn | P1 | Validation | NEW |
| SC-SENDER-006 | Đăng tin thành công | REQ-SENDER-004 | DOC-v1.0-01 §1.4 | Đang ở bước 3 tóm tắt, đã điền đủ thông tin | Tick checkbox điều khoản, bấm "Đăng tin ngay" | Hiển thị màn "Đăng tin thành công!" đúng text banner, có 2 CTA "Theo dõi đơn" / "Về trang chủ" | P1 | Functional | NEW |
| SC-SENDER-007 | UI smoke bước 3 | REQ-SENDER-004 | DOC-v1.0-01 §1.4 | Đang ở bước 3 tóm tắt | Quan sát toàn màn hình | Hiển thị đủ block: Tóm tắt đơn (loại hàng·giá trị, khung giờ, người gửi, người nhận, ghi chú), cảnh báo hàng cấm, checkbox điều khoản, nút "Đăng tin ngay" | P2 | UI | NEW |
| SC-SENDER-008 | Theo dõi đơn | REQ-SENDER-005 | DOC-v1.0-01 §1.5 | Vừa đăng tin thành công | Bấm "Theo dõi đơn" | Hiển thị timeline 5 mốc (Chờ ghép/Lấy hàng/Đang giao/Đã giao/Hoàn thành) với mốc "Chờ ghép" active, 4 mốc sau chưa active | P1 | UI | NEW |
| SC-SENDER-009 | Tự điền người nhận qua email | REQ-SENDER-006 | DOC-v1.0-02 §D1b US-D18 | Đang ở wizard bước 2, ô "Email công ty người nhận" ở đầu mục Người nhận | Nhập 1 email công ty có trong hệ thống nội bộ | Tự điền tên/SĐT/địa chỉ người nhận + hiện thông báo "Đã tìm thấy trong hệ thống nội bộ" | P2 | Functional | NEW |
| SC-SENDER-010 | Email không tìm thấy | REQ-SENDER-006 | DOC-v1.0-02 §D1b US-D18 | Đang ở wizard bước 2, ô "Email công ty người nhận" | Nhập 1 email KHÔNG có trong hệ thống nội bộ | Hiện thông báo "Không tìm thấy · nhập thủ công", 3 field tên/SĐT/địa chỉ chuyển sang cho phép nhập tay | P2 | Negative | NEW |

#### Source Detail per Scenario (verbatim quotes — `references/quoting-guide.md`)

##### SC-SENDER-001 — Màn chọn vai trò hiển thị đủ 2 lựa chọn

**Source Quote:**
> ""Bạn muốn làm gì?" với 2 lựa chọn: "Tôi cần gửi hàng" ... "Tôi nhận giao hàng" ..."

**Source Location:** `DOC-v1.0-01 §1.1 "Chọn vai trò"`

**Analyst Note:** UI smoke cấp màn hình, verify cả 2 option cùng hiển thị (không chỉ 1). Tiền đề cho SC-SENDER-002.

##### SC-SENDER-002 — Chọn "Tôi cần gửi hàng" mở wizard bước 1

**Source Quote:**
> ""Tôi cần gửi hàng" — "Bạn có hàng cần gửi, tìm đồng nghiệp đi thuận đường mang hộ""

**Source Location:** `DOC-v1.0-01 §1.1 "Chọn vai trò"`

**Analyst Note:** Đây là entry point duy nhất chạy được end-to-end trong prototype (nhánh còn lại xem C-SENDER-1).

##### SC-SENDER-003 — Điền wizard bước 1 → chuyển bước 2

**Source Quote:**
> "Loại hàng (chip chọn 1) [...] Ghi chú (free text) [...] Giá trị hàng (ước tính) (chip chọn 1) [...] Nút "Tiếp theo""

**Source Location:** `DOC-v1.0-01 §1.2 "Form bước 1 — Chi tiết hàng"`

**Analyst Note:** Given/When/Then dựng theo đúng field order trong doc. Note "dữ liệu không mất khi quay lại" lấy từ hành vi đã verify thực tế (wizard giữ state qua nhiều lần mở lại).

##### SC-SENDER-004 — Điền wizard bước 2 → chuyển bước 3 tóm tắt

**Source Quote:**
> ""Người nhận": tên, SĐT, địa chỉ giao hàng — nhập tay, 3 field text. [...] Nút "Tiếp theo"."

**Source Location:** `DOC-v1.0-01 §1.3 "Form bước 2 — Người gửi / Người nhận / Lịch"`

**Analyst Note:** Given nêu rõ Người gửi pre-filled để phân biệt field nào cần nhập tay (chỉ Người nhận + lịch).

##### SC-SENDER-005 — Chưa tick điều khoản → nút "Đăng tin ngay" không khả dụng

**Source Quote:**
> "Nút "Đăng tin ngay" — disabled cho tới khi tick checkbox điều khoản (đã verify qua browser: nút không phản hồi click khi checkbox chưa tick — cần verify lại bằng test case P1)."

**Source Location:** `DOC-v1.0-01 §1.4 "Bước 3 — Tóm tắt & đăng tin"`

**Analyst Note:** Doc tự đánh dấu "cần verify lại bằng test case P1" — đây chính là scenario đó. Ưu tiên P1 vì là validation gate ngăn submit sai/thiếu đồng ý điều khoản.

##### SC-SENDER-006 — Tick điều khoản + đăng tin ngay → thành công

**Source Quote:**
> "Sau submit → màn "Đăng tin thành công!" — "Tin của bạn đã được đăng lên bảng tin. Chúng tôi sẽ thông báo ngay khi có người quan tâm." — 2 CTA: "Theo dõi đơn" / "Về trang chủ"."

**Source Location:** `DOC-v1.0-01 §1.4 "Bước 3 — Tóm tắt & đăng tin"`

**Analyst Note:** Happy path chính của toàn module SENDER — đã verify thực tế 2 lần (kết quả nhất quán).

##### SC-SENDER-007 — UI smoke bước 3 — đủ block tóm tắt + cảnh báo + điều khoản

**Source Quote:**
> "Hiển thị "Tóm tắt đơn gửi hàng": Loại hàng·Giá trị, Khung giờ, Người gửi (...), Người nhận (...), Ghi chú. [...] Cảnh báo cố định [...] Checkbox bắt buộc trước khi submit"

**Source Location:** `DOC-v1.0-01 §1.4 "Bước 3 — Tóm tắt & đăng tin"`

**Analyst Note:** UI coverage tối thiểu cấp màn hình theo nguyên tắc analyze-requirements — liệt kê đủ block để tránh sót nội dung khi review.

##### SC-SENDER-008 — Theo dõi đơn hiển thị timeline, mốc "Chờ ghép" active

**Source Quote:**
> "Màn "Theo dõi đơn" hiển thị timeline 5 mốc: Chờ ghép → Lấy hàng → Đang giao → Đã giao → Hoàn thành"

**Source Location:** `DOC-v1.0-01 §1.5 "Theo dõi đơn (Sender)"`

**Analyst Note:** Verify trạng thái ban đầu ngay sau đăng tin = "Chờ ghép" — baseline cho các scenario transition ở module ORDER/CARRIER/RECEIVER.

##### SC-SENDER-009 — Nhập email công ty người nhận → tự điền tên/SĐT/địa chỉ

**Source Quote:**
> "Ô "Email công ty người nhận" nằm đầu mục Người nhận; nhập email có trong hệ thống → tự điền tên/SĐT/địa chỉ + báo "Đã tìm thấy trong hệ thống nội bộ""

**Source Location:** `DOC-v1.0-02 §D1b US-D18 Acceptance Criteria`

**Analyst Note:** 🚫 Blocked — field email này chưa tồn tại trong wizard bước 2 của prototype hiện tại. Scenario ghi nhận theo spec BRD, chờ dev implement trước khi generate-tc/vibe-test.

##### SC-SENDER-010 — Email không có trong hệ thống → báo "Không tìm thấy · nhập thủ công"

**Source Quote:**
> "không có → báo "Không tìm thấy · nhập thủ công""

**Source Location:** `DOC-v1.0-02 §D1b US-D18 Acceptance Criteria`

**Analyst Note:** 🚫 Blocked — negative case của SC-SENDER-009, cùng lý do chưa có UI.

---

### CARRIER

| Scenario ID | Feature | Req ID | DOC Source | Given | When | Then | Priority | Test Type | Lifecycle |
|-------------|---------|--------|-----------|-------|------|------|----------|-----------|-----------|
| SC-CARRIER-001 | Xem chi tiết tin | REQ-CARRIER-001 | DOC-v1.0-01 §2.1 | Đang ở trang chủ Carrier, có đơn "Chờ ghép" trong "Tin mới" | Bấm vào 1 item | Hiển thị màn "Chi tiết tin" đủ block: tiêu đề, ảnh sản phẩm, thông tin hàng, lộ trình, khung giờ, người gửi (tên·SĐT·nút Gọi), CTA "Tôi mang giúp được" | P2 | UI | NEW |
| SC-CARRIER-002 | Nhận đơn | REQ-CARRIER-002 | DOC-v1.0-01 §2.2 | Đang ở màn Chi tiết tin, đơn "Chờ ghép" | Bấm "Tôi mang giúp được" → dialog "Xác nhận mang giúp" → bấm "Xác nhận" | Order status chuyển posted → matched ("Đã ghép"), SĐT 2 bên hiện ra, CTA đổi "Tôi đã lấy hàng", đồng bộ badge "Đã ghép" cả 3 màn tức thời | P1 | Functional | NEW |
| SC-CARRIER-003 | Nhận đơn — huỷ dialog | REQ-CARRIER-002 | DOC-v1.0-01 §2.2 | Dialog "Xác nhận mang giúp" đang mở | Bấm "Huỷ" | Đóng dialog, order status giữ nguyên "Chờ ghép", không có gì thay đổi | P2 | Negative | NEW |
| SC-CARRIER-004 | Lấy hàng | REQ-CARRIER-003 | DOC-v1.0-01 §2.3 | Order đang "Đã ghép" | Bấm "Tôi đã lấy hàng" → dialog xác nhận → bấm "Xác nhận" | Order status chuyển matched → in_transit ("Đang giao"), đồng bộ 3 màn, CTA đổi "Đã giao cho người nhận" | P1 | Functional | NEW |
| SC-CARRIER-005 | Giao hàng | REQ-CARRIER-004 | DOC-v1.0-01 §2.4 | Order đang "Đang giao" | Bấm "Đã giao cho người nhận" → dialog xác nhận → bấm "Xác nhận" | Order status chuyển in_transit → delivered ("Đã giao"), CTA Carrier chuyển disabled text "Đã giao · chờ người nhận xác nhận" | P1 | Functional | NEW |
| SC-CARRIER-006 | Giới hạn quyền Carrier | REQ-CARRIER-004 | DOC-v1.0-01 §2.4 | Order đang "Đã giao" (delivered) | Carrier xem màn theo dõi đơn | KHÔNG có nút hành động nào cho phép Carrier tự chuyển đơn sang "Hoàn thành" | P1 | Negative/Permission | NEW |
| SC-CARRIER-007 | Sync hoàn thành | REQ-CARRIER-005 | DOC-v1.0-01 §2.5 | Order đang "Đã giao", Receiver vừa xác nhận đã nhận hàng ở màn của họ | Carrier đang mở màn theo dõi đơn (không thao tác gì) | Trạng thái tự động đồng bộ sang "Hoàn thành", CTA hiện disabled "Đơn đã hoàn thành ✓" | P1 | Functional | NEW |
| SC-CARRIER-008 | Tag "Tin của bạn" EP | REQ-CARRIER-006 | DOC-v1.0-03 | Đang xem Bảng tin | (a) xem tin do chính mình đăng, (b) xem tin của Sender khác | (a) Tag "Tin của bạn" hiện trên list item; (b) Tag KHÔNG hiện | P2 | UI/EP | NEW |
| SC-CARRIER-009 | Ảnh sản phẩm — case không có ảnh | REQ-CARRIER-006 | DOC-v1.0-03 | Mở Chi tiết tin của 1 đơn KHÔNG có ảnh sản phẩm (Sender bỏ qua bước ảnh, vốn tuỳ chọn) | Quan sát section "ẢNH SẢN PHẨM" | ⚠️ Chưa xác định — cần vibe-test xác nhận UI thật xử lý ra sao (ẩn section/placeholder/khác) | P3 | UI/EP | NEW |

#### Source Detail per Scenario

##### SC-CARRIER-001 — UI smoke màn Chi tiết tin

**Source Quote:**
> "Bấm vào item → màn "Chi tiết tin": Tiêu đề dạng "Gửi [loại hàng] từ [điểm lấy] → [điểm giao]" [...] Ảnh sản phẩm, Thông tin hàng [...], Lộ trình [...], Khung giờ, Người gửi [...] CTA cuối trang: nút cam "Tôi mang giúp được""

**Source Location:** `DOC-v1.0-01 §2.1 "Xem tin & xem chi tiết"`

**Analyst Note:** UI coverage tối thiểu cấp màn hình — liệt kê đủ 6 block quan sát được để không sót khi review.

##### SC-CARRIER-002 — Nhận đơn thành công (posted → matched), đồng bộ 3 màn

**Source Quote:**
> "Bấm "Xác nhận" → trạng thái đơn chuyển posted → matched ("Chờ ghép" → "Đã ghép") — đồng bộ tức thời cả 3 màn (đã verify)."

**Source Location:** `DOC-v1.0-01 §2.2 "Nhận đơn (Chờ ghép → Đã ghép)"`

**Analyst Note:** Scenario cốt lõi nhất của toàn app (differentiator = đồng bộ 3 vai trò tức thời). Đã verify thực tế 2 lần, PASS.

##### SC-CARRIER-003 — Bấm "Huỷ" ở dialog xác nhận mang giúp → không đổi trạng thái

**Source Quote:**
> "Dialog xác nhận: [...] 2 nút: "Huỷ" / "Xác nhận""

**Source Location:** `DOC-v1.0-01 §2.2 "Nhận đơn (Chờ ghép → Đã ghép)"`

**Analyst Note:** Doc chỉ mô tả happy path "Xác nhận"; nhánh "Huỷ" suy luận hợp lý từ pattern dialog chuẩn (2-button modal) — chưa được vibe-test riêng, đánh dấu ⏳ trong Scenario Index.

##### SC-CARRIER-004 — Lấy hàng thành công (matched → in_transit)

**Source Quote:**
> "Bấm "Xác nhận" → matched → in_transit ("Đang giao"). CTA đổi thành "Đã giao cho người nhận"."

**Source Location:** `DOC-v1.0-01 §2.3 "Lấy hàng (Đã ghép → Đang giao)"`

**Analyst Note:** Cùng pattern dialog xác nhận như SC-CARRIER-002 — đã verify thực tế.

##### SC-CARRIER-005 — Giao hàng thành công (in_transit → delivered)

**Source Quote:**
> "Bấm "Xác nhận" → in_transit → delivered ("Đã giao"). CTA cuối trang chuyển thành nút disabled, text: "Đã giao · chờ người nhận xác nhận""

**Source Location:** `DOC-v1.0-01 §2.4 "Giao hàng (Đang giao → Đã giao, chờ receiver xác nhận)"`

**Analyst Note:** Then-clause tách rõ 2 phần: (1) status transition, (2) CTA đổi thành disabled — cả 2 đều assert trong TC.

##### SC-CARRIER-006 — Carrier KHÔNG có nút tự hoàn tất đơn ở trạng thái "Đã giao"

**Source Quote:**
> "Carrier không thể tự hoàn tất đơn, phải chờ Receiver."

**Source Location:** `DOC-v1.0-01 §2.4 "Giao hàng (Đang giao → Đã giao, chờ receiver xác nhận)"`

**Analyst Note:** Permission-boundary quan trọng nhất trong toàn spec — nếu Carrier vô tình có quyền tự hoàn tất, phá vỡ tính toàn vẹn nghiệp vụ (Receiver không xác nhận đã nhận hàng thật). Rủi ro High, xem risk_assessment RISK-CARRIER-01.

##### SC-CARRIER-007 — Carrier tự động thấy "Hoàn thành" khi Receiver xác nhận (sync)

**Source Quote:**
> "Khi Receiver xác nhận (xem §3.2) → delivered → completed ("Hoàn thành") — đồng bộ về Carrier, CTA đổi thành disabled, text "Đơn đã hoàn thành ✓"."

**Source Location:** `DOC-v1.0-01 §2.5 "Hoàn thành"`

**Analyst Note:** Verify hướng đồng bộ cross-role (Receiver action → Carrier UI update), không phải self-action.

##### SC-CARRIER-008 — Tag "Tin của bạn" chỉ hiện trên tin của chính mình

**Source Quote:**
> (quan sát trực tiếp qua Chrome MCP, DOC-v1.0-03) List item ở Bảng tin có tag "Tin của bạn" — quan sát thấy tag này XUẤT HIỆN khi xem Bảng tin của Sender với đơn do chính Sender đó đăng, và KHÔNG xuất hiện trên các item khác trong cùng danh sách

**Source Location:** `DOC-v1.0-03` — quan sát UI trực tiếp, không có §section BRD

**Analyst Note:** EP đơn giản 2 partition (của mình / của người khác) nhưng quan trọng vì nếu tag hiện sai sẽ gây nhầm lẫn user không biết đâu là tin họ đã đăng.

##### SC-CARRIER-009 — Ảnh sản phẩm ở Chi tiết tin khi KHÔNG có ảnh

**Source Quote:**
> (suy luận từ REQ-SENDER-002 — "ảnh không bắt buộc" ở wizard đăng tin) — chưa quan sát được tin thực tế nào KHÔNG có ảnh trong dữ liệu demo (mọi tin mẫu đều có sẵn ảnh)

**Source Location:** `DOC-v1.0-03` (chưa quan sát trực tiếp — case cần vibe-test riêng để xác nhận)

**Analyst Note:** Không đoán UI xử lý ra sao khi thiếu ảnh (ẩn hẳn section "ẢNH SẢN PHẨM", hiện placeholder, hay hiện icon mặc định) — Expected Result để "chưa xác định" theo đúng nguyên tắc dự án, cần vibe-test tạo 1 đơn không ảnh để xác nhận trước khi viết TC Steps cụ thể.

---

### RECEIVER

| Scenario ID | Feature | Req ID | DOC Source | Given | When | Then | Priority | Test Type | Lifecycle |
|-------------|---------|--------|-----------|-------|------|------|----------|-----------|-----------|
| SC-RECEIVER-001 | Theo dõi đơn | REQ-RECEIVER-001 | DOC-v1.0-01 §3.1 | Order đang "Chờ ghép" (chưa matched) | Receiver mở màn theo dõi đơn | Block "NGƯỜI GIAO HÀNG" KHÔNG hiển thị | P2 | Negative/UI | NEW |
| SC-RECEIVER-002 | Theo dõi đơn | REQ-RECEIVER-001 | DOC-v1.0-01 §3.1 | Order đã "Đã ghép" trở lên | Receiver mở màn theo dõi đơn | Block "NGƯỜI GIAO HÀNG" hiển thị đúng tên/SĐT Carrier kèm nút Gọi | P1 | Functional | NEW |
| SC-RECEIVER-003 | Xác nhận nhận hàng | REQ-RECEIVER-002 | DOC-v1.0-01 §3.2 | Order đang "Đã giao" (delivered) | Bấm "Xác nhận đã nhận hàng" → dialog xác nhận → bấm "Xác nhận" | Order status chuyển delivered → completed ("Hoàn thành"), đồng bộ 3 màn, mọi CTA chuyển disabled "Đơn đã hoàn thành ✓" | P1 | Functional | NEW |
| SC-RECEIVER-004 | Giới hạn CTA xác nhận | REQ-RECEIVER-002 | DOC-v1.0-01 §3.2 | Order CHƯA ở trạng thái "Đã giao" (vd đang "Đang giao") | Receiver mở màn theo dõi đơn | CTA "Xác nhận đã nhận hàng" KHÔNG hiển thị/không khả dụng | P1 | Negative/Permission | NEW |

#### Source Detail per Scenario

##### SC-RECEIVER-001 — Block "Người giao hàng" ẩn khi đơn chưa ghép

**Source Quote:**
> "hiển thị thêm block "NGƯỜI GIAO HÀNG" (...) — chỉ xuất hiện sau khi đã ghép (trước đó không có Carrier để hiện)."

**Source Location:** `DOC-v1.0-01 §3.1 "Theo dõi đơn (Receiver)"`

**Analyst Note:** Negative counterpart của SC-RECEIVER-002 — conditional rendering cần verify cả 2 chiều (ẩn/hiện).

##### SC-RECEIVER-002 — Block "Người giao hàng" hiện đúng dữ liệu sau khi đã ghép

**Source Quote:**
> "hiển thị thêm block "NGƯỜI GIAO HÀNG" (tên Carrier · SĐT · nút Gọi)"

**Source Location:** `DOC-v1.0-01 §3.1 "Theo dõi đơn (Receiver)"`

**Analyst Note:** Đã verify thực tế: sau khi Carrier "Nguyễn Anh Tuấn" nhận đơn, block hiện đúng tên + SĐT tương ứng.

##### SC-RECEIVER-003 — Xác nhận đã nhận hàng thành công (delivered → completed)

**Source Quote:**
> "Bấm "Xác nhận" → delivered → completed ("Hoàn thành") — đồng bộ tức thời cả 3 màn, CTA đổi thành disabled "Đơn đã hoàn thành ✓"."

**Source Location:** `DOC-v1.0-01 §3.2 "Xác nhận đã nhận hàng (Đã giao → Hoàn thành)"`

**Analyst Note:** Scenario khép vòng đời đơn hàng — happy path chính module RECEIVER, đã verify thực tế 2 lần.

##### SC-RECEIVER-004 — CTA "Xác nhận đã nhận hàng" không hiện khi đơn chưa "Đã giao"

**Source Quote:**
> "Khi đơn ở trạng thái "Đã giao", màn theo dõi đơn của Receiver hiện CTA cam "Xác nhận đã nhận hàng"."

**Source Location:** `DOC-v1.0-01 §3.2 "Xác nhận đã nhận hàng (Đã giao → Hoàn thành)"`

**Analyst Note:** Suy luận ngược (negation) từ câu điều kiện "Khi đơn ở trạng thái Đã giao" — hàm ý CTA không xuất hiện ở các trạng thái khác. Đây là suy luận hợp lý từ văn bản, không phải quote trực tiếp phủ định — Analyst Note ghi rõ derivation, chưa vibe-test riêng (đánh dấu ⏳).

---

### OFFER

> 🔓 **UNBLOCKED 2026-07-27:** BRD đặc tả đầy đủ (Nhóm 3, US-D10→D13) — trước đó tưởng HTML prototype chưa có UI, nhưng verify qua Chrome MCP trên DOC-v1.0-03 xác nhận CÓ UI thật (bấm "+" Đăng tin → "Bạn muốn làm gì?" → "Tôi nhận giao hàng" → form đầy đủ field). TC Status = ⏳ Ready, sẵn sàng generate-tc.

| Scenario ID | Feature | Req ID | DOC Source | Given | When | Then | Priority | Test Type | Lifecycle |
|-------------|---------|--------|-----------|-------|------|------|----------|-----------|-----------|
| SC-OFFER-001 | Đăng tin OFFER | REQ-OFFER-001 | DOC-v1.0-02 §D1b US-D10 | Carrier đang có nhu cầu di chuyển, mở màn đăng tin OFFER | Điền Điểm xuất phát, Điểm đến, Khung giờ, Tên, SĐT + tick đồng ý điều khoản, bấm đăng | Tin OFFER được ghi nhận (lưu vào hệ thống chờ khớp) | P2 | Functional | NEW |
| SC-OFFER-002 | Xác nhận tuyến đã ghi nhận | REQ-OFFER-002 | DOC-v1.0-02 §D1b US-D11 | Vừa đăng tin OFFER thành công | Quan sát màn xác nhận | Hiển thị màn "Đã ghi nhận tuyến đường" giải thích tuyến được lưu (không công khai), sẽ có thông báo khi khớp | P2 | UI | NEW |
| SC-OFFER-003 | Nhận thông báo khớp tuyến | REQ-OFFER-003 | DOC-v1.0-02 §D1b US-D12 | Carrier đã đăng tuyến OFFER; có 1 tin NEED mới trùng điểm lấy & điểm giao | Hệ thống tự quét khớp (không cần thao tác Carrier) | Carrier nhận thông báo "Tìm thấy đơn hàng phù hợp tuyến của bạn" | P2 | Functional | NEW |
| SC-OFFER-004 | Nhận giao từ thông báo | REQ-OFFER-004 | DOC-v1.0-02 §D1b US-D13 | Carrier vừa nhận thông báo khớp tuyến, bấm vào thông báo | Bấm nút "Nhận giao" tại màn chi tiết tin NEED phù hợp | Đơn chuyển MATCHED, lộ liên hệ 2 bên, chuyển vào màn Theo dõi đơn | P1 | Functional | NEW |

#### Source Detail per Scenario

##### SC-OFFER-001 — Carrier đăng tin OFFER thành công

**Source Quote:**
> "Màn đăng tin OFFER 1 màn duy nhất, các trường: Điểm xuất phát, Điểm đến, Khung giờ, Tên, SĐT + tick đồng ý điều khoản"

**Source Location:** `DOC-v1.0-02 §D1b US-D10 Acceptance Criteria`

**Analyst Note:** Khác cấu trúc với wizard SENDER 3 bước — đây chỉ 1 màn duy nhất. **UI Confirmation (DOC-v1.0-03):** verify trực tiếp — form có Thông tin của tôi (tên/SĐT tự điền), Điểm xuất phát (A, tự điền), Điểm đến (B), Khoảng thời gian (Từ ngày/Đến ngày), Thời gian di chuyển (Khởi hành/Đến nơi), checkbox điều khoản, nút "Đăng tin ngay" (disabled tới khi đủ field). Lưu ý: BRD viết gọn "Khung giờ" nhưng UI thật tách 2 nhóm field (ngày + giờ) — viết TC Steps theo UI thật.

##### SC-OFFER-002 — Màn "Đã ghi nhận tuyến đường" hiển thị đúng giải thích

**Source Quote:**
> "màn "Đã ghi nhận tuyến đường" giải thích: tuyến được lưu (không công khai), khi có người cần gửi trùng điểm lấy & điểm giao hệ thống sẽ gửi thông báo để bạn xem xét"

**Source Location:** `DOC-v1.0-02 §D1b US-D11 Acceptance Criteria`

**Analyst Note:** Nhấn mạnh yếu tố privacy (không công khai) — cần TC verify tuyến KHÔNG xuất hiện trên bảng tin công khai. ⚠️ Chưa verify trực tiếp màn kết quả sau khi bấm "Đăng tin ngay" (mới verify tới form nhập) — cần vibe-test xác nhận nội dung chính xác màn "Đã ghi nhận tuyến đường".

##### SC-OFFER-003 — Carrier nhận thông báo khi tuyến khớp NEED

**Source Quote:**
> "Khi một tin NEED trùng điểm lấy & điểm giao với tuyến → hệ thống đẩy thông báo "Tìm thấy đơn hàng phù hợp tuyến của bạn""

**Source Location:** `DOC-v1.0-02 §D1b US-D12 Acceptance Criteria`

**Analyst Note:** Phụ thuộc hệ thống notification (module NOTIFICATION) — nay cả 2 module đều đã unblock. **UI Confirmation (DOC-v1.0-03):** quan sát notification thật "Có chuyến đi mới hợp tuyến của bạn — Lê Hoàng Nam vừa đăng chuyến KCX Tân Thuận → Thủ Đức, 17:30-18:30" trong màn Thông báo — khớp đúng ý spec.

##### SC-OFFER-004 — Bấm "Nhận giao" từ thông báo → MATCHED

**Source Quote:**
> "Tại chi tiết tin NEED phù hợp có nút "Nhận giao"; bấm → ghép (MATCHED) → lộ liên hệ 2 bên → vào màn Theo dõi đơn"

**Source Location:** `DOC-v1.0-02 §D1b US-D13 Acceptance Criteria`

**Analyst Note:** Ưu tiên P1 (giống REQ-CARRIER-002) vì tạo cùng outcome quan trọng (MATCHED). TC nên tái sử dụng phần lớn Steps/Expected của TC-CARRIER-002, chỉ khác điểm vào. ⚠️ Chưa verify riêng bước "Nhận giao" từ thông báo (cần vibe-test).

---

### CANCEL

> 🔓 **UNBLOCKED 2026-07-27:** BRD đặc tả chi tiết (US-D16, CNL-01, BR-CNL-01, OPR-09/11) — trước đó tưởng prototype không có nút/popup Huỷ đơn, nhưng verify qua Chrome MCP trên DOC-v1.0-03 xác nhận CÓ (màn "Theo dõi đơn" → nút "❌ Huỷ đơn" → popup lý do bắt buộc). TC Status = ⏳ Ready, sẵn sàng generate-tc.

| Scenario ID | Feature | Req ID | DOC Source | Given | When | Then | Priority | Test Type | Lifecycle |
|-------------|---------|--------|-----------|-------|------|------|----------|-----------|-----------|
| SC-CANCEL-001 | Validation lý do huỷ | REQ-CANCEL-001 | DOC-v1.0-02 §D1b US-D16 | Popup Huỷ đơn đang mở, ô lý do còn trống | Bấm nút "Xác nhận" mà chưa nhập lý do | Nút "Xác nhận" ở trạng thái khoá (disabled), KHÔNG huỷ được đơn | P1 | Validation | NEW |
| SC-CANCEL-002 | Huỷ đơn thành công | REQ-CANCEL-001 | DOC-v1.0-02 §D1b US-D16 | Popup Huỷ đơn đang mở, order ở trạng thái cho phép huỷ (Chờ ghép/Đã ghép chưa lấy hàng) | Nhập lý do, bấm "Xác nhận" | Đơn chuyển CANCELLED (hoặc về Chờ ghép nếu Carrier huỷ — xem SC-CANCEL-004), ghi rõ vai trò người huỷ + lý do, đồng bộ realtime cả 3 bên | P1 | Functional | NEW |
| SC-CANCEL-003 | Không huỷ được khi đang giao | REQ-CANCEL-002 | DOC-v1.0-02 §D7 OPR-11 | Order đang "Đang giao" (IN_TRANSIT) | Tìm nút "Huỷ đơn" ở mọi màn (Sender/Carrier/Receiver) | KHÔNG có nút "Huỷ đơn" khả dụng cho bất kỳ vai trò nào | P1 | Negative/Permission | NEW |
| SC-CANCEL-004 | Carrier huỷ → trả về Chờ ghép | REQ-CANCEL-003 | DOC-v1.0-02 §D7 OPR-09 | Order đang "Đã ghép" (MATCHED, Carrier chưa "Tôi đã lấy hàng") | Carrier huỷ đơn kèm lý do | Đơn tự động chuyển về "Chờ ghép" (KHÔNG phải CANCELLED hẳn), hiện lại trên bảng tin cho carrier khác | P1 | State | NEW |

#### Source Detail per Scenario

##### SC-CANCEL-001 — Popup huỷ khoá nút "Xác nhận" tới khi nhập lý do

**Source Quote:**
> "popup huỷ bắt buộc nhập lý do (nút Xác nhận khoá tới khi có lý do)"

**Source Location:** `DOC-v1.0-02 §D1b US-D16 Acceptance Criteria`

**Analyst Note:** Cùng pattern validation-gate như checkbox điều khoản ở SENDER (SC-SENDER-005/TC-SENDER-008 existing) — P1 vì ngăn huỷ đơn thiếu lý do (audit requirement, BR-CNL-01). **UI Confirmation (DOC-v1.0-03):** verify trực tiếp — popup "Huỷ đơn hàng" có textarea "Lý do huỷ *" (placeholder "VD: đổi lịch, không cần gửi nữa..."), nút "Xác nhận" khoá tới khi có lý do, nút "Huỷ" để đóng popup không huỷ. Khớp đúng BRD.

##### SC-CANCEL-002 — Huỷ đơn thành công kèm lý do, ghi rõ vai trò người huỷ

**Source Quote:**
> "đơn huỷ ghi rõ ai huỷ (Người gửi/Người vận chuyển/Người nhận) + lý do, đồng bộ realtime cho cả 3 bên"

**Source Location:** `DOC-v1.0-02 §D1b US-D16 Acceptance Criteria`

**Analyst Note:** Cần TC riêng cho từng actor huỷ (Sender/Carrier/Receiver) vì Then khác nhau tuỳ actor (xem SC-CANCEL-004 cho trường hợp riêng của Carrier). ⚠️ Chưa bấm "Xác nhận" thật khi verify (dừng ở bước mở popup để giữ nguyên state demo) — kết quả sau khi huỷ thành công (status CANCELLED, đồng bộ 3 màn) cần vibe-test xác nhận khi thực thi TC thật.

##### SC-CANCEL-003 — KHÔNG ai huỷ được khi đơn đã "Đang giao"

**Source Quote:**
> "đã lấy hàng → sang "Đang giao" thì KHÔNG ai được huỷ"

**Source Location:** `DOC-v1.0-02 §D7 "Rule vận hành" · OPR-11`

**Analyst Note:** Permission-boundary quan trọng nhất của module CANCEL — cùng lớp rủi ro với SC-CARRIER-006 (existing). Sau mốc này, thay Huỷ phải dùng luồng "Báo sự cố" (INCIDENT, ngoài phạm vi phân tích chi tiết ở BRD này). ⚠️ Chưa verify riêng — nút "Huỷ đơn" mới quan sát được ở trạng thái "Chờ ghép", chưa đẩy đơn sang "Đang giao" để xác nhận nút biến mất.

##### SC-CANCEL-004 — Carrier huỷ khi đã ghép (chưa lấy hàng) → đơn về "Chờ ghép"

**Source Quote:**
> "Người vận chuyển huỷ ở trạng thái Đã ghép (chưa "Tôi đã lấy hàng") → đơn tự động về "Chờ ghép" và hiển thị lại trên bảng tin cho người khác nhận"

**Source Location:** `DOC-v1.0-02 §D7 OPR-09`

**Analyst Note:** State transition đặc biệt — khác hành vi CANCELLED chuẩn của SC-CANCEL-002. Dễ nhầm lẫn khi implement/test, ưu tiên P1. ⚠️ Chưa verify riêng (cần vibe-test đẩy đơn tới MATCHED rồi thử huỷ từ phía Carrier).

---

### GIFT

> 🔓 **UNBLOCKED 2026-07-27:** BRD đặc tả (§A7, US-D15/D20, GIFT-01) — trước đó tưởng prototype không có màn tặng quà, nhưng verify qua Chrome MCP trên DOC-v1.0-03 xác nhận CÓ (Hoạt động → Đơn của tôi → Đã hoàn thành → tap đơn → màn "Tặng quà"). TC Status = ⏳ Ready. **Clarification C-GENERAL-2 tái khẳng định (2026-07-27, lần 2)** — DOC-v1.0-03 hiện UI rating (5 sao) mâu thuẫn, nhưng user re-confirm KHÔNG rating sao, coi là prototype inconsistency. **Clarification C-GIFT-2 mới** — màn "Quà đã nhận" nên ở Precondition Carrier (Figma xác nhận), DOC-v1.0-03 đang hiện ở Receiver (khả năng bug wiring).

| Scenario ID | Feature | Req ID | DOC Source | Given | When | Then | Priority | Test Type | Lifecycle |
|-------------|---------|--------|-----------|-------|------|------|----------|-----------|-----------|
| SC-GIFT-001 | UI màn tặng quà | REQ-GIFT-001 | DOC-v1.0-02 §A7; UI DOC-v1.0-03 | Order vừa chuyển "Hoàn thành", Sender đang ở tab "Đã hoàn thành" (Hoạt động → Đơn của tôi), tap vào đơn | Quan sát màn "Tặng quà" | Hiển thị đủ 4 loại quà: bông hoa, ly cà phê, gấu bông, vương miện, kèm subtitle "Hành trình hoàn thành! Gửi một món quà cảm ơn người vận chuyển" | P3 | UI | NEW |
| SC-GIFT-002 | Gửi quà thành công | REQ-GIFT-002 | DOC-v1.0-02 §D1b US-D15; UI DOC-v1.0-03 | Đang ở màn "Tặng quà", đủ 4 loại quà hiển thị | Chọn 1 loại quà (vd "bông hoa"), bấm "Xác nhận tặng quà" | Gửi thành công (⚠️ UI thật CÓ nút xác nhận, khác BRD "gửi ngay không cần xác nhận" — xem Analyst Note) | P2 | Functional | NEW |
| SC-GIFT-003 | Người nhận quà thấy cập nhật | REQ-GIFT-003 | DOC-v1.0-02 §D1b US-D20; UI DOC-v1.0-03 | Sender vừa gửi quà | Mở "Cá nhân" → mục "Quà đã nhận" (Precondition: phone Carrier theo Figma — xem C-GIFT-2) | Nhận thông báo "Bạn nhận được một món quà cảm ơn"; card đếm đúng loại quà + lịch sử nhận quà cập nhật | P3 | Functional | NEW |
| SC-GIFT-004 | Xem lịch sử quà đã nhận | REQ-GIFT-004 | UI DOC-v1.0-03 | Đang ở tab "Cá nhân", có ≥1 lịch sử nhận quà | Tap menu "Quà đã nhận" | Hiển thị "Tổng quà đã nhận: N món" + breakdown 4 ô theo loại + "LỊCH SỬ NHẬN QUÀ" (loại quà + tên người tặng + thời gian, sắp giảm dần) | P3 | UI/Functional | NEW |

#### Source Detail per Scenario

##### SC-GIFT-001 — Màn hoàn tất Sender hiển thị đủ 4 loại quà

**Source Quote:**
> "4 loại quà: bông hoa, ly cà phê, gấu bông, vương miện — biểu tượng phi vật chất"

**Source Location:** `DOC-v1.0-02 §A7 "Phần thưởng — Quà ảo"`

**Analyst Note:** UI smoke đơn giản, P3 vì không chặn happy-path chính. **UI Confirmation (DOC-v1.0-03):** verify trực tiếp, đúng 4 loại quà + đúng đường dẫn navigation.

##### SC-GIFT-002 — Chọn quà → bấm "Xác nhận tặng quà"

**Source Quote:**
> "Gửi ngay, không cần bước xác nhận; người nhận thấy thông báo "Bạn nhận được một món quà cảm ơn""

**Source Location:** `DOC-v1.0-02 §A7`, cross-ref `§D1b US-D15`

**Analyst Note:** Lưu ý pattern KHÁC với mọi transition khác trong app (không có dialog Huỷ/Xác nhận trung gian như REQ-ORDER-002) theo BRD — nhưng UI thật lại CÓ 1 bước xác nhận (nút "Xác nhận tặng quà"). ⚠️ **UI Discrepancy (DOC-v1.0-03):** viết TC Steps có bước bấm "Xác nhận tặng quà" (không phải "chọn xong là gửi ngay" như BRD text). Chưa bấm confirm thật để xem popup "Cảm ơn của bạn đã được gửi" — cần vibe-test xác nhận nội dung chính xác sau khi gửi.

##### SC-GIFT-003 — Người nhận quà thấy thông báo + Cá nhân cập nhật đếm quà

**Source Quote:**
> "màn Quà đã nhận hiển thị 1 card đếm số bông hoa/ly cà phê/gấu bông/vương miện + danh sách lịch sử nhận quà"

**Source Location:** `DOC-v1.0-02 §D1b US-D20 Acceptance Criteria`

**Analyst Note:** Trang "Cá nhân" nay đã confirm có thật (bottom nav). ⚠️ **C-GIFT-2:** BRD nói Carrier nhận quà, nhưng DOC-v1.0-03 hiện màn "Quà đã nhận" ở phone Receiver — Figma board gốc xác nhận màn này thuộc Carrier ("NGƯỜI GIAO"). Viết Precondition theo Figma (Carrier), không theo DOC-v1.0-03.

##### SC-GIFT-004 — Xem lịch sử "Quà đã nhận"

**Source Quote:**
> (quan sát trực tiếp qua Chrome MCP, DOC-v1.0-03) "Tổng quà đã nhận: 8 món" + lưới 4 ô đếm theo loại + "LỊCH SỬ NHẬN QUÀ" (5 dòng: loại quà, tên người tặng, thời gian — vd "Bông hoa — Đồng Công Chí Linh · Hôm nay · 17:20")

**Source Location:** `DOC-v1.0-03` — quan sát UI trực tiếp, không có §section BRD tương ứng (REQ-GIFT-003 chỉ nói chung chung "1 card đếm + lịch sử")

**Analyst Note:** Chi tiết hoá của REQ-GIFT-003 — tách SC riêng vì đủ chi tiết cụ thể để test riêng (đếm đúng số, thứ tự thời gian, đúng tên người tặng). Cùng lưu ý C-GIFT-2 về vai trò hiển thị.

---

### NOTIFICATION

> 🔓 **UNBLOCKED 2026-07-27:** BRD tự đánh dấu "Nháp — chờ BA review & bổ sung" (§D6), trước đó tưởng chưa có hệ thống thông báo trong prototype — verify qua Chrome MCP trên DOC-v1.0-03 xác nhận CÓ (bấm chuông → màn "Thông báo" đầy đủ, nhóm theo HÔM NAY/HÔM QUA/TUẦN NÀY). TC Status = ⏳ Ready. Gộp 9 sự kiện NTF-01→09 vào 1 scenario documentation-level — nay đã verify được nội dung thật cho 1 số sự kiện (xem Analyst Note), số còn lại vẫn cần trigger thật để xác nhận.

| Scenario ID | Feature | Req ID | DOC Source | Given | When | Then | Priority | Test Type | Lifecycle |
|-------------|---------|--------|-----------|-------|------|------|----------|-----------|-----------|
| SC-NOTIFICATION-001 | 9 sự kiện thông báo | REQ-NOTIFICATION-001 | DOC-v1.0-02 §D6; UI DOC-v1.0-03 | Bất kỳ 1 trong 9 sự kiện trigger (NTF-01→09) xảy ra | Hệ thống bắn thông báo tương ứng | Đúng người nhận (theo bảng NTF) thấy đúng nội dung mẫu; SĐT KHÔNG xuất hiện trong nội dung push (OPR-07) | P3 | Functional | NEW |
| SC-NOTIFICATION-002 | Đánh dấu tất cả đã đọc | REQ-NOTIFICATION-002 | UI DOC-v1.0-03 | Màn "Thông báo" đang mở, có ≥1 thông báo chưa đọc (red-dot) | Bấm link "Đánh dấu đã đọc" | Toàn bộ thông báo hết trạng thái chưa đọc; red-dot ở icon chuông biến mất | P3 | Functional | NEW |

#### Source Detail per Scenario

##### SC-NOTIFICATION-001 — 9 sự kiện thông báo bắn đúng nội dung cho đúng người nhận

**Source Quote:**
> Table §D6: NTF-01 "Có người bấm 'Tôi mang giúp được'" → Người gửi: "Đã có người nhận mang giúp đơn của bạn — SĐT đã được lộ để liên hệ" [...] NTF-09 "Tin quá hạn chưa ghép" → Người đăng tin: "Tin của bạn đã quá hạn — gỡ hoặc đăng lại nếu vẫn cần"

**Source Location:** `DOC-v1.0-02 §D6 "Thông báo (Notifications)" · Table NTF-01→09`, cross-ref `§D7 OPR-07 "SĐT chỉ lộ sau khi ghép... không đưa SĐT vào nội dung push"`

**Analyst Note:** Khi generate-tc, nên tách lại thành TC riêng cho từng NTF đã verify được nội dung thật thay vì 1 TC gộp. **UI Confirmation (DOC-v1.0-03):** verify trực tiếp màn "Thông báo" — nội dung quan sát được khớp NTF-01 ("Có người muốn mang giúp đơn của bạn"), NTF-02 ("Ghép thành công — SĐT đã được lộ"), NTF-03 ("Có chuyến đi mới hợp tuyến"), NTF-04 ("Người mang giúp đã nhận hàng"). Riêng nội dung "Đơn đã hoàn thành — đánh giá ngay" / "Bạn nhận được đánh giá 5 sao" quan sát được KHÔNG đưa vào TC (rating — xem C-GENERAL-2, prototype inconsistency). Các NTF còn lại (05,06,08,09) chưa trigger được để verify trong phiên này.

##### SC-NOTIFICATION-002 — Đánh dấu tất cả đã đọc

**Source Quote:**
> (quan sát trực tiếp qua Chrome MCP, DOC-v1.0-03) Header màn "Thông báo" có link "Đánh dấu đã đọc" ở góc phải

**Source Location:** `DOC-v1.0-03` — quan sát UI trực tiếp, không có trong BRD

**Analyst Note:** Chưa bấm thử để verify hành vi thật (red-dot có biến mất không) — cần vibe-test xác nhận khi thực thi TC.

---

### ORDER

| Scenario ID | Feature | Req ID | DOC Source | Given | When | Then | Priority | Test Type | Lifecycle |
|-------------|---------|--------|-----------|-------|------|------|----------|-----------|-----------|
| SC-ORDER-001 | Badge trạng thái | REQ-ORDER-001 | DOC-v1.0-01 §4 | Order đang ở bất kỳ 1 trong 5 mốc | Quan sát badge "Trạng thái đơn" ở header + timeline trên 3 phone | Label và màu badge khớp đúng bảng mapping (posted=xanh dương, matched=tím, in_transit=cam, delivered/completed=xanh ngọc) | P2 | UI | NEW |
| SC-ORDER-002 | Reset demo | REQ-ORDER-002 | DOC-v1.0-01 §4 | Order đang ở giữa luồng (vd "Đang giao") | Bấm "↺ Chạy lại từ đầu" | Order status reset về "Chờ ghép" trên cả 3 màn | P1 | Functional | NEW |
| SC-ORDER-003 | Đồng bộ real-time | REQ-ORDER-002 | DOC-v1.0-01 §4 | 1 hành động chuyển trạng thái vừa thực hiện ở 1 màn (vd Carrier xác nhận lấy hàng) | Quan sát đồng thời 2 màn còn lại, KHÔNG reload trang | Trạng thái ở 2 màn còn lại cập nhật tức thời, không cần thao tác gì thêm | P1 | Functional | NEW |
| SC-ORDER-004 | Dialog xác nhận trung gian | REQ-ORDER-002 | DOC-v1.0-01 §4 | Đang ở bất kỳ bước transition nào (matched/in_transit/delivered/completed) | Bấm nút hành động chính (vd "Tôi mang giúp được") | LUÔN xuất hiện dialog xác nhận trung gian (Huỷ/Xác nhận) trước khi status đổi — không transition thẳng | P2 | UI/Consistency | NEW |
| SC-ORDER-005 | Chỉnh sửa đơn | REQ-ORDER-003 | DOC-v1.0-02 §D1b US-D19 | Order đang "Chờ ghép" (POSTED) | Bấm nút "Chỉnh sửa" | Mở màn giống tạo đơn nhưng đã điền sẵn dữ liệu cũ, có 2 nút "Cập nhật" / "Huỷ chỉnh sửa" | P2 | Functional | NEW |
| SC-ORDER-006 | Khoá chỉnh sửa sau khi ghép | REQ-ORDER-003 | DOC-v1.0-02 §D4 BR-EDIT-01 | Order đã "Đã ghép" (MATCHED) trở đi | Tìm nút "Chỉnh sửa" trên màn theo dõi đơn | KHÔNG hiển thị/không có nút "Chỉnh sửa" khả dụng | P1 | Negative/Permission | NEW |
| SC-ORDER-007 | Tin hết hạn | REQ-ORDER-004 | DOC-v1.0-02 §D1b US-D04 | Order đang "Chờ ghép", quá ngưỡng thời gian cấu hình mà chưa có ai nhận | Hệ thống tự kiểm tra (không cần thao tác người dùng) | Order status tự chuyển "EXPIRED", hiện badge "Hết hạn" ở tab hoàn tất kèm lý do "Không có ai nhận mang giúp trong thời gian đăng" | P2 | State | NEW |

#### Source Detail per Scenario

##### SC-ORDER-001 — Badge trạng thái đúng label + màu theo từng mốc

**Source Quote:**
> Table §4: `posted`→"Chờ ghép"/Xanh dương `#1D4ED8`; `matched`→"Đã ghép"/Tím `#5933EB`; `in_transit`→"Đang giao"/Cam `#B86000`; `delivered`→"Đã giao"/Xanh ngọc `#0F766E`; `completed`→"Hoàn thành"/Xanh ngọc `#0F766E`

**Source Location:** `DOC-v1.0-01 §4 "ORDER STATUS MACHINE" · Table`

**Analyst Note:** 5 giá trị màu hex cụ thể — TC có thể assert bằng computed style nếu automation sau này, hiện tại verify bằng mắt/screenshot.

##### SC-ORDER-002 — "↺ Chạy lại từ đầu" reset order status về "Chờ ghép"

**Source Quote:**
> "ngoại trừ nút toàn cục "↺ Chạy lại từ đầu" reset về `posted` ban đầu"

**Source Location:** `DOC-v1.0-01 §4 "ORDER STATUS MACHINE" · "Ràng buộc quan trọng" bullet 1`

**Analyst Note:** Chỉ assert phần chắc chắn (status reset) — KHÔNG assert hành vi wizard form data (xem Clarification C-ORDER-1, chưa resolve).

##### SC-ORDER-003 — Đồng bộ trạng thái tức thời cả 3 màn không cần reload

**Source Quote:**
> "Đồng bộ 3 màn là tức thời (cùng 1 lần click, không cần reload/refresh) — quan sát qua `window.FoxEcoStore.subscribe`."

**Source Location:** `DOC-v1.0-01 §4 "ORDER STATUS MACHINE" · "Ràng buộc quan trọng" bullet 4`

**Analyst Note:** Đây là scenario differentiator quan trọng nhất của toàn sản phẩm demo — đã verify thực tế xuyên suốt 2 lần chạy full-flow (PASS cả 2).

##### SC-ORDER-004 — Mọi transition đều có dialog xác nhận trung gian

**Source Quote:**
> "Mỗi transition đều có dialog xác nhận trung gian (Huỷ/Xác nhận) — không transition thẳng khi bấm nút chính."

**Source Location:** `DOC-v1.0-01 §4 "ORDER STATUS MACHINE" · "Ràng buộc quan trọng" bullet 2`

**Analyst Note:** Consistency rule áp dụng cho cả 4 transition (matched/in_transit/delivered/completed) — TC nên lặp assert này ở từng bước thay vì chỉ test 1 lần.

##### SC-ORDER-005 — Nút "Chỉnh sửa" chỉ hiện ở "Chờ ghép", mở form điền sẵn

**Source Quote:**
> "Nút "Chỉnh sửa" chỉ hiện ở trạng thái Chờ ghép (POSTED); mở màn giống tạo đơn nhưng đã điền sẵn; có nút "Cập nhật" & "Huỷ chỉnh sửa""

**Source Location:** `DOC-v1.0-02 §D1b US-D19 Acceptance Criteria`

**Analyst Note:** 🚫 Blocked — chưa có nút "Chỉnh sửa" trong prototype hiện tại (Sender chỉ có "Xem tất cả" ở card "Đơn của tôi"). Ghi nhận theo spec BRD.

##### SC-ORDER-006 — Sau khi "Đã ghép" trở đi, KHÔNG cho sửa đơn nữa

**Source Quote:**
> "Chỉ được chỉnh sửa tin khi còn "Chờ ghép" (POSTED); đã MATCHED trở đi khoá chỉnh sửa"

**Source Location:** `DOC-v1.0-02 §D4 "Business Rules" · BR-EDIT-01`

**Analyst Note:** 🚫 Blocked. Permission-boundary cùng lớp rủi ro với SC-CARRIER-006/SC-RECEIVER-004 (existing) — ưu tiên P1 khi có UI để test.

##### SC-ORDER-007 — Tin quá hạn cấu hình chưa ghép → tự chuyển "EXPIRED"

**Source Quote:**
> "Quá hạn cấu hình mà chưa MATCHED → tự chuyển EXPIRED, hiển thị badge "Hết hạn" ở tab hoàn tất kèm lý do "Không có ai nhận mang giúp trong thời gian đăng""

**Source Location:** `DOC-v1.0-02 §D1b US-D04 Acceptance Criteria`

**Analyst Note:** 🚫 Blocked (1 phần) — cơ chế thời gian (worker/cron) chưa tồn tại trong prototype client-side. Ngưỡng thời gian **đã Resolved (C-ORDER-2, 2026-07-27)**: mốc = giá trị field "Từ ngày" đã chọn ở wizard bước 2 (không phải duration cố định như "24h") — khi implement, viết TC boundary quanh mốc "Từ ngày" thay vì số giờ/ngày tự chọn. **UI Confirmation 1 phần (DOC-v1.0-03):** badge "Hết hạn" + text "Không có ai nhận mang giúp trong thời gian đăng — tin đã tự động đóng" CÓ THẬT ở tab "Đã hoàn thành" (lịch sử riêng của Sender). CHƯA verify hành vi ở "Bảng tin" (feed công khai cho Carrier/Receiver khác) — giữ Blocked cho tới khi verify nốt phần đó.

---

### ADMIN

> 🚫 Toàn bộ module ADMIN: BRD liệt kê quyền override chi tiết (§D4 Permission Matrix) nhưng KHÔNG có Admin Web Portal nào trong prototype (chỉ 3 màn Sender/Carrier/Receiver). Spec-only, out of scope test cho tới khi có Admin Portal.

| Scenario ID | Feature | Req ID | DOC Source | Given | When | Then | Priority | Test Type | Lifecycle |
|-------------|---------|--------|-----------|-------|------|------|----------|-----------|-----------|
| SC-ADMIN-001 | Quyền override của Admin | REQ-ADMIN-001 | DOC-v1.0-02 §D4 | Admin đăng nhập Admin Web Portal (chưa tồn tại) | Thực hiện override 1 hành động (vd "Đã nhận hàng" thay Carrier) | Hành động được ghi nhận với actor = Admin, không phải actor gốc | P3 | Permission | NEW |

#### Source Detail per Scenario

##### SC-ADMIN-001 — Admin có quyền override trên các hành động chính

**Source Quote:**
> Table §D4 Permission Matrix, cột ADMIN: "Chấp nhận người ghép ✓ override · 'Đã nhận hàng'/'Đã giao' ✓ override · Xác nhận 'Đã nhận' ✓ override"

**Source Location:** `DOC-v1.0-02 §D4 "Business Rules & Permission Matrix" · bảng phân quyền`

**Analyst Note:** 🚫 Blocked hoàn toàn — không có Admin UI nào để test. Ghi nhận ở mức spec cho tương lai khi Admin Web Portal được xây.

---

### MEDIA

> 🚫 Toàn bộ module MEDIA: 2 tính năng tùy chọn (ảnh bằng chứng + GPS) mô tả trong BRD (§D3 PUP-03/GPS-01) nhưng chưa có UI trong luồng Carrier của prototype (khác với "Ảnh hàng" ở wizard đăng tin Sender — đó là ảnh sản phẩm lúc ĐĂNG, không phải ảnh bằng chứng lúc NHẬN của Carrier).

| Scenario ID | Feature | Req ID | DOC Source | Given | When | Then | Priority | Test Type | Lifecycle |
|-------------|---------|--------|-----------|-------|------|------|----------|-----------|-----------|
| SC-MEDIA-001 | Chụp ảnh hàng lúc nhận | REQ-MEDIA-001 | DOC-v1.0-02 §D3 PUP-03 | Carrier vừa bấm "Tôi đã lấy hàng" | Chụp ảnh hàng (tùy chọn) | Ảnh được lưu, gắn vào timeline đơn làm bằng chứng | P3 | Functional | NEW |
| SC-MEDIA-002 | Chia sẻ vị trí khi đang giao | REQ-MEDIA-002 | DOC-v1.0-02 §D3 GPS-01 | Order đang "Đang giao" (IN_TRANSIT), Carrier bật chia sẻ vị trí (tùy chọn) | Order chuyển "Đã giao" (đóng đơn) | Dữ liệu vị trí bị xoá, không còn active | P3 | Functional | NEW |

#### Source Detail per Scenario

##### SC-MEDIA-001 — Carrier chụp ảnh hàng lúc nhận (tùy chọn, làm bằng chứng)

**Source Quote:**
> "Chụp ảnh hàng lúc nhận: Tùy chọn (khuyến nghị) — lưu S3, gắn timeline làm bằng chứng"

**Source Location:** `DOC-v1.0-02 §D3 "Functional Requirements" · PUP-03`

**Analyst Note:** 🚫 Blocked. "Tùy chọn" nghĩa là không bắt buộc — TC khi có UI cần cover cả case "không chụp ảnh vẫn tiếp tục được luồng bình thường".

##### SC-MEDIA-002 — Chia sẻ vị trí GPS khi đang giao (tùy chọn, tắt sau khi đóng)

**Source Quote:**
> "Chia sẻ vị trí khi đang giao: Tùy chọn; chỉ active khi đang giao; xóa sau khi đóng"

**Source Location:** `DOC-v1.0-02 §D3 "Functional Requirements" · GPS-01`

**Analyst Note:** 🚫 Blocked. Ràng buộc privacy quan trọng (tự xoá sau khi đóng đơn) — nên có TC riêng verify việc xoá đúng thời điểm khi có UI, tránh rò rỉ dữ liệu vị trí sau khi đơn kết thúc.

---

### GENERAL

| Scenario ID | Feature | Req ID | DOC Source | Given | When | Then | Priority | Test Type | Lifecycle |
|-------------|---------|--------|-----------|-------|------|------|----------|-----------|-----------|
| SC-GENERAL-001 | Nội dung tĩnh | REQ-GENERAL-001 | DOC-v1.0-01 §0 | Đang ở màn "Bạn muốn làm gì?" (wizard đăng tin) | Xem banner cảnh báo/tuyên bố | Hiển thị đúng nguyên văn "App không thu phí, không chat, không thanh toán. Sau khi ghép, SĐT hai bên sẽ được lộ để liên hệ ngoài app." | P3 | UI Content | NEW |
| SC-GENERAL-002 | Bottom nav điều hướng | REQ-GENERAL-002 | UI DOC-v1.0-03 | Đang ở bất kỳ màn nào có bottom nav, với 1 trong 3 vai trò | Tap từng icon (Trang chủ/Bảng tin/Đăng tin/Hoạt động/Cá nhân) | Điều hướng đúng màn tương ứng, icon active hiện đúng trạng thái (màu cam), nhất quán cả 3 vai trò | P2 | UI/Navigation | NEW |
| SC-GENERAL-003 | Trang chủ dashboard theo vai trò | REQ-GENERAL-003 | DOC-v1.0-03 | Mở app với vai trò Sender/Receiver | Xem Trang chủ | Hiển thị section "Đơn của tôi" (card đơn hiện tại, badge trạng thái, progress bar, link theo dõi) | P2 | UI/Functional | NEW |
| SC-GENERAL-004 | Empty state Trang chủ | REQ-GENERAL-003 | DOC-v1.0-03 (⚠️ chưa quan sát) | Mở Trang chủ khi KHÔNG có đơn/tin nào (Sender/Receiver không có đơn hoạt động, hoặc Carrier không có tin nào ở feed) | Xem section "Đơn của tôi" / "Tin mới" | ⚠️ Chưa xác định — cần vibe-test xác nhận (ẩn section/hiện text "Chưa có đơn nào"/khác) | P3 | UI/EP | NEW |

#### Source Detail per Scenario

##### SC-GENERAL-001 — Banner "không thu phí/không chat/không thanh toán" hiển thị đúng nội dung

**Source Quote:**
> "App **không** thu phí, không chat, không thanh toán. Sau khi ghép, SĐT hai bên sẽ được lộ để liên hệ ngoài app."

**Source Location:** `DOC-v1.0-01 §0 "Bối cảnh chung (Context)"`

**Analyst Note:** UI content-only scenario, priority thấp nhưng vẫn cần vì là tuyên bố pháp lý/kỳ vọng người dùng — sai lệch nội dung này có thể gây hiểu nhầm nghiêm trọng dù risk kỹ thuật thấp.

##### SC-GENERAL-002 — Bottom nav (5 icon) điều hướng đúng màn, nhất quán 3 vai trò

**Source Quote:**
> (quan sát trực tiếp qua Chrome MCP, DOC-v1.0-03) Thanh điều hướng dưới cùng mỗi phone có 5 icon: "Trang chủ", "Bảng tin", nút tròn cam "+" ở giữa ("Đăng tin"), "Hoạt động", "Cá nhân" — xuất hiện giống hệt trên cả 3 phone

**Source Location:** `DOC-v1.0-03` — quan sát UI trực tiếp, không có §section (không mô tả trong DOC-v1.0-01/02)

**Analyst Note:** Chỉ test navigation (tap đúng icon → đúng màn, active state đúng) — không lặp lại nội dung màn đích (đã có REQ/SC riêng cho Trang chủ/Bảng tin/Hoạt động→GIFT/Cá nhân→GIFT/NOTIFICATION).

##### SC-GENERAL-003 — Trang chủ hiển thị đúng dashboard theo vai trò

**Source Quote:**
> (quan sát trực tiếp qua Chrome MCP, DOC-v1.0-03) Trang chủ Sender/Receiver có section "Đơn của tôi" (card đơn: tiêu đề, badge trạng thái, Từ/Đến, progress bar, link "Chạm để theo dõi đơn của bạn", link "Xem tất cả"); Trang chủ Carrier có thêm/thay bằng section "Tin mới" (danh sách tin đang chờ nhận)

**Source Location:** `DOC-v1.0-03` — quan sát UI trực tiếp, không có §section BRD

**Analyst Note:** Nội dung khác nhau có chủ đích theo vai trò (không phải bug) — viết TC riêng cho từng biến thể thay vì 1 TC chung "hiển thị đúng nội dung". Badge trạng thái dùng chung EP đã có ở SC-ORDER-001, không duplicate ở đây.

##### SC-GENERAL-004 — Empty state "Đơn của tôi" / "Tin mới"

**Source Quote:**
> (chưa quan sát được — dữ liệu demo luôn có sẵn 1 đơn/tin mẫu, không có cách nào qua UI để xoá hết về trạng thái rỗng)

**Source Location:** `DOC-v1.0-03` (gap — chưa thể quan sát trong phạm vi demo hiện tại)

**Analyst Note:** Ghi nhận là gap cần vibe-test/dev xác nhận (có thể cần seed data đặc biệt hoặc code review để biết chắc UI thật xử lý ra sao khi rỗng) — KHÔNG đoán Expected Result. Nếu tiếp tục không quan sát được khi vibe-test thật, cân nhắc chuyển thành Clarification thay vì giữ ở dạng SC treo.

## Scenarios — CARRIED (reference only)

| Scenario ID | Tên ngắn | Module | Origin Version | Priority | Reference |
|-------------|----------|--------|---------------|----------|-----------|
| _(không có — v1.0 là version đầu tiên)_ | | | | | |

## Scenarios — DEPRECATED

| Scenario ID | Tên ngắn | Module | Deprecated ở | Lý do |
|-------------|----------|--------|-------------|-------|
| _(không có — v1.0 là version đầu tiên)_ | | | | |
