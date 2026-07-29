# Risk Assessment — v1.1

> Tạo bởi: analyze-requirements (mode DELTA từ v1.0). Risk CARRIED không đổi — xem `02_analyze-requirements/v1.0/risk_assessment.md`. Bên dưới chỉ risk MỚI hoặc THAY ĐỔI severity so với v1.0.
> Cập nhật 2026-07-28 (lần 2): user đã resolve 4/4 clarification mới (C-ORDER-2, C-SENDER-3, C-CANCEL-1, C-GENERAL-4) — hầu hết risk bên dưới đã đóng hoặc hạ severity, còn 1 action-item thật (RISK-CANCEL-05, cần dev fix) và 1 risk vẫn Open (RISK-GENERAL-06, tier badge).
>
> **Structure-lock:** dùng DUY NHẤT 1 dạng bảng chi tiết hợp nhất bên dưới cho MỌI module.

## Tổng quan
| Module | Risk Level | Rủi ro chính |
|--------|-----------|--------------|
| ORDER | Medium (hạ từ High — đã resolved) | Ngưỡng EXPIRED đã chốt "Đến ngày"; risk còn lại chỉ là chưa có cơ chế backend/worker để test thật |
| SENDER | Medium (hạ từ High — đã resolved) | Danh mục "Loại hàng" đã xác nhận giữ 8 mục theo UI, "Thuốc/Y tế" KHÔNG phải hàng cấm — đóng nghi vấn contradiction P1 kế thừa từ v1.0 |
| CANCEL | **High (không đổi — action item thật)** | Rule đúng (BRD, tối thiểu 5 ký tự) đã chốt nhưng UI CHƯA implement — đây là gap thật cần dev fix, không phải ambiguity nữa |
| GENERAL | Low-Medium (hạ từ Medium — 1/2 risk đã resolved) | "Tin mới" cho cả 2 vai trò đã chốt; tier badge "Hạng Đồng hành" vẫn Open (chưa hỏi lại user) |

## Chi tiết rủi ro (bảng hợp nhất — 1 dạng cho mọi module)
| Risk ID | Module/Area | Rủi ro | Severity | Why (Source) | Test Focus | REQ/SC |
|---------|-------------|--------|----------|--------------|------------|--------|
| RISK-ORDER-03 | ORDER / EXPIRED threshold | **✅ Resolved** — ngưỡng EXPIRED = "Đến ngày" (user, 2026-07-28). Risk còn lại: prototype chưa có cơ chế backend/worker để tự động trigger EXPIRED — SC-ORDER-007 vẫn 🚫 Blocked cho TC thật dù business rule đã rõ | Medium | `DOC-v1.1-01 §D8.1/§D8.2`, resolved qua user 2026-07-28 | Viết TC boundary quanh mốc "Đến ngày" ngay khi có UI/worker; cho tới đó chỉ giữ ở mức spec | SC-ORDER-007, REQ-ORDER-004, C-ORDER-2 |
| RISK-SENDER-05 | SENDER / Loại hàng danh mục | **✅ Resolved** — giữ 8 category theo UI (BRD 5-category không áp dụng); "Thuốc/Y tế" xác nhận KHÔNG phải hàng cấm (user, 2026-07-28) — đóng nghi vấn contradiction P1 kế thừa từ v1.0 (TC-SENDER-EP07) | Low (hạ từ High) | `DOC-v1.1-01 §D8.1` vs UI `DOC-v1.1-02`, resolved qua user 2026-07-28 | Viết EP bình thường cho đủ 8 category, không cần risk-flag P1 riêng cho "Thuốc/Y tế" nữa | SC-SENDER-003, REQ-SENDER-002, C-SENDER-3 |
| RISK-CANCEL-05 | CANCEL / Validation lý do | **Action item thật (không còn ambiguity):** rule đúng = BRD VAL-04 (tối thiểu 5 ký tự, user 2026-07-28 xác nhận "lấy theo rule BRD"), nhưng UI hiện tại CHỈ chặn rỗng — đây là gap implementation thật, TC viết theo BRD sẽ FAIL trên UI hiện tại cho tới khi dev bổ sung rule | **High** | `DOC-v1.1-01 §D8.3 VAL-04` vs UI trực tiếp đã verify `DOC-v1.1-02`, resolved qua user 2026-07-28 | Viết TC theo BRD (5 ký tự tối thiểu) làm target; kết quả FAIL trên UI hiện tại là ĐÚNG dự kiến — khuyến nghị log-bug tham chiếu C-CANCEL-1 khi tới giai đoạn đó | SC-CANCEL-001, REQ-CANCEL-001, C-CANCEL-1 |
| RISK-GENERAL-05 | GENERAL / Trang chủ dashboard | **✅ Resolved** — "Tin mới" cap-5 áp dụng cho cả Sender lẫn Carrier (user, 2026-07-28 "viết theo UI luôn") | Low (hạ từ Medium) | `DOC-v1.1-01 §D1b US-D06` vs UI `DOC-v1.1-02`, resolved qua user 2026-07-28 | Viết TC cap-5 dùng chung 2 vai trò; cần data demo >5 tin để tự verify ngưỡng cắt thật | SC-GENERAL-003, REQ-GENERAL-003, C-GENERAL-4 |
| RISK-GENERAL-06 | GENERAL / Profile tier badge | Tier badge "Hạng Đồng hành" vẫn hiện trên Cá nhân dù BRD §A7 khẳng định "không tier/xếp hạng" — cùng loại rủi ro với rating sao (C-GENERAL-2, đã xác nhận là UI lỗi thời không viết TC) nhưng CHƯA được user xác nhận tương tự cho tier badge — **vẫn Open, chưa hỏi trong đợt resolve này** | Low-Medium | `DOC-v1.1-01 §A7` vs UI trực tiếp `DOC-v1.1-02` | KHÔNG viết TC cho tier badge tới khi user quyết định giữ/bỏ | REQ-GENERAL-002 (profile), C-GENERAL-3 |
| RISK-RECEIVER-05 | RECEIVER / SLA xác nhận | SLA "2 giờ nhắc + 2 giờ admin" (BR-CNF-04) hoàn toàn spec-only — prototype không có cơ chế timer, nên rủi ro chính là generate-tc/dev estimate effort sai nếu không tách rõ happy-path (test được ngay) khỏi SLA-timeout (cần backend + worker mới test được) | Low | `DOC-v1.1-01 §D1b US-D14, §D4 BR-CNF-04` | Tách 2 TC riêng: happy-path (Ready) và SLA-timeout (Blocked, spec-only) | SC-RECEIVER-003, REQ-RECEIVER-002 |

## Khuyến nghị tổng thể
1. **✅ Đã resolve (2026-07-28, lần 2):** C-ORDER-2, C-SENDER-3, C-GENERAL-4 — không còn chặn generate-tc, viết TC bình thường theo resolution đã ghi.
2. **🔴 Action item thật cần theo dõi:** **C-CANCEL-1 (RISK-CANCEL-05)** — không còn là câu hỏi mở, mà là gap implementation đã xác nhận (UI thiếu enforce rule 5 ký tự). Viết TC theo BRD, kỳ vọng FAIL trên UI hiện tại, và cân nhắc log-bug ngay khi tới giai đoạn log-bug/execute.
3. **Ưu tiên test P1 high-risk (không đổi từ v1.0 + mới):** SC-SENDER-003 (validation gate), SC-CANCEL-001 (spec vs implementation), toàn bộ chuỗi transition CARRIED (SC-CARRIER-002/004/005/006, SC-RECEIVER-003/004, SC-ORDER-002/003).
4. **Performance / cần môi trường:** SLA timeout (SC-RECEIVER-003 nhánh 2), EXPIRED worker (SC-ORDER-007) — defer tới khi có backend thật.
5. **Còn 1 điểm Open thật sự cần hỏi lại:** C-GENERAL-3 (tier badge "Hạng Đồng hành") — chưa nằm trong đợt resolve vừa rồi, vẫn cần user xác nhận giữ hay bỏ trước khi mở rộng TC cho profile.
6. **Đã đóng ở v1.1 (không cần theo dõi tiếp):** C-GIFT-2 (role bug fixed, verify khớp Figma + UI).
