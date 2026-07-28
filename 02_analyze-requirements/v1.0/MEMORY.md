# MEMORY — Analyze Requirements Output — v1.0

> Tạo bởi: skill analyze-requirements
> Cập nhật lần cuối: 2026-07-24 — bổ sung ma trận nhãn nút theo trạng thái (quan sát thực tế app STG, QA GiangDC2): +4 scenario (SC-DLV-012/013/014, SC-GIFT-004), +1 requirement (REQ-GIFT-003)
> Cập nhật 2026-07-24 (bổ sung #2): thêm nguồn DOC-v1.0-04 (Fox Eco Doc, 82 ảnh Figma) — resolve C-DLV-01, C-DLV-03 (Resolved/Partially Resolved); cập nhật C-USR-01, C-GIFT-01 (Partially Resolved); cập nhật REQ-NTF-001 với nội dung thông báo verbatim chính xác cao; +1 clarification mới C-ORD-05 (2 biến thể "Đăng tin thành công" có/không "Mã tin")
> Cập nhật 2026-07-24 (bổ sung #3): QA GiangDC2 xác nhận trực tiếp trên app STG — màn Cá nhân KHÔNG có chức năng cập nhật hồ sơ (chỉ xem/view-only), khác với USR-02 mô tả "Xem/cập nhật hồ sơ" — +1 clarification mới **C-USR-03** (Resolved — xác nhận view-only), sửa lại scope REQ-USR-002/SC-USR-002
> Cập nhật 2026-07-27 (UPDATE — BA/PO trả lời batch clarifications): resolve/deferred 13/16 clarification qua chat trực tiếp BA/PO. **Resolved — Out of scope v1.0 (deferred to future phase):** C-ORD-02 (ngưỡng giá trị hàng, gỡ BLOCKER cứng), C-USR-01 (tier/hạng), C-GIFT-01 (rating sao), C-USR-02 (cấu hình kênh liên hệ), C-TS-01 (Admin Portal), C-CNL-01 (Báo sự cố). **Resolved — có rule mới áp dụng ngay:** C-ORD-01 (validate bắt buộc + maxlength TBD), C-ORD-03 (hạn tin = giá trị user chọn), C-ORD-04 (không chặn Thuốc/Y tế ở v1.0), C-ASN-01 (SĐT lộ sau ghép), C-ASN-02 (cấm tự nhận), C-DLV-03 (modal đơn giản chính thức). **Partially Resolved:** C-NTF-02 (khớp tuyến = địa chỉ + khung giờ, còn thiếu độ lệch khung giờ/chu kỳ quét). **Còn Open thực sự (chưa trả lời):** C-ORD-05 (mã tin), C-NTF-01 (đã bổ sung bảng unified 3 nguồn, chờ BA chọn), C-DLV-02 (default vị trí — phase sau nhưng chưa có giá trị). Xem chi tiết §6/§6.1.
> Cập nhật 2026-07-27 (bổ sung #5 — rescan UI riêng màn Thông báo): rà lại `00_input/v1.0/27072026/` (BRD v3.2, Design v3.2, 1 ảnh chụp app STG) — không tìm thấy bằng chứng UI mới cho màn Thông báo (§D6 BRD v3.2 không đổi so với v3.1, ảnh chụp là màn "Đơn của tôi" không phải Thông báo). Theo yêu cầu user, +1 scenario mới **SC-NTF-007** (empty state danh sách thông báo) — áp dụng lại pattern đã dùng ở SC-ORD-023/SC-GIFT-006, mở rộng phạm vi **C-ORD-06** sang module NTF.
> Cập nhật 2026-07-27 (bổ sung #6 — gap phát hiện khi review TC-NTF): user phát hiện thiếu TC cho "đánh dấu đã đọc" và "scroll load thêm dữ liệu" tại màn Thông báo. +2 scenario mới **SC-NTF-008** (đánh dấu đã đọc, tap 1 item / mark-all) và **SC-NTF-009** (scroll load thêm dữ liệu/phân trang) — cả 2 không có bằng chứng tài liệu cho cơ chế cụ thể, hành vi test theo UX chuẩn do QA đề xuất, +1 clarification mới **C-NTF-03** (Open, cần BA/Dev confirm cơ chế thật).
> Cập nhật 2026-07-27 (bổ sung #7 — UPDATE, fix finding từ health-check): **SC-ORD-015..026** (12 scenario, màn Hoạt động — đã có sẵn trong `test_scenario_map.md` + `requirement_traceability.md` từ phiên generate-tc trước) bị THIẾU khỏi §4 Scenario Index — đã bổ sung đủ 12 row. Recompute lại §3 Tổng row: **65→82** scenario, priority Tổng **P1:19·P2:29·P3:17 → P1:19·P2:37·P3:26** (per-module row của ORD vốn đã đúng 26/4/15/7 từ trước, chỉ dòng Tổng cộng dồn bị stale). Không phát sinh scenario mới — đây là data-repair sync, không phải thêm scope.
> **Cập nhật 2026-07-28 (bổ sung #8 — UPDATE, BRD v3.2 mới):** BA cập nhật `00_input/v1.0/27072026/FoxEco BRD v3.2.md` — so với v3.1 chỉ thêm **1 section mới `§D8 · Validate & Giá trị mặc định (Form Rules)`** (D8.1 form Đơn cần gửi hàng, D8.2 form Tin nhận giao hàng, D8.3 quy tắc chung VAL-01..05); toàn bộ §A1-A10/D1-D7 giữ nguyên y hệt v3.1 (đã diff xác nhận), `FoxEco Design v3.2.html` cũng không đổi nội dung thực (chỉ khác UUID bundler nội bộ). D8 **resolve dứt điểm phần "TBD" còn lại của C-ORD-01** (maxlength cụ thể per field: Ghi chú 300 ký tự, Địa chỉ lấy/giao hàng 200 ký tự, Điểm xuất phát OFFER 200 ký tự, Tên người nhận 2–60 ký tự) + hé lộ cơ chế thật của field "Giá trị hàng" (chip thấp/vừa/cao, chọn "Cao" → cảnh báo tự chịu trách nhiệm — KHÁC với ngưỡng số tiền BR-ORD-03 vẫn đang Deferred ở C-ORD-02, xem note phân biệt 2 cơ chế tại §6.1 C-ORD-02). +2 REQ mới (`REQ-ORD-012`, `REQ-ORD-013`), +4 scenario ORD (`SC-ORD-027..030`), +1 scenario CNL (`SC-CNL-005`), 1 scenario MODIFIED (`SC-ORD-013` — từ "DEFERRED, không derive TC" sang "Giá trị hàng = Cao → cảnh báo trách nhiệm tự thoả thuận", derive TC được). Đồng thời phát hiện: dòng "Chờ BA bổ sung: bán kính/cùng tuyến, độ lệch khung giờ, chu kỳ quét" cuối §D7 (v3.1) đã bị XOÁ khỏi v3.2 nhưng KHÔNG có câu trả lời thay thế nào cho 3 câu hỏi đó — **C-NTF-02 giữ nguyên Partially Resolved**, chỉ cập nhật Source Quote note (đoạn text nguồn không còn tồn tại verbatim trong v3.2). Tổng scenario: **82→87** (P1:20 · P2:39 · P3:28); Tổng REQ: **41→43** (nhân tiện phát hiện + fix dòng Tổng §3 vốn đã lệch 40 vs tổng thật 41 trước cả update này — data-repair, không phải do update BRD v3.2 gây ra). **Lưu ý thêm:** dòng Tổng §3 trước update này cũng ghi P1=19 dù tổng thật per-module (kể cả trước khi thêm scenario mới) đã là P1=20 (ORD module row ghi nhầm P1=4 thay vì 5 từ đợt sync trước) — đã fix cùng lúc, không phải do BRD v3.2.
> **Cập nhật 2026-07-28 (bổ sung #9 — UPDATE, QA xác nhận trực tiếp qua ảnh Figma DOC-v1.0-04 + UI thật):** (1) Block "2 lựa chọn" màn "Đăng tin mới" bị thiếu 3 field so với UI thật (subtitle "Bạn muốn làm gì?", banner cam kết "App không thu phí, không chat, không thanh toán. Sau khi ghép, SĐT hai bên sẽ được lộ để liên hệ ngoài app.", mô tả card 2 verbatim) — xác nhận qua ảnh Figma hash `f821ba3087b8cc6e8065fbde6e327274d34482b2`, đã bổ sung đủ 5 field vào `test_scenario_map.md`. (2) QA GiangDC2 xác nhận trực tiếp: **C-ORD-06** (empty state "Hiện tại chưa có dữ liệu") và **C-NTF-03** (đánh dấu đã đọc + scroll load thêm) đều là hành vi THẬT trên UI app STG, không còn ở dạng đề xuất/suy luận chờ BA — cả 2 clarification chuyển **Resolved** (xem §6.1 chi tiết).
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
> **Cập nhật 2026-07-27 (sync sau health-check):** Priority breakdown (ORD, Tổng) và Risk Level đồng bộ lại theo trạng thái thực tế sau đợt batch-clarifications 2026-07-27 — xem `test_scenario_map.md` (priority per-scenario) và `risk_assessment.md` Tổng quan (risk level).

| Module | DOC Source | Tổng Req | Tổng SC | NEW | MODIFIED | CARRIED | DEPRECATED | P1 | P2 | P3 | Risk Level |
|--------|-----------|----------|---------|-----|----------|---------|-----------|----|----|----|-----------:|
| USR | DOC-v1.0-01, DOC-v1.0-02, DOC-v1.0-04, quan sát thực tế app | 5 | 7 | 7 | 0 | 0 | 0 | 1 | 4 | 2 | Low |
| ORD | DOC-v1.0-01, DOC-v1.0-02, quan sát thực tế app | 13 | 30 | 30 | 0 | 0 | 0 | 5 | 16 | 9 | Medium |
| ASN | DOC-v1.0-01, DOC-v1.0-02, DOC-v1.0-03 | 9 | 12 | 12 | 0 | 0 | 0 | 7 | 4 | 1 | High |
| DLV | DOC-v1.0-01, DOC-v1.0-02, DOC-v1.0-03, quan sát thực tế app | 6 | 14 | 14 | 0 | 0 | 0 | 5 | 4 | 5 | Medium |
| GIFT | DOC-v1.0-01, DOC-v1.0-02, quan sát thực tế app | 3 | 7 | 7 | 0 | 0 | 0 | 0 | 2 | 5 | Low |
| CNL | DOC-v1.0-01, DOC-v1.0-02 | 3 | 5 | 5 | 0 | 0 | 0 | 2 | 3 | 0 | Low |
| NTF | DOC-v1.0-01, DOC-v1.0-02, DOC-v1.0-04, quan sát thực tế app | 2 | 9 | 9 | 0 | 0 | 0 | 0 | 4 | 5 | Medium |
| TS | DOC-v1.0-01 | 2 | 3 | 3 | 0 | 0 | 0 | 0 | 2 | 1 | Low |
| **Tổng** | | **43** | **87** | **87** | **0** | **0** | **0** | **20** | **39** | **28** | |

## 4. Scenario Index
| SC ID | Tên ngắn | Module | DOC Source | Priority | Test Type | Lifecycle | TC Status | Vibe Status | Vibe Date |
|-------|----------|--------|-----------|----------|-----------|-----------|-----------|-------------|-----------|
| SC-USR-001 | Đăng nhập SSO thành công | USR | DOC-v1.0-01 | P1 | Functional | NEW | — | — | — |
| SC-USR-002 | Xem hồ sơ cá nhân (view-only — xác nhận không có update, C-USR-03) | USR | DOC-v1.0-01 | P2 | Functional | NEW | ✅ Đã tạo TC | — | — |
| SC-USR-003 | Hiển thị phòng ban + khu vực trên hồ sơ | USR | DOC-v1.0-01 | P2 | UI | NEW | ✅ Đã tạo TC | — | — |
| SC-USR-004 | Hiển thị đúng 2 chỉ số (đơn giúp + quà nhận), không hiện điểm/tier/CO2 | USR | DOC-v1.0-01, DOC-v1.0-02 | P2 | Business Rule | NEW | ✅ Đã tạo TC | — | — |
| SC-USR-005 | Cấu hình kênh liên hệ sẽ lộ | USR | DOC-v1.0-01 | P3 | Functional | NEW | ✅ Đã tạo TC | — | — |
| SC-USR-006 | Check đầy đủ hiển thị header màn Cá nhân (completeness) | USR | DOC-v1.0-01, DOC-v1.0-04 | P2 | UI | NEW | ✅ Đã tạo TC | — | — |
| SC-USR-007 | Menu "Đơn của tôi" tại Cá nhân điều hướng sang màn Hoạt động | USR | Quan sát thực tế app | P3 | Functional | NEW | ✅ Đã tạo TC | — | — |
| SC-ORD-001 | Đăng tin NEED "Cần gửi" qua wizard 3 bước | ORD | DOC-v1.0-01, DOC-v1.0-02 | P1 | Functional | NEW | ✅ Đã tạo TC | — | — |
| SC-ORD-002 | Đăng tin OFFER "Nhận giao hàng" (form 1 bước) | ORD | DOC-v1.0-01, DOC-v1.0-02 | P2 | Functional | NEW | ✅ Đã tạo TC | — | — |
| SC-ORD-003 | Tin xuất hiện ở "Đơn của tôi" ngay sau đăng, không hiện mã đơn | ORD | DOC-v1.0-02 | P2 | UI | NEW | ✅ Đã tạo TC | — | — |
| SC-ORD-004 | Timeline tin ghi nhận đầy đủ mốc thời gian | ORD | DOC-v1.0-01 | P1 | Functional | NEW | ✅ Đã tạo TC | — | — |
| SC-ORD-005 | Tin tự động "Hết hạn" khi quá thời gian không ai ghép | ORD | DOC-v1.0-01, DOC-v1.0-02 | P1 | Business Rule | NEW | ✅ Đã tạo TC | — | — |
| SC-ORD-006 | Không tick điều khoản → chặn đăng tin (Bước 3) | ORD | DOC-v1.0-01 | P2 | Business Rule | NEW | ✅ Đã tạo TC | — | — |
| SC-ORD-007 | [Gap] Bỏ trống Loại hàng/Giá trị Bước 1 vẫn qua Bước 2 | ORD | DOC-v1.0-02 | P3 | Business Rule | NEW | ✅ Đã tạo TC | — | — |
| SC-ORD-008 | Chỉnh sửa tin khi đang "Chờ ghép" | ORD | DOC-v1.0-01, DOC-v1.0-02 | P2 | Functional | NEW | ✅ Đã tạo TC | — | — |
| SC-ORD-009 | Khoá chỉnh sửa khi đã "Đã ghép" trở đi | ORD | DOC-v1.0-01, DOC-v1.0-02 | P1 | Business Rule | NEW | ✅ Đã tạo TC | — | — |
| SC-ORD-010 | Chọn nhanh 1 trong 6 văn phòng preset FPT | ORD | DOC-v1.0-01 | P3 | UI | NEW | ✅ Đã tạo TC | — | — |
| SC-ORD-011 | Email công ty người nhận có trong hệ thống → tự điền | ORD | DOC-v1.0-01, DOC-v1.0-02 | P2 | Functional | NEW | ✅ Đã tạo TC | — | — |
| SC-ORD-012 | Email công ty người nhận không có → báo nhập thủ công | ORD | DOC-v1.0-01, DOC-v1.0-02 | P2 | Business Rule | NEW | ✅ Đã tạo TC | — | — |
| SC-ORD-013 | Chọn Giá trị hàng "Cao" → cảnh báo trách nhiệm tự thoả thuận (⚠ MODIFIED 2026-07-28, un-deferred — xem C-ORD-02) | ORD | DOC-v1.0-01 (BRD v3.2 §D8.1) | P2 | Business Rule | NEW | ✅ Đã tạo TC | — | — |
| SC-ORD-014 | Đăng tin chứa hàng cấm → hệ thống chặn | ORD | DOC-v1.0-01 | P1 | Business Rule | NEW | ✅ Đã tạo TC | — | — |
| SC-ORD-015 | Đủ 2 tab "Đang diễn ra"/"Đã hoàn thành" tại Hoạt động | ORD | Quan sát thực tế app | P2 | UI | NEW | ✅ Đã tạo TC | — | — |
| SC-ORD-016 | Tab mặc định khi mới vào màn Hoạt động | ORD | Quan sát thực tế app | P2 | UI | NEW | ✅ Đã tạo TC | — | — |
| SC-ORD-017 | Check dữ liệu đúng tại tab "Đang diễn ra" | ORD | Quan sát thực tế app | P2 | Functional | NEW | ✅ Đã tạo TC | — | — |
| SC-ORD-018 | Check đầy đủ field trên 1 card đơn (completeness) | ORD | Quan sát thực tế app | P2 | UI | NEW | ✅ Đã tạo TC | — | — |
| SC-ORD-019 | Card trạng thái "Hoàn thành" hiển thị đúng, không assert rating | ORD | Quan sát thực tế app | P3 | UI | NEW | ✅ Đã tạo TC | — | — |
| SC-ORD-020 | Card trạng thái "Chờ ghép" hiển thị tại tab "Đang diễn ra" | ORD | Quan sát thực tế app | P3 | UI | NEW | ✅ Đã tạo TC | — | — |
| SC-ORD-021 | Tap card trạng thái khác "Hết hạn" → mở Chi tiết tin | ORD | Quan sát thực tế app | P2 | Functional | NEW | ✅ Đã tạo TC | — | — |
| SC-ORD-022 | Tap card "Hết hạn" → không cho thao tác | ORD | Quan sát thực tế app | P3 | Business Rule | NEW | ✅ Đã tạo TC | — | — |
| SC-ORD-023 | Empty state khi danh sách rỗng (cả 2 tab, C-ORD-06 Resolved) | ORD | Quan sát thực tế app | P3 | UI | NEW | ✅ Đã tạo TC | — | — |
| SC-ORD-024 | Đơn "Đã huỷ" (CNL) không hiển thị tại Hoạt động | ORD | Quan sát thực tế app | P2 | Business Rule | NEW | ✅ Đã tạo TC | — | — |
| SC-ORD-025 | Bottom nav đủ 5 tab, "Hoạt động" highlight đúng | ORD | Quan sát thực tế app | P3 | UI | NEW | ✅ Đã tạo TC | — | — |
| SC-ORD-026 | Check dữ liệu đúng tại tab "Đã hoàn thành" | ORD | Quan sát thực tế app | P2 | Functional | NEW | ✅ Đã tạo TC | — | — |
| SC-ORD-027 | Giới hạn ký tự tối đa các trường text + định dạng/kích thước ảnh sản phẩm (⚠ NEW 2026-07-28) | ORD | DOC-v1.0-01 (BRD v3.2 §D8.1/D8.2) | P3 | Business Rule | NEW | ✅ Đã tạo TC | — | — |
| SC-ORD-028 | Khung giờ (NEED + OFFER) phải cách nhau tối thiểu 30 phút (⚠ NEW 2026-07-28) | ORD | DOC-v1.0-01 (BRD v3.2 §D8.1/D8.2) | P2 | Business Rule | NEW | ✅ Đã tạo TC | — | — |
| SC-ORD-029 | Tự động cắt khoảng trắng + chuẩn hoá SĐT trước khi lưu (VAL-03, ⚠ NEW 2026-07-28) | ORD | DOC-v1.0-01 (BRD v3.2 §D8.3) | P3 | Business Rule | NEW | ✅ Đã tạo TC | — | — |
| SC-ORD-030 | Nút submit vô hiệu hoá tới khi hợp lệ; lỗi hiện inline on-blur; cuộn tới lỗi đầu tiên khi submit (VAL-01/02, ⚠ NEW 2026-07-28) | ORD | DOC-v1.0-01 (BRD v3.2 §D8.3) | P2 | UI | NEW | ✅ Đã tạo TC | — | — |
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
| SC-GIFT-003 | Card "Quà đã nhận" chỉ load đúng loại đã nhận (không hiện loại chưa nhận) | GIFT | Quan sát thực tế app | P3 | Business Rule | NEW | ✅ Đã tạo TC | — | — |
| SC-GIFT-004 | Nút "Cảm ơn người vận chuyển" đổi thành "Bạn đã đánh giá" sau khi gửi quà | GIFT | Quan sát thực tế app | P2 | Functional | NEW | — | — | — |
| SC-GIFT-005 | Menu "Quà đã nhận" tại Cá nhân điều hướng sang màn Quà đã nhận | GIFT | Quan sát thực tế app | P3 | Functional | NEW | ✅ Đã tạo TC | — | — |
| SC-GIFT-006 | Màn "Quà đã nhận" rỗng khi chưa nhận quà nào | GIFT | Quan sát thực tế app | P3 | UI | NEW | ✅ Đã tạo TC | — | — |
| SC-GIFT-007 | Icon quay lại tại màn "Quà đã nhận" | GIFT | Quan sát thực tế app | P3 | UI | NEW | ✅ Đã tạo TC | — | — |
| SC-CNL-001 | Huỷ đơn ở POSTED/MATCHED → popup bắt buộc nhập lý do | CNL | DOC-v1.0-01, DOC-v1.0-02 | P1 | Business Rule | NEW | — | — | — |
| SC-CNL-002 | Không cho huỷ khi đơn đã "Đang giao" trở đi | CNL | DOC-v1.0-01 | P1 | Business Rule | NEW | — | — | — |
| SC-CNL-003 | Đơn huỷ ghi rõ vai trò người huỷ + lý do, đồng bộ realtime 3 bên | CNL | DOC-v1.0-01, DOC-v1.0-02 | P2 | Business Rule | NEW | — | — | — |
| SC-CNL-004 | Carrier huỷ khi "Đã ghép" (chưa lấy hàng) → đơn về "Chờ ghép" | CNL | DOC-v1.0-01 | P2 | Business Rule | NEW | — | — | — |
| SC-CNL-005 | Lý do huỷ tối thiểu 5 ký tự mới bật nút Xác nhận (VAL-04, ⚠ NEW 2026-07-28) | CNL | DOC-v1.0-01 (BRD v3.2 §D8.3) | P2 | Business Rule | NEW | — | — | — |
| SC-NTF-001 | Thông báo khi ghép ngay (NTF-01/02) | NTF | DOC-v1.0-01 | P2 | Functional | NEW | ✅ Đã tạo TC | — | — |
| SC-NTF-002 | Thông báo khi khớp tuyến OFFER (NTF-03) | NTF | DOC-v1.0-01 | P2 | Functional | NEW | ✅ Đã tạo TC | — | — |
| SC-NTF-003 | Thông báo theo mốc vận chuyển: lấy hàng/đã giao/hoàn tất (NTF-04/05/06) | NTF | DOC-v1.0-01 | P2 | Functional | NEW | ✅ Đã tạo TC | — | — |
| SC-NTF-004 | Thông báo khi nhận quà cảm ơn (NTF-07) | NTF | DOC-v1.0-01 | P3 | Functional | NEW | ✅ Đã tạo TC | — | — |
| SC-NTF-005 | Thông báo khi đơn huỷ (NTF-08) và tin quá hạn (NTF-09) | NTF | DOC-v1.0-01 | P2 | Functional | NEW | ✅ Đã tạo TC | — | — |
| SC-NTF-006 | Carrier bị giới hạn trần thông báo khớp/ngày | NTF | DOC-v1.0-01 | P3 | Business Rule | NEW | ✅ Đã tạo TC | — | — |
| SC-NTF-007 | Empty state khi chưa có thông báo nào (mở rộng C-ORD-06, Resolved) | NTF | Quan sát thực tế app | P3 | UI | NEW | ✅ Đã tạo TC | — | — |
| SC-NTF-008 | Đánh dấu đã đọc (tap 1 thông báo / nút mark-all, C-NTF-03 Resolved) | NTF | DOC-v1.0-04 / Quan sát thực tế app | P3 | Functional | NEW | ✅ Đã tạo TC | — | — |
| SC-NTF-009 | Scroll xuống load thêm dữ liệu (phân trang, C-NTF-03 Resolved) | NTF | Quan sát thực tế app | P3 | Functional | NEW | ✅ Đã tạo TC | — | — |
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

#### REQ-ORD-011 — Màn Hoạt động (Đơn của tôi) — theo dõi lịch sử đơn theo tab — NEW 2026-07-27

**Source Quote:**
> Ảnh chụp màn "Đơn của tôi" (tab "Hoạt động" ở bottom nav): 2 tab "Đang diễn ra"/"Đã hoàn thành"; mỗi card hiện icon trạng thái + tên tin + tuyến + ngày + badge; card "Hết hạn" kèm dòng lý do; bottom nav 5 tab. Bổ sung qua trả lời trực tiếp (QA GiangDC2, 2026-07-27): default tab "Đang diễn ra"; tap card ≠"Hết hạn"→"Chi tiết tin", tap card "Hết hạn"→không thao tác được; đơn "Đã huỷ" không hiển thị ở màn này; empty state (cả 2 tab) hiển thị text "Hiện tại chưa có dữ liệu" (QA GiangDC2 xác nhận trực tiếp trên UI thật, 2026-07-28 — xem C-ORD-06 Resolved).

**Source Location:** `Quan sát thực tế app STG (QA GiangDC2) — ảnh 00_input/v1.0/27072026/Screenshot From 2026-07-27 15-23-25.png, xác nhận nghiệp vụ qua chat 2026-07-27`

**Analyst Note:** Không có trong BRD/PRD/Figma (DOC-v1.0-01/02/04) — hoàn toàn từ quan sát trực tiếp app STG, cùng dạng nguồn với REQ-DLV-003 (ma trận nhãn nút) và REQ-GIFT-003 (SC-GIFT-004). Card "Hoàn thành" có hiện "★★★★★ Đã đánh giá" nhưng đây là UI leftover của tính năng rating đã bị BA/PO xác nhận out-of-scope v1.0 (xem **C-GIFT-01**) — KHÔNG derive TC assert rating. Case "đơn Đã huỷ không hiển thị ở Hoạt động" liên hệ trực tiếp REQ-CNL-001 (luồng huỷ) — nếu CNL có thay đổi sau này (vd thêm biến thể huỷ mới), cần rà lại rule này.

#### REQ-ORD-012 — Validate & giá trị mặc định các trường form đăng tin (NEED + OFFER) — NEW 2026-07-28

**Source Quote #1 (D8.1 — Đơn cần gửi hàng, người gửi đăng tin):**
> "Loại hàng | Có | Tài liệu | Chọn 1 trong danh mục... Không cho để trống — Ghi chú | Không | Trống | Tối đa 300 ký tự... — Giá trị hàng | Có | Trống (chưa chọn) | Chọn 1: Giá trị thấp / vừa / cao. Chọn Giá trị cao → hiện cảnh báo trách nhiệm tự thoả thuận — Ảnh sản phẩm | Không | Trống | Chỉ 1 ảnh duy nhất, ≤ 5MB, định dạng JPG/PNG... — Địa chỉ lấy hàng | Có | ... | Không để trống, tối đa 200 ký tự — Email công ty người nhận | Có | Trống | Đúng định dạng email & thuộc tên miền nội bộ. Tra danh bạ: tìm thấy → tự điền tên/SĐT/địa chỉ; không thấy → cảnh báo & cho nhập thủ công — Tên người nhận | Có | Tự điền từ danh bạ | Không để trống, 2–60 ký tự — Số điện thoại | Có | Tự điền từ danh bạ | Số điện thoại VN hợp lệ (10 số, đầu 0)... — Địa chỉ giao hàng | Có | ... | Không để trống; phải khác địa chỉ lấy hàng — Khung giờ (từ – đến) | Có | 17:00 – 18:30 | đến > từ; khoảng tối thiểu 30 phút"

**Source Location #1:** `DOC-v1.0-01 (BRD v3.2) §D8.1 "Đơn cần gửi hàng (người gửi đăng tin)"`

**Source Quote #2 (D8.2 — Tin nhận giao hàng, người vận chuyển đăng):**
> "Điểm xuất phát | Có | Điền sẵn vị trí làm việc của người giao... để trống nếu hệ thống chưa có thông tin | Không để trống khi submit, tối đa 200 ký tự. User sửa được — Điểm đến | Có | Trống | Không để trống; phải khác điểm xuất phát — Thời gian di chuyển | Có | 17:30 – 18:30 | đến > từ; khoảng tối thiểu 30 phút"

**Source Location #2:** `DOC-v1.0-01 (BRD v3.2) §D8.2 "Tin nhận giao hàng / thuận đường (người vận chuyển đăng)"`

**Analyst Note:** Bổ sung từ BRD v3.2 (`00_input/v1.0/27072026/FoxEco BRD v3.2.md`, không có trong v3.1) — cung cấp maxlength/BVA cụ thể còn thiếu ở **C-ORD-01** (Resolved 2026-07-27 chỉ có phần "validate bắt buộc", phần maxlength khi đó còn TBD — nay đã có số, xem cập nhật tại §6.1 C-ORD-01). Riêng field "Giá trị hàng" (chip thấp/vừa/cao, đã biết từ DOC-v1.0-02) nay có thêm hành vi cụ thể: chọn "Cao" → hiện cảnh báo tĩnh về trách nhiệm tự thoả thuận — đây là cơ chế ĐƠN GIẢN (không phải ngưỡng số tiền), KHÁC với BR-ORD-03 (REQ-ORD-009, ngưỡng giá trị hàng bằng số tiền cụ thể — vẫn Deferred theo C-ORD-02, xem phân biệt 2 cơ chế tại §6.1 C-ORD-02). Điểm mới đáng chú ý khác: Địa chỉ giao hàng "phải khác địa chỉ lấy hàng" (validate so sánh 2 field, trước đây chưa có); Điểm đến (OFFER) "phải khác điểm xuất phát" tương tự.

#### REQ-ORD-013 — Quy tắc chung cho form (VAL-01..05) — NEW 2026-07-28

**Source Quote:**
> "VAL-01 | Nút submit vô hiệu hoá đến khi mọi trường bắt buộc hợp lệ + đã tick điều khoản — VAL-02 | Lỗi hiện ngay dưới ô nhập khi rời ô (on blur), không dùng popup; cuộn tới ô lỗi đầu tiên khi bấm submit — VAL-03 | Tự cắt khoảng trắng đầu/cuối; chuẩn hoá SĐT (bỏ khoảng trắng, dấu chấm) trước khi lưu — VAL-04 | Huỷ đơn: bắt buộc nhập lý do (tối thiểu 5 ký tự) mới bật nút Xác nhận — VAL-05 | Sửa đơn: form nạp sẵn dữ liệu cũ; áp dụng cùng bộ validate; chỉ mở khi đơn còn 'Chờ ghép' (xem OPR-10)"

**Source Location:** `DOC-v1.0-01 (BRD v3.2) §D8.3 "Quy tắc chung cho form"`

**Analyst Note:** VAL-05 chỉ xác nhận lại rule đã biết (REQ-ORD-006/OPR-10, không đổi). VAL-04 là chi tiết MỚI cho REQ-CNL-001 (SC-CNL-001 trước đây chỉ biết "bắt buộc nhập lý do", chưa có số ký tự tối thiểu — nay có, đủ để viết BVA). VAL-01/VAL-02 là hành vi UX cross-cutting áp dụng cho toàn bộ wizard NEED lẫn form OFFER — chưa từng được đặc tả trước đây (trước chỉ biết "nút Đăng tin ngay" tồn tại, chưa biết cơ chế disable/inline-error). VAL-03 (auto-trim + chuẩn hoá SĐT) là rule xử lý dữ liệu ẩn, ảnh hưởng tới cách viết test data (input có khoảng trắng thừa vẫn phải PASS sau khi trim).

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

**Cập nhật 2026-07-27 (rescan UI + empty state):** Đã rà lại `00_input/v1.0/27072026/` (BRD v3.2, Design v3.2, 1 ảnh chụp app STG) theo yêu cầu user "phân tích riêng màn hình thông báo" — không có bằng chứng UI mới cho màn Thông báo (§D6 BRD v3.2 giữ nguyên nội dung so với v3.1; ảnh chụp mới là màn "Đơn của tôi", không phải Thông báo). Riêng trạng thái rỗng (chưa có thông báo nào) không có trong bất kỳ nguồn nào — theo yêu cầu user, áp dụng lại pattern đã dùng cho tab Hoạt động/màn Quà đã nhận ("Hiện tại chưa có dữ liệu") → +**SC-NTF-007**, mở rộng phạm vi **C-ORD-06** sang module NTF (xem `test_scenario_map.md` block "Empty state (không có thông báo nào)").

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
| ORD | DOC-v1.0-01, DOC-v1.0-02 | Loại hàng, Ghi chú (≤300 ký tự), Giá trị hàng (thấp/vừa/cao), Ảnh (≤5MB JPG/PNG), Người nhận (tên 2-60 ký tự/SĐT/địa chỉ ≤200 ký tự/email), khung giờ (≥30 phút), khoảng ngày | 6 | 5 | Có — maxlength/BVA đầy đủ từ BRD v3.2 §D8 (2026-07-28); ngưỡng giá trị hàng bằng số tiền (BR-ORD-03) vẫn chưa có số (Deferred, C-ORD-02) |
| ASN | DOC-v1.0-01 | Điểm lấy/giao (OFFER), khung giờ | 2 | 1 | Không |
| DLV | DOC-v1.0-01 | Ảnh bằng chứng, vị trí GPS, chi phí (số tiền tự khai) | 2 | 1 | Không |
| GIFT | DOC-v1.0-01 | Loại quà (4 giá trị enum) | 1 | 1 | Không |
| CNL | DOC-v1.0-01, DOC-v1.0-02 | Lý do huỷ (text bắt buộc, tối thiểu 5 ký tự) | 1 | 1 | Có — min-length 5 ký tự (VAL-04, BRD v3.2 §D8.3, 2026-07-28) |
| NTF | DOC-v1.0-01 | — (nội dung mẫu, chưa final) | — | — | Không |
| TS | DOC-v1.0-01 | — (backend/log, không có input field UI) | — | — | Không |

## 6. Clarifications & Blockers
| # | Req ID | DOC Source | Vấn đề | Answer | Status | Ngày resolve | Ảnh hưởng |
|---|--------|-----------|--------|--------|--------|-------------|-----------|
| 1 | C-USR-01 | DOC-v1.0-01, DOC-v1.0-02, DOC-v1.0-04 | Demo/prototype hiển thị Hạng thành viên + Điểm ECO + Điểm uy tín, nhưng BRD (USR-05, A7) khẳng định KHÔNG tính điểm/tier/CO2 | BA/PO xác nhận (2026-07-27, qua chat): **phase sau** — v1.0 CHƯA có rule/logic phân hạng "Hạng Đồng hành"; badge (nếu build) chỉ hiển thị dạng text tĩnh, không có cơ chế tính toán | Resolved — Out of scope v1.0 (deferred to future phase) | 2026-07-27 | REQ-USR-004, SC-USR-004 (không viết TC logic phân hạng) |
| 2 | C-ORD-01 | DOC-v1.0-02, DOC-v1.0-01 (BRD v3.2 §D8) | Wizard đăng tin không có validate bắt buộc — Loại hàng/Giá trị (B1), Người nhận (B2) đều có thể để trống; maxlength cụ thể chưa có số | BA/PO xác nhận (2026-07-27): CÓ rule bắt buộc. **Cập nhật 2026-07-28 (BRD v3.2 §D8.1/D8.2):** đã có đủ maxlength cụ thể — Ghi chú ≤300 ký tự, Địa chỉ lấy/giao hàng ≤200 ký tự, Điểm xuất phát (OFFER) ≤200 ký tự, Tên người nhận 2–60 ký tự, khung giờ tối thiểu cách nhau 30 phút | **Resolved — đầy đủ, không còn follow-up** | 2026-07-28 (maxlength) | REQ-ORD-002, REQ-ORD-012, SC-ORD-007, SC-ORD-027, SC-ORD-028 |
| 3 | C-ORD-02 | DOC-v1.0-01, DOC-v1.0-04 | Ngưỡng giá trị hàng (BR-ORD-03) + có bắt buộc ảnh khi vượt ngưỡng — chưa có con số | BA/PO xác nhận (2026-07-27): **phase này chưa làm** — v1.0 chưa triển khai rule ngưỡng giá trị hàng/cảnh báo bảo hiểm | Resolved — Out of scope v1.0 (deferred to future phase) | 2026-07-27 | REQ-ORD-009, SC-ORD-013 (không viết BVA cho ngưỡng ở v1.0) |
| 4 | C-ORD-03 | DOC-v1.0-01 | Hạn tin mặc định (ORD-06 "quá hạn cấu hình") — chưa có giá trị cụ thể | BA/PO xác nhận (2026-07-27): hạn tin = **giá trị người dùng đã CHỌN** lúc đăng tin (khoảng "Từ ngày/Đến ngày" ở Bước 2/3) — không phải hằng số hệ thống cố định; đến đúng "Đến ngày" đã chọn thì tin tự động chuyển EXPIRED/huỷ | Resolved — hạn tin theo giá trị user chọn, không phải default cố định | 2026-07-27 | REQ-ORD-004, SC-ORD-005 |
| 5 | C-ORD-04 | DOC-v1.0-01, DOC-v1.0-02 | Chip "Thuốc/Y tế" vẫn là lựa chọn hợp lệ ở Loại hàng dù nguyên tắc cấm gửi thuốc — cơ chế validate chặn hay chỉ cảnh báo tĩnh chưa rõ | BA/PO xác nhận (2026-07-27): **phase hiện tại có thể chọn bất kỳ** loại hàng nào kể cả "Thuốc/Y tế" — v1.0 chưa triển khai validate chặn theo danh mục cấm, banner cảnh báo chỉ mang tính thông tin tĩnh | Resolved — v1.0 không chặn, mọi loại hàng chọn được | 2026-07-27 | REQ-ORD-010, SC-ORD-014 (không viết TC negative chặn "Thuốc/Y tế") |
| 6 | C-ASN-01 | DOC-v1.0-01, DOC-v1.0-02 | Thời điểm lộ SĐT chưa nhất quán — banner nói SĐT chỉ lộ SAU KHI ghép, nhưng demo Chi tiết tin hiện sẵn SĐT+nút Gọi ngay từ "Chờ ghép" | BA/PO xác nhận (2026-07-27): **rule chính thức = lộ sau ghép** (khớp BRD BR-CON-02); hành vi demo hiện tại (lộ sớm ở "Chờ ghép") là bug, KHÔNG phải hành vi mong muốn | Resolved — SĐT chỉ lộ sau khi ghép, theo BRD | 2026-07-27 | REQ-ASN-002/003, SC-ASN-003 |
| 7 | C-ASN-02 | DOC-v1.0-01, DOC-v1.0-02 | OPR-05 cấm tự khớp chính mình, nhưng demo cho phép chủ tin/Người nhận của đơn tự bấm "Tôi mang giúp được" trên tin liên quan đến mình | BA/PO xác nhận (2026-07-27): **không được phép** — khớp OPR-05; hành vi demo hiện tại (cho phép tự nhận) là bug | Resolved — cấm tự nhận, theo OPR-05 | 2026-07-27 | REQ-ASN-008, SC-ASN-011 |
| 8 | C-DLV-01 | DOC-v1.0-01, DOC-v1.0-02, DOC-v1.0-04 | Ai được xác nhận "Đã nhận" — DLV-03 (D3) ghi RECEIVER/SENDER, nhưng BR-INT-03 (A5) + demo docx §5.2 chỉ cho phép Receiver | Ảnh Figma xác nhận nhất quán qua nhiều màn (5dc3ce81c, 7d8b4a8cf, 82d9aace4, 8563adc1, 91b08fb1): nút "Xác nhận đã nhận hàng" CHỈ active với Receiver; Sender/Carrier ở cùng bước "Đã giao" chỉ thấy nhãn disabled "Đã giao · chờ người nhận xác nhận" | Resolved — Receiver-only | 2026-07-24 | REQ-DLV-003, SC-DLV-005/011 |
| 9 | C-DLV-02 | DOC-v1.0-01 | Chia sẻ vị trí (GPS-01) mặc định bật/tắt — BRD tự nêu câu hỏi mở, chưa có câu trả lời | BA/PO xác nhận (2026-07-27): **phase sau** — default bật/tắt chưa chốt ở v1.0 | Open (non-blocking) — default value deferred to future phase | 2026-07-27 (ghi nhận, chưa chốt số) | REQ-DLV-002, SC-DLV-003 |
| 10 | C-DLV-03 | DOC-v1.0-02, DOC-v1.0-04 | 2 phiên bản màn "Xác nhận đã nhận hàng" — modal đơn giản (§5.2) vs form đầy đủ có ảnh bằng chứng + điểm uy tín carrier (§5.3) — chưa chốt bản chính thức | BA/PO xác nhận (2026-07-27): **chốt theo Figma** — bản modal đơn giản ("Xác nhận" / "Bạn xác nhận đã nhận được hàng từ người vận chuyển?" / nút Huỷ-Xác nhận) là thiết kế chính thức; form đầy đủ KHÔNG áp dụng ở v1.0 | Resolved — modal đơn giản là chính thức | 2026-07-27 | SC-DLV-005/011 |
| 11 | C-GIFT-01 | DOC-v1.0-01, DOC-v1.0-04 | RAT-01/02 (đánh giá 1-5 sao) mâu thuẫn trực tiếp với BR-INT-06/A7/A8 (không đánh giá sao); NT-07 + A10 KPI lại ngầm giả định có rating | BA/PO xác nhận (2026-07-27): **phase sau** — rating 1-5 sao chưa triển khai ở v1.0 (chỉ tồn tại dạng text mẫu trong notification, chưa có màn thao tác chấm sao) | Resolved — Out of scope v1.0 (deferred to future phase) | 2026-07-27 | REQ-GIFT-002 (không viết TC luồng chấm sao ở v1.0) |
| 12 | C-NTF-01 | DOC-v1.0-01, DOC-v1.0-02, DOC-v1.0-04 | 9 loại thông báo trong demo (Table 4, gồm "đánh giá 5 sao", "cộng đồng đạt mốc X đơn") khác nội dung với NTF-01..09 trong BRD | User note (2026-07-27): **chưa tổng hợp lại cụ thể có tất cả bao nhiêu loại** — đã tổng hợp 3 nguồn (BRD D6, demo Table 4, Figma DOC-v1.0-04) thành 1 bảng unified bên dưới (§6.1 C-NTF-01) để BA review/chọn danh sách chính thức dễ hơn | Open (non-blocking) — cần BA chọn danh sách chính thức từ bảng tổng hợp | 2026-07-27 (ghi nhận, chưa chốt danh sách) | REQ-NTF-001 |
| 13 | C-NTF-02 | DOC-v1.0-01 | Nhiều tham số vận hành chưa chốt: bán kính/định nghĩa "cùng tuyến", độ lệch khung giờ cho phép, chu kỳ quét khớp (D7); ngưỡng nhắc, gộp thông báo (D6) — chính BRD tự ghi "Chờ BA bổ sung" | BA/PO xác nhận (2026-07-27): định nghĩa khớp tuyến = **trùng địa chỉ giao hàng đã chọn** + **khung giờ phù hợp** (KHÔNG dùng bán kính GPS/khoảng cách địa lý) | Partially Resolved — đã chốt cơ chế match (địa chỉ + khung giờ); vẫn cần chốt cụ thể "khung giờ phù hợp" (trùng hoàn toàn hay có độ lệch cho phép) + chu kỳ quét khớp/ngưỡng gộp thông báo | 2026-07-27 (partial) | REQ-ASN-006, REQ-NTF-001/002 |
| 14 | C-TS-01 | DOC-v1.0-01 | Admin Web Portal (A3) chưa có đặc tả UI/màn hình cụ thể ở cả 2 tài liệu | BA/PO xác nhận (2026-07-27): **phase sau** — Admin Web Portal chưa triển khai/chưa có đặc tả ở v1.0 | Resolved — Out of scope v1.0 (deferred to future phase) | 2026-07-27 | REQ-TS-002, SC-TS-003 |
| 15 | C-CNL-01 | DOC-v1.0-01, DOC-v1.0-02 | Màn "Báo sự cố" (Incident) chưa có đặc tả field cụ thể — chỉ nhắc tên trong phụ lục + vài rule liên quan | BA/PO xác nhận (2026-07-27): **phase sau** — màn "Báo sự cố" chưa có đặc tả field ở v1.0 | Resolved — Out of scope v1.0 (deferred to future phase) | 2026-07-27 | REQ-DLV-005 (phần "tạo sự cố" deferred) |
| 16 | C-ORD-05 | DOC-v1.0-04 | Màn "Đăng tin thành công!" tồn tại 2 biến thể ngay trên cùng board Figma — 1 bản CÓ trường "Mã tin" (vd `#ECO-2026-0451`), 1 bản KHÔNG có — mâu thuẫn nội bộ nguồn thiết kế, đồng thời đối lập với US-D02 (DOC-v1.0-01, "KHÔNG hiển thị mã đơn — mã kỹ thuật vô nghĩa với người dùng") | — (chưa có câu trả lời) | Open (non-blocking, ảnh hưởng SC-ORD-003) | — | REQ-ORD-001, SC-ORD-003 |
| 17 | C-USR-02 | DOC-v1.0-01, DOC-v1.0-04 | USR-07 "Cấu hình kênh liên hệ sẽ lộ" (SĐT bắt buộc/Workplace-email tuỳ chọn) chỉ có trong BRD text — KHÔNG xuất hiện ở bất kỳ ảnh Figma nào (DOC-v1.0-04) của màn Cá nhân (chỉ có avatar/tên/phòng ban/badge tier/2 số liệu/menu) | BA/PO xác nhận (2026-07-27): **phase sau** — tính năng cấu hình kênh liên hệ không thuộc scope UI v1.0 | Resolved — Out of scope v1.0 (deferred to future phase) | 2026-07-27 | REQ-USR-005, SC-USR-005 |
| 18 | C-USR-03 | DOC-v1.0-01 | USR-02 "Xem/cập nhật hồ sơ" — BRD khẳng định có chức năng cập nhật hồ sơ (tên, SĐT, avatar, phòng ban, khu vực, kênh liên hệ) | QA xác nhận trực tiếp trên app STG thật: màn Cá nhân KHÔNG có chức năng cập nhật/sửa hồ sơ nào — toàn bộ 6 trường chỉ ở dạng xem (view-only) | Resolved — view-only, không có update | 2026-07-24 | REQ-USR-002, SC-USR-002 |
| 19 | C-ORD-06 | Quan sát thực tế app | Empty state của màn Hoạt động (Đơn của tôi), màn Quà đã nhận, và màn Thông báo khi không có data — chưa có trong BRD/PRD/Figma, không có text chính thức | **QA GiangDC2 xác nhận trực tiếp (2026-07-28): text "Hiện tại chưa có dữ liệu" là copy THẬT hiển thị trên UI app STG (cả 3 màn), không còn là đề xuất chờ duyệt** | **Resolved** — QA xác nhận đúng UI thật, dùng làm final copy | 2026-07-28 (Resolved, xác nhận qua UI thật — trước đó 2026-07-27 ghi nhận dạng đề xuất) | REQ-ORD-011/SC-ORD-023, REQ-GIFT-001/SC-GIFT-006, REQ-NTF-001/SC-NTF-007 |
| 20 | C-NTF-03 | DOC-v1.0-04, Quan sát thực tế app | (a) Nút "Đánh dấu đã đọc" + chấm đỏ chưa đọc CÓ trên UI (Figma) nhưng KHÔNG có mô tả cơ chế khi bấm/tap (mark-all vs mark-per-item); (b) KHÔNG có đặc tả phân trang/lazy-load cho màn Thông báo ở bất kỳ tài liệu nào | **QA GiangDC2 xác nhận trực tiếp (2026-07-28): cả 2 hành vi (a) tap 1 item → đánh dấu riêng / nút header → mark-all, và (b) scroll cuối danh sách → tự động load thêm, đều là hành vi THẬT trên UI app STG, không còn là suy luận theo UX chuẩn** | **Resolved** — QA xác nhận đúng hành vi thật trên UI | 2026-07-28 (Resolved, xác nhận qua UI thật — trước đó 2026-07-27 ghi nhận dạng suy luận) | REQ-NTF-001/SC-NTF-008, REQ-NTF-001/SC-NTF-009 |

**Nguồn câu trả lời BA/PO (2026-07-27):** QA GiangDC2 tổng hợp qua chat trực tiếp với BA/PO — xem chi tiết Analyst Note cập nhật trong §6.1 bên dưới per clarification.

### 6.1. Clarification Source Detail (per `references/quoting-guide.md` EC6)

#### C-USR-01 — Demo hiển thị tier/điểm/CO2, BRD nói không có (Partially Resolved)

**Source Quote (ambiguous):**
> "USR-05 Hiển thị tổng số đơn đã giúp + tổng số quà ảo đã nhận (không tính điểm/CO₂)" (DOC-v1.0-01 §A6) — đối lập — "Hạng thành viên | 🔒 'Hạng Đồng hành' — cơ chế tier/gamification... 3 chỉ số | Đơn đã giúp (12) · Điểm uy tín (4.8) · Điểm ECO (540)" (DOC-v1.0-02 Table 10, §3.9) — và mục tiêu sản phẩm ghi trong chính DOC-v1.0-02 §1.2: "Xây dựng động lực tham gia bằng cơ chế ghi nhận đóng góp: điểm ECO, điểm uy tín, hạng thành viên, thống kê cộng đồng (số đơn, số người, CO₂ tiết kiệm)."

**Source Location:** `DOC-v1.0-01 §A6/§A7` + `DOC-v1.0-02 §1.2, §3.9 Table 10`

**Source Quote (DOC-v1.0-04 — Figma "Cá nhân", ảnh `570ad9d32e3dbdf44c72d6140826f0e6f9a3393e` + `e5764b10a94b0d51fab023c1a92b6f25732cb402`, đã zoom 4x xác nhận):**
> Header cam: Avatar + "Nguyễn Anh Tuấn" / "Phòng Vận hành · MNV: FTEL3382" / badge pill nhỏ "🏆 Hạng Đồng hành". Card trắng bên dưới: 2 số liệu "12" — "đơn đã giúp" và "8" — "quà đã nhận". Menu: "Đơn của tôi", "Quà đã nhận". KHÔNG có "Điểm ECO", "Điểm uy tín" hay bất kỳ con số điểm/CO₂ nào trên màn hình.

**Source Location:** `DOC-v1.0-04 — images/570ad9d32e3dbdf44c72d6140826f0e6f9a3393e, e5764b10a94b0d51fab023c1a92b6f25732cb402`

**Analyst Note:** BRD v3.1 (ngày cập nhật mới hơn, 23/07/2026) rõ ràng loại bỏ điểm/tier/CO2 khỏi scope v1.0, nhưng prototype tham chiếu (mà D1 BRD tự nhận là "đồng bộ với") vẫn có đầy đủ các yếu tố này. Ảnh thiết kế Figma thực tế (DOC-v1.0-04) cho kết quả **TRUNG GIAN** giữa 2 nhánh: **CÓ** hiển thị badge tier dạng text "🏆 Hạng Đồng hành" (khớp 1 phần nhánh demo — "Hạng thành viên" tồn tại), nhưng **KHÔNG** có "Điểm ECO (540)"/"Điểm uy tín (4.8)" dạng số nào cả (khớp 1 phần nhánh BRD — "không tính điểm/CO₂").

**Update 2026-07-27 (BA/PO xác nhận):** Cơ chế phân hạng "Hạng Đồng hành" thuộc **phase sau** — v1.0 chưa có rule tính tier. → **Resolved — Out of scope v1.0 (deferred).** Nếu badge tier xuất hiện trên UI thực tế, chỉ coi là hiển thị tĩnh (display-only); generate-tc KHÔNG viết TC test logic lên hạng/ngưỡng phân hạng cho REQ-USR-004/SC-USR-004 ở v1.0.

#### C-USR-02 — Cấu hình kênh liên hệ (USR-07) không có bằng chứng UI (Open — GAP)

**Source Quote (BRD, chỉ 1 nguồn):**
> "USR-07 Cấu hình kênh liên hệ sẽ lộ: SĐT (bắt buộc), Workplace/email (tùy chọn)"

**Source Location:** `DOC-v1.0-01 §A6 "Actors & Hồ sơ (chung)" · row USR-07`

**Đối chiếu UI (DOC-v1.0-04 + app STG thật):** Ảnh Figma màn Cá nhân đã zoom xác nhận (`570ad9d32e3dbdf44c72d6140826f0e6f9a3393e`, `e5764b10a94b0d51fab023c1a92b6f25732cb402` — xem C-USR-01) chỉ có: avatar, tên, "Phòng [ban] · MNV", badge tier, 2 số liệu (đơn đã giúp/quà đã nhận), menu "Đơn của tôi"/"Quà đã nhận" — KHÔNG có mục cấu hình kênh liên hệ nào. QA GiangDC2 xác nhận trực tiếp trên app STG (2026-07-24): không tìm thấy màn/toggle nào để bật-tắt hiển thị SĐT/email ở bất kỳ đâu trong app.

**Analyst Note:** Áp dụng rule mới `Project_rule.md §10.1` (UI Figma phải khớp tài liệu mới được viết TC) — vì 2 nguồn KHÔNG khớp, generate-tc KHÔNG được viết TC khẳng định vị trí/hành vi UI cho USR-07. `SC-USR-005` giữ nguyên trong scenario map nhưng cần gắn cờ GAP; nếu generate-tc chạy trước khi có xác nhận BA, chỉ nên viết dạng "GAP finding" (rà toàn app xác nhận không có UI) thay vì TC test hành vi bật/tắt. Cần BA/PO xác nhận: (a) tính năng này có thực sự nằm trong scope UI v1.0 không, (b) nếu có, nó nên nằm ở đâu (màn Cá nhân, hay 1 màn Cài đặt riêng chưa được thiết kế/chưa có trong bộ ảnh Figma).

**Update 2026-07-27 (BA/PO xác nhận):** **Phase sau** — tính năng "Cấu hình kênh liên hệ" (USR-07) KHÔNG thuộc scope UI v1.0. → **Resolved — Out of scope v1.0 (deferred to future phase).** generate-tc cho REQ-USR-005/SC-USR-005 chỉ viết 1 "GAP/negative finding" xác nhận tính năng chưa tồn tại ở v1.0 (nếu cần), KHÔNG viết TC hành vi bật/tắt kênh liên hệ.

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

**Update 2026-07-27 (BA/PO xác nhận):** CÓ rule — validate bắt buộc cho Loại hàng/Giá trị (B1) + toàn bộ Người nhận (B2); có maxlength cho các trường text (giá trị cụ thể per field: **TBD, BA bổ sung sau**); có thể có thêm rule validate khác do BA bổ sung tiếp theo dõi. → **Resolved.** generate-tc viết TC validate bắt buộc (để trống → chặn "Tiếp theo"/báo lỗi) thay cho nhánh "để trống vẫn qua"; boundary test maxlength chờ BA cung cấp con số cụ thể (follow-up item).

**Update 2026-07-28 (BRD v3.2 §D8.1/D8.2, follow-up đã có câu trả lời):** Maxlength cụ thể per field nay đã đầy đủ — Ghi chú ≤300 ký tự; Địa chỉ lấy hàng / Địa chỉ giao hàng ≤200 ký tự; Điểm xuất phát (OFFER) ≤200 ký tự; Tên người nhận 2–60 ký tự; SĐT chuẩn VN (10 số, đầu 0); khung giờ (cả NEED lẫn OFFER) yêu cầu "đến > từ" và khoảng cách tối thiểu 30 phút. Thêm 2 rule so-sánh-field mới: Địa chỉ giao hàng phải KHÁC địa chỉ lấy hàng; Điểm đến (OFFER) phải KHÁC điểm xuất phát. → **Resolved — đầy đủ, không còn follow-up.** Xem `REQ-ORD-012` (Source Detail đầy đủ) + scenario mới `SC-ORD-027` (maxlength/ảnh), `SC-ORD-028` (khung giờ tối thiểu 30 phút) tại `test_scenario_map.md`.

#### C-ORD-02 — Ngưỡng giá trị hàng chưa xác định (Resolved — Deferred)

**Source Quote (ambiguous):**
> "Câu hỏi mở cho BA — Ngưỡng giá trị hàng? Ảnh bắt buộc cho hàng > ngưỡng?"

**Source Location:** `DOC-v1.0-01 §D5 "Edge Cases · Data Model · KPI" · "Câu hỏi mở cho BA"`

**Analyst Note:** Chính BRD tự liệt kê đây là câu hỏi mở, chưa có câu trả lời. Không thể viết test data Boundary Value Analysis cho BR-ORD-03 (REQ-ORD-009) khi chưa có con số ngưỡng cụ thể.

**Update 2026-07-27 (BA/PO xác nhận):** **Phase này chưa làm** — v1.0 không có rule ngưỡng giá trị hàng/cảnh báo bảo hiểm. → **Resolved — Out of scope v1.0 (deferred to future phase).** Không còn BLOCKER: generate-tc KHÔNG viết BVA cho ngưỡng giá trị hàng ở REQ-ORD-009/SC-ORD-013 tại v1.0; đánh dấu REQ-ORD-009 là Deferred trong traceability.

**Update 2026-07-28 (BRD v3.2 §D8.1, phân biệt 2 cơ chế — KHÔNG đảo ngược Resolved ở trên):** D8.1 mô tả field "Giá trị hàng" là **chip chọn categorical** (thấp/vừa/cao, đã biết từ DOC-v1.0-02) với hành vi cụ thể mới: *"Chọn Giá trị cao → hiện cảnh báo trách nhiệm tự thoả thuận"*. Đây là cơ chế ĐANG CÓ SẴN ở v1.0 (banner cảnh báo tĩnh, không có logic ngưỡng số tiền) — **KHÁC HẲN** với BR-ORD-03 (REQ-ORD-009, ngưỡng giá trị hàng bằng SỐ TIỀN cụ thể + bắt buộc ảnh khi vượt ngưỡng) vẫn đang **Deferred out-of-scope v1.0** theo xác nhận BA/PO 2026-07-27. Kết luận: `SC-ORD-013` được viết lại (un-deferred) để test đúng cơ chế categorical này thay vì tiếp tục giữ trạng thái DEFERRED — xem `test_scenario_map.md` SC-ORD-013 (updated 2026-07-28). `REQ-ORD-009`/BR-ORD-03 (ngưỡng số tiền) tiếp tục Deferred, không đổi.

#### C-ORD-03 — Hạn tin mặc định chưa xác định (Resolved)

**Source Quote (ambiguous):**
> "Hạn tin mặc định?" (mục Câu hỏi mở cho BA)

**Source Location:** `DOC-v1.0-01 §D5 "Edge Cases · Data Model · KPI" · "Câu hỏi mở cho BA"`

**Analyst Note:** Liên quan REQ-ORD-004 (ORD-06/US-D04) — "quá hạn cấu hình" không có giá trị số cụ thể (bao nhiêu giờ/ngày). Non-blocking cho happy-path test (verify tin CÓ chuyển EXPIRED) nhưng blocker cho test đúng THỜI ĐIỂM chuyển (cần môi trường test có thể set hạn ngắn hoặc mock thời gian).

**Update 2026-07-27 (BA/PO xác nhận):** Hạn tin KHÔNG phải hằng số hệ thống — bằng **giá trị "Đến ngày" mà user đã chọn** ở Bước 2/3 (Block "Thời gian", `test_scenario_map.md`); đến đúng ngày đó tin tự động chuyển EXPIRED/huỷ. → **Resolved.** generate-tc viết TC theo hướng: tạo tin với "Đến ngày" = ngày test gần (vd hôm nay/ngày mai) → verify tự động EXPIRED đúng thời điểm đó, thay vì test theo 1 con số hạn cố định.

#### C-ORD-04 — Chip "Thuốc/Y tế" vẫn hợp lệ dù cấm gửi thuốc (Resolved)

**Source Quote (ambiguous):**
> "Loại hàng | Chip chọn 1: Tài liệu (mặc định) · Đồ điện tử · Thực phẩm · Hàng nhỏ · Đồ dễ vỡ · Quần áo · Thuốc/Y tế · Khác" (Table 6, §3.5.1) — đối chiếu — "Cấm gửi: thuốc, vũ khí, chất nguy hiểm, hàng phi pháp." (§1.4)

**Source Location:** `DOC-v1.0-02 §3.5.1 Table 6` + `§1.4 "Nguyên tắc cốt lõi"`

**Analyst Note:** Chip "Thuốc/Y tế" (bao gồm cả các sản phẩm y tế hợp pháp không phải "thuốc cấm") có thể hợp lý nếu ý là "vật tư y tế nói chung" chứ không phải riêng "thuốc" — nhưng label trùng chữ "Thuốc" với danh mục cấm gây nhầm lẫn UX và khó xác định pass/fail khi test.

**Update 2026-07-27 (BA/PO xác nhận):** **Phase hiện tại có thể chọn bất kỳ** loại hàng nào kể cả "Thuốc/Y tế" — v1.0 chưa triển khai validate chặn theo danh mục cấm, banner cảnh báo (Bước 3/3) chỉ mang tính thông tin tĩnh, không có cơ chế chặn thật. → **Resolved.** generate-tc viết TC xác nhận có thể chọn/đăng thành công với mọi chip Loại hàng kể cả "Thuốc/Y tế" ở v1.0; KHÔNG viết TC negative kỳ vọng hệ thống chặn.

#### C-ASN-01 — Thời điểm lộ SĐT chưa nhất quán (Resolved)

**Source Quote (ambiguous):**
> "⚠ Lưu ý: Màn 'Đăng tin mới' cam kết SĐT chỉ lộ SAU KHI ghép, nhưng thực tế Chi tiết tin đã hiển thị sẵn SĐT + nút Gọi của Người gửi ngay từ trạng thái 'Chờ ghép' (chưa ai xác nhận mang giúp). Cần xác nhận đây có phải hành vi dự kiến."

**Source Location:** `DOC-v1.0-02 §3.4 "Màn hình Chi tiết tin"`

**Analyst Note:** Mâu thuẫn trực tiếp với BR-CON-02 (BRD, REQ-ASN-003): *"trước khi ghép không lộ SĐT"*. Nếu hành vi hiện tại của demo (SĐT hiện sớm) là bug cần fix, SC-ASN-003 (P1) sẽ là regression test quan trọng.

**Update 2026-07-27 (BA/PO xác nhận):** **Rule chính thức = lộ sau ghép** (khớp BRD BR-CON-02). Hành vi demo hiện tại (SĐT hiện sớm ở "Chờ ghép") là **bug**, không phải hành vi mong muốn. → **Resolved.** generate-tc/vibe-test viết SC-ASN-003 khẳng định SĐT KHÔNG hiển thị khi trạng thái = "Chờ ghép" (POSTED), CHỈ hiển thị sau khi chuyển "Đã ghép" (MATCHED); nếu app thật vẫn lộ sớm khi vibe-test → log bug, không coi là pass.

#### C-ASN-02 — Chủ tin/Người nhận có thể tự "nhận mang giúp" đơn của mình (Resolved)

**Source Quote (ambiguous):**
> "9 | Chủ tin / Người nhận có thể tự 'nhận mang giúp' | Chi tiết tin cho phép chính chủ tin hoặc Người nhận của đơn tự bấm 'Tôi mang giúp được' trên tin liên quan đến mình — nên rà soát logic ẩn/hiện nút theo vai trò thực."

**Source Location:** `DOC-v1.0-02 §7 "Các điểm cần làm rõ" · Table 17 row 9`

**Analyst Note:** Vi phạm trực tiếp OPR-05 (REQ-ASN-008): *"Không gợi ý tin do chính người đó đăng; người gửi ≠ người vận chuyển của cùng một đơn"*.

**Update 2026-07-27 (BA/PO xác nhận):** **Không được phép** — khớp OPR-05; hành vi demo hiện tại (cho phép tự nhận) là bug. → **Resolved.** generate-tc/vibe-test viết SC-ASN-011 khẳng định nút "Tôi mang giúp được" PHẢI ẩn/disable khi người xem = chủ tin hoặc Người nhận của chính đơn đó; nếu app thật vẫn hiện nút → log bug.

#### C-DLV-01 — Ai được xác nhận "Đã nhận" (Resolved — Receiver-only)

**Source Quote (ambiguous):**
> "DLV-03 RECEIVER/SENDER xác nhận đã nhận" (DOC-v1.0-01 §D3) — đối lập — "BR-INT-03 Hoàn thành cần người nhận xác nhận đã nhận hàng" (DOC-v1.0-01 §A5) — và — "⇒ Đây là quyền hạn ĐẶC BIỆT DUY NHẤT của vai trò Người nhận: chỉ Người nhận mới có thể chốt đơn 'Hoàn thành' — Người vận chuyển chỉ đưa đơn tới 'Đã giao' rồi phải chờ." (DOC-v1.0-02 §5.2)

**Source Location:** `DOC-v1.0-01 §D3 row DLV-03, §A5 row BR-INT-03` + `DOC-v1.0-02 §5.2 "Màn hình Theo dõi đơn (nhãn phụ 'Tôi nhận hàng')"`

**Source Quote (DOC-v1.0-04 — Figma, xác nhận qua nhiều ảnh độc lập, đã zoom xác nhận nội dung popup):**
> Receiver ("Tôi nhận hàng"), bước "Đã giao": nút cam active **"Xác nhận đã nhận hàng"** (`7d8b4a8cf5c78355a0977f13fa8f1ae3d3b96091`) → bấm ra popup "Xác nhận" — "Bạn xác nhận đã nhận được hàng từ người vận chuyển?" — nút Huỷ/Xác nhận (`5dc3ce81c38a42c96f6bf3f6bab751e90dcfa3fe`, `82d9aace478ba585169b74e5bdedec3053e96bbe`). CÙNG bước "Đã giao": Sender thấy nhãn DISABLED "Đã giao · chờ người nhận xác nhận" (`8563adc10d2b0697bff7c2f68c4839008ffa5f16`); Carrier cũng thấy nhãn DISABLED tương tự (`91b08fb10c09ab34d0943d1999b891b029a96526`). Carrier có hành động RIÊNG, độc lập, ở bước "Đang giao": nút "Đã giao cho người nhận" (`e1699c4f6f52bd9bf1c1277d4db122fb3d0aa978`) → popup "Xác nhận" — "Bạn xác nhận đã giao hàng tận tay người nhận?" (`ca5e7239037e6d21a5fc337235100d6abfb31e6a`) — đây là Carrier TỰ BÁO đã giao xong (chuyển POSTED→"Đã giao"), KHÁC với Receiver xác nhận đã NHẬN (chuyển "Đã giao"→"Hoàn thành").

**Source Location:** `DOC-v1.0-04 — images/7d8b4a8cf5c78355a0977f13fa8f1ae3d3b96091, 5dc3ce81c38a42c96f6bf3f6bab751e90dcfa3fe, 82d9aace478ba585169b74e5bdedec3053e96bbe, 8563adc10d2b0697bff7c2f68c4839008ffa5f16, 91b08fb10c09ab34d0943d1999b891b029a96526, e1699c4f6f52bd9bf1c1277d4db122fb3d0aa978, ca5e7239037e6d21a5fc337235100d6abfb31e6a`

**Analyst Note:** 3/4 nguồn (BR-INT-03 + demo/docx §5.2 + Figma DOC-v1.0-04, nguồn có độ tin cậy cao nhất vì là ảnh thiết kế UI thực tế) đồng thuận CHỈ Receiver được xác nhận "Đã nhận hàng"; chỉ DLV-03 (D3, văn bản BA nháp) nói cả Receiver/Sender. **Resolved theo hướng Receiver-only.** Phát hiện thêm quy trình 2 bước tách biệt rõ ràng: (1) Carrier bấm "Đã giao cho người nhận" ở bước "Đang giao" → chuyển "Đã giao"; (2) Receiver bấm "Xác nhận đã nhận hàng" ở bước "Đã giao" → chuyển "Hoàn thành". Sender không có action nào ở cả 2 bước, chỉ xem trạng thái. generate-tc dùng Receiver làm actor chính cho REQ-DLV-003/SC-DLV-005/SC-DLV-011; vẫn khuyến nghị 1 dòng note cho BA xác nhận chính thức trước khi đóng hẳn DLV-03 (D3) như lỗi văn bản.

#### C-DLV-02 — Chia sẻ vị trí mặc định bật/tắt (Open — deferred)

**Source Quote (ambiguous):**
> "Chia sẻ vị trí mặc định bật/tắt?"

**Source Location:** `DOC-v1.0-01 §D5 "Edge Cases · Data Model · KPI" · "Câu hỏi mở cho BA"`

**Analyst Note:** Liên quan GPS-01 (REQ-DLV-002). Non-blocking cho happy-path (verify chia sẻ vị trí hoạt động khi user bật) nhưng ảnh hưởng Given ban đầu của SC-DLV-003 (mặc định OFF hay ON khi vào màn Theo dõi đơn ở trạng thái IN_TRANSIT).

**Update 2026-07-27 (BA/PO xác nhận):** Giá trị default cụ thể là **phase sau** — chưa chốt ở v1.0. → Giữ **Open (non-blocking)**, đánh dấu rõ default value deferred to future phase. generate-tc viết SC-DLV-003 theo hướng "verify tính năng chia sẻ vị trí hoạt động đúng khi user chủ động bật/tắt", KHÔNG assert cứng trạng thái default ban đầu.

#### C-DLV-03 — 2 phiên bản màn "Xác nhận đã nhận hàng" chưa chốt (Resolved)

**Source Quote (ambiguous):**
> "Trong quá trình khảo sát, phát hiện thêm một biến thể đầy đủ hơn của hành động xác nhận nhận hàng... có thể là bản thiết kế đầy đủ dự kiến, trong khi modal đơn giản ở Mục 5.2 là bản rút gọn dùng cho luồng demo đồng bộ 3 màn... ⚠ Lưu ý: Cần xác nhận với đội thiết kế: bản chính thức dùng form đầy đủ này (có ảnh bằng chứng) hay modal xác nhận đơn giản như ở Mục 5.2 — vì đây là 2 cách triển khai khác nhau cho CÙNG một hành động nghiệp vụ."

**Source Location:** `DOC-v1.0-02 §5.3 "Màn hình 'Xác nhận đã nhận hàng' (phiên bản chi tiết)"`

**Analyst Note (cập nhật DOC-v1.0-04):** Đã quét toàn bộ 82 ảnh Figma — chỉ tìm thấy bản **modal đơn giản** ("Xác nhận" / "Bạn xác nhận đã nhận được hàng từ người vận chuyển?" / nút Huỷ-Xác nhận, xem C-DLV-01) ở MỌI ảnh liên quan tới bước xác nhận nhận hàng. KHÔNG có ảnh nào cho thấy form đầy đủ (thông tin Carrier + điểm uy tín + ảnh bằng chứng) như mô tả ở DOC-v1.0-02 §5.3.

**Update 2026-07-27 (BA/PO xác nhận):** **Chốt theo Figma** — bản modal đơn giản là thiết kế chính thức của v1.0; form đầy đủ (§5.3, ảnh bằng chứng + điểm uy tín) KHÔNG áp dụng ở v1.0. → **Resolved.** generate-tc viết SC-DLV-005/SC-DLV-011 CHỈ theo bản modal đơn giản; Screen "Xác nhận đã nhận hàng (đầy đủ)" trong `test_scenario_map.md` đánh dấu Out-of-scope v1.0 (tham khảo, không derive TC).

#### C-GIFT-01 — RAT-01/02 mâu thuẫn nguyên tắc "không đánh giá sao" (Partially Resolved)

**Source Quote (ambiguous):**
> "RAT-01/02 Đánh giá 2 chiều 1–5 sao + nhận xét" (DOC-v1.0-01 §D3) — đối lập — "BR-INT-06 Không đánh giá sao; ghi nhận thiện chí bằng quà ảo người gửi tặng người vận chuyển sau khi hoàn tất" (§A5) — và — "Phạm vi hiện tại: chỉ ghi log + admin can thiệp hỗ trợ. KHÔNG có chấm sao/đánh giá, KHÔNG có chặn (block) người dùng." (§A8) — nhưng — "Rating average > 4.0/5.0" vẫn xuất hiện trong bảng KPI nền tảng (§A10)

**Source Location:** `DOC-v1.0-01 §D3 row RAT-01/02, §A5 row BR-INT-06, §A8, §A10 "KPIs chung"`

**Source Quote (DOC-v1.0-04 — Figma "Thông báo", đã zoom 4x xác nhận, ảnh `db4dfb7e4f07138be5712aff5cb7dea61d983353` + `1c6c57c1a6356fee121b59007f85478d244d43d2`):**
> "Đơn đã hoàn thành — đánh giá ngay" — ""Gửi đồ ăn sáng" đã giao xong. Hãy đánh giá Trần Thị Lan để giúp cộng đồng tin cậy hơn." · "Bạn nhận được đánh giá 5 sao" — "Phạm Quốc Hùng: "Đúng giờ, nhiệt tình, sẽ nhớ tiếp lần sau!"" (icon ngôi sao cam). Đồng thời, màn "Tặng quà" (`5d29d0821b4abe7e831646cdad7fa6cdbea69118`, `165aaa39e070e12b4fe61084d05b47959a3111ba`) và popup "Đã gửi lời cảm ơn!" (`808c25763c360700f941f055a2c2e9923ee53a31`, `851d2b9f636f0e6682ccbf1093f8929028b7cb92`) chỉ có 4 icon quà (Bông hoa/Ly cà phê/Gấu bông/Vương miện) — KHÔNG có UI sao 1-5 ở đây.

**Source Location:** `DOC-v1.0-04 — images/db4dfb7e4f07138be5712aff5cb7dea61d983353, 1c6c57c1a6356fee121b59007f85478d244d43d2, 5d29d0821b4abe7e831646cdad7fa6cdbea69118, 808c25763c360700f941f055a2c2e9923ee53a31`

**Analyst Note:** Mâu thuẫn gốc xuất hiện ở 4 vị trí khác nhau trong CÙNG 1 tài liệu BRD v3.1 (khả năng cao do sót nội dung từ version cũ chưa dọn hết ở D3/A10). Bằng chứng ảnh Figma (DOC-v1.0-04, nguồn thiết kế UI thực tế) cho thấy **tính năng đánh giá sao 1-5 THỰC SỰ TỒN TẠI** trong copy notification ("Bạn nhận được đánh giá 5 sao" kèm comment cụ thể) — trực tiếp mâu thuẫn với BR-INT-06 ("Không đánh giá sao"). Tuy nhiên, màn hình THAO TÁC chấm sao (nơi user thực sự bấm 1-5 sao) KHÔNG xuất hiện trong 82 ảnh đã quét — chỉ thấy màn Gift (icon quà, không sao).

**Update 2026-07-27 (BA/PO xác nhận):** **Phase sau** — rating 1-5 sao chưa triển khai ở v1.0 (dòng notification "Bạn nhận được đánh giá 5 sao" chỉ là text mẫu/leftover chưa dọn, không phải tính năng đang hoạt động). → **Resolved — Out of scope v1.0 (deferred to future phase).** generate-tc KHÔNG viết TC cho luồng chấm sao/nhận đánh giá sao ở REQ-GIFT-002 tại v1.0; đánh dấu Deferred trong traceability. Notification "đánh giá 5 sao" (nếu còn xuất hiện trên app thật) nên được ghi nhận là nội dung chưa dọn, không phải chức năng cần test.

#### C-NTF-01 — Nội dung 9 thông báo demo khác BRD

**Source Quote (ambiguous):**
> "Có người muốn mang giúp đơn của bạn | ... · Bạn nhận được đánh giá 5 sao | Kèm nhận xét từ đối tác đơn hàng · ... · Cộng đồng FoxEco vừa đạt mốc X đơn | Thông điệp 'tiết kiệm Y kg CO₂' — gamification"

**Source Location:** `DOC-v1.0-02 §3.2 "Màn hình Thông báo" · Table 4`

**Analyst Note:** Danh sách 9 loại thông báo trong demo/docx không khớp NTF-01..09 (BRD D6) — đặc biệt có 2 loại liên quan trực tiếp tới các tính năng đã bị BRD loại bỏ (đánh giá sao — xem C-GIFT-01; CO2/gamification — xem C-USR-01). Non-blocking cho REQ-NTF-001 (test theo danh sách BRD D6, đã là nguồn mới hơn) nhưng củng cố thêm bằng chứng cho 2 clarification kia.

**Cập nhật 2026-07-24 (DOC-v1.0-04):** Ảnh Figma thực tế cho ra danh sách THỨ BA (xem REQ-NTF-001 §4.1 Source Quote #2) — cũng khác cả BRD D6 lẫn demo Table 4. Trùng với demo Table 4 ở điểm có "đánh giá 5 sao"; KHÔNG có "cộng đồng đạt mốc X đơn" (CO2/gamification) ở bất kỳ đâu trong 82 ảnh — củng cố nhánh "CO2/gamification không có trong scope v1.0" (khớp C-USR-01), nhưng làm YẾU đi nhánh "rating không có trong scope" (đối lập C-GIFT-01). DOC-v1.0-04 nên là nguồn verbatim ưu tiên cho generate-tc vì là artifact thiết kế gốc.

**Update 2026-07-27 (bảng tổng hợp unified — theo yêu cầu user "chưa tổng hợp lại cụ thể có tất cả bao nhiêu loại"):** Dưới đây là toàn bộ nội dung 3 nguồn xếp theo cùng 1 hàng sự kiện, để BA chọn danh sách chính thức 1 lần thay vì đọc rời rạc 3 nguồn.

| # | Sự kiện / Người nhận | BRD D6 (NTF-xx) | Demo Table 4 (§3.2) | Figma thực tế (DOC-v1.0-04, đã xác nhận ảnh) | Ghi chú |
|---|----------------------|------------------|----------------------|-----------------------------------------------|---------|
| 1 | Carrier ngỏ ý/ghép ngay [Sender] | NTF-01: "Đã có người nhận mang giúp đơn của bạn — SĐT đã được lộ để liên hệ" (ghép NGAY, lộ SĐT) | "Có người muốn mang giúp đơn của bạn" — "[Tên] ngỏ ý mang giúp '...'. Xác nhận để lộ SĐT." (chỉ "ngỏ ý", cần xác nhận riêng mới lộ SĐT) | Không quan sát riêng biệt (có thể trùng với hàng #2 dưới) | BRD vs Demo khác nhau về THỜI ĐIỂM lộ SĐT (ghép ngay vs cần xác nhận thêm) — liên quan C-ASN-01 |
| 2 | Ghép thành công [cả 2 bên] | NTF-02: "Đơn gửi tới bạn đã có người vận chuyển nhận giao" [Người nhận] | "Ghép thành công — SĐT đã được lộ" — "Thông báo khi hai bên đã ghép đơn" | "Ghép thành công — SĐT đã được lộ" — "Bạn và Trần Thị Lan đã được kết nối. Liên hệ để sắp xếp..." (khớp GẦN NHƯ Y HỆT text Demo) | Figma khớp Demo, khác câu chữ BRD — dùng Figma/Demo cho verbatim |
| 3 | Khớp tuyến gợi ý [Carrier] | NTF-03: "Tìm thấy đơn hàng phù hợp tuyến của bạn — xem chi tiết để nhận giao" | "Có chuyến đi mới hợp tuyến của bạn" — "Gợi ý chuyến của người khác trùng cung đường" | "Tìm thấy đơn hàng phù hợp tuyến của bạn" — "Có người cần gửi... trùng tuyến bạn đã đăng..." (khớp gần với BRD NTF-03 hơn Demo) | 3 nguồn diễn đạt khác nhau nhưng cùng 1 sự kiện |
| 4 | Carrier đã lấy hàng [Sender+Receiver] | NTF-04: "Người vận chuyển đã lấy hàng và bắt đầu giao" | "Người mang giúp đã nhận hàng" — "Cập nhật khi carrier xác nhận lấy hàng" | Không quan sát trong 82 ảnh đã quét | — |
| 5 | Carrier đã giao (DELIVERED) [Receiver+Sender] | NTF-05: "Đơn đã được giao — vui lòng xác nhận đã nhận hàng" | Không có mục riêng (có thể gộp vào #6) | Không quan sát | — |
| 6 | Receiver xác nhận nhận → COMPLETED [Sender+Carrier] | NTF-06: "Đơn đã hoàn tất — cảm ơn bạn!" | "Đơn đã hoàn thành — đánh giá ngay" — "Nhắc đánh giá sau khi hoàn tất" | "Đơn đã hoàn thành — đánh giá ngay" — ""...đã giao xong. Hãy đánh giá [Carrier]..."" (khớp Y HỆT Demo) | Demo/Figma gắn kèm lời mời ĐÁNH GIÁ — xem C-GIFT-01 (đã Resolved: rating deferred, phase sau) |
| 6b | Nhận được đánh giá 5 sao [Carrier] | Không có mục tương ứng | "Bạn nhận được đánh giá 5 sao" — "Kèm nhận xét từ đối tác đơn hàng" | "Bạn nhận được đánh giá 5 sao" — "[Tên]: 'Đúng giờ, nhiệt tình...'" (khớp Y HỆT Demo) | Loại thông báo MỚI so với BRD — theo C-GIFT-01 (Resolved 2026-07-27: rating out-of-scope v1.0) → loại này KHÔNG áp dụng cho v1.0 |
| 7 | Nhận quà ảo [Carrier] | NTF-07: "Bạn nhận được một món quà cảm ơn 🎁 — mở Trang cá nhân để xem" | Không có mục riêng | "Bạn nhận được một món quà cảm ơn 🎁" — "[Tên] đã gửi tặng bạn một món quà..." (khớp gần BRD) | Dùng cho REQ-GIFT-001 (trong scope v1.0) |
| 8 | Đơn bị huỷ [các bên còn lại] | NTF-08: "Đơn đã bị huỷ bởi [vai trò] — lý do: […]" | Không có mục riêng | "Đơn của bạn đã bị người vận chuyển huỷ" — "Lý do: 'bận họp gấp'. Đơn đang chờ người vận chuyển mới..." | Figma cụ thể hơn BRD (thêm câu "đang chờ người mới"), dùng làm verbatim ưu tiên |
| 9 | Tin quá hạn chưa ghép [Sender] | NTF-09: "Tin của bạn đã quá hạn — gỡ hoặc đăng lại nếu vẫn cần" | Không có mục riêng | Không quan sát | Liên quan REQ-ORD-004/C-ORD-03 (đã Resolved: hạn theo giá trị user chọn) |
| 10 | Nhắc khung giờ hẹn giao [Sender/Receiver] | Không có mục tương ứng | "Sắp đến khung giờ hẹn giao" — "Nhắc lịch giao hàng" | "Sắp đến khung giờ hẹn giao" — "Đơn của bạn hẹn giao trong khung 17:00–18:30 hôm nay." (khớp Y HỆT Demo) | Loại MỚI so với BRD, có mặt cả Demo lẫn Figma → khả năng cao THUỘC scope thật, BRD D6 có thể sót |
| 11 | Cộng đồng đạt mốc X đơn (gamification/CO2) | Không có mục tương ứng | "Cộng đồng FoxEco vừa đạt mốc X đơn" — "Thông điệp 'tiết kiệm Y kg CO₂'" | Không quan sát trong 82 ảnh | Theo C-USR-01 (Resolved 2026-07-27: tier/điểm/CO2 deferred, phase sau) → loại này KHÔNG áp dụng cho v1.0 |
| 12 | Nhắc nguyên tắc an toàn (static) | Không có mục tương ứng | "Nhắc lại nguyên tắc an toàn" — "Không gửi/nhận hàng cấm" | Không quan sát | Thông báo tĩnh, không gắn sự kiện nghiệp vụ cụ thể |

**Khuyến nghị cho BA/PO:** chọn 1 trong 3 hướng — (a) dùng nguyên BRD D6 (9 loại, NTF-01..09) làm chuẩn — đơn giản nhất nhưng thiếu 3 loại đã thấy trên UI thật (#6b, #10 xác nhận có trên Figma; #11/#12 chỉ có ở Demo); (b) dùng Figma + Demo (khớp nhau ở hầu hết các dòng) làm chuẩn, bỏ #6b/#11 vì đã Resolved deferred (rating/tier); (c) hợp nhất cả 3 thành danh sách mới ~10 loại (bỏ #6b, #11 theo 2 clarification đã resolved; giữ lại #10 "nhắc khung giờ" vì có bằng chứng UI thật). Cho tới khi BA chọn, generate-tc tạm dùng hướng (c) làm baseline vì có bằng chứng UI thật nhiều nhất. Status vẫn giữ Open (non-blocking) — chưa chốt chính thức.

#### C-NTF-02 — Nhiều tham số vận hành "Chờ BA bổ sung"

**Source Quote (ambiguous):**
> "Chờ BA bổ sung: bán kính/định nghĩa 'cùng tuyến', độ lệch khung giờ cho phép, chu kỳ quét khớp, hạ ưu tiên người huỷ nhiều lần, quy tắc ưu tiên khi nhiều carrier cùng tuyến." (§D7) — và — "Chờ BA bổ sung: ngưỡng thời gian nhắc, gộp/không gộp thông báo, thông báo cho người thứ 3 (VD người nhận khi carrier huỷ), cấu hình bật/tắt theo loại." (§D6)

**Source Location:** `DOC-v1.0-01 §D7 "Rule vận hành (Operating Rules)"` + `§D6 "Thông báo (Notifications)"`

**Analyst Note:** Doc TỰ đánh dấu các tham số này là chưa hoàn thiện ("Nháp — chờ BA review & bổ sung" xuất hiện ở cả D6 và D7). Non-blocking cho test happy-path (giá trị cụ thể không ảnh hưởng luồng chính) nhưng cần môi trường cấu hình được (hoặc mock) để test chính xác các ngưỡng khi giá trị thật được xác nhận.

**Update 2026-07-27 (BA/PO xác nhận):** Định nghĩa "khớp tuyến" (REQ-ASN-006) = **trùng địa chỉ giao hàng đã chọn** + **khung giờ phù hợp** — KHÔNG dùng bán kính GPS/khoảng cách địa lý như đề xuất ban đầu trong BRD. → **Partially Resolved.** generate-tc viết SC-ASN-009 theo hướng: 2 tin có ĐỊA CHỈ GIAO HÀNG trùng nhau + khung giờ giao nhau → match; địa chỉ khác nhau → không match (test rõ ràng "cùng địa chỉ chính xác" vs "khác địa chỉ hẳn" để tránh vùng xám). Vẫn CÒN MỞ: (a) "khung giờ phù hợp" nghĩa là trùng khung giờ hoàn toàn hay cho phép độ lệch (vd ±30 phút) — cần BA chốt thêm; (b) chu kỳ quét khớp (bao lâu quét 1 lần) và ngưỡng gộp thông báo (OPR-06/D6) vẫn chưa có số — defer BVA các tham số này tới khi có giá trị cụ thể.

**Update 2026-07-28 (BRD v3.2 — quan sát tài liệu, KHÔNG phải câu trả lời mới):** Dòng "Chờ BA bổ sung: bán kính/định nghĩa 'cùng tuyến', độ lệch khung giờ cho phép, chu kỳ quét khớp..." (§D7, quote gốc ở trên) đã bị **XOÁ khỏi BRD v3.2** — vị trí cuối §D7 nay là section mới `§D8 Validate & Giá trị mặc định` (không liên quan chủ đề khớp tuyến). Đây CHỈ là xoá text placeholder, KHÔNG kèm câu trả lời thay thế cho 3 câu hỏi mở (bán kính, độ lệch khung giờ, chu kỳ quét) — **status giữ nguyên Partially Resolved**, không nâng lên Resolved. §D6 (danh sách "Chờ BA bổ sung" về ngưỡng nhắc/gộp thông báo) không đổi giữa v3.1/v3.2.

#### C-TS-01 — Admin Web Portal chưa có đặc tả UI (Resolved — Deferred)

**Source Quote (ambiguous):**
> "Nền tảng: Mobile App (iOS/Android) + Admin Web Portal." (§A3) — không có mô tả màn hình/field nào khác cho Admin Web Portal trong toàn bộ 2 tài liệu.

**Source Location:** `DOC-v1.0-01 §A3 "Bộ sản phẩm & Thứ tự ưu tiên"`

**Analyst Note:** REQ-TS-002 (Admin can thiệp hỗ trợ) không có UI cụ thể để viết TC chi tiết. Non-blocking cho v1.0 (test scope giới hạn ở hệ quả quan sát được từ phía end-user), nhưng sẽ trở thành blocker nếu cần test trực tiếp chức năng Admin.

**Update 2026-07-27 (BA/PO xác nhận):** **Phase sau** — Admin Web Portal chưa triển khai/chưa có đặc tả ở v1.0. → **Resolved — Out of scope v1.0 (deferred to future phase).** generate-tc cho REQ-TS-002/SC-TS-003 chỉ viết TC hệ quả quan sát được từ phía end-user (vd đơn chuyển "chờ admin hỗ trợ" sau timeout); KHÔNG viết TC thao tác trực tiếp trên Admin Portal.

#### C-CNL-01 — Màn "Báo sự cố" chưa có đặc tả field (Resolved — Deferred)

**Source Quote (ambiguous):**
> "Báo sự cố | Cả 3 vai trò | —" (chỉ liệt kê tên màn trong phụ lục, không có field/nội dung cụ thể)

**Source Location:** `DOC-v1.0-02 §8 "Phụ lục — Danh sách toàn bộ màn hình đã khảo sát" · Table 18`

**Analyst Note:** Liên quan BR-ASN-03/REQ-DLV-005 (sau IN_TRANSIT phải tạo sự cố thay vì huỷ). Không có đặc tả field (loại sự cố, mô tả, ảnh đính kèm...) ở cả 2 doc. Non-blocking cho v1.0 (đủ để test "đường huỷ thường bị khoá + có đường thay thế Báo sự cố tồn tại"), cần bổ sung khi có thiết kế chi tiết màn này.

**Update 2026-07-27 (BA/PO xác nhận):** **Phase sau** — màn "Báo sự cố" (field cụ thể: loại sự cố, mô tả, ảnh đính kèm...) chưa có đặc tả/chưa triển khai ở v1.0. → **Resolved — Out of scope v1.0 (deferred to future phase).** REQ-DLV-005/SC-DLV-009 chỉ viết TC verify "đường huỷ thường bị khoá sau IN_TRANSIT + có lối thoát thay thế (nút/link 'Báo sự cố' tồn tại và điều hướng được)"; KHÔNG viết TC chi tiết field/submit form Báo sự cố.

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
| Quan sát thực tế app + DOC-v1.0-01 | 2026-07-27 | 13 | `fragments/TC-HOATDONG-v1.0.xlsx` (Mã CN TC_01, Screen "Hoạt động (Đơn của tôi)") | High:1, Medium:7, Low:5 | standard | N/A | ⏳ |
| DOC-v1.0-01, DOC-v1.0-02, DOC-v1.0-04, quan sát thực tế app | 2026-07-27 | 10 | `fragments/TC-CANHAN-v1.0.xlsx` (Mã CN TC_02, Screen "Cá nhân") | Medium:4, Low:6 | standard | N/A | ⏳ |
| DOC-v1.0-01, DOC-v1.0-04, DOC-v1.0-02, quan sát thực tế app | 2026-07-27 | 28 | `fragments/TC-NTF-v1.0.xlsx` (Mã CN TC_03, Screen "Thông báo") — REGENERATE comprehensive, thay thế bản standard 12 TC trước đó | Medium:14, Low:14 | comprehensive | B1, B2, B4 | ✅ 85/100 (CONDITIONAL, 2026-07-28) |
| Quan sát thực tế app + DOC-v1.0-01 | 2026-07-28 | 20 | `fragments/TC-HOATDONG-v1.0.xlsx` (Mã CN TC_01, Screen "Hoạt động (Đơn của tôi)") — REGENERATE comprehensive, thay thế bản standard 13 TC trước đó | High:1, Medium:12, Low:7 | comprehensive | B1, B2 | ✅ 85/100 (CONDITIONAL, 2026-07-28) |
| DOC-v1.0-01, DOC-v1.0-02, DOC-v1.0-04 (BRD v3.2 §D8.1/D8.2/D8.3) | 2026-07-28 | 100 | `fragments/TC-DANGTIN-v1.0.xlsx` (Mã CN TC_04, Screens: Đăng tin mới chọn vai trò / Wizard Bước 1-2-3 / Đăng tin thành công / Theo dõi đơn — Timeline / Đăng tin OFFER / Chỉnh sửa tin / Trang chủ-Hoạt động hết hạn) — 18 scenario nguồn (SC-ORD-001/002/003/004/005/006/007/008/009/010/011/012/013/014/027/028/029/030), + Coverage Matrix sheet — **REGENERATE 2026-07-28 (fix review findings, lần 1):** (1) tách toàn bộ Steps/Expected về đúng 1:1 (trước đó 66/94 TC dùng dòng Expected gộp range "1-2. ..."); (2) bổ sung TC completeness "Check đủ 2 lựa chọn hiển thị đúng nhãn" cho Block "2 lựa chọn" (Step 3b, trước đó thiếu); (3) bổ sung 3 TC mới cho SC-ORD-004 (P1, trước đó 0 TC ở bất kỳ đâu trong project) — Screen mới "Theo dõi đơn (Sender) — Timeline trạng thái". Tổng TC 94→98. **REGENERATE 2026-07-28 (lần 2, user yêu cầu rà lại completeness từng màn hình):** phát hiện 2 gap còn sót — Block "Đơn của tôi" (Trang chủ, 6 field: nhãn hướng/loại hàng\|giá trị/badge/Từ-Đến/progress 5 bước/"chạm để theo dõi") chưa có TC completeness dù được SC-ORD-003/004 tham chiếu trực tiếp; Block "Form điền sẵn" (Chỉnh sửa tin) thiếu TC riêng "đủ 2 nút Cập nhật/Huỷ chỉnh sửa". Đã bổ sung 2 TC. **Bỏ qua màn "Chi tiết tin" theo yêu cầu user — sẽ có bộ TC riêng sau.** Tổng TC 98→**100**. **Update lần 3 (2026-07-28):** làm giàu nội dung TC completeness "2 lựa chọn" (Screen "Đăng tin mới") từ 2 field lên đủ 5 field (subtitle "Bạn muốn làm gì?", banner cam kết không phí/không chat/không thanh toán + SĐT lộ sau ghép, mô tả verbatim 2 card) sau khi QA xác nhận qua ảnh Figma DOC-v1.0-04 hash `f821ba3087b8cc6e8065fbde6e327274d34482b2` — không đổi tổng TC (vẫn 100), chỉ nâng chất lượng nội dung 1 TC hiện có + đồng bộ `test_scenario_map.md` Block Definitions. | High:5, Medium:63, Low:32 | comprehensive | B1, B2, B3, B4, B6 | ✅ 85/100 (CONDITIONAL, capped — direct mode; 0 finding còn lại trong phạm vi đã audit, cap 85 do không có review-agent/AGENT.md) |
| DOC-v1.0-01, DOC-v1.0-02, DOC-v1.0-04, quan sát thực tế app | 2026-07-28 | 15 | `fragments/TC-CANHAN-v1.0.xlsx` (Mã CN TC_02, Screen "Cá nhân") — REGENERATE comprehensive, thay thế bản standard 10 TC trước đó | Medium:5, Low:10 | comprehensive | B1, B2 | ✅ 85/100 (CONDITIONAL, 2026-07-28) |
