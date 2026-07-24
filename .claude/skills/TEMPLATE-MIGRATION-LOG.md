# Log cập nhật pipeline theo template ISC mới

> **Bối cảnh:** QA ban hành template mới `ISC_Template_SDLC_TestCase_Report_Version.xlsx`
> (nguồn: `/home/giangdc2/AI/Template/`) — 42 cột A-AP, multi-round (R1-R5), 8 sheet chuẩn
> (Cover/Guideline/Revision History/Summary/Dashboard/Report Test/Bug Data/RTM) + N sheet
> Test Cases/module. Khác hoàn toàn schema cũ (16 cột, Overview/ALL/per-module).
>
> Ngày thực hiện: 2026-07-21. Trạng thái: 8/8 skill có tương tác trực tiếp với TC-MASTER Excel
> đã migrate xong + đã verify chéo. Còn 2 việc tồn đọng (xem cuối file).

## Thứ tự cập nhật (theo mức rủi ro giảm dần)

| # | Skill | Lý do rủi ro | Trạng thái |
|---|---|---|---|
| 1 | `generate-tc` | Gốc sinh ra schema — mọi skill khác phụ thuộc | ✅ Done |
| 2 | `review-tc` | Parse trực tiếp TC-MASTER theo vị trí cột | ✅ Done (đã migrate sẵn khi kiểm tra tới) |
| 3 | `implement-automation` | Hardcode cột I/J/K/F cũ → sinh code SAI nếu không sửa | ✅ Done |
| 4 | `review-src-tc` | Hardcode cột I/J/K/M/P cũ → so sánh SAI, báo Critical giả | ✅ Done |
| 5 | `health-check` | Check cột O/N cũ (Lifecycle/Version Origin) — cột không còn tồn tại | ✅ Done |
| 6 | `log-bug` | Chưa từng ghi Excel — Bug Data sheet trống, Report Test KPI luôn = 0 | ✅ Done |
| 7 | `vibe-test` | Chưa từng ghi Excel — cột Vibe-test/Kết quả round luôn trống | ✅ Done |
| 8 | `test-report` | Rủi ro thấp nhất, tự parse thay vì đọc Dashboard/RTM/Report Test có sẵn | ✅ Done |

## Chi tiết từng skill

### 1. generate-tc
- Schema 16→42 cột, ID đổi từ `TC-[MODULE]-[NNN]` (tự đặt) → `[Mã CN].[STT]` (formula tự sinh, KHÔNG gõ tay).
- Sheet model: bỏ Overview/ALL/per-module → 1 sheet/module + 8 sheet workbook-level cố định.
- File naming chuẩn QA: `ISC_[Project]_[Version]_TC_[TCVersion]_R[Round].xlsx`, vẫn xuất kèm alias
  `TC-MASTER-v[X].xlsx`/`TC-MASTER-LATEST.xlsx` cho downstream skill chưa migrate.
- Không còn Scenario ID/Test Data/Version Origin/Lifecycle/Assigned To/Notes riêng — dồn vào
  Steps (data inline), Remark (ghi chú/technique tag/carried tag), Version MEMORY (lifecycle).
- RTM formula hard-code tên sheet (không INDIRECT) → phải tự nối thêm term mỗi khi thêm module.
- Phát hiện khi double-check: formula cột A thiếu `&""` so với bản gốc, row "Tổng" RTM có range cố
  định không tự mở rộng khi thêm Req ID — đã sửa cả 2.

### 2. review-tc
- Đã tự migrate đầy đủ trước khi tôi kiểm tra tới (không rõ do đâu, không phải tôi làm) — verify kỹ
  và xác nhận khớp 100% với generate-tc.

### 3. implement-automation
- Bug nghiêm trọng nhất tìm được: bảng "Quy tắc bắt buộc" lấy Step từ cột I (thực ra là Expected),
  Expected từ cột J (thực ra là Origin AI/QC), test data từ cột K (thực ra là Review status) — sẽ
  sinh code với assertion/data SAI hoàn toàn nếu không sửa. Đã sửa về đúng H/I, bỏ cột K (test data
  giờ inline trong Steps).
- Thêm năng lực mới: ghi ngược cột Automated/Script sau khi implement xong (cột này có sẵn trong
  template nhưng skill cũ chưa từng dùng).
- Bỏ yêu cầu bắt buộc "SC ID" trong `@Test description`/test name → thay bằng Req ID.

### 4. review-src-tc
- Cùng loại lỗi cột như implement-automation (M3-01 so hardcoded data với cột K = Review status).
- `--member` filter gãy hoàn toàn vì cột "Assigned To" bị xoá khỏi template — thêm fallback dùng
  `git log --format='%an'` (tác giả commit).

### 5. health-check
- C-06/C-07 trước đây so sánh cột O (Lifecycle)/N (Version Origin) — 2 cột này giờ là KQ Script/
  Vibe-test của Round 1, hoàn toàn khác nghĩa. Thiết kế lại dựa trên tag `Carried từ v[X]` ở Remark.
- C-02 (TC orphan) đổi từ so SC ID → so Req ID qua RTM.

### 6. log-bug
- Thêm đồng bộ 2 chiều với sheet `Bug Data` (file mới `references/sync-excel.md`).
- Đổi nhãn severity `High`→`Major` khớp đúng dropdown Bug Data (mã hoá `Critical=20/Major=10/
  Medium=5/Low=2`).
- Thêm field mới: `platform`, `defect`, `effect`, `round_found`, `round_closed`, `rework_number`,
  `wont_fix_reason` (danh mục đọc động từ cột Y Bug Data, không hardcode).
- Thêm bước ghi ngược `jira_key` vào cột "ID Bugs" của sheet Test Cases sau khi push-jira thành công
  (phát hiện thiếu bước này khi verify chéo với vibe-test — đã bổ sung).

### 7. vibe-test
- Gap lớn nhất đã sửa: giờ ghi trực tiếp cột Vibe-test=Yes/Kết quả/Executed By/ID Bugs vào đúng round
  (1-5) trong TC-MASTER, thay vì chỉ ghi Version MEMORY §4 (giờ MEMORY chỉ là cache).
- Round tự xác định: round đầu tiên còn trống cho từng TC row (không đồng bộ toàn run trừ khi
  `--round N`). Retest mặc định ghi đè round gần nhất, `--new-round` mới mở round mới.
- Không đụng cột KQ Script (dành riêng cho execute-maintain — xem mục "Tồn đọng" bên dưới).

### 8. test-report
- Chuyển từ tự parse row Excel → đọc KPI có sẵn ở `Dashboard`/`RTM`/`Report Test` (coverage, pass
  rate, automation, bug KPI... đều đã có formula tính sẵn).
- Làm rõ 2 khái niệm dễ nhầm: Bug Priority (P1-3, Jira, không đổi) vs Bug Severity (Critical/Major/
  Medium/Low, đổi nhãn theo Bug Data sheet).

## Verify chéo (theo yêu cầu "kiểm tra lại lần nữa") — lỗi tìm thấy & đã sửa

1. `review-agent/AGENT.md` (system prompt dùng chung review-tc + review-src-tc): mô tả field còn nhắc
   "test data, SC ID" đã bị bỏ; đếm sai "R1-R4 (52 checks)" trong khi thực tế 60 (17+17+15+11) — lỗi
   này **có từ trước, không phải do lần cập nhật này** nhưng tiện sửa luôn.
2. vibe-test hứa log-bug sẽ cập nhật ID Bugs → jira_key nhưng log-bug chưa từng code việc này (2 skill
   không khớp nhau) — đã bổ sung vào log-bug.
3. Lỗi chính tả: test-report viết "N-A" thay vì "N/A" đúng theo header thật của Dashboard.

## Tồn đọng — CHƯA sửa, cần quyết định tiếp

| Việc | Ảnh hưởng | Ghi chú |
|---|---|---|
| **`execute-maintain`** chưa ghi cột "KQ Script" mỗi round | Không hỏng (skill này chưa từng đụng Excel), nhưng Dashboard/Report Test sẽ luôn thiếu số liệu automation vì cột này chỉ dành cho execute-maintain ghi | Cần thêm bước ghi Excel tương tự vibe-test |
| **`init-project`** scaffold 2 file mẫu còn schema cũ | Không làm skill nào chạy sai (không ai đọc lại 2 file này), nhưng gây hiểu nhầm cho dự án mới | `references/templates.md`: mẫu `template-bug-report.md` (severity "High" cũ) + mẫu `TC-001-template.md` (schema 16-cột cũ) |

## Danh sách file đã sửa (tham khảo nhanh)

```
generate-tc/SKILL.md, references/{generate,consolidate,sync,regenerate,direct,review,techniques,technique-rubric}.md, assets/coverage-matrix-template.md
review-tc/SKILL.md, references/{full,module,recheck}.md   (đã ở trạng thái migrated khi kiểm tra tới)
implement-automation/SKILL.md, references/{implement,implement-typescript,update}.md
review-src-tc/SKILL.md, references/{full,full-typescript,scope}.md
health-check/SKILL.md
log-bug/SKILL.md, references/{log,update,close,push-jira}.md, references/sync-excel.md (mới)
vibe-test/SKILL.md, references/{execute,retest,status}.md
test-report/SKILL.md, references/{release,sprint,adhoc,cross-version}.md
review-agent/AGENT.md
```

---

# Phần 2 — Phân rã Block/Screen trong TC (2026-07-21 → 2026-07-22)

> **Bối cảnh:** User phản ánh (2026-07-21): gen TC không group theo cụm màn hình/chức năng → review
> khó (không biết TC đã đủ/đúng rule chưa theo từng khu vực UI). Giải pháp chọn (scope "Đầy đủ"): thêm
> **Screen/Block** làm dimension tường minh ngay từ bước phân tích, generate-tc dùng lại để group TC
> khi xuất Excel bằng row label chèn thẳng vào sheet (không dùng Excel Group/Outline — xem lý do trong
> mục "Xác nhận từ ví dụ thật" bên dưới).
>
> **Ngày hoàn tất:** 2026-07-22. **Trạng thái:** ✅ Toàn bộ scope "Đầy đủ" đã xong + đã audit chéo
> 15 skill, vá xong 3 skill có rủi ro false-positive/ghi đè dữ liệu khi dùng Block. Chưa phát hiện tồn
> đọng chặn pipeline nào (xem "Verify chéo" bên dưới).

## Xác nhận từ ví dụ thật (template Excel QA cập nhật 2026-07-22)

QA thêm ví dụ minh hoạ vào sheet `Test Cases` của `ISC_Template_SDLC_TestCase_Report_Version_2207.xlsx`
(dòng 7-31). Quy ước thực tế xác nhận qua ví dụ:
- **Screen** = 1 row label merge **A:I**, fill `FF729FCF` (xanh dương), bold, text = tên màn hình
  verbatim (không tiền tố "Screen:").
- **Block** = 1 row label merge **B:I** (lùi 1 cột), fill `FFAFD095` (xanh lá), không bold, text =
  `"Block " + tên block`.
- TC có thể nằm NGAY dưới Screen mà KHÔNG cần Block riêng (case phổ biến, không phải ngoại lệ) — đã
  sửa lại giả định sai ban đầu ("Cross-block" tự bịa, không có trong ví dụ thật) trong
  `scenario-map-template.md`.
- Không outline/group Excel (row_dimensions outline level = 0 ở mọi row) — xác nhận đây là row label
  chèn thẳng vào bảng, không phải tính năng Group/Outline.

## Thứ tự cập nhật

| # | File | Thay đổi | Trạng thái |
|---|---|---|---|
| 1 | `analyze-requirements/assets/scenario-map-template.md` | Thêm section "Block Definitions" (Module→Screen→Block→Field/Rule table), cột Screen/Block ở bảng Scenarios, sửa lại chú thích Block-trống (screen-level TC là case bình thường, không phải "Cross-block") | ✅ Done |
| 2 | `analyze-requirements/references/init.md` | Thêm bước "Xác định Screen/Block" vào Step 3 (trước khi derive Scenario), rule tên Screen/Block phải khớp verbatim ở Step 4, checklist item | ✅ Done |
| 3 | `analyze-requirements/references/update.md` | Thêm 1 dòng feedback-type "Thêm/đổi Block cho màn hình X" vào bảng xử lý feedback | ✅ Done |
| 4 | `generate-tc/references/generate.md` | Step 6: sắp xếp TC theo Screen/Block + chèn row label đúng style ví dụ thật (merge cell, fill màu, không bold cho Block) | ✅ Done |
| 5 | `generate-tc/references/consolidate.md` | Copy row label (không chỉ cột B–M) khi tạo sheet module mới; CARRIED TC chèn đúng nhóm Screen/Block thay vì append cuối sheet | ✅ Done |
| 6 | `generate-tc/references/sync.md` | REPLACE xoá/ghi lại theo row (cả label lẫn TC) — tránh xoá nhầm text Block đang nằm ở cột B nếu chỉ xoá theo cột | ✅ Done |
| 7 | `generate-tc/references/regenerate.md` | TC mới chèn đúng nhóm Screen/Block thay vì append cuối sheet (cùng lỗi gốc như #6) | ✅ Done |

## Verify chéo — audit toàn bộ 15 skill đọc/ghi sheet Test Cases (2026-07-22)

Sau khi 7 file trên xong, quét lại **tất cả** skill còn lại (không chỉ generate-tc) xem có bị vỡ bởi
row label mới không — vì review-tc/health-check/vibe-test/log-bug/implement-automation/review-src-tc/
test-report/execute-maintain đều được migrate template ISC hôm 21/07 nhưng KHÔNG biết về row label
(tính năng ra đời sau, 22/07).

**Xác nhận VỠ — đã vá:**

| Skill | Lỗi gốc | Hậu quả nếu không vá | Vá xong |
|---|---|---|---|
| `review-tc/references/full.md` | Văn bản "Row 7+: data, 1 row = 1 TC" sai từ khi có row label; R1-05/06/08/09/10/11/12 chạy trên mọi row không phân biệt label | False Critical/Major tràn ngập report mỗi khi project dùng Block — score bị tính sai | ✅ |
| `health-check/SKILL.md` | C-02 đọc cột B mọi row coi là Req ID — Block label có text ở cột B (vd "Block Thông tin filter") không phải Req ID thật | False C-02 CRITICAL "TC orphan" lặp lại mỗi lần chạy | ✅ |
| `vibe-test/references/execute.md` | Step 1 parse TC list không filter row label | Rủi ro "execute" row label như 1 TC (steps rỗng) hoặc ghi đè round data lên ô đang giữ text label | ✅ |

**Xác nhận AN TOÀN — không cần sửa:**

| Skill | Vì sao an toàn |
|---|---|
| `implement-automation`, `review-src-tc` | Key theo cột A (Testcase ID, formula-resolved) — row label có cột A rỗng (do cột C rỗng) nên tự động bị loại, đúng thiết kế sẵn có |
| `log-bug` | Ghi sheet `Bug Data` riêng (không đụng Test Cases rows); ghi ID Bugs theo TC ID cụ thể (keyed lookup, không duyệt toàn bộ row) |
| `test-report` | Chỉ đọc KPI formula có sẵn ở Dashboard/RTM/Report Test, không tự duyệt row Test Cases |
| `vibe-test/references/retest.md`, `references/status.md` | `retest.md` chỉ re-parse TC đã biết chắc là thật (từ vibe-log, đã qua filter của `execute.md`); `status.md` chỉ đọc/hiển thị, không ghi — rủi ro không đáng kể, không sửa |
| `execute-maintain` | Chưa từng ghi Excel (tồn đọng cũ từ Phần 1) — chưa có nguy cơ hiện tại, nhưng PHẢI áp dụng cùng guard (lọc row label theo cột A rỗng) khi implement bước ghi cột KQ Script sau này |

## Tồn đọng — chưa cần xử lý ngay

| Việc | Ghi chú |
|---|---|
| `execute-maintain` ghi cột "KQ Script" | Kế thừa từ Phần 1 (chưa implement) — khi làm, PHẢI thêm guard lọc row label giống `vibe-test/execute.md` |
| `init-project` scaffold 2 file mẫu schema cũ | Kế thừa từ Phần 1, chưa quyết định có cần sửa không |

## Danh sách file đã sửa (Phần 2)

```
analyze-requirements/assets/scenario-map-template.md
analyze-requirements/references/init.md
analyze-requirements/references/update.md
generate-tc/references/generate.md
generate-tc/references/consolidate.md
generate-tc/references/sync.md
generate-tc/references/regenerate.md
review-tc/references/full.md
health-check/SKILL.md
vibe-test/references/execute.md
```
