# Requirement Traceability — v1.1

> Tạo bởi: analyze-requirements (mode DELTA từ v1.0). Ma trận truy vết REQ ↔ DOC ↔ Scenario ↔ Clarification.
> Text-level traceability: Source Quote per REQ MODIFIED ở `MEMORY.md §4.1`, per SC MODIFIED ở `test_scenario_map.md`. REQ/SC CARRIED (không đổi) — xem `02_analyze-requirements/v1.0/requirement_traceability.md`.
>
> **Structure-lock:** giữ nguyên header cột + section dưới đây. KHÔNG tự thêm/bớt/đổi tên cột.

## 1. Traceability Matrix (REQ → DOC → SC)

> 1 bảng con per module. 1 dòng / REQ (KHÔNG gộp nhiều REQ vào 1 dòng). `Lifecycle` thêm vào cuối tên cột Scenarios để đánh dấu MODIFIED/CARRIED nhanh.

### Module SENDER — DOC-v1.1-01, DOC-v1.1-02
| REQ ID | Maps (Ref DOC) | DOC §section | Scenarios | Clarification |
|--------|----------------|--------------|-----------|---------------|
| REQ-SENDER-001 | — | §D1b US-D01 (Figma-observed) | SC-SENDER-001 (CARRIED), SC-SENDER-002 (CARRIED) | C-SENDER-1 (resolved) |
| REQ-SENDER-002 | — | §D8.1 "Loại hàng/Ghi chú/Giá trị/Ảnh" + §D8.3 VAL-01/02 | SC-SENDER-003 (**MODIFIED**) | C-SENDER-2 (Open), C-SENDER-3 (✅ Resolved) |
| REQ-SENDER-003 | — | §D1b US-D18, §D8.1 "Người nhận" + §D8.3 VAL-03 | SC-SENDER-004 (**MODIFIED**) | — |
| REQ-SENDER-004 | — | §D8.1 "Khoảng thời gian/Khung giờ/Điều khoản" | SC-SENDER-005 (CARRIED), SC-SENDER-006 (CARRIED), SC-SENDER-007 (CARRIED) | — |
| REQ-SENDER-005 | — | §D1 "Prototype tham chiếu" | SC-SENDER-008 (CARRIED) | C-SENDER-2 (Open) |
| REQ-SENDER-006 | — | §D1b US-D18 | SC-SENDER-009 (**MODIFIED — UNBLOCK**), SC-SENDER-010 (**MODIFIED — UNBLOCK**) | — |

### Module CARRIER — DOC-v1.1-01, DOC-v1.1-02
| REQ ID | Maps (Ref DOC) | DOC §section | Scenarios | Clarification |
|--------|----------------|--------------|-----------|---------------|
| REQ-CARRIER-001 | — | §D1b US-D06/D07 | SC-CARRIER-001 (CARRIED) | — |
| REQ-CARRIER-002 | — | §D1b US-D07, §D3 ASN-01/02 | SC-CARRIER-002 (CARRIED), SC-CARRIER-003 (CARRIED) | — |
| REQ-CARRIER-003 | — | §D1b US-D09 | SC-CARRIER-004 (CARRIED) | — |
| REQ-CARRIER-004 | — | §D1b US-D09, §D3 DLV-03 | SC-CARRIER-005 (CARRIED), SC-CARRIER-006 (CARRIED) | C-CARRIER-1 (resolved) |
| REQ-CARRIER-005 | — | §D1b US-D14 | SC-CARRIER-007 (CARRIED) | C-CARRIER-2 (resolved) |
| REQ-CARRIER-006 | — | UI DOC-v1.1-02 (Bảng tin/Chi tiết tin field-level, không có §section BRD riêng) | SC-CARRIER-008 (CARRIED), SC-CARRIER-009 (CARRIED) | — |

### Module RECEIVER — DOC-v1.1-01, DOC-v1.1-02
| REQ ID | Maps (Ref DOC) | DOC §section | Scenarios | Clarification |
|--------|----------------|--------------|-----------|---------------|
| REQ-RECEIVER-001 | — | §D1b US-D08/D21 | SC-RECEIVER-001 (CARRIED), SC-RECEIVER-002 (CARRIED) | — |
| REQ-RECEIVER-002 | — | §D1b US-D14, §D4 BR-CNF-04 | SC-RECEIVER-003 (**MODIFIED**), SC-RECEIVER-004 (CARRIED) | C-GENERAL-2 (reaffirmed) |

### Module OFFER — DOC-v1.1-01, DOC-v1.1-03 (Ready, không đổi so với v1.0)
| REQ ID | Maps (Ref DOC) | DOC §section | Scenarios | Clarification |
|--------|----------------|--------------|-----------|---------------|
| REQ-OFFER-001 | — | §D1b US-D10, §D8.2 (form field-level mới) | SC-OFFER-001 (CARRIED) | C-SENDER-1 (unblocked) |
| REQ-OFFER-002 | — | §D1b US-D11 | SC-OFFER-002 (CARRIED) | — |
| REQ-OFFER-003 | — | §D1b US-D12, §D6 NTF-03 | SC-OFFER-003 (CARRIED) | — |
| REQ-OFFER-004 | — | §D1b US-D13 | SC-OFFER-004 (CARRIED) | — |

### Module CANCEL — DOC-v1.1-01, DOC-v1.1-02, DOC-v1.1-03
| REQ ID | Maps (Ref DOC) | DOC §section | Scenarios | Clarification |
|--------|----------------|--------------|-----------|---------------|
| REQ-CANCEL-001 | — | §D1b US-D16, §D3 CNL-01, §D4 BR-CNL-01, §D8.3 VAL-04 (mới) | SC-CANCEL-001 (**MODIFIED**), SC-CANCEL-002 (CARRIED) | C-CARRIER-1 (unblocked), C-CANCEL-1 (✅ Resolved — theo BRD, UI có gap) |
| REQ-CANCEL-002 | — | §D7 OPR-11, §D4 BR-ASN-03 | SC-CANCEL-003 (CARRIED) | — |
| REQ-CANCEL-003 | — | §D7 OPR-09 | SC-CANCEL-004 (CARRIED) | — |
| REQ-CANCEL-004 | — | §D1b US-D16 | SC-CANCEL-002 (CARRIED) | — |

### Module GIFT — DOC-v1.1-01, DOC-v1.1-02, DOC-v1.1-03
| REQ ID | Maps (Ref DOC) | DOC §section | Scenarios | Clarification |
|--------|----------------|--------------|-----------|---------------|
| REQ-GIFT-001 | — | §A7 | SC-GIFT-001 (CARRIED) | — |
| REQ-GIFT-002 | — | §D1b US-D15 | SC-GIFT-002 (**MODIFIED**) | C-GENERAL-2 (reaffirmed) |
| REQ-GIFT-003 | — | §D1b US-D20 | SC-GIFT-003 (**MODIFIED — C-GIFT-2 RESOLVED**) | C-GIFT-2 (**Resolved**) |
| REQ-GIFT-004 | — | UI DOC-v1.1-02 (không có §section BRD tương ứng) | SC-GIFT-004 (**MODIFIED — C-GIFT-2 RESOLVED**) | C-GIFT-2 (**Resolved**) |

### Module NOTIFICATION — DOC-v1.1-01, DOC-v1.1-02 (Ready, không đổi so với v1.0)
| REQ ID | Maps (Ref DOC) | DOC §section | Scenarios | Clarification |
|--------|----------------|--------------|-----------|---------------|
| REQ-NOTIFICATION-001 | — | §D6 | SC-NOTIFICATION-001 (CARRIED) | — |
| REQ-NOTIFICATION-002 | — | UI DOC-v1.1-02 (không có §section BRD tương ứng) | SC-NOTIFICATION-002 (CARRIED) | — |

### Module ORDER — DOC-v1.1-01, DOC-v1.1-02
| REQ ID | Maps (Ref DOC) | DOC §section | Scenarios | Clarification |
|--------|----------------|--------------|-----------|---------------|
| REQ-ORDER-001 | — | §D2 "ORDER STATUS MACHINE" | SC-ORDER-001 (CARRIED) | — |
| REQ-ORDER-002 | — | §D2 | SC-ORDER-002 (CARRIED), SC-ORDER-003 (CARRIED), SC-ORDER-004 (CARRIED) | C-ORDER-1 (Open) |
| REQ-ORDER-003 | — | §D1b US-D19, §D4 BR-EDIT-01, §D8.3 VAL-05 | SC-ORDER-005 (**MODIFIED — UNBLOCK partial**), SC-ORDER-006 (**MODIFIED — UNBLOCK partial**) | — |
| REQ-ORDER-004 | — | §D1b US-D04, §D8.1/§D8.2 "Đến ngày" (ngưỡng đã resolve) | SC-ORDER-007 (**MODIFIED**) | C-ORDER-2 (**✅ Resolved — "Đến ngày"**) |

### Module ADMIN — DOC-v1.1-01 (🚫 Blocked — không có Admin Portal, không đổi)
| REQ ID | Maps (Ref DOC) | DOC §section | Scenarios | Clarification |
|--------|----------------|--------------|-----------|---------------|
| REQ-ADMIN-001 | — | §D4 "Permission Matrix" | SC-ADMIN-001 (CARRIED) | — |

### Module MEDIA — DOC-v1.1-01 (🚫 Blocked — chưa có UI, không đổi)
| REQ ID | Maps (Ref DOC) | DOC §section | Scenarios | Clarification |
|--------|----------------|--------------|-----------|---------------|
| REQ-MEDIA-001 | — | §D3 PUP-03 | SC-MEDIA-001 (CARRIED) | — |
| REQ-MEDIA-002 | — | §D3 GPS-01 | SC-MEDIA-002 (CARRIED) | — |

### Module GENERAL — DOC-v1.1-01, DOC-v1.1-02
| REQ ID | Maps (Ref DOC) | DOC §section | Scenarios | Clarification |
|--------|----------------|--------------|-----------|---------------|
| REQ-GENERAL-001 | — | §A2 NT-02/NT-03 | SC-GENERAL-001 (CARRIED) | — |
| REQ-GENERAL-002 | — | UI DOC-v1.1-02 (không có §section BRD) | SC-GENERAL-002 (CARRIED) | — |
| REQ-GENERAL-003 | — | §D1b US-D06 (cap-5, mới); UI DOC-v1.1-02 | SC-GENERAL-003 (**MODIFIED**), SC-GENERAL-004 (CARRIED) | C-GENERAL-4 (✅ Resolved — áp dụng cả Sender lẫn Carrier) |
| REQ-GENERAL-004 | — | UI DOC-v1.1-02 (không có §section BRD) | SC-GENERAL-005 (**NEW(v1.1)**) | C-GENERAL-5 (Open — back ở màn Tặng quà không nhất quán) |

> **Cột Maps (Ref DOC):** `req_notation: none` — BRD v3.2 vẫn dùng mã ID riêng theo module (ORD-xx/CNL-xx/GIFT-xx/US-Dxx/VAL-xx) không phải hệ FR/VR thống nhất — cột này để `—`, traceability dựa vào `DOC §section` (đã kèm mã gốc BRD trong ref).

## 2. Coverage Summary
- **Scenario có REQ + DOC source:** 52/52 (100%).
- **REQ có ≥1 scenario:** 39/39 (100%).
- **REQ chưa có scenario (gap có chủ đích):** Không có.
- **Delta v1.1 so với v1.0:** 0 REQ/SC mới hoàn toàn, 0 deprecated. **13/51 SC (25%) nâng cấp CARRIED→MODIFIED** vì có thông tin đủ ảnh hưởng TC (validation cụ thể mới ở §D8, 2 UI unblock mới — Chỉnh sửa đơn + Email autofill, 1 role-bug fix — Gift history, 4 clarification mới nay đã resolve).
- **✅ Toàn bộ 4 clarification mới của v1.1 đã RESOLVED (user, 2026-07-28):**
  - **C-ORDER-2 (đảo ngược v1.0):** ngưỡng EXPIRED = **"Đến ngày"** (không phải "Từ ngày" như v1.0 từng chốt). Mở khoá SC-ORDER-007 cho generate-tc (business rule; vẫn 🚫 Blocked cho TC thật vì thiếu cơ chế backend).
  - **C-SENDER-3:** giữ 8 category Loại hàng theo UI thật; **"Thuốc/Y tế" xác nhận KHÔNG phải hàng cấm** — đóng nghi vấn P1 contradiction kế thừa từ v1.0.
  - **C-CANCEL-1:** lấy theo BRD VAL-04 (tối thiểu 5 ký tự) làm target; UI hiện tại là gap cần dev bổ sung — TC nên viết theo BRD, dự kiến FAIL trên UI hiện tại.
  - **C-GENERAL-4:** viết TC theo UI thật — "Tin mới" cap-5 áp dụng cho cả Sender lẫn Carrier.
- **🟢 1 clarification RESOLVED khác ở v1.1:** C-GIFT-2 — bug wiring role (Quà đã nhận hiện ở Receiver thay vì Carrier) đã được sửa, verify lại qua UI + Figma đều khớp Carrier.
- **🟡 1 clarification Partially Resolved (chưa hỏi lại):** C-GENERAL-3 — phần điểm số (điểm uy tín/điểm ECO) đã tự resolve (UI đã bỏ, khớp BRD); tier badge "Hạng Đồng hành" vẫn Open.
- **🚫 REQ/SC còn Blocked thật (không đổi từ v1.0):** REQ-ADMIN-001/SC-ADMIN-001, REQ-MEDIA-001..002/SC-MEDIA-001..002 (chưa có UI); REQ-ORDER-004/SC-ORDER-007 (EXPIRED, nay blocked vì thiếu cơ chế backend, KHÔNG còn vì xung đột ngưỡng).
- **REQ/SC vừa UNBLOCK ở v1.1:** REQ-SENDER-006/SC-SENDER-009..010 (email tự điền — field đã có UI). REQ-ORDER-003/SC-ORDER-005..006 (chỉnh sửa đơn) — **cập nhật 2026-07-29: đã verify sâu đầy đủ** (bấm Chỉnh sửa → wizard pre-fill đúng 2 bước → bấm Cập nhật đơn thật → lưu thành công, đồng bộ 3 màn, không thêm log LỊCH SỬ; Huỷ chỉnh sửa không lưu; nút biến mất sau khi Đã ghép, đúng OPR-10) — chuyển từ ⏳ Ready sang ✅ Confirmed, 7 TC mới trong Flow sheet (TC-FLOW-022..028).

## 3. Clarifications — Source Quote (ambiguous text)

> Trích nguyên văn đoạn mơ hồ per clarification (quoting-guide EC6). Clarification CARRIED không đổi (C-SENDER-1/2, C-CARRIER-1/2, C-ORDER-1, C-GENERAL-2) — xem đầy đủ tại `02_analyze-requirements/v1.0/requirement_traceability.md §3`. Bên dưới chỉ trích các clarification MỚI hoặc có ĐỔI TRẠNG THÁI ở v1.1 (tất cả đã Resolved).

#### C-ORDER-2 — Ngưỡng EXPIRED (✅ RESOLVED 2026-07-28 — đảo ngược v1.0)
**Source Quote (2 nguồn từng mâu thuẫn):**
> Nguồn 1 (resolution v1.0, user 2026-07-27): "sau khi qua hạn ngày Từ ngày khi tạo sẽ hết hạn tin"
> Nguồn 2 (DOC-v1.1-01 §D8.1): "Đến ngày | ... | Phải ≥ Từ ngày . Quá ngày này mà chưa ghép → tin tự chuyển trạng thái Hết hạn"
> Nguồn 3 (DOC-v1.1-01 §D8.2, lặp lại cho form OFFER): "Đến ngày | ... | Sau ngày này tin tự chuyển trạng thái Hết hạn và ngừng khớp"

**Source Location:** `DOC-v1.1-01 §D8.1` + `§D8.2` (2 vị trí độc lập, nhất quán "Đến ngày")
**Analyst Note:** BRD v3.2 nói "Đến ngày" nhất quán ở cả 2 loại form — không phải lỗi đánh máy đơn lẻ.
**Resolution (user, 2026-07-28):** "Den ngay dung" — ngưỡng chính thức = "Đến ngày". Resolution v1.0 ("Từ ngày") không dùng lại. generate-tc viết TC boundary cho SC-ORDER-007 dựa trên mốc "Đến ngày".

#### C-SENDER-3 — Danh mục "Loại hàng": 5 (BRD) hay 8 (UI)? (✅ RESOLVED 2026-07-28)
**Source Quote:**
> BRD: "Loại hàng | Có | Tài liệu | Chọn 1 trong danh mục: Tài liệu · Đồ điện tử · Thực phẩm · Quà tặng · Khác"
> UI thật (DOC-v1.1-02, quan sát trực tiếp): "Tài liệu, Đồ điện tử, Thực phẩm, Hàng nhỏ, Đồ dễ vỡ, Quần áo, Thuốc/Y tế, Khác" (8 chip)

**Source Location:** `DOC-v1.1-01 §D8.1` vs UI trực tiếp `DOC-v1.1-02`
**Resolution (user, 2026-07-28):** "van 8 loai hang nhu UI nha, thuoc/y te khong phai hang cam" — giữ 8 category theo UI, BRD 5-category KHÔNG áp dụng. **"Thuốc/Y tế" xác nhận KHÔNG phải hàng cấm** — đóng nghi vấn P1 contradiction kế thừa từ v1.0 (TC-SENDER-EP07). generate-tc viết EP cho đủ 8 category, hạ risk-flag "Thuốc/Y tế" về EP bình thường.

#### C-CANCEL-1 — Lý do huỷ: tối thiểu 5 ký tự (BRD) hay chỉ chặn rỗng (UI)? (✅ RESOLVED 2026-07-28)
**Source Quote:**
> BRD: "VAL-04: Huỷ đơn: bắt buộc nhập lý do (tối thiểu 5 ký tự) mới bật nút Xác nhận"
> UI thật (verify trực tiếp 2026-07-28): nhập "ab" (2 ký tự) → nút "Xác nhận" đã enable ngay

**Source Location:** `DOC-v1.1-01 §D8.3 VAL-04` vs UI trực tiếp `DOC-v1.1-02`
**Resolution (user, 2026-07-28):** "lay theo rule BRD nha" — target/rule đúng = BRD VAL-04 (tối thiểu 5 ký tự). UI hiện tại (chỉ chặn rỗng) là gap cần dev bổ sung. generate-tc viết Expected theo BRD — TC dự kiến FAIL trên UI hiện tại (đúng như kỳ vọng), khuyến nghị log-bug khi tới giai đoạn đó.

#### C-GENERAL-4 — "Tin mới" trên Trang chủ: chỉ Carrier hay cả Sender? (✅ RESOLVED 2026-07-28)
**Source Quote:**
> BRD: "Là Carrier, tôi muốn xem tối đa 5 tin cần gửi mới nhất ngay trên trang chủ..." (US-D06 — chỉ mô tả cho Carrier)
> UI thật (DOC-v1.1-02, quan sát trực tiếp): Trang chủ của Sender cũng có section "Tin mới" bên dưới "Đơn của tôi"

**Source Location:** `DOC-v1.1-01 §D1b US-D06` vs UI trực tiếp `DOC-v1.1-02`
**Resolution (user, 2026-07-28):** "viet theo UI luon nha" — tính năng áp dụng cho CẢ Sender lẫn Carrier. generate-tc viết TC cap-5 dùng chung cho 2 vai trò.

#### C-GIFT-2 — Vai trò hiển thị màn "Quà đã nhận" (✅ RESOLVED — bug đã fix, verify lại 2026-07-28)
**Source Quote (re-verify, không đổi so với v1.0):**
> Figma board gốc (node 23:153, connector 94:255): "Note: màng hình này nằm ở menu Cá nhân \\ Quà đã nhận" — gắn trên nhánh NGƯỜI GIAO (Carrier)

**Source Location:** Re-fetch `DOC-v1.1-03` (Figma, cùng node 23:153) + UI trực tiếp `DOC-v1.1-02`
**Analyst Note:** v1.0 quan sát bug (màn hiện nhầm ở Receiver). v1.1 verify lại: UI đã sửa, đúng ở Carrier's Cá nhân — khớp hoàn toàn với note Figma gốc (không đổi qua 2 lần đọc). Trạng thái đổi từ "Resolved qua suy luận Figma" (v1.0) sang **"Resolved — đã verify bằng chứng thực tế khớp"** (v1.1, độ tin cậy cao nhất).

#### C-GENERAL-3 — Tier/điểm uy tín/điểm ECO (🟡 Partially Resolved 2026-07-28)
**Source Quote (không đổi):**
> BRD: "Không tính điểm, không tier/xếp hạng, không CO₂..." (`DOC-v1.1-01 §A7`); cũng `§A6 USR-05`: "Hiển thị tổng số đơn đã giúp + tổng số quà ảo đã nhận (không tính điểm/CO₂)"
> UI v1.1 (DOC-v1.1-02, quan sát trực tiếp): Cá nhân Carrier hiện "12 đơn đã giúp" + "8 quà đã nhận" (KHÔNG còn "điểm uy tín"/"điểm ECO" như v1.0) NHƯNG badge tier **"Hạng Đồng hành" vẫn còn**

**Source Location:** `DOC-v1.1-01 §A6 USR-05`, `§A7` vs UI trực tiếp `DOC-v1.1-02`
**Analyst Note:** Phần số liệu điểm (điểm uy tín/điểm ECO) đã tự resolve — UI đã bỏ, khớp đúng USR-05 mới. Phần tier badge vẫn còn tồn tại, chưa khớp §A7 "không tier/xếp hạng" — vẫn Open, cần user xác nhận giữ hay bỏ tier badge.
