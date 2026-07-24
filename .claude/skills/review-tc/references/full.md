# Review TC — Mode FULL

> `/review-tc` | `/review-tc --version v2.0`

## Workflow

### Step 1: Đọc context + guard
1. PIPELINE.md → check generate-tc ≥ PARTIAL
2. MASTER-MEMORY §8 → kiểm tra generate-tc status
3. Version MEMORY, scenario_map, data_catalog, risk_assessment
4. Ghi §8 review-tc = IN_PROGRESS

### Step 2: Parse TC-MASTER (openpyxl) — template ISC

TC-MASTER giờ là file build từ template QA chính thức (`03_test-cases/_template/ISC_Template_SDLC_TestCase_Report_Version.xlsx` — xem `generate-tc/references/consolidate.md`). File chính thức: `ISC_[Project]_[Version]_TC_[TCVersion]_R[Round].xlsx`; generate-tc luôn xuất kèm alias `TC-MASTER-v[X].xlsx` / `TC-MASTER-LATEST.xlsx` trỏ tới cùng nội dung — review-tc đọc alias này.

```python
import openpyxl
wb = openpyxl.load_workbook('03_test-cases/v[X]/TC-MASTER-v[X].xlsx', data_only=True)
wb_formulas = openpyxl.load_workbook('03_test-cases/v[X]/TC-MASTER-v[X].xlsx', data_only=False)  # để check formula bị gõ đè
```

**Sheet map (workbook-level, cố định):** `Cover`, `Guideline`, `Revision History`, `Summary`, `Dashboard`, `Report Test`, `Bug Data`, `RTM`. Mọi sheet còn lại (tên `Test Cases`, `Test Case 2`, `Test Case 3`...) là **1 module/function riêng** — trừ `Coverage Matrix` (và `Coverage Matrix - [Module]`), đó là phụ lục kỹ thuật của comprehensive/selective mode, không phải sheet TC.

**Mỗi sheet TC, header cố định:**
- Row 2–4: meta header — `C2` Mã chức năng (vd `TC_01`), `C3` Tên chức năng, `I3` Version (formula), `C4` Execution (formula), `I4` PIC
- Row 6: header 42 cột (cố định, không sửa)
- Row 7+: **1 row = 1 TC, XEN KẼ với row label Screen/Block** (chèn theo `generate-tc/references/generate.md`
  Step 6.4 khi scenario_map có Block Definitions — Screen: merge A:I, fill `FF729FCF`, bold; Block: merge
  B:I, fill `FFAFD095`, không bold). **Row label KHÔNG phải TC** — nhận diện bằng cột A (Testcase ID,
  giá trị đã resolve `data_only=True`) RỖNG (vì công thức `IF(C="","",...)` trả rỗng khi cột C trống —
  row label luôn để trống cột C). **BẮT BUỘC lọc bỏ mọi row có cột A rỗng khỏi tập TC TRƯỚC khi đếm
  hoặc chạy bất kỳ check R1-R4 nào** — không được coi row label là TC thiếu dữ liệu (DOC Source/Req
  ID/Title/Steps/Expected trống là bình thường ở row label, không phải lỗi).

**42 cột (A–AP):**

| Col | Field | Ghi chú parse |
|-----|-------|---------------|
| A | Testcase ID | Formula copy-down `[Mã CN].[STT]` — đọc value đã resolve (data_only=True) VÀ formula gốc (data_only=False) để đối chiếu |
| B | Req ID | Có thể nhiều giá trị, phân cách dấu phẩy |
| C | DOC Source | Formula cột A dựa vào cột này để đếm STT — trống = phá numbering |
| D | Group | Dropdown: `Functional` / `UI` / `Integration` / `Database Test Case` |
| E | Priority | Dropdown: `High` / `Medium` / `Low` (không hậu tố P1/P2/P3 trong cell) |
| F | Test Title | Quy định bắt đầu bằng `"Check ..."` (Guideline mục 3) |
| G | Pre-condition | |
| H | Test Steps | Test data ghi thẳng giá trị cụ thể — template KHÔNG có cột Test Data riêng |
| I | Expected Result | 1:1 với Steps |
| J | Origin | `AI` / `QC` |
| K | Review | `Pending` / `Reviewed` / `N/A` |
| L | Automated | `Yes` / `No` |
| M | Script | Path automation script (nếu Automated=Yes) |
| N–R | Round 1 (Vibe-test/KQ Script/Kết quả/Executed By/ID Bugs) | Execution scope — để trống ở TC vừa tạo, chưa qua round nào |
| S–W | Round 2 | nt |
| X–AB | Round 3 | nt |
| AC–AG | Round 4 | nt |
| AH–AL | Round 5 | nt |
| AM | Vibe-test (tổng) | Formula copy-down — auto-rollup ≥1 round Yes |
| AN | KQ Script (tổng) | Formula copy-down — auto = round mới nhất có giá trị |
| AO | Status | Formula copy-down — auto = round mới nhất có giá trị. KHÔNG BAO GIỜ gõ tay |
| AP | Remark | generate-tc ghi có điều kiện: `Technique: <tag>` (derived TC), field/column completeness tag, `Cần bổ sung test data trong catalog`, `Carried từ v[X]`. Downstream skills PHẢI nối thêm (` \| `), không ghi đè |

> **Đã bỏ so với schema 16-cột cũ:** không còn cột Test Data, Version Origin, Lifecycle, Notes riêng. Test data → inline trong Steps. Lifecycle (NEW/CARRIED/MODIFIED) → chỉ sống trong Version MEMORY §4. Ghi chú/technique tag/carried tag → dồn vào Remark (AP).

Đếm: total TCs, per module (per sheet/Mã CN), per Priority (High/Medium/Low), per Group.

### Step 3: Determine review mode (agent vs direct)

```
pipeline_status['generate-tc'] in ['COMPLETED', 'PARTIAL']?
  → CÓ + no --direct flag → Agent mode (call Anthropic API)
  → KHÔNG hoặc --direct → Direct mode (self-review + disclaimer)
```

Agent: xem `review-agent/AGENT.md` §3a cho system prompt (persona + format).
**Checks R1-R4 bên dưới là SINGLE SOURCE OF TRUTH** — gửi cho agent qua payload, KHÔNG duplicate.

### Step 4: Run R1-R4 checks ★ SINGLE SOURCE — cả direct mode và agent mode đều dùng checks này

**R1: Structural Integrity (17 checks)**

| Check | Severity | Logic |
|-------|----------|-------|
| R1-01 | Critical | Testcase ID (cột A) bị gõ giá trị tĩnh thay vì để formula `=IF(C[row]="","",$C$2&"."&COUNTA($C$7:C[row])&"")` copy-down → phá auto-numbering khi thêm/xoá row sau này |
| R1-02 | Critical | 2+ rows Testcase ID trùng giá trị (sau khi resolve) — dấu hiệu formula bị phá hoặc row bị duplicate |
| R1-03 | Major | Testcase ID nhảy số trong 1 sheet (STT không liên tục) — thường do DOC Source (C) trống ở 1 row khiến COUNTA bỏ qua |
| R1-04 | Critical | Steps/Expected count mismatch → step N nhưng expected chỉ đến N-1 (hoặc ngược lại) |
| R1-05 | Critical | Req ID (B) hoặc DOC Source (C) trống — DOC Source trống nghiêm trọng hơn vì phá cả numbering cột A (chỉ áp dụng cho row đã xác định LÀ TC theo guard ở Step 2 — row label Screen/Block không tính) |
| R1-06 | Minor | Title (F) trống, <10 ký tự, hoặc không bắt đầu bằng `"Check "` (Guideline mục 3) |
| R1-07 | Minor | Precondition (G) trống (chấp nhận được với 1 số TCs) |
| R1-08 | Major | Steps (H) trống |
| R1-09 | Major | Expected (I) trống |
| R1-10 | Major | Priority (E) trống hoặc không đúng 1 trong 3 giá trị `High`/`Medium`/`Low` |
| R1-11 | Major | Group (D) trống hoặc không đúng 1 trong 4 giá trị dropdown — lưu ý giá trị đúng là `Database Test Case`, KHÔNG phải `Database` (lỗi hay gặp) |
| R1-12 | Major | Origin (J) trống hoặc không phải `AI`/`QC` |
| R1-13 | Minor | Review (K) trống hoặc không phải `Pending`/`Reviewed`/`N/A` |
| R1-14 | Minor | Automated (L)/Script (M) inconsistent → Automated=`Yes` nhưng Script trống, hoặc Automated=`No` nhưng Script có giá trị |
| R1-15 | Critical | Round data (N–AL, bất kỳ block nào trong 5 round) không trống ở TC được xác nhận CHƯA qua execution (chưa có `/vibe-test` hoặc `/execute-maintain` nào chạy cho version này) → dấu hiệu copy nhầm kết quả round cũ khi CARRIED, vi phạm quy tắc round data phải để trống cho version mới (`generate-tc/references/consolidate.md` Step 2) |
| R1-16 | Minor | Meta header thiếu — `C2` (Mã chức năng) hoặc `C3` (Tên chức năng) trống ở đầu sheet TC |
| R1-17 | Minor | **(mode-aware)** Khi Version MEMORY §9 Mode = `comprehensive` HOẶC `selective`: Remark (AP) phải chứa `Technique: <B[1-8]>-<subtype>` cho derived TCs (per `~/.claude/skills/generate-tc/references/techniques.md`). Remark trống ở derived TC = Minor. Mode = `standard` hoặc trống → skip check này |

**R2: Coverage Completeness (17 checks)**

| Check | Severity | Logic |
|-------|----------|-------|
| R2-01 | Critical | NEW scenario chưa có TC → SC ID trong MEMORY §4 (NEW) nhưng 0 TCs |
| R2-02 | Critical | MODIFIED scenario chưa có TC → cần regenerate |
| R2-03 | Major | Module thiếu negative TC → chỉ có positive (happy path) |
| R2-04 | Major | Module thiếu boundary TC → field có range nhưng 0 boundary TCs |
| R2-05 | Minor | Module thiếu UI TC → có Figma/wireframe nhưng 0 UI TCs |
| R2-06 | Info | Blocked scenario → clarification chưa resolve |
| R2-07 | Info | Low priority scenarios skipped → Low (P3) chưa có TC |
| R2-08 | Major | Happy path missing → module có scenarios nhưng 0 positive TC |
| R2-09 | Info | Coverage % < 80% cho 1 module — lấy từ sheet `RTM` cột `% phủ` |
| R2-10 | Info | Total coverage % — lấy từ row `Tổng` sheet `RTM` |
| R2-11 | Major | CARRIED TC thiếu → regression scope yêu cầu (MASTER-MEMORY §4) nhưng không có TC nào ghi `Carried từ v[PARENT]` trong Remark (AP) |
| R2-12 | Minor | DEPRECATED scenario (MEMORY §4) vẫn còn TC trong sheet — should be removed/marked |
| R2-13 | Minor | **(mode-aware)** TC-MASTER thiếu sheet `Coverage Matrix` khi Mode = `comprehensive`/`selective`. Fix: re-run `/generate-tc --consolidate` |
| R2-14 | Info | **(mode-aware)** Technique distribution suspicious (1 technique chiếm >70% TC count → rubric có thể bị over-apply) |
| R2-15 | Major | Field/Column/Dropdown-Option completeness gap: Version MEMORY (Source Quote/Analyst Note) liệt kê ≥2 trường/cột hiển thị cho 1 màn hình (bảng/form/card/dialog), HOẶC ≥2 option cụ thể trong 1 dropdown/select (enum cố định) — kể cả khi option list đó định nghĩa ở REQ/SC khác với REQ mô tả hành vi dùng dropdown — nhưng TC-MASTER KHÔNG có TC Group=UI nào verify đủ + đúng toàn bộ danh sách đó (chỉ có TC test hành vi hẹp, vd "chọn option → lọc đúng"). Per generate-tc Step 3b (bắt buộc mọi mode; case study dropdown: CMS v1.4 LDP SC-LDP-061, 2026-07-22). Fix: bổ sung TC "Check đầy đủ [N] trường/cột/option hiển thị tại [màn hình/dropdown]" rồi `/generate-tc --sync` |
| R2-16 | Critical | Req ID xuất hiện trong 1 sheet TC nhưng KHÔNG có row tương ứng trong sheet `RTM`, hoặc formula RTM (cột E–H) của Req ID đó thiếu term `COUNTIF` cho sheet hiện tại, HOẶC Req ID đó nằm ngoài range `SUM(...)` của row "Tổng" cuối RTM (range cố định, không tự mở rộng khi thêm row — xem `generate-tc/references/consolidate.md` Step 3.2d) → orphan traceability, RTM báo sai coverage. Fix: `/generate-tc --consolidate` lại |
| R2-17 | Major | Sheet TC không có row tương ứng trong sheet `Dashboard`, hoặc `Dashboard` cột D (tên tab) không khớp 100% tên sheet thật → formula tổng hợp của Dashboard/RTM tính thiếu module này |

**R3: Content Quality (15 checks)**

| Check | Severity | Logic |
|-------|----------|-------|
| R3-01 | Major | Step vague → "Nhập email sai" thay vì "Nhập 'user@' vào field Email" |
| R3-02 | Major | Expected non-verifiable → "Hiển thị lỗi" thay vì "Hiển thị text 'Email không hợp lệ'" |
| R3-03 | Major | Step reference data (vd "nhập email hợp lệ") nhưng KHÔNG ghi giá trị cụ thể ngay trong Step — template không có cột Test Data riêng nên giá trị bắt buộc phải inline |
| R3-04 | Minor | Giá trị test data trong Steps không khớp `test_data_catalog.md` |
| R3-05 | Minor | Title quá generic → "Test login" thay vì "Check đăng nhập với email sai format", hoặc không bắt đầu bằng "Check" |
| R3-06 | Minor | Step chứa nhiều actions → 1 step = 1 action |
| R3-07 | Info | Expected chứa nhiều verifications → 1 expected = 1 check |
| R3-08 | Minor | Precondition trùng Steps → login/navigate nên trong Steps |
| R3-09 | Major | Step reference element không rõ → "click button" (button nào?) |
| R3-10 | Minor | Ngôn ngữ inconsistent → Guideline yêu cầu tiếng Việt, TC mix Anh/Việt trong cùng sheet |
| R3-11 | Info | Step quá dài → >200 chars, nên tách |
| R3-12 | Minor | Expected không có giá trị cụ thể → "hiển thị đúng" thay vì "hiển thị '5 items'" |
| R3-13 | Info | **(Part 2 verbatim quoting awareness)** Khi scenario_map.md có Source Detail blocks (Source Quote + Source Location + Analyst Note per scenario): verify TC Steps + Expected reasonably derived từ Source Quote text. Drift = Info finding. Legacy versions không có Source Detail blocks → skip |
| R3-14 | Major | TC có Test Title/Expected chứa "mặc định"/"default"/"init" nhưng Steps lại verify qua 1 record/data ĐÃ TỒN TẠI từ trước thay vì "Mở màn/form MỚI, chưa thao tác gì". Per `generate-tc/references/generate.md` (Quy tắc viết Expected). Case study: SC-PROMO-032 (PROMO v1.3, VR-008, 2026-07-10 — xem BUG-005) |
| R3-15 | Minor | Step chứa placeholder chưa resolve (vd `[TBD: giá trị hợp lệ tối đa]`) mà Remark (AP) không ghi `Cần bổ sung test data trong catalog` — thiếu traceability lý do placeholder |

**R4: Cross-TC Consistency (11 checks)**

| Check | Severity | Logic |
|-------|----------|-------|
| R4-01 | Minor | Terminology inconsistent → TC_01.1 gọi "Đăng nhập", TC_01.2 gọi "Login" |
| R4-02 | Major | Priority mismatch → happy path = Low, edge case = High |
| R4-03 | Minor | Precondition inconsistent → cùng precondition nhưng viết khác nhau |
| R4-04 | Info | Data reuse → nhiều TCs dùng cùng test data |
| R4-05 | Minor | Step ordering inconsistent → TC_01.1 login → navigate, TC_01.2 navigate → login |
| R4-06 | Info | Duplicate TC → 2 TCs test cùng scenario cùng cách |
| R4-07 | Minor | DOC Source inconsistent → cùng feature nhưng khác DOC ID |
| R4-08 | Minor | Module grouping sai → TC nằm trong sheet của module X nhưng Steps/Expected mô tả feature của module khác (không khớp Tên chức năng ở C3) |
| R4-09 | Minor | CARRIED TC (Remark có `Carried từ v[X]`) nhưng round data (N–AL) KHÔNG trống → vi phạm quy tắc phải để trống, bắt buộc retest ở version mới |
| R4-10 | Major | Remark `Carried từ v[X]` không khớp Version MEMORY §4 — MEMORY ghi NEW/MODIFIED cho scenario nhưng Excel có tag Carried, hoặc MEMORY ghi CARRIED nhưng không TC nào có tag tương ứng |
| R4-11 | Major | Status (AO) bị gõ giá trị tĩnh thay vì formula copy-down → có nguy cơ hiển thị sai kết quả round mới nhất, vi phạm nguyên tắc "KHÔNG BAO GIỜ gõ tay" |

### Step 5: Scoring

```
Score = 100 - (Critical × 5 + Major × 3 + Minor × 1)
```

Info findings KHÔNG trừ điểm — informational only, dùng cho recommendations section.

| Score | Verdict |
|-------|---------|
| 90-100 | APPROVED |
| 70-89 | CONDITIONAL (fix recommended) |
| 50-69 | NEEDS REWORK |
| 0-49 | REJECTED |

Quality Gate G1: Score ≥ 70 → PASS.

**Mode-aware checks:**

| Mode (read from MEMORY §9) | Checks enforced |
|---|---|
| `standard` hoặc trống | skip R1-17, R2-13, R2-14 |
| `comprehensive` / `selective` | R1-17 + R2-13 + R2-14 enforced |
| Có Source Detail blocks (Part 2 enabled) | R3-13 enforced (TC drift vs Source Quote) |

Backward-compat: review report của TC-MASTER schema 16-cột cũ (trước khi migrate sang template ISC) dùng bộ check ID cũ — KHÔNG map ngược 1-1 sang bộ ID mới này. Khi recheck 1 TC-MASTER đã migrate, luôn dùng bộ checks trong file này.

### Step 6: Generate review report

**Output:** `11_tc-review/review-report-v[X].md`

```markdown
# TC Review Report — v[X]

> Generated: [datetime]
> Mode: Agent / Direct
> TC-MASTER: [file path] (ISC: [ISC_Project_Version_TC_...xlsx])
> Score: [score]/100 — [APPROVED / CONDITIONAL / NEEDS REWORK / REJECTED]

## Summary
| Severity | Count |
|----------|-------|
| 🔴 CRITICAL | [N] |
| 🟠 MAJOR | [N] |
| 🟡 MINOR | [N] |
| 🔵 INFO | [N] |

## Findings

### 🔴 CRITICAL
(per finding: check_id, Testcase ID, sheet/module, field, issue, suggestion)

### 🟠 MAJOR
...

### 🟡 MINOR
...

## Version-Specific Checks
| Check | Result |
|-------|--------|
| CARRIED TCs included (Remark tag) | [N]/[expected] |
| DEPRECATED TCs removed | [Y/N] |
| RTM: mọi Req ID có row + đủ term COUNTIF | [Y/N] |
| RTM: row "Tổng" range SUM bao hết Req ID (không sót row mới) | [Y/N] |
| Dashboard: mọi sheet TC có row tương ứng | [Y/N] |
| Cột A/AM/AN/AO vẫn là formula (không bị gõ đè) | [Y/N] |

## Score Breakdown
Score = 100 - (CRITICAL×5 + MAJOR×3 + MINOR×1) = [score]
Quality Gate G1: [PASS / FAIL]
```

### Step 7: Update MEMORY

- Version MEMORY §9 (TC Gen Log): cột `Review Status` → `✅ [score]/100` (hoặc `❌` nếu REJECTED)
- MASTER-MEMORY §6: TC Files Registry → review status
- §8 = COMPLETED

## Checklist
- [ ] TC-MASTER parsed (openpyxl, không từ MEMORY summary) — mọi sheet TC (Test Cases, Test Case 2, ...) đã được duyệt, không chỉ sheet đầu tiên
- [ ] Row label Screen/Block (cột A rỗng) đã bị loại khỏi tập TC trước khi đếm/chạy check — không có false Critical nào phát sinh từ row label
- [ ] Formula cột A/AM/AN/AO đã đối chiếu (data_only=False) để phát hiện bị gõ đè
- [ ] Agent gọi (hoặc fallback + disclaimer)
- [ ] R1-R4 checks run (60 total checks)
- [ ] Findings classified by severity
- [ ] Score calculated
- [ ] Report file tạo
- [ ] §8 = COMPLETED
