# Test Scenario Map — v1.1

## Tổng quan
- Tổng số scenarios: 51 (NEW: 0, MODIFIED: 13, CARRIED: 38)
- Phân bổ priority: P1: 22 | P2: 18 | P3: 11

## Scenarios — NEW & MODIFIED (chi tiết đầy đủ)

### SENDER

| Scenario ID | Feature | Req ID | DOC Source | Given | When | Then | Priority | Test Type | Lifecycle |
|-------------|---------|--------|-----------|-------|------|------|----------|-----------|-----------|
| SC-SENDER-003 | Wizard bước 1 — validation gate mới | REQ-SENDER-002 | DOC-v1.1-01 §D8.1/D8.3; DOC-v1.1-02 | Sender đang ở wizard bước 1 (Loại hàng "Tài liệu" mặc định, Giá trị hàng chưa chọn) | Bấm "Tiếp theo" mà chưa chọn Giá trị hàng | Hiện lỗi inline đỏ "Vui lòng chọn giá trị hàng" ngay dưới field, KHÔNG chuyển sang bước 2 | P1 | Validation | MODIFIED(v1.1) |
| SC-SENDER-004 | Wizard bước 2 — field Email công ty người nhận | REQ-SENDER-003 | DOC-v1.1-01 §D1b US-D18, §D8.1; DOC-v1.1-02 | Sender đang ở wizard bước 2 | Nhìn vào đầu mục "NGƯỜI NHẬN" | Thấy field "Email công ty người nhận" là field đầu tiên, kèm hint text hướng dẫn tự động điền tên/SĐT/địa chỉ từ hệ thống nội bộ | P1 | UI/Functional | MODIFIED(v1.1) |
| SC-SENDER-009 | Email công ty người nhận → tự điền (field tồn tại, hành vi autofill chưa verify) | REQ-SENDER-003, US-D18 | DOC-v1.1-01 §D1b US-D18; DOC-v1.1-02 | Sender ở wizard bước 2, field Email công ty người nhận đang trống | Nhập 1 email công ty có trong hệ thống nội bộ | Tên/SĐT/địa chỉ tự điền + báo "Đã tìm thấy trong hệ thống nội bộ" (theo Source Quote BRD — CHƯA tự verify qua UI vì không có email demo hợp lệ để test) | P2 | Functional | MODIFIED(v1.1) — UNBLOCK |
| SC-SENDER-010 | Email không có trong hệ thống → báo lỗi nhập thủ công | REQ-SENDER-003, US-D18 | DOC-v1.1-01 §D1b US-D18 | Sender ở wizard bước 2, field Email công ty người nhận đang trống | Nhập 1 email KHÔNG có trong hệ thống nội bộ | Báo "Không tìm thấy · nhập thủ công", cho phép tiếp tục nhập tay 3 field còn lại (theo Source Quote BRD — CHƯA tự verify qua UI) | P2 | Negative | MODIFIED(v1.1) — UNBLOCK |

#### Source Detail per Scenario (verbatim quotes — `references/quoting-guide.md`)

##### SC-SENDER-003 — Wizard bước 1: validation gate mới

**Source Quote #1 (old, v1.0):**
> "Nút "Tiếp theo" — luôn khả dụng kể cả khi chưa chọn loại hàng"

**Source Quote #2 (new, v1.1 — DOC-v1.1-01 §D8.3):**
> "VAL-01: Nút submit vô hiệu hoá đến khi mọi trường bắt buộc hợp lệ + đã tick điều khoản. VAL-02: Lỗi hiện ngay dưới ô nhập khi rời ô (on blur), không dùng popup; cuộn tới ô lỗi đầu tiên khi bấm submit"

**Source Location:** `DOC-v1.1-01 §D8.3 "Quy tắc chung cho form"`, đối chiếu `DOC-v1.0-01 §1.2`

**Analyst Note (diff):** Hành vi đảo ngược hoàn toàn so với v1.0 — trước "luôn khả dụng", nay có gate thật. **Đã verify trực tiếp qua Chrome MCP (DOC-v1.1-02):** bấm "Tiếp theo" khi Giá trị hàng chưa chọn → hiện "Vui lòng chọn giá trị hàng" màu đỏ, không chuyển bước; sau khi chọn 1 giá trị → chuyển bước 2 bình thường. Given/When/Then viết theo hành vi đã verify, độ tin cậy cao.

---

##### SC-SENDER-004 — Wizard bước 2: field Email công ty người nhận

**Source Quote:**
> "Ô "Email công ty người nhận" nằm đầu mục Người nhận; nhập email có trong hệ thống → tự điền tên/SĐT/địa chỉ + báo "Đã tìm thấy trong hệ thống nội bộ"; không có → báo "Không tìm thấy · nhập thủ công""

**Source Location:** `DOC-v1.1-01 §D1b US-D18 Acceptance Criteria`

**Analyst Note:** Field mới hoàn toàn so với 3-field-only của v1.0. Đã verify field TỒN TẠI qua UI (không chỉ theo spec) — placement, hint text khớp đúng BRD. Behavior autofill (khi nhập email hợp lệ/không hợp lệ) tách thành SC-SENDER-009/010 riêng vì cần dữ liệu test cụ thể chưa xác định được trong phiên verify.

---

##### SC-SENDER-009 / SC-SENDER-010 — Email autofill (UNBLOCK)

**Source Quote:** (như trên, US-D18)

**Source Location:** `DOC-v1.1-01 §D1b US-D18`

**Analyst Note:** v1.0 các SC này ở trạng thái 🚫 Blocked vì field hoàn toàn chưa tồn tại trong UI. v1.1 xác nhận field ĐÃ CÓ → chuyển ⏳ Ready. Given/When/Then viết theo Source Quote BRD (chưa tự verify hành vi thật bằng UI vì thiếu dữ liệu email demo hợp lệ) — cần vibe-test bổ sung để xác nhận trước khi coi Expected Result là chắc chắn 100%.

---

### RECEIVER

| Scenario ID | Feature | Req ID | DOC Source | Given | When | Then | Priority | Test Type | Lifecycle |
|-------------|---------|--------|-----------|-------|------|------|----------|-----------|-----------|
| SC-RECEIVER-003 | Xác nhận đã nhận hàng (happy path, không đổi) + SLA nhắc/admin mới | REQ-RECEIVER-002 | DOC-v1.1-01 §D1b US-D14, §D4 BR-CNF-04 | Đơn ở trạng thái "Đã giao" | Receiver bấm "Xác nhận đã nhận hàng" | Đơn chuyển "Hoàn thành", đồng bộ 3 màn tức thời (đã verify, không đổi so với v1.0). Nếu KHÔNG xác nhận trong 2 giờ → hệ thống nhắc; thêm 2 giờ nữa (tổng 4 giờ) → admin hỗ trợ (spec-only, không có timer trong prototype để verify) | P1 | Functional | MODIFIED(v1.1) |

#### Source Detail per Scenario

##### SC-RECEIVER-003 — SLA cụ thể hoá

**Source Quote:**
> "Chỉ xác nhận được sau khi Carrier đã bấm "Đã giao"; quá 2 giờ không xác nhận → hệ thống nhắc, thêm 2 giờ → admin hỗ trợ"

**Source Location:** `DOC-v1.1-01 §D1b US-D14 Acceptance Criteria`, cross-ref `§D4 BR-CNF-04`

**Analyst Note:** Happy path (Then đầu) đã verify trực tiếp qua Chrome MCP end-to-end (posted→matched→in_transit→delivered→completed). Nhánh SLA timeout (Then thứ 2) chỉ ở mức spec — prototype không có cơ chế timer/nhắc tự động để test. generate-tc nên tách 2 TC: 1 happy-path (Ready, ✅) + 1 SLA-timeout (Blocked/spec-only cho tới khi có backend thật).

---

### ORDER

| Scenario ID | Feature | Req ID | DOC Source | Given | When | Then | Priority | Test Type | Lifecycle |
|-------------|---------|--------|-----------|-------|------|------|----------|-----------|-----------|
| SC-ORDER-005 | Nút "Chỉnh sửa" hiện ở "Chờ ghép" | REQ-ORDER-003 | DOC-v1.1-01 §D1b US-D19, §D4 BR-EDIT-01; DOC-v1.1-02 | Đơn ở trạng thái "Chờ ghép", Sender đang xem "Theo dõi đơn" | Cuộn tới cuối màn | Thấy 2 nút "✏️ Chỉnh sửa" và "❌ Huỷ đơn" (đã verify UI tồn tại; CHƯA verify form chỉnh sửa mở ra có điền sẵn dữ liệu cũ hay không) | P2 | Functional | MODIFIED(v1.1) — UNBLOCK (partial) |
| SC-ORDER-006 | Sau "Đã ghép" không cho sửa đơn nữa | REQ-ORDER-003 | DOC-v1.1-01 §D4 BR-EDIT-01 | Đơn đã chuyển "Đã ghép" trở đi | Sender/Carrier xem "Theo dõi đơn" | Nút "Chỉnh sửa" KHÔNG còn hiện (suy luận từ BR-EDIT-01 — CHƯA tự verify trực tiếp bằng cách bấm thử ở trạng thái Đã ghép) | P1 | Negative/Permission | MODIFIED(v1.1) — UNBLOCK (partial) |
| SC-ORDER-007 | Tin quá hạn → EXPIRED (ngưỡng = "Đến ngày", resolved) | REQ-ORDER-004 | DOC-v1.1-01 §D8.1/D8.2; DOC-v1.1-02; C-ORDER-2 resolved | Đơn ở "Chờ ghép", current date đã qua "Đến ngày" mà chưa MATCHED | *(current date > Đến ngày, đơn vẫn `posted`)* | Đơn tự chuyển "EXPIRED", badge "Hết hạn" + text "Không có ai nhận mang giúp trong thời gian đăng — tin đã tự động đóng." (text/badge đã verify UI qua order mẫu có sẵn; ngưỡng "Đến ngày" đã resolve — cơ chế trigger backend/worker vẫn chưa có trong prototype nên vẫn không test được thật) | P2 | State | MODIFIED(v1.1) |

#### Source Detail per Scenario

##### SC-ORDER-005 / SC-ORDER-006 — Chỉnh sửa đơn (UNBLOCK)

**Source Quote:**
> "Chỉ được chỉnh sửa tin khi còn "Chờ ghép" (POSTED); đã MATCHED trở đi khoá chỉnh sửa"

**Source Location:** `DOC-v1.1-01 §D4 BR-EDIT-01`

**Analyst Note:** v1.0 hoàn toàn 🚫 Blocked (nút được cho là chưa có UI). v1.1 verify trực tiếp: nút "✏️ Chỉnh sửa" CÓ tồn tại cạnh "❌ Huỷ đơn" ở trạng thái Chờ ghép. Do phạm vi phiên verify có giới hạn, KHÔNG bấm vào để xem form chỉnh sửa thật, và KHÔNG verify trực tiếp việc nút biến mất sau MATCHED — cả 2 SC chuyển ⏳ Ready nhưng cần vibe-test bổ sung trước khi generate-tc coi Expected Result là chắc chắn.

---

##### SC-ORDER-007 — EXPIRED (ngưỡng "Đến ngày", resolved)

**Source Quote #1 (D8.1, form SENDER):**
> "Đến ngày | ... | Quá ngày này mà chưa ghép → tin tự chuyển trạng thái Hết hạn"

**Source Quote #2 (D8.2, form OFFER):**
> "Đến ngày | ... | Sau ngày này tin tự chuyển trạng thái Hết hạn và ngừng khớp"

**Source Location:** `DOC-v1.1-01 §D8.1` + `§D8.2`

**Analyst Note:** Text/badge "Hết hạn" đã verify UI thật (không đổi so với v1.0). **Resolution (user, 2026-07-28): "Den ngay dung"** — ngưỡng chính thức = "Đến ngày", đảo ngược resolution v1.0 ("Từ ngày"). generate-tc viết TC boundary dựa trên mốc "Đến ngày" (vd current date = Đến ngày → chưa expired; = Đến ngày + 1 → expired) khi có UI/worker thật — vẫn 🚫 Blocked cho TC thật vì cơ chế backend chưa có trong prototype.

---

### GENERAL

| Scenario ID | Feature | Req ID | DOC Source | Given | When | Then | Priority | Test Type | Lifecycle |
|-------------|---------|--------|-----------|-------|------|------|----------|-----------|-----------|
| SC-GENERAL-003 | Trang chủ dashboard — cap 5 tin + "Xem thêm" (áp dụng cả Sender lẫn Carrier, resolved) | REQ-GENERAL-003 | DOC-v1.1-01 §D1b US-D06; DOC-v1.1-02; C-GENERAL-4 resolved | Sender HOẶC Carrier ở Trang chủ, có >5 tin đang chờ ghép trên bảng tin | Xem section "Tin mới" (Carrier: mục chính; Sender: bên dưới "Đơn của tôi") | Cả 2 vai trò đều hiển thị đúng tối đa 5 tin mới nhất; nếu còn tin khác → nút "Xem thêm trên Bảng tin" dẫn sang Bảng tin (đã resolve: tính năng áp dụng chung mọi vai trò, không chỉ Carrier như BRD mô tả; cap-5 CHƯA tự verify số vì demo hiện chỉ có 2 tin mẫu) | P2 | UI/Functional | MODIFIED(v1.1) |
| SC-GENERAL-005 | Nút back (←) điều hướng đúng màn cha + giữ nguyên dữ liệu wizard | REQ-GENERAL-004 | DOC-v1.1-02 (quan sát UI trực tiếp) | Bất kỳ vai trò nào, đang ở 1 màn con có icon back (←) ở header (role-choice, wizard bước 1/2/3, form OFFER, Chi tiết tin, Bảng tin, Theo dõi đơn, Đơn của tôi, Thông báo) | Bấm icon back (←) | Quay về đúng 1 màn cha cố định theo cây điều hướng (không theo lịch sử click); riêng các bước wizard, dữ liệu đã nhập/chọn trước đó vẫn được giữ nguyên khi back rồi quay lại bước đó, không có dialog cảnh báo mất dữ liệu (10 TC — không bao gồm màn "Tặng quà", xem C-GENERAL-5 Open) | P2 | UI/Navigation | NEW(v1.1) |

#### Source Detail per Scenario

##### SC-GENERAL-003 — cap 5, áp dụng cả Sender lẫn Carrier (resolved)

**Source Quote:**
> "Trang chủ hiển thị đúng 5 tin mới nhất; nếu còn tin khác hiện nút "Xem thêm trên Bảng tin" dẫn sang màn Bảng tin"

**Source Location:** `DOC-v1.1-01 §D1b US-D06 Acceptance Criteria`

**Analyst Note:** Rule chỉ mô tả cho Carrier trong text BRD. UI thật cho thấy Sender's Trang chủ CŨNG có section "Tin mới".

**Resolution (user, 2026-07-28):** "viet theo UI luon nha" — tính năng "Tin mới" cap-5 áp dụng cho CẢ Sender lẫn Carrier (không chỉ Carrier như BRD mô tả). generate-tc viết Given/When/Then dùng chung cho 2 vai trò như bảng trên. Chưa đủ dữ liệu demo (chỉ 2 tin mẫu) để tự verify cap-5 hoạt động đúng ở cả 2 vai trò — cần vibe-test bổ sung với data giả lập >5 tin.

---

##### SC-GENERAL-005 — Nút back (←) điều hướng đúng màn cha + giữ dữ liệu (mới, 2026-07-29)

**Source Quote:**
> (quan sát trực tiếp qua Chrome MCP, DOC-v1.1-02, localhost:8767) Xem verbatim đầy đủ tại `02_analyze-requirements/v1.1/MEMORY.md` REQ-GENERAL-004.

**Source Location:** `DOC-v1.1-02` — quan sát UI trực tiếp, không có §section BRD/Figma tương ứng.

**Analyst Note:** 10/11 điểm back-icon đã verify nhất quán (đích luôn là 1 màn cha cố định + không mất dữ liệu wizard). 1 điểm ngoại lệ — màn "Tặng quà" — cho kết quả không nhất quán/không đúng kỳ vọng logic, đã tách thành Clarification riêng (C-GENERAL-5, Open) thay vì gộp chung vào scenario này, để không viết TC với Expected Result chưa xác định chắc chắn.

---

### CANCEL

| Scenario ID | Feature | Req ID | DOC Source | Given | When | Then | Priority | Test Type | Lifecycle |
|-------------|---------|--------|-----------|-------|------|------|----------|-----------|-----------|
| SC-CANCEL-001 | Popup huỷ — validation lý do tối thiểu 5 ký tự (theo BRD, target — UI hiện tại chưa đạt) | REQ-CANCEL-001 | DOC-v1.1-01 §D1b US-D16, §D8.3 VAL-04; DOC-v1.1-02; C-CANCEL-1 resolved | Đơn ở "Chờ ghép", popup "Huỷ đơn hàng" đang mở, ô "Lý do huỷ" đang trống | Nhập lý do <5 ký tự (vd "ab") rồi thử bấm "Xác nhận" | Nút "Xác nhận" PHẢI vẫn khoá (disabled) tới khi đủ 5 ký tự (theo BRD VAL-04 — **⚠️ UI hiện tại KHÔNG đạt**: đã verify trực tiếp "ab" 2 ký tự làm nút enable ngay — TC này dự kiến FAIL trên UI hiện tại, xem chờ dev implement) | P1 | Validation | MODIFIED(v1.1) |

#### Source Detail per Scenario

##### SC-CANCEL-001 — validation lý do tối thiểu 5 ký tự (theo BRD, resolved)

**Source Quote (BRD — target behavior đã resolve):**
> "VAL-04: Huỷ đơn: bắt buộc nhập lý do (tối thiểu 5 ký tự) mới bật nút Xác nhận"

**Source Location:** `DOC-v1.1-01 §D8.3 VAL-04`

**Analyst Note:** Đã test trực tiếp qua Chrome MCP: nhập "ab" (2 ký tự) → nút "Xác nhận" đã enable ngay — xác nhận chắc chắn UI hiện tại chỉ có non-empty gate, KHÔNG có ngưỡng ký tự tối thiểu.

**Resolution (user, 2026-07-28):** "lay theo rule BRD nha" — rule đúng/target = BRD VAL-04 (tối thiểu 5 ký tự). Given/When/Then viết theo target behavior này; UI hiện tại là gap cần dev bổ sung. Khi vibe-test/execute TC này trên UI hiện tại, kết quả FAIL là ĐÚNG như dự kiến (không phải TC sai) — khuyến nghị log-bug tham chiếu C-CANCEL-1 khi tới giai đoạn đó.

---

### GIFT

| Scenario ID | Feature | Req ID | DOC Source | Given | When | Then | Priority | Test Type | Lifecycle |
|-------------|---------|--------|-----------|-------|------|------|----------|-----------|-----------|
| SC-GIFT-002 | Chọn quà → Xác nhận → popup cảm ơn (full verify) | REQ-GIFT-002 | DOC-v1.1-01 §D1b US-D15; DOC-v1.1-02 | Đơn ở trạng thái "Hoàn thành", Sender đang ở màn "Tặng quà" | Chọn 1 trong 4 loại quà rồi bấm "Xác nhận tặng quà" | Hiện popup "Đã gửi lời cảm ơn!" kèm text "Món quà và lời cảm ơn của bạn đã được gửi đến người vận chuyển." + nút "Về trang chủ" (đã verify full flow tới cùng, khác nhẹ text so với BRD) | P2 | Functional | MODIFIED(v1.1) |
| SC-GIFT-003 | Carrier nhận thông báo + xem "Quà đã nhận" (role đã đúng) | REQ-GIFT-003 | DOC-v1.1-01 §D1b US-D20; DOC-v1.1-02; DOC-v1.1-03 | Sender vừa tặng quà thành công cho Carrier | Carrier mở tab "Cá nhân" | Thấy mục "Quà đã nhận" đúng ở Cá nhân của Carrier (KHÔNG còn là bug ở Receiver như v1.0) | P3 | Functional | MODIFIED(v1.1) — C-GIFT-2 RESOLVED |
| SC-GIFT-004 | Xem lịch sử "Quà đã nhận" (role đã đúng) | REQ-GIFT-004 | DOC-v1.1-02 | Carrier ở tab "Cá nhân" | Tap mục "Quà đã nhận" | Hiện "Tổng quà đã nhận: N món" + breakdown 4 loại + "LỊCH SỬ NHẬN QUÀ" theo thời gian giảm dần | P3 | UI/Functional | MODIFIED(v1.1) — C-GIFT-2 RESOLVED |

#### Source Detail per Scenario

##### SC-GIFT-002 — full verify

**Source Quote:**
> "chọn quà → gửi ngay không cần bước xác nhận → popup "Cảm ơn của bạn đã được gửi" → nút "Về trang chủ""

**Source Location:** `DOC-v1.1-01 §D1b US-D15 Acceptance Criteria`

**Analyst Note:** v1.0 dừng lại trước bước xác nhận cuối để giữ nguyên state demo — v1.1 chạy tới cùng lần đầu. Xác nhận discrepancy "có bước xác nhận" (đã ghi từ v1.0) vẫn giữ nguyên, KHÔNG đổi. Text popup cuối verify được, khác nhẹ so với BRD quote — cập nhật Then theo UI thật.

---

##### SC-GIFT-003 / SC-GIFT-004 — role đã đúng (C-GIFT-2 RESOLVED)

**Source Quote:**
> "Carrier nhận thông báo "Bạn nhận được một món quà cảm ơn" → mở Trang cá nhân... màn Quà đã nhận hiển thị 1 card đếm số... + danh sách lịch sử nhận quà"

**Source Location:** `DOC-v1.1-01 §D1b US-D20 Acceptance Criteria`

**Analyst Note:** v1.0 quan sát nhầm màn này ở Receiver — nghi bug, dẫn chứng bằng note Figma (nhánh NGƯỜI GIAO). v1.1 verify lại: bug đã sửa, UI + Figma re-check đều khớp Carrier. Precondition trong bảng trên đổi từ "Receiver" (case nghi bug ở v1.0) sang "Carrier" (đúng theo spec, đã verify).

---

## Scenarios — CARRIED (reference only)

| Scenario ID | Tên ngắn | Module | Origin Version | Priority | Reference |
|-------------|----------|--------|---------------|----------|-----------|
| SC-SENDER-001 | Màn chọn vai trò hiển thị đủ 2 lựa chọn | SENDER | v1.0 | P2 | `02_analyze-requirements/v1.0/test_scenario_map.md` |
| SC-SENDER-002 | Chọn "Tôi cần gửi hàng" mở wizard bước 1 | SENDER | v1.0 | P1 | `02_analyze-requirements/v1.0/test_scenario_map.md` |
| SC-SENDER-005 | Chưa tick điều khoản → nút "Đăng tin ngay" không khả dụng | SENDER | v1.0 | P1 | `02_analyze-requirements/v1.0/test_scenario_map.md` |
| SC-SENDER-006 | Tick điều khoản + đăng tin → thành công | SENDER | v1.0 | P1 | `02_analyze-requirements/v1.0/test_scenario_map.md` |
| SC-SENDER-007 | UI smoke bước 3 — đủ block tóm tắt + cảnh báo + điều khoản | SENDER | v1.0 | P2 | `02_analyze-requirements/v1.0/test_scenario_map.md` |
| SC-SENDER-008 | Theo dõi đơn hiển thị timeline, mốc "Chờ ghép" active | SENDER | v1.0 | P1 | `02_analyze-requirements/v1.0/test_scenario_map.md` |
| SC-CARRIER-001 | UI smoke màn Chi tiết tin | CARRIER | v1.0 | P2 | `02_analyze-requirements/v1.0/test_scenario_map.md` |
| SC-CARRIER-002 | Nhận đơn thành công (posted → matched) | CARRIER | v1.0 | P1 | `02_analyze-requirements/v1.0/test_scenario_map.md` |
| SC-CARRIER-003 | Bấm "Huỷ" ở dialog xác nhận → không đổi trạng thái | CARRIER | v1.0 | P2 | `02_analyze-requirements/v1.0/test_scenario_map.md` |
| SC-CARRIER-004 | Lấy hàng thành công (matched → in_transit) | CARRIER | v1.0 | P1 | `02_analyze-requirements/v1.0/test_scenario_map.md` |
| SC-CARRIER-005 | Giao hàng thành công (in_transit → delivered) | CARRIER | v1.0 | P1 | `02_analyze-requirements/v1.0/test_scenario_map.md` |
| SC-CARRIER-006 | Carrier KHÔNG có nút tự hoàn tất đơn | CARRIER | v1.0 | P1 | `02_analyze-requirements/v1.0/test_scenario_map.md` |
| SC-CARRIER-007 | Carrier tự động thấy "Hoàn thành" khi Receiver xác nhận | CARRIER | v1.0 | P1 | `02_analyze-requirements/v1.0/test_scenario_map.md` |
| SC-CARRIER-008 | Tag "Tin của bạn" đúng phạm vi | CARRIER | v1.0 | P2 | `02_analyze-requirements/v1.0/test_scenario_map.md` |
| SC-CARRIER-009 | Ảnh sản phẩm — case không có ảnh (chưa xác định) | CARRIER | v1.0 | P3 | `02_analyze-requirements/v1.0/test_scenario_map.md` |
| SC-RECEIVER-001 | Block "Người giao hàng" ẩn khi đơn chưa ghép | RECEIVER | v1.0 | P2 | `02_analyze-requirements/v1.0/test_scenario_map.md` |
| SC-RECEIVER-002 | Block "Người giao hàng" hiện đúng dữ liệu sau khi ghép | RECEIVER | v1.0 | P1 | `02_analyze-requirements/v1.0/test_scenario_map.md` |
| SC-RECEIVER-004 | CTA không hiện khi đơn chưa "Đã giao" | RECEIVER | v1.0 | P1 | `02_analyze-requirements/v1.0/test_scenario_map.md` |
| SC-ORDER-001 | Badge trạng thái đúng label + màu | ORDER | v1.0 | P2 | `02_analyze-requirements/v1.0/test_scenario_map.md` |
| SC-ORDER-002 | "↺ Chạy lại từ đầu" reset order status | ORDER | v1.0 | P1 | `02_analyze-requirements/v1.0/test_scenario_map.md` |
| SC-ORDER-003 | Đồng bộ trạng thái tức thời cả 3 màn | ORDER | v1.0 | P1 | `02_analyze-requirements/v1.0/test_scenario_map.md` |
| SC-ORDER-004 | Mọi transition đều có dialog xác nhận trung gian | ORDER | v1.0 | P2 | `02_analyze-requirements/v1.0/test_scenario_map.md` |
| SC-GENERAL-001 | Banner "không thu phí/không chat/không thanh toán" | GENERAL | v1.0 | P3 | `02_analyze-requirements/v1.0/test_scenario_map.md` |
| SC-GENERAL-002 | Bottom nav điều hướng đúng màn | GENERAL | v1.0 | P2 | `02_analyze-requirements/v1.0/test_scenario_map.md` |
| SC-GENERAL-004 | Empty state "Đơn của tôi"/"Tin mới" (chưa xác định) | GENERAL | v1.0 | P3 | `02_analyze-requirements/v1.0/test_scenario_map.md` |
| SC-OFFER-001 | Carrier đăng tin OFFER thành công | OFFER | v1.0 | P2 | `02_analyze-requirements/v1.0/test_scenario_map.md` |
| SC-OFFER-002 | Màn "Đã ghi nhận tuyến đường" | OFFER | v1.0 | P2 | `02_analyze-requirements/v1.0/test_scenario_map.md` |
| SC-OFFER-003 | Thông báo khi tin NEED khớp tuyến | OFFER | v1.0 | P2 | `02_analyze-requirements/v1.0/test_scenario_map.md` |
| SC-OFFER-004 | "Nhận giao" từ thông báo → MATCHED | OFFER | v1.0 | P1 | `02_analyze-requirements/v1.0/test_scenario_map.md` |
| SC-CANCEL-002 | Huỷ đơn thành công kèm lý do | CANCEL | v1.0 | P1 | `02_analyze-requirements/v1.0/test_scenario_map.md` |
| SC-CANCEL-003 | KHÔNG ai huỷ được khi "Đang giao" | CANCEL | v1.0 | P1 | `02_analyze-requirements/v1.0/test_scenario_map.md` |
| SC-CANCEL-004 | Carrier huỷ khi đã ghép → trả về "Chờ ghép" | CANCEL | v1.0 | P1 | `02_analyze-requirements/v1.0/test_scenario_map.md` |
| SC-GIFT-001 | Màn "Tặng quà" hiển thị đủ 4 loại quà | GIFT | v1.0 | P3 | `02_analyze-requirements/v1.0/test_scenario_map.md` |
| SC-NOTIFICATION-001 | 9 sự kiện thông báo đúng nội dung | NOTIFICATION | v1.0 | P3 | `02_analyze-requirements/v1.0/test_scenario_map.md` |
| SC-NOTIFICATION-002 | "Đánh dấu đã đọc" hết red-dot | NOTIFICATION | v1.0 | P3 | `02_analyze-requirements/v1.0/test_scenario_map.md` |
| SC-ADMIN-001 | Admin override permission | ADMIN | v1.0 | P3 | `02_analyze-requirements/v1.0/test_scenario_map.md` |
| SC-MEDIA-001 | Chụp ảnh hàng lúc nhận | MEDIA | v1.0 | P3 | `02_analyze-requirements/v1.0/test_scenario_map.md` |
| SC-MEDIA-002 | Chia sẻ vị trí GPS khi đang giao | MEDIA | v1.0 | P3 | `02_analyze-requirements/v1.0/test_scenario_map.md` |

## Scenarios — DEPRECATED

| Scenario ID | Tên ngắn | Module | Deprecated ở | Lý do |
|-------------|----------|--------|-------------|-------|
| _(không có)_ | | | | |
