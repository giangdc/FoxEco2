# Project Rules — FoxEco

> Quy tắc dự án dùng chung cho toàn pipeline QA. Các skill đọc file này để áp đúng convention.

## 1. Thông tin dự án (Project Info)
- **Tên dự án:** FoxEco
- **Loại sản phẩm:** SDK tích hợp vào app mobile **FoxPro** có sẵn (không phải web app độc lập)
- **QC phụ trách:** GiangDC2
- **Mode:** Solo
- **Version đầu tiên:** v1.0

## 2. Môi trường (Environments)
| Env | Host app | Default |
|-----|----------|---------|
| STG | FoxPro (mobile) | ✅ |

> Không có URL riêng vì FoxEco là SDK, không phải web app. Chi tiết host app/platform/build cập nhật vào `07_environments/environments.md`.

## 3. Loại kiểm thử (Test Types)
- Smoke
- Functional
- Regression

## 4. Ngôn ngữ (Language)
- Nội dung test case, mô tả, bước thực hiện, các thông báo trả ra trên terminal khi làm việc: **Tiếng Việt**
- Thuật ngữ kỹ thuật, keywords, status: **Tiếng Anh**

## 5. Automation
- **Có automation:** Không (hiện tại)
- (Khi cần thêm: chạy `/init-source-code --archetype appium-java` vì FoxEco là SDK tích hợp app mobile — Appium Java phù hợp nhất để scaffold `10_source-code/`.)

## 6. Quy tắc đặt tên (Naming Conventions)
- Documents: `DOC-v[VERSION]-[NN]`
- Scenarios: `SC-[MODULE]-[NNN]`
- Test cases: `TC-[MODULE]-[NNN]`
- TC Master: `TC-MASTER-v[VERSION].xlsx`
- Bug reports: `BUG-[NNN]-[short-title].md`
- Test runs: `TR-v[VERSION]-[YYYY-MM-DD].md`
- Reports: `REPORT-[TYPE]-v[VERSION]-[DATE].md`

## 7. Priority & Severity
- Priority: P1 (Highest) · P2 (High) · P3 (Medium) · P4 (Low)
- Severity: Critical · High · Medium · Low

## 8. Quality Gates (mặc định)
- G1: TC Review score ≥ 70
- G2: P1 pass rate = 100%
- G3: Overall pass rate ≥ 90%
- G4: No P1 bugs open
- G5: Bug fix rate ≥ 80%
- G6: Blocked ≤ 0
- G7: SRC-TC match score ≥ 70 (nếu có automation)

## 9. DOC Notation
req_notation: FR/VR (doc-native, module-prefixed)
# FR/VR: doc đánh số Functional/Validation Rule (vd kiểu FCP)
# none:  doc không đánh số → traceability dùng DOC-ID §section
# auto:  chưa rõ → analyze-requirements tự phát hiện từ doc ở lần chạy đầu rồi GHI NGƯỢC giá trị thật vào đây
#
# [auto-detected 2026-07-24 by analyze-requirements --init v1.0]
# DOC-v1.0-01 (FoxEco BRD v3.1) CÓ đánh số requirement, nhưng theo ID riêng từng domain thay vì
# 1 cặp FR/VR thống nhất: ORD-NN, ASN-NN, DLV-NN (viết tắt PUP/GPS/DLV/COST theo bước flow), GIFT-NN,
# CNL-NN, MTCH-NN, LOC-NN, RAT-NN (chức năng Gửi Hàng — bảng §D3); BR-<MODULE>-NN (Business Rules —
# §D4/§A5); NTF-NN (Notifications — §D6); OPR-NN (Operating Rules — §D7); NT-NN/USR-NN/TS-NN
# (Nền tảng chung — §A2/§A6/§A8); US-D<NN> (User Story kèm cột Acceptance Criteria riêng — §D1b).
# → Traceability cột "Maps (Ref DOC)" dùng TRỰC TIẾP ID gốc này (vd `ORD-01`, `BR-CNL-01`, `US-D16`),
#   không quy đổi sang ký hiệu FR/VR chuẩn hoá. DOC-v1.0-02 (PRD tái dựng từ demo, .docx) KHÔNG có ID
#   riêng cho từng field — định vị bằng `§section · Table N` (heading + số bảng).
# req_notation ghi "FR/VR (doc-native, module-prefixed)" để phản ánh: có đánh số thật (không phải
# "none"), nhưng không phải 1 ký hiệu FR/VR đơn nhất — mọi lần chạy sau dùng nguyên ID gốc theo domain.

## 10. Custom Rules

### 10.1 UI Figma phải khớp Tài liệu mới được viết TC (added 2026-07-24, QA GiangDC2)
- Chỉ viết test case khẳng định 1 field/nút/màn hình/hành vi UI cụ thể khi **cả 2 nguồn khớp nhau**:
  (a) tài liệu yêu cầu (BRD/PRD/US) và
  (b) bằng chứng UI thực tế (ảnh Figma DOC-v1.0-04 hoặc quan sát app STG thật).
- Nếu 2 nguồn **KHÔNG khớp** (field có trong tài liệu nhưng không thấy trên UI/Figma, hoặc ngược lại) → **KHÔNG tự suy đoán/bịa vị trí hay hành vi UI**. Bắt buộc:
  1. Ghi nhận thành clarification mới (`C-[MODULE]-NN`) trong `test_scenario_map.md`/`MEMORY.md`, đánh dấu rõ "chưa xác nhận UI".
  2. Không viết TC khẳng định field/hành vi đó tồn tại ở 1 màn hình cụ thể cho tới khi có xác nhận (BA/PO hoặc vibe-test trên app thật).
  3. Nếu cần, viết 1 TC dạng "GAP finding" ghi nhận sự thiếu vắng, thay vì TC test hành vi giả định.
- Áp dụng cho mọi skill sinh/viết TC: `generate-tc`, `vibe-test`, trả lời liệt kê case trực tiếp trong chat.
- Case gốc (ví dụ minh hoạ khi 2 nguồn không khớp): `USR-07` "Cấu hình kênh liên hệ sẽ lộ" (SĐT/Workplace-email) — có trong BRD (`DOC-v1.0-01`) nhưng KHÔNG xuất hiện ở bất kỳ ảnh Figma nào (`DOC-v1.0-04`) của màn Cá nhân, và QA xác nhận không thấy trên app STG thật. **Cập nhật 2026-07-27:** `C-USR-02` nay đã **Resolved — Deferred** (BA/PO xác nhận tính năng này là phase sau, không thuộc scope UI v1.0) — không còn là GAP đang chờ xác nhận nữa, nhưng vẫn giữ làm case tham khảo cho rule này khi gặp mâu thuẫn tương tự ở clarification khác.

### 10.2 Màn hình có tab/segmented-control → mỗi tab 1 TC riêng verify data (added 2026-07-27, QA GiangDC2)
- Khi 1 màn hình có tab switcher/segmented-control lọc dữ liệu theo trạng thái (vd "Đang diễn ra"/"Đã hoàn thành"), **KHÔNG gộp việc verify data của cả 2 (hoặc nhiều) tab vào chung 1 TC "chuyển tab qua lại"**.
- Bắt buộc: mỗi tab có **≥1 TC riêng biệt** verify đúng data hiển thị khi tab đó active (danh sách chỉ chứa đúng nhóm trạng thái thuộc tab đó, không lẫn dữ liệu của tab khác).
- Lý do: khi 1 TC gộp gồm nhiều bước kiểm tra data ở nhiều tab, nếu FAIL sẽ không rõ ngay tab nào sai (phải đọc lại từng step) — tách riêng giúp trace lỗi tức thì + khớp nguyên tắc atomic test case (1 TC verify 1 điều kiện rõ ràng).
- Việc UI tab switcher tồn tại/switch được (cơ chế bấm đổi tab) vẫn có thể giữ là 1 TC riêng, độc lập với các TC verify-data-theo-tab.
- Áp dụng cho mọi skill sinh TC: `generate-tc`, `vibe-test`, trả lời liệt kê case trực tiếp trong chat.
- Case gốc: màn "Hoạt động" (Đơn của tôi) — SC-ORD-017 (data tab "Đang diễn ra") và SC-ORD-026 (data tab "Đã hoàn thành"), tách ra từ 1 TC gộp ban đầu.

### Phase 1 Scope (PM confirm 2026-07-24)
PM chốt phạm vi kiểm thử v1.0 (Phase 1) chỉ gồm 5 luồng chính:
1. Đăng tin (NEED/OFFER) — module ORD
2. Bảng tin — module ORD (screen Bảng tin)
3. Ghép nối — module ASN (⚠ chưa rõ có gồm auto-match OFFER↔NEED hay chỉ luồng thủ công — câu hỏi RIÊNG về scope Phase 1 test, khác clarification C-xxx, PM chưa trả lời)
4. Xác nhận nhận hàng / hoàn thành — module DLV (⚠ chưa rõ có gồm ảnh bằng chứng/GPS/chi phí/báo sự cố hay chỉ core confirm — câu hỏi RIÊNG về scope Phase 1 test, khác clarification C-xxx, PM chưa trả lời)
5. Đánh giá — module GIFT (✅ Resolved 2026-07-27: "Đánh giá" trong Phase 1 chỉ có nghĩa **Quà ảo (GIFT-01)** — Chấm sao/RAT-01/02 là phase sau, out of scope v1.0, xem C-GIFT-01)

**Ngoài phạm vi Phase 1 (đã xác nhận Out of scope v1.0, 2026-07-27):** CNL (Huỷ đơn), NTF (Thông báo), TS (Trust & Safety/Admin), USR chỉ số cá nhân nâng cao (tier/điểm ECO/CO2), chỉnh sửa tin (ORD-10), ảnh bằng chứng/GPS/chi phí/báo sự cố (nhánh phụ của DLV), auto-match tuyến OFFER↔NEED (nhánh phụ của ASN).

**Câu hỏi ưu tiên cần PM/BA trả lời trong scope Phase 1 — Đã resolved (2026-07-27, BA/PO trả lời qua chat, chi tiết đầy đủ xem `02_analyze-requirements/v1.0/MEMORY.md §6`):**
- "Đánh giá" = Quà ảo hay Chấm sao? → **Quà ảo (GIFT-01)**; Chấm sao là phase sau (C-GIFT-01, C-USR-01: Resolved — Deferred).
- Ai được xác nhận "Đã nhận hàng"? → **Chỉ Receiver** (C-DLV-01: Resolved).
- Ngưỡng giá trị hàng cảnh báo bảo hiểm? → **Chưa làm ở v1.0** (C-ORD-02: Resolved — Deferred).
- Wizard đăng tin có field nào bắt buộc không? → **Có** — Loại hàng/Giá trị (B1) + Người nhận (B2) bắt buộc, maxlength TBD (C-ORD-01: Resolved).
- Hạn tin mặc định bao lâu? → **Theo giá trị "Đến ngày" user tự chọn** lúc đăng tin, không phải hằng số (C-ORD-03: Resolved).
- SĐT có nên hiện sớm ở Chi tiết tin trước khi ghép không? → **Không** — chỉ lộ sau khi ghép, theo BRD (C-ASN-01: Resolved).
- Chủ tin/Người nhận có được tự "nhận mang giúp" tin của mình không? → **Không**, khớp OPR-05 (C-ASN-02: Resolved).
- Dùng UI nào cho màn xác nhận nhận hàng? → **Modal đơn giản** (theo Figma); form đầy đủ out of scope v1.0 (C-DLV-03: Resolved).

**Còn Open thực sự (chưa có câu trả lời):** `C-ORD-05` (biến thể "Mã tin"), `C-NTF-01` (danh sách thông báo chính thức — đã có bảng unified 3 nguồn ở `MEMORY.md §6.1` chờ BA chọn), `C-DLV-02` (default bật/tắt chia sẻ vị trí), maxlength cụ thể của `C-ORD-01`.
