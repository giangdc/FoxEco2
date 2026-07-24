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
- Case gốc (ví dụ vi phạm nếu không theo rule): `USR-07` "Cấu hình kênh liên hệ sẽ lộ" (SĐT/Workplace-email) — có trong BRD (`DOC-v1.0-01`) nhưng KHÔNG xuất hiện ở bất kỳ ảnh Figma nào (`DOC-v1.0-04`) của màn Cá nhân, và QA xác nhận không thấy trên app STG thật → xem `C-USR-02` trong `MEMORY.md`.

### Phase 1 Scope (PM confirm 2026-07-24)
PM chốt phạm vi kiểm thử v1.0 (Phase 1) chỉ gồm 5 luồng chính:
1. Đăng tin (NEED/OFFER) — module ORD
2. Bảng tin — module ORD (screen Bảng tin)
3. Ghép nối — module ASN (⚠ chưa rõ có gồm auto-match OFFER↔NEED hay chỉ luồng thủ công — xem câu hỏi B7 dưới)
4. Xác nhận nhận hàng / hoàn thành — module DLV (⚠ chưa rõ có gồm ảnh bằng chứng/GPS/chi phí/báo sự cố hay chỉ core confirm — cần hỏi PM)
5. Đánh giá — module GIFT (⚠ **chưa rõ nghĩa là Quà ảo (GIFT-01) hay Chấm sao (RAT-01/02)** — câu hỏi ưu tiên #1, xem MEMORY.md C-GIFT-01)

**Ngoài phạm vi Phase 1 (note lại, confirm sau):** CNL (Huỷ đơn), NTF (Thông báo), TS (Trust & Safety/Admin), USR chỉ số cá nhân nâng cao (tier/điểm ECO/CO2), chỉnh sửa tin (ORD-10), ảnh bằng chứng/GPS/chi phí/báo sự cố (nhánh phụ của DLV), auto-match tuyến OFFER↔NEED (nhánh phụ của ASN).

**Câu hỏi ưu tiên cần PM/BA trả lời trong scope Phase 1** (chi tiết đầy đủ + Source Quote xem `02_analyze-requirements/v1.0/MEMORY.md §6`):
- "Đánh giá" = Quà ảo hay Chấm sao? (liên quan C-GIFT-01, C-USR-01)
- Ai được xác nhận "Đã nhận hàng" — chỉ Receiver hay cả Sender? (C-DLV-01)
- Ngưỡng giá trị hàng cảnh báo bảo hiểm là bao nhiêu? (C-ORD-02)
- Wizard đăng tin có field nào bắt buộc không? (C-ORD-01)
- Hạn tin mặc định bao lâu? (C-ORD-03)
- SĐT có nên hiện sớm ở Chi tiết tin trước khi ghép không? (C-ASN-01)
- Chủ tin/Người nhận có được tự "nhận mang giúp" tin của mình không? (C-ASN-02)
- Dùng UI nào cho màn xác nhận nhận hàng — modal đơn giản hay form đầy đủ? (C-DLV-03)
-
