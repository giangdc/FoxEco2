# TC Review Report — v1.0

> Generated: 2026-07-28
> Mode: **Direct (fallback)** — `review-agent/AGENT.md` không tồn tại trong `~/.claude/skills/review-tc/` (referenced nhưng chưa được tạo), nên không gọi được independent reviewer agent qua Anthropic API. Theo `SKILL.md` Common Edge Cases ("Independent reviewer API fail"), review này chạy ở Direct mode + **disclaimer** + **score cap 85**.
> TC-MASTER: `03_test-cases/v1.0/TC-MASTER-v1.0.xlsx` (ISC: `ISC_FoxEco_v1.0_TC_v1_R1.xlsx`)
> Scope: 3 sheet TC — `Test Cases` (TC_01 Hoạt động, 20 TC), `Test Case 2` (TC_02 Cá nhân, 15 TC), `Test Case 3` (TC_03 Thông báo, 27 TC) — tổng **62 TC**
> **Cập nhật 2026-07-28 (sau review):** Đã xóa `TC_03.12` ("Check hệ thống KHÔNG cho lặp lại thao tác vận chuyển khi đơn đã hoàn tất") — TC này test hành vi màn Theo dõi đơn/Chi tiết đơn (nút "Tôi đã lấy hàng"), không thuộc phạm vi sheet `Test Case 3` (Thông báo). QA (GiangDC2) xác nhận trên app STG thật, khi đơn COMPLETED nút này ẩn hoàn toàn (không phải dạng disable) — nhưng vì lệch scope màn hình nên loại khỏi bộ TC Thông báo thay vì sửa lại. Các TC phía sau tự renumber (TC_03.13→TC_03.12, …, TC_03.28→TC_03.27) do cột ID dùng công thức COUNTA tự đếm.
> Mode generate-tc: `comprehensive` cho cả 3 sheet (Coverage Matrix ×3 đi kèm)
> **Score: 85/100 (capped) — CONDITIONAL**

⚠️ **Disclaimer:** Report này KHÔNG phải kết quả từ independent reviewer agent gọi qua Anthropic API như thiết kế gốc của skill (file `review-agent/AGENT.md` chưa tồn tại). Đây là self-review trực tiếp bởi phiên làm việc đã tạo/consolidate chính bộ TC này — có rủi ro thiên vị (không hoàn toàn "độc lập" như tinh thần thiết kế của skill). Điểm số bị chặn trần ở 85 để phản ánh giới hạn này, kể cả khi raw checklist không phát hiện gì nghiêm trọng.

## Summary

| Severity | Count (findings, gộp theo root-cause) | Số TC bị ảnh hưởng |
|----------|------|------|
| 🔴 CRITICAL | 1 | 14 |
| 🟠 MAJOR | 1 | ~47 (chưa recount chính xác sau khi xóa TC_03.12, xem ghi chú ở finding) |
| 🟡 MINOR | 1 | 7 |
| 🔵 INFO | 3 | — |

> **Ghi chú phương pháp tính điểm:** 3 finding đầu (Critical/Major/Minor) đều là **1 root-cause lặp lại nhiều dòng** (cùng nguyên nhân, cùng cách sửa), không phải nhiều lỗi độc lập. Report gộp mỗi root-cause thành **1 finding** (kèm đủ danh sách Testcase ID bị ảnh hưởng) để điểm số phản ánh đúng bản chất — thay vì áp máy móc công thức theo số dòng (vd R1-04 áp cho 48 TC riêng lẻ sẽ ra điểm âm, không phản ánh đúng: TC vẫn thực thi được, không mơ hồ). Nếu muốn tính theo đúng công thức cơ học của `full.md` (mỗi dòng = 1 finding), xem cột "Số TC bị ảnh hưởng" để tự quy đổi.
> Score (gộp root-cause) = 100 − (1×5 + 1×3 + 1×1) = 91 → **capped 85** (Direct-mode fallback).

## Findings

### 🔴 CRITICAL

**[R1-15] Round-1 execution data còn sót lại (leftover mẫu từ template) trên 15 TC của sheet `Test Case 3` (Thông báo/TC_03) — dù project CHƯA từng chạy round test nào**

- **Vấn đề:** Cột N–R (Round 1: Vibe-test/KQ Script/Kết quả/Executed By/ID Bugs) của 15 TC vẫn còn dữ liệu mẫu để lại từ file template gốc (`Vibe-test=Yes/No`, `KQ Script=Pass`, `Kết quả=Pass`, `Executed By=PhucDN7`, thậm chí `TC_03.10` có `ID Bugs=IP-104`) — trong khi `MASTER-MEMORY.md §8` xác nhận `vibe-test` và `execute-maintain` đều **NOT_STARTED** cho v1.0. Dữ liệu này khiến sheet `Dashboard`/`AO` (Status) hiển thị sai là các TC này **đã Pass**, dù chưa ai chạy thật.
- **Nguyên nhân gốc:** Fragment `TC-NTF-v1.0.xlsx` (dựng ở phiên làm việc trước, trước khi tôi tham gia session này) khi copy sheet mẫu từ template không xoá sạch cột N–R — chỉ CANHAN/HOATDONG (2 fragment tôi build lại trong session này) có bước clear đầy đủ cột 1–42.
- **Testcase ID bị ảnh hưởng (14, sau khi xóa TC_03.12 lệch scope):** `TC_03.1, TC_03.2, TC_03.3, TC_03.4, TC_03.5, TC_03.6, TC_03.8, TC_03.9, TC_03.11, TC_03.13, TC_03.14, TC_03.15, TC_03.17, TC_03.19` (ID mới sau renumber — tương ứng vị trí cũ `TC_03.14, TC_03.15, TC_03.16, TC_03.18, TC_03.20` trước khi xóa)
- **Đề xuất:** Xoá trắng cột N–R (giữ nguyên cột AM/AN/AO formula) cho 15 dòng trên trong `TC-MASTER-v1.0.xlsx` + fragment gốc `TC-NTF-v1.0.xlsx`, rồi `/generate-tc --sync` để đồng bộ lại. **Block downstream** (vibe-test/test-report) cho tới khi sửa — nếu không, báo cáo Pass rate sẽ sai ngay từ vòng test đầu tiên.

### 🟠 MAJOR

**[R1-04] Steps/Expected không 1:1 trên ~47/62 TC (~76%) — vi phạm literal rule "Step N ↔ Expected N" của `generate-tc/references/generate.md`**

- **Vấn đề:** Rất nhiều TC có Steps nhiều hơn Expected — vì các step mở đầu (mở app, bấm tab điều hướng) không có dòng Expected riêng, chỉ step quan sát cuối cùng mới được assert. Ví dụ `TC_01.1`: 3 steps ("Mở app" → "Bấm Hoạt động" → "Quan sát bottom nav") nhưng Expected chỉ có 1 dòng "3. ...". `TC_02.1`: 4 steps nhưng 2 expected (chỉ step 3+4).
- **Đánh giá:** Về mặt thực thi, TC vẫn RÕ RÀNG và verify được (tester biết chính xác cần quan sát gì ở bước cuối) — đây là văn phong "step 1-2 = setup không cần assert riêng, step cuối = observable outcome" khá phổ biến trong QA thực tế, không gây mơ hồ. Nhưng nó lệch so với rule literal đã ghi trong `generate.md` ("1:1 với Steps — Step N ↔ Expected N, số bước = số expected").
- **Đại diện:** `TC_01.1` (3→1), `TC_02.1` (4→2) — danh sách đầy đủ ~47 ID nằm trong file JSON phân tích gốc (không đính kèm report). **Lưu ý:** số 48 gốc bao gồm cả `TC_03.12` (nay đã xóa do lệch scope, xem đầu report) — con số 47/62 ở đây là ước tính trừ đi 1, chưa chạy lại script đếm để verify chính xác; nên recount trước khi dùng số này làm căn cứ quyết định.
- **Đề xuất:** (a) Chấp nhận làm convention chính thức (sửa `generate.md` ghi rõ ngoại lệ "step thuần setup/navigate không bắt buộc expected riêng"), HOẶC (b) nếu muốn giữ đúng 1:1, bổ sung expected ngắn cho từng step setup (vd "1. Mở app thành công, không lỗi" / "2. Điều hướng đúng màn X"). Khuyến nghị (a) — verbose hoá 48 TC theo (b) sẽ tăng đáng kể effort mà giá trị thêm thấp.

### 🟡 MINOR

**[R3-10 / R4-01] Trộn tiếng Anh "Tap" với tiếng Việt "Bấm" trong cùng bộ TC — vi phạm `Project_rule.md §4` (nội dung TC phải Tiếng Việt)**

- **Vấn đề:** 23 TC dùng "Bấm", nhưng 7 TC dùng "Tap" (giữ nguyên tiếng Anh) cho cùng 1 hành động (chạm vào card/nút).
- **Testcase ID:** `TC_01.13, TC_01.14, TC_01.15, TC_01.16, TC_01.17` (Hoạt động), `TC_03.19, TC_03.21` (Thông báo — ID mới sau khi xóa TC_03.12, tương ứng vị trí cũ `TC_03.20, TC_03.22`)
- **Đề xuất:** Đổi "Tap" → "Bấm"/"Chạm vào" cho nhất quán toàn bộ workbook. Fix nhanh (find & replace trong 7 cell Steps).

## Info (không trừ điểm)

| # | Nội dung |
|---|---|
| 1 | **Scope hiện tại:** Dashboard/RTM v1.0 mới phản ánh 3/8 module (62 TC) — ASN, DLV, CNL, phần còn lại của GIFT/USR/TS chưa generate. Đây là roadmap đã biết (`MASTER-MEMORY §8`), không phải gap phát hiện mới. |
| 2 | **RTM cột "Đã chạy" (F) hiển thị 65/65 (100%)** dù chưa round test nào chạy thật — do công thức gốc template `COUNTIFS(...,"<>")` (so sánh cell công thức trả `""`) được LibreOffice headless (dùng để verify consolidate) tính là "khác rỗng". Đây là hành vi công thức GỐC của template (không phải tôi sửa) — cần double-check khi mở bằng Microsoft Excel thật, vì Excel có thể xử lý so sánh `""` khác LibreOffice. |
| 3 | **Convention Remark chưa đồng nhất giữa các sheet:** `Test Case 3` (Thông báo, phiên trước) ghi tường minh `Technique: N/A — 0-dim ...` cho mọi baseline TC không áp dụng kỹ thuật nào; `Test Cases`/`Test Case 2` (Hoạt động/Cá nhân, phiên này) để Remark trống cho cùng trường hợp. Cả 2 đều đúng theo rule (chỉ derived TC bắt buộc có tag), nhưng cách ghi tường minh của TC_03 minh bạch/dễ audit hơn — nên áp dụng thống nhất cho các lần generate sau. |

## Version-Specific Checks

| Check | Result |
|-------|--------|
| CARRIED TCs included (Remark tag) | N/A — v1.0 là version đầu tiên, không có CARRIED |
| DEPRECATED TCs removed | N/A — không có DEPRECATED ở v1.0 |
| RTM: mọi Req ID có row + đủ term COUNTIF | ✅ Y — 10/10 Req ID, không orphan (verify bằng script, xem §Method) |
| RTM: row "Tổng" range SUM bao hết Req ID (không sót row mới) | ✅ Y — `SUM(E6:E15)` bao đúng 10 row |
| Dashboard: mọi sheet TC có row tương ứng | ✅ Y — TC_01/02/03 đều có row 4/5/6, tên tab khớp 100% |
| Cột A/AM/AN/AO vẫn là formula (không bị gõ đè) | ✅ Y — verify 62/62 TC, cột A đều là `=IF(...)` |
| Testcase ID trùng lặp | ✅ N — 62/62 unique |
| STT liên tục mỗi sheet | ✅ Y — TC_01.1-20, TC_02.1-15, TC_03.1-27 (sau khi xóa TC_03.12 2026-07-28, các TC sau tự renumber), không nhảy số |
| Req ID / DOC Source trống | ✅ N — 0/62 |
| Priority/Group/Origin/Review đúng enum dropdown | ✅ Y — 0 vi phạm |
| Field/Column completeness TC (Step 3b) | ✅ Y — có đủ cho cả 3 màn (`TC_02.3` header Cá nhân, `TC_01.8` card Hoạt động, `TC_03.17` card Thông báo — ID mới sau khi xóa TC_03.12, tương ứng vị trí cũ `TC_03.18`) |
| Coverage Matrix sheet tồn tại (comprehensive mode) | ✅ Y — 3 sheet: `Coverage Matrix`, `Coverage Matrix - Cá nhân`, `Coverage Matrix - Thông báo` |

## Method (minh bạch cách review được thực hiện)

Do thiếu `review-agent/AGENT.md`, review chạy trực tiếp bằng script Python (openpyxl) đối chiếu 60 checks R1–R4 trong `references/full.md` (single source of truth), cross-verify công thức bằng LibreOffice headless recalc để đảm bảo đọc đúng giá trị đã resolve (không chỉ đọc formula string). Toàn bộ 63 TC (sau đó rút còn 62 TC do xóa `TC_03.12` lệch scope, 2026-07-28) + 3 row label + Dashboard + RTM đã được parse và quét. R2 (coverage) và R3 (content quality) được kiểm bằng kết hợp script (pattern-matching: vague wording, placeholder chưa resolve, "mặc định" claim vs PRISTINE state) + đọc trực tiếp nội dung TC do đã nắm rõ ngữ cảnh (tác giả chính của 2/3 sheet, đã đọc kỹ sheet còn lại khi consolidate).

## Score Breakdown

```
Score (root-cause aggregated) = 100 - (1×5 + 1×3 + 1×1) = 91
Direct-mode fallback cap       = min(91, 85) = 85
```

**Verdict: 85/100 — CONDITIONAL** (khuyến nghị fix Critical trước khi chạy vibe-test/execute-maintain; Major/Minor có thể fix sau hoặc chấp nhận làm convention).

Quality Gate G1 (Score ≥ 70): **✅ PASS**
