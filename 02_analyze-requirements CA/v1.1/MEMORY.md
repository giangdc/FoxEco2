# MEMORY — Analyze Requirements Output — v1.1

> Tạo bởi: skill analyze-requirements (mode DELTA)
> Cập nhật lần cuối: 2026-07-28 (lần 5) — user đính chính 2 điểm: (1) chỉ "Tên người gửi" là chỉ đọc (không phải cả 3 field NGƯỜI GỬI — SĐT/Địa chỉ vẫn sửa được theo đúng BRD); (2) Bảng tin state rỗng VẪN generate TC, chỉ để trống cột Expected Result cho user tự điền sau. Sẵn sàng chạy generate-tc mode comprehensive cho 3 sheet Trang chủ/Bảng tin/Đăng tin.
> Cập nhật lần cuối (lần 4): 2026-07-28 — user resolve 2 điểm còn treo ở §6.2 (bản đầu, đã đính chính ở lần 5).
> Cập nhật lần cuối (lần 3): 2026-07-28 — bổ sung §6.2 UI Block Map cho 3 sheet Trang chủ/Bảng tin/Đăng tin (theo yêu cầu user, chuẩn bị generate-tc mode comprehensive chia sheet theo bottom-nav).
> Cập nhật lần cuối (lần 2): 2026-07-28 — user resolve toàn bộ 4 clarification mới của v1.1 (C-ORDER-2 re-opened, C-SENDER-3, C-CANCEL-1, C-GENERAL-4). Xem §6.
> Cập nhật lần cuối (lần 1): 2026-07-28 — delta từ v1.0, nguồn thay thế hoàn toàn: BRD v3.2 + Design v3.2 (prototype cập nhật) + Figma board gốc (re-verify). User yêu cầu KHÔNG dùng nội dung 3 DOC v1.0 cũ (Flow-Spec, BRD v3.1, Design prototype cũ) làm source quote — chỉ dùng danh sách REQ/SC v1.0 làm baseline lifecycle so sánh.
> Parent version: v1.0

## 0. Version Context
- **Version:** v1.1
- **Parent:** v1.0
- **Delta type:** Major (thay thế toàn bộ nguồn tài liệu + BRD bổ sung khối lượng lớn validation rule cụ thể D8 + phát hiện 1 xung đột với clarification đã resolve ở v1.0)
- **Input folder:** 00_input/v1.1/
- **Shared docs applied:** Không
- **Analysis mode:** DELTA

## 1. Project Overview
- **Dự án:** FoxEco — nền tảng kết nối 3 vai trò (Người gửi / Người vận chuyển / Người nhận) để nhờ nhau mang hộ đồ tiện đường, phần "Gửi hàng" (Delivery) của mạng xã hội tương trợ nội bộ FPT Telecom.
- **Mô tả:** Bản demo hiện tại là 1 file HTML standalone (bundler format) mô phỏng 3 vai trò trên cùng 1 app, đồng bộ trạng thái tức thời qua client-side store (`window.FoxEcoStore`). Chưa có backend/multi-order thật — verify trực tiếp qua Chrome MCP (serve local qua `python3 -m http.server`, vì bundler yêu cầu origin http/https, không chạy được qua `file://`).
- **Môi trường:** DEMO — URL gốc: http://localhost:8765/ (v1.0); v1.1 verify qua http://localhost:8767/ (local serve riêng cho `00_input/v1.1/`).

## 2. Document Registry (version-scoped)
| DOC ID | File | Loại | Ngày phân tích | Status | Modules liên quan |
|--------|------|------|---------------|--------|-------------------|
| DOC-v1.1-01 | `00_input/v1.1/DOC-v1.1-01-FoxEco-BRD-v3.2.html` | HTML (bundler format) — BRD v3.2, bản thay thế BRD v3.1 (FPT Telecom, cập nhật 27/07/2026) | 2026-07-28 | Analyzed (text extract qua embedded `__bundler/template` script tag) — nguồn chính thức cho business rule | SENDER, CARRIER, RECEIVER, OFFER, CANCEL, GIFT, NOTIFICATION, ORDER, ADMIN, MEDIA, GENERAL |
| DOC-v1.1-02 | `00_input/v1.1/DOC-v1.1-02-FoxEco-Design-v3.2.html` | HTML (bundler format) — Design/prototype v3.2, bản thay thế Design prototype cũ | 2026-07-28 | Analyzed — verify trực tiếp qua Chrome MCP (đăng tin, order lifecycle đầy đủ posted→completed, gift flow, cancel flow, profile tab) — **nguồn chính thức cho UI thật đã dựng** | SENDER, CARRIER, RECEIVER, ORDER, GIFT, GENERAL |
| DOC-v1.1-03 | Figma board "Fox Eco Doc" — `https://www.figma.com/board/SEu9ekmu2wh1XxZCJkqAbP/Fox-Eco-Doc?node-id=23-153` | FigJam board — pulled qua Figma MCP `get_figjam` | 2026-07-28 | Analyzed — dùng để re-verify design intent (đặc biệt vị trí màn "Quà đã nhận" — xem C-GIFT-2), không đổi so với lần đọc ở v1.0 | GIFT, CANCEL, OFFER, ORDER |

## 3. Module Summary
| Module | DOC Source | Tổng Req | Tổng SC | NEW | MODIFIED | CARRIED | DEPRECATED | P1 | P2 | P3 | Risk Level |
|--------|-----------|----------|---------|-----|----------|---------|-----------|----|----|----|-----------:|
| SENDER | DOC-v1.1-01, DOC-v1.1-02 | 6 | 10 | 0 | 4 | 6 | 0 | 6 | 4 | 0 | High |
| CARRIER | DOC-v1.1-01, DOC-v1.1-02 | 6 | 9 | 0 | 0 | 9 | 0 | 5 | 3 | 1 | High |
| RECEIVER | DOC-v1.1-01, DOC-v1.1-02 | 2 | 4 | 0 | 1 | 3 | 0 | 3 | 1 | 0 | High |
| ORDER | DOC-v1.1-01, DOC-v1.1-02 | 4 | 7 | 0 | 3 | 4 | 0 | 3 | 4 | 0 | High |
| GENERAL | DOC-v1.1-01, DOC-v1.1-02 | 4 | 5 | 1 | 1 | 3 | 0 | 0 | 3 | 2 | Medium |
| OFFER | DOC-v1.1-01, DOC-v1.1-03 | 4 | 4 | 0 | 0 | 4 | 0 | 1 | 3 | 0 | Medium |
| CANCEL | DOC-v1.1-01, DOC-v1.1-02, DOC-v1.1-03 | 4 | 4 | 0 | 1 | 3 | 0 | 4 | 0 | 0 | High |
| GIFT | DOC-v1.1-01, DOC-v1.1-02, DOC-v1.1-03 | 4 | 4 | 0 | 3 | 1 | 0 | 0 | 1 | 3 | Low |
| NOTIFICATION | DOC-v1.1-01, DOC-v1.1-02 | 2 | 2 | 0 | 0 | 2 | 0 | 0 | 0 | 2 | Low |
| ADMIN | DOC-v1.1-01 | 1 | 1 | 0 | 0 | 1 | 0 | 0 | 0 | 1 | Low |
| MEDIA | DOC-v1.1-01 | 2 | 2 | 0 | 0 | 2 | 0 | 0 | 0 | 2 | Low |
| **Tổng** | | **39** | **52** | **1** | **13** | **38** | **0** | **22** | **19** | **11** | |

> **Không có REQ/SC mới hoàn toàn** — BRD v3.2 không mở module nghiệp vụ mới so với v1.0 (vẫn là file "01 Gửi Hàng"), mà bổ sung khối lượng lớn **validation rule cụ thể (§D8 — 3 bảng field-level mới)** cho các field đã có, cùng vài refinement UI đã verify được (email autofill, SLA xác nhận, role gift-history). 13 SC được nâng cấp từ CARRIED → MODIFIED vì có thông tin mới đủ ảnh hưởng TC (validation cụ thể, UI unblock, hoặc phát hiện discrepancy). Không có SC nào bị DEPRECATED.
>
> **✅ 4/4 clarification mới của v1.1 đã RESOLVED (user, 2026-07-28, lần 2):**
> 1. **C-ORDER-2 (re-opened → Resolved, đảo ngược resolution v1.0):** ngưỡng "Hết hạn" (EXPIRED) = mốc **"Đến ngày"** (không phải "Từ ngày" như v1.0 từng chốt — BRD v3.2 đúng, resolution v1.0 nay lỗi thời).
> 2. **C-SENDER-3 → Resolved:** giữ nguyên **8 loại hàng như UI hiện tại** (không rút xuống 5 theo BRD D8.1 — coi BRD là chưa cập nhật). **"Thuốc/Y tế" KHÔNG phải hàng cấm** — đóng luôn nghi vấn contradiction P1 kế thừa từ v1.0 (banner "cấm gửi thuốc" không áp dụng cho category "Thuốc/Y tế" trong chip).
> 3. **C-CANCEL-1 → Resolved:** lấy theo rule BRD — **lý do huỷ tối thiểu 5 ký tự** là behavior ĐÚNG/mục tiêu; UI hiện tại (chỉ chặn rỗng) là gap cần dev bổ sung, không phải BRD sai.
> 4. **C-GENERAL-4 → Resolved:** viết TC theo UI thật — section "Tin mới" trên Trang chủ áp dụng cho **cả Sender lẫn Carrier** (không chỉ riêng Carrier như BRD US-D06 mô tả).
>
> **+1 REQ/SC mới (2026-07-29) — live-verify nút back (←):** User yêu cầu kiểm tra xem đã có TC cho icon back ở từng màn hình chưa. Phát hiện CHƯA có → live-verify trực tiếp qua Chrome MCP (localhost:8767, DOC-v1.1-02) hành vi back icon trên toàn bộ màn hình có header với icon back, rồi generate TC ngay. Thêm **REQ-GENERAL-004** (Back icon navigation) + **SC-GENERAL-005**. Phát hiện đồng thời 1 **inconsistency chưa xác định** ở màn "Tặng quà" — xem C-GENERAL-5 (Open).

## 4. Scenario Index
> CARRIED scenarios (38) không liệt kê lại Given/When/Then — xem `02_analyze-requirements/v1.0/test_scenario_map.md`. Chỉ 13 MODIFIED liệt kê đầy đủ bên dưới, roll-up CARRIED ở cuối bảng.

| SC ID | Tên ngắn | Module | DOC Source | Priority | Test Type | Lifecycle | TC Status | Vibe Status | Vibe Date |
|-------|----------|--------|-----------|----------|-----------|-----------|-----------|-------------|-----------|
| SC-SENDER-003 | Điền wizard bước 1 → chuyển bước 2 (validation gate mới; 8 loại hàng xác nhận đúng, Thuốc/Y tế KHÔNG phải hàng cấm) | SENDER | DOC-v1.1-01 §D8.1; DOC-v1.1-02 (verify UI); C-SENDER-3 resolved | P1 | Functional/Validation | MODIFIED(v1.1) | ✅ (cần regenerate TC) | ✅ | 2026-07-28 |
| SC-SENDER-004 | Điền wizard bước 2 → chuyển bước 3 (email autofill + boundary mới) | SENDER | DOC-v1.1-01 §D1b US-D18, §D8.1; DOC-v1.1-02 (verify UI) | P1 | Functional | MODIFIED(v1.1) | ✅ (cần regenerate TC) | ✅ | 2026-07-28 |
| SC-SENDER-009 | Email công ty người nhận → tự điền tên/SĐT/địa chỉ | SENDER | DOC-v1.1-01 §D1b US-D18; DOC-v1.1-02 (UI confirm field tồn tại) | P2 | Functional | MODIFIED(v1.1) — **UNBLOCK** | ⏳ Ready (field tồn tại, chưa verify autofill thật vì không có email demo hợp lệ để test) | ⏳ | — |
| SC-SENDER-010 | Email không có trong hệ thống → báo lỗi nhập thủ công | SENDER | DOC-v1.1-01 §D1b US-D18 | P2 | Negative | MODIFIED(v1.1) — **UNBLOCK** | ⏳ Ready (field tồn tại, chưa verify message thật) | ⏳ | — |
| SC-RECEIVER-003 | Xác nhận đã nhận hàng (SLA nhắc/admin cụ thể hoá) | RECEIVER | DOC-v1.1-01 §D1b US-D14, §D4 BR-CNF-04 | P1 | Functional | MODIFIED(v1.1) | ✅ (cần regenerate TC — thêm case SLA) | ✅ (happy path) / ⏳ (SLA timeout case) | 2026-07-28 |
| SC-ORDER-005 | Nút "Chỉnh sửa" hiện ở "Chờ ghép" | ORDER | DOC-v1.1-01 §D1b US-D19, §D4 BR-EDIT-01, §D7 OPR-10; DOC-v1.1-02 (UI confirm) | P2 | Functional | MODIFIED(v1.1) — **UNBLOCK (confirmed)** | ✅ (6 TC, xem TC-FLOW-022..027) | ✅ | 2026-07-29 |
| SC-ORDER-006 | Sau "Đã ghép" không cho sửa đơn nữa | ORDER | DOC-v1.1-01 §D4 BR-EDIT-01, §D7 OPR-10 | P1 | Negative/Permission | MODIFIED(v1.1) — **UNBLOCK (confirmed)** | ✅ (TC-FLOW-028, verify trực tiếp nút biến mất sau Đã ghép) | ✅ | 2026-07-29 |
| SC-ORDER-007 | Tin quá hạn → EXPIRED, badge "Hết hạn" (ngưỡng = "Đến ngày", đã resolve) | ORDER | DOC-v1.1-01 §D1b US-D04, §D8.1/D8.2; DOC-v1.1-02 (badge UI confirm); C-ORDER-2 resolved (Đến ngày) | P2 | State | MODIFIED(v1.1) | 🚫 Blocked (badge có UI, ngưỡng đã chốt = "Đến ngày", nhưng cơ chế trigger backend/worker chưa có trong prototype — vẫn chưa test được thật) | ⏳ | — |
| SC-GENERAL-003 | Trang chủ dashboard (cap 5 tin + Xem thêm; áp dụng cho cả Sender lẫn Carrier — đã resolve) | GENERAL | DOC-v1.1-01 §D1b US-D06; DOC-v1.1-02 (verify UI); C-GENERAL-4 resolved | P2 | UI/Functional | MODIFIED(v1.1) | ✅ (cần regenerate TC — viết 2 case: Carrier + Sender) | ✅ | 2026-07-28 |
| SC-GENERAL-005 | Nút back (←) ở mỗi màn hình điều hướng đúng về màn cha + không mất dữ liệu wizard đang nhập | GENERAL | DOC-v1.1-02 (quan sát UI trực tiếp) | P2 | UI/Navigation | NEW(v1.1) | ✅ (10 TC, xem §9) | ✅ | 2026-07-29 |
| SC-GENERAL-002 | Bottom nav 5 icon điều hướng đúng màn hình tương ứng | GENERAL | DOC-v1.0-03, DOC-v1.1-02 (quan sát UI) | P2 | UI/Navigation | CARRIED | ✅ (2026-07-29: track từ v1.0 nhưng CHƯA từng có TC thật — bổ sung TC-TRANGCHU-006, live-verify đủ 5 icon) | ✅ | 2026-07-29 |
| SC-CANCEL-001 | Popup huỷ khoá nút "Xác nhận" tới khi nhập lý do (Expected theo BRD: tối thiểu 5 ký tự — target behavior, UI hiện tại chưa đạt) | CANCEL | DOC-v1.1-01 §D1b US-D16, §D8.3 VAL-04; DOC-v1.1-02 (verify UI); C-CANCEL-1 resolved (theo BRD) | P1 | Validation | MODIFIED(v1.1) | ⚠️ Ready — Expected Result viết theo BRD VAL-04 (tối thiểu 5 ký tự) làm target; TC nên FAIL trên UI hiện tại (chỉ chặn rỗng) → khuyến nghị log-bug khi tới giai đoạn đó | ✅ | 2026-07-28 |
| SC-GIFT-002 | Chọn quà → Xác nhận tặng quà → popup cảm ơn | GIFT | DOC-v1.1-01 §D1b US-D15; DOC-v1.1-02 (verify UI đầy đủ lần đầu, kể cả popup cuối) | P2 | Functional | MODIFIED(v1.1) | ✅ (cần regenerate TC — bổ sung text popup thật) | ✅ | 2026-07-28 |
| SC-GIFT-003 | Người nhận quà thấy thông báo + màn "Quà đã nhận" | GIFT | DOC-v1.1-01 §D1b US-D20; DOC-v1.1-02 (verify vai trò đúng); DOC-v1.1-03 (Figma re-confirm) | P3 | Functional | MODIFIED(v1.1) — **C-GIFT-2 RESOLVED** | ✅ (cần regenerate TC — precondition đổi sang Carrier's Cá nhân, KHÔNG còn là bug) | ✅ | 2026-07-28 |
| SC-GIFT-004 | Xem lịch sử "Quà đã nhận" | GIFT | DOC-v1.1-02 (verify UI, đúng vai trò Carrier) | P3 | UI/Functional | MODIFIED(v1.1) — **C-GIFT-2 RESOLVED** | ✅ (cần regenerate TC — precondition đổi) | ✅ | 2026-07-28 |

**CARRIED (38 — không đổi, xem `02_analyze-requirements/v1.0/test_scenario_map.md`):** SC-SENDER-001/002/005/006/007/008, SC-CARRIER-001..009, SC-RECEIVER-001/002/004, SC-ORDER-001/002/003/004, SC-GENERAL-001/002/004, SC-OFFER-001..004, SC-CANCEL-002/003/004, SC-GIFT-001, SC-NOTIFICATION-001/002, SC-ADMIN-001, SC-MEDIA-001/002.

> **TC Status ✅ cần regenerate:** các SC MODIFIED có TC cũ trong TC-MASTER-v1.0.xlsx dựa trên hành vi v1.0 — TC steps/expected cần cập nhật theo Source Detail mới bên dưới trước khi coi là hợp lệ cho v1.1. Xem cảnh báo downstream ở cuối file.

### 4.1. Source Detail (verbatim quotes — mandatory per `references/quoting-guide.md`)

#### REQ-SENDER-002 — Form bước 1: chi tiết hàng (MODIFIED)

**Source Quote (old, v1.0 — DOC-v1.0-01 §1.2):**
> "Loại hàng (chip chọn 1): Tài liệu / Đồ điện tử / Thực phẩm / Hàng nhỏ / Đồ dễ vỡ / Quần áo / Thuốc·Y tế / Khác ... Nút "Tiếp theo" — luôn khả dụng kể cả khi chưa chọn loại hàng"

**Source Quote (new, v1.1 — DOC-v1.1-01 §D8.1):**
> "Loại hàng | Có | Tài liệu | Chọn 1 trong danh mục: Tài liệu · Đồ điện tử · Thực phẩm · Quà tặng · Khác. Không cho để trống
> Ghi chú | Không | Trống | Tối đa 300 ký tự...
> Giá trị hàng | Có | Trống (chưa chọn) | Chọn 1: Giá trị thấp / vừa / cao. Chọn Giá trị cao → hiện cảnh báo trách nhiệm tự thoả thuận
> Ảnh sản phẩm | Không | Trống | Chỉ 1 ảnh duy nhất, ≤ 5MB, định dạng JPG/PNG..."
>
> `§D8.3` VAL-01: "Nút submit vô hiệu hoá đến khi mọi trường bắt buộc hợp lệ + đã tick điều khoản." VAL-02: "Lỗi hiện ngay dưới ô nhập khi rời ô (on blur), không dùng popup."

**Source Location:** `DOC-v1.1-01 §D8.1 "Đơn cần gửi hàng" · table` + `§D8.3 "Quy tắc chung cho form"`, đối chiếu `DOC-v1.0-01 §1.2`

**Analyst Note (diff):** 3 thay đổi lớn so với v1.0:
1. **Danh mục Loại hàng thu gọn 8→5** (bỏ Hàng nhỏ/Đồ dễ vỡ/Quần áo/**Thuốc·Y tế**, thêm Quà tặng) — việc bỏ "Thuốc·Y tế" khỏi danh mục có thể là cách BRD sửa chính contradiction candidate mà comprehensive generate-tc v1.0 từng flag (TC-SENDER-EP07: chip cho chọn "Thuốc/Y tế" trong khi banner cấm gửi thuốc).
2. **Validation gate mới:** trước đây "Tiếp theo" luôn khả dụng bất kể trạng thái field; nay VAL-01/VAL-02 yêu cầu disable tới khi hợp lệ + hiện lỗi inline.
3. **Boundary cụ thể mới:** Ghi chú ≤300 ký tự, Ảnh ≤5MB JPG/PNG 1 ảnh duy nhất — trước đây "chưa xác định" trong test_data_catalog v1.0.

**UI Confirmation (2026-07-28, DOC-v1.1-02, verify qua Chrome MCP):** Mở wizard bước 1 (Sender) — chip Loại hàng **VẪN hiện đủ 8 lựa chọn cũ** (Tài liệu/Đồ điện tử/Thực phẩm/Hàng nhỏ/Đồ dễ vỡ/Quần áo/**Thuốc/Y tế**/Khác, "Tài liệu" pre-selected mặc định) — **KHÔNG khớp danh mục 5 mục mới của BRD** → xem Clarification C-SENDER-3. Validation gate **CÓ hoạt động đúng như VAL-01/02**: bấm "Tiếp theo" khi chưa chọn Giá trị hàng → hiện lỗi inline đỏ "Vui lòng chọn giá trị hàng" ngay dưới field, nút không chuyển bước — đây là hành vi MỚI so với v1.0 (trước đây luôn khả dụng). Chưa verify trực tiếp boundary Ghi chú 300 ký tự và Ảnh 5MB (không thao tác nhập/upload thật trong phiên verify này).

**Resolution (user, 2026-07-28):** "van 8 loai hang nhu UI nha, thuoc/y te khong phai hang cam" — **C-SENDER-3 RESOLVED:** giữ nguyên 8 category như UI hiện tại (danh sách 5-mục của BRD D8.1 coi là chưa cập nhật, KHÔNG áp dụng). **"Thuốc/Y tế" xác nhận KHÔNG phải hàng cấm** — đóng luôn nghi vấn P1 contradiction kế thừa từ v1.0 (banner "không được gửi: thuốc..." không áp dụng cho category chip này, có thể banner chỉ nói tới thuốc kê đơn/chất cấm cụ thể chứ không cấm toàn bộ nhóm "Thuốc/Y tế"). generate-tc: viết TC EP cho đủ 8 category theo UI thật, KHÔNG cần giữ P1 risk-flag cho case "Thuốc/Y tế" nữa — hạ xuống EP bình thường.

---

#### REQ-SENDER-003 — Form bước 2: người gửi/người nhận/lịch (MODIFIED)

**Source Quote (old, v1.0 — DOC-v1.0-01 §1.3):**
> "Người nhận: tên, SĐT, địa chỉ giao hàng — nhập tay, 3 field text."

**Source Quote (new, v1.1 — DOC-v1.1-01 §D8.1):**
> "Email công ty người nhận | Có | Trống | Đúng định dạng email & thuộc tên miền nội bộ. Tra danh bạ: tìm thấy → tự điền tên/SĐT/địa chỉ; không thấy → cảnh báo & cho nhập thủ công
> Tên người nhận | Có | Tự điền từ danh bạ | Không để trống, 2–60 ký tự
> Số điện thoại | Có | Tự điền từ danh bạ | Số điện thoại VN hợp lệ (10 số, đầu 0). Chỉ lộ cho bên còn lại sau khi ghép
> Địa chỉ giao hàng | Có | Trống — tự điền theo địa chỉ người nhận khi tra được email nội bộ | Không để trống; phải khác địa chỉ lấy hàng
> Khung giờ (từ – đến) | Có | 17:00 – 18:30 | đến > từ ; khoảng tối thiểu 30 phút"
>
> `§D8.3` VAL-03: "Tự cắt khoảng trắng đầu/cuối; chuẩn hoá SĐT (bỏ khoảng trắng, dấu chấm) trước khi lưu."

**Source Location:** `DOC-v1.1-01 §D1b US-D18`, `§D8.1 table`, `§D8.3 VAL-03`

**Analyst Note (diff):** Field "Email công ty người nhận" hoàn toàn mới so với 3-field text cũ của v1.0 (đã có REQ-SENDER-006/US-D18 ghi nhận từ trước nhưng UI v1.0 CHƯA có — xem SC-SENDER-009/010 UNBLOCK bên dưới). Boundary mới: tên 2-60 ký tự, SĐT format 10 số đầu 0, địa chỉ phải khác địa chỉ lấy hàng, khung giờ tối thiểu 30 phút — tất cả đều là "chưa xác định" trong test_data_catalog v1.0, nay đã có con số cụ thể. VAL-03 (auto-trim, chuẩn hoá SĐT) resolves câu hỏi whitespace/trim từng đặt ra ở B6 Error Guessing v1.0.

**UI Confirmation (2026-07-28, DOC-v1.1-02):** Wizard bước 2 hiện đúng field "Email công ty người nhận" ở đầu mục NGƯỜI NHẬN, kèm hint text "Nhập email công ty để tự động điền tên, SĐT và địa chỉ từ hệ thống nội bộ." — field này **KHÔNG tồn tại trong bản v1.0**. Không có email demo hợp lệ để test autofill/not-found message thật trong phiên này — hành vi autofill/error message vẫn dựa theo Source Quote BRD, chưa verify UI trực tiếp.

---

#### REQ-SENDER-009/010 — Email tự điền người nhận (UNBLOCK — xem C-SENDER-1 lineage cũ không áp dụng, đây là REQ riêng US-D18)

**UI Confirmation (2026-07-28, DOC-v1.1-02):** Trước đây (v1.0) SC-SENDER-009/010 ở trạng thái 🚫 Blocked vì "Bản HTML prototype hiện tại KHÔNG có field email này ở wizard bước 2". Nay xác nhận field **ĐÃ TỒN TẠI** (xem REQ-SENDER-003 UI Confirmation ở trên) → chuyển **⏳ Ready**. Lưu ý: chỉ xác nhận field tồn tại, CHƯA verify được hành vi autofill thật (tìm thấy/không tìm thấy) vì không rõ danh sách email hợp lệ trong dữ liệu demo — cần vibe-test bổ sung trước khi generate-tc.

---

#### REQ-RECEIVER-002 — Xác nhận đã nhận hàng (MODIFIED — SLA cụ thể hoá)

**Source Quote (old, v1.0 — DOC-v1.0-01 §3.2):** *(không có SLA cụ thể — chỉ mô tả có CTA)*

**Source Quote (new, v1.1 — DOC-v1.1-01 §D1b US-D14, §D4 BR-CNF-04):**
> "Là Receiver/Sender, tôi muốn xác nhận "Đã nhận" sau khi Carrier báo đã giao... Chỉ xác nhận được sau khi Carrier đã bấm "Đã giao"; quá 2 giờ không xác nhận → hệ thống nhắc, thêm 2 giờ → admin hỗ trợ"
> `BR-CNF-04`: "RECEIVER không xác nhận 2 giờ → nhắc; thêm 2 giờ → admin hỗ trợ"

**Source Location:** `DOC-v1.1-01 §D1b US-D14 Acceptance Criteria`, `§D4 BR-CNF-04`

**Analyst Note (diff):** v1.0 chỉ có DLV-03/BR-CNF-04 dạng khung ("quá N giờ chưa xác nhận → nhắc → admin hỗ trợ", N chưa xác định). v1.1 chốt số cụ thể: **2 giờ đầu → nhắc, +2 giờ nữa (tổng 4 giờ) → admin hỗ trợ**. Đây là dữ liệu mới đủ để viết TC boundary/timing khi có cơ chế backend thật (hiện tại prototype vẫn chỉ có xác nhận thủ công tức thời qua nút bấm, KHÔNG có timer/nhắc tự động — case SLA timeout vẫn ở mức spec-only, chưa test được qua UI).

**UI Confirmation (2026-07-28, DOC-v1.1-02):** Happy-path (Carrier "Đã giao cho người nhận" → Receiver "Xác nhận đã nhận hàng" ngay) verify chạy đúng, đồng bộ 3 màn tức thời, chuyển "Hoàn thành". Case SLA 2h/4h **KHÔNG verify được** (không có cơ chế timer trong prototype).

---

#### REQ-ORDER-003 — Chỉnh sửa đơn khi "Chờ ghép" (UNBLOCK — partial)

**Source Quote:** *(không đổi so với v1.0, xem `02_analyze-requirements/v1.0/MEMORY.md` REQ-ORDER-003)* — `DOC-v1.1-01 §D1b US-D19`, `§D4 BR-EDIT-01`.

**UI Confirmation (2026-07-28, DOC-v1.1-02):** Ở màn "Theo dõi đơn" trạng thái "Chờ ghép" (Sender), cuối màn có 2 nút "✏️ Chỉnh sửa" và "❌ Huỷ đơn" — nút Chỉnh sửa **CÓ tồn tại trong UI**. Chưa bấm vào để verify form chỉnh sửa thật (điền sẵn dữ liệu cũ, nút Cập nhật/Huỷ chỉnh sửa) trong phiên verify này. SC-ORDER-005 chuyển 🚫 Blocked → ⏳ Ready (partial — cần vibe-test sâu hơn trước generate-tc). SC-ORDER-006 (khoá sửa sau MATCHED) cũng chuyển ⏳ Ready theo suy luận từ BR-EDIT-01 nhưng CHƯA tự verify trực tiếp (chưa thử bấm Chỉnh sửa ở trạng thái Đã ghép để xác nhận nút biến mất).

---

#### REQ-ORDER-004 — Tin quá hạn tự chuyển EXPIRED (MODIFIED — ngưỡng resolved = "Đến ngày")

**Source Quote (v1.1 — DOC-v1.1-01 §D8.1):**
> "Đến ngày | Có | Ngày hiện tại | Thời hạn cuối cùng để gửi hàng. Phải ≥ Từ ngày . **Quá ngày này mà chưa ghép → tin tự chuyển trạng thái Hết hạn** (xem OPR-04 & NTF-09)"

**Source Quote (v1.1 — DOC-v1.1-01 §D8.2, lặp lại cho OFFER):**
> "Đến ngày | Có | Ngày hiện tại | Thời gian kết thúc có thể giao. Phải ≥ Từ ngày . **Sau ngày này tin tự chuyển trạng thái Hết hạn** và ngừng khớp (xem OPR-04 & NTF-09)"

**Source Location:** `DOC-v1.1-01 §D8.1 "Đơn cần gửi hàng" table hàng "Đến ngày"`, `§D8.2 "Tin nhận giao hàng" table hàng "Đến ngày"`

**Analyst Note (⚠️ CONFLICT — cần user/BA re-confirm):** v1.0 (`02_analyze-requirements/v1.0/MEMORY.md` C-ORDER-2) đã ghi nhận user resolve trực tiếp: *"sau khi qua hạn ngày Từ ngày khi tạo sẽ hết hạn tin"* → ngưỡng EXPIRED = mốc **"Từ ngày"**. Nhưng BRD v3.2 nêu **RÕ RÀNG và LẶP LẠI 2 LẦN** (cả form SENDER lẫn form OFFER) rằng ngưỡng là **"Đến ngày"**, không phải "Từ ngày". Đây là 2 nguồn khác nhau về cùng 1 business rule — không tự chọn 1 bên, ghi Open lại ở §6 (addendum C-ORDER-2) để user xác nhận: **"Từ ngày" hay "Đến ngày" mới đúng là ngưỡng EXPIRED?** Ảnh hưởng trực tiếp tới TC boundary khi generate-tc cho SC-ORDER-007.

**UI Confirmation (2026-07-28, DOC-v1.1-02):** Tab "Đã hoàn thành" (Sender) vẫn hiện 1 order card mẫu với badge **"Hết hạn"** + text **"Không có ai nhận mang giúp trong thời gian đăng — tin đã tự động đóng."** — cùng UI/text như v1.0, KHÔNG có thông tin ngày Từ/Đến cụ thể hiển thị trên card này để đối chiếu trực tiếp ngưỡng nào đã kích hoạt. Badge tồn tại nhưng cơ chế trigger (worker backend) vẫn chưa có trong prototype — giữ 🚫 Blocked cho TC thật.

**Resolution (user, 2026-07-28):** "Den ngay dung" — **C-ORDER-2 RESOLVED (đảo ngược resolution v1.0):** ngưỡng EXPIRED = mốc tuyệt đối **"Đến ngày"** (field cuối trong khoảng ngày Sender/Carrier chọn ở wizard), KHÔNG phải "Từ ngày" như v1.0 từng chốt. Rule chính thức: nếu current date đã qua "Đến ngày" mà đơn vẫn ở `posted` (chưa MATCHED) → tự chuyển `EXPIRED`. generate-tc có thể viết TC boundary dựa trên mốc "Đến ngày" (vd: current date = Đến ngày → chưa expired; current date = Đến ngày + 1 → expired) khi UI/worker được implement. Vẫn 🚫 Blocked cho TC thật vì chưa có cơ chế backend trong prototype hiện tại — chỉ phần business rule được mở khoá.

---

#### REQ-GENERAL-003 — Trang chủ: dashboard (MODIFIED — cap 5 + Sender cũng có "Tin mới")

**Source Quote (v1.1 — DOC-v1.1-01 §D1b US-D06):**
> "Là Carrier, tôi muốn xem tối đa 5 tin cần gửi mới nhất ngay trên trang chủ, để nhanh chóng biết có ai cần giúp mà không cần vào sâu Bảng tin. | Trang chủ hiển thị đúng 5 tin mới nhất; nếu còn tin khác hiện nút "Xem thêm trên Bảng tin" dẫn sang màn Bảng tin"

**Source Location:** `DOC-v1.1-01 §D1b US-D06 Acceptance Criteria`

**Analyst Note (diff):** v1.0 REQ-GENERAL-003 mô tả content khác theo vai trò dạng nhị phân (Sender/Receiver = "Đơn của tôi"; Carrier = "Tin mới") nhưng KHÔNG có giới hạn số lượng. v1.1 chốt cụ thể: tối đa 5 tin + nút "Xem thêm trên Bảng tin" khi còn tin khác — nhưng BRD **chỉ mô tả rule này cho Carrier**, không nhắc Sender.

**UI Confirmation (2026-07-28, DOC-v1.1-02, ⚠️ discrepancy mới phát hiện):** Quan sát trực tiếp — **Trang chủ của SENDER cũng hiển thị section "Tin mới"** (bên dưới "Đơn của tôi"), liệt kê các tin khác trên bảng tin — không chỉ Carrier mới có section này như REQ-GENERAL-003 gốc (v1.0) mô tả. Chưa verify được cap "tối đa 5" có áp dụng đúng hay không (demo data hiện chỉ có 2 tin mẫu, chưa đủ để kiểm tra ngưỡng cắt).

**Resolution (user, 2026-07-28):** "viet theo UI luon nha" — **C-GENERAL-4 RESOLVED:** section "Tin mới" trên Trang chủ là tính năng CHUNG cho cả Sender lẫn Carrier (không chỉ riêng Carrier như BRD US-D06 mô tả) — viết TC theo đúng UI quan sát được. generate-tc nên viết 2 case cap-5 (1 cho mỗi vai trò) thay vì chỉ 1 case Carrier như trước.

---

#### REQ-CANCEL-001 — Huỷ đơn bắt buộc lý do (MODIFIED — min-length resolved: theo BRD, UI có gap)

**Source Quote (v1.1 — DOC-v1.1-01 §D8.3 VAL-04):**
> "Huỷ đơn: bắt buộc nhập lý do (**tối thiểu 5 ký tự**) mới bật nút Xác nhận"

**Source Location:** `DOC-v1.1-01 §D8.3 "Quy tắc chung cho form" · VAL-04`

**Analyst Note (diff):** v1.0 chỉ có "bắt buộc nhập lý do" (non-empty gate), không có ngưỡng ký tự. v1.1 thêm rule cụ thể: tối thiểu 5 ký tự.

**UI Confirmation (2026-07-28, DOC-v1.1-02, ⚠️ CONFIRMED discrepancy):** Test trực tiếp — mở popup "Huỷ đơn hàng" ở trạng thái "Chờ ghép", nhập **"ab" (2 ký tự)** vào textarea "Lý do huỷ" → nút "Xác nhận" **ĐÃ BẬT (enabled)** ngay, không chờ đủ 5 ký tự. Kết luận: UI thật **CHỈ chặn rỗng, KHÔNG enforce ngưỡng 5 ký tự tối thiểu** như VAL-04 mô tả.

**Resolution (user, 2026-07-28):** "lay theo rule BRD nha" — **C-CANCEL-1 RESOLVED:** rule đúng/target = BRD VAL-04 (tối thiểu 5 ký tự). UI hiện tại (chỉ chặn rỗng) là **gap cần dev bổ sung**, không phải BRD sai. generate-tc nên viết Expected Result theo BRD (5 ký tự tối thiểu) làm target behavior — TC này dự kiến sẽ **FAIL trên UI hiện tại** (vì thiếu enforce), ghi rõ trong Notes để khi tới giai đoạn vibe-test/execute, kết quả FAIL này được hiểu đúng là "chờ dev implement" chứ không phải TC viết sai — khuyến nghị log-bug tham chiếu C-CANCEL-1 khi tới giai đoạn đó.

---

#### REQ-GIFT-002 — Gửi quà (MODIFIED — verify đầy đủ lần đầu, kể cả popup cuối)

**Source Quote:** *(không đổi so với v1.0 — BRD v3.2 giữ nguyên text "gửi ngay không cần bước xác nhận... popup 'Cảm ơn của bạn đã được gửi'"; xem `02_analyze-requirements/v1.0/MEMORY.md` REQ-GIFT-002)*

**UI Confirmation (2026-07-28, DOC-v1.1-02 — hoàn tất phần v1.0 để dở):** Chạy trọn luồng lần đầu tới cùng (v1.0 dừng lại trước khi bấm Xác nhận để giữ nguyên state demo). Sau khi chọn quà (Bông hoa) và bấm "Xác nhận tặng quà" (nút xác nhận **VẪN CÒN** — cùng discrepancy đã ghi nhận ở v1.0, không đổi), popup cuối hiện: tiêu đề **"Đã gửi lời cảm ơn!"** + text **"Món quà và lời cảm ơn của bạn đã được gửi đến người vận chuyển."** + nút "Về trang chủ". Text này **khác nhẹ** so với câu BRD quote ("Cảm ơn của bạn đã được gửi") — khác biệt nội dung câu chữ, không đổi ý nghĩa nghiệp vụ, non-blocking. TC nên dùng đúng text UI thật đã verify.

---

#### REQ-GIFT-003/004 — "Quà đã nhận" — vai trò (MODIFIED — C-GIFT-2 RESOLVED)

**Source Quote:** *(không đổi — xem `02_analyze-requirements/v1.0/MEMORY.md` REQ-GIFT-003/004)*

**UI Confirmation (2026-07-28, DOC-v1.1-02 + DOC-v1.1-03 Figma re-check):** Ở v1.0, màn "Quà đã nhận" quan sát nhầm ở phone Receiver (Phan Văn Hưng) — nghi vấn bug wiring, đã ghi Clarification C-GIFT-2 dựa theo bằng chứng Figma (note "màng hình này nằm ở menu Cá nhân \ Quà đã nhận" gắn ở nhánh NGƯỜI GIAO). **v1.1 verify lại: bug đã được SỬA.** Tab "Cá nhân" của **Carrier (Nguyễn Anh Tuấn)** nay hiện đúng 2 mục "Đơn của tôi" và "Quà đã nhận"; tap vào "Quà đã nhận" → màn hiện đúng "Tổng quà đã nhận: 8 món" + breakdown 4 loại (3 Bông hoa/2 Ly cà phê/2 Gấu bông/1 Vương miện) + "LỊCH SỬ NHẬN QUÀ". Re-fetch Figma board (node 23:153) ở v1.1 xác nhận lại note gốc không đổi: connector `94:255` "*màng hình này nằm ở menu Cá nhân \ Quà đã nhận*" vẫn gắn ở nhánh NGƯỜI GIAO (Carrier) — khớp hoàn toàn với UI v1.1. **C-GIFT-2 → RESOLVED (bug đã fix), không còn Open.**

---

#### REQ-GENERAL-004 — Nút back (←) điều hướng đúng màn cha + không mất dữ liệu (MỚI, 2026-07-29)

**Source Quote:**
> (quan sát trực tiếp qua Chrome MCP, DOC-v1.1-02, không có text mô tả trong BRD/Figma — ghi lại nguyên trạng UI) Mọi màn con (không phải 1 trong 5 tab gốc của bottom nav) đều có icon back (←) ở góc trên trái header. Verify lần lượt: "Bạn muốn làm gì?" → back → Trang chủ; wizard bước 1 → back → "Bạn muốn làm gì?"; wizard bước 2 → back → bước 1; wizard bước 3 → back → bước 2; form OFFER "Tôi nhận giao hàng" → back → "Bạn muốn làm gì?"; Chi tiết tin → back → Bảng tin; Bảng tin → back → Trang chủ; Theo dõi đơn → back → "Đơn của tôi" (danh sách, tab Đang diễn ra/Đã hoàn thành) — **kể cả khi được mở trực tiếp từ card ở Trang chủ** (không đi theo lịch sử click thật, luôn có 1 đích cố định theo cây điều hướng); "Đơn của tôi" → back → Trang chủ; Thông báo → back → Trang chủ. Ở mọi bước wizard, dữ liệu đã nhập/chọn trước đó (chip Loại hàng, Giá trị hàng, Ghi chú, Tên/SĐT/Địa chỉ người nhận, Email công ty...) **KHÔNG bị mất** khi bấm back rồi quay lại bước đó — không có dialog cảnh báo mất dữ liệu nào xuất hiện (vì thực tế không có dữ liệu nào bị mất).

**Source Location:** `DOC-v1.1-02` — quan sát UI trực tiếp (localhost:8767, Design v3.2), không có §section tương ứng trong BRD/Figma (navigation-level behavior, không phải business rule)

**Analyst Note:** Cùng dạng REQ với REQ-GENERAL-002 (bottom nav, v1.0) — quan sát hành vi thực thi, không phải văn bản đặc tả. Điểm đáng chú ý nhất: (1) back luôn về 1 "màn cha" cố định theo cây điều hướng logic (Bảng tin → Trang chủ, Đơn của tôi → Trang chủ, Theo dõi đơn → Đơn của tôi...), KHÔNG phải "quay lại theo lịch sử click" kiểu trình duyệt — quan trọng vì Theo dõi đơn có thể được mở trực tiếp từ card Trang chủ (bỏ qua màn Đơn của tôi) nhưng back vẫn nhảy tới Đơn của tôi thay vì Trang chủ; (2) toàn bộ wizard đăng tin (3 bước) giữ nguyên state form khi back/forward qua lại giữa các bước, khác với giả định thường gặp là back sẽ làm mất dữ liệu chưa submit.

**⚠️ Inconsistency chưa xác định (2026-07-29):** Từ màn "Tặng quà" (mở qua Đơn của tôi → tab "Đã hoàn thành" → tap 1 đơn mẫu "Gửi đồ ăn sáng"), bấm back **KHÔNG** quay về "Đơn của tôi" như kỳ vọng logic, mà nhảy tới màn "Xác nhận đã nhận hàng" của **1 đơn khác không liên quan** (hiện "THÔNG TIN CARRIER: Trần Thị Lan", "ẢNH BẰNG CHỨNG" — thuộc luồng MEDIA/REQ-MEDIA-001, dữ liệu của đơn "Đồ điện tử" đang track chính, không phải đơn "Gửi đồ ăn sáng" vừa tặng quà). Nhiều khả năng là do các item tĩnh trong tab "Đã hoàn thành" (dữ liệu mẫu minh hoạ, không phải đơn thật có back-stack riêng) chưa được wiring đầy đủ — cùng loại giới hạn kiến trúc demo đã ghi nhận ở C-SENDER-2 (single-order-slot). Xem Clarification C-GENERAL-5 (Open) — **KHÔNG viết TC cho hành vi back ở màn Tặng quà** cho tới khi user/dev xác nhận đây là bug cần fix hay chỉ là giới hạn demo chấp nhận được.

---

## 5. Test Data Summary
| Module | DOC Source | Fields chính | Số bộ valid | Số bộ invalid | Có boundary? |
|--------|-----------|-------------|-------------|---------------|-------------|
| SENDER | DOC-v1.1-01 §D8.1 | Loại hàng (8 mục theo UI, resolved — BRD 5-mục KHÔNG áp dụng, C-SENDER-3), Ghi chú (≤300 ký tự — MỚI), Giá trị hàng (bắt buộc chọn — MỚI), Ảnh (≤5MB JPG/PNG — MỚI), Tên người nhận (2-60 ký tự — MỚI), SĐT (10 số đầu 0 — MỚI), Email công ty người nhận (MỚI field), Khung giờ (tối thiểu 30 phút — MỚI) | 8 | 6 (bao gồm 5 case boundary mới) | **Có — nhiều boundary mới cụ thể hoá từ "chưa xác định" v1.0** |
| ORDER | DOC-v1.1-01 §D8.1/D8.2 | Từ ngày / Đến ngày — ngưỡng EXPIRED = **"Đến ngày"** (resolved, đảo ngược resolution v1.0, xem C-ORDER-2) | 2 | 2 | Có — boundary quanh mốc "Đến ngày" |
| CANCEL | DOC-v1.1-01 §D8.3 VAL-04 | Lý do huỷ (target = BRD tối thiểu 5 ký tự, resolved; UI hiện tại chưa enforce — gap cần dev fix, xem C-CANCEL-1) | 1 | 2 (rỗng, và case 1-4 ký tự để verify boundary 5) | Có — 5 ký tự là boundary chính thức |

## 6. Clarifications & Blockers
| # | Req ID | DOC Source | Vấn đề | Answer | Status | Ngày resolve | Ảnh hưởng |
|---|--------|-----------|--------|--------|--------|-------------|-----------|
| C-SENDER-1, C-CARRIER-1, C-CARRIER-2 | (nhiều) | — | Xem `02_analyze-requirements/v1.0/MEMORY.md §6` | — | **CARRIED — không đổi** (đã Resolved+Unblocked ở v1.0) | 2026-07-24/27 | — |
| C-SENDER-2 | REQ-SENDER-002/005 | DOC-v1.0-01 | Wizard không tạo listing độc lập trong feed | — | **CARRIED — Open, không đổi** (xem thêm ghi chú multi-listing UI mới ở REQ-CARRIER-006 Analyst Note, chưa đủ bằng chứng để resolve hẳn — feed hiện có nhiều item hiển thị nhưng click vào item khác vẫn route về CÙNG 1 order state với order chính, cho thấy vẫn là single-order-slot ở tầng logic dù UI hiện đa dạng hơn) | — | generate-tc: giữ nguyên note cũ |
| C-ORDER-1 | REQ-ORDER-002 | DOC-v1.0-01 | Reset có xoá form wizard data không | — | **CARRIED — Open, không đổi** | — | — |
| C-ORDER-2 (đảo ngược v1.0) | REQ-ORDER-004 | DOC-v1.1-01 §D8.1/D8.2 vs resolution user 2026-07-27 (v1.0) | v1.0 user đã chốt ngưỡng EXPIRED = "Từ ngày". BRD v3.2 nói RÕ RÀNG (2 lần, cả 2 loại form) ngưỡng là **"Đến ngày"** — mâu thuẫn trực tiếp với câu trả lời cũ | "Den ngay dung" | **✅ RESOLVED — ngưỡng = "Đến ngày"** (đảo ngược resolution v1.0) | 2026-07-28 | generate-tc: viết TC boundary cho EXPIRED dựa trên mốc "Đến ngày" khi có UI/worker. Ghi rõ trong Notes rằng resolution v1.0 ("Từ ngày") đã lỗi thời, không dùng lại |
| C-GENERAL-2 | REQ-RECEIVER-002, REQ-GIFT-* | DOC-v1.1-02 (renewed evidence) | Rating sao có tồn tại không? | User đã xác nhận 2 lần ở v1.0: KHÔNG. v1.1 quan sát lại: order card "Đã hoàn thành" (mẫu demo có sẵn, không phải order vừa test) vẫn hiện **"★★★★★ Đã đánh giá"**, và Lịch sử của order vừa hoàn thành ghi text "Hoàn thành & đã đánh giá" — nhưng luồng hoàn thành thật (vừa test end-to-end) **KHÔNG** hiện popup rating nào, chỉ có luồng Gift | *(giữ nguyên: không rating)* | **Resolved (reaffirm) — nhưng UI còn tàn dư text/badge "đánh giá" cần dev dọn** | 2026-07-28 (reaffirm) | Không viết TC cho bước rating. Khuyến nghị: khi vào giai đoạn log-bug, ghi nhận UI leftover ("★★★★★ Đã đánh giá" trên order mẫu cũ + text Lịch sử "đã đánh giá") là bug cần dọn, tham chiếu C-GENERAL-2 |
| C-GENERAL-3 | Profile Carrier/Receiver | DOC-v1.1-01 §A6 USR-05 vs DOC-v1.1-02 | Tier/điểm uy tín/điểm ECO có nên hiện trên profile không? | **Một phần đã tự sửa:** UI v1.1 KHÔNG còn hiện số "điểm uy tín"/"điểm ECO" (chỉ còn "đơn đã giúp" + "quà đã nhận" — khớp đúng BRD §A6 USR-05 "không tính điểm/CO₂"). Nhưng **badge tier "Hạng Đồng hành" VẪN CÒN** trên Cá nhân | *(chưa hỏi lại — chỉ phần điểm số đã tự resolve)* | **🟡 Partially Resolved (v1.1)** — điểm số: Resolved (đã bỏ); tier badge: vẫn Open | 2026-07-28 (partial) | generate-tc: có thể viết TC cho "đơn đã giúp"/"quà đã nhận" (không tranh cãi); KHÔNG viết TC cho tier badge tới khi user xác nhận giữ hay bỏ |
| C-GIFT-2 | REQ-GIFT-003/004 | DOC-v1.1-02 + DOC-v1.1-03 (Figma re-check) | Màn "Quà đã nhận" thuộc vai trò nào? | Bug wiring v1.0 (hiện nhầm ở Receiver) đã được sửa — nay đúng ở Carrier's Cá nhân, khớp Figma | **✅ RESOLVED (bug fixed)** | 2026-07-28 | generate-tc: viết TC bình thường, Precondition = Carrier's Cá nhân tab, không còn là case "kỳ vọng bug" |
| C-SENDER-3 | REQ-SENDER-002 | DOC-v1.1-01 §D8.1 vs DOC-v1.1-02 | BRD liệt kê 5 danh mục Loại hàng (Tài liệu/Đồ điện tử/Thực phẩm/**Quà tặng**/Khác) nhưng UI vẫn hiện 8 chip cũ (gồm cả **Thuốc/Y tế** — chip từng bị flag mâu thuẫn với banner cấm hàng cấm ở v1.0 comprehensive TC) | "van 8 loai hang nhu UI nha, thuoc/y te khong phai hang cam" | **✅ RESOLVED — giữ 8 category theo UI, Thuốc/Y tế xác nhận KHÔNG phải hàng cấm** | 2026-07-28 | generate-tc: viết TC EP cho đủ 8 category theo UI thật; ĐÓNG cảnh báo P1 contradiction "Thuốc/Y tế" kế thừa từ v1.0 (không còn là rủi ro) — hạ về EP bình thường |
| C-CANCEL-1 | REQ-CANCEL-001 | DOC-v1.1-01 §D8.3 VAL-04 vs DOC-v1.1-02 | BRD yêu cầu lý do huỷ tối thiểu 5 ký tự, UI thật chỉ chặn rỗng (đã verify trực tiếp: 2 ký tự vẫn bật nút Xác nhận) | "lay theo rule BRD nha" | **✅ RESOLVED — target = BRD (tối thiểu 5 ký tự); UI hiện tại là gap cần fix** | 2026-07-28 | generate-tc: viết Expected theo BRD (5 ký tự) làm target — TC dự kiến FAIL trên UI hiện tại, ghi rõ "chờ dev implement"; khuyến nghị log-bug khi tới giai đoạn đó |
| C-GENERAL-4 | REQ-GENERAL-003 | DOC-v1.1-01 §D1b US-D06 vs DOC-v1.1-02 | BRD mô tả section "Tin mới" cap-5 là tính năng riêng cho Carrier, nhưng UI v1.1 cho thấy **Sender's Trang chủ cũng có section "Tin mới"** | "viet theo UI luon nha" | **✅ RESOLVED — áp dụng cho cả Sender lẫn Carrier** | 2026-07-28 | generate-tc: viết 2 case cap-5 (Sender + Carrier) thay vì chỉ Carrier như BRD mô tả |
| C-GENERAL-5 | REQ-GENERAL-004 | DOC-v1.1-02 (quan sát UI trực tiếp) | Back (←) ở màn "Tặng quà" (mở từ item mẫu tab "Đã hoàn thành") nhảy tới màn "Xác nhận đã nhận hàng" của 1 đơn KHÁC không liên quan (Trần Thị Lan/ảnh bằng chứng), thay vì quay về "Đơn của tôi" như mọi màn con khác đều làm nhất quán | — | **Open** — chưa hỏi user, nhiều khả năng là giới hạn demo (item mẫu tĩnh chưa wiring back-stack riêng, cùng loại C-SENDER-2) chứ không phải bug nghiêm trọng | — | generate-tc: KHÔNG viết TC cho back-behavior ở màn Tặng quà cho tới khi resolve; các back-icon khác (đã verify nhất quán) vẫn viết TC bình thường (xem §9) |
| C-SENDER-4 | REQ-SENDER-002, REQ-SENDER-003 | DOC-v1.1-01 §D8.1 vs user 2026-07-29 | BRD §D8.1 ghi RÕ 2 field "Địa chỉ lấy hàng" (Người gửi) và "Địa chỉ giao hàng" (Người nhận) là free-text ("Không để trống, tối đa 200 ký tự"), UI hiện tại (2026-07-29) cũng đang render textbox tự do — nhưng user khẳng định đây là **bug trong file html**, hành vi ĐÚNG phải là dropdown/select | "Dia chi lay hang va Dia chi giao hang a" (xác nhận 2 field) + yêu cầu trực tiếp: đổi field input Địa chỉ giao và Địa chỉ nhận thành droplist | **Resolved theo hướng override** — dropdown là target chính thức, BRD §D8.1 (free-text) coi là chưa cập nhật theo quyết định mới nhất của user | 2026-07-29 | generate-tc: viết TC theo hành vi dropdown (target) cho cả 2 field — các TC này dự kiến FAIL trên UI hiện tại (vẫn textbox), cần log-bug khi tới giai đoạn thực thi. KHÔNG có danh sách địa điểm cụ thể được cung cấp — TC dùng "1 địa điểm bất kỳ trong dropdown" làm đại diện, tương tự cách xử lý chip Loại hàng. **Bổ sung 2026-07-29 (lần 3):** cả 2 dropdown phải có rule bắt buộc chọn (không cho để trống) — đối xứng, áp dụng cho cả "Địa chỉ lấy hàng" (vốn trước đó chỉ có TC pre-fill mặc định, thiếu case bắt buộc chọn) lẫn "Địa chỉ giao hàng" (đã có sẵn) |
| C-CANCEL-2 | REQ-CANCEL-001, REQ-CANCEL-004 | DOC-v1.1-02 (quan sát UI trực tiếp) vs user 2026-07-29 | Live-verify qua Chrome MCP (2026-07-29) cho thấy hành động Huỷ đơn (Sender/Receiver) và Huỷ nhận đơn (Carrier) KHÔNG ghi log nào vào block LỊCH SỬ — Huỷ đơn chỉ hiện ở banner đỏ riêng "Đơn hàng đã bị huỷ", Huỷ nhận đơn còn XOÁ LUÔN dòng "Ghép thành công" khỏi LỊCH SỬ. User yêu cầu sửa lại: "huy don va huy nhan don hien tai cu luu log lich su nha" — coi đây là hành vi target/mong muốn (đơn giản hoá, nhất quán với mọi transition khác đều ghi log) | "huy don va huy nhan don hien tai cu luu log lich su nha" | **Resolved theo hướng override** — LỊCH SỬ có ghi log cho cả 2 hành động huỷ là target chính thức; hành vi UI hiện tại (không log / xoá dòng) coi là gap cần dev bổ sung | 2026-07-29 | generate-tc: sửa Expected Result của 5 TC (Sender huỷ Chờ ghép/Đã ghép, Receiver huỷ Chờ ghép/Đã ghép, Carrier huỷ nhận đơn) để khẳng định LỊCH SỬ có thêm dòng mới; các TC này dự kiến FAIL trên UI hiện tại, cần log-bug khi tới giai đoạn thực thi |

### 6.1. Clarification Source Detail (per `references/quoting-guide.md` EC6)

#### C-ORDER-2 — Ngưỡng EXPIRED: "Từ ngày" hay "Đến ngày"? (✅ RESOLVED — đảo ngược v1.0)

**Source Quote (2 nguồn từng mâu thuẫn):**
> Nguồn 1 (v1.0, user resolve 2026-07-27): "sau khi qua hạn ngày Từ ngày khi tạo sẽ hết hạn tin"
> Nguồn 2 (v1.1, DOC-v1.1-01 §D8.1): "Đến ngày | ... | Phải ≥ Từ ngày . Quá ngày này mà chưa ghép → tin tự chuyển trạng thái Hết hạn"
> Nguồn 3 (v1.1, DOC-v1.1-01 §D8.2, lặp lại cho form OFFER): "Đến ngày | ... | Sau ngày này tin tự chuyển trạng thái Hết hạn và ngừng khớp"

**Source Location:** `DOC-v1.1-01 §D8.1` + `§D8.2` (2 vị trí độc lập, cùng nói "Đến ngày"), đối chiếu resolution cũ tại `02_analyze-requirements/v1.0/MEMORY.md §6.1 C-ORDER-2`

**Analyst Note:** BRD v3.2 nói "Đến ngày" nhất quán ở CẢ 2 form (SENDER và OFFER) — không phải lỗi đánh máy đơn lẻ.

**Resolution (user, 2026-07-28):** "Den ngay dung" — ngưỡng EXPIRED chính thức = mốc **"Đến ngày"**. Resolution v1.0 ("Từ ngày") coi như lỗi thời, KHÔNG dùng lại. generate-tc viết TC boundary cho SC-ORDER-007 dựa trên mốc "Đến ngày" (vd current date = Đến ngày → chưa expired; = Đến ngày + 1 → expired) khi có UI/worker thật.

#### C-SENDER-3 — Danh mục "Loại hàng": 5 (BRD) hay 8 (UI)? (✅ RESOLVED)

**Source Quote:**
> BRD: "Loại hàng | Có | Tài liệu | Chọn 1 trong danh mục: Tài liệu · Đồ điện tử · Thực phẩm · Quà tặng · Khác"
> UI thật (quan sát trực tiếp DOC-v1.1-02): chip hiện "Tài liệu, Đồ điện tử, Thực phẩm, Hàng nhỏ, Đồ dễ vỡ, Quần áo, Thuốc/Y tế, Khác" (8 chip)

**Source Location:** `DOC-v1.1-01 §D8.1` vs quan sát UI trực tiếp `DOC-v1.1-02`

**Resolution (user, 2026-07-28):** "van 8 loai hang nhu UI nha, thuoc/y te khong phai hang cam" — giữ nguyên 8 category như UI hiện tại (BRD 5-category KHÔNG áp dụng, coi là chưa cập nhật). **"Thuốc/Y tế" xác nhận KHÔNG phải hàng cấm** — đóng nghi vấn P1 contradiction kế thừa từ v1.0 (banner cấm hàng "thuốc" không áp dụng cho category chip này). generate-tc viết EP cho đủ 8 category, không cần giữ risk-flag P1 cho "Thuốc/Y tế" nữa.

### 6.2. UI Block Map — per màn hình (theo yêu cầu user 2026-07-28, phục vụ generate-tc viết UI-smoke TC)

> Verify trực tiếp qua Chrome MCP (`get_page_text` trên DOM thật, không suy đoán) 2026-07-28. Phạm vi: 3 sheet **Trang chủ / Bảng tin / Đăng tin** (đã yêu cầu trước). Sheet còn lại (Hoạt động/Cá nhân/Thông báo) sẽ làm tương tự khi tới lượt generate-tc cho các sheet đó. Mỗi block liệt kê là 1 ứng viên UI-smoke TC (đủ hiển thị đúng) — generate-tc dùng danh sách này làm checklist, không cần tự dò lại UI.

#### Màn "Trang chủ" (dashboard, landing screen mặc định)
1. Header: "Xin chào, {tên}" + icon chuông (có red-dot khi có thông báo chưa đọc)
2. Banner cam: "Tiện đường — Giúp đồng nghiệp" + badge icon "FOX ECO"
3. Card "Đóng góp của bạn": số lớn "{N} đơn đã giúp" + "Cộng đồng FoxEco: {N} đơn · {N} người"
4. Button "Xem bảng tin gửi hàng"
5. Section "Đơn của tôi" + link "Xem tất cả" — card: "{Gửi/Nhận}: {loại hàng} | {giá trị}" + badge trạng thái, "Từ:"/"Đến:", progress bar, "Chạm để theo dõi đơn của bạn" — **chỉ Sender/Receiver có card này (Carrier không có, đã verify)**
6. Section "Tin mới" — list item: "{loại hàng} | {giá trị}" + mốc thời gian tương đối, "Nhận:"/"Giao:", "{ngày} · {khung giờ}" — **cả 3 vai trò đều có section này (Sender/Carrier/Receiver, resolved C-GENERAL-4 — trước đó tưởng chỉ Carrier)**
7. Bottom nav: Trang chủ (active) / Bảng tin / + / Hoạt động / Cá nhân

#### Màn "Bảng tin" (danh sách đầy đủ, vào từ icon bottom nav hoặc "Xem bảng tin gửi hàng")
1. Header: back arrow + tiêu đề "Bảng tin"
2. List item (lặp lại N lần): icon/ảnh thumbnail, "{loại hàng} | {giá trị}" + mốc thời gian tương đối (góc phải), "Nhận: {địa chỉ}", "Giao: {địa chỉ}", "{ngày} · {khung giờ}"
3. Tag "Tin của bạn" — CHỈ hiện trên item do chính vai trò đang xem đăng (đã có SC-CARRIER-008)
4. **State KHÔNG có data (list rỗng) — CHƯA verify được UI thật** (demo luôn có ≥1 tin mẫu). Theo yêu cầu user (2026-07-28): **vẫn generate TC** (Precondition "Bảng tin không có tin nào" + Steps quan sát màn hình) nhưng **để trống cột Expected Result** — user sẽ tự điền khi có UI thật để đối chiếu.

#### Màn "Chi tiết tin" (tap 1 item từ Bảng tin)
1. Header: back arrow + "Chi tiết tin"
2. Mốc thời gian tương đối (dưới header)
3. Title: "Gửi {loại hàng} từ {A} → {B}"
4. Section "ẢNH SẢN PHẨM" — ảnh (hoặc case không ảnh, chưa xác định — SC-CARRIER-009)
5. Section "THÔNG TIN HÀNG" — 2 cột: Loại hàng | Giá trị
6. "Ghi chú" — text tự do
7. Section "LỘ TRÌNH" — Lấy hàng (địa chỉ) / Giao hàng (địa chỉ) + "Bản đồ · ~{N} km" (placeholder, không phải map thật)
8. Section "KHUNG GIỜ" — "{ngày} · {giờ từ} – {giờ đến}"
9. Section "NGƯỜI GỬI" — tên, SĐT, nút "Gọi"
10. CTA cuối trang: "Tôi mang giúp được" (đổi theo trạng thái đơn — xem SC-CARRIER-001..007)

#### Màn "Bạn muốn làm gì?" (bấm "+" Đăng tin)
1. Header "Đăng tin mới"
2. Heading "Bạn muốn làm gì?"
3. Card "Tôi cần gửi hàng" + mô tả
4. Card "Tôi nhận giao hàng" + mô tả
5. Banner: "App không thu phí, không chat, không thanh toán. Sau khi ghép, SĐT hai bên sẽ được lộ để liên hệ ngoài app." (= REQ-GENERAL-001/SC-GENERAL-001)

#### Wizard "Tôi cần gửi hàng" — Bước 1/3 "Thông tin hàng"
1. Progress "Bước 1 / 3"
2. LOẠI HÀNG — 8 chip (Tài liệu*/Đồ điện tử/Thực phẩm/Hàng nhỏ/Đồ dễ vỡ/Quần áo/Thuốc·Y tế/Khác), *mặc định
3. GHI CHÚ — textarea
4. GIÁ TRỊ HÀNG (ƯỚC TÍNH) — 3 chip (bắt buộc chọn, validation gate đã verify)
5. ẢNH HÀNG (KHUYẾN NGHỊ) — "Chụp ảnh hoặc chọn từ thư viện"
6. Button "Tiếp theo" (khoá tới khi Giá trị hàng được chọn — đã verify)

#### Wizard "Tôi cần gửi hàng" — Bước 2/3 "Địa điểm & Thời gian"
1. Progress "Bước 2 / 3"
2. NGƯỜI GỬI — 3 field (Tên/SĐT/Địa chỉ lấy hàng — pre-filled từ tài khoản, **đã verify đây là textbox có thể sửa, KHÔNG readonly như BRD D8.1 mô tả "Chỉ đọc" — discrepancy mới, chưa ghi Clarification riêng, cần user xác nhận có phải bug không**)
3. NGƯỜI NHẬN — Email công ty người nhận (field mới, có validation riêng "Vui lòng nhập email công ty người nhận" nếu bỏ trống; nhập email không có trong hệ thống → **"Không tìm thấy email này trong hệ thống · vui lòng nhập thủ công."** — đã verify nguyên văn UI thật, khớp gần đúng BRD), Tên người nhận, Số điện thoại, Địa chỉ giao hàng (đều có validation "Vui lòng nhập..." riêng — đã verify)
4. KHOẢNG THỜI GIAN (NGÀY) — Từ ngày / Đến ngày (date picker, default hôm nay)
5. KHUNG GIỜ MONG MUỐN — Từ / Đến (time picker, default 17:00–18:30)
6. Button "Tiếp theo"

#### Wizard "Tôi cần gửi hàng" — Bước 3/3 "Xác nhận & Đăng tin"
1. Progress "Bước 3 / 3"
2. "Tóm tắt đơn gửi hàng": Loại hàng, Khung giờ, Người gửi (tên·SĐT + địa chỉ), Người nhận (tên·SĐT + địa chỉ), Ghi chú (hoặc "Không có ghi chú" nếu để trống — đã verify default text)
3. Banner cảnh báo: "Không được gửi: thuốc, vũ khí, chất nguy hiểm, hàng phi pháp. FoxEco là nền tảng kết nối, không chịu trách nhiệm về nội dung hàng."
4. Checkbox: "Tôi đã đọc và đồng ý Điều khoản sử dụng FoxEco. Tôi tự chịu trách nhiệm về hàng hóa và thỏa thuận với người mang giúp."
5. Button "Đăng tin ngay" (khoá tới khi tick checkbox)

#### Wizard "Tôi nhận giao hàng" (OFFER — 1 màn duy nhất)
1. Title "Tôi nhận giao hàng"
2. Subtitle: "Hệ thống sẽ tự tìm kiếm và kết nối bạn với người cần gửi. Mọi thông tin chỉ được chia sẻ sau khi bạn xác nhận nhận giao đơn hàng."
3. THÔNG TIN CỦA TÔI — tên/SĐT pre-filled
4. ĐIỂM XUẤT PHÁT (A) — pre-filled từ nơi làm việc (theo BRD), sửa được
5. ĐIỂM ĐẾN (B) — trống
6. KHOẢNG THỜI GIAN (NGÀY) — Từ ngày / Đến ngày
7. THỜI GIAN DI CHUYỂN — Khởi hành / Đến nơi
8. Checkbox "Tôi đã đọc và đồng ý Điều khoản sử dụng FoxEco."
9. Button "Đăng tin ngay"

**✅ RESOLVED, đính chính (user, 2026-07-28 — lần 2 "update lại tên người gửi chỉ đọc nha"):** Đọc lại đúng BRD D8.1 theo từng dòng: chỉ **"Tên người gửi"** ghi rõ "Chỉ đọc (lấy từ hồ sơ nhân viên)"; **"SĐT người gửi"** và **"Địa chỉ lấy hàng"** có validate rule riêng (format SĐT VN hợp lệ; địa chỉ không để trống ≤200 ký tự) — nghĩa là 2 field này VỐN ĐÃ được thiết kế để sửa được, không mâu thuẫn gì. Câu trả lời đầu ("được sửa a") áp dụng đúng cho SĐT/Địa chỉ; riêng **Tên người gửi = CHỈ ĐỌC** theo đúng BRD (đính chính lại, không phải "cả 3 field đều sửa được" như note trước). **Lưu ý:** lúc verify UI trực tiếp, "Tên người gửi" hiện dưới dạng textbox trong accessibility tree giống hệt 2 field kia — CHƯA tự test gõ thử để xác nhận có thực sự bị khoá (readonly) hay không. generate-tc cần viết TC verify "Tên người gửi" là readonly/disabled (không sửa được), và nếu vibe-test sau này phát hiện UI thật cho sửa được thì đó là gap cần log-bug (không phải target behavior).

**Bảng tin — state rỗng (không có tin nào):** user xác nhận (2026-07-28, đã update lại) — **VẪN generate TC bình thường** (đủ Steps/Precondition), chỉ riêng cột **Expected Result để trống** cho user tự điền sau khi có UI thật quan sát được. Đây là ngoại lệ có chủ đích cho case này, KHÔNG áp dụng Custom Rule #4 (vốn là "không generate khi Expected chưa xác định") — ngoại lệ chỉ áp cho SC/case này, không đổi rule chung.

## 8. Deliverable Files Reference
| File | Đường dẫn | Mô tả |
|------|-----------|-------|
| Requirement Traceability | `02_analyze-requirements/v1.1/requirement_traceability.md` | Ma trận truy vết |
| Test Scenario Map | `02_analyze-requirements/v1.1/test_scenario_map.md` | Chi tiết scenarios MODIFIED + roll-up CARRIED |
| Test Data Catalog | `02_analyze-requirements/v1.1/test_data_catalog.md` | Dữ liệu test — nhiều boundary mới cụ thể hoá |
| Risk Assessment | `02_analyze-requirements/v1.1/risk_assessment.md` | Đánh giá rủi ro, thêm risk cho 2 discrepancy mới |

## 9. TC Generation Log
> **PARTIAL — 3/6 sheet đã generate (Trang chủ/Bảng tin/Đăng tin), còn Hoạt động/Cá nhân/Thông báo chưa làm.** Mode kết hợp `comprehensive` (B1 EP, B3 BVA, B6 EG) + 13-loại TC checklist qc7 (Custom Rule #7-9, `Project_rule.md §8`) — theo yêu cầu user 2026-07-28. File: `03_test-cases/v1.1/TC-MASTER-v1.1.xlsx` (có sheet `ALL` gộp phẳng cả 3 sheet + `Overview` + `Coverage Matrix`).
> **Cập nhật (lần 2, cùng ngày):** user yêu cầu (1) thêm sheet `ALL`, (2) mọi Steps phải bắt đầu bằng bước đăng nhập FoxEco, (3) droplist/chip-select chỉ cần 1 case đại diện thay vì liệt kê hết giá trị, (4) Error Guessing + Validation nhiều case gộp lại thành ít TC hơn (cho phép Expected nhiều dòng trong các TC gộp này — ngoại lệ với Custom Rule #2). Đã áp dụng lại toàn bộ → Đăng tin giảm từ 120 xuống 72 TC.

| DOC ID | Ngày generate | Tổng TC | File output | Priority | Mode | Techniques | Review Status |
|--------|--------------|---------|-------------|----------|------|------------|---------------|
| DOC-v1.1-01/02 | 2026-07-28 | 25 | TC-MASTER-v1.1.xlsx (sheet "Trang chủ") | P1:1, P2:12, P3:12 | comprehensive+qc7 | B1, B3 | ⏳ |
| DOC-v1.1-01/02 | 2026-07-28 | 14 | TC-MASTER-v1.1.xlsx (sheet "Bảng tin") | P1:4, P2:7, P3:3 | comprehensive+qc7 | N/A (0-dim cho sheet này) | ⏳ |
| DOC-v1.1-01/02 | 2026-07-28 | 72 | TC-MASTER-v1.1.xlsx (sheet "Đăng tin") | P1:14, P2:33, P3:25 | comprehensive+qc7 | B1 (đại diện), B3, B6 (gộp) | ⏳ |
| **Tổng** | | **111** | | P1:19, P2:52, P3:40 | | | |
| DOC-v1.1-02 | 2026-07-29 | 10 | TC-MASTER-v1.1.xlsx (SC-GENERAL-005, rải 4 sheet: Đăng tin +5, Bảng tin +2, Flow +2, Trang chủ +1) | P1:0, P2:5, P3:5 | qc7 (Happy-Path) | N/A | ⏳ |

> **Lưu ý:** bảng trên dừng ở batch 111 TC (2026-07-28, trước khi thêm sheet Flow 49 TC cùng ngày) — không phải tổng số hiện tại của TC-MASTER. Xem `Overview` sheet trong file .xlsx để lấy tổng chính xác nhất (158 TC tính đến 2026-07-29).

**Ghi chú generate-tc:**
- **2026-07-29 (lần 9 — sắp xếp lại block SENDER trong sheet Flow):** user yêu cầu gộp 2 block "SENDER" (bị tách rời do "SENDER — Chỉnh sửa đơn (OPR-10)" chèn giữa) thành 1 block liền mạch, và đặt "Chỉnh sửa đơn" xuống SAU cùng. Kết quả: header "SENDER" trùng lặp bị xoá (còn 1 header duy nhất bao TC-FLOW-015 → 029 liền mạch — gồm CTA/Huỷ đơn + CTA Đang giao/Đã giao + Tặng quà), theo sau là header "SENDER — Chỉnh sửa đơn (OPR-10)" chứa TC-FLOW-030 → 036 (7 TC, nội dung giữ nguyên, chỉ đổi ID). Toàn bộ 15 TC từ 022-036 được renumber lại cho liên tục theo vị trí vật lý mới (project rule: TC ID phải liên tục theo thứ tự xuất hiện). TC-FLOW-037 trở đi (CARRIER/OFFER/RECEIVER) không đổi vì tổng số TC trong 2 block SENDER không đổi. Đã full-rebuild sheet Flow + sheet ALL (Flow portion), verify lại 67 TC/0 trùng ID/ID liên tục 1..67, re-run skillconvert → sheet-format vẫn 180 TC. **Coverage Matrix — rebuild mục "Flow" (2026-07-29, ngay sau lần 9):** phát hiện mục "Flow" trong `Coverage Matrix` sai định dạng từ trước — dùng TC ID làm giá trị cột "SC ID" (49 dòng, 1 dòng/TC) thay vì group theo SC ID như 3 sheet Trang chủ/Bảng tin/Đăng tin, cộng thêm 11 dòng vá rải rác ở cuối sheet mỗi khi có TC mới (SC-CANCEL-001/002/004, SC-ORDER-001/005/006, SC-CARRIER-004/005, SC-RECEIVER-002, SC-GENERAL-005) — dữ liệu bị lệch hẳn so với TC ID thật sau các lần renumber (vd dòng cũ ghi "TC-FLOW-020 (SC-GIFT-001)" trong khi TC-FLOW-020 thật là về Huỷ đơn). Đã rebuild lại toàn bộ mục Flow: đọc trực tiếp cột Scenario ID (cột B) + tag QC7-Type trong Notes của từng TC trong sheet Flow (nguồn xác thực duy nhất, không suy đoán) → gom thành **27 dòng theo SC ID** (thay vì 49 dòng sai + 11 dòng vá = 60 dòng cũ), mỗi dòng liệt kê rõ TC ID liên quan trong cột "13-loại áp dụng". B1-B8 giữ N/A toàn bộ (Flow sheet generate ở mode qc7 Happy-Path, không tag kỹ thuật B1-B8 như Đăng tin comprehensive mode). Không đụng tới 3 sheet Trang chủ/Bảng tin/Đăng tin (giữ nguyên, kể cả 1 dòng trùng lặp sẵn có ở Bảng tin SC-CARRIER-001 — ngoài phạm vi yêu cầu lần này).
- **2026-07-29 (nút Back):** user hỏi TC-MASTER đã cover icon back (←) ở từng màn chưa → kiểm tra thấy CHƯA có → live-verify trực tiếp qua Chrome MCP (không đoán, theo Custom Rule #6) rồi generate 10 TC mới cho SC-GENERAL-005/REQ-GENERAL-004. 1 hành vi phát hiện không nhất quán (back ở màn "Tặng quà" nhảy sang màn không liên quan) — KHÔNG generate TC cho case này, ghi Clarification C-GENERAL-5 (Open) thay vì đoán Expected Result.
- **2026-07-29 (lần 2 — user feedback sau khi xem TC nút Back):** 3 yêu cầu chỉnh sửa: (1) 10 TC nút Back phải nằm trong block UI tương ứng thay vì section riêng "Nút Back (←)" — đã di chuyển từng TC vào đúng section (vd back ở wizard bước 1 → cuối section "Wizard bước 1 — Ảnh hàng"; back ở Chi tiết tin → cuối section "Chi tiết tin"...), renumber lại toàn bộ 4 sheet liên quan theo thứ tự vật lý mới. (2) Field "Địa chỉ giao hàng" và "Địa chỉ lấy hàng" (Người gửi) phải là dropdown, không phải textbox như UI hiện tại — user xác nhận đây là bug trong html, xem C-SENDER-4 (override BRD §D8.1). Viết lại TC theo hành vi dropdown target: Người gửi +2 TC mới (pre-fill dropdown, đổi lựa chọn), Địa chỉ giao hàng bỏ 1 TC EG rỗng/khoảng trắng (không áp dụng cho dropdown) + thêm 1 TC happy-path chọn địa điểm khác — tất cả các TC dropdown này ghi rõ trong Notes là dự kiến FAIL trên UI hiện tại. (3) Flow sheet: bổ sung Expected Result cho block LỊCH SỬ ở 9 TC chuyển trạng thái, live-verify từng transition qua Chrome MCP (chạy full happy-path Chờ ghép→Hoàn thành + 2 nhánh huỷ) — phát hiện quan trọng: hành động Huỷ đơn (Sender/Receiver) KHÔNG log vào LỊCH SỬ mà hiện ở banner đỏ riêng "Đơn hàng đã bị huỷ"; Carrier huỷ nhận đơn (Đã ghép→Chờ ghép) cũng KHÔNG log mà XOÁ LUÔN dòng "Ghép thành công" khỏi LỊCH SỬ. Tổng TC-MASTER: 148 → 160.
- **2026-07-29 (lần 4b — rà soát gap coverage lần cuối, theo yêu cầu "check lại 4 sheet còn thiếu case nào không"):** đối chiếu tính đối xứng vai trò + lịch sử track scenario, phát hiện 2 gap thật: (1) Receiver thiếu cặp TC lock/dismiss cho dialog "Huỷ đơn hàng" mà Sender và Carrier đều có sẵn — bổ sung TC-FLOW-059/060. (2) SC-GENERAL-002 (bottom nav 5 icon) được track từ v1.0 nhưng CHƯA TỪNG có TC thật ở bất kỳ version nào (kể cả v1.0's 82-TC comprehensive set) — live-verify đủ 5 icon (Bảng tin/Đăng tin/Hoạt động/Cá nhân/Trang chủ) qua Chrome MCP rồi bổ sung TC-TRANGCHU-006. Tổng TC-MASTER: 177 → 180.
- **2026-07-29 (lần 3 — user feedback tiếp theo):** 3 yêu cầu: (1) "huỷ đơn và huỷ nhận đơn hiện tại cứ lưu log lịch sử nha" — user override finding ở lần 2 (huỷ không log): sửa lại Expected của 5 TC (Sender huỷ Chờ ghép/Đã ghép, Receiver huỷ Chờ ghép/Đã ghép, Carrier huỷ nhận đơn) để khẳng định LỊCH SỬ CÓ ghi log cho hành động huỷ — coi là target behavior, ghi Clarification mới C-CANCEL-2, các TC này dự kiến FAIL trên UI hiện tại. (2) Thêm rule bắt buộc chọn cho "Địa chỉ lấy hàng" (đối xứng với "Địa chỉ giao hàng" đã có) — +1 TC mới TC-DANGTIN-024. (3) Flow: thêm 3 TC mới — banner "Đơn hàng đã bị huỷ" hiển thị đúng trên Theo dõi đơn (đặt trong section chung 3 vai trò), popup xác nhận "Huỷ đơn hàng" (Sender/Receiver) và popup "Huỷ nhận đơn" (Carrier) — đã live-verify nguyên văn text cảnh báo của cả 2 popup qua Chrome MCP trước khi viết ("Bạn chắc chắn muốn huỷ đơn hàng này? Thao tác không thể hoàn tác." / "Bạn chắc chắn muốn huỷ nhận giao đơn này? Đơn sẽ được trả lại bảng tin để người khác nhận."). Tổng TC-MASTER: 160 → 164.
- **2026-07-29 (lần 6 — quét lại TOÀN BỘ file, xoá sạch "(đúng vai trò tương ứng với TC)"):** Lần 5 mới sửa 30 TC ở các section thực sự mơ hồ (role không suy ra được từ đâu cả). User yêu cầu quét lại toàn bộ file vì "còn nhiều text (đúng vai trò tương ứng với TC)" — đúng vậy, phrase này vẫn còn ở 133 chỗ khác trên cả 4 sheet (kể cả những TC mà role SUY RA được từ title/section, như "Sender thấy...", cả sheet Đăng tin). Lần này thay TOÀN BỘ 133 chỗ bằng tên vai trò cụ thể theo đúng ngữ cảnh: Đăng tin — Sender cho mọi wizard "Tôi cần gửi hàng" (bước 1-3), Carrier cho toàn bộ section OFFER; Flow — theo đúng section SENDER/CARRIER/RECEIVER, OFFER→Carrier, khối "chung 3 vai trò" còn lại theo title (Sender/Carrier tương ứng); Trang chủ — theo title khi có (Sender/Carrier/Receiver), "Đơn của tôi" section → "Sender hoặc Receiver" (2 vai trò cùng thấy), "Tin mới (cả 3 vai trò)" section không role riêng → Carrier đại diện; Bảng tin — Sender (người đăng)/Carrier (người xem tin người khác) tuỳ ngữ cảnh. Verify lại bằng script: 0 chỗ còn sót trên toàn bộ workbook. Không thêm TC mới, tổng vẫn 170.
- **2026-07-29 (lần 5 — sửa triệt để lỗi "vai trò mơ hồ" trên toàn bộ 3 sheet):** Lần 4 mới chỉ sửa Precondition của đúng 2 TC bị user chỉ ra trực tiếp; user phát hiện lỗi tương tự VẪN còn ở nhiều TC khác — cả trong Precondition (TC-TRANGCHU-001 vẫn còn "(vai trò bất kỳ)") lẫn trong Steps (rất nhiều TC dùng "(đúng vai trò tương ứng với TC)" mà không có chỗ nào khác trong TC nói rõ vai trò là gì). Đã rà soát toàn diện 3 sheet Trang chủ/Bảng tin/Flow, sửa 30 TC: Trang chủ 8 TC (section "Header & Thông báo" + "Banner..." — chọn Sender làm vai trò đại diện), Bảng tin 14 TC (section "Danh sách Bảng tin" + "Chi tiết tin" — chọn Carrier làm vai trò đại diện vì đây là hành động chính của Carrier), Flow 8 TC (section "THEO DÕI ĐƠN chung 3 vai trò" — Sender, đồng bộ với TC-FLOW-007/013 đã sửa ở lần 4). Nguyên tắc áp dụng: TC nào role đã rõ từ title (vd "Sender thấy...", "Carrier nhận đơn...") thì KHÔNG cần sửa; chỉ sửa TC nào role KHÔNG suy ra được từ bất kỳ đâu trong TC. Không có TC mới, chỉ sửa nội dung Precondition/Steps — tổng TC-MASTER giữ nguyên 170.
- **2026-07-29 (lần 4 — sửa Precondition + rà soát gap coverage toàn diện):** 2 yêu cầu: (1) Precondition "(bất kỳ vai trò nào)" ở TC-FLOW-006/012 (khi đó) bị user từ chối — không rõ ràng cho tester, phải ghi tên vai trò cụ thể. Sửa cả 2 thành "Sender" kèm ghi chú áp dụng tương tự cho Carrier/Receiver. (2) User yêu cầu rà soát lại đủ 4 sheet xem còn thiếu UI/popup/field nào chưa lên case — rà soát bằng cách đối chiếu mọi màn/dialog đã trực tiếp quan sát qua Chrome MCP trong suốt phiên làm việc với danh sách TC hiện có, phát hiện 6 gap thật sự (không phải suy đoán — đều đã live-verify tồn tại trước khi viết TC): (a) block "LỘ TRÌNH" (cả Theo dõi đơn lẫn Chi tiết tin) có dòng khoảng cách "Bản đồ · ~N km" nhưng chưa có TC riêng — thêm 2 TC (Flow TC-FLOW-003, Bảng tin TC-BANGTIN-011); (b) 3/4 dialog xác nhận chuyển trạng thái ("Tôi đã lấy hàng", "Đã giao cho người nhận", "Xác nhận đã nhận hàng") thiếu test "bấm Huỷ không đổi trạng thái" — chỉ dialog "Tôi mang giúp được" và 2 dialog Huỷ đơn có sẵn test này; verify lại qua Chrome MCP xác nhận cả 3 dialog đều có nút "Huỷ" cặp với "Xác nhận" — thêm đủ 3 TC (Flow); (c) form OFFER có field "Điểm đến (B)" (trống mặc định, placeholder "Bạn sẽ đến đâu") nhưng chưa có TC bắt buộc nhập — thêm 1 TC (Đăng tin). Tổng TC-MASTER: 164 → 170.
- Không generate TC cho SC-CARRIER-009 (ảnh vắng mặt ở Chi tiết tin) — Expected vẫn chưa xác định và CHƯA được user cho phép ngoại lệ (khác với 2 case rỗng dưới đây).
- 2 case để trống Expected Result có chủ đích theo yêu cầu user (2026-07-28): SC-GENERAL-004 (Trang chủ — "Đơn của tôi"/"Tin mới" rỗng, TC-TRANGCHU-014/025) và Bảng tin rỗng (TC-BANGTIN-006). Steps/Precondition đầy đủ, chỉ Expected Result để trống chờ user tự điền khi có UI thật.
- **EG gộp (2026-07-28, lần 2):** thay vì 10 TC riêng/field, gộp thành 3 TC/field theo nhóm (rỗng&khoảng trắng / dữ liệu đặc biệt / input độc hại) — áp dụng cho Ghi chú + Email/Tên/SĐT/Địa chỉ người nhận = 5 field × 3 TC = 15 TC (trước đó 50 TC). Các TC gộp này Expected có nhiều dòng đánh số 1:1 với sub-step trong Steps — ngoại lệ có chủ đích với Custom Rule #2 (chỉ áp cho case gộp nhiều pattern, KHÔNG áp dụng chung cho toàn bộ TC-MASTER).
- **EP droplist rút gọn (2026-07-28, lần 2):** Loại hàng (8 chip) và Giá trị hàng-nhóm-thấp/vừa (2 chip) chỉ còn 1 TC đại diện mỗi nhóm thay vì liệt kê hết — vì đã resolve C-SENDER-3 (8 category tương đương, không còn hành vi khác biệt). "Giá trị cao" vẫn giữ TC riêng vì có hành vi khác (cảnh báo bảo hiểm).
- **Validation gộp (2026-07-28, lần 2):** các case validate cùng field (SĐT sai định dạng ×3, ngày tháng không hợp lệ ×2, Ảnh không hợp lệ ×2, NGƯỜI GỬI SĐT+Địa chỉ ×2) gộp thành 1 TC/nhóm với nhiều sub-step + Expected nhiều dòng.
- **Steps bắt buộc bắt đầu bằng bước đăng nhập** (2026-07-28, lần 2, theo yêu cầu user) — mọi TC ở cả 3 sheet có Step 1 = "Đăng nhập thành công vào FoxEco (đúng vai trò tương ứng với TC), vào màn Trang chủ", các step sau renumber lại.
- Group enum chỉ dùng `UI`/`Functional` cho cả 111 TC — không có `Integration`/`Database` vì đây là demo client-side thuần, không có hệ thống thứ 2 hay data layer tách biệt để verify trực tiếp.
