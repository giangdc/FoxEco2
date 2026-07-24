# MEMORY — Analyze Requirements Output — v1.0

> Tạo bởi: skill analyze-requirements
> Cập nhật lần cuối: 2026-07-24 — bổ sung ma trận nhãn nút theo trạng thái (quan sát thực tế app STG, QA GiangDC2): +4 scenario (SC-DLV-012/013/014, SC-GIFT-004), +1 requirement (REQ-GIFT-003)
> Cập nhật 2026-07-24 (bổ sung #2): thêm nguồn DOC-v1.0-04 (Fox Eco Doc, 82 ảnh Figma) — resolve C-DLV-01, C-DLV-03 (Resolved/Partially Resolved); cập nhật C-USR-01, C-GIFT-01 (Partially Resolved); cập nhật REQ-NTF-001 với nội dung thông báo verbatim chính xác cao; +1 clarification mới C-ORD-05 (2 biến thể "Đăng tin thành công" có/không "Mã tin")
> Cập nhật 2026-07-24 (bổ sung #3): QA GiangDC2 xác nhận trực tiếp trên app STG — màn Cá nhân KHÔNG có chức năng cập nhật hồ sơ (chỉ xem/view-only), khác với USR-02 mô tả "Xem/cập nhật hồ sơ" — +1 clarification mới **C-USR-03** (Resolved — xác nhận view-only), sửa lại scope REQ-USR-002/SC-USR-002
> Parent version: — version đầu tiên

## 0. Version Context
- **Version:** v1.0
- **Parent:** — (version đầu tiên)
- **Delta type:** — (N/A, INIT)
- **Input folder:** 00_input/v1.0/
- **Shared docs applied:** Không
- **Analysis mode:** INIT

## 1. Project Overview
- **Dự án:** FoxEco — mạng xã hội tương trợ nội bộ FPT Telecom, SDK/app tích hợp vào app mobile FoxPro có sẵn.
- **Mô tả:** Nền tảng kết nối CBNV nội bộ đăng tin cần gửi hàng (NEED) với đồng nghiệp tiện đường nhận mang giúp (OFFER) — mô hình tương trợ, không thu phí/không chat/không thanh toán trong app. Phạm vi v1.0 = chức năng **Gửi Hàng** (ưu tiên #1 trong bộ 3 chức năng của nền tảng) + phần Nền tảng chung (Auth/Profile, Actors, Gift, Trust & Safety).
- **Môi trường:** STG — Host app: FoxPro (mobile). Không có URL riêng (xem `07_environments/environments.md`).

## 2. Document Registry (version-scoped)
| DOC ID | File | Loại | Ngày phân tích | Status | Modules liên quan |
|--------|------|------|---------------|--------|-------------------|
| DOC-v1.0-01 | `FoxEco BRD/FoxEco BRD v3.1 (1).html` (BRD v3.1 · Tách theo chức năng, cập nhật 23/07/2026) | HTML (đã giải nén từ bundler export) | 2026-07-24 | Analyzed | USR, ORD, ASN, DLV, GIFT, CNL, NTF, TS (tất cả) |
| DOC-v1.0-02 | `FoxEco Demo 3 vai tro (standalone)/tổng hợp từ file demo.docx` (PRD — "Phân tích được xây dựng lại từ bản demo standalone") | Word (.docx) | 2026-07-24 | Analyzed | USR, ORD, ASN, DLV, GIFT, NTF (bổ trợ screen/field chi tiết) |
| DOC-v1.0-03 | `FoxEco Demo 3 vai tro (standalone)/FoxEco Demo 3 vai tro (standalone) (2).html` (Prototype tương tác 3 vai trò, JS-driven — hầu hết nội dung render runtime, không tĩnh) | HTML (bundler, JS component chưa render tĩnh) | 2026-07-24 | Analyzed (reference-only — chỉ literal `orderStatus` state map lấy được từ script `Component.renderVals()`) | ASN, DLV (state machine literal) |

**Ghi chú nguồn:** DOC-v1.0-01 và DOC-v1.0-02 (file `.html`) là dạng "bundler export" (cần giải nén script `type="__bundler/template"` để lấy HTML gốc — đã thực hiện thủ công trước khi phân tích). DOC-v1.0-02 tự mô tả (đoạn mở đầu): *"Phân tích được xây dựng lại từ bản demo standalone (3 vai trò), phục vụ chuẩn bị kiểm thử (test)"* và tự nêu giới hạn: *"⚠ Phạm vi & giới hạn của phân tích: Toàn bộ phân tích trong tài liệu này dựa trên việc thao tác trực tiếp bản demo — không có URD gốc để đối chiếu."* — vì vậy DOC-v1.0-02 được dùng làm nguồn bổ trợ (screen/field chi tiết), DOC-v1.0-01 (BRD, ngày cập nhật mới hơn) được ưu tiên làm nguồn chính khi 2 tài liệu mâu thuẫn (xem §6 Clarifications — nhiều điểm mâu thuẫn giữa BRD và prototype tham chiếu).

## 3. Module Summary
| Module | DOC Source | Tổng Req | Tổng SC | NEW | MODIFIED | CARRIED | DEPRECATED | P1 | P2 | P3 | Risk Level |
|--------|-----------|----------|---------|-----|----------|---------|-----------|----|----|----|-----------:|
| USR | DOC-v1.0-01, DOC-v1.0-02 | 5 | 5 | 5 | 0 | 0 | 0 | 1 | 3 | 1 | Medium |
| ORD | DOC-v1.0-01, DOC-v1.0-02 | 10 | 14 | 14 | 0 | 0 | 0 | 5 | 7 | 2 | High |
| ASN | DOC-v1.0-01, DOC-v1.0-02, DOC-v1.0-03 | 9 | 12 | 12 | 0 | 0 | 0 | 7 | 4 | 1 | High |
| DLV | DOC-v1.0-01, DOC-v1.0-02, DOC-v1.0-03, quan sát thực tế app | 6 | 14 | 14 | 0 | 0 | 0 | 5 | 4 | 5 | High |
| GIFT | DOC-v1.0-01, DOC-v1.0-02, quan sát thực tế app | 3 | 4 | 4 | 0 | 0 | 0 | 0 | 2 | 2 | Medium-High |
| CNL | DOC-v1.0-01, DOC-v1.0-02 | 3 | 4 | 4 | 0 | 0 | 0 | 2 | 2 | 0 | Medium |
| NTF | DOC-v1.0-01, DOC-v1.0-02 | 2 | 6 | 6 | 0 | 0 | 0 | 0 | 4 | 2 | Medium |
| TS | DOC-v1.0-01 | 2 | 3 | 3 | 0 | 0 | 0 | 0 | 2 | 1 | Medium |
| **Tổng** | | **40** | **62** | **62** | **0** | **0** | **0** | **20** | **28** | **14** | |

## 4. Scenario Index
| SC ID | Tên ngắn | Module | DOC Source | Priority | Test Type | Lifecycle | TC Status | Vibe Status | Vibe Date |
|-------|----------|--------|-----------|----------|-----------|-----------|-----------|-------------|-----------|
| SC-USR-001 | Đăng nhập SSO thành công | USR | DOC-v1.0-01 | P1 | Functional | NEW | — | — | — |
| SC-USR-002 | Xem hồ sơ cá nhân (view-only — xác nhận không có update, C-USR-03) | USR | DOC-v1.0-01 | P2 | Functional | NEW | — | — | — |
| SC-USR-003 | Hiển thị phòng ban + khu vực trên hồ sơ | USR | DOC-v1.0-01 | P2 | UI | NEW | — | — | — |
| SC-USR-004 | Hiển thị đúng 2 chỉ số (đơn giúp + quà nhận), không hiện điểm/tier/CO2 | USR | DOC-v1.0-01, DOC-v1.0-02 | P2 | Business Rule | NEW | — | — | — |
| SC-USR-005 | Cấu hình kênh liên hệ sẽ lộ | USR | DOC-v1.0-01 | P3 | Functional | NEW | — | — | — |
| SC-ORD-001 | Đăng tin NEED "Cần gửi" qua wizard 3 bước | ORD | DOC-v1.0-01, DOC-v1.0-02 | P1 | Functional | NEW | — | — | — |
| SC-ORD-002 | Đăng tin OFFER "Nhận giao hàng" (form 1 bước) | ORD | DOC-v1.0-01, DOC-v1.0-02 | P2 | Functional | NEW | — | — | — |
| SC-ORD-003 | Tin xuất hiện ở "Đơn của tôi" ngay sau đăng, không hiện mã đơn | ORD | DOC-v1.0-02 | P2 | UI | NEW | — | — | — |
| SC-ORD-004 | Timeline tin ghi nhận đầy đủ mốc thời gian | ORD | DOC-v1.0-01 | P1 | Functional | NEW | — | — | — |
| SC-ORD-005 | Tin tự động "Hết hạn" khi quá thời gian không ai ghép | ORD | DOC-v1.0-01, DOC-v1.0-02 | P1 | Business Rule | NEW | — | — | — |
| SC-ORD-006 | Không tick điều khoản → chặn đăng tin (Bước 3) | ORD | DOC-v1.0-01 | P2 | Business Rule | NEW | — | — | — |
| SC-ORD-007 | [Gap] Bỏ trống Loại hàng/Giá trị Bước 1 vẫn qua Bước 2 | ORD | DOC-v1.0-02 | P3 | Business Rule | NEW | — | — | — |
| SC-ORD-008 | Chỉnh sửa tin khi đang "Chờ ghép" | ORD | DOC-v1.0-01, DOC-v1.0-02 | P2 | Functional | NEW | — | — | — |
| SC-ORD-009 | Khoá chỉnh sửa khi đã "Đã ghép" trở đi | ORD | DOC-v1.0-01, DOC-v1.0-02 | P1 | Business Rule | NEW | — | — | — |
| SC-ORD-010 | Chọn nhanh 1 trong 6 văn phòng preset FPT | ORD | DOC-v1.0-01 | P3 | UI | NEW | — | — | — |
| SC-ORD-011 | Email công ty người nhận có trong hệ thống → tự điền | ORD | DOC-v1.0-01, DOC-v1.0-02 | P2 | Functional | NEW | — | — | — |
| SC-ORD-012 | Email công ty người nhận không có → báo nhập thủ công | ORD | DOC-v1.0-01, DOC-v1.0-02 | P2 | Business Rule | NEW | — | — | — |
| SC-ORD-013 | Giá trị hàng vượt ngưỡng → cảnh báo nên mua bảo hiểm | ORD | DOC-v1.0-01 | P2 | Business Rule | NEW | — | — | — |
| SC-ORD-014 | Đăng tin chứa hàng cấm → hệ thống chặn | ORD | DOC-v1.0-01 | P1 | Business Rule | NEW | — | — | — |
| SC-ASN-001 | Carrier bấm "Tôi mang giúp được" → gửi đề nghị | ASN | DOC-v1.0-01, DOC-v1.0-02 | P1 | Functional | NEW | — | — | — |
| SC-ASN-002 | Ghép ngay khi Carrier nhận (không cần chủ tin duyệt) → MATCHED + lộ SĐT | ASN | DOC-v1.0-01, DOC-v1.0-02 | P1 | Business Rule | NEW | — | — | — |
| SC-ASN-003 | Trước khi ghép, SĐT KHÔNG lộ | ASN | DOC-v1.0-01, DOC-v1.0-02 | P1 | Business Rule | NEW | — | — | — |
| SC-ASN-004 | 2 Carrier cùng bấm nhận gần đồng thời → chỉ 1 người ghép (chống double-accept) | ASN | DOC-v1.0-01 | P1 | Business Rule | NEW | — | — | — |
| SC-ASN-005 | Tin ẩn khỏi Bảng tin sau khi có người ghép | ASN | DOC-v1.0-01 | P1 | Business Rule | NEW | — | — | — |
| SC-ASN-006 | Hệ thống tự khớp tuyến OFFER với tin NEED trùng điểm lấy/giao | ASN | DOC-v1.0-01, DOC-v1.0-02 | P1 | Functional | NEW | — | — | — |
| SC-ASN-007 | Carrier bấm "Nhận giao" từ thông báo khớp tuyến → MATCHED | ASN | DOC-v1.0-01, DOC-v1.0-02 | P2 | Functional | NEW | — | — | — |
| SC-ASN-008 | Carrier chỉ nhận tối đa 5 tin gợi ý cùng lúc | ASN | DOC-v1.0-01 | P3 | Business Rule | NEW | — | — | — |
| SC-ASN-009 | Tin không trùng điểm lấy/giao hoặc khung giờ không giao nhau → không gợi ý | ASN | DOC-v1.0-01 | P2 | Business Rule | NEW | — | — | — |
| SC-ASN-010 | Gợi ý ưu tiên theo độ gần tuyến rồi thời gian đăng mới nhất | ASN | DOC-v1.0-01 | P2 | Business Rule | NEW | — | — | — |
| SC-ASN-011 | Không tự khớp tin của chính mình | ASN | DOC-v1.0-01 | P1 | Business Rule | NEW | — | — | — |
| SC-ASN-012 | Tin huỷ bởi Carrier (chưa lấy hàng) quay lại "Chờ ghép" và được khớp lại | ASN | DOC-v1.0-01 | P2 | Business Rule | NEW | — | — | — |
| SC-DLV-001 | Carrier chụp ảnh hàng lúc nhận (tuỳ chọn) → lưu, gắn timeline | DLV | DOC-v1.0-01 | P2 | Functional | NEW | — | — | — |
| SC-DLV-002 | Bỏ qua chụp ảnh lúc nhận vẫn chuyển trạng thái được | DLV | DOC-v1.0-01 | P3 | Business Rule | NEW | — | — | — |
| SC-DLV-003 | Carrier bật chia sẻ vị trí khi đang giao | DLV | DOC-v1.0-01 | P3 | Functional | NEW | — | — | — |
| SC-DLV-004 | Vị trí chia sẻ tự tắt/xoá sau khi đơn đóng | DLV | DOC-v1.0-01 | P3 | Business Rule | NEW | — | — | — |
| SC-DLV-005 | Nút "Xác nhận đã nhận hàng" chỉ kích hoạt khi = Đã giao | DLV | DOC-v1.0-01, DOC-v1.0-02 | P1 | Business Rule | NEW | — | — | — |
| SC-DLV-006 | Nút hành động Carrier bị động ở trạng thái trước "Đã giao" | DLV | DOC-v1.0-02 | P1 | Business Rule | NEW | — | — | — |
| SC-DLV-007 | Quá N giờ chưa xác nhận nhận hàng → nhắc → admin hỗ trợ | DLV | DOC-v1.0-01 | P2 | Business Rule | NEW | — | — | — |
| SC-DLV-008 | (Tuỳ chọn) Ghi nhận chi phí đối soát offline, không qua app | DLV | DOC-v1.0-01 | P3 | Functional | NEW | — | — | — |
| SC-DLV-009 | Sau khi đã lấy hàng (IN_TRANSIT), huỷ thường bị chặn → chỉ tạo được sự cố | DLV | DOC-v1.0-01 | P2 | Business Rule | NEW | — | — | — |
| SC-DLV-010 | Không thể bấm "Đã giao" trước khi bấm "Tôi đã lấy hàng" | DLV | DOC-v1.0-01 | P1 | Business Rule | NEW | — | — | — |
| SC-DLV-011 | Người nhận xác nhận → đơn "Hoàn thành" ngay lập tức | DLV | DOC-v1.0-01, DOC-v1.0-02 | P1 | Functional | NEW | — | — | — |
| SC-DLV-012 | Nhãn nút Sender/Receiver đúng theo trạng thái Đã ghép/Đang giao | DLV | Quan sát thực tế app | P2 | UI | NEW | — | — | — |
| SC-DLV-013 | Tại "Đã giao": Sender/Carrier disable, chỉ Receiver enable | DLV | Quan sát thực tế app | P1 | Business Rule | NEW | — | — | — |
| SC-DLV-014 | Carrier/Receiver thấy nhãn "Đơn đã hoàn thành" sau Hoàn thành | DLV | Quan sát thực tế app | P3 | UI | NEW | — | — | — |
| SC-GIFT-001 | Sau Hoàn thành, Sender chọn 1/4 loại quà tặng Carrier | GIFT | DOC-v1.0-01, DOC-v1.0-02 | P2 | Functional | NEW | — | — | — |
| SC-GIFT-002 | Gửi quà không cần Carrier xác nhận → popup cảm ơn | GIFT | DOC-v1.0-01, DOC-v1.0-02 | P3 | Functional | NEW | — | — | — |
| SC-GIFT-003 | Carrier xem lịch sử/số lượng quà đã nhận theo loại | GIFT | DOC-v1.0-01, DOC-v1.0-02 | P3 | UI | NEW | — | — | — |
| SC-GIFT-004 | Nút "Cảm ơn người vận chuyển" đổi thành "Bạn đã đánh giá" sau khi gửi quà | GIFT | Quan sát thực tế app | P2 | Functional | NEW | — | — | — |
| SC-CNL-001 | Huỷ đơn ở POSTED/MATCHED → popup bắt buộc nhập lý do | CNL | DOC-v1.0-01, DOC-v1.0-02 | P1 | Business Rule | NEW | — | — | — |
| SC-CNL-002 | Không cho huỷ khi đơn đã "Đang giao" trở đi | CNL | DOC-v1.0-01 | P1 | Business Rule | NEW | — | — | — |
| SC-CNL-003 | Đơn huỷ ghi rõ vai trò người huỷ + lý do, đồng bộ realtime 3 bên | CNL | DOC-v1.0-01, DOC-v1.0-02 | P2 | Business Rule | NEW | — | — | — |
| SC-CNL-004 | Carrier huỷ khi "Đã ghép" (chưa lấy hàng) → đơn về "Chờ ghép" | CNL | DOC-v1.0-01 | P2 | Business Rule | NEW | — | — | — |
| SC-NTF-001 | Thông báo khi ghép ngay (NTF-01/02) | NTF | DOC-v1.0-01 | P2 | Functional | NEW | — | — | — |
| SC-NTF-002 | Thông báo khi khớp tuyến OFFER (NTF-03) | NTF | DOC-v1.0-01 | P2 | Functional | NEW | — | — | — |
| SC-NTF-003 | Thông báo theo mốc vận chuyển: lấy hàng/đã giao/hoàn tất (NTF-04/05/06) | NTF | DOC-v1.0-01 | P2 | Functional | NEW | — | — | — |
| SC-NTF-004 | Thông báo khi nhận quà cảm ơn (NTF-07) | NTF | DOC-v1.0-01 | P3 | Functional | NEW | — | — | — |
| SC-NTF-005 | Thông báo khi đơn huỷ (NTF-08) và tin quá hạn (NTF-09) | NTF | DOC-v1.0-01 | P2 | Functional | NEW | — | — | — |
| SC-NTF-006 | Carrier bị giới hạn trần thông báo khớp/ngày | NTF | DOC-v1.0-01 | P3 | Business Rule | NEW | — | — | — |
| SC-TS-001 | Mọi tương tác được ghi log đầy đủ mốc thời gian | TS | DOC-v1.0-01 | P2 | Functional | NEW | — | — | — |
| SC-TS-002 | Log tương tác không thể sửa/xoá sau khi ghi | TS | DOC-v1.0-01 | P2 | Business Rule | NEW | — | — | — |
| SC-TS-003 | Admin can thiệp hỗ trợ dựa trên log khi có vướng mắc | TS | DOC-v1.0-01 | P3 | Functional | NEW | — | — | — |

### 4.1. Source Detail (verbatim quotes — mandatory per `references/quoting-guide.md`)

> 1 block per REQ. Scenario quotes (Given/When/Then justification) ở `test_scenario_map.md`; mỗi SC trace về REQ tương ứng (xem `requirement_traceability.md`).

#### REQ-USR-001 — Đăng nhập SSO nội bộ

**Source Quote:**
> "USR-01 Đăng nhập SSO nội bộ FPT → JWT, role, profile"

**Source Location:** `DOC-v1.0-01 §A6 "Actors & Hồ sơ (chung)" · bảng "Tài khoản & Hồ sơ (USR)" · row USR-01`

**Analyst Note:** Đăng nhập qua SSO nội bộ FPT (không có form đăng nhập username/password riêng trong app FoxEco), trả về JWT + role + profile. Liên hệ NT-07 (§A2): *"Định danh & tin cậy — SSO; hiển thị phòng ban, đánh giá, tier để hai bên tự cân nhắc"* — cụm "đánh giá, tier" ở đây mâu thuẫn với A7/A8 (xem C-USR-01, C-GIFT-01).

#### REQ-USR-002 — Xem hồ sơ cá nhân (view-only — xem C-USR-03)

**Source Quote:**
> "USR-02 Xem/cập nhật hồ sơ: tên, SĐT, avatar, phòng ban, khu vực/văn phòng, kênh liên hệ"

**Source Location:** `DOC-v1.0-01 §A6 "Actors & Hồ sơ (chung)" · bảng "Tài khoản & Hồ sơ (USR)" · row USR-02`

**Source Quote (Quan sát thực tế app STG, QA GiangDC2, 2026-07-24):**
> Màn Cá nhân trên app STG thật KHÔNG có chức năng cập nhật/sửa hồ sơ — toàn bộ 6 trường (tên, SĐT, avatar, phòng ban, khu vực/văn phòng, kênh liên hệ) chỉ ở dạng xem (view-only), không có form/nút "Chỉnh sửa" nào.

**Source Location:** Quan sát trực tiếp app STG (QA GiangDC2, 2026-07-24)

**Analyst Note:** BRD (USR-02) mô tả "Xem/cập nhật hồ sơ" nhưng QA xác nhận trực tiếp trên app STG: KHÔNG tồn tại chức năng cập nhật nào — toàn bộ 6 trường chỉ hiển thị (view-only). Sửa lại scope REQ-USR-002/SC-USR-002 thành "Xem hồ sơ cá nhân" (bỏ nhánh "cập nhật"). Xem **C-USR-03 (Resolved)**.

#### REQ-USR-003 — Hiển thị phòng ban + khu vực/tỉnh

**Source Quote:**
> "USR-04 Hiển thị phòng ban + khu vực/tỉnh (tin cậy + ghép địa lý)"

**Source Location:** `DOC-v1.0-01 §A6 "Actors & Hồ sơ (chung)" · bảng "Tài khoản & Hồ sơ (USR)" · row USR-04`

**Analyst Note:** Phòng ban + khu vực/tỉnh phục vụ 2 mục đích: hiển thị tin cậy (trust signal) và làm điều kiện ghép theo địa lý (NT-06). Đối chiếu demo: nhân vật "Đồng Công Chí Linh · Phòng Kỹ thuật · MNV: FTEL2291" — phòng ban hiển thị dưới dạng text cạnh tên trong header/card liên hệ (DOC-v1.0-02 §3.1, §Header Table 2).

#### REQ-USR-004 — Hiển thị tổng đơn đã giúp + tổng quà ảo nhận (không tính điểm/CO₂)

**Source Quote #1:**
> "USR-05 Hiển thị tổng số đơn đã giúp + tổng số quà ảo đã nhận (không tính điểm/CO₂)"

**Source Location #1:** `DOC-v1.0-01 §A6 "Actors & Hồ sơ (chung)" · bảng "Tài khoản & Hồ sơ (USR)" · row USR-05`

**Source Quote #2:**
> "Trang cá nhân tổng hợp tổng số đơn đã giúp + số quà ảo đã nhận (đếm theo loại) + lịch sử nhận quà — Không tính điểm, không tier/xếp hạng, không CO₂, không quy đổi tiền / thanh toán in-app"

**Source Location #2:** `DOC-v1.0-01 §A7 "Phần thưởng — Quà ảo"`

**Analyst Note:** BRD khẳng định RÕ 2 lần (USR-05 và A7) rằng Trang cá nhân v1.0 CHỈ hiện 2 chỉ số (tổng đơn đã giúp, tổng quà đã nhận) — không điểm, không tier, không CO₂. Tuy nhiên demo/prototype tham chiếu (DOC-v1.0-02 §3.9, Table 10) lại hiển thị "Hạng Đồng hành" (tier) + "Điểm uy tín (4.8)" + "Điểm ECO (540)" — mâu thuẫn trực tiếp với BRD hiện hành. Xem **C-USR-01 (BLOCKER)**.

#### REQ-USR-005 — Cấu hình kênh liên hệ sẽ lộ

**Source Quote:**
> "USR-07 Cấu hình kênh liên hệ sẽ lộ: SĐT (bắt buộc), Workplace/email (tùy chọn)"

**Source Location:** `DOC-v1.0-01 §A6 "Actors & Hồ sơ (chung)" · bảng "Tài khoản & Hồ sơ (USR)" · row USR-07`

**Analyst Note:** SĐT bắt buộc lộ khi ghép; Workplace/email tuỳ chọn bật thêm. Chưa rõ UI cấu hình cụ thể (toggle ở đâu) — cả 2 doc không có màn hình minh hoạ; generate-tc test ở mức business rule (SĐT luôn lộ, email theo cấu hình) hơn là UI cụ thể.

#### REQ-ORD-001 — Đăng tin gửi hàng NEED/OFFER

**Source Quote:**
> "ORD-01 Đăng tin gửi hàng (NEED/OFFER) — NEED: mô tả, ảnh tùy chọn, điểm lấy/giao, giá trị, loại hàng, khung giờ, người nhận. OFFER: điểm xuất phát→đến, khung giờ, tên/SĐT — không công khai lên bảng tin"

**Source Location:** `DOC-v1.0-01 §D3 "Functional Requirements — Gửi Hàng" · row ORD-01`

**Analyst Note:** 2 chiều đăng tin khác field: NEED (7 trường, hiển thị công khai bảng tin) vs OFFER (4 trường, KHÔNG công khai — chỉ lưu chờ hệ thống tự khớp, xem REQ-ASN-004). Đối chiếu bảng D1 (§D1): *"NEED 'Tôi cần gửi' SENDER Món hàng, điểm lấy, điểm giao, khung giờ, người nhận CARRIER thuận đường 'Tôi mang giúp được' — OFFER 'Tôi nhận giao hàng' CARRIER Điểm xuất phát → điểm đến, khung giờ, tên & SĐT (tuyến không công khai lên bảng tin) Hệ thống tự khớp"*.

#### REQ-ORD-002 — Wizard đăng tin ngắn 3 bước

**Source Quote:**
> "ORD-02 Wizard đăng tin ngắn — B1 Loại tin+hàng → B2 Địa điểm/lộ trình+thời gian → B3 Xác nhận + đồng ý điều khoản"

**Source Location:** `DOC-v1.0-01 §D3 "Functional Requirements — Gửi Hàng" · row ORD-02`

**Analyst Note:** Wizard 3 bước áp dụng cho chiều NEED. Chiều OFFER dùng **form 1 màn duy nhất** (không phải wizard) theo US-D10: *"Màn đăng tin OFFER 1 màn duy nhất, các trường: Điểm xuất phát, Điểm đến, Khung giờ, Tên, SĐT + tick đồng ý điều khoản"* — khớp với DOC-v1.0-02 §4.4: *"Form đăng ký lịch trình di chuyển (1 bước, không phải wizard)"*. Đối chiếu B1/B2/B3 nội dung xem Block Definitions ở `test_scenario_map.md`.

#### REQ-ORD-003 — Tin có timeline trạng thái

**Source Quote:**
> "ORD-04 Tin có timeline trạng thái — Lịch sử đầy đủ với timestamp"

**Source Location:** `DOC-v1.0-01 §D3 "Functional Requirements — Gửi Hàng" · row ORD-04`

**Analyst Note:** Mọi tin ghi lịch sử đầy đủ kèm timestamp mỗi lần đổi trạng thái. Liên hệ Table 9 (DOC-v1.0-02 §3.6): *"Lịch sử | Timeline mốc sự kiện: Đăng tin → Ghép thành công → Lấy hàng → Đã giao → Hoàn thành"* — đây là hiển thị cụ thể của yêu cầu ORD-04 trên màn Theo dõi đơn.

#### REQ-ORD-004 — Tin hết hạn tự động

**Source Quote #1:**
> "ORD-06 Tin hết hạn — Quá hạn chưa ghép → gửi thông báo để người đăng tự gỡ/đăng lại ; hệ thống không tự can thiệp ở phase này"

**Source Location #1:** `DOC-v1.0-01 §D3 "Functional Requirements — Gửi Hàng" · row ORD-06`

**Source Quote #2:**
> "US-D04 Là Sender, tôi muốn tin tự động chuyển trạng thái 'Hết hạn' và quay về mục Đơn của tôi nếu quá thời gian không ai nhận mang giúp... Quá hạn cấu hình mà chưa MATCHED → tự chuyển EXPIRED, hiển thị badge 'Hết hạn' ở tab hoàn tất kèm lý do 'Không có ai nhận mang giúp trong thời gian đăng'"

**Source Location #2:** `DOC-v1.0-01 §D1b "User Story — Gửi Hàng" · Nhóm 1 · US-D04`

**Analyst Note:** ⚠️ Mâu thuẫn nhẹ: ORD-06 nói hệ thống "không tự can thiệp" (chỉ gửi thông báo, người đăng tự gỡ/đăng lại) nhưng US-D04 AC nói tin "TỰ chuyển EXPIRED" (hệ thống tự đổi trạng thái). Suy luận hợp lý: hệ thống TỰ đổi trạng thái tin → EXPIRED (US-D04, đây là hành vi UI quan sát được) nhưng KHÔNG tự động xoá/gỡ tin hay tạo hành động thay người dùng (ORD-06) — 2 quote mô tả 2 khía cạnh không thực sự loại trừ nhau, không cần Clarification riêng. Hạn tin mặc định (giá trị "quá hạn cấu hình" là bao nhiêu) chưa xác định — xem **C-ORD-03**.

#### REQ-ORD-005 — Consent điều khoản trước khi đăng

**Source Quote:**
> "ORD-09 Consent điều khoản trước khi đăng — Bắt buộc tick 'đồng ý tự chịu trách nhiệm'"

**Source Location:** `DOC-v1.0-01 §D3 "Functional Requirements — Gửi Hàng" · row ORD-09`

**Analyst Note:** Checkbox bắt buộc tick trước khi đăng, đối chiếu Table 8 (DOC-v1.0-02 §3.5.3): *"Checkbox điều khoản | Mặc định đã tick sẵn — 'Tôi tự chịu trách nhiệm về hàng hoá và thoả thuận với người mang giúp'"* — demo cho thấy checkbox **mặc định đã tick sẵn** (pre-checked), khác hành vi "bắt buộc user tự tick". Non-blocking — cả 2 đều thoả điều kiện "có tick mới đăng được"; generate-tc test cả nhánh untick→chặn.

#### REQ-ORD-006 — Chỉnh sửa tin chỉ khi "Chờ ghép"

**Source Quote #1:**
> "ORD-10 Chỉnh sửa tin khi 'Chờ ghép' — Form điền sẵn; chỉ trạng thái POSTED; có 'Cập nhật' & 'Huỷ chỉnh sửa'"

**Source Location #1:** `DOC-v1.0-01 §D3 "Functional Requirements — Gửi Hàng" · row ORD-10`

**Source Quote #2:**
> "BR-EDIT-01 Chỉ được chỉnh sửa tin khi còn 'Chờ ghép' (POSTED); đã MATCHED trở đi khoá chỉnh sửa"

**Source Location #2:** `DOC-v1.0-01 §D4 "Business Rules & Permission Matrix" · row BR-EDIT-01`

**Source Quote #3:**
> "OPR-10 Điều kiện chỉnh sửa đơn — Chỉ được sửa đơn khi chưa có ai nhận (trạng thái 'Chờ ghép'); ngay khi đã có người nhận (Đã ghép trở đi) → khoá chỉnh sửa hoàn toàn"

**Source Location #3:** `DOC-v1.0-01 §D7 "Rule vận hành (Operating Rules)" · row OPR-10`

**Analyst Note:** 3 nguồn đồng nhất mô tả cùng 1 rule (edit chỉ khi POSTED). Khớp US-D19 AC: *"Nút 'Chỉnh sửa' chỉ hiện ở trạng thái Chờ ghép (POSTED); mở màn giống tạo đơn nhưng đã điền sẵn; có nút 'Cập nhật' & 'Huỷ chỉnh sửa'; sau IN_TRANSIT không cho sửa"* (§D1b Nhóm 1 US-D19) — lưu ý US-D19 nói "sau IN_TRANSIT" trong khi ORD-10/BR-EDIT-01/OPR-10 đều nói khoá ngay từ MATCHED — MATCHED xảy ra TRƯỚC IN_TRANSIT trong flow, nên "khoá từ MATCHED" là điều kiện chặt hơn/đúng hơn theo đa số nguồn; test theo mốc MATCHED.

#### REQ-ORD-007 — Quick-select văn phòng FPT

**Source Quote:**
> "LOC-03 Quick-select văn phòng FPT — Hiển thị preset 6 văn phòng (+ mở rộng theo tỉnh)"

**Source Location:** `DOC-v1.0-01 §D3 "Functional Requirements — Gửi Hàng" · row LOC-03`

**Analyst Note:** 6 văn phòng preset cụ thể (tên) không được liệt kê trong doc — cần xác nhận danh sách thật khi vibe-test/automation (giống lưu ý "master data" ở `test_data_catalog.md`). Không có trong demo (demo chỉ nhập địa chỉ tự do ở Bước 2/3, không thấy quick-select) — REQ này CHƯA có bằng chứng UI cụ thể, chỉ có trong BRD.

#### REQ-ORD-008 — Tự điền người nhận từ email công ty

**Source Quote #1:**
> "USR-EML Tự điền người nhận từ email công ty — Tra danh bạ nội bộ; khớp → tự điền tên/SĐT/địa chỉ; không khớp → nhập tay"

**Source Location #1:** `DOC-v1.0-01 §D3 "Functional Requirements — Gửi Hàng" · row USR-EML`

**Source Quote #2:**
> "US-D18 Là Sender, tôi muốn nhập email công ty của người nhận để hệ thống tự điền tên, SĐT và địa chỉ từ danh bạ nội bộ, để khỏi gõ tay và tránh sai thông tin. Ô 'Email công ty người nhận' nằm đầu mục Người nhận; nhập email có trong hệ thống → tự điền tên/SĐT/địa chỉ + báo 'Đã tìm thấy trong hệ thống nội bộ'; không có → báo 'Không tìm thấy · nhập thủ công'"

**Source Location #2:** `DOC-v1.0-01 §D1b "User Story — Gửi Hàng" · Nhóm 1 · US-D18`

**Analyst Note:** Ô Email công ty nằm ĐẦU mục Người nhận (trước Tên/SĐT/Địa chỉ). 2 nhánh rõ ràng: match → auto-fill 3 trường + message xác nhận; no-match → message + cho nhập tay. Đối chiếu Table 7 (DOC-v1.0-02 §3.5.2) mô tả mục Người nhận nhập tay — chưa thấy field Email công ty trong bảng field liệt kê ở demo gốc, nghĩa là đây là tính năng MỚI hơn bản demo (BRD bổ sung sau, chưa có trong prototype tham chiếu) — không phải mâu thuẫn, chỉ là delta hợp lý giữa demo (cũ) và BRD hiện hành (mới hơn).

#### REQ-ORD-009 — Ngưỡng giá trị hàng & cảnh báo bảo hiểm

**Source Quote:**
> "BR-ORD-03 Giá trị hàng trong ngưỡng cấu hình; trên ngưỡng → cảnh báo nên mua bảo hiểm (phase sau)"

**Source Location:** `DOC-v1.0-01 §D4 "Business Rules & Permission Matrix" · row BR-ORD-03`

**Analyst Note:** Ngưỡng giá trị hàng cụ thể (số tiền) CHƯA xác định — chính BRD tự liệt kê đây là câu hỏi mở: *"Câu hỏi mở cho BA — Ngưỡng giá trị hàng? Ảnh bắt buộc cho hàng > ngưỡng?"* (§D5). Xem **C-ORD-02 (BLOCKER)** — generate-tc không thể viết BVA cho ngưỡng khi chưa có con số.

#### REQ-ORD-010 — Hàng cấm không được đăng

**Source Quote #1:**
> "BR-ORD-04 Hàng cấm không được đăng"

**Source Location #1:** `DOC-v1.0-01 §D4 "Business Rules & Permission Matrix" · row BR-ORD-04`

**Source Quote #2:**
> "Cấm gửi: thuốc, vũ khí, chất nguy hiểm, hàng phi pháp. FoxEco là nền tảng kết nối, không chịu trách nhiệm về nội dung hàng."

**Source Location #2:** `DOC-v1.0-02 §1.4 "Nguyên tắc cốt lõi"`

**Analyst Note:** Danh mục cấm cụ thể (4 loại: thuốc, vũ khí, chất nguy hiểm, hàng phi pháp) lấy từ docx §1.4, khớp banner cảnh báo Table 8 (§3.5.3): *"Banner cảnh báo | 'Không được gửi: thuốc, vũ khí, chất nguy hiểm, hàng phi pháp...'"*. Cơ chế CHẶN (block đăng) hay chỉ CẢNH BÁO (banner, không validate field Loại hàng) — demo hiện tại chỉ có banner tĩnh, KHÔNG có validate chặn theo Loại hàng đã chọn ở Bước 1 (Loại hàng là chip chọn cố định: Tài liệu/Đồ điện tử/Thực phẩm/Hàng nhỏ/Đồ dễ vỡ/Quần áo/Thuốc-Y tế/Khác — "Thuốc/Y tế" vẫn là 1 lựa chọn hợp lệ trong chip, mâu thuẫn với "cấm gửi thuốc"). Xem **C-ORD-04**.

#### REQ-ASN-001 — Bày tỏ quan tâm/đề nghị mang giúp

**Source Quote:**
> "ASN-01 Bày tỏ quan tâm / đề nghị mang giúp — Gửi tới chủ tin push + in-app"

**Source Location:** `DOC-v1.0-01 §D3 "Functional Requirements — Gửi Hàng" · row ASN-01`

**Analyst Note:** Khớp US-D07: *"Là Carrier, tôi muốn bấm 'Tôi mang giúp được' ngay tại thẻ tin hoặc màn chi tiết... Đề nghị gửi push + in-app tới Sender; trạng thái tin cập nhật chờ chấp nhận"* (§D1b Nhóm 2). Lưu ý: câu "trạng thái tin cập nhật chờ chấp nhận" (US-D07) có vẻ ngụ ý có bước DUYỆT của chủ tin, nhưng BR-CON-01 (REQ-ASN-002) lại nói ghép NGAY không cần duyệt — xem phân tích ở REQ-ASN-002.

#### REQ-ASN-002 — Ghép ngay khi chấp nhận + lộ liên hệ

**Source Quote #1:**
> "ASN-02 Chủ tin chấp nhận 1 người — MATCHED + lộ liên hệ"

**Source Location #1:** `DOC-v1.0-01 §D3 "Functional Requirements — Gửi Hàng" · row ASN-02`

**Source Quote #2:**
> "BR-CON-01 Người B bấm 'Tôi mang giúp được' → hệ thống ghép ngay, không cần bước chủ tin duyệt — BR-CON-02 Sau khi ghép: lộ SĐT + kênh liên hệ cho đúng 2 người trong cặp ghép; trước khi ghép không lộ SĐT"

**Source Location #2:** `DOC-v1.0-01 §A5 "Tương tác 2 chiều & Cơ chế kết nối"`

**Analyst Note:** ⚠️ Mâu thuẫn nội bộ BRD: cột "Người ghép" chủ tin chấp nhận 1 người" (ASN-02, D3) hàm ý có bước DUYỆT của Sender, nhưng BR-CON-01 (A5) nói rõ "ghép ngay, KHÔNG cần bước chủ tin duyệt". Demo/docx khớp với BR-CON-01 hơn (§4.2: *"Bấm 'Tôi mang giúp được' → hiện modal xác nhận... Bấm Xác nhận → đơn chuyển trạng thái 'Đã ghép'"* — chỉ 1 bước xác nhận từ chính Carrier, không thấy bước Sender duyệt riêng). Ưu tiên BR-CON-01/02 + docx làm chuẩn test (ghép ngay khi Carrier tự xác nhận), ghi nhận cách gọi "chủ tin chấp nhận" ở ASN-02 có thể chỉ là cách diễn đạt khác cho "modal Carrier tự confirm" chứ không phải bước duyệt riêng của Sender — non-blocking, không tạo Clarification riêng (đã đủ rõ qua đối chiếu 3 nguồn).

#### REQ-ASN-003 — Chống ghép trùng (1 tin chỉ 1 cặp active)

**Source Quote #1:**
> "ASN-03 Chống ghép trùng — 1 tin chỉ 1 cặp active (DB constraint + tx lock)"

**Source Location #1:** `DOC-v1.0-01 §D3 "Functional Requirements — Gửi Hàng" · row ASN-03`

**Source Quote #2:**
> "OPR-03 1 tin — 1 cặp ghép — Ghép ngay cho người bấm 'Tôi mang giúp được' đầu tiên; ngay khi có người nhận, tin bị ẩn khỏi bảng tin và không ai bấm 'Tôi mang giúp được' được nữa (chống double-accept)"

**Source Location #2:** `DOC-v1.0-01 §D7 "Rule vận hành (Operating Rules)" · row OPR-03`

**Analyst Note:** Cơ chế: người bấm ĐẦU TIÊN thắng (first-come), backend dùng DB constraint + transaction lock chống race condition khi 2 người bấm gần như đồng thời. Ngay sau ghép, tin ẩn khỏi Bảng tin (liên hệ REQ-ASN-005/009).

#### REQ-ASN-004 — Tự động khớp tuyến OFFER↔NEED

**Source Quote #1:**
> "MTCH-01 Tự khớp tuyến OFFER ↔ NEED — Trùng điểm lấy & điểm giao → đẩy thông báo cho Carrier duyệt 'Nhận giao'"

**Source Location #1:** `DOC-v1.0-01 §D3 "Functional Requirements — Gửi Hàng" · row MTCH-01`

**Source Quote #2:**
> "BR-MTCH-01 OFFER khớp NEED khi trùng điểm lấy & điểm giao; tuyến OFFER không hiển thị công khai"

**Source Location #2:** `DOC-v1.0-01 §D4 "Business Rules & Permission Matrix" · row BR-MTCH-01`

**Analyst Note:** Khác với chiều NEED→ASN (Carrier chủ động bấm nhận), chiều OFFER là hệ thống CHỦ ĐỘNG tìm & đẩy thông báo, Carrier chỉ "duyệt" (không phải tự tìm). Khớp US-D12/US-D13 (§D1b Nhóm 3): hệ thống đẩy thông báo "Tìm thấy đơn hàng phù hợp tuyến của bạn" → Carrier bấm "Nhận giao" tại chi tiết tin → MATCHED.

#### REQ-ASN-005 — Trần số tin gợi ý cho 1 carrier

**Source Quote:**
> "OPR-01 Trần số tin gợi ý cho 1 carrier — Mỗi người vận chuyển chỉ nhận thông báo tối đa 5 tin cần gửi phù hợp (mới & gần tuyến nhất); tránh làm phiền/spam"

**Source Location:** `DOC-v1.0-01 §D7 "Rule vận hành (Operating Rules)" · row OPR-01`

**Analyst Note:** Trần 5 tin/carrier, ưu tiên mới & gần tuyến nhất khi vượt trần. Khớp US-D06 (Trang chủ hiển thị đúng 5 tin mới nhất, "Xem thêm trên Bảng tin" khi còn tin khác) — lưu ý US-D06 mô tả UI Trang chủ (hiển thị tối đa 5), còn OPR-01 mô tả giới hạn THÔNG BÁO — có thể là 2 cơ chế riêng (UI cap khác notification cap) nhưng cùng con số 5, khả năng cao là cùng 1 rule diễn đạt ở 2 chỗ khác nhau.

#### REQ-ASN-006 — Điều kiện khớp: trùng điểm lấy/giao + khung giờ giao nhau

**Source Quote:**
> "OPR-02 Điều kiện khớp — Chỉ khớp khi trùng điểm lấy & điểm giao (cùng khu vực/tuyến) và giao nhau về khung giờ"

**Source Location:** `DOC-v1.0-01 §D7 "Rule vận hành (Operating Rules)" · row OPR-02`

**Analyst Note:** 2 điều kiện AND: (1) trùng điểm lấy & giao (cùng khu vực/tuyến), (2) khung giờ giao nhau (không cần trùng tuyệt đối, chỉ cần overlap). Định nghĩa chính xác "cùng khu vực/tuyến" (bán kính bao nhiêu km?) CHƯA rõ — BRD tự nêu: *"Chờ BA bổ sung: bán kính/định nghĩa 'cùng tuyến', độ lệch khung giờ cho phép..."* (§D7). Xem **C-NTF-02**.

#### REQ-ASN-007 — Ưu tiên gợi ý theo độ gần & thời gian đăng

**Source Quote:**
> "OPR-04 Ưu tiên gợi ý — Sắp xếp theo độ gần tuyến → thời gian đăng (mới trước); tin quá hạn loại khỏi luồng khớp"

**Source Location:** `DOC-v1.0-01 §D7 "Rule vận hành (Operating Rules)" · row OPR-04`

**Analyst Note:** Thứ tự ưu tiên 2 tầng: (1) độ gần tuyến trước, (2) mới đăng trước (tie-breaker). Tin EXPIRED tự động loại khỏi pool khớp — liên hệ REQ-ORD-004.

#### REQ-ASN-008 — Không tự khớp với chính mình

**Source Quote:**
> "OPR-05 Không tự khớp với chính mình — Không gợi ý tin do chính người đó đăng; người gửi ≠ người vận chuyển của cùng một đơn"

**Source Location:** `DOC-v1.0-01 §D7 "Rule vận hành (Operating Rules)" · row OPR-05`

**Analyst Note:** Rule an toàn cơ bản: 1 tài khoản không thể vừa là Sender vừa là Carrier của CÙNG 1 đơn. Đối chiếu vấn đề đã ghi nhận ở docx Table 17 #9: *"Chi tiết tin cho phép chính chủ tin hoặc Người nhận của đơn tự bấm 'Tôi mang giúp được' trên tin liên quan đến mình — nên rà soát logic ẩn/hiện nút theo vai trò thực"* — đây là BẰNG CHỨNG THỰC TẾ rằng bản demo (as-built) đang VI PHẠM chính rule OPR-05 này. Xem **C-ASN-02**.

#### REQ-ASN-009 — Vòng đời tin trong luồng khớp

**Source Quote:**
> "OPR-08 Vòng đời tin trong luồng khớp — Tin đang MATCHED/IN_TRANSIT không xuất hiện ở gợi ý cho carrier khác; tin huỷ bởi carrier quay lại 'Chờ ghép' và được khớp lại"

**Source Location:** `DOC-v1.0-01 §D7 "Rule vận hành (Operating Rules)" · row OPR-08`

**Analyst Note:** 2 vế: (1) tin đã ghép/đang giao ẩn khỏi pool gợi ý cho carrier khác (củng cố REQ-ASN-005/003), (2) tin bị Carrier huỷ (trước khi lấy hàng) quay lại pool khớp — liên hệ trực tiếp REQ-CNL-002 (OPR-09).

#### REQ-DLV-001 — Chụp ảnh hàng lúc nhận (tuỳ chọn)

**Source Quote #1:**
> "PUP-03 Chụp ảnh hàng lúc nhận — Tùy chọn (khuyến nghị) — lưu S3, gắn timeline làm bằng chứng"

**Source Location #1:** `DOC-v1.0-01 §D3 "Functional Requirements — Gửi Hàng" · row PUP-03`

**Source Quote #2:**
> "BR-CNF-01 Ảnh hàng lúc nhận tùy chọn nhưng khuyến nghị mạnh — bằng chứng chính khi tranh chấp"

**Source Location #2:** `DOC-v1.0-01 §D4 "Business Rules & Permission Matrix" · row BR-CNF-01`

**Analyst Note:** Không bắt buộc (optional) nhưng là bằng chứng CHÍNH khi có tranh chấp (D5 edge case: *"Sau khi nhận, hàng hỏng/mất → Tạo sự cố, không cho COMPLETED thường; dùng timeline + ảnh làm bằng chứng"*). Ảnh lưu S3, gắn kèm timestamp+geo (liên hệ data model `delivery.proof_photos`).

#### REQ-DLV-002 — Chia sẻ vị trí khi đang giao (tuỳ chọn)

**Source Quote:**
> "GPS-01 Chia sẻ vị trí khi đang giao — Tùy chọn; chỉ active khi đang giao; xóa sau khi đóng"

**Source Location:** `DOC-v1.0-01 §D3 "Functional Requirements — Gửi Hàng" · row GPS-01`

**Analyst Note:** Tuỳ chọn (không bắt buộc), chỉ active trong trạng thái IN_TRANSIT, tự xoá khi đơn đóng (COMPLETED/CANCELLED). Mặc định bật/tắt chưa xác định — BRD tự nêu câu hỏi mở: *"Chia sẻ vị trí mặc định bật/tắt?"* (§D5). Xem **C-DLV-02**.

#### REQ-DLV-003 — Xác nhận đã nhận hàng + escalate

**Source Quote #1:**
> "DLV-03 RECEIVER/SENDER xác nhận đã nhận — Quá N giờ chưa xác nhận → nhắc → admin hỗ trợ"

**Source Location #1:** `DOC-v1.0-01 §D3 "Functional Requirements — Gửi Hàng" · row DLV-03`

**Source Quote #2:**
> "BR-CNF-04 RECEIVER không xác nhận 2 giờ → nhắc; thêm 2 giờ → admin hỗ trợ"

**Source Location #2:** `DOC-v1.0-01 §D4 "Business Rules & Permission Matrix" · row BR-CNF-04`

**Source Quote #3:**
> "BR-INT-03 Hoàn thành cần người nhận xác nhận đã nhận hàng; nếu không xác nhận → nhắc + admin hỗ trợ"

**Source Location #3:** `DOC-v1.0-01 §A5 "Tương tác 2 chiều & Cơ chế kết nối"`

**Analyst Note:** ⚠️ Mâu thuẫn ai được quyền xác nhận: DLV-03 (D3) ghi "RECEIVER/SENDER" (cả 2 đều được), nhưng BR-INT-03 (A5) chỉ ghi "người nhận" (Receiver only). Đối chiếu DOC-v1.0-02 §5.2 khẳng định RÕ: *"Nút 'Xác nhận đã nhận hàng' chỉ kích hoạt khi trạng thái = Đã giao ⇒ Đây là quyền hạn ĐẶC BIỆT DUY NHẤT của vai trò Người nhận: chỉ Người nhận mới có thể chốt đơn 'Hoàn thành' — Người vận chuyển chỉ đưa đơn tới 'Đã giao' rồi phải chờ."* — demo/docx nhất quán với BR-INT-03 (Receiver-only), ngược với DLV-03 (D3). Thời hạn 2 giờ + thêm 2 giờ lấy từ BR-CNF-04. Xem **C-DLV-01 (BLOCKER)** — ảnh hưởng trực tiếp cột "Vai trò thực hiện" khi viết TC.

#### REQ-DLV-004 — (Tuỳ chọn) ghi nhận chi phí đối soát offline

**Source Quote #1:**
> "COST-01 (Tùy chọn) ghi nhận chi phí — Bản ghi tham khảo; app KHÔNG thanh toán; đối soát offline"

**Source Location #1:** `DOC-v1.0-01 §D3 "Functional Requirements — Gửi Hàng" · row COST-01`

**Source Quote #2:**
> "BR-COST-01 App không xử lý tiền; chỉ ghi con số hai bên tự khai (tùy chọn)"

**Source Location #2:** `DOC-v1.0-01 §D4 "Business Rules & Permission Matrix" · row BR-COST-01`

**Analyst Note:** Chỉ là con số ghi chú tham khảo (2 bên tự khai), KHÔNG có cổng thanh toán/ví trong app (nhất quán NT-03). Không có UI minh hoạ cụ thể ở cả 2 doc — generate-tc test ở mức "field optional lưu số, không kích hoạt luồng thanh toán nào".

#### REQ-DLV-005 — Sau khi lấy hàng (IN_TRANSIT) không huỷ thường → phải tạo sự cố

**Source Quote:**
> "BR-ASN-03 Sau khi nhận hàng (IN_TRANSIT) không hủy thường → phải tạo sự cố"

**Source Location:** `DOC-v1.0-01 §D4 "Business Rules & Permission Matrix" · row BR-ASN-03`

**Analyst Note:** Từ IN_TRANSIT trở đi, đường huỷ thường (CNL-01) bị khoá — chỉ còn đường "Báo sự cố" (Incident). Không có đặc tả field màn Báo sự cố ở cả 2 doc — xem **C-CNL-01**. Khớp Permission Matrix (D4): *"Báo sự cố ✓ ✓ ✓ ✓"* — cả 4 actor đều báo được.

#### REQ-DLV-006 — Thứ tự bắt buộc: "Tôi đã lấy hàng" trước "Đã giao"

**Source Quote:**
> "US-D09 Là Carrier, tôi muốn bấm 'Tôi đã lấy hàng' rồi 'Đã giao cho người nhận' theo đúng thứ tự, để hệ thống ghi nhận mốc thời gian minh bạch cho cả hai bên. Không thể bấm 'Đã giao' trước khi 'Tôi đã lấy hàng'; timeline theo dõi 5 mốc (Chờ ghép · Lấy hàng · Đang giao · Đã giao · Hoàn thành), mỗi bước ghi timestamp"

**Source Location:** `DOC-v1.0-01 §D1b "User Story — Gửi Hàng" · Nhóm 2 · US-D09`

**Analyst Note:** Ràng buộc thứ tự UI (nút "Đã giao" chỉ enable sau khi đã bấm "Tôi đã lấy hàng"), khớp Table 12 (DOC-v1.0-02 §4.3): *"Trạng thái 'Lấy hàng' | Nút '✓ Tôi đã lấy hàng' → modal xác nhận — Trạng thái 'Đang giao' | Nút '✓ Đã giao cho người nhận' → modal xác nhận"*.

#### REQ-GIFT-001 — Tặng quà cảm ơn Carrier (4 loại)

**Source Quote #1:**
> "GIFT-01 Tặng quà cảm ơn Carrier — 4 loại quà phi vật chất (KHÔNG thanh toán); gửi không cần xác nhận; tổng hợp ở 'Quà đã nhận'"

**Source Location #1:** `DOC-v1.0-01 §D3 "Functional Requirements — Gửi Hàng" · row GIFT-01`

**Source Quote #2:**
> "BR-GIFT-01 Quà cảm ơn là biểu tượng phi vật chất, không quy đổi tiền, không qua thanh toán in-app"

**Source Location #2:** `DOC-v1.0-01 §D4 "Business Rules & Permission Matrix" · row BR-GIFT-01`

**Analyst Note:** 4 loại quà cụ thể theo A7: *"4 loại quà: bông hoa, ly cà phê, gấu bông, vương miện — biểu tượng phi vật chất"*, khớp demo docx §3.8: *"4 lựa chọn quà: 🌷 Bông hoa · ☕ Ly cà phê · 🧸 Gấu bông · 👑 Vương miện"*. Đây là điểm NHẤT QUÁN giữa BRD và demo (không có mâu thuẫn).

#### REQ-GIFT-002 — [MÂU THUẪN] Đánh giá 2 chiều 1–5 sao

**Source Quote:**
> "RAT-01/02 Đánh giá 2 chiều 1–5 sao + nhận xét"

**Source Location:** `DOC-v1.0-01 §D3 "Functional Requirements — Gửi Hàng" · row RAT-01/02`

**Analyst Note:** ⚠️ **Testability: BLOCKED.** RAT-01/02 (D3, chức năng Gửi Hàng) mâu thuẫn trực tiếp với ÍT NHẤT 4 chỗ khác trong CÙNG bộ tài liệu: (1) BR-INT-06 (§A5): *"Không đánh giá sao; ghi nhận thiện chí bằng quà ảo"*; (2) A7: *"Không tính điểm, không tier/xếp hạng"*; (3) A8: *"Phạm vi hiện tại: chỉ ghi log + admin can thiệp hỗ trợ. KHÔNG có chấm sao/đánh giá..."*; (4) ngược lại, A2 NT-07 và A10 KPI (*"Rating average > 4.0/5.0"*) lại NGẦM GIẢ ĐỊNH có hệ thống đánh giá sao. Demo/docx không có UI chấm sao nào (chỉ có mục "Đánh giá đã nhận" ở Cá nhân nhưng "không có phản hồi khi bấm" — docx Table 17 #6). KHÔNG derive scenario cho tính năng này (theo nguyên tắc "mơ hồ → Clarification, không đoán") — xem **C-GIFT-01 (BLOCKER)**.

#### REQ-GIFT-003 — Nút "Cảm ơn người vận chuyển" khoá lại sau khi gửi quà

**Source Quote:**
> "Hoàn thành: người gởi: 'Cảm ơn người vận chuyển' - enable --> click Cảm ơn người vận chuyển + chọn quà thành công -> vào lại chi tiết thì btn sẽ là 'Bạn đã đánh giá'"

**Source Location:** `Quan sát thực tế app STG — QA GiangDC2, xác nhận 2026-07-24 (không có trong DOC-v1.0-01/02/03)`

**Analyst Note:** Phát hiện mới trong quá trình QA trả lời trước generate-tc, không xuất hiện ở BRD/PRD/docx demo gốc — REQ-GIFT-001 chỉ mô tả hành động gửi quà (chọn 1/4 loại, gửi không cần Carrier xác nhận), không mô tả việc nút CTA đổi nhãn/khoá lại sau khi gửi. Sau khi Sender hoàn tất gửi quà, nút tại màn Theo dõi đơn/Chi tiết đơn đổi từ "Cảm ơn người vận chuyển" (enable) sang nhãn "Bạn đã đánh giá" (disable) — ngăn gửi quà lặp lại cho cùng 1 đơn. Xem `test_scenario_map.md` block "Theo dõi đơn — Ma trận nhãn nút theo trạng thái" và `SC-GIFT-004`.

#### REQ-CNL-001 — Huỷ đơn kèm lý do bắt buộc + đồng bộ realtime

**Source Quote #1:**
> "CNL-01 Huỷ đơn kèm lý do — Lý do bắt buộc; ghi actor (Sender/Carrier/Receiver); đồng bộ realtime; Carrier huỷ → về POSTED"

**Source Location #1:** `DOC-v1.0-01 §D3 "Functional Requirements — Gửi Hàng" · row CNL-01`

**Source Quote #2:**
> "BR-CNL-01 Huỷ đơn bắt buộc có lý do; hệ thống ghi rõ vai trò người huỷ + đồng bộ cho cả 3 bên"

**Source Location #2:** `DOC-v1.0-01 §D4 "Business Rules & Permission Matrix" · row BR-CNL-01`

**Source Quote #3:**
> "BR-INT-05 Huỷ sau khi MATCHED phải có lý do (bắt buộc), ghi rõ ai huỷ + đồng bộ realtime cả 3 bên"

**Source Location #3:** `DOC-v1.0-01 §A5 "Tương tác 2 chiều & Cơ chế kết nối"`

**Source Quote #4:**
> "US-D16 Là Sender/Carrier/Receiver, tôi muốn huỷ đơn (kèm lý do) và biết rõ ai đã huỷ... Huỷ được ở POSTED/MATCHED; popup huỷ bắt buộc nhập lý do (nút Xác nhận khoá tới khi có lý do); đơn huỷ ghi rõ ai huỷ (Người gửi/Người vận chuyển/Người nhận) + lý do, đồng bộ realtime cho cả 3 bên; Carrier huỷ nhận → đơn trả lại bảng tin (về 'Chờ ghép'); sau IN_TRANSIT phải tạo báo cáo sự cố"

**Source Location #4:** `DOC-v1.0-01 §D1b "User Story — Gửi Hàng" · Nhóm 4 · US-D16`

**Analyst Note:** 4 nguồn nhất quán. US-D16 AC là chi tiết nhất: popup lý do bắt buộc (nút Xác nhận disable tới khi có lý do), phạm vi huỷ = POSTED/MATCHED (khớp OPR-11/REQ-CNL-003), Carrier huỷ → về POSTED (khớp OPR-09/REQ-CNL-002), sau IN_TRANSIT → chuyển sang tạo sự cố (khớp BR-ASN-03/REQ-DLV-005).

#### REQ-CNL-002 — Carrier huỷ khi chưa lấy hàng → trả đơn về "Chờ ghép"

**Source Quote:**
> "OPR-09 Carrier huỷ khi chưa lấy hàng → trả đơn về bảng tin — Người vận chuyển huỷ ở trạng thái Đã ghép (chưa 'Tôi đã lấy hàng') → đơn tự động về 'Chờ ghép' và hiển thị lại trên bảng tin cho người khác nhận"

**Source Location:** `DOC-v1.0-01 §D7 "Rule vận hành (Operating Rules)" · row OPR-09`

**Analyst Note:** Chỉ áp dụng khi Carrier huỷ Ở TRẠNG THÁI MATCHED (chưa bấm "Tôi đã lấy hàng"). Đơn quay lại POSTED và hiện lại Bảng tin (liên hệ REQ-ASN-009 vòng đời tin trong luồng khớp).

#### REQ-CNL-003 — Điều kiện được phép huỷ theo trạng thái

**Source Quote:**
> "OPR-11 Điều kiện huỷ đơn — Chỉ được huỷ khi chưa ai nhận ('Chờ ghép') hoặc đang 'Lấy hàng' (đã ghép, chưa lấy được hàng); đã lấy hàng → sang 'Đang giao' thì KHÔNG ai được huỷ"

**Source Location:** `DOC-v1.0-01 §D7 "Rule vận hành (Operating Rules)" · row OPR-11`

**Analyst Note:** Phạm vi được huỷ = POSTED hoặc MATCHED (trước khi Carrier bấm "Tôi đã lấy hàng"). Từ IN_TRANSIT trở đi, KHÔNG AI (kể cả Admin theo bảng Permission Matrix ghi "✓ trước IN_TRANSIT" cho Sender/Receiver) được huỷ thường — chỉ còn đường Báo sự cố (REQ-DLV-005).

#### REQ-NTF-001 — Thông báo theo sự kiện vòng đời đơn (9 loại)

**Source Quote #1 (DOC-v1.0-01, draft BA):**
> "NTF-01 Có người bấm 'Tôi mang giúp được' → ghép ngay [Người gửi] 'Đã có người nhận mang giúp đơn của bạn — SĐT đã được lộ để liên hệ' · NTF-02 Đơn được ghép (MATCHED) [Người nhận] 'Đơn gửi tới bạn đã có người vận chuyển nhận giao' · NTF-03 Hệ thống khớp tuyến OFFER với 1 tin NEED [Người vận chuyển] 'Tìm thấy đơn hàng phù hợp tuyến của bạn — xem chi tiết để nhận giao' · NTF-04 Carrier bấm 'Tôi đã lấy hàng' (IN_TRANSIT) [Người gửi · Người nhận] 'Người vận chuyển đã lấy hàng và bắt đầu giao' · NTF-05 Carrier bấm 'Đã giao cho người nhận' (DELIVERED) [Người nhận · Người gửi] 'Đơn đã được giao — vui lòng xác nhận đã nhận hàng' · NTF-06 Người nhận 'Xác nhận đã nhận hàng' (COMPLETED) [Người gửi · Người vận chuyển] 'Đơn đã hoàn tất — cảm ơn bạn!' · NTF-07 Người gửi tặng quà ảo [Người vận chuyển] 'Bạn nhận được một món quà cảm ơn 🎁 — mở Trang cá nhân để xem' · NTF-08 Đơn bị huỷ (kèm lý do) [Các bên còn lại của đơn] 'Đơn đã bị huỷ bởi [vai trò] — lý do: […]' · NTF-09 Tin quá hạn chưa ghép [Người đăng tin] 'Tin của bạn đã quá hạn — gỡ hoặc đăng lại nếu vẫn cần'"

**Source Location #1:** `DOC-v1.0-01 §D6 "Thông báo (Notifications)" · bảng NTF-01..09`

**Source Quote #2 (DOC-v1.0-04 — màn hình Figma "Thông báo", verbatim chụp từ ảnh `db4dfb7e4f07138be5712aff5cb7dea61d983353` + `1c6c57c1a6356fee121b59007f85478d244d43d2`, đã zoom 4x xác nhận, độ tin cậy CAO NHẤT vì là artifact thiết kế gốc):**
> HÔM NAY: 🎁 "Bạn nhận được một món quà cảm ơn 🎁" — "Đồng Công Chí Linh đã gửi tặng bạn một món quà vì đã giúp giao hàng. Mở trang cá nhân để xem." (Vừa xong) · 🤝 "Tìm thấy đơn hàng phù hợp tuyến của bạn" — "Có người cần gửi "Đồ điện tử · Lô B3 → Q.3" trùng tuyến bạn đã đăng. Xem chi tiết để nhận giao." (5 phút trước) · 📞 "Ghép thành công — SĐT đã được lộ" — "Bạn và Trần Thị Lan đã được kết nối. Liên hệ để sắp xếp lấy hàng.ép giao nhận." (48 phút trước — chữ ".ép" nghi là lỗi/artifact bản thiết kế, có thể gốc là "lấy hàng/giao nhận.", cần verify với đội design) · ❌ "Đơn của bạn đã bị người vận chuyển huỷ" — "Lý do: "bận họp gấp". Đơn đang chờ người vận chuyển mới nhận giúp." (35 phút trước) · 🕐 "Sắp đến khung giờ hẹn giao" — "Đơn của bạn hẹn giao trong khung 17:00–18:30 hôm nay." (1 giờ trước) — HÔM QUA: ✅ "Đơn đã hoàn thành — đánh giá ngay" — ""Gửi đồ ăn sáng" đã giao xong. Hãy đánh giá Trần Thị Lan để giúp cộng đồng tin cậy hơn." (Hôm qua · 18:20) · ⭐ "Bạn nhận được đánh giá 5 sao" — "Phạm Quốc Hùng: "Đúng giờ, nhiệt tình, sẽ nhớ tiếp lần sau!"" (Hôm qua · 09:40) · 🔀 "Có chuyến đi mới hợp tuyến của bạn" — "Lê Hoàng Nam vừa đăng chuyến KCX Tân Thuận..." (bị cắt trong ảnh, chưa đọc được hết). Header: "Thông báo", nút "Đánh dấu đã đọc" góc phải, nhóm theo "HÔM NAY"/"HÔM QUA", chấm đỏ = unread.

**Source Location #2:** `DOC-v1.0-04 (Fox Eco Doc, ảnh Figma) — images/db4dfb7e4f07138be5712aff5cb7dea61d983353, 1c6c57c1a6356fee121b59007f85478d244d43d2` (+ 4 ảnh biến thể trùng nội dung: `026e00357047c5b15dd9a4499cfa575a46a5d513`, `1099ea1cd6e3820f67be7cd7ef8ba6251ee4771c`, `221b12582c868e57a5d6e23f74a60b96e86ead30`)

**Analyst Note:** DOC-v1.0-01 §D6 tự đánh dấu *"Nháp — chờ BA review & bổ sung"* — nội dung KHÔNG final. DOC-v1.0-04 (thiết kế Figma thực tế) cho ra **1 danh sách thứ BA**, không khớp hoàn toàn với NTF-01..09 (D6) LẪN Table 4 demo (DOC-v1.0-02) — có 8 loại quan sát được (thay vì 9), trong đó: (a) trùng khái niệm nhưng khác câu chữ với NTF-01/02/03/04/07 của D6; (b) **KHÔNG thấy** loại tương đương NTF-05/06 (Carrier/Receiver xác nhận) hay NTF-08 (huỷ chuẩn) — thay vào đó có notification huỷ dạng khác "Đơn của bạn đã bị người vận chuyển huỷ" kèm lý do free-text mẫu; (c) **CÓ THÊM** 2 loại hoàn toàn mới không có trong D6: "Sắp đến khung giờ hẹn giao" (nhắc lịch) và cặp "Đơn đã hoàn thành — đánh giá ngay" / "Bạn nhận được đánh giá 5 sao" (rating — xem **C-GIFT-01**). Vì đây là artifact thiết kế UI gốc (screenshot Figma thực tế, không phải văn bản mô tả), **khuyến nghị dùng Source Quote #2 làm nguồn chính cho copy verbatim khi viết Expected Result trong test case** (đúng yêu cầu độ chính xác cao của dự án), giữ NTF-01..09 (D6) làm baseline logic sự kiện/người nhận cho các case chưa có ảnh xác nhận (NTF-06 "Receiver xác nhận nhận hàng" — hoàn tất). Xem **C-NTF-01** (cập nhật status).

#### REQ-NTF-002 — Trần thông báo khớp/ngày + lộ liên hệ có kiểm soát

**Source Quote #1:**
> "OPR-06 Trần thông báo khớp / ngày — Giới hạn số lần bắn thông báo khớp cho mỗi carrier trong ngày (ngưỡng admin cấu hình)"

**Source Location #1:** `DOC-v1.0-01 §D7 "Rule vận hành (Operating Rules)" · row OPR-06`

**Source Quote #2:**
> "OPR-07 Lộ liên hệ có kiểm soát — SĐT chỉ lộ sau khi ghép, chỉ cho đúng 2 người trong cặp; không đưa SĐT vào nội dung push"

**Source Location #2:** `DOC-v1.0-01 §D7 "Rule vận hành (Operating Rules)" · row OPR-07`

**Analyst Note:** OPR-06: ngưỡng cụ thể (bao nhiêu lần/ngày) do admin cấu hình, không có giá trị mặc định trong doc. OPR-07: ràng buộc bổ sung cho NTF — nội dung push KHÔNG được chứa SĐT (dù đơn đã MATCHED), test riêng biệt với REQ-ASN-002/003 (là lộ SĐT trong app, khác với "không đưa vào push").

#### REQ-TS-001 — Ghi log toàn bộ tương tác, không sửa được

**Source Quote #1:**
> "TS-01 Ghi log toàn bộ tương tác: ai đăng, ai nhận, mốc thời gian, đổi trạng thái, huỷ (kèm lý do + ai huỷ) — TS-02 Log không sửa được sau khi ghi (audit trail)"

**Source Location #1:** `DOC-v1.0-01 §A8 "Pháp lý, Trách nhiệm & Trust/Safety" · bảng "Trust & Safety (chung)"`

**Source Quote #2:**
> "BR-INT-04 Timeline tương tác không sửa được sau khi ghi (audit)"

**Source Location #2:** `DOC-v1.0-01 §A5 "Tương tác 2 chiều & Cơ chế kết nối"`

**Analyst Note:** Log bao gồm: ai đăng, ai nhận, mốc thời gian, đổi trạng thái, huỷ (lý do + actor). Immutable sau khi ghi (audit trail, xác nhận 2 lần: TS-02 và BR-INT-04). Test chủ yếu ở mức API/data (không có UI xem log cho end-user — chỉ Admin), scope test v1.0 giới hạn ở việc verify log được TẠO đúng khi có sự kiện (qua hệ quả quan sát được: timeline hiển thị ở Theo dõi đơn), verify KHÔNG SỬA ĐƯỢC cần môi trường/API level (ngoài phạm vi UI test thường).

#### REQ-TS-002 — Admin can thiệp hỗ trợ dựa trên log

**Source Quote:**
> "TS-03 Admin có quyền can thiệp hỗ trợ khi có vướng mắc (dựa trên log)"

**Source Location:** `DOC-v1.0-01 §A8 "Pháp lý, Trách nhiệm & Trust/Safety" · bảng "Trust & Safety (chung)"`

**Analyst Note:** Không có đặc tả UI Admin Web Portal cụ thể ở cả 2 doc (A3 chỉ nhắc tên nền tảng: *"Nền tảng: Mobile App (iOS/Android) + Admin Web Portal"*, không có màn hình/field nào được mô tả). Scope test v1.0 giới hạn ở việc verify HỆ QUẢ quan sát được từ phía end-user (vd đơn quá hạn xác nhận → chuyển "admin hỗ trợ" theo BR-CNF-04/REQ-DLV-003), không test được UI Admin Portal trực tiếp. Xem **C-TS-01**.

## 5. Test Data Summary
| Module | DOC Source | Fields chính | Số bộ valid | Số bộ invalid | Có boundary? |
|--------|-----------|-------------|-------------|---------------|-------------|
| USR | DOC-v1.0-01 | Tên, SĐT, avatar, phòng ban, khu vực, kênh liên hệ (SĐT/email) | 2 | 1 | Không |
| ORD | DOC-v1.0-01, DOC-v1.0-02 | Loại hàng, Ghi chú, Giá trị hàng, Ảnh, Người nhận (tên/SĐT/địa chỉ/email), khung giờ, khoảng ngày | 6 | 5 | Có (giá trị hàng ngưỡng — chưa có số cụ thể) |
| ASN | DOC-v1.0-01 | Điểm lấy/giao (OFFER), khung giờ | 2 | 1 | Không |
| DLV | DOC-v1.0-01 | Ảnh bằng chứng, vị trí GPS, chi phí (số tiền tự khai) | 2 | 1 | Không |
| GIFT | DOC-v1.0-01 | Loại quà (4 giá trị enum) | 1 | 1 | Không |
| CNL | DOC-v1.0-01, DOC-v1.0-02 | Lý do huỷ (text bắt buộc) | 1 | 1 | Không |
| NTF | DOC-v1.0-01 | — (nội dung mẫu, chưa final) | — | — | Không |
| TS | DOC-v1.0-01 | — (backend/log, không có input field UI) | — | — | Không |

## 6. Clarifications & Blockers
| # | Req ID | DOC Source | Vấn đề | Answer | Status | Ngày resolve | Ảnh hưởng |
|---|--------|-----------|--------|--------|--------|-------------|-----------|
| 1 | C-USR-01 | DOC-v1.0-01, DOC-v1.0-02, DOC-v1.0-04 | Demo/prototype hiển thị Hạng thành viên + Điểm ECO + Điểm uy tín, nhưng BRD (USR-05, A7) khẳng định KHÔNG tính điểm/tier/CO2 | Ảnh Figma thực tế (DOC-v1.0-04) CÓ badge tier "🏆 Hạng Đồng hành" ở Trang cá nhân, nhưng KHÔNG có điểm ECO/điểm uy tín dạng số | Partially Resolved (còn thiếu xác nhận BA về cơ chế tier) | 2026-07-24 | REQ-USR-004, SC-USR-004 |
| 2 | C-ORD-01 | DOC-v1.0-02 | Wizard đăng tin không có validate bắt buộc — Loại hàng/Giá trị (B1), Người nhận (B2) đều có thể để trống | — | Open (non-blocking) | — | REQ-ORD-002, SC-ORD-007 |
| 3 | C-ORD-02 | DOC-v1.0-01, DOC-v1.0-04 | Ngưỡng giá trị hàng (BR-ORD-03) + có bắt buộc ảnh khi vượt ngưỡng — chưa có con số | Đã quét toàn bộ 82 ảnh Figma (DOC-v1.0-04) — KHÔNG tìm thấy con số ngưỡng VNĐ nào; UI chỉ có 3 chip định tính "Giá trị thấp/vừa/cao", không cảnh báo bảo hiểm kèm số tiền | Open (BLOCKER cho BVA) — vẫn chưa có câu trả lời, đã loại trừ khả năng con số nằm ở UI | 2026-07-24 (rà soát, chưa resolve) | REQ-ORD-009, SC-ORD-013 |
| 4 | C-ORD-03 | DOC-v1.0-01 | Hạn tin mặc định (ORD-06 "quá hạn cấu hình") — chưa có giá trị cụ thể | — | Open (non-blocking) | — | REQ-ORD-004, SC-ORD-005 |
| 5 | C-ORD-04 | DOC-v1.0-01, DOC-v1.0-02 | Chip "Thuốc/Y tế" vẫn là lựa chọn hợp lệ ở Loại hàng dù nguyên tắc cấm gửi thuốc — cơ chế validate chặn hay chỉ cảnh báo tĩnh chưa rõ | — | Open (non-blocking) | — | REQ-ORD-010, SC-ORD-014 |
| 6 | C-ASN-01 | DOC-v1.0-01, DOC-v1.0-02 | Thời điểm lộ SĐT chưa nhất quán — banner nói SĐT chỉ lộ SAU KHI ghép, nhưng demo Chi tiết tin hiện sẵn SĐT+nút Gọi ngay từ "Chờ ghép" | — | Open (non-blocking) | — | REQ-ASN-002/003, SC-ASN-003 |
| 7 | C-ASN-02 | DOC-v1.0-01, DOC-v1.0-02 | OPR-05 cấm tự khớp chính mình, nhưng demo cho phép chủ tin/Người nhận của đơn tự bấm "Tôi mang giúp được" trên tin liên quan đến mình | — | Open (non-blocking) | — | REQ-ASN-008, SC-ASN-011 |
| 8 | C-DLV-01 | DOC-v1.0-01, DOC-v1.0-02, DOC-v1.0-04 | Ai được xác nhận "Đã nhận" — DLV-03 (D3) ghi RECEIVER/SENDER, nhưng BR-INT-03 (A5) + demo docx §5.2 chỉ cho phép Receiver | Ảnh Figma xác nhận nhất quán qua nhiều màn (5dc3ce81c, 7d8b4a8cf, 82d9aace4, 8563adc1, 91b08fb1): nút "Xác nhận đã nhận hàng" CHỈ active với Receiver; Sender/Carrier ở cùng bước "Đã giao" chỉ thấy nhãn disabled "Đã giao · chờ người nhận xác nhận" | Resolved — Receiver-only | 2026-07-24 | REQ-DLV-003, SC-DLV-005/011 |
| 9 | C-DLV-02 | DOC-v1.0-01 | Chia sẻ vị trí (GPS-01) mặc định bật/tắt — BRD tự nêu câu hỏi mở, chưa có câu trả lời | — | Open (non-blocking) | — | REQ-DLV-002, SC-DLV-003 |
| 10 | C-DLV-03 | DOC-v1.0-02, DOC-v1.0-04 | 2 phiên bản màn "Xác nhận đã nhận hàng" — modal đơn giản (§5.2) vs form đầy đủ có ảnh bằng chứng + điểm uy tín carrier (§5.3) — chưa chốt bản chính thức | Cả 82 ảnh Figma chỉ thấy bản modal đơn giản ("Xác nhận" / "Bạn xác nhận đã nhận được hàng từ người vận chuyển?" / nút Huỷ-Xác nhận) — KHÔNG thấy bản form đầy đủ (ảnh bằng chứng/điểm uy tín) ở bất kỳ đâu trong bộ ảnh thiết kế | Partially Resolved — nghiêng về bản modal đơn giản là thiết kế chính thức | 2026-07-24 | SC-DLV-005/011 |
| 11 | C-GIFT-01 | DOC-v1.0-01, DOC-v1.0-04 | RAT-01/02 (đánh giá 1-5 sao) mâu thuẫn trực tiếp với BR-INT-06/A7/A8 (không đánh giá sao); NT-07 + A10 KPI lại ngầm giả định có rating | Ảnh Figma "Thông báo" (db4dfb7e4, 1c6c57c1a — đã zoom xác nhận) CÓ 2 notification liên quan rating: "Đơn đã hoàn thành — đánh giá ngay" (mời đánh giá) + "Bạn nhận được đánh giá 5 sao" kèm comment cụ thể ("Phạm Quốc Hùng: 'Đúng giờ, nhiệt tình...'") → tính năng rating THỰC SỰ TỒN TẠI trong UI. Tuy nhiên KHÔNG tìm thấy màn hình UI để "cho" sao (chỉ thấy màn "Tặng quà" dùng icon quà, không có sao) trong 82 ảnh — có thể màn rating chưa nằm trong bộ ảnh này | Partially Resolved — rating tồn tại (contradicts BR-INT-06), nhưng màn thao tác chấm sao chưa xác định được | 2026-07-24 | REQ-GIFT-002 |
| 12 | C-NTF-01 | DOC-v1.0-01, DOC-v1.0-02, DOC-v1.0-04 | 9 loại thông báo trong demo (Table 4, gồm "đánh giá 5 sao", "cộng đồng đạt mốc X đơn") khác nội dung với NTF-01..09 trong BRD | DOC-v1.0-04 (ảnh Figma thực tế) là NGUỒN THỨ BA, cũng không khớp hoàn toàn NTF-01..09 (D6) lẫn Table 4 (demo) — xem chi tiết REQ-NTF-001 §4.1. Củng cố bằng chứng rating tồn tại (khớp 1 phần với demo Table 4, không khớp BRD D6) | Open (non-blocking) — nay có thêm dữ liệu verbatim chính xác cao từ DOC-v1.0-04 để dùng làm baseline test | 2026-07-24 | REQ-NTF-001 |
| 13 | C-NTF-02 | DOC-v1.0-01 | Nhiều tham số vận hành chưa chốt: bán kính/định nghĩa "cùng tuyến", độ lệch khung giờ cho phép, chu kỳ quét khớp (D7); ngưỡng nhắc, gộp thông báo (D6) — chính BRD tự ghi "Chờ BA bổ sung" | — | Open (non-blocking) | — | REQ-ASN-006, REQ-NTF-001/002 |
| 14 | C-TS-01 | DOC-v1.0-01 | Admin Web Portal (A3) chưa có đặc tả UI/màn hình cụ thể ở cả 2 tài liệu | — | Open (non-blocking) | — | REQ-TS-002, SC-TS-003 |
| 15 | C-CNL-01 | DOC-v1.0-01, DOC-v1.0-02 | Màn "Báo sự cố" (Incident) chưa có đặc tả field cụ thể — chỉ nhắc tên trong phụ lục + vài rule liên quan | — | Open (non-blocking) | — | REQ-DLV-005 |
| 16 | C-ORD-05 | DOC-v1.0-04 | Màn "Đăng tin thành công!" tồn tại 2 biến thể ngay trên cùng board Figma — 1 bản CÓ trường "Mã tin" (vd `#ECO-2026-0451`), 1 bản KHÔNG có — mâu thuẫn nội bộ nguồn thiết kế, đồng thời đối lập với US-D02 (DOC-v1.0-01, "KHÔNG hiển thị mã đơn — mã kỹ thuật vô nghĩa với người dùng") | — | Open (non-blocking, ảnh hưởng SC-ORD-003) | — | REQ-ORD-001, SC-ORD-003 |
| 17 | C-USR-02 | DOC-v1.0-01, DOC-v1.0-04 | USR-07 "Cấu hình kênh liên hệ sẽ lộ" (SĐT bắt buộc/Workplace-email tuỳ chọn) chỉ có trong BRD text — KHÔNG xuất hiện ở bất kỳ ảnh Figma nào (DOC-v1.0-04) của màn Cá nhân (chỉ có avatar/tên/phòng ban/badge tier/2 số liệu/menu) | QA xác nhận trực tiếp trên app STG thật: KHÔNG tồn tại màn/mục cấu hình kênh liên hệ nào | Open — GAP xác nhận (BRD có, UI không có) | 2026-07-24 | REQ-USR-005, SC-USR-005 |
| 18 | C-USR-03 | DOC-v1.0-01 | USR-02 "Xem/cập nhật hồ sơ" — BRD khẳng định có chức năng cập nhật hồ sơ (tên, SĐT, avatar, phòng ban, khu vực, kênh liên hệ) | QA xác nhận trực tiếp trên app STG thật: màn Cá nhân KHÔNG có chức năng cập nhật/sửa hồ sơ nào — toàn bộ 6 trường chỉ ở dạng xem (view-only) | Resolved — view-only, không có update | 2026-07-24 | REQ-USR-002, SC-USR-002 |

### 6.1. Clarification Source Detail (per `references/quoting-guide.md` EC6)

#### C-USR-01 — Demo hiển thị tier/điểm/CO2, BRD nói không có (Partially Resolved)

**Source Quote (ambiguous):**
> "USR-05 Hiển thị tổng số đơn đã giúp + tổng số quà ảo đã nhận (không tính điểm/CO₂)" (DOC-v1.0-01 §A6) — đối lập — "Hạng thành viên | 🔒 'Hạng Đồng hành' — cơ chế tier/gamification... 3 chỉ số | Đơn đã giúp (12) · Điểm uy tín (4.8) · Điểm ECO (540)" (DOC-v1.0-02 Table 10, §3.9) — và mục tiêu sản phẩm ghi trong chính DOC-v1.0-02 §1.2: "Xây dựng động lực tham gia bằng cơ chế ghi nhận đóng góp: điểm ECO, điểm uy tín, hạng thành viên, thống kê cộng đồng (số đơn, số người, CO₂ tiết kiệm)."

**Source Location:** `DOC-v1.0-01 §A6/§A7` + `DOC-v1.0-02 §1.2, §3.9 Table 10`

**Source Quote (DOC-v1.0-04 — Figma "Cá nhân", ảnh `570ad9d32e3dbdf44c72d6140826f0e6f9a3393e` + `e5764b10a94b0d51fab023c1a92b6f25732cb402`, đã zoom 4x xác nhận):**
> Header cam: Avatar + "Nguyễn Anh Tuấn" / "Phòng Vận hành · MNV: FTEL3382" / badge pill nhỏ "🏆 Hạng Đồng hành". Card trắng bên dưới: 2 số liệu "12" — "đơn đã giúp" và "8" — "quà đã nhận". Menu: "Đơn của tôi", "Quà đã nhận". KHÔNG có "Điểm ECO", "Điểm uy tín" hay bất kỳ con số điểm/CO₂ nào trên màn hình.

**Source Location:** `DOC-v1.0-04 — images/570ad9d32e3dbdf44c72d6140826f0e6f9a3393e, e5764b10a94b0d51fab023c1a92b6f25732cb402`

**Analyst Note:** BRD v3.1 (ngày cập nhật mới hơn, 23/07/2026) rõ ràng loại bỏ điểm/tier/CO2 khỏi scope v1.0, nhưng prototype tham chiếu (mà D1 BRD tự nhận là "đồng bộ với") vẫn có đầy đủ các yếu tố này. Ảnh thiết kế Figma thực tế (DOC-v1.0-04) cho kết quả **TRUNG GIAN** giữa 2 nhánh: **CÓ** hiển thị badge tier dạng text "🏆 Hạng Đồng hành" (khớp 1 phần nhánh demo — "Hạng thành viên" tồn tại), nhưng **KHÔNG** có "Điểm ECO (540)"/"Điểm uy tín (4.8)" dạng số nào cả (khớp 1 phần nhánh BRD — "không tính điểm/CO₂"). → **Partially Resolved**: v1.0 có tier/hạng (text, không phải điểm số) nhưng không có điểm ECO/CO2 dạng số. Vẫn cần BA/PO xác nhận: (a) cơ chế "Hạng Đồng hành" tính như thế nào (theo số đơn đã giúp? có nhiều hạng khác không?), (b) badge tier có thực sự thuộc scope v1.0 hay là leftover thiết kế cũ chưa gỡ. Không còn BLOCKER cứng cho SC-USR-004 nhờ bằng chứng ảnh, nhưng vẫn nên hỏi BA về logic tier trước khi viết boundary test cho cơ chế lên hạng.

#### C-USR-02 — Cấu hình kênh liên hệ (USR-07) không có bằng chứng UI (Open — GAP)

**Source Quote (BRD, chỉ 1 nguồn):**
> "USR-07 Cấu hình kênh liên hệ sẽ lộ: SĐT (bắt buộc), Workplace/email (tùy chọn)"

**Source Location:** `DOC-v1.0-01 §A6 "Actors & Hồ sơ (chung)" · row USR-07`

**Đối chiếu UI (DOC-v1.0-04 + app STG thật):** Ảnh Figma màn Cá nhân đã zoom xác nhận (`570ad9d32e3dbdf44c72d6140826f0e6f9a3393e`, `e5764b10a94b0d51fab023c1a92b6f25732cb402` — xem C-USR-01) chỉ có: avatar, tên, "Phòng [ban] · MNV", badge tier, 2 số liệu (đơn đã giúp/quà đã nhận), menu "Đơn của tôi"/"Quà đã nhận" — KHÔNG có mục cấu hình kênh liên hệ nào. QA GiangDC2 xác nhận trực tiếp trên app STG (2026-07-24): không tìm thấy màn/toggle nào để bật-tắt hiển thị SĐT/email ở bất kỳ đâu trong app.

**Analyst Note:** Áp dụng rule mới `Project_rule.md §10.1` (UI Figma phải khớp tài liệu mới được viết TC) — vì 2 nguồn KHÔNG khớp, generate-tc KHÔNG được viết TC khẳng định vị trí/hành vi UI cho USR-07. `SC-USR-005` giữ nguyên trong scenario map nhưng cần gắn cờ GAP; nếu generate-tc chạy trước khi có xác nhận BA, chỉ nên viết dạng "GAP finding" (rà toàn app xác nhận không có UI) thay vì TC test hành vi bật/tắt. Cần BA/PO xác nhận: (a) tính năng này có thực sự nằm trong scope UI v1.0 không, (b) nếu có, nó nên nằm ở đâu (màn Cá nhân, hay 1 màn Cài đặt riêng chưa được thiết kế/chưa có trong bộ ảnh Figma).

#### C-USR-03 — Hồ sơ cá nhân (USR-02) không có chức năng cập nhật, chỉ view-only (Resolved)

**Source Quote (BRD):**
> "USR-02 Xem/cập nhật hồ sơ: tên, SĐT, avatar, phòng ban, khu vực/văn phòng, kênh liên hệ"

**Source Location:** `DOC-v1.0-01 §A6 "Actors & Hồ sơ (chung)" · row USR-02`

**Đối chiếu thực tế (app STG thật):** QA GiangDC2 xác nhận trực tiếp trên app STG (2026-07-24): màn Cá nhân KHÔNG có bất kỳ form/nút "Chỉnh sửa"/"Cập nhật" nào cho 6 trường (tên, SĐT, avatar, phòng ban, khu vực/văn phòng, kênh liên hệ) — toàn bộ chỉ hiển thị dạng xem (view-only), khớp với việc các trường này auto-fill từ SSO (readonly) đã ghi trong `test_data_catalog.md`.

**Analyst Note:** BRD (USR-02) dùng cụm "Xem/cập nhật" nhưng thực tế app v1.0 chỉ triển khai phần "Xem" — nhánh "cập nhật" KHÔNG tồn tại trên UI thật. Khác với C-USR-02 (GAP còn mở, chưa xác nhận rõ), case này đã có xác nhận trực tiếp rõ ràng từ QA trên app thật → **Resolved**. Đã cập nhật lại `REQ-USR-002`/`SC-USR-002` thành "Xem hồ sơ cá nhân (view-only)" — generate-tc từ nay chỉ viết TC display/verification cho 6 trường, KHÔNG viết TC hành vi "cập nhật/lưu" (CRUD update) cho scenario này.

#### C-ORD-01 — Wizard đăng tin không có validate bắt buộc

**Source Quote (ambiguous):**
> "⚠ Lưu ý: Không có trường nào bắt buộc (*) — có thể bấm 'Tiếp theo' mà không chọn Loại hàng/Giá trị." (§3.5.1) — "⚠ Lưu ý: Có thể bỏ trống toàn bộ thông tin Người nhận mà vẫn qua được Bước 3 — không có validate bắt buộc trong bản demo." (§3.5.2)

**Source Location:** `DOC-v1.0-02 §3.5.1 "Wizard đăng tin ... Bước 1/3", §3.5.2 "Bước 2/3"`

**Analyst Note:** Đây là hành vi quan sát được TRÊN PROTOTYPE (giới hạn demo tự nhận ở §Phạm vi & giới hạn phân tích), không rõ có phải đặc tả chính thức hay chỉ là gap của bản demo. BRD (D3 ORD-01/02) không nói rõ field nào bắt buộc/optional ngoài ORD-09 (consent). Non-blocking — generate-tc ghi nhận cả 2 khả năng (test cả nhánh "để trống vẫn qua" theo hành vi hiện tại VÀ note cần xác nhận BA nếu chuyển sang bắt buộc).

#### C-ORD-02 — Ngưỡng giá trị hàng chưa xác định (BLOCKER)

**Source Quote (ambiguous):**
> "Câu hỏi mở cho BA — Ngưỡng giá trị hàng? Ảnh bắt buộc cho hàng > ngưỡng?"

**Source Location:** `DOC-v1.0-01 §D5 "Edge Cases · Data Model · KPI" · "Câu hỏi mở cho BA"`

**Analyst Note:** Chính BRD tự liệt kê đây là câu hỏi mở, chưa có câu trả lời. Không thể viết test data Boundary Value Analysis cho BR-ORD-03 (REQ-ORD-009) khi chưa có con số ngưỡng cụ thể — **BLOCKER cho generate-tc phần BVA giá trị hàng**.

#### C-ORD-03 — Hạn tin mặc định chưa xác định

**Source Quote (ambiguous):**
> "Hạn tin mặc định?" (mục Câu hỏi mở cho BA)

**Source Location:** `DOC-v1.0-01 §D5 "Edge Cases · Data Model · KPI" · "Câu hỏi mở cho BA"`

**Analyst Note:** Liên quan REQ-ORD-004 (ORD-06/US-D04) — "quá hạn cấu hình" không có giá trị số cụ thể (bao nhiêu giờ/ngày). Non-blocking cho happy-path test (verify tin CÓ chuyển EXPIRED) nhưng blocker cho test đúng THỜI ĐIỂM chuyển (cần môi trường test có thể set hạn ngắn hoặc mock thời gian).

#### C-ORD-04 — Chip "Thuốc/Y tế" vẫn hợp lệ dù cấm gửi thuốc

**Source Quote (ambiguous):**
> "Loại hàng | Chip chọn 1: Tài liệu (mặc định) · Đồ điện tử · Thực phẩm · Hàng nhỏ · Đồ dễ vỡ · Quần áo · Thuốc/Y tế · Khác" (Table 6, §3.5.1) — đối chiếu — "Cấm gửi: thuốc, vũ khí, chất nguy hiểm, hàng phi pháp." (§1.4)

**Source Location:** `DOC-v1.0-02 §3.5.1 Table 6` + `§1.4 "Nguyên tắc cốt lõi"`

**Analyst Note:** Chip "Thuốc/Y tế" (bao gồm cả các sản phẩm y tế hợp pháp không phải "thuốc cấm") có thể hợp lý nếu ý là "vật tư y tế nói chung" chứ không phải riêng "thuốc" — nhưng label trùng chữ "Thuốc" với danh mục cấm gây nhầm lẫn UX và khó xác định pass/fail khi test. Non-blocking, cần BA làm rõ ranh giới "Thuốc/Y tế" hợp lệ vs "thuốc" bị cấm.

#### C-ASN-01 — Thời điểm lộ SĐT chưa nhất quán

**Source Quote (ambiguous):**
> "⚠ Lưu ý: Màn 'Đăng tin mới' cam kết SĐT chỉ lộ SAU KHI ghép, nhưng thực tế Chi tiết tin đã hiển thị sẵn SĐT + nút Gọi của Người gửi ngay từ trạng thái 'Chờ ghép' (chưa ai xác nhận mang giúp). Cần xác nhận đây có phải hành vi dự kiến."

**Source Location:** `DOC-v1.0-02 §3.4 "Màn hình Chi tiết tin"`

**Analyst Note:** Mâu thuẫn trực tiếp với BR-CON-02 (BRD, REQ-ASN-003): *"trước khi ghép không lộ SĐT"*. Nếu hành vi hiện tại của demo (SĐT hiện sớm) là bug cần fix, SC-ASN-003 (P1) sẽ là regression test quan trọng. Non-blocking để viết scenario (rule BRD đã rõ ràng — test theo BRD, tức "SĐT KHÔNG lộ trước khi ghép" là expected đúng), nhưng cần lưu ý khi vibe-test trên bản hiện tại có thể FAIL do gap này.

#### C-ASN-02 — Chủ tin/Người nhận có thể tự "nhận mang giúp" đơn của mình

**Source Quote (ambiguous):**
> "9 | Chủ tin / Người nhận có thể tự 'nhận mang giúp' | Chi tiết tin cho phép chính chủ tin hoặc Người nhận của đơn tự bấm 'Tôi mang giúp được' trên tin liên quan đến mình — nên rà soát logic ẩn/hiện nút theo vai trò thực."

**Source Location:** `DOC-v1.0-02 §7 "Các điểm cần làm rõ" · Table 17 row 9`

**Analyst Note:** Vi phạm trực tiếp OPR-05 (REQ-ASN-008): *"Không gợi ý tin do chính người đó đăng; người gửi ≠ người vận chuyển của cùng một đơn"*. Non-blocking để viết scenario (BRD đã rõ, test theo OPR-05 là expected đúng — nút "Tôi mang giúp được" PHẢI ẩn với chính chủ tin/Người nhận của đơn đó).

#### C-DLV-01 — Ai được xác nhận "Đã nhận" (Resolved — Receiver-only)

**Source Quote (ambiguous):**
> "DLV-03 RECEIVER/SENDER xác nhận đã nhận" (DOC-v1.0-01 §D3) — đối lập — "BR-INT-03 Hoàn thành cần người nhận xác nhận đã nhận hàng" (DOC-v1.0-01 §A5) — và — "⇒ Đây là quyền hạn ĐẶC BIỆT DUY NHẤT của vai trò Người nhận: chỉ Người nhận mới có thể chốt đơn 'Hoàn thành' — Người vận chuyển chỉ đưa đơn tới 'Đã giao' rồi phải chờ." (DOC-v1.0-02 §5.2)

**Source Location:** `DOC-v1.0-01 §D3 row DLV-03, §A5 row BR-INT-03` + `DOC-v1.0-02 §5.2 "Màn hình Theo dõi đơn (nhãn phụ 'Tôi nhận hàng')"`

**Source Quote (DOC-v1.0-04 — Figma, xác nhận qua nhiều ảnh độc lập, đã zoom xác nhận nội dung popup):**
> Receiver ("Tôi nhận hàng"), bước "Đã giao": nút cam active **"Xác nhận đã nhận hàng"** (`7d8b4a8cf5c78355a0977f13fa8f1ae3d3b96091`) → bấm ra popup "Xác nhận" — "Bạn xác nhận đã nhận được hàng từ người vận chuyển?" — nút Huỷ/Xác nhận (`5dc3ce81c38a42c96f6bf3f6bab751e90dcfa3fe`, `82d9aace478ba585169b74e5bdedec3053e96bbe`). CÙNG bước "Đã giao": Sender thấy nhãn DISABLED "Đã giao · chờ người nhận xác nhận" (`8563adc10d2b0697bff7c2f68c4839008ffa5f16`); Carrier cũng thấy nhãn DISABLED tương tự (`91b08fb10c09ab34d0943d1999b891b029a96526`). Carrier có hành động RIÊNG, độc lập, ở bước "Đang giao": nút "Đã giao cho người nhận" (`e1699c4f6f52bd9bf1c1277d4db122fb3d0aa978`) → popup "Xác nhận" — "Bạn xác nhận đã giao hàng tận tay người nhận?" (`ca5e7239037e6d21a5fc337235100d6abfb31e6a`) — đây là Carrier TỰ BÁO đã giao xong (chuyển POSTED→"Đã giao"), KHÁC với Receiver xác nhận đã NHẬN (chuyển "Đã giao"→"Hoàn thành").

**Source Location:** `DOC-v1.0-04 — images/7d8b4a8cf5c78355a0977f13fa8f1ae3d3b96091, 5dc3ce81c38a42c96f6bf3f6bab751e90dcfa3fe, 82d9aace478ba585169b74e5bdedec3053e96bbe, 8563adc10d2b0697bff7c2f68c4839008ffa5f16, 91b08fb10c09ab34d0943d1999b891b029a96526, e1699c4f6f52bd9bf1c1277d4db122fb3d0aa978, ca5e7239037e6d21a5fc337235100d6abfb31e6a`

**Analyst Note:** 3/4 nguồn (BR-INT-03 + demo/docx §5.2 + Figma DOC-v1.0-04, nguồn có độ tin cậy cao nhất vì là ảnh thiết kế UI thực tế) đồng thuận CHỈ Receiver được xác nhận "Đã nhận hàng"; chỉ DLV-03 (D3, văn bản BA nháp) nói cả Receiver/Sender. **Resolved theo hướng Receiver-only.** Phát hiện thêm quy trình 2 bước tách biệt rõ ràng: (1) Carrier bấm "Đã giao cho người nhận" ở bước "Đang giao" → chuyển "Đã giao"; (2) Receiver bấm "Xác nhận đã nhận hàng" ở bước "Đã giao" → chuyển "Hoàn thành". Sender không có action nào ở cả 2 bước, chỉ xem trạng thái. generate-tc dùng Receiver làm actor chính cho REQ-DLV-003/SC-DLV-005/SC-DLV-011; vẫn khuyến nghị 1 dòng note cho BA xác nhận chính thức trước khi đóng hẳn DLV-03 (D3) như lỗi văn bản.

#### C-DLV-02 — Chia sẻ vị trí mặc định bật/tắt

**Source Quote (ambiguous):**
> "Chia sẻ vị trí mặc định bật/tắt?"

**Source Location:** `DOC-v1.0-01 §D5 "Edge Cases · Data Model · KPI" · "Câu hỏi mở cho BA"`

**Analyst Note:** Liên quan GPS-01 (REQ-DLV-002). Non-blocking cho happy-path (verify chia sẻ vị trí hoạt động khi user bật) nhưng ảnh hưởng Given ban đầu của SC-DLV-003 (mặc định OFF hay ON khi vào màn Theo dõi đơn ở trạng thái IN_TRANSIT).

#### C-DLV-03 — 2 phiên bản màn "Xác nhận đã nhận hàng" chưa chốt (Partially Resolved)

**Source Quote (ambiguous):**
> "Trong quá trình khảo sát, phát hiện thêm một biến thể đầy đủ hơn của hành động xác nhận nhận hàng... có thể là bản thiết kế đầy đủ dự kiến, trong khi modal đơn giản ở Mục 5.2 là bản rút gọn dùng cho luồng demo đồng bộ 3 màn... ⚠ Lưu ý: Cần xác nhận với đội thiết kế: bản chính thức dùng form đầy đủ này (có ảnh bằng chứng) hay modal xác nhận đơn giản như ở Mục 5.2 — vì đây là 2 cách triển khai khác nhau cho CÙNG một hành động nghiệp vụ."

**Source Location:** `DOC-v1.0-02 §5.3 "Màn hình 'Xác nhận đã nhận hàng' (phiên bản chi tiết)"`

**Analyst Note (cập nhật DOC-v1.0-04):** Đã quét toàn bộ 82 ảnh Figma — chỉ tìm thấy bản **modal đơn giản** ("Xác nhận" / "Bạn xác nhận đã nhận được hàng từ người vận chuyển?" / nút Huỷ-Xác nhận, xem C-DLV-01) ở MỌI ảnh liên quan tới bước xác nhận nhận hàng. KHÔNG có ảnh nào cho thấy form đầy đủ (thông tin Carrier + điểm uy tín + ảnh bằng chứng) như mô tả ở DOC-v1.0-02 §5.3. **Partially Resolved** — nghiêng mạnh về bản modal đơn giản là thiết kế chính thức hiện tại của v1.0; form đầy đủ nhiều khả năng là đề xuất/phiên bản tương lai chưa lên thiết kế. Khuyến nghị generate-tc ưu tiên viết case theo modal đơn giản, giữ 1 note nhắc BA xác nhận nếu form đầy đủ vẫn còn trong roadmap gần.

#### C-GIFT-01 — RAT-01/02 mâu thuẫn nguyên tắc "không đánh giá sao" (Partially Resolved)

**Source Quote (ambiguous):**
> "RAT-01/02 Đánh giá 2 chiều 1–5 sao + nhận xét" (DOC-v1.0-01 §D3) — đối lập — "BR-INT-06 Không đánh giá sao; ghi nhận thiện chí bằng quà ảo người gửi tặng người vận chuyển sau khi hoàn tất" (§A5) — và — "Phạm vi hiện tại: chỉ ghi log + admin can thiệp hỗ trợ. KHÔNG có chấm sao/đánh giá, KHÔNG có chặn (block) người dùng." (§A8) — nhưng — "Rating average > 4.0/5.0" vẫn xuất hiện trong bảng KPI nền tảng (§A10)

**Source Location:** `DOC-v1.0-01 §D3 row RAT-01/02, §A5 row BR-INT-06, §A8, §A10 "KPIs chung"`

**Source Quote (DOC-v1.0-04 — Figma "Thông báo", đã zoom 4x xác nhận, ảnh `db4dfb7e4f07138be5712aff5cb7dea61d983353` + `1c6c57c1a6356fee121b59007f85478d244d43d2`):**
> "Đơn đã hoàn thành — đánh giá ngay" — ""Gửi đồ ăn sáng" đã giao xong. Hãy đánh giá Trần Thị Lan để giúp cộng đồng tin cậy hơn." · "Bạn nhận được đánh giá 5 sao" — "Phạm Quốc Hùng: "Đúng giờ, nhiệt tình, sẽ nhớ tiếp lần sau!"" (icon ngôi sao cam). Đồng thời, màn "Tặng quà" (`5d29d0821b4abe7e831646cdad7fa6cdbea69118`, `165aaa39e070e12b4fe61084d05b47959a3111ba`) và popup "Đã gửi lời cảm ơn!" (`808c25763c360700f941f055a2c2e9923ee53a31`, `851d2b9f636f0e6682ccbf1093f8929028b7cb92`) chỉ có 4 icon quà (Bông hoa/Ly cà phê/Gấu bông/Vương miện) — KHÔNG có UI sao 1-5 ở đây.

**Source Location:** `DOC-v1.0-04 — images/db4dfb7e4f07138be5712aff5cb7dea61d983353, 1c6c57c1a6356fee121b59007f85478d244d43d2, 5d29d0821b4abe7e831646cdad7fa6cdbea69118, 808c25763c360700f941f055a2c2e9923ee53a31`

**Analyst Note:** Mâu thuẫn gốc xuất hiện ở 4 vị trí khác nhau trong CÙNG 1 tài liệu BRD v3.1 (khả năng cao do sót nội dung từ version cũ chưa dọn hết ở D3/A10). Bằng chứng ảnh Figma (DOC-v1.0-04, nguồn thiết kế UI thực tế) cho thấy **tính năng đánh giá sao 1-5 THỰC SỰ TỒN TẠI** trong copy notification ("Bạn nhận được đánh giá 5 sao" kèm comment cụ thể) — trực tiếp mâu thuẫn với BR-INT-06 ("Không đánh giá sao"). Tuy nhiên, màn hình THAO TÁC chấm sao (nơi user thực sự bấm 1-5 sao) KHÔNG xuất hiện trong 82 ảnh đã quét — chỉ thấy màn Gift (icon quà, không sao). **Partially Resolved**: xác nhận rating tồn tại ở tầng notification/kết quả, nhưng chưa xác nhận được UI nhập rating có tồn tại/nằm ở đâu trong scope v1.0. Khuyến nghị BA/PO xác nhận: (a) rating 1-5 sao có thực sự trong scope hay chỉ là text mẫu minh hoạ chưa dọn trong bộ ảnh notification, (b) nếu có, màn hình thao tác chấm sao nằm ở đâu (có thể ngoài phạm vi 82 ảnh đã có). Không còn là BLOCKER cứng cho REQ-GIFT-002 nhờ có Source Quote để viết baseline test cho notification, nhưng scenario "user thao tác chấm sao" vẫn chưa thể viết tới khi có màn hình xác nhận.

#### C-NTF-01 — Nội dung 9 thông báo demo khác BRD

**Source Quote (ambiguous):**
> "Có người muốn mang giúp đơn của bạn | ... · Bạn nhận được đánh giá 5 sao | Kèm nhận xét từ đối tác đơn hàng · ... · Cộng đồng FoxEco vừa đạt mốc X đơn | Thông điệp 'tiết kiệm Y kg CO₂' — gamification"

**Source Location:** `DOC-v1.0-02 §3.2 "Màn hình Thông báo" · Table 4`

**Analyst Note:** Danh sách 9 loại thông báo trong demo/docx không khớp NTF-01..09 (BRD D6) — đặc biệt có 2 loại liên quan trực tiếp tới các tính năng đã bị BRD loại bỏ (đánh giá sao — xem C-GIFT-01; CO2/gamification — xem C-USR-01). Non-blocking cho REQ-NTF-001 (test theo danh sách BRD D6, đã là nguồn mới hơn) nhưng củng cố thêm bằng chứng cho 2 clarification kia.

**Cập nhật 2026-07-24 (DOC-v1.0-04):** Ảnh Figma thực tế cho ra danh sách THỨ BA (xem REQ-NTF-001 §4.1 Source Quote #2) — cũng khác cả BRD D6 lẫn demo Table 4. Trùng với demo Table 4 ở điểm có "đánh giá 5 sao"; KHÔNG có "cộng đồng đạt mốc X đơn" (CO2/gamification) ở bất kỳ đâu trong 82 ảnh — củng cố nhánh "CO2/gamification không có trong scope v1.0" (khớp C-USR-01), nhưng làm YẾU đi nhánh "rating không có trong scope" (đối lập C-GIFT-01). DOC-v1.0-04 nên là nguồn verbatim ưu tiên cho generate-tc vì là artifact thiết kế gốc.

#### C-NTF-02 — Nhiều tham số vận hành "Chờ BA bổ sung"

**Source Quote (ambiguous):**
> "Chờ BA bổ sung: bán kính/định nghĩa 'cùng tuyến', độ lệch khung giờ cho phép, chu kỳ quét khớp, hạ ưu tiên người huỷ nhiều lần, quy tắc ưu tiên khi nhiều carrier cùng tuyến." (§D7) — và — "Chờ BA bổ sung: ngưỡng thời gian nhắc, gộp/không gộp thông báo, thông báo cho người thứ 3 (VD người nhận khi carrier huỷ), cấu hình bật/tắt theo loại." (§D6)

**Source Location:** `DOC-v1.0-01 §D7 "Rule vận hành (Operating Rules)"` + `§D6 "Thông báo (Notifications)"`

**Analyst Note:** Doc TỰ đánh dấu các tham số này là chưa hoàn thiện ("Nháp — chờ BA review & bổ sung" xuất hiện ở cả D6 và D7). Non-blocking cho test happy-path (giá trị cụ thể không ảnh hưởng luồng chính) nhưng cần môi trường cấu hình được (hoặc mock) để test chính xác các ngưỡng khi giá trị thật được xác nhận.

#### C-TS-01 — Admin Web Portal chưa có đặc tả UI

**Source Quote (ambiguous):**
> "Nền tảng: Mobile App (iOS/Android) + Admin Web Portal." (§A3) — không có mô tả màn hình/field nào khác cho Admin Web Portal trong toàn bộ 2 tài liệu.

**Source Location:** `DOC-v1.0-01 §A3 "Bộ sản phẩm & Thứ tự ưu tiên"`

**Analyst Note:** REQ-TS-002 (Admin can thiệp hỗ trợ) không có UI cụ thể để viết TC chi tiết. Non-blocking cho v1.0 (test scope giới hạn ở hệ quả quan sát được từ phía end-user), nhưng sẽ trở thành blocker nếu cần test trực tiếp chức năng Admin.

#### C-CNL-01 — Màn "Báo sự cố" chưa có đặc tả field

**Source Quote (ambiguous):**
> "Báo sự cố | Cả 3 vai trò | —" (chỉ liệt kê tên màn trong phụ lục, không có field/nội dung cụ thể)

**Source Location:** `DOC-v1.0-02 §8 "Phụ lục — Danh sách toàn bộ màn hình đã khảo sát" · Table 18`

**Analyst Note:** Liên quan BR-ASN-03/REQ-DLV-005 (sau IN_TRANSIT phải tạo sự cố thay vì huỷ). Không có đặc tả field (loại sự cố, mô tả, ảnh đính kèm...) ở cả 2 doc. Non-blocking cho v1.0 (đủ để test "đường huỷ thường bị khoá + có đường thay thế Báo sự cố tồn tại"), cần bổ sung khi có thiết kế chi tiết màn này.

#### C-ORD-05 — 2 biến thể màn "Đăng tin thành công!" (có/không "Mã tin") — NEW 2026-07-24

**Source Quote (DOC-v1.0-04 — cả 4 ảnh đã zoom 4x xác nhận, cùng layout/copy chính nhưng khác 1 field):**
> Biến thể A — KHÔNG có "Mã tin" (`1cc41f87de9f6f9aa41e31eb1e783234771fa554`, `b2807d958cc82bbe871a43566a8b1c54ff02c462`): Title "Đăng tin thành công!" — Nội dung "Tin của bạn đã được đăng lên bảng tin. Chúng tôi sẽ thông báo ngay khi có người quan tâm." — Nút "Theo dõi đơn" / "Về trang chủ".
> Biến thể B — CÓ "Mã tin" (`53410b9a9962e145550cf91680a13bbabaf9b47c`, `c8a72f19d00292f5776ea53759535937bc8f9b9e`): Title + Nội dung giống hệt biến thể A, thêm 1 dòng field "Mã tin" — giá trị mẫu "#ECO-2026-0451" (chữ cam) — trước 2 nút.

**Source Location:** `DOC-v1.0-04 — images/1cc41f87de9f6f9aa41e31eb1e783234771fa554, b2807d958cc82bbe871a43566a8b1c54ff02c462 (biến thể A); 53410b9a9962e145550cf91680a13bbabaf9b47c, c8a72f19d00292f5776ea53759535937bc8f9b9e (biến thể B)`

**Analyst Note:** Cả 2 biến thể xuất hiện với số lượng ngang nhau (2 ảnh mỗi bản) trên cùng board Figma — không đủ cơ sở để xác định bản nào mới hơn/chính thức hơn chỉ từ dữ liệu ảnh. Đối chiếu US-D02 (DOC-v1.0-01 §D1b): *"Sau khi bấm 'Đăng tin ngay' → màn 'Đăng tin thành công' (**KHÔNG hiển thị mã đơn** — mã kỹ thuật vô nghĩa với người dùng)"* → biến thể A khớp US-D02, biến thể B mâu thuẫn. Khuyến nghị: dùng **biến thể A (không Mã tin)** làm baseline cho SC-ORD-003 (khớp văn bản BRD hiện hành + đa số ảnh nguồn khác trong bộ 82 ảnh không có trường này), đồng thời note rõ cho BA/design xác nhận biến thể B có phải bản cũ/thử nghiệm chưa gỡ khỏi board hay là hướng thiết kế mới (nếu có Mã tin, sẽ cần thêm field trong data model + REQ mới cho việc sinh mã tin theo format `#ECO-YYYY-NNNN`). Non-blocking cho happy-path test, ảnh hưởng duy nhất là có/không assert dòng "Mã tin" trong TC.

## 7. Automation Context (nếu có)
- Chưa có automation ở v1.0 (xem `PIPELINE.md`, `COMMANDS.md`). Khi cần: `/init-source-code --archetype appium-java` (SDK tích hợp app mobile FoxPro).

## 8. Deliverable Files Reference
| File | Đường dẫn | Mô tả |
|------|-----------|-------|
| Requirement Traceability | `02_analyze-requirements/v1.0/requirement_traceability.md` | Ma trận truy vết |
| Test Scenario Map | `02_analyze-requirements/v1.0/test_scenario_map.md` | Chi tiết scenarios + Block Definitions |
| Test Data Catalog | `02_analyze-requirements/v1.0/test_data_catalog.md` | Dữ liệu test |
| Risk Assessment | `02_analyze-requirements/v1.0/risk_assessment.md` | Đánh giá rủi ro |

## 9. TC Generation Log
> Header khớp generate-tc (Mode + Techniques cols). Mode ∈ standard/comprehensive/selective; Techniques = N/A (standard) hoặc danh sách B-ID (B1..B8). Priority = breakdown P1/P2/P3 (generate-tc ghi); Review Status (review-tc ghi: ⏳/✅/score).

| DOC ID | Ngày generate | Tổng TC | File output | Priority | Mode | Techniques | Review Status |
|--------|--------------|---------|-------------|----------|------|------------|---------------|
