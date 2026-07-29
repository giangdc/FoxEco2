# MEMORY — Analyze Requirements Output — v1.0

> Tạo bởi: skill analyze-requirements
> Cập nhật lần cuối: 2026-07-27 (lần 3) — bổ sung field-level detail cho Trang chủ + Bảng tin theo yêu cầu user (chuẩn bị generate-tc theo sheet-by-tab): +REQ-GENERAL-003 (Trang chủ dashboard, +SC-GENERAL-003/004) và +REQ-CARRIER-006 (Bảng tin/Chi tiết tin field-level: tag "Tin của bạn" EP, ảnh sản phẩm tuỳ chọn EP, +SC-CARRIER-008/009). +4 SC mới (2 case "Expected chưa xác định" vì chưa quan sát được trong demo — empty state, ảnh vắng mặt). Tổng nay 38 REQ, 51 SC.
> Cập nhật 2026-07-27 (lần 2) — tích hợp DOC-v1.0-03 (bản prototype cập nhật, verify qua Chrome MCP): +1 REQ/SC bottom nav (GENERAL), +1 REQ/SC xem lịch sử quà đã nhận (GIFT), **UNBLOCK NOTIFICATION + GIFT** (UI thật đã xác nhận tồn tại), ORDER-007/EXPIRED xác nhận 1 phần (UI có ở màn lịch sử Sender, feed công khai chưa verify). Phát hiện thêm 1 mâu thuẫn UI-vs-BRD mới (C-GENERAL-3, tier/điểm uy tín/điểm ECO — Open) và tái khẳng định C-GENERAL-2 (không rating sao) trước bằng chứng UI mới (user reconfirm). Trước đó cùng ngày: user resolve C-ORDER-2 (ngưỡng EXPIRED = mốc "Từ ngày") và C-GENERAL-2 BLOCKER (KHÔNG rating sao, chỉ quà ảo). 2026-07-24: tích hợp BRD v3.1 chính thức (DOC-v1.0-02), resolve 3 clarification, +9 REQ/+20 SC mới (6 module mới: OFFER/CANCEL/GIFT/NOTIFICATION/ADMIN/MEDIA)
> Parent version: — version đầu tiên

## 0. Version Context
- **Version:** v1.0
- **Parent:** — version đầu tiên
- **Delta type:** Major (khởi tạo)
- **Input folder:** 00_input/v1.0/
- **Shared docs applied:** Không
- **Analysis mode:** INIT

## 1. Project Overview
- **Dự án:** FoxEco — nền tảng kết nối 3 vai trò (Người gửi / Người vận chuyển / Người nhận) để nhờ nhau mang hộ đồ tiện đường.
- **Mô tả:** Bản demo hiện tại là 1 file HTML standalone mô phỏng 3 vai trò trên cùng 1 đơn hàng, đồng bộ trạng thái tức thời qua client-side store. Chưa có backend/multi-order thật.
- **Môi trường:** DEMO — URL: http://localhost:8765/

## 2. Document Registry (version-scoped)
| DOC ID | File | Loại | Ngày phân tích | Status | Modules liên quan |
|--------|------|------|---------------|--------|-------------------|
| DOC-v1.0-01 | `00_input/v1.0/DOC-v1.0-01-FoxEco-Flow-Spec.md` | Markdown (tổng hợp Figma board + verified UI behavior) | 2026-07-24 | Analyzed (superseded làm nguồn phụ — xem DOC-v1.0-02) | SENDER, CARRIER, RECEIVER, ORDER, GENERAL |
| DOC-v1.0-02 | `00_input/v1.0/FoxEco BRD/FoxEco BRD v3.1 (1).html` | HTML — Business Requirements Document chính thức (FPT Telecom, ngày 23/07/2026) | 2026-07-24 | Analyzed — nguồn chính thức cho business rule, ưu tiên hơn DOC-v1.0-01 khi có mâu thuẫn | SENDER, CARRIER, RECEIVER, OFFER, CANCEL, GIFT, NOTIFICATION, ORDER, ADMIN, MEDIA, GENERAL |
| DOC-v1.0-03 | `00_input/v1.0/DOC-v1.0-03-FoxEco-Design-Updated-Prototype.html` | HTML prototype — bản cập nhật của DOC-v1.0-01 (hash khác nhau, cùng layout 3 vai trò), verify trực tiếp qua Chrome MCP (localhost:8766) | 2026-07-27 | Analyzed — **nguồn chính thức cho UI thật đã dựng, ưu tiên hơn DOC-v1.0-01 khi có khác biệt UI** (BRD DOC-v1.0-02 vẫn ưu tiên cho business rule) | GENERAL (bottom nav), NOTIFICATION, GIFT, ORDER (EXPIRED UI) |

## 3. Module Summary
| Module | DOC Source | Tổng Req | Tổng SC | NEW | MODIFIED | CARRIED | DEPRECATED | P1 | P2 | P3 | Risk Level |
|--------|-----------|----------|---------|-----|----------|---------|-----------|----|----|----|-----------:|
| SENDER | DOC-v1.0-01, DOC-v1.0-02 | 6 | 10 | 10 | 0 | 0 | 0 | 6 | 4 | 0 | High |
| CARRIER | DOC-v1.0-01, DOC-v1.0-03 | 6 | 9 | 9 | 0 | 0 | 0 | 5 | 3 | 1 | High |
| RECEIVER | DOC-v1.0-01 | 2 | 4 | 4 | 0 | 0 | 0 | 3 | 1 | 0 | High |
| ORDER | DOC-v1.0-01, DOC-v1.0-02 | 4 | 7 | 7 | 0 | 0 | 0 | 3 | 4 | 0 | Medium |
| GENERAL | DOC-v1.0-01, DOC-v1.0-02, DOC-v1.0-03 | 3 | 4 | 4 | 0 | 0 | 0 | 0 | 2 | 2 | Low |
| OFFER | DOC-v1.0-02, DOC-v1.0-03 | 4 | 4 | 4 | 0 | 0 | 0 | 1 | 3 | 0 | Medium |
| CANCEL | DOC-v1.0-02, DOC-v1.0-03 | 4 | 4 | 4 | 0 | 0 | 0 | 4 | 0 | 0 | High |
| GIFT | DOC-v1.0-02, DOC-v1.0-03 | 4 | 4 | 4 | 0 | 0 | 0 | 0 | 1 | 3 | Low |
| NOTIFICATION | DOC-v1.0-02, DOC-v1.0-03 | 2 | 2 | 2 | 0 | 0 | 0 | 0 | 0 | 2 | Low |
| ADMIN | DOC-v1.0-02 | 1 | 1 | 1 | 0 | 0 | 0 | 0 | 0 | 1 | Low |
| MEDIA | DOC-v1.0-02 | 2 | 2 | 2 | 0 | 0 | 0 | 0 | 0 | 2 | Low |
| **Tổng** | | **38** | **51** | **51** | **0** | **0** | **0** | **22** | **18** | **11** | |

> **Cập nhật 2026-07-24 — tích hợp BRD v3.1 (DOC-v1.0-02):** SENDER +1 REQ/+2 SC (tự điền người nhận qua email công ty). ORDER +2 REQ/+3 SC (Chỉnh sửa đơn khi Chờ ghép, Tin quá hạn EXPIRED). +6 module hoàn toàn mới: OFFER, CANCEL, GIFT, NOTIFICATION, ADMIN, MEDIA. **Toàn bộ 20 SC mới đều TC Status = 🚫 Blocked** — BRD mô tả các tính năng này nhưng bản HTML prototype hiện tại CHƯA có UI implement, không thể viết TC Steps cụ thể cho màn hình chưa tồn tại (nguyên tắc "không tự bịa"). Xem §4.

> **Cập nhật 2026-07-27 (lần 2) — tích hợp DOC-v1.0-03 (bản prototype cập nhật):** phát hiện UI thật đã dựng cho những phần trước đó tưởng chưa có — **UNBLOCK NOTIFICATION và GIFT**. +3 SC mới: SC-GENERAL-002 (bottom nav 5 icon, cả 3 vai trò), SC-GIFT-004 (xem lịch sử "Quà đã nhận"), SC-NOTIFICATION-002 (đánh dấu tất cả đã đọc). SC-ORDER-007 (EXPIRED) xác nhận UI có thật ở màn lịch sử Sender nhưng CHƯA verify phía feed công khai — giữ nguyên 🚫 Blocked cho tới khi verify nốt. Xem §4 và §6 (2 clarification mới C-GENERAL-3, C-GIFT-2).

## 4. Scenario Index
| SC ID | Tên ngắn | Module | DOC Source | Priority | Test Type | Lifecycle | TC Status | Vibe Status | Vibe Date |
|-------|----------|--------|-----------|----------|-----------|-----------|-----------|-------------|-----------|
| SC-SENDER-001 | Màn chọn vai trò hiển thị đủ 2 lựa chọn | SENDER | DOC-v1.0-01 §1.1 | P2 | UI | NEW | ✅ | ⏳ | — |
| SC-SENDER-002 | Chọn "Tôi cần gửi hàng" mở wizard bước 1 | SENDER | DOC-v1.0-01 §1.1 | P1 | Functional | NEW | ✅ | ✅ | 2026-07-24 |
| SC-SENDER-003 | Điền wizard bước 1 → chuyển bước 2 | SENDER | DOC-v1.0-01 §1.2 | P1 | Functional | NEW | ✅ | ✅ | 2026-07-24 |
| SC-SENDER-004 | Điền wizard bước 2 → chuyển bước 3 tóm tắt | SENDER | DOC-v1.0-01 §1.3 | P1 | Functional | NEW | ✅ | ✅ | 2026-07-24 |
| SC-SENDER-005 | Chưa tick điều khoản → nút "Đăng tin ngay" không khả dụng | SENDER | DOC-v1.0-01 §1.4 | P1 | Validation | NEW | ✅ | ⏳ | — |
| SC-SENDER-006 | Tick điều khoản + đăng tin → thành công | SENDER | DOC-v1.0-01 §1.4 | P1 | Functional | NEW | ✅ | ✅ | 2026-07-24 |
| SC-SENDER-007 | UI smoke bước 3 — đủ block tóm tắt + cảnh báo + điều khoản | SENDER | DOC-v1.0-01 §1.4 | P2 | UI | NEW | ✅ | ⏳ | — |
| SC-SENDER-008 | Theo dõi đơn hiển thị timeline, mốc "Chờ ghép" active | SENDER | DOC-v1.0-01 §1.5 | P1 | UI | NEW | ✅ | ✅ | 2026-07-24 |
| SC-CARRIER-001 | UI smoke màn Chi tiết tin | CARRIER | DOC-v1.0-01 §2.1 | P2 | UI | NEW | ✅ (di chuyển sang sheet Bảng tin, 2026-07-27) | ✅ | 2026-07-24 |
| SC-CARRIER-002 | Nhận đơn thành công (posted → matched), đồng bộ 3 màn | CARRIER | DOC-v1.0-01 §2.2 | P1 | Functional | NEW | ✅ (di chuyển sang sheet Bảng tin, 2026-07-27) | ✅ | 2026-07-24 |
| SC-CARRIER-003 | Bấm "Huỷ" ở dialog xác nhận mang giúp → không đổi trạng thái | CARRIER | DOC-v1.0-01 §2.2 | P2 | Negative | NEW | ✅ (di chuyển sang sheet Bảng tin, 2026-07-27) | ⏳ | — |
| SC-CARRIER-004 | Lấy hàng thành công (matched → in_transit) | CARRIER | DOC-v1.0-01 §2.3 | P1 | Functional | NEW | ✅ | ✅ | 2026-07-24 |
| SC-CARRIER-005 | Giao hàng thành công (in_transit → delivered) | CARRIER | DOC-v1.0-01 §2.4 | P1 | Functional | NEW | ✅ | ✅ | 2026-07-24 |
| SC-CARRIER-006 | Carrier KHÔNG có nút tự hoàn tất đơn ở trạng thái "Đã giao" | CARRIER | DOC-v1.0-01 §2.4 | P1 | Negative/Permission | NEW | ✅ | ✅ | 2026-07-24 |
| SC-CARRIER-007 | Carrier tự động thấy "Hoàn thành" khi Receiver xác nhận (sync) | CARRIER | DOC-v1.0-01 §2.5 | P1 | Functional | NEW | ✅ | ✅ | 2026-07-24 |
| SC-CARRIER-008 | Tag "Tin của bạn" CHỈ hiện trên tin do chính mình đăng, KHÔNG hiện trên tin người khác | CARRIER | DOC-v1.0-03 (quan sát UI) | P2 | UI/EP | NEW | ✅ (sheet Bảng tin) | ✅ | 2026-07-27 |
| SC-CARRIER-009 | Ảnh sản phẩm ở Chi tiết tin — case KHÔNG có ảnh (tuỳ chọn theo REQ-SENDER-002) | CARRIER | DOC-v1.0-03 (⚠️ chưa quan sát được — chỉ thấy case CÓ ảnh) | P3 | UI/EP | NEW | ⏳ Ready (⚠️ user yêu cầu KHÔNG gen TC khi Expected chưa xác định — chờ hỏi lại trước) | ⏳ | — |
| SC-RECEIVER-001 | Block "Người giao hàng" ẩn khi đơn chưa ghép | RECEIVER | DOC-v1.0-01 §3.1 | P2 | Negative/UI | NEW | ✅ | ⏳ | — |
| SC-RECEIVER-002 | Block "Người giao hàng" hiện đúng dữ liệu sau khi đã ghép | RECEIVER | DOC-v1.0-01 §3.1 | P1 | Functional | NEW | ✅ | ✅ | 2026-07-24 |
| SC-RECEIVER-003 | Xác nhận đã nhận hàng thành công (delivered → completed) | RECEIVER | DOC-v1.0-01 §3.2 | P1 | Functional | NEW | ✅ | ✅ | 2026-07-24 |
| SC-RECEIVER-004 | CTA "Xác nhận đã nhận hàng" không hiện khi đơn chưa "Đã giao" | RECEIVER | DOC-v1.0-01 §3.2 | P1 | Negative/Permission | NEW | ✅ | ⏳ | — |
| SC-ORDER-001 | Badge trạng thái đúng label + màu theo từng mốc | ORDER | DOC-v1.0-01 §4 | P2 | UI | NEW | ✅ | ✅ | 2026-07-24 |
| SC-ORDER-002 | "↺ Chạy lại từ đầu" reset order status về "Chờ ghép" | ORDER | DOC-v1.0-01 §4 | P1 | Functional | NEW | ✅ | ✅ | 2026-07-24 |
| SC-ORDER-003 | Đồng bộ trạng thái tức thời cả 3 màn không cần reload | ORDER | DOC-v1.0-01 §4 | P1 | Functional | NEW | ✅ | ✅ | 2026-07-24 |
| SC-ORDER-004 | Mọi transition đều có dialog xác nhận trung gian (không transition thẳng) | ORDER | DOC-v1.0-01 §4 | P2 | UI/Consistency | NEW | ✅ | ✅ | 2026-07-24 |
| SC-GENERAL-001 | Banner "không thu phí/không chat/không thanh toán" hiển thị đúng nội dung | GENERAL | DOC-v1.0-01 §0 | P3 | UI Content | NEW | ✅ | ✅ | 2026-07-24 |
| SC-GENERAL-002 | Bottom nav (Trang chủ/Bảng tin/Đăng tin/Hoạt động/Cá nhân) điều hướng đúng màn, nhất quán cả 3 vai trò | GENERAL | DOC-v1.0-03 (quan sát UI) | P2 | UI/Navigation | NEW | ⏳ Ready | ✅ | 2026-07-27 |
| SC-GENERAL-003 | Trang chủ hiển thị đúng dashboard theo vai trò — Sender/Receiver "Đơn của tôi", Carrier "Tin mới" | GENERAL | DOC-v1.0-03 (quan sát UI) | P2 | UI/Functional | NEW | ✅ (sheet Trang chủ) | ✅ | 2026-07-27 |
| SC-GENERAL-004 | Empty state "Đơn của tôi" / "Tin mới" khi không có đơn/tin nào | GENERAL | DOC-v1.0-03 (⚠️ chưa quan sát được — demo luôn có sẵn dữ liệu mẫu) | P3 | UI/EP | NEW | ⏳ Ready (⚠️ user yêu cầu KHÔNG gen TC khi Expected chưa xác định — chờ hỏi lại trước) | ⏳ | — |
| SC-SENDER-009 | Nhập email công ty người nhận → tự điền tên/SĐT/địa chỉ | SENDER | DOC-v1.0-02 §D1b US-D18 | P2 | Functional | NEW | 🚫 Blocked | 🚫 N/A | — |
| SC-SENDER-010 | Email không có trong hệ thống → báo "Không tìm thấy · nhập thủ công" | SENDER | DOC-v1.0-02 §D1b US-D18 | P2 | Negative | NEW | 🚫 Blocked | 🚫 N/A | — |
| SC-OFFER-001 | Carrier đăng tin OFFER (điểm xuất phát/đến/khung giờ/tên/SĐT) thành công | OFFER | DOC-v1.0-02 §D1b US-D10; UI xác nhận DOC-v1.0-03 | P2 | Functional | NEW | ⏳ Ready | ✅ | 2026-07-27 |
| SC-OFFER-002 | Màn "Đã ghi nhận tuyến đường" hiển thị đúng giải thích (không công khai) | OFFER | DOC-v1.0-02 §D1b US-D11 | P2 | UI | NEW | ⏳ Ready (⚠️ chưa verify text màn kết quả, mới verify tới form) | ⏳ | — |
| SC-OFFER-003 | Carrier nhận thông báo khi có tin NEED khớp tuyến đã đăng | OFFER | DOC-v1.0-02 §D1b US-D12; UI xác nhận DOC-v1.0-03 (thấy notification "Có chuyến đi mới hợp tuyến") | P2 | Functional | NEW | ⏳ Ready | ✅ | 2026-07-27 |
| SC-OFFER-004 | Bấm "Nhận giao" từ thông báo → ghép (MATCHED) + lộ liên hệ | OFFER | DOC-v1.0-02 §D1b US-D13 | P1 | Functional | NEW | ⏳ Ready (⚠️ chưa verify riêng bước "Nhận giao") | ⏳ | — |
| SC-CANCEL-001 | Popup huỷ khoá nút "Xác nhận" tới khi nhập lý do | CANCEL | DOC-v1.0-02 §D1b US-D16; UI xác nhận DOC-v1.0-03 | P1 | Validation | NEW | ⏳ Ready | ✅ | 2026-07-27 |
| SC-CANCEL-002 | Huỷ đơn thành công kèm lý do, ghi rõ vai trò người huỷ | CANCEL | DOC-v1.0-02 §D1b US-D16 | P1 | Functional | NEW | ⏳ Ready (⚠️ chưa bấm Xác nhận thật để verify kết quả sau huỷ — dừng trước khi confirm để giữ nguyên state demo) | ⏳ | — |
| SC-CANCEL-003 | KHÔNG ai huỷ được khi đơn đã ở trạng thái "Đang giao" | CANCEL | DOC-v1.0-02 §D7 OPR-11 | P1 | Negative/Permission | NEW | ⏳ Ready (⚠️ chưa verify — mới thấy nút Huỷ ở "Chờ ghép") | ⏳ | — |
| SC-CANCEL-004 | Carrier huỷ khi đã ghép (chưa lấy hàng) → đơn trả về "Chờ ghép", hiện lại bảng tin | CANCEL | DOC-v1.0-02 §D7 OPR-09 | P1 | State | NEW | ⏳ Ready (⚠️ chưa verify riêng) | ⏳ | — |
| SC-GIFT-001 | Màn "Tặng quà" hiển thị đủ 4 loại quà (bông hoa/ly cà phê/gấu bông/vương miện) | GIFT | DOC-v1.0-02 §A7, §D1b US-D15; UI xác nhận DOC-v1.0-03 | P3 | UI | NEW | ⏳ Ready | ✅ | 2026-07-27 |
| SC-GIFT-002 | Chọn quà → bấm "Xác nhận tặng quà" → gửi thành công | GIFT | DOC-v1.0-02 §D1b US-D15; UI xác nhận DOC-v1.0-03 (⚠️ có nút xác nhận, khác text BRD "không cần xác nhận" — xem Analyst Note REQ-GIFT-002) | P2 | Functional | NEW | ⏳ Ready | ✅ | 2026-07-27 |
| SC-GIFT-003 | Người nhận quà thấy thông báo + màn "Quà đã nhận" cập nhật đếm theo loại + lịch sử | GIFT | DOC-v1.0-02 §D1b US-D20; UI xác nhận DOC-v1.0-03 (⚠️ quan sát ở phone Receiver, chưa xác nhận Carrier có màn này hay không — xem C-GIFT-2) | P3 | Functional | NEW | ⏳ Ready | ✅ | 2026-07-27 |
| SC-GIFT-004 | Xem lịch sử "Quà đã nhận" (tổng số + breakdown theo loại + danh sách người tặng/ngày) | GIFT | DOC-v1.0-03 (quan sát UI) | P3 | UI/Functional | NEW | ⏳ Ready | ✅ | 2026-07-27 |
| SC-NOTIFICATION-001 | 9 sự kiện thông báo (NTF-01→09) bắn đúng nội dung cho đúng người nhận | NOTIFICATION | DOC-v1.0-02 §D6; UI xác nhận DOC-v1.0-03 (màn "Thông báo" có thật, nhóm theo HÔM NAY/HÔM QUA/TUẦN NÀY) | P3 | Functional | NEW | ⏳ Ready | ✅ | 2026-07-27 |
| SC-NOTIFICATION-002 | Bấm "Đánh dấu đã đọc" → toàn bộ thông báo hết trạng thái chưa đọc (red dot) | NOTIFICATION | DOC-v1.0-03 (quan sát UI) | P3 | Functional | NEW | ⏳ Ready | ✅ | 2026-07-27 |
| SC-ORDER-005 | Nút "Chỉnh sửa" chỉ hiện ở "Chờ ghép", mở form điền sẵn dữ liệu cũ | ORDER | DOC-v1.0-02 §D1b US-D19 | P2 | Functional | NEW | 🚫 Blocked | 🚫 N/A | — |
| SC-ORDER-006 | Sau khi đã "Đã ghép" trở đi, KHÔNG cho sửa đơn nữa | ORDER | DOC-v1.0-02 §D4 BR-EDIT-01 | P1 | Negative/Permission | NEW | 🚫 Blocked | 🚫 N/A | — |
| SC-ORDER-007 | Tin quá hạn cấu hình chưa ghép → tự chuyển "EXPIRED", hiện badge "Hết hạn" | ORDER | DOC-v1.0-02 §D1b US-D04; DOC-v1.0-03 xác nhận 1 phần (badge "Hết hạn" có thật ở màn lịch sử Sender, feed công khai CHƯA verify) | P2 | State | NEW | 🚫 Blocked (partial) | 🚫 N/A | — |
| SC-ADMIN-001 | Admin có quyền override trên các hành động chính (chấp nhận/đã nhận/đã giao/xác nhận/huỷ) | ADMIN | DOC-v1.0-02 §D4 Permission Matrix | P3 | Permission | NEW | 🚫 Blocked | 🚫 N/A | — |
| SC-MEDIA-001 | Carrier chụp ảnh hàng lúc nhận (tùy chọn, làm bằng chứng) | MEDIA | DOC-v1.0-02 §D3 PUP-03 | P3 | Functional | NEW | 🚫 Blocked | 🚫 N/A | — |
| SC-MEDIA-002 | Chia sẻ vị trí GPS khi đang giao (tùy chọn, tắt sau khi đóng đơn) | MEDIA | DOC-v1.0-02 §D3 GPS-01 | P3 | Functional | NEW | 🚫 Blocked | 🚫 N/A | — |

> **Vibe Status ✅ (2026-07-24):** các scenario đánh dấu ✅ đã được verify thủ công qua Chrome MCP trong 2 lần chạy full-flow trước khi phân tích này (xem hội thoại) — kết quả khớp hành vi mô tả. Các scenario ⏳ (validation/negative/UI-detail chưa test riêng: SC-SENDER-001/005/007, SC-CARRIER-003, SC-RECEIVER-001/004) cần chạy `vibe-test` bổ sung.
>
> **🚫 Blocked (2026-07-24 — tích hợp BRD v3.1):** 20 scenario mới (SC-SENDER-009/010, SC-OFFER-*, SC-CANCEL-*, SC-GIFT-*, SC-NOTIFICATION-001, SC-ORDER-005/006/007, SC-ADMIN-001, SC-MEDIA-*) được BRD đặc tả chi tiết nhưng **hoàn toàn chưa có UI** trong bản HTML prototype hiện tại (`FoxEco Demo 3 vai tro (standalone)`). Không thể vibe-test hay viết TC Steps cụ thể cho màn hình chưa dựng. Đây là scope GAP giữa BRD (đích) và prototype (hiện trạng) — cần dev implement trước khi generate-tc/vibe-test cho nhóm này.
>
> **✅ UNBLOCK (2026-07-27 — tích hợp DOC-v1.0-03):** User cung cấp bản prototype cập nhật (`FoxEco Design.html`, hash khác DOC-v1.0-01) — verify trực tiếp qua Chrome MCP phát hiện UI thật đã tồn tại cho **NOTIFICATION** (màn "Thông báo" đầy đủ, nhóm theo ngày) và **GIFT** (flow tặng quà chạy được: Hoạt động → Đơn của tôi → tab "Đã hoàn thành" → tap đơn → màn "Tặng quà" → chọn 1/4 quà → "Xác nhận tặng quà"; + màn "Quà đã nhận" xem lịch sử). SC-GIFT-001/002/003 và SC-NOTIFICATION-001 chuyển từ 🚫 Blocked → ⏳ Ready (sẵn sàng generate-tc, chưa generate). SC-ORDER-007 (EXPIRED) xác nhận 1 phần — badge "Hết hạn" có thật ở màn lịch sử Sender, nhưng CHƯA verify hành vi ở feed công khai (Bảng tin) nên giữ nguyên 🚫 Blocked. Thêm mới: SC-GENERAL-002 (bottom nav), SC-GIFT-004 (xem lịch sử quà), SC-NOTIFICATION-002 (đánh dấu đã đọc) — cả 3 đã verify UI, TC Status ⏳ Ready. **Phát hiện đồng thời 1 mâu thuẫn UI-vs-BRD mới:** màn "Tặng quà" có nút xác nhận rõ ràng, khác text BRD "gửi ngay không cần xác nhận" (minor, không blocking). Xem §6 Clarifications: addendum C-GENERAL-2, mới C-GENERAL-3 (Open), C-GIFT-2 (Open, non-blocking).
>
> **✅ UNBLOCK bổ sung (2026-07-27, cùng đợt) — OFFER và CANCEL:** Verify tiếp qua Chrome MCP xác nhận CẢ 2 module này cũng đã có UI thật trong DOC-v1.0-03:
> - **OFFER:** Bấm nút "Đăng tin" (+) → màn "Bạn muốn làm gì?" hiện lại đúng 2 lựa chọn như Figma gốc ("Tôi cần gửi hàng" / "Tôi nhận giao hàng") → chọn "Tôi nhận giao hàng" → mở form đầy đủ: Thông tin của tôi (tên/SĐT tự điền), Điểm xuất phát (A, tự điền), Điểm đến (B), Khoảng thời gian (Từ ngày/Đến ngày), Thời gian di chuyển (Khởi hành/Đến nơi), checkbox điều khoản, nút "Đăng tin ngay" (disabled tới khi điền đủ) — khớp đúng BRD US-D10.
> - **CANCEL:** Từ màn "Theo dõi đơn" (Trang chủ → tap đơn "Đơn của tôi" → "Chạm để theo dõi đơn") ở trạng thái "Chờ ghép", cuối màn có 2 nút "✏️ Chỉnh sửa" và "❌ Huỷ đơn". Bấm "Huỷ đơn" → popup "Huỷ đơn hàng" với text "Bạn chắc chắn muốn huỷ đơn hàng này? Thao tác không thể hoàn tác.", textarea "Lý do huỷ *" (bắt buộc, placeholder "VD: đổi lịch, không cần gửi nữa..."), 2 nút "Huỷ"/"Xác nhận" — "Xác nhận" khoá tới khi nhập lý do. Khớp đúng BRD US-D16. **Chưa bấm Xác nhận thật** (để tránh thay đổi state demo ngoài dự kiến) — SC-CANCEL-002/003/004 (kết quả sau khi huỷ thật, permission ở trạng thái khác, Carrier huỷ) vẫn cần verify thêm khi generate-tc/vibe-test thật sự chạy TC.
> SC-OFFER-001..004 và SC-CANCEL-001..004 chuyển từ 🚫 Blocked → ⏳ Ready. Xem §6: C-SENDER-1 và C-CARRIER-1 cập nhật trạng thái Unblocked.

### 4.1. Source Detail (verbatim quotes — mandatory per `references/quoting-guide.md`)

#### REQ-SENDER-001 — Chọn vai trò khi đăng tin

**Source Quote:**
> "Từ trang chủ, bấm nút "+" (Đăng tin) ở bottom nav → hiện màn "Bạn muốn làm gì?" với 2 lựa chọn:
> - "Tôi cần gửi hàng" — "Bạn có hàng cần gửi, tìm đồng nghiệp đi thuận đường mang hộ"
> - "Tôi nhận giao hàng" — "Bạn đang có nhu cầu đi chuyển và có thể nhận giao hàng giúp cho đồng nghiệp""

**Source Location:** `DOC-v1.0-01 §1.1 "Chọn vai trò" · bullet list`

**Analyst Note:** Entry point của luồng đăng tin có rẽ nhánh vai trò. Chỉ nhánh "Tôi cần gửi hàng" implement được trong bản demo — nhánh còn lại xem Clarification C-SENDER-1.

#### REQ-SENDER-002 — Form bước 1: chi tiết hàng

**Source Quote:**
> "Loại hàng (chip chọn 1): Tài liệu / Đồ điện tử / Thực phẩm / Hàng nhỏ / Đồ dễ vỡ / Quần áo / Thuốc·Y tế / Khác ... Giá trị hàng (ước tính) (chip chọn 1): Giá trị thấp / Giá trị vừa / Giá trị cao ... Nút "Tiếp theo" — luôn khả dụng kể cả khi chưa chọn loại hàng"

**Source Location:** `DOC-v1.0-01 §1.2 "Form bước 1 — Chi tiết hàng" · bullet list`

**Analyst Note:** 8 loại hàng, 3 mức giá trị, ghi chú tự do, ảnh không bắt buộc. Hành vi "Tiếp theo luôn khả dụng kể cả chưa chọn loại hàng" là quan sát thực tế nhưng chưa rõ có phải hành vi mong muốn hay thiếu validation — không đoán, đã ghi Clarification C-SENDER-2 (test data catalog).

#### REQ-SENDER-003 — Form bước 2: người gửi/người nhận/lịch

**Source Quote:**
> "Người nhận: tên, SĐT, địa chỉ giao hàng — nhập tay, 3 field text. Khoảng thời gian (ngày): Từ ngày — Đến ngày (date picker). Khung giờ mong muốn: Từ — Đến (time picker)."

**Source Location:** `DOC-v1.0-01 §1.3 "Form bước 2 — Người gửi / Người nhận / Lịch"`

**Analyst Note:** Người gửi pre-filled (không sửa được trong demo), Người nhận nhập tay 3 field. Chưa rõ ràng buộc validate format SĐT/rỗng — xem test_data_catalog ghi chú nguồn.

#### REQ-SENDER-004 — Tóm tắt & đăng tin, điều khoản bắt buộc

**Source Quote:**
> "Nút "Đăng tin ngay" — disabled cho tới khi tick checkbox điều khoản sử dụng (đã verify qua browser: nút không phản hồi click khi checkbox chưa tick — cần verify lại bằng test case P1)."

**Source Location:** `DOC-v1.0-01 §1.4 "Bước 3 — Tóm tắt & đăng tin"`

**Analyst Note:** Ràng buộc quan trọng P1: checkbox điều khoản là gate bắt buộc. Cảnh báo hàng cấm và text điều khoản là UI copy cố định — có scenario UI riêng verify nội dung hiển thị đúng (SC-SENDER-007).

#### REQ-SENDER-005 — Theo dõi đơn (Sender)

**Source Quote:**
> "Màn "Theo dõi đơn" hiển thị timeline 5 mốc: Chờ ghép → Lấy hàng → Đang giao → Đã giao → Hoàn thành, kèm lộ trình (Lấy hàng / Giao hàng), ảnh sản phẩm, và trạng thái nút cuối trang thay đổi theo mốc hiện tại"

**Source Location:** `DOC-v1.0-01 §1.5 "Theo dõi đơn (Sender)"`

**Analyst Note:** Timeline dùng chung UI component cho cả 3 vai trò (xem REQ-ORDER-001). Sender không có CTA hành động — chỉ theo dõi (read-only).

#### REQ-CARRIER-001 — Xem tin & chi tiết

**Source Quote:**
> "Feed "Tin mới" trên trang chủ Carrier hiển thị list đơn đang chờ ghép ... Bấm vào item → màn "Chi tiết tin" ... CTA cuối trang: nút cam "Tôi mang giúp được""

**Source Location:** `DOC-v1.0-01 §2.1 "Xem tin & xem chi tiết"`

**Analyst Note:** Màn chi tiết tin tổng hợp nhiều block thông tin (ảnh, thông tin hàng, lộ trình, khung giờ, người gửi) — cần UI smoke scenario cấp trang verify đủ block (SC-CARRIER-001) theo nguyên tắc UI coverage tối thiểu.

#### REQ-CARRIER-002 — Nhận đơn (posted → matched)

**Source Quote:**
> "Bấm "Tôi mang giúp được" → dialog xác nhận: [...] Bấm "Xác nhận" → trạng thái đơn chuyển posted → matched ("Chờ ghép" → "Đã ghép") — đồng bộ tức thời cả 3 màn (đã verify)."

**Source Location:** `DOC-v1.0-01 §2.2 "Nhận đơn (Chờ ghép → Đã ghép)"`

**Analyst Note:** Core transition đầu tiên trong order status machine. Có dialog xác nhận trung gian (Huỷ/Xác nhận) — 2 scenario: happy path (SC-CARRIER-002) và huỷ dialog (SC-CARRIER-003).

#### REQ-CARRIER-003 — Lấy hàng (matched → in_transit)

**Source Quote:**
> "Bấm "Tôi đã lấy hàng" → dialog xác nhận ... Bấm "Xác nhận" → matched → in_transit ("Đang giao")."

**Source Location:** `DOC-v1.0-01 §2.3 "Lấy hàng (Đã ghép → Đang giao)"`

**Analyst Note:** Transition thứ 2, cùng pattern dialog xác nhận như REQ-CARRIER-002.

#### REQ-CARRIER-004 — Giao hàng, Carrier không tự hoàn tất

**Source Quote:**
> "Bấm "Đã giao cho người nhận" → dialog xác nhận ... CTA cuối trang chuyển thành nút disabled, text: "Đã giao · chờ người nhận xác nhận" — Carrier không thể tự hoàn tất đơn, phải chờ Receiver."

**Source Location:** `DOC-v1.0-01 §2.4 "Giao hàng (Đang giao → Đã giao, chờ receiver xác nhận)"`

**Analyst Note:** Ràng buộc phân quyền quan trọng: sau khi Carrier báo đã giao, quyền chuyển sang "Hoàn thành" thuộc về Receiver, không phải Carrier. Cần scenario negative riêng verify Carrier không có nút hành động (SC-CARRIER-006) — đây là permission-boundary, rủi ro cao nếu bị vi phạm (Carrier có thể tự ý đóng đơn).

#### REQ-CARRIER-005 — Hoàn thành (sync về Carrier)

**Source Quote:**
> "Khi Receiver xác nhận (xem §3.2) → delivered → completed ("Hoàn thành") — đồng bộ về Carrier, CTA đổi thành disabled, text "Đơn đã hoàn thành ✓"."

**Source Location:** `DOC-v1.0-01 §2.5 "Hoàn thành"`

**Analyst Note:** Verify sync một chiều: hành động của Receiver phản ánh ngay trên màn Carrier mà Carrier không thao tác gì.

#### REQ-CARRIER-006 — Bảng tin & Chi tiết tin: field-level detail (mới, 2026-07-27)

**Source Quote:**
> (quan sát trực tiếp qua Chrome MCP, DOC-v1.0-03) Màn "Bảng tin": list item gồm tiêu đề (loại hàng | giá trị), tag **"Tin của bạn"** (chỉ hiện trên tin do chính Sender hiện tại đăng, KHÔNG hiện trên tin của người khác), địa chỉ Nhận/Giao, mốc thời gian tương đối ("15 phút trước", "1 giờ trước"). Tap 1 item → màn "Chi tiết tin": tiêu đề "Gửi {loại hàng} từ {A} → {B}", section "ẢNH SẢN PHẨM" (quan sát thấy CÓ ảnh ở tin test — cần verify case KHÔNG có ảnh, vì SENDER wizard ghi ảnh là tuỳ chọn), "THÔNG TIN HÀNG" (Loại hàng, Giá trị), "Ghi chú" (text tự do), "LỘ TRÌNH" (Lấy hàng, Giao hàng — 2 địa chỉ), nút "🚚 Tôi mang giúp được"

**Source Location:** `DOC-v1.0-03` — quan sát UI trực tiếp (Bảng tin + Chi tiết tin), không có §section riêng trong BRD/Figma cho field-level chi tiết này (chỉ có SC-CARRIER-001 mức tổng quát "đủ block hiển thị")

**Analyst Note:** Đây là phần chi tiết hoá field-level của SC-CARRIER-001 (đã có, mức tổng quát). Cần thêm 2 kỹ thuật thiết kế test:
- **EP tag "Tin của bạn":** 2 partition — (a) đang xem Bảng tin của chính mình → tin mình đăng CÓ tag, (b) xem Bảng tin với tư cách người khác (Carrier) → tin của Sender khác KHÔNG có tag. Rủi ro: nếu tag hiện sai (vd hiện luôn hoặc không hiện) có thể gây nhầm lẫn "đây là tin của ai".
- **EP Ảnh sản phẩm tuỳ chọn:** 2 partition — (a) tin có ảnh → hiển thị đúng ảnh đã upload, (b) tin không có ảnh (vì SENDER wizard ghi rõ "ảnh không bắt buộc" — REQ-SENDER-002) → màn Chi tiết tin cần xử lý hợp lý (placeholder hoặc ẩn section), chưa quan sát được case này vì tin test đều có sẵn ảnh mẫu.
- Badge trạng thái đơn trên list item Bảng tin: đã có EP riêng qua SC-ORDER-001 (áp dụng chung cho mọi nơi hiển thị badge) — KHÔNG duplicate ở đây.

#### REQ-RECEIVER-001 — Theo dõi đơn (Receiver) + hiển thị block người giao

**Source Quote:**
> "Bấm vào card → màn "Theo dõi đơn" chi tiết, hiển thị thêm block "NGƯỜI GIAO HÀNG" (tên Carrier · SĐT · nút Gọi) — chỉ xuất hiện sau khi đã ghép (trước đó không có Carrier để hiện)."

**Source Location:** `DOC-v1.0-01 §3.1 "Theo dõi đơn (Receiver)"`

**Analyst Note:** Điều kiện hiển thị có điều kiện (conditional rendering) dựa trên order status ≥ matched — cần cả positive (hiện đúng) và negative (ẩn khi chưa matched) scenario.

#### REQ-RECEIVER-002 — Xác nhận đã nhận hàng

**Source Quote:**
> "Khi đơn ở trạng thái "Đã giao", màn theo dõi đơn của Receiver hiện CTA cam "Xác nhận đã nhận hàng". [...] Đây là bước duy nhất chỉ Receiver mới có quyền thực hiện — Carrier không tự hoàn tất được đơn (xem §2.4)."

**Source Location:** `DOC-v1.0-01 §3.2 "Xác nhận đã nhận hàng (Đã giao → Hoàn thành)"`

**Analyst Note:** Transition cuối cùng, quyền độc quyền Receiver — cross-reference REQ-CARRIER-004. Cần negative scenario verify CTA không xuất hiện sớm (trước khi delivered).

#### REQ-ORDER-001 — Order Status Machine: bảng mapping

**Source Quote:**
> Table §4 "ORDER STATUS MACHINE":
> | Status code | Label hiển thị | Màu badge | Actor thực hiện transition | Action trigger |
> |---|---|---|---|---|
> | `posted` | "Chờ ghép" | Xanh dương `#1D4ED8` | Sender (đăng tin) | Submit wizard đăng tin |
> | `matched` | "Đã ghép" | Tím `#5933EB` | Carrier | "Tôi mang giúp được" → Xác nhận |
> | `in_transit` | "Đang giao" | Cam `#B86000` | Carrier | "Tôi đã lấy hàng" → Xác nhận |
> | `delivered` | "Đã giao" | Xanh ngọc `#0F766E` | Carrier | "Đã giao cho người nhận" → Xác nhận |
> | `completed` | "Hoàn thành" | Xanh ngọc `#0F766E` | Receiver | "Xác nhận đã nhận hàng" → Xác nhận |

**Source Location:** `DOC-v1.0-01 §4 "ORDER STATUS MACHINE" · Table (5 rows)`

**Analyst Note:** Bảng mapping canonical cho toàn bộ order lifecycle, dùng chung cả 3 module. SC-ORDER-001 verify UI badge khớp đúng bảng này ở từng mốc.

#### REQ-ORDER-002 — Transition rules ràng buộc

**Source Quote:**
> "1. Transition chỉ đi 1 chiều tuần tự, không có UI để lùi trạng thái (ngoại trừ nút toàn cục "↺ Chạy lại từ đầu" reset về posted ban đầu...). 2. Mỗi transition đều có dialog xác nhận trung gian (Huỷ/Xác nhận) — không transition thẳng khi bấm nút chính. 3. Transition cuối (delivered → completed) chỉ Receiver thực hiện được... 4. Đồng bộ 3 màn là tức thời (cùng 1 lần click, không cần reload/refresh)... 5. Header toàn cục (thanh điều khiển demo) hiển thị badge "Trạng thái đơn" + màu tương ứng, cập nhật đồng thời với 3 phone."

**Source Location:** `DOC-v1.0-01 §4 "ORDER STATUS MACHINE" · "Ràng buộc quan trọng" bullet 1-5`

**Analyst Note:** 5 ràng buộc hệ thống cốt lõi, mỗi ràng buộc map tới 1 scenario (SC-ORDER-002 ↔ #1, SC-ORDER-004 ↔ #2, SC-CARRIER-006/RECEIVER-003 ↔ #3, SC-ORDER-003 ↔ #4, SC-ORDER-001 ↔ #5).

#### REQ-GENERAL-001 — Tuyên bố không thu phí/không chat/không thanh toán

**Source Quote:**
> "App **không** thu phí, không chat, không thanh toán. Sau khi ghép, SĐT hai bên sẽ được lộ để liên hệ ngoài app."

**Source Location:** `DOC-v1.0-01 §0 "Bối cảnh chung (Context)"`

**Analyst Note:** UI copy cố định trong banner wizard đăng tin (đã verify vị trí thực tế: bước "Bạn muốn làm gì?"). Priority thấp (P3) vì là nội dung tĩnh, không ảnh hưởng luồng nghiệp vụ, nhưng vẫn cần verify đúng chữ vì là tuyên bố pháp lý/kỳ vọng người dùng.

#### REQ-GENERAL-002 — Bottom navigation bar (5 icon, cả 3 vai trò)

**Source Quote:**
> (quan sát trực tiếp qua Chrome MCP, DOC-v1.0-03, không có text mô tả trong tài liệu — ghi lại nguyên trạng UI) Thanh điều hướng dưới cùng mỗi phone có 5 icon: "Trang chủ", "Bảng tin", nút tròn cam "+" ở giữa (mở wizard "Đăng tin"), "Hoạt động", "Cá nhân". Xuất hiện giống hệt nhau trên cả 3 phone (Sender/Carrier/Receiver).

**Source Location:** `DOC-v1.0-03` — quan sát UI trực tiếp (không có §section vì không phải văn bản đặc tả, là prototype thực thi được)

**Analyst Note:** Đây là navigation chưa từng được ghi nhận trong DOC-v1.0-01/02 (2 tài liệu trước chỉ mô tả luồng nghiệp vụ theo từng bước wizard, không mô tả cấu trúc điều hướng tổng thể của app). "Đăng tin" (nút giữa) đã có REQ/SC riêng qua SENDER module. 4 icon còn lại (Trang chủ/Bảng tin/Hoạt động/Cá nhân) dẫn tới các màn đã có REQ riêng lẻ (Trang chủ = dashboard hiện có, Bảng tin = feed đơn, Hoạt động = "Đơn của tôi" 2 tab Đang diễn ra/Đã hoàn thành dẫn tới GIFT flow, Cá nhân = profile dẫn tới GIFT-003/004) — REQ này cụ thể chỉ test **navigation** (tap đúng icon → đúng màn, active-tab state đúng), không lặp lại nội dung màn đích.

---

#### REQ-GENERAL-003 — Trang chủ: dashboard field-level detail (mới, 2026-07-27)

**Source Quote:**
> (quan sát trực tiếp qua Chrome MCP, DOC-v1.0-03) Màn "Trang chủ" (mặc định khi mở app): header "Xin chào, {tên}" + icon chuông (có red-dot khi có thông báo chưa đọc), banner "Tiện đường — Giúp đồng nghiệp" + badge "FOX ECO", card "Đóng góp của bạn" → "{N} đơn đã giúp" + "Cộng đồng FoxEco: {N} đơn · {N} người", nút "Xem bảng tin gửi hàng" (điều hướng sang Bảng tin). Nội dung tiếp theo **khác nhau theo vai trò**: Sender/Receiver thấy section "Đơn của tôi" (card đơn hiện tại: tiêu đề, badge trạng thái, Từ/Đến, progress bar, link "Chạm để theo dõi đơn của bạn", link "Xem tất cả"); Carrier thấy thêm/thay bằng section "Tin mới" (danh sách tin đang chờ nhận, mỗi item: tiêu đề, Nhận/Giao, mốc thời gian)

**Source Location:** `DOC-v1.0-03` — quan sát UI trực tiếp, không có §section BRD/Figma tương ứng (đây là dashboard tổng hợp, không phải 1 bước cụ thể trong flow)

**Analyst Note:** Các kỹ thuật cần áp dụng:
- **Content khác theo vai trò (không phải bug, là chủ đích):** "Đơn của tôi" (Sender/Receiver) vs "Tin mới" (Carrier) — viết 2 SC riêng thay vì 1 SC chung, vì đây là 2 nội dung khác nhau thật, không phải cùng field hiển thị khác data.
- **EP empty state:** "Đơn của tôi" khi KHÔNG có đơn nào đang hoạt động (chưa quan sát được — dữ liệu demo luôn có sẵn 1 đơn mẫu) và "Tin mới" khi bảng tin trống — cả 2 case CHƯA xác định được UI thật hiển thị gì (ẩn section, hay hiện text "Chưa có đơn nào"...). Ghi "chưa xác định" thay vì đoán, tương tự nguyên tắc đã áp dụng cho SENDER field validation.
- Badge trạng thái trên card "Đơn của tôi": dùng chung EP đã có ở SC-ORDER-001, KHÔNG duplicate.
- Stats số liệu ("{N} đơn đã giúp", "{N} người") — ưu tiên thấp (P3), chỉ cần 1 TC display-only vì là read-only data từ demo, không có input để test invalid/boundary.

---

#### REQ-SENDER-006 — Tự điền người nhận qua email công ty

**Source Quote:**
> "Ô "Email công ty người nhận" nằm đầu mục Người nhận; nhập email có trong hệ thống → tự điền tên/SĐT/địa chỉ + báo "Đã tìm thấy trong hệ thống nội bộ"; không có → báo "Không tìm thấy · nhập thủ công""

**Source Location:** `DOC-v1.0-02 §D1b "User Story — Gửi Hàng" · US-D18 Acceptance Criteria`

**Analyst Note:** Tính năng tra danh bạ nội bộ (USR-EML) — tăng tốc nhập liệu, giảm sai sót. Bản HTML prototype hiện tại KHÔNG có field email này ở wizard bước 2 (chỉ có 3 field nhập tay: tên/SĐT/địa chỉ) — hoàn toàn mới so với DOC-v1.0-01.

#### REQ-ORDER-003 — Chỉnh sửa đơn khi "Chờ ghép"

**Source Quote:**
> "Nút "Chỉnh sửa" chỉ hiện ở trạng thái Chờ ghép (POSTED); mở màn giống tạo đơn nhưng đã điền sẵn; có nút "Cập nhật" & "Huỷ chỉnh sửa"; sau IN_TRANSIT không cho sửa"

**Source Location:** `DOC-v1.0-02 §D1b US-D19 Acceptance Criteria`, cross-ref `§D4 BR-EDIT-01`

**Analyst Note:** BR-EDIT-01 làm rõ ranh giới chính xác hơn US-D19 ("sau IN_TRANSIT"): "Chỉ được chỉnh sửa tin khi còn 'Chờ ghép' (POSTED); đã MATCHED trở đi khoá chỉnh sửa" — tức khoá ngay từ MATCHED, không phải chờ tới IN_TRANSIT. Ưu tiên BR-EDIT-01 (Business Rule, chính xác hơn) khi viết TC negative (SC-ORDER-006).

#### REQ-ORDER-004 — Tin quá hạn tự chuyển EXPIRED

**Source Quote:**
> "Quá hạn cấu hình mà chưa MATCHED → tự chuyển EXPIRED, hiển thị badge "Hết hạn" ở tab hoàn tất kèm lý do "Không có ai nhận mang giúp trong thời gian đăng""

**Source Location:** `DOC-v1.0-02 §D1b US-D04 Acceptance Criteria`, cross-ref `§D3 ORD-06`

**Analyst Note:** Ngưỡng thời gian cụ thể chưa được nêu trong BRD (nằm trong "CÂU HỎI MỞ CHO BA — Hạn tin mặc định?" ở §D5) — cần BA xác nhận số giờ/ngày cụ thể trước khi viết TC data-driven (boundary). Ghi Clarification C-ORDER-2.

**UI Confirmation (2026-07-27, DOC-v1.0-03):** Quan sát trực tiếp tab "Đã hoàn thành" (Hoạt động → Đơn của tôi, phone Sender) có 1 order card với badge **"Hết hạn"** + text **"Không có ai nhận mang giúp trong thời gian đăng — tin đã tự động đóng."** — khớp gần như nguyên văn với Source Quote BRD ở trên. Xác nhận 1 phần: UI/badge có thật, nhưng CHƯA verify liệu tin EXPIRED có bị ẩn/đánh dấu tương ứng ở phía "Bảng tin" (feed công khai cho Carrier/Receiver khác xem) hay không — chỉ mới xem từ góc nhìn lịch sử đơn của chính Sender. Ngưỡng thời gian cụ thể vẫn theo resolution C-ORDER-2 (mốc "Từ ngày", không phải duration cố định) — phần đó không đổi.

#### REQ-OFFER-001 — Đăng tin OFFER "Tôi nhận giao hàng"

**Source Quote:**
> "Là Carrier đang có nhu cầu di chuyển, tôi muốn đăng tin "Tôi nhận giao hàng" với điểm xuất phát, điểm đến, khung giờ và tên/SĐT... Màn đăng tin OFFER 1 màn duy nhất, các trường: Điểm xuất phát, Điểm đến, Khung giờ, Tên, SĐT + tick đồng ý điều khoản"

**Source Location:** `DOC-v1.0-02 §D1b US-D10 Acceptance Criteria`

**Analyst Note:** Khác biệt quan trọng với wizard SENDER (3 bước) — OFFER chỉ 1 màn duy nhất. Đây chính là nhánh mà DOC-v1.0-01 từng ghi Clarification C-SENDER-1 "chưa rõ có trong scope" — BRD xác nhận CÓ, đặc tả chi tiết.

**UI Confirmation (2026-07-27, DOC-v1.0-03):** Quan sát trực tiếp — bấm "+" (Đăng tin) → màn "Bạn muốn làm gì?" hiện đúng 2 lựa chọn (Tôi cần gửi hàng / Tôi nhận giao hàng) → chọn "Tôi nhận giao hàng" → mở form 1 màn: "THÔNG TIN CỦA TÔI" (tên/SĐT tự điền sẵn), "ĐIỂM XUẤT PHÁT (A)" (tự điền), "ĐIỂM ĐẾN (B)" (trống, placeholder "Bạn sẽ đến đâu"), "KHOẢNG THỜI GIAN (NGÀY)" (Từ ngày/Đến ngày — date picker), "THỜI GIAN DI CHUYỂN" (Khởi hành/Đến nơi — time picker), checkbox điều khoản, nút "Đăng tin ngay" (disabled khi form chưa đủ). **Lưu ý nhỏ:** BRD viết gọn là "Khung giờ" (1 field) nhưng UI thật tách thành 2 nhóm field (khoảng ngày + khoảng giờ di chuyển) — chi tiết hơn BRD, không mâu thuẫn, chỉ cần TC Steps theo đúng UI thật (4 field ngày/giờ thay vì 1 "khung giờ"). Chưa bấm "Đăng tin ngay" để xem màn kết quả (xem REQ-OFFER-002 — chưa verify riêng).

#### REQ-OFFER-002 — Xác nhận tuyến đã ghi nhận (không công khai)

**Source Quote:**
> "Sau khi đăng → màn "Đã ghi nhận tuyến đường" giải thích: tuyến được lưu (không công khai), khi có người cần gửi trùng điểm lấy & điểm giao hệ thống sẽ gửi thông báo để bạn xem xét"

**Source Location:** `DOC-v1.0-02 §D1b US-D11 Acceptance Criteria`, cross-ref `§A4 "tuyến OFFER không hiển thị công khai"`

**Analyst Note:** Điểm khác biệt cố ý so với tin NEED (hiển thị công khai trên feed) — tuyến OFFER private, chỉ dùng để hệ thống tự khớp.

#### REQ-OFFER-003 — Nhận thông báo khi tuyến khớp tin NEED

**Source Quote:**
> "Khi một tin NEED trùng điểm lấy & điểm giao với tuyến → hệ thống đẩy thông báo "Tìm thấy đơn hàng phù hợp tuyến của bạn"; bấm vào thông báo → mở màn chi tiết tin cần vận chuyển đó"

**Source Location:** `DOC-v1.0-02 §D1b US-D12 Acceptance Criteria`, cross-ref `§D3 MTCH-01`, `§D6 NTF-03`

**Analyst Note:** Phụ thuộc hệ thống notification (§D6) — chưa có UI notification trong prototype, nên scenario này chỉ document được ở mức spec, không thể vibe-test.

#### REQ-OFFER-004 — Nhận giao từ thông báo → MATCHED

**Source Quote:**
> "Tại chi tiết tin NEED phù hợp có nút "Nhận giao"; bấm → ghép (MATCHED) → lộ liên hệ 2 bên → vào màn Theo dõi đơn"

**Source Location:** `DOC-v1.0-02 §D1b US-D13 Acceptance Criteria`

**Analyst Note:** Kết quả cuối giống hệt luồng CARRIER hiện có (MATCHED → lộ liên hệ → Theo dõi đơn) — chỉ khác điểm vào (từ thông báo thay vì bấm "Tôi mang giúp được" trên feed). P1 vì tạo cùng 1 outcome quan trọng như REQ-CARRIER-002.

#### REQ-CANCEL-001 — Huỷ đơn bắt buộc lý do

**Source Quote:**
> "popup huỷ bắt buộc nhập lý do (nút Xác nhận khoá tới khi có lý do); đơn huỷ ghi rõ ai huỷ (Người gửi/Người vận chuyển/Người nhận) + lý do, đồng bộ realtime cho cả 3 bên"

**Source Location:** `DOC-v1.0-02 §D1b US-D16 Acceptance Criteria`, cross-ref `§D4 BR-CNL-01`, `§D3 CNL-01`

**Analyst Note:** Đây chính là nhánh DOC-v1.0-01 từng ghi Clarification C-CARRIER-1 "chưa rõ scope" — BRD xác nhận CÓ, đặc tả rất chi tiết gồm cả validation gate (nút khoá tới khi nhập lý do).

**UI Confirmation (2026-07-27, DOC-v1.0-03):** Quan sát trực tiếp — từ màn "Theo dõi đơn" (trạng thái "Chờ ghép"), cuối màn có 2 nút "✏️ Chỉnh sửa" và "❌ Huỷ đơn". Bấm "Huỷ đơn" → popup "Huỷ đơn hàng": text "Bạn chắc chắn muốn huỷ đơn hàng này? Thao tác không thể hoàn tác.", textarea "Lý do huỷ *" (bắt buộc, placeholder "VD: đổi lịch, không cần gửi nữa..."), 2 nút "Huỷ" (đóng popup)/"Xác nhận" (khoá tới khi có lý do — khớp đúng BRD). Đã đóng popup bằng nút "Huỷ" (không bấm "Xác nhận" thật) để giữ nguyên state demo cho các bước kiểm tra khác — SC-CANCEL-002 (kết quả sau khi huỷ thành công) chưa verify được nội dung chính xác sau khi Xác nhận, cần vibe-test thật để hoàn tất.

#### REQ-CANCEL-002 — Giới hạn thời điểm được huỷ

**Source Quote:**
> "Chỉ được huỷ khi chưa ai nhận ("Chờ ghép") hoặc đang "Lấy hàng" (đã ghép, chưa lấy được hàng); đã lấy hàng → sang "Đang giao" thì KHÔNG ai được huỷ"

**Source Location:** `DOC-v1.0-02 §D7 "Rule vận hành" · OPR-11`, cross-ref `§D4 BR-ASN-03 "Sau khi nhận hàng (IN_TRANSIT) không hủy thường → phải tạo sự cố"`

**Analyst Note:** Ràng buộc permission-boundary quan trọng, cùng lớp rủi ro với REQ-CARRIER-004 (Carrier không tự hoàn tất đơn). Sau IN_TRANSIT, thay vì Huỷ phải dùng luồng "Báo sự cố" (INCIDENT) — không có scope chi tiết cho incident trong BRD này, chỉ nhắc tên.

#### REQ-CANCEL-003 — Carrier huỷ → đơn trả về "Chờ ghép"

**Source Quote:**
> "Người vận chuyển huỷ ở trạng thái Đã ghép (chưa "Tôi đã lấy hàng") → đơn tự động về "Chờ ghép" và hiển thị lại trên bảng tin cho người khác nhận"

**Source Location:** `DOC-v1.0-02 §D7 OPR-09`, cross-ref `§D1b US-D16 "Carrier huỷ nhận → đơn trả lại bảng tin (về 'Chờ ghép')"`

**Analyst Note:** Khác với Sender/Receiver huỷ (kết thúc đơn hẳn ở CANCELLED) — Carrier huỷ có hành vi đặc biệt: đơn KHÔNG chết mà quay lại vòng matching. Đây là state transition dễ nhầm lẫn, ưu tiên P1.

#### REQ-CANCEL-004 — Đồng bộ realtime huỷ cho cả 3 bên

**Source Quote:**
> "ghi rõ ai huỷ (Người gửi/Người vận chuyển/Người nhận) + lý do, đồng bộ realtime cho cả 3 bên"

**Source Location:** `DOC-v1.0-02 §D1b US-D16 Acceptance Criteria`

**Analyst Note:** Cùng nguyên tắc đồng bộ real-time đã verify ở REQ-ORDER-002 (existing) — áp dụng nhất quán cho nhánh Cancel mới.

#### REQ-GIFT-001 — Màn tặng quà hiển thị 4 loại quà

**Source Quote:**
> "4 loại quà: bông hoa, ly cà phê, gấu bông, vương miện — biểu tượng phi vật chất"

**Source Location:** `DOC-v1.0-02 §A7 "Phần thưởng — Quà ảo"`, cross-ref `§D1b US-D15`

**Analyst Note:** Danh mục 4 loại quà cố định — tương tự cách 8 loại hàng/3 mức giá trị ở SENDER wizard là danh mục cố định trong client.

**UI Confirmation (2026-07-27, DOC-v1.0-03):** Quan sát trực tiếp màn "Tặng quà" (đường dẫn: phone Sender → tab "Hoạt động" → "Đơn của tôi" → sub-tab "Đã hoàn thành" → tap 1 đơn đã hoàn thành) — hiển thị đúng 4 lựa chọn: Bông hoa 🌷, Ly cà phê ☕, Gấu bông 🧸, Vương miện 👑, kèm subtitle "Hành trình hoàn thành! Gửi một món quà cảm ơn người vận chuyển". Khớp đúng BRD. TC Status → ⏳ Ready.

#### REQ-GIFT-002 — Gửi quà (có bước xác nhận trong UI thật — khác BRD text)

**Source Quote:**
> "chọn quà → gửi ngay không cần bước xác nhận → popup "Cảm ơn của bạn đã được gửi" → nút "Về trang chủ""

**Source Location:** `DOC-v1.0-02 §D1b US-D15 Acceptance Criteria`

**Analyst Note:** Khác với các transition khác trong app (luôn có dialog Huỷ/Xác nhận trung gian — REQ-ORDER-002) — tặng quà KHÔNG có bước xác nhận trung gian, gửi ngay khi chọn. Cần lưu ý khi viết TC để không áp nhầm pattern "luôn có dialog xác nhận".

**⚠️ UI Discrepancy (2026-07-27, DOC-v1.0-03):** Quan sát trực tiếp — sau khi chọn 1 quà, UI hiển thị nút **"Xác nhận tặng quà"** ở cuối màn (phải bấm thêm 1 bước, KHÔNG phải "gửi ngay không cần xác nhận" như BRD mô tả). Chưa quan sát được popup "Cảm ơn của bạn đã được gửi" sau khi bấm (dừng lại trước khi bấm confirm để tránh thay đổi state demo ngoài dự kiến). Đây là khác biệt nhỏ giữa BRD text và UI thật — KHÔNG blocking, nhưng TC Steps nên viết theo UI thật (có bước "Xác nhận tặng quà") thay vì theo văn bản BRD. Ghi nhận, không cần Clarification riêng vì không ảnh hưởng nghiệp vụ cốt lõi.

#### REQ-GIFT-003 — Người nhận quà thấy thông báo + màn "Quà đã nhận"

**Source Quote:**
> "Carrier nhận thông báo "Bạn nhận được một món quà cảm ơn" → mở Trang cá nhân... màn Quà đã nhận hiển thị 1 card đếm số bông hoa/ly cà phê/gấu bông/vương miện + danh sách lịch sử nhận quà"

**Source Location:** `DOC-v1.0-02 §D1b US-D20 Acceptance Criteria`

**Analyst Note:** Trang "Cá nhân" hoàn toàn chưa xuất hiện trong prototype (bottom nav demo có icon "Cá nhân" nhưng chưa test nội dung bên trong) — cần dev build trước khi test được.

**UI Confirmation + Open Question (2026-07-27, DOC-v1.0-03):** Quan sát trực tiếp màn "Quà đã nhận" ở tab "Cá nhân" — có thật, hiển thị "Tổng quà đã nhận: 8 món" + breakdown (3 Bông hoa/2 Ly cà phê/2 Gấu bông/1 Vương miện) + "LỊCH SỬ NHẬN QUÀ" (5 dòng, mỗi dòng: loại quà + tên người tặng + ngày). **Khác biệt so với BRD:** BRD nói quà đi từ Người gửi → Người vận chuyển (Carrier là người nhận quà) — nhưng màn "Quà đã nhận" quan sát được lại nằm ở phone gắn nhãn "NGƯỜI NHẬN" (Phan Văn Hưng), không phải phone "NGƯỜI VẬN CHUYỂN". Chưa xác định được đây là (a) dữ liệu demo mock hiển thị sẵn không phụ thuộc vai trò thật trong đơn đang track, hay (b) menu "Quà đã nhận" thực ra xuất hiện ở CẢ 3 vai trò (vì ai cũng có thể từng là carrier cho người khác trong cộng đồng 328 người), hay (c) đây là nhầm lẫn/bug trong prototype. Chưa verify được phone Sender/Carrier có menu này hay không. → Ghi Clarification C-GIFT-2 (Open, non-blocking).

#### REQ-GIFT-004 — Xem lịch sử "Quà đã nhận" (breakdown + history)

**Source Quote:**
> (quan sát trực tiếp qua Chrome MCP, DOC-v1.0-03) Màn "Quà đã nhận": header "Tổng quà đã nhận" + số lượng ("8 món"), lưới 4 ô đếm theo loại quà (vd "3 · Bông hoa", "2 · Ly cà phê", "2 · Gấu bông", "1 · Vương miện"), section "LỊCH SỬ NHẬN QUÀ" liệt kê từng lần nhận quà (loại quà + tên người tặng + mốc thời gian, vd "Bông hoa — Đồng Công Chí Linh · Hôm nay · 17:20")

**Source Location:** `DOC-v1.0-03` — quan sát UI trực tiếp (không có §section, không có mô tả tương ứng trong BRD DOC-v1.0-02 — chỉ có REQ-GIFT-003 nói chung chung "1 card đếm số... + danh sách lịch sử", DOC-v1.0-03 là nguồn đầu tiên cho chi tiết cụ thể của màn này)

**Analyst Note:** Đây là phần chi tiết hoá của REQ-GIFT-003 (màn đích khi tap "Quà đã nhận" từ Cá nhân) — tách thành REQ/SC riêng vì có đủ chi tiết UI cụ thể để viết TC riêng (đếm đúng số theo loại, thứ tự lịch sử theo thời gian giảm dần, hiển thị đúng tên người tặng). Cùng lưu ý mở (vai trò nào thấy màn này) như ghi ở REQ-GIFT-003 — xem C-GIFT-2.

#### REQ-NOTIFICATION-001 — 9 sự kiện thông báo

**Source Quote:**
> Table §D6 "Thông báo (Notifications)": NTF-01 "Có người bấm 'Tôi mang giúp được'" → Người gửi; NTF-02 "Đơn được ghép (MATCHED)" → Người nhận; NTF-03 "Hệ thống khớp tuyến OFFER" → Người vận chuyển; NTF-04 "Carrier bấm 'Tôi đã lấy hàng'" → Người gửi·Người nhận; NTF-05 "Carrier bấm 'Đã giao'" → Người nhận·Người gửi; NTF-06 "Xác nhận đã nhận hàng" → Người gửi·Người vận chuyển; NTF-07 "Tặng quà ảo" → Người vận chuyển; NTF-08 "Đơn bị huỷ" → các bên còn lại; NTF-09 "Tin quá hạn" → Người đăng tin

**Source Location:** `DOC-v1.0-02 §D6 "Thông báo (Notifications)" · Table NTF-01→09`

**Analyst Note:** Tài liệu tự đánh dấu "Nháp — chờ BA review & bổ sung" — nội dung thông báo (mẫu text) đã có nhưng cơ chế kênh (push/in-app), UI hiển thị danh sách thông báo hoàn toàn chưa có trong prototype. Gộp 9 sự kiện vào 1 scenario documentation-level thay vì 9 scenario riêng, vì không thể test độc lập từng event khi chưa có hệ thống notification thật.

**UI Confirmation (2026-07-27, DOC-v1.0-03):** Quan sát trực tiếp — bấm icon chuông (góc trên phải mỗi phone, có red-dot khi có tin chưa đọc) → mở màn "Thông báo" đầy đủ, nhóm theo "HÔM NAY"/"HÔM QUA"/"TUẦN NÀY". Nội dung quan sát được thực tế: "Có người muốn mang giúp đơn của bạn" (khớp NTF-01), "Ghép thành công — SĐT đã được lộ" (khớp NTF-02), "Người mang giúp đã nhận hàng" (khớp NTF-04), "Sắp đến khung giờ hẹn giao" (không khớp trực tiếp NTF nào trong bảng 9 sự kiện — có thể là 1 loại nhắc lịch bổ sung, cần BA xác nhận có phải NTF-10 mới hay chỉ là biến thể UI của NTF khác), "Có chuyến đi mới hợp tuyến của bạn" (khớp NTF-03), "Đơn đã hoàn thành — đánh giá ngay" + "Bạn nhận được đánh giá 5 sao" (⚠️ nhắc tới rating sao — xem C-GENERAL-2 addendum, KHÔNG phải NTF-07 "Tặng quà ảo" như kỳ vọng — coi là nội dung lỗi thời trong prototype, không viết TC theo đúng text này). TC Status → ⏳ Ready cho phần khung màn hình + các NTF đã khớp; phần "đánh giá 5 sao" loại khỏi TC scope (xem clarification).

#### REQ-NOTIFICATION-002 — Đánh dấu tất cả đã đọc

**Source Quote:**
> (quan sát trực tiếp qua Chrome MCP, DOC-v1.0-03) Header màn "Thông báo" có link "Đánh dấu đã đọc" ở góc phải, cạnh tiêu đề

**Source Location:** `DOC-v1.0-03` — quan sát UI trực tiếp (không có trong BRD DOC-v1.0-02, chỉ liệt kê nội dung 9 sự kiện, không mô tả UI màn danh sách thông báo)

**Analyst Note:** Hành vi chưa verify hết (chưa bấm thử để xem tất cả red-dot có biến mất không) — SC-NOTIFICATION-002 cần vibe-test xác nhận hành vi thật khi generate-tc/execute.

#### REQ-ADMIN-001 — Quyền override của Admin

**Source Quote:**
> Table §D4 Permission Matrix, cột ADMIN: "Đăng tin gửi hàng ✓ · Chấp nhận người ghép ✓ override · 'Đã nhận hàng'/'Đã giao' ✓ override · Xác nhận 'Đã nhận' ✓ override · Huỷ đơn ✓ · Chỉnh sửa tin ✓ · Báo sự cố ✓"

**Source Location:** `DOC-v1.0-02 §D4 "Business Rules & Permission Matrix" · bảng phân quyền`

**Analyst Note:** Admin có quyền "override" trên hầu hết action — nhưng KHÔNG có Admin Portal/UI nào trong bản HTML prototype (chỉ có 3 màn Sender/Carrier/Receiver). Toàn bộ module ADMIN ở mức spec-only, out of scope test cho tới khi có Admin Web Portal.

#### REQ-MEDIA-001 — Chụp ảnh hàng lúc nhận (tùy chọn)

**Source Quote:**
> "Chụp ảnh hàng lúc nhận: Tùy chọn (khuyến nghị) — lưu S3, gắn timeline làm bằng chứng"

**Source Location:** `DOC-v1.0-02 §D3 "Functional Requirements" · PUP-03`, cross-ref `§D4 BR-CNF-01 "bằng chứng chính khi tranh chấp"`

**Analyst Note:** Khác với "Ảnh hàng (khuyến nghị)" ở wizard đăng tin của Sender (ảnh sản phẩm khi ĐĂNG tin, đã có trong prototype) — đây là ảnh Carrier chụp lúc NHẬN hàng (bằng chứng giao nhận), một tính năng khác, chưa có UI.

#### REQ-MEDIA-002 — Chia sẻ vị trí GPS khi đang giao (tùy chọn)

**Source Quote:**
> "Chia sẻ vị trí khi đang giao: Tùy chọn; chỉ active khi đang giao; xóa sau khi đóng"

**Source Location:** `DOC-v1.0-02 §D3 "Functional Requirements" · GPS-01`

**Analyst Note:** Ràng buộc privacy rõ ràng (chỉ active trong lúc "Đang giao", tự xoá sau khi đóng đơn) — cần TC riêng verify việc xoá dữ liệu vị trí đúng thời điểm khi có UI thật.

*(Source Detail cho từng SC đặt tại `test_scenario_map.md` theo template; Source Detail cho Clarification đặt tại §6.1 bên dưới và `requirement_traceability.md §3`.)*

## 5. Test Data Summary
| Module | DOC Source | Fields chính | Số bộ valid | Số bộ invalid | Có boundary? |
|--------|-----------|-------------|-------------|---------------|-------------|
| SENDER | DOC-v1.0-01 §1.2-1.4 | Loại hàng, Giá trị hàng, Ghi chú, Tên/SĐT/Địa chỉ người nhận, Checkbox điều khoản, Email công ty người nhận | 7 | 1 rõ ràng (checkbox) + 5 chưa xác định | Không rõ (xem test_data_catalog ghi chú) |
| OFFER | DOC-v1.0-02 §D1b US-D10 | Điểm xuất phát, Điểm đến, Khung giờ, Tên, SĐT | 5 (spec-only, chưa có UI) | Chưa xác định | Chưa xác định |
| CANCEL | DOC-v1.0-02 §D1b US-D16 | Lý do huỷ (free text, bắt buộc) | 1 (spec-only) | 1 (rỗng → khoá nút Xác nhận) | Không |
| GIFT | DOC-v1.0-02 §A7 | Loại quà (bông hoa/ly cà phê/gấu bông/vương miện) | 4 (spec-only, chưa có UI) | N/A (chip select cố định) | Không |

## 6. Clarifications & Blockers
| # | Req ID | DOC Source | Vấn đề | Answer | Status | Ngày resolve | Ảnh hưởng |
|---|--------|-----------|--------|--------|--------|-------------|-----------|
| C-SENDER-1 | REQ-SENDER-001, REQ-OFFER-001..004 | DOC-v1.0-01 §1.1 | Nhánh "Tôi nhận giao hàng" (Carrier tự đăng tin rảnh rỗi) mô tả trong Figma board nhưng KHÔNG có UI trong bản HTML prototype | **RESOLVED bởi BRD v3.1 (DOC-v1.0-02 §D1b Nhóm 3, US-D10→D13)**, **UI UNBLOCKED 2026-07-27 (DOC-v1.0-03):** CÓ trong scope, VÀ nay có UI thật (màn "Bạn muốn làm gì?" → "Tôi nhận giao hàng" → form đầy đủ) | Resolved (scope) / **Unblocked (test) 2026-07-27** | 2026-07-24 (scope), 2026-07-27 (UI) | generate-tc: có REQ-OFFER-001..004 + SC-OFFER-001..004, sẵn sàng generate TC thật (⏳ Ready) |
| C-CARRIER-1 | REQ-CARRIER-002..004, REQ-CANCEL-001..004 | DOC-v1.0-01 §2.5 | Nhánh "Huỷ đơn" (nhiều điểm chèn trong Figma: sau xem tin/đã ghép/đã lấy hàng) KHÔNG có UI trong bản HTML prototype | **RESOLVED bởi BRD v3.1 (DOC-v1.0-02 §D1b US-D16, §D3 CNL-01, §D4 BR-CNL-01, §D7 OPR-09/11)**, **UI UNBLOCKED 2026-07-27 (DOC-v1.0-03):** CÓ trong scope, VÀ nay có UI thật (nút "Huỷ đơn" ở màn Theo dõi đơn → popup lý do bắt buộc) | Resolved (scope) / **Unblocked (test) 2026-07-27** | 2026-07-24 (scope), 2026-07-27 (UI) | generate-tc: có REQ-CANCEL-001..004 + SC-CANCEL-001..004, sẵn sàng generate TC thật (⏳ Ready) |
| C-CARRIER-2 | REQ-CARRIER-005, REQ-GIFT-001..004 | DOC-v1.0-01 §2.5 | Nhánh "Tặng quà cảm ơn cho người vận chuyển" sau khi hoàn thành KHÔNG có UI trong bản HTML prototype | **RESOLVED bởi BRD v3.1 (DOC-v1.0-02 §A7, §D1b US-D15/D20, §D3 GIFT-01)**, **UI UNBLOCKED 2026-07-27 (DOC-v1.0-03):** CÓ trong scope, VÀ nay đã có UI thật chạy được (flow tặng quà + màn Quà đã nhận, xem REQ-GIFT-001..004) | Resolved (scope) / **Unblocked (test) 2026-07-27** | 2026-07-24 (scope), 2026-07-27 (UI) | generate-tc: có REQ-GIFT-001..004 + SC-GIFT-001..004, sẵn sàng generate TC thật (⏳ Ready) |
| C-SENDER-2 | REQ-SENDER-002, REQ-SENDER-005 | DOC-v1.0-01 §1.2, §1.5 | Wizard đăng tin không tạo listing độc lập trong feed Carrier/Receiver — chưa rõ đây là giới hạn kiến trúc demo (chấp nhận) hay hành vi cần fix trước automation thật | — | Open (non-blocking, đã ghi nhận Known Limitation trong Project_rule.md §7) | — | Không log bug P1/P2 cho hành vi này; generate-tc ghi rõ note "chỉ verify order slot hiện có, không verify multi-order" |
| C-ORDER-1 | REQ-ORDER-002 | DOC-v1.0-01 §4 | Nút "↺ Chạy lại từ đầu" reset order status về `posted`, nhưng CHƯA rõ có reset luôn dữ liệu đã nhập trong wizard đăng tin hay không (quan sát: wizard giữ nguyên form data sau reset ở 1 lần test) | — | Open (non-blocking) | — | SC-ORDER-002 chỉ verify status reset, KHÔNG assert wizard form state — cần BA/dev xác nhận trước khi mở rộng scenario |
| C-ORDER-2 | REQ-ORDER-004 | DOC-v1.0-02 §D1b US-D04, §D5 | Ngưỡng thời gian cụ thể để tin tự chuyển "EXPIRED" chưa được BRD nêu rõ — chính tài liệu tự liệt kê trong "CÂU HỎI MỞ CHO BA": "Hạn tin mặc định?" | **User xác nhận (2026-07-27):** Ngưỡng hết hạn KHÔNG phải khoảng thời gian cố định tính từ lúc tạo tin (không phải "24h"/"3 ngày" kể từ creation) — mà tin tự chuyển EXPIRED khi đã **qua "Từ ngày"** (giá trị field "Từ ngày" trong khoảng ngày Sender chọn ở wizard bước 2) mà đơn vẫn chưa được ai nhận (chưa MATCHED) | Resolved | 2026-07-27 | generate-tc: TC boundary cho SC-ORDER-007 dùng mốc "Từ ngày" làm ngưỡng (vd: current date > Từ ngày AND status = posted → EXPIRED), KHÔNG dùng số giờ/ngày cố định. Vẫn 🚫 Blocked chờ UI/worker implement — chỉ mở khoá phần business rule, chưa mở khoá phần TC thật |
| C-GENERAL-2 | REQ-RECEIVER-002, REQ-GIFT-001..004 | DOC-v1.0-02 §A7, §A5 BR-INT-06 vs §D2, §D3 RAT-01/02; addendum DOC-v1.0-03 | **Mâu thuẫn nội bộ trong chính BRD:** §A7 "Không tính điểm, không tier/xếp hạng..." và §A5 BR-INT-06 "Không đánh giá sao; ghi nhận thiện chí bằng quà ảo" khẳng định KHÔNG có rating — nhưng §D2 (workflow) liệt kê bước "[HOÀN TẤT] Đánh giá 2 chiều → ... → CO₂ + điểm → COMPLETED" và §D3 liệt kê "RAT-01/02 Đánh giá 2 chiều 1–5 sao + nhận xét" như functional requirement chính thức. **Addendum 2026-07-27:** DOC-v1.0-03 (prototype cập nhật) lại hiện UI 5 sao thật ("Đã đánh giá" + 5 sao cam trên order card, notification "Bạn nhận được đánh giá 5 sao") — bằng chứng UI mạnh hơn suy luận từ text, khiến câu hỏi bị mở lại | **User xác nhận (2026-07-27, LẦN 1):** KHÔNG có rating sao. Model đúng = §A7/§A5 BR-INT-06 (quà ảo thay thế hoàn toàn rating) — §D2/§D3 (Đánh giá 2 chiều 1-5 sao, RAT-01/02) là phần spec cũ chưa đồng bộ, KHÔNG implement. **User tái xác nhận (2026-07-27, LẦN 2, sau khi xem bằng chứng UI DOC-v1.0-03):** "rating k ton tai, chi co gift thoi, trong figma cung k co rating dau" — rating KHÔNG tồn tại, chỉ có gift; Figma gốc cũng không có rating. → UI 5-sao trong DOC-v1.0-03 là **known prototype inconsistency** (phần tử UI lỗi thời/nhầm lẫn, KHÔNG phản ánh scope thật), không phải căn cứ để đảo ngược quyết định | **Resolved (tái khẳng định lần 2)** | 2026-07-27 | generate-tc: giữ nguyên — bước ngay sau "Hoàn thành" chỉ theo luồng GIFT, KHÔNG viết TC cho rating sao dù DOC-v1.0-03 có hiện UI. Đề xuất: khi có log-bug/dev stage, ghi nhận UI rating sao trong prototype là điểm cần dev xoá bỏ (không thuộc phạm vi generate-tc/analyze) |
| C-GENERAL-3 | REQ-CARRIER (profile), REQ-RECEIVER (profile) | DOC-v1.0-02 §A7 vs DOC-v1.0-03 (quan sát UI) | BRD §A7 khẳng định "Không tính điểm, không tier/xếp hạng, không CO₂..." — nhưng màn "Cá nhân" trong DOC-v1.0-03 hiển thị rõ: badge tier **"Hạng Đồng hành"**, chỉ số **"điểm uy tín"** (vd 4.8) và **"điểm ECO"** (vd 540) trên profile Carrier. Cùng loại mâu thuẫn UI-vs-BRD như C-GENERAL-2 (rating), nhưng KHÁC Ở CHỖ: điểm này chưa được user re-confirm trực tiếp như rating — không tự suy ra là "prototype inconsistency" | — | **Open** — cần user/BA xác nhận: (a) tier/điểm uy tín/điểm ECO cũng là UI lỗi thời cần bỏ (giống rating), hay (b) đây là phần thật sự có trong scope và BRD §A7 mới là phần chưa cập nhật | — | KHÔNG viết TC cho tier/điểm uy tín/điểm ECO cho tới khi có câu trả lời — nếu generate-tc chạy trước khi resolve, loại các field này khỏi TC scope của REQ-GENERAL-002/profile-related SC |
| C-GIFT-2 | REQ-GIFT-003, REQ-GIFT-004 | DOC-v1.0-03 (quan sát UI) vs Figma board gốc (node 23:153, section "Trạng thái hoàn thành") | Màn "Quà đã nhận" (lịch sử quà) quan sát được ở phone gắn nhãn "NGƯỜI NHẬN" (Receiver, Phan Văn Hưng) trong DOC-v1.0-03 — nhưng theo BRD, quà đi từ Người gửi → Người vận chuyển (Carrier mới là người nhận quà), không phải Receiver | **Bằng chứng Figma (2026-07-27):** Figma board gốc (file `SEu9ekmu2wh1XxZCJkqAbP`, node 23:153) ghi rõ ở connector cuối chuỗi "Tặng quà" (94:230→94:239): **"Note: màng hình này nằm ở menu Cá nhân \\ Quà đã nhận"** — note này nằm trên hàng "NGƯỜI GIAO" (Carrier), NGAY SAU bước "Người giao hàng nhận được thông báo" → "mở thông báo nhận được quà". Figma xác nhận rõ ràng: màn "Quà đã nhận" thuộc về Carrier, KHÔNG phải Receiver | **Resolved (độ tin cậy cao, dựa Figma)** — DOC-v1.0-03 hiện màn này ở phone Receiver nhiều khả năng là **lỗi wiring dữ liệu trong bản prototype** (gán nhầm role), không phải chủ đích thiết kế | 2026-07-27 | generate-tc: viết TC cho SC-GIFT-003/004 với Precondition = **Carrier's Cá nhân tab** (theo Figma), không phải Receiver. Khi vibe-test/execute trên UI thật, nếu vẫn thấy màn này ở Receiver thay vì Carrier → log bug (role-wiring sai), tham chiếu C-GIFT-2 |

### 6.1. Clarification Source Detail (per `references/quoting-guide.md` EC6)

#### C-SENDER-1 — Nhánh "Tôi nhận giao hàng" chưa implement

**Source Quote (ambiguous):**
> ""Tôi nhận giao hàng" — "Bạn đang có nhu cầu đi chuyển và có thể nhận giao hàng giúp cho đồng nghiệp" *(khớp Figma: nhánh "Tôi nhận giao hàng" trong section "93:217", có connector label "Đăng tin")* [...] **Known gap vs Figma:** Nhánh "Tôi nhận giao hàng" [...] chưa được implement trong bản HTML prototype này"

**Source Location:** `DOC-v1.0-01 §1.1 "Chọn vai trò" · paragraph "Known gap vs Figma"`

**Analyst Note:** Figma board mô tả nhánh Carrier tự đăng tin (reverse flow) nhưng bản HTML chỉ chạy được nhánh Sender đăng tin. Cần BA/PO confirm: nhánh này có trong scope v1.0 (chờ dev implement) hay defer sang version sau. Non-blocking vì không ảnh hưởng test nhánh đã có.

**Resolution Quote (2026-07-24, từ DOC-v1.0-02):**
> "Là Carrier đang có nhu cầu di chuyển, tôi muốn đăng tin "Tôi nhận giao hàng" với điểm xuất phát, điểm đến, khung giờ và tên/SĐT, để báo rằng tôi có thể nhận giao giúp đồng nghiệp trên đường đi." (US-D10, `DOC-v1.0-02 §D1b`)

**Resolution Note:** BRD xác nhận nhánh này CÓ trong scope chính thức v1.0 (Nhóm 3, US-D10→D13) — không phải out-of-scope như đoán trước đây. Đã tạo module OFFER với REQ-OFFER-001..004/SC-OFFER-001..004. Vẫn Blocked cho TC thật vì UI chưa dựng.

#### C-CARRIER-1 — Nhánh "Huỷ đơn" chưa implement

**Source Quote (ambiguous):**
> "**Known gap vs Figma:** Nhánh "Huỷ đơn" (mô tả trong Figma tại nhiều điểm... → dẫn tới section "HUỶ ĐƠN" với "xác nhận Huỷ đơn" → "Nhận thông báo" → "Trả đơn về lại bảng tin") chưa có UI trong bản HTML prototype."

**Source Location:** `DOC-v1.0-01 §2.5 "Hoàn thành" · paragraph "Known gap vs Figma" #1`

**Analyst Note:** Huỷ đơn là 1 nhánh nghiệp vụ quan trọng thường có trong app thực tế (đổi ý, sai thông tin...) nhưng thiếu hoàn toàn trong demo. Cần xác nhận đây có phải scope v1.0 không trước khi generate-tc phân bổ effort.

**Resolution Quote (2026-07-24, từ DOC-v1.0-02):**
> "popup huỷ bắt buộc nhập lý do (nút Xác nhận khoá tới khi có lý do); đơn huỷ ghi rõ ai huỷ (Người gửi/Người vận chuyển/Người nhận) + lý do, đồng bộ realtime cho cả 3 bên" (US-D16, `DOC-v1.0-02 §D1b`)

**Resolution Note:** BRD xác nhận CÓ trong scope, đặc tả rất chi tiết (CNL-01, BR-CNL-01, OPR-09/11). Đã tạo module CANCEL với REQ-CANCEL-001..004/SC-CANCEL-001..004. Vẫn Blocked cho TC thật vì UI chưa dựng.

#### C-CARRIER-2 — Nhánh "Tặng quà cảm ơn" chưa implement

**Source Quote (ambiguous):**
> "**Known gap vs Figma:** Nhánh "Tặng quà cảm ơn cho người vận chuyển" sau khi hoàn thành (Figma: "Cho phép người gửi gửi lời cảm ơn" → "Tặng quà → done" → Carrier "nhận được thông báo" → "mở thông báo nhận được quà", ghi chú "màn hình này nằm ở menu Cá nhân / Quà đã nhận") chưa có UI trong bản HTML prototype."

**Source Location:** `DOC-v1.0-01 §2.5 "Hoàn thành" · paragraph "Known gap vs Figma" #2`

**Analyst Note:** Tính năng thuộc luồng post-completion / retention, không chặn happy-path chính. Ghi nhận out-of-scope v1.0 trừ khi BA xác nhận ngược lại.

**Resolution Quote (2026-07-24, từ DOC-v1.0-02):**
> "4 loại quà: bông hoa, ly cà phê, gấu bông, vương miện — biểu tượng phi vật chất" (`DOC-v1.0-02 §A7`)

**Resolution Note:** BRD xác nhận CÓ trong scope, đặc tả chi tiết hơn cả Figma (4 loại quà cụ thể, gửi ngay không cần xác nhận). Đã tạo module GIFT với REQ-GIFT-001..003/SC-GIFT-001..003. Vẫn Blocked cho TC thật vì UI chưa dựng. **Lưu ý:** xem C-GENERAL-2 — có mâu thuẫn nội bộ trong BRD về việc quà ảo có thay thế hoàn toàn rating sao hay không.

#### C-SENDER-2 — Wizard không tạo listing độc lập

**Source Quote (ambiguous):**
> "**Known gap:** Đơn đăng qua wizard **không** xuất hiện như tin mới độc lập trong feed "Tin mới" của Carrier/Receiver — ghi đè vào 1 order slot có sẵn trong store demo. Không phải bug nghiệp vụ, là giới hạn kiến trúc của bản prototype"

**Source Location:** `DOC-v1.0-01 §1.5 "Theo dõi đơn (Sender)" · paragraph "Known gap"`

**Analyst Note:** Do tác giả tài liệu tự đánh giá "không phải bug" — nhưng vì đây là suy luận của analyst khi vibe-test, KHÔNG phải xác nhận từ BA/dev, vẫn giữ ở dạng Open để tránh giả định sai khi generate-tc/automation thật với backend multi-order.

#### C-ORDER-1 — Hành vi reset chưa rõ ràng với wizard form state

**Source Quote (ambiguous):**
> "Transition chỉ đi 1 chiều tuần tự, không có UI để lùi trạng thái (ngoại trừ nút toàn cục "↺ Chạy lại từ đầu" reset về `posted` ban đầu, KHÔNG xoá đơn vừa đăng qua wizard — cần verify lại kỹ hơn vì đã quan sát wizard giữ nguyên form data sau reset)."

**Source Location:** `DOC-v1.0-01 §4 "ORDER STATUS MACHINE" · "Ràng buộc quan trọng" bullet 1`

**Analyst Note:** Tác giả tài liệu tự đánh dấu "cần verify lại kỹ hơn" — đúng tinh thần KHÔNG đoán khi mơ hồ. Giữ Open, scenario SC-ORDER-002 chỉ test phần chắc chắn (status reset).

#### C-ORDER-2 — Ngưỡng thời gian hết hạn tin (EXPIRED) chưa xác định

**Source Quote (ambiguous):**
> "Quá hạn cấu hình mà chưa MATCHED → tự chuyển EXPIRED... [...] CÂU HỎI MỞ CHO BA: Ngưỡng giá trị hàng? Ảnh bắt buộc cho hàng > ngưỡng? Chia sẻ vị trí mặc định bật/tắt? Ai được xác nhận "đã nhận"? **Hạn tin mặc định?**"

**Source Location:** `DOC-v1.0-02 §D1b US-D04` + `§D5 "Câu hỏi mở cho BA"`

**Analyst Note:** Chính BRD liệt kê đây là câu hỏi mở chưa có câu trả lời — không phải lỗi phân tích, là gap có chủ đích trong tài liệu gốc. Không được tự chọn 1 con số (vd 24h/48h/3 ngày) để viết TC boundary — phải chờ BA. Non-blocking cho các scenario khác.

**Resolution (user, 2026-07-27):**
> "sau khi qua hạn ngày Từ ngày khi tạo sẽ hết hạn tin"

**Resolution Note:** Ngưỡng EXPIRED KHÔNG phải là khoảng thời gian cố định đếm từ lúc tạo tin (không phải duration như "24h sau khi đăng"), mà là **mốc tuyệt đối = giá trị field "Từ ngày"** mà Sender chọn ở wizard bước 2 (khoảng ngày "Từ ngày — Đến ngày"). Rule suy ra: nếu current date đã qua "Từ ngày" mà đơn vẫn ở `posted` (chưa MATCHED) → tự chuyển `EXPIRED`. Resolved — generate-tc có thể viết TC boundary dựa trên mốc "Từ ngày" (vd: current date = Từ ngày → chưa expired; current date = Từ ngày + 1 → expired) khi UI/worker được implement. Vẫn 🚫 Blocked cho TC thật vì chưa có UI/cơ chế backend trong prototype hiện tại.

#### C-GENERAL-2 — Mâu thuẫn nội bộ: có rating sao hay không?

**Source Quote (ambiguous, 2 đoạn mâu thuẫn nhau trong cùng 1 tài liệu):**
> Đoạn 1 (§A7): "Không tính điểm, không tier/xếp hạng, không CO₂, không quy đổi tiền / thanh toán in-app"
> Đoạn 2 (§A5 BR-INT-06): "Không đánh giá sao; ghi nhận thiện chí bằng quà ảo người gửi tặng người vận chuyển sau khi hoàn tất"
> Đoạn 3 (§D2, mâu thuẫn với đoạn 1&2): "[HOÀN TẤT] Đánh giá 2 chiều → (tùy chọn) ghi chi phí offline → CO₂ + điểm → COMPLETED"
> Đoạn 4 (§D3, cũng mâu thuẫn): "RAT-01/02 Đánh giá 2 chiều — 1–5 sao + nhận xét"

**Source Location:** `DOC-v1.0-02 §A5 BR-INT-06`, `§A7`, `§D2 "Workflow & Status Flow"`, `§D3 "Functional Requirements" RAT-01/02`

**Analyst Note:** Đây là mâu thuẫn nội bộ thật sự trong chính tài liệu BRD, không phải hiểu nhầm của analyst — §A (nền tảng chung, có vẻ là bản cập nhật mới hơn) khẳng định dứt khoát KHÔNG có rating/điểm/CO₂, thay bằng quà ảo; nhưng §D2/§D3 (phần Gửi Hàng chi tiết, có vẻ chưa được đồng bộ theo mô hình mới) vẫn liệt kê rating 1-5 sao + CO₂ + điểm như yêu cầu chính thức. **BLOCKER** cho scenario/TC ở bước ngay sau "Hoàn thành" — không viết TC cho bước rating cho tới khi BA xác nhận model đúng.

**Resolution (user, 2026-07-27):**
> "khong rating sao"

**Resolution Note:** Model chính thức = §A7/§A5 BR-INT-06 — **KHÔNG có đánh giá sao**, quà ảo (GIFT) là cơ chế duy nhất ghi nhận thiện chí sau "Hoàn thành". §D2 (bước "Đánh giá 2 chiều" trong workflow) và §D3 RAT-01/02 là phần spec cũ/chưa đồng bộ, KHÔNG được implement/test. Resolved — generate-tc có thể mở khoá TC cho bước ngay sau "Hoàn thành" ở SC-RECEIVER-003/SC-GIFT-002, chỉ theo luồng GIFT, không có bước rating sao. Nếu prototype/dev sau này hiện UI chấm sao, đó là bug (theo spec đã lỗi thời) — log bug tham chiếu C-GENERAL-2.

## 7. Automation Context (nếu có)
- Không áp dụng — dự án chưa có automation (xem `Project_rule.md`).

## 8. Deliverable Files Reference
| File | Đường dẫn | Mô tả |
|------|-----------|-------|
| Requirement Traceability | `02_.../v1.0/requirement_traceability.md` | Ma trận truy vết |
| Test Scenario Map | `02_.../v1.0/test_scenario_map.md` | Chi tiết scenarios |
| Test Data Catalog | `02_.../v1.0/test_data_catalog.md` | Dữ liệu test |
| Risk Assessment | `02_.../v1.0/risk_assessment.md` | Đánh giá rủi ro |

## 9. TC Generation Log
> Header khớp generate-tc (Mode + Techniques cols). Mode ∈ qc7/standard/comprehensive/selective (qc7 = default). Techniques = N/A (standard/qc7) hoặc danh sách B-ID (comprehensive/selective). Priority = breakdown P1/P2/P3 (generate-tc ghi); Review Status (review-tc ghi: ⏳/✅/score).

| DOC ID | Ngày generate | Tổng TC | File output | Priority | Mode | Techniques | Review Status |
|--------|--------------|---------|-------------|----------|------|------------|---------------|
| DOC-v1.0-01 | 2026-07-24 | 10 | fragments/TC-SENDER-v1.0.xlsx | P1:6, P2:4, P3:0 | qc7 | N/A | ⏳ |
| DOC-v1.0-01 | 2026-07-24 | 7 | fragments/TC-CARRIER-v1.0.xlsx | P1:5, P2:2, P3:0 | qc7 | N/A | ⏳ |
| DOC-v1.0-01 | 2026-07-24 | 4 | fragments/TC-RECEIVER-v1.0.xlsx | P1:3, P2:1, P3:0 | qc7 | N/A | ⏳ |
| DOC-v1.0-01 | 2026-07-24 | 4 | fragments/TC-ORDER-v1.0.xlsx | P1:2, P2:2, P3:0 | qc7 | N/A | ⏳ |
| DOC-v1.0-01 | 2026-07-24 | 1 | fragments/TC-GENERAL-v1.0.xlsx | P1:0, P2:0, P3:1 | qc7 | N/A | ⏳ |
| DOC-v1.0-01 | 2026-07-24 | 26 (consolidated) | TC-MASTER-v1.0.xlsx | P1:16, P2:9, P3:1 | qc7 | N/A | ✅ 97/100 (bản qc7 — đã superseded, xem dòng dưới) |
| DOC-v1.0-01 | 2026-07-24 | 59 | fragments/TC-SENDER-v1.0.xlsx | P1:7, P2:28, P3:24 | comprehensive | B1, B4, B6 | ⏳ (regenerate — cần review-tc lại) |
| DOC-v1.0-01 | 2026-07-24 | 7 | fragments/TC-CARRIER-v1.0.xlsx | P1:5, P2:2, P3:0 | comprehensive | B4 | ⏳ |
| DOC-v1.0-01 | 2026-07-24 | 4 | fragments/TC-RECEIVER-v1.0.xlsx | P1:3, P2:1, P3:0 | comprehensive | B4 | ⏳ |
| DOC-v1.0-01 | 2026-07-24 | 11 | fragments/TC-ORDER-v1.0.xlsx | P1:5, P2:6, P3:0 | comprehensive | B4, B6 | ⏳ |
| DOC-v1.0-01 | 2026-07-24 | 1 | fragments/TC-GENERAL-v1.0.xlsx | P1:0, P2:0, P3:1 | comprehensive | N/A (0-dim) | ⏳ |
| DOC-v1.0-01 | 2026-07-24 | 82 (consolidated, thay thế bản 26 TC qc7) | TC-MASTER-v1.0.xlsx | P1:20, P2:37, P3:25 | comprehensive | B1 EP, B4 ST, B6 EG (B2/B3/B5/B7/B8 xét đủ, N/A có lý do — xem Coverage Matrix sheet) | ✅ Recheck #2: 95/100 (1 Major casing bug "eP"/"cTA" + 2 Minor stale ref/câu mơ hồ) — đã fix ngay + tự verify bằng code (0 lỗi còn lại). Điểm ước tính ~100/100 (chưa qua thêm 1 lượt agent độc lập). |
| DOC-v1.0-03 | 2026-07-27 | 34 (sheet "Trang chủ" 15 + "Bảng tin" 19, sau 2 vòng mở rộng) | TC-MASTER-v1.0.xlsx | P1:1, P2:18, P3:15 | comprehensive | B1 EP, Database data-binding checks | ⏳ — **Bắt đầu chuyển TC-MASTER sang cấu trúc sheet-theo-tab** (thay module → tab bottom-nav, theo yêu cầu user). Vòng 1 (94 TC tổng): 9 Trang chủ + 6 Bảng tin (3 TC cũ TC-CARRIER-001/002/003 di chuyển từ sheet CARRIER, đổi prefix). Vòng 2 (113 TC tổng, cùng ngày, theo yêu cầu user "lên chi tiết case data load từ đâu"): mở rộng field-level/data-binding cho từng field trong 1 block (tiêu đề/địa chỉ/mốc thời gian lấy từ đâu, đúng dữ liệu đã đăng hay không) — Trang chủ 9→15 TC, Bảng tin 6→19 TC. Nhiều TC mới dùng Group=`Database` (kiểm tra data-binding thay vì chỉ UI hiển thị). 4 sheet còn lại (Đăng tin, Hoạt động, Cá nhân, Thông báo) sẽ chuyển tiếp ở lượt sau — cùng mức độ chi tiết field-level này. |
