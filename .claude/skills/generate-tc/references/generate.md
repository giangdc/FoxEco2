# Generate TC — Mode GENERATE

> `/generate-tc` | `/generate-tc --module Dashboard --version v2.0 --priority P1`

## Input

```
1. CLAUDE.md
2. 02_analyze-requirements/Project_rule.md           → naming rules, template source path (nếu override default)
3. 02_analyze-requirements/MASTER-MEMORY.md          → active version, regression scope
4. 02_analyze-requirements/[version]/MEMORY.md       → scenarios, doc registry
5. 02_analyze-requirements/[version]/test_scenario_map.md
6. 02_analyze-requirements/[version]/test_data_catalog.md
7. 02_analyze-requirements/[version]/risk_assessment.md
8. 03_test-cases/_template/ISC_Template_SDLC_TestCase_Report_Version.xlsx  → template gốc QA ban hành (xem Step 0)
```

## Output

```
03_test-cases/v[X]/fragments/TC-[MODULE]-v[X].xlsx
```

## Step 0: Đảm bảo có template gốc (chạy 1 lần, mọi mode)

Toàn bộ output Excel của skill này PHẢI dựa trên template QA ban hành — KHÔNG tự dựng sheet/cột từ đầu.

```
1. Check 03_test-cases/_template/ISC_Template_SDLC_TestCase_Report_Version.xlsx tồn tại?
   - Có → dùng luôn.
   - Không → copy từ đường dẫn cấu hình trong Project_rule.md (key `tc-template-path`),
     mặc định /home/giangdc2/AI/Template/ISC_Template_SDLC_TestCase_Report_Version.xlsx
     → 03_test-cases/_template/ (giữ nguyên tên file).
   - Cả 2 đều không có → DỪNG, báo user cần cung cấp template.
2. KHÔNG sửa file trong _template/ — đây là bản gốc read-only, mọi generate/consolidate đọc từ đây rồi copy ra working file.
```

## Workflow

### Step 1: Đọc context + guard

```
1. PIPELINE.md → check analyze-requirements §8 ≥ COMPLETED
2. MASTER-MEMORY → active version, regression scope §4
3. Version MEMORY → scenarios §4, doc registry §2
4. Ghi §8 generate-tc = IN_PROGRESS
```

Trình bày scope cho user:
```
📋 Version: v2.0 (active)
Scenarios available:
  - NEW: 12 scenarios (chưa có TC)
  - MODIFIED: 3 scenarios (TC cũ cần regenerate)
  - CARRIED: 15 scenarios (đã có TC từ v1.0)

Bạn muốn:
  (a) TC cho NEW + MODIFIED (15 TCs mới)
  (b) Tất cả + include CARRIED vào TC-MASTER (regression)
  (c) Chỉ module cụ thể
  (d) Chỉ priority High (P1)
```

### Step 2: Tạo folder structure

```bash
mkdir -p 03_test-cases/v[X]/fragments/
mkdir -p 03_test-cases/v[X]/functional/
```

### Step 3: Generate Test Cases

#### Mapping: Scenario → TC(s)

| Scenario Test Type | TC cần tạo |
|-------------------|------------|
| Functional (positive) | 1 TC happy path |
| Negative | 1 TC cho mỗi invalid case |
| Boundary | 1 TC cho mỗi boundary value |
| UI | 1 TC layout/display |
| Integration | 1 TC luồng liên kết |
| **Field/Column/Dropdown-Option List (≥2 trường/cột/option được requirement liệt kê cho 1 màn hình/khu vực/dropdown)** | **1 TC riêng "completeness check"** — xem Step 3b, BẮT BUỘC dù ở mode nào (standard/comprehensive/selective) |

#### Step 3b: Field/Column/Dropdown-Option Completeness Check — BẮT BUỘC, mọi mode (standard included)

> **Vì sao có rule này:** case thật #1 (PROMO v1.3, VR-008 2026-07-10) — requirement liệt kê 8 cột cho bảng danh sách (STT, Gói bán, Kênh bán, SKU, **Loại gói**, Thời gian/Người cập nhật, Thời gian/Người tạo, icon), nhưng generate-tc chỉ sinh 2 SC/TC hẹp cho 2 cột cụ thể (định dạng datetime, placeholder SKU rỗng) — không TC nào verify **tổng thể đủ cột**. Kết quả: UI thiếu hẳn cột "Loại gói" nhưng không TC nào từng bắt được, mãi đến khi user tự soi mới phát hiện.
> **Case thật #2 (CMS v1.4, LDP, 2026-07-22)** — cùng lớp gap nhưng ở **dropdown option list** thay vì cột bảng: REQ-LDP-029 mô tả dropdown "Tất cả template" (Block "Bộ lọc & Tìm kiếm"), SC-LDP-061 chỉ test hành vi "chọn 1 template → lọc đúng danh sách" — không SC/TC nào verify dropdown có đủ + đúng cả 5 loại template (định nghĩa ở REQ-LDP-018..022, TÁCH RIÊNG khỏi REQ mô tả dropdown, nên khó grep ra bằng cách đọc 1 đoạn văn). Phát hiện được TRƯỚC khi generate-tc chạy (qua review thủ công), nhưng rule cần được viết ra để không phải dựa vào may mắn lần sau. Đã bổ sung song song ở `analyze-requirements/references/init.md` §Dropdown/Enum option-list completeness (root fix ở tầng SC) — rule ở đây là **lưới an toàn tầng TC**, phòng khi 1 dropdown lọt qua bước phân tích.
> Rule này tồn tại để KHÔNG lặp lại 2 gap đó, dù bị lọt ở tầng SC hay tầng TC.

**Trigger (áp dụng bất kỳ khi nào xuất hiện, không chỉ bảng):** Source Quote hoặc Analyst Note trong Version MEMORY liệt kê **≥2 trường/cột/field/option hiển thị** cho 1 màn hình hoặc 1 khu vực UI cụ thể — ví dụ:
- Cột bảng danh sách (list/table columns)
- Field trên form Tạo mới/Chỉnh sửa
- Field trên summary card / mirror block / dashboard widget
- Field hiển thị trên 1 dialog/popup xác nhận
- **Danh sách giá trị/option trong 1 dropdown/select/filter — enum cố định, nhiều option đặt tên cụ thể (không phải free-text)**, kể cả khi các option đó được định nghĩa ở 1 REQ/SC KHÁC với REQ/SC mô tả bản thân dropdown (vd enum Template/Trạng thái/Vai trò tái sử dụng làm filter ở màn khác) — case #2 ở trên là ví dụ; nếu chỉ thấy SC test "chọn giá trị → hành vi" mà không thấy SC nào test "dropdown hiển thị đủ/đúng option", đây chính là gap cần vá.

**Hành động bắt buộc:** Với MỖI nhóm field/cột/option được liệt kê như vậy, sinh **1 TC riêng** (KHÔNG gộp/chìm vào TC hẹp test hành vi 1 field/option cụ thể):

| Cột (theo template ISC) | Nội dung |
|-----|----------|
| Group (D) | `UI` |
| Priority (E) | `Medium` (mặc định, trừ khi risk_assessment ghi cao hơn) |
| Test Title (F) | `Check đầy đủ + đúng [N] trường/cột/option hiển thị tại [tên màn hình/khu vực/dropdown]` |
| Test Steps (H) | Liệt kê rõ tên từng field/cột/option theo ĐÚNG tên + ĐÚNG thứ tự lấy verbatim từ Source Quote/Analyst Note (không diễn giải lại); với dropdown: bước đầu phải là "Mở [màn hình] MỚI/SẠCH (chưa chọn/thao tác gì)" trước khi mở dropdown quan sát (verify pristine state, xem Quy tắc viết Expected bên dưới) |
| Expected Result (I) | Liệt kê đủ N field/cột/option, đúng tên, đúng thứ tự (nếu requirement có quy định thứ tự); mỗi field/cột init hiển thị giá trị hợp lý (không rỗng bất thường, không lỗi render); với dropdown: nêu rõ option mặc định là gì |
| Remark (AP) | `Field/column/dropdown-option completeness check — auto-derived (xem generate.md Step 3b)` |

**Checklist tự-audit khi generate xong 1 module** (chạy trước khi báo hoàn thành, áp dụng CẢ standard mode):
1. Grep Version MEMORY của module đó cho các cụm chỉ dấu liệt kê field/cột/option: "Cột bảng", "cột:", "field:", "trường hiển thị", "dropdown", "select", "combo box", "danh sách lựa chọn", danh sách đánh số STT trong 1 Source Quote (`"12 |", "13 |"...`).
2. Với mỗi nhóm tìm được, xác nhận có ≥1 TC Group=UI riêng test đúng đủ danh sách đó — nếu KHÔNG có, tự sinh thêm TC theo template trên trước khi coi module là generate xong.
3. Với mỗi Scenario dạng "chọn dropdown X → hành vi Y": tra xem enum giá trị của dropdown X có được định nghĩa ở REQ/SC khác trong CÙNG module không (không chỉ đọc đoạn văn ngay cạnh Scenario đó) — nếu có và chưa có TC completeness riêng cho dropdown X, tự sinh thêm.
4. Không tự ý bỏ qua field/option vì "đã có TC test hành vi riêng của field/option đó" — TC hành vi riêng (vd "cột SKU hiện — khi rỗng", "chọn template A → lọc đúng") KHÔNG thay thế được TC completeness (vd "bảng có đủ 9 cột X/Y/Z...", "dropdown có đủ 5 template + option mặc định").

#### Step 3a: Test Design Techniques (CHỈ khi `--mode comprehensive` hoặc `--techniques <list>` active)

> **⚠️ COMPREHENSIVE MODE CONTRACT — đọc TRƯỚC khi generate. Đây là hợp đồng BẮT BUỘC, không phải gợi ý:**
> - Với **MỖI** scenario: apply **MỌI** technique rubric đánh `applicable` — KHÔNG bỏ bớt cho gọn.
> - Output = baseline 1-1 TC **+** derived TC từ techniques. Expansion điển hình **3-5×** (floor định lượng: xem Step 6).
> - Sheet `Coverage Matrix` **BẮT BUỘC**; mỗi derived TC có `Technique: <tag>` ở Remark column (xem lưu ý cuối Step 3a).
> - Chỉ được hạ 1 scenario về 1-1 khi: rubric phát hiện **thật sự 0 dimension** (log `N/A — 0-dim`) **HOẶC** user **chủ động** skip (log `user-skipped`). Mọi trường hợp khác mà output ít hơn rubric estimate = **VI PHẠM** → Checklist gate cuối file sẽ chặn.

**Skip Step 3a nếu no-flag invocation** — preserve backward-compat (Standard mode = current 1-1 behavior).

Khi flag active, per scenario chạy rubric:

1. Load `references/technique-rubric.md` — heuristic table.
2. Scan scenario Given/When/Then + Source Quote (nếu Part 2 verbatim quoting enabled trong analyze-requirements).
3. Detect 4 dimensions: #inputs / #states / #conditions / #parameters.
4. Output applicable techniques list (subset của B1-B8).
5. Present rubric to user (interactive confirm):
   ```
   🔍 Rubric for SC-XXX-NNN:
     Applicable: B1 EP (3 partitions) · B2 BVA (range field) · B6 EG (per input × 10 patterns)
     Estimated: ~25 TCs
     Proceed? (y/n/edit)
   ```
   **Non-interactive (batch / không có user để confirm):** KHÔNG chờ vô hạn và KHÔNG hạ về standard — auto-apply TẤT CẢ technique applicable theo rubric; log tập đã auto-apply (Coverage Matrix + Remark `Technique: <tag> (auto)`); nêu summary cuối cho review sau.
6. After user confirm (hoặc auto-apply ở chế độ non-interactive), load `references/techniques.md` cho applicable techniques only.
7. Per technique, follow Procedure → expand to N TCs.
8. Per derived TC, set Remark column (AP) = `Technique: <tag>` (per technique convention trong `techniques.md`).

> **Remark column dùng chung với execution.** Cột Remark (AP) cũng là nơi vibe-test/execute-maintain/log-bug ghi chú kết quả round sau này. generate-tc chỉ được **ghi mới** vào ô đang trống lúc tạo TC — downstream skills khi cập nhật Remark PHẢI nối thêm (` | Technique: ...` giữ nguyên, thêm remark mới phía sau) chứ không được ghi đè xoá mất tag kỹ thuật. Đây là điểm cần các skill downstream (vibe-test, execute-maintain, log-bug) tôn trọng khi được cập nhật theo template mới — flag lại nếu phát hiện bị ghi đè.

**TC ID không tự đặt tay.** Cột Testcase ID (A) là formula của template (`=IF(C[row]="","",$C$2&"."&COUNTA($C$7:C[row])&"")`) — tự sinh `[Mã chức năng].[STT]` (vd `TC_01.1`, `TC_01.2`...) dựa theo thứ tự row và cột DOC Source (C) không rỗng. generate-tc (kể cả derived TC từ technique) chỉ cần đảm bảo:
- Mỗi TC (kể cả derived) có 1 row riêng, viết đủ cột C (DOC Source) để formula nhận diện là row có TC.
- Copy formula của cột A xuống row mới (xem Step 6) — KHÔNG gõ tay chuỗi ID.
- Thứ tự row quyết định STT — không chèn row ở giữa làm xáo trộn ID của TC đã tồn tại (đặc biệt khi REGENERATE/SYNC — xem `regenerate.md`/`sync.md`).

**Standard mode + Comprehensive mode interaction:** Standard mapping (above table) chạy FIRST → produces baseline TCs. Step 3a thêm derived TCs sau, không thay thế. Final TC count = baseline + derived.

#### TC Structure — 42 cột theo template ISC (`Test Cases` sheet, header row 6, data từ row 7)

generate-tc **chỉ ghi giá trị vào cột B–M (2–13)**. Cột A và cột 39/40/41 (AM/AN/AO) là formula của template — copy-down, không gõ tay. Cột 14–38 (N–AL, 5 block Round) và cột 42 (AP Remark, trừ trường hợp Step 3a/3b nêu trên) để TRỐNG — thuộc phạm vi execution (vibe-test/execute-maintain/implement-automation/log-bug), không phải generate-tc.

| Col | Field | Ai ghi | Nội dung |
|-----|-------|--------|----------|
| A | Testcase ID | **Formula (copy-down)** | `[Mã chức năng].[STT]` — tự sinh, xem trên |
| B | Req ID | generate-tc | `REQ-[NN]` — 1 hoặc nhiều, phân cách dấu phẩy (vd `REQ-02, REQ-03`) |
| C | DOC Source | generate-tc | `DOC-v[X]-[NN]` — **bắt buộc không rỗng**, formula cột A dựa vào cột này để đếm STT |
| D | Group | generate-tc | `Functional` / `UI` / `Integration` / `Database Test Case` (đúng 4 giá trị dropdown template — lưu ý giá trị thật là `Database Test Case`, không phải `Database`) |
| E | Priority | generate-tc | `High` / `Medium` / `Low` (Guideline sheet hiển thị kèm nhãn P1/P2/P3 nhưng giá trị cell CHỈ là chữ, không có hậu tố) |
| F | Test Title | generate-tc | Tiếng Việt, bắt đầu bằng `"Check ..."` (quy định Guideline sheet mục 3) |
| G | Pre-condition | generate-tc | Điều kiện trước test. KHÔNG ghi login/navigate (thuộc Steps) |
| H | Test Steps | generate-tc | Tiếng Việt, đánh số, cụ thể actionable — **test data ghi thẳng giá trị cụ thể trong step** (template KHÔNG có cột Test Data riêng) |
| I | Expected Result | generate-tc | Tiếng Việt, đánh số 1:1 với Steps, verifiable |
| J | Origin | generate-tc | `AI` (TC do generate-tc sinh) / `QC` (TC viết tay, giữ nguyên khi import) |
| K | Review | generate-tc | Ghi `Pending` khi mới tạo (review-tc sẽ đổi thành `Reviewed`/`N/A` sau) |
| L | Automated | generate-tc | `No` mặc định khi mới tạo (implement-automation đổi thành `Yes` + điền cột M sau) |
| M | Script | generate-tc | Để trống (implement-automation điền path sau) |
| N–R | Round 1 (Vibe-test/KQ Script/Kết quả/Executed By/ID Bugs) | *execution skills* | Để trống |
| S–W | Round 2 | *execution skills* | Để trống |
| X–AB | Round 3 | *execution skills* | Để trống |
| AC–AG | Round 4 | *execution skills* | Để trống |
| AH–AL | Round 5 | *execution skills* | Để trống |
| AM | Vibe-test (tổng) | **Formula (copy-down)** | Auto-rollup ≥1 round Yes |
| AN | KQ Script (tổng) | **Formula (copy-down)** | Auto = round mới nhất có giá trị |
| AO | Status | **Formula (copy-down)** | Auto = round mới nhất có giá trị — KHÔNG BAO GIỜ gõ tay |
| AP | Remark | generate-tc (có điều kiện) | Chỉ ghi khi: (a) Step 3a technique tag, (b) Step 3b completeness tag, (c) test data thiếu trong catalog → `Cần bổ sung test data trong catalog`, (d) TC carried từ version cha → `Carried từ v[X]`. Nhiều lý do cùng lúc → nối bằng ` \| `. Nếu không thuộc case nào → để trống |

> **Đã bỏ so với schema 16-cột cũ:** không còn Scenario ID riêng (traceability qua Req ID + DOC ID; SC↔TC mapping vẫn lưu ở Version MEMORY §9), không còn Test Data/Version Origin/Lifecycle/Assigned To/Notes as cột riêng — nội dung tương đương dồn vào Steps (test data), Remark (ghi chú/carried tag), và Version MEMORY (lifecycle NEW/CARRIED/MODIFIED — xem Step 8).

#### Meta header mỗi sheet (row 2–4) — ghi 1 lần khi tạo sheet mới cho module

| Cell | Nội dung | Ai ghi |
|------|----------|--------|
| C2 | Mã chức năng (vd `TC_01`) | generate-tc — **sequential**: quét cột C (Mã CN) hiện có ở sheet `Dashboard` (row 4–33), lấy số lớn nhất + 1 |
| C3 | Tên chức năng (tên module/màn hình, tiếng Việt) | generate-tc |
| I3 | Version | **Formula, giữ nguyên** (`=Summary!$C$8`) — không ghi đè |
| C4 | Execution (khoảng ngày test) | **Formula, giữ nguyên** (`=TEXT(Summary!$C$10,...)...`) — không ghi đè |
| I4 | PIC | Để trống khi generate — QC lead điền tay sau (email) |

Row 6 (header cột) là cố định của template — **không sửa**.

#### Quy tắc viết Steps

- **Cụ thể, actionable** — tester đọc là làm được, không cần suy luận
- **TỐT:** "Nhập 'user@' vào field Email"
- **XẤU:** "Nhập email sai format"
- Đánh số: 1, 2, 3...
- **Test data ghi thẳng giá trị cụ thể trong step** — template không có cột Test Data riêng, giá trị lấy từ `test_data_catalog.md` (KHÔNG tự bịa). Nếu catalog thiếu, dùng placeholder rõ ràng trong step (vd "nhập [TBD: giá trị hợp lệ tối đa]") và ghi Remark: `Cần bổ sung test data trong catalog`.
- CARRIED scenarios → test data reference data catalog parent version

#### Quy tắc viết Expected

- **Verifiable** — criteria cụ thể biết pass/fail
- **TỐT:** "Hiển thị text 'Email không hợp lệ' màu đỏ bên dưới field Email"
- **XẤU:** "Hiển thị thông báo lỗi"
- **1:1 với Steps** — Step N ↔ Expected N (số bước = số expected)
- Mô tả: thông báo hiển thị, trạng thái UI, hành vi hệ thống
- **Claim "mặc định"/"default"/"init" PHẢI kèm Step yêu cầu verify trên state PRISTINE (màn/field vừa mở, CHƯA từng thao tác).** KHÔNG được viết Step cho phép verify qua 1 record/data đã tồn tại từ trước (record đó có thể đã bị user khác chọn giá trị thủ công, không chứng minh được default thật). Case study (PROMO v1.3, VR-008 2026-07-10): SC-PROMO-032 claim "Gói tính cước mặc định Trả trước" từng bị PASS sai vì tester chỉ mở 1 record ĐÃ LƯU và thấy có giá trị "Trả trước" — không phải vì đó là default, mà vì người tạo record đã chủ động chọn. Khi verify lại đúng cách (đọc `value`/`selectedIndex` của field NGAY KHI mở form, chưa click gì), giá trị thật là rỗng. → Step cho mọi TC test "default/mặc định" phải ghi rõ: "Mở [màn hình] MỚI/SẠCH (chưa chọn/nhập gì) → quan sát field [X]" — không được thay bằng "mở 1 record đã có sẵn".

### Step 4: Coverage checklist

Kiểm tra đã cover các areas:

| Area | Kiểm tra |
|------|---------|
| UI / Layout | Hiển thị đúng elements, responsive |
| **Field/Column/Dropdown-Option completeness** | **BẮT BUỘC (xem Step 3b):** mọi danh sách ≥2 field/cột mà requirement liệt kê (bảng, form, card, dialog) HOẶC ≥2 option cụ thể trong 1 dropdown/select đều có ít nhất 1 TC riêng verify ĐỦ + ĐÚNG toàn bộ danh sách — không chỉ hành vi hẹp của từng field/option (vd "chọn option A → lọc đúng" KHÔNG thay thế "dropdown đủ N option") |
| Dropdown | Load options, select, default value — **và** đủ/đúng toàn bộ danh sách option (completeness, xem Step 3b) khi option là enum cố định |
| Permission | Các role khác nhau thấy gì |
| Field data load | Data tự điền từ DB/API |
| Date / Time | Format, timezone, range |
| Button show/hide | Enable/disable theo conditions |
| Pagination | Chuyển trang, items per page |
| Search / Filter | Tìm kiếm, filter, reset |

### Step 5: Tối ưu + gộp TC

Gộp TCs có thể test cùng lúc (steps liên tiếp, không ảnh hưởng lẫn nhau).
Bỏ TC duplicate hoặc quá giống.

### Step 6: Xuất file Excel (.xlsx)

**Đọc skill xlsx trước:** `view /mnt/skills/public/xlsx/SKILL.md`

Output: `03_test-cases/v[X]/fragments/TC-[MODULE]-v[X].xlsx`

**Cách tạo fragment (dựa trên template, KHÔNG tự dựng sheet):**

```
1. Mở 03_test-cases/_template/ISC_Template_SDLC_TestCase_Report_Version.xlsx (Step 0)
2. Copy sheet "Test Cases" (giữ nguyên toàn bộ formatting/data validation/conditional formatting/
   merged cells của template) → đây là sheet duy nhất của file fragment.
3. Ghi meta header: C2 (Mã chức năng), C3 (Tên chức năng) — KHÔNG đụng I3/C4 (formula) trong fragment
   riêng lẻ; nếu fragment chưa có sheet Summary, tạm để I3/C4 as-is (giá trị thật sẽ đúng khi
   consolidate copy sheet này vào workbook có Summary — xem consolidate.md).
4. Sắp xếp thứ tự TC theo Screen/Block (nguồn: "Block Definitions" + cột Screen/Block ở bảng
   Scenarios trong `test_scenario_map.md` — xem `analyze-requirements/references/init.md`
   §Xác định Screen/Block):
   - Nhóm TC theo Screen trước, giữ đúng thứ tự Screen xuất hiện trong Block Definitions. Trong mỗi
     Screen, TC không thuộc Block nào (cột Block để trống/`—`) xếp TRƯỚC mọi Block con (khớp ví dụ
     thật của template QA), sau đó mới đến từng Block theo thứ tự khai báo.
   - Trước TC đầu tiên của 1 Screen mới: chèn 1 row label — merge **A:I**, text = đúng tên Screen
     (verbatim, không thêm tiền tố), fill nền `FF729FCF`, font bold. Các cột khác của row để trống.
   - Trước TC đầu tiên của 1 Block mới (trong cùng Screen): chèn 1 row label — merge **B:I**,
     text = `"Block " + tên block` (verbatim tên block), fill nền `FFAFD095`, font KHÔNG bold.
   - Row label để trống cột C (DOC Source) → formula cột A (COUNTA theo cột C) tự bỏ qua, không ảnh
     hưởng STT của các TC.
5. Với mỗi TC (viết vào row hiện tại, sau khi đã chèn đủ row label theo bước 4):
   a. Ghi giá trị cột B–M.
   b. Copy formula cột A/AM/AN/AO từ row mẫu (row 7 của template gốc), dịch số row tương ứng
      (dùng openpyxl.formula.translate.Translator hoặc thay thế số row thủ công trong chuỗi formula).
   c. Formula/data-validation của cột N–AP tại row đó GIỮ NGUYÊN như template (đã có sẵn theo dropdown
      list — không cần set lại).
6. KHÔNG ghi gì vào cột N–AL. Cột AP chỉ ghi theo điều kiện ở bảng 42-cột phía trên.
7. Xoá các sheet khác của template gốc (Cover/Guideline/.../Bug Data) khỏi file fragment — fragment
   chỉ cần 1 sheet TC, các sheet workbook-level chỉ tồn tại ở TC-MASTER sau khi consolidate.
```

**Formatting:** không tự set — toàn bộ style/conditional-formatting/data-validation đã có sẵn trong sheet template được copy nguyên. Chỉ ghi giá trị cell, không ghi đè style.

**Coverage Matrix (nếu comprehensive/selective mode):** thêm 1 sheet phụ `Coverage Matrix` vào fragment (schema: `~/.claude/skills/generate-tc/assets/coverage-matrix-template.md`) — sheet này KHÔNG thuộc bộ sheet chuẩn ISC, chỉ là phụ lục kỹ thuật nội bộ, giữ nguyên khi consolidate. Chỉ generate khi `--mode comprehensive` hoặc `--techniques` flag active.

**Comprehensive/Selective — TC count floor (kiểm TRƯỚC khi coi là xong):**
- Mỗi scenario: số TC thực tế ≥ tổng `Estimated TC` của các technique applicable (rubric item 5).
- Tổng thực tế < ~80% rubric estimate mà KHÔNG có lý do được log (`user-skipped` / `N/A 0-dim` / dedupe-exact) → **FAIL** → KHÔNG kết thúc; quay lại Step 3a apply cho đủ (Compliance gate bên dưới chặn).

### Step 7: Hỏi consolidate

```
✅ TC created: 03_test-cases/v2.0/fragments/TC-DASHBOARD-v2.0.xlsx (12 TCs)

Bạn muốn:
  (a) Gộp vào TC-MASTER luôn (auto SYNC) → /generate-tc --sync
  (b) Giữ trong fragments/, sync sau
  (c) Generate thêm module khác trước rồi consolidate 1 lần
```

### Step 8: Cập nhật MEMORY + CHANGELOG

**Version MEMORY §4 (Scenario Index):**
TC Status: `⏳ Chưa tạo TC` → `✅ Đã tạo TC`
Blocked scenarios → `🚫 Blocked`
Lifecycle (NEW/CARRIED/MODIFIED) ghi ở đây — template Excel không còn cột này, MEMORY §4 là nguồn duy nhất cho lifecycle tracking.

**Version MEMORY §9 (TC Gen Log) — 8 cột canonical (PHẢI khớp `version-memory-template.md`): `DOC ID | Ngày generate | Tổng TC | File output | Priority | Mode | Techniques | Review Status`:**
```
| DOC-v2.0-01 | 2026-04-15 | 12 | fragments/TC-DASHBOARD-v2.0.xlsx | High:5, Medium:4, Low:3 | standard | N/A | ⏳ |
| DOC-v2.0-02 | 2026-04-16 | 35 | fragments/TC-AUTH-v2.0.xlsx | High:25, Medium:8, Low:2 | comprehensive | B1, B2, B6 | ⏳ |
```

Priority column: breakdown High/Medium/Low (khớp đúng giá trị cell, không dùng hậu tố P1/P2/P3). Mode column: `standard` (default) / `comprehensive` / `selective`. Techniques column: `N/A` cho standard mode; comma-separated B-IDs cho comprehensive/selective (e.g., `B1, B2, B6`). Review Status column: ghi `⏳` khi tạo; review-tc cập nhật (✅/score) sau — generate-tc KHÔNG bỏ cột này.

**CHANGELOG.md trong 03_test-cases/v[X]/:**
```
| [date] | GENERATE | Dashboard | 12 TCs | TC-DASHBOARD-v2.0.xlsx |
```

Ghi §8 = PARTIAL (chưa consolidate).

## Checklist

- [ ] Mỗi TC có Req ID + DOC ID (traceability) — cột B, C không rỗng
- [ ] Steps cụ thể, actionable, test data inline (không có cột Test Data riêng)
- [ ] Expected verifiable, 1:1 với Steps
- [ ] TC ID KHÔNG gõ tay — cột A là formula copy-down đúng từ template
- [ ] Excel dựa trên sheet "Test Cases" copy từ `03_test-cases/_template/` — đúng 42 cột, chỉ ghi B–M (+ AP có điều kiện)
- [ ] Group/Priority/Origin/Review/Automated đúng enum dropdown template (đặc biệt `Database Test Case`, không phải `Database`)
- [ ] Coverage checklist passed (9 areas — bao gồm Field/Column/Dropdown-Option completeness)
- [ ] **Field/Column/Dropdown-Option completeness (Step 3b, BẮT BUỘC mọi mode):** đã grep Version MEMORY tìm mọi nhóm ≥2 field/cột/option được liệt kê cho 1 màn hình hoặc 1 dropdown, và mỗi nhóm có ≥1 TC Group=UI riêng verify đủ danh sách — không dựa vào TC hành vi hẹp của từng field/option (kể cả khi option list của dropdown định nghĩa ở REQ khác)
- [ ] MEMORY §4 + §9 cập nhật (§9 với Mode + Techniques cols, Priority breakdown dùng High/Medium/Low)
- [ ] §8 = PARTIAL

### Compliance gate — Comprehensive/Selective mode (BẮT BUỘC, blocking)

> Chạy gate này TRƯỚC khi báo hoàn thành. **Bất kỳ mục nào FAIL → KHÔNG báo done; sửa rồi verify lại.** KHÔNG được âm thầm hạ về standard.

- [ ] **Per-scenario coverage:** với mỗi scenario, MỌI technique rubric đánh `applicable` đều đã sinh TC — hoặc được log rõ `user-skipped` / `N/A 0-dim`. Không technique applicable nào bị bỏ im lặng.
- [ ] **TC count floor:** tổng TC thực tế ≥ ~80% rubric estimate (Step 6 floor). Thiếu mà không có lý do log → FAIL.
- [ ] **Coverage Matrix điền đủ:** sheet tồn tại VÀ mọi scenario có row, mọi cell technique applicable được đánh (✅/❌/N/A) — không chỉ "có sheet rỗng".
- [ ] **Technique tag:** mọi derived TC có `Technique: <tag>` ở Remark column (rubric/interactive) hoặc `(auto)` (non-interactive).
- [ ] **§9 TC Gen Log:** Mode = `comprehensive`/`selective` + cột Techniques liệt kê đúng B-IDs đã apply.
