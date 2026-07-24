# Risk Assessment — v1.0

> Tạo bởi: analyze-requirements. Đánh giá rủi ro per module + định hướng test focus cho generate-tc/vibe-test.
>
> **Structure-lock:** dùng DUY NHẤT 1 dạng bảng chi tiết hợp nhất bên dưới cho MỌI module.

## Tổng quan
| Module | Risk Level | Rủi ro chính |
|--------|-----------|--------------|
| USR | Medium | Chỉ số cá nhân — chưa chốt có tier/điểm ECO/CO2 hay không (demo vs BRD mâu thuẫn) |
| ORD | High | Wizard thiếu validate bắt buộc + ngưỡng giá trị hàng chưa xác định + hàng cấm (thuốc) vẫn chọn được |
| ASN | High | SĐT lộ sớm trước khi ghép + double-accept race condition + tự khớp chính mình chưa bị chặn đúng |
| DLV | High | Actor được quyền xác nhận "Đã nhận" không nhất quán giữa các nguồn (Receiver-only vs Receiver/Sender) |
| GIFT | Medium-High | RAT-01/02 (đánh giá sao) mâu thuẫn 4 vị trí trong BRD — rủi ro build sai scope nếu không chốt trước |
| CNL | Medium | Màn "Báo sự cố" (lối thoát duy nhất sau IN_TRANSIT) chưa có đặc tả — rủi ro user bị "kẹt" đơn |
| NTF | Medium | Nội dung + tham số vận hành (bán kính tuyến, độ lệch khung giờ) đều "Nháp — chờ BA bổ sung" |
| TS | Medium | Admin Web Portal không có đặc tả UI — không test trực tiếp được escalation/admin intervention |

## Chi tiết rủi ro (bảng hợp nhất — 1 dạng cho mọi module)
| Risk ID | Module/Area | Rủi ro | Severity | Why (Source) | Test Focus | REQ/SC |
|---------|-------------|--------|----------|--------------|------------|--------|
| RISK-USR-01 | USR / Chỉ số cá nhân | Demo hiển thị Hạng thành viên + Điểm ECO + Điểm uy tín; BRD (USR-05, A7) khẳng định KHÔNG tính điểm/tier/CO2 — chưa chốt bản build theo nguồn nào | Medium-High | §A6/§A7 (C-USR-01) | Verify Trang cá nhân chỉ hiện 2 chỉ số theo BRD; nếu bản build có tier/điểm → escalate ngay, không tự coi là "đủ pass" | SC-USR-004, REQ-USR-004 |
| RISK-ORD-01 | ORD / Wizard validate | Không có trường bắt buộc ở Bước 1 (Loại hàng/Giá trị) và Bước 2 (toàn bộ Người nhận) — có thể đăng tin thiếu thông tin liên hệ người nhận, gây khó khăn khi giao hàng thực tế | High | §3.5.1, §3.5.2 (C-ORD-01) | Test cả 2 nhánh (để trống hiện tại vs BA có thể bắt buộc sau); ưu tiên xác nhận BA trước automate | SC-ORD-007, REQ-ORD-002 |
| RISK-ORD-02 | ORD / Ngưỡng giá trị hàng | Ngưỡng kích hoạt cảnh báo bảo hiểm (BR-ORD-03) chưa có con số — không thể viết BVA chính xác, rủi ro miss case hàng giá trị cao không được cảnh báo | Medium-High | §D5 "Câu hỏi mở cho BA" (C-ORD-02) | Chốt ngưỡng với BA trước khi viết TC BVA; tạm test bằng giá trị "rõ ràng cao" (vd nhiều triệu đồng) để verify cơ chế cảnh báo tồn tại | SC-ORD-013, REQ-ORD-009 |
| RISK-ORD-03 | ORD / Hàng cấm | Chip Loại hàng "Thuốc/Y tế" vẫn là lựa chọn hợp lệ dù nguyên tắc cấm gửi thuốc — rủi ro pháp lý/compliance nếu không có validate rõ ràng | High | §3.5.1 Table 6, §1.4 (C-ORD-04) | Xác nhận ranh giới "Thuốc/Y tế" hợp lệ vs "thuốc" cấm với BA; test cả banner cảnh báo lẫn cơ chế chặn thật (nếu có) | SC-ORD-014, REQ-ORD-010 |
| RISK-ORD-04 | ORD / Mốc khoá chỉnh sửa | US-D19 AC nói "sau IN_TRANSIT không cho sửa" trong khi 3 nguồn khác (ORD-10/BR-EDIT-01/OPR-10) đều khoá từ MATCHED — nếu build theo US-D19 sẽ cho sửa tin đã có người nhận (MATCHED→IN_TRANSIT), rủi ro dữ liệu đơn không khớp giữa 2 bên | Medium | §D1b US-D19 vs §D3/§D4/§D7 | Verify chính xác mốc khoá = MATCHED (đa số nguồn); regression nếu phát hiện build cho sửa tới IN_TRANSIT | SC-ORD-009, REQ-ORD-006 |
| RISK-ASN-01 | ASN / Lộ SĐT sớm | Demo Chi tiết tin hiện sẵn SĐT+nút Gọi của Người gửi ngay từ "Chờ ghép", vi phạm cam kết "SĐT chỉ lộ sau khi ghép" (BR-CON-02) — rủi ro privacy | High | §3.4 (C-ASN-01) | Regression test SC-ASN-003 kỹ — đây là bug tiềm ẩn đã biết trên bản hiện tại | SC-ASN-003, REQ-ASN-002 |
| RISK-ASN-02 | ASN / Double-accept | 2 Carrier bấm "Tôi mang giúp được" gần đồng thời — nếu tx lock không hoạt động đúng, có thể ghép nhầm cho cả 2 hoặc lỗi trạng thái đơn | High | §D3 row ASN-03, §D7 row OPR-03 | Test concurrency thực tế (2 request gần như đồng thời) nếu có thể; ưu tiên P1 | SC-ASN-004, REQ-ASN-003 |
| RISK-ASN-03 | ASN / Tự khớp chính mình | Demo cho phép chủ tin/Người nhận tự bấm "Tôi mang giúp được" trên tin liên quan đến mình, vi phạm OPR-05 — rủi ro gian lận (tự tạo đơn "đã giúp" ảo nếu sau này có gamification quay lại) | High | §7 Table 17 #9 (C-ASN-02) | Regression test SC-ASN-011 kỹ — bug tiềm ẩn đã biết trên bản hiện tại | SC-ASN-011, REQ-ASN-008 |
| RISK-DLV-01 | DLV / Actor xác nhận "Đã nhận" | DLV-03 (D3) cho phép cả Sender xác nhận, nhưng BR-INT-03 (A5) + demo chỉ cho Receiver — nếu build sai theo DLV-03, Sender có thể tự chốt "Hoàn thành" mà không cần Receiver thực sự nhận hàng → rủi ro gian lận/tranh chấp | High | §D3 row DLV-03, §A5 row BR-INT-03, DOC-v1.0-02 §5.2 (C-DLV-01) | Verify CHỈ Receiver bấm được nút xác nhận; Sender xem màn tương ứng phải KHÔNG có nút này | SC-DLV-005, SC-DLV-011, REQ-DLV-003 |
| RISK-DLV-02 | DLV / 2 UI xác nhận nhận hàng | Modal đơn giản (§5.2) vs form đầy đủ có ảnh bằng chứng + điểm uy tín (§5.3) chưa chốt bản chính thức — automation/vibe-test có thể nhắm sai màn nếu build thay đổi UI | Medium | §5.2, §5.3 (C-DLV-03) | Xác nhận UI chính thức với đội thiết kế trước khi viết TC step-by-step chi tiết | SC-DLV-011 |
| RISK-DLV-03 | DLV / Thứ tự trạng thái backend | US-D09 mô tả ràng buộc UI (nút disable) nhưng không có bằng chứng validate ở tầng API/backend — nếu chỉ chặn UI, có thể bypass qua API trực tiếp | Medium | §D1b US-D09 | Nếu có quyền test API: verify backend cũng reject request "Đã giao" khi chưa "Tôi đã lấy hàng", không chỉ dựa vào UI disable | SC-DLV-010, REQ-DLV-006 |
| RISK-GIFT-01 | GIFT / RAT-01/02 | Đánh giá 1-5 sao (D3) mâu thuẫn trực tiếp nguyên tắc cốt lõi "không đánh giá sao" (A5/A7/A8) — nếu team dev build theo D3 sẽ lệch hẳn định hướng sản phẩm (Quà ảo thay vì Rating) | High | §D3 row RAT-01/02 vs §A5/§A7/§A8/§A10 (C-GIFT-01) | KHÔNG viết TC cho tính năng rating tới khi BA/PO xác nhận chính thức; theo dõi sát changelog BRD | REQ-GIFT-002 |
| RISK-CNL-01 | CNL / Màn Báo sự cố | Sau IN_TRANSIT, đường huỷ thường bị khoá hoàn toàn — lối thoát duy nhất "Báo sự cố" lại chưa có đặc tả field nào — rủi ro user bị "kẹt" đơn không có cách xử lý rõ ràng khi có sự cố thực tế | Medium | §D4 row BR-ASN-03, DOC-v1.0-02 §8 Table 18 (C-CNL-01) | Xác nhận thiết kế màn Báo sự cố sớm — đây là gap ảnh hưởng trực tiếp trải nghiệm khi có sự cố thật (hàng hỏng/mất) | SC-DLV-009, REQ-DLV-005 |
| RISK-NTF-01 | NTF / Nội dung thông báo | Toàn bộ nội dung 9 loại thông báo (D6) được doc tự đánh dấu "Nháp — chờ BA review & bổ sung" — dễ lệch giữa expected hiện tại và bản chính thức | Medium | §D6 (nháp) | Test theo baseline hiện tại nhưng đánh dấu rõ "cần re-sync khi BA duyệt nội dung final" trong TC | SC-NTF-001..005, REQ-NTF-001 |
| RISK-NTF-02 | NTF-ASN / Tham số vận hành | Bán kính/định nghĩa "cùng tuyến", độ lệch khung giờ, chu kỳ quét khớp (D7) đều "Chờ BA bổ sung" — khó test chính xác biên của việc match tuyến | Medium | §D7 (C-NTF-02) | Test case rõ ràng (khác tỉnh hẳn / cùng địa chỉ chính xác) để tránh vùng xám; defer BVA biên tới khi có tham số | SC-ASN-009, REQ-ASN-006 |
| RISK-TS-01 | TS / Admin Portal | Không có đặc tả UI Admin Web Portal trong cả 2 tài liệu — không thể test trực tiếp escalation/admin intervention, chỉ test được hệ quả gián tiếp từ phía end-user | Medium | §A3 (C-TS-01) | Test hệ quả quan sát được (đơn chuyển "chờ admin hỗ trợ" sau 4h); bổ sung TC Admin khi có đặc tả UI | SC-TS-003, REQ-TS-002 |

## Khuyến nghị tổng thể
1. **Resolve blocker clarifications trước generate-tc các scenario liên quan:** C-USR-01 (tier/điểm), C-ORD-02 (ngưỡng giá trị hàng), C-DLV-01 (actor xác nhận nhận hàng), C-GIFT-01 (RAT-01/02 rating).
2. **Ưu tiên test P1 high-risk:** SC-ASN-003/004/011 (privacy + double-accept + tự khớp), SC-DLV-005/006/010/011 (state-gate + actor xác nhận), SC-ORD-009/014 (khoá sửa + hàng cấm).
3. **Performance / cần môi trường:** SC-ASN-004 (concurrency 2 carrier đồng thời) cần môi trường test song song thật; SC-ORD-005/SC-DLV-007 (auto-expire/escalate theo giờ) cần mock thời gian hoặc môi trường chờ dài.
4. **ID/text cleanup (non-blocking, cần trước automation):** chốt nội dung 9 thông báo NTF-01..09 (đang nháp), chốt UI chính thức màn "Xác nhận đã nhận hàng" (2 biến thể), bổ sung đặc tả màn "Báo sự cố" và Admin Web Portal.
