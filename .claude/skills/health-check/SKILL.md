---
name: health-check
description: Validate tính nhất quán giữa các MEMORY files, TC-MASTER Excel, bug-index, và Pipeline Status. Phát hiện data drift, orphan references, missing entries, stale status. Chạy bất kỳ lúc nào — khuyến nghị sau mỗi skill hoàn thành. Trigger khi user nhắc "health check", "kiểm tra consistency", "validate MEMORY", "check pipeline status", "data có khớp không", "MEMORY có đúng không", "kiểm tra dữ liệu", "so sánh MEMORY files", hoặc khi user nghi ngờ data không nhất quán giữa các bước.
license: Proprietary — FPT QA Toolkit v1.0 (qc-claude-v1)
compatibility: Designed for Claude Code QA projects with 00_..11_ folder structure (qc-claude-v1). Requires Claude Code or compatible agent runtime.
metadata:
  toolkit: qc-claude-v1
  pipeline-position: "13"
  status-section: MASTER-MEMORY-section-8
  owner: QC Team
  version: "1.1"
  released: "2026-06-05"
  updated: "2026-07-21 — migrated Group C checks sang template ISC (42-cột, xem generate-tc/references/consolidate.md): C-02 SC ID→Req ID orphan, C-06/C-07 Lifecycle/Version Origin column (đã bị xoá) → Remark tag 'Carried từ v[X]', C-09 Notes→Remark column. Trước đó (2026-05-29): Mode-aware C-03; added C-08 Coverage Matrix, C-09 technique tag format, F-05/F-06 Source Detail blocks."
---

# Health Check — Pipeline Consistency Validator

Quét và đối chiếu dữ liệu giữa tất cả MEMORY files + TC-MASTER + bug-index. Phát hiện inconsistency, orphan references, stale data, pipeline status anomalies.

---

## Nguyên tắc cốt lõi

- **Chỉ đọc, không sửa.** Skill này report findings — user hoặc skill liên quan sửa.
- **Cross-reference, không đoán.** Mỗi finding phải chỉ rõ: file A nói gì, file B nói gì, mâu thuẫn ở đâu.
- **Severity-based.** CRITICAL → WARNING → INFO — giúp user ưu tiên xử lý.
- **Nhanh.** Mode QUICK chạy dưới 30 giây, đọc MEMORY files only (không parse Excel).

---

## Vị trí trong Pipeline

```
              ┌──────────────────────────────────────────────┐
              │          ★ health-check ★                     │
              │   Cross-cutting — chạy bất kỳ lúc nào       │
              │   Đọc: tất cả MEMORY files + TC-MASTER       │
              │   Ghi: report vào 09_reports/                │
              └──────────────────────────────────────────────┘
                    ↕               ↕              ↕
              MASTER-MEMORY   Version MEMORY   Source MEMORY
              TC-MASTER       bug-index        Pipeline §8
```

Không có upstream/downstream dependency. Chạy độc lập bất kỳ lúc nào.

---

## Cách gọi & Entry Modes

### Mode QUICK — Kiểm tra nhanh (chỉ MEMORY files)
```
"Health check"
"Kiểm tra consistency"
"MEMORY có khớp không"
"Quick check"
```
**Scope:** Chỉ đọc .md files (MASTER-MEMORY, Version MEMORY, Source MEMORY, bug-index, Pipeline §8). KHÔNG parse Excel.
**Thời gian:** < 30 giây.
**Output:** Inline summary trong chat.

### Mode FULL — Kiểm tra toàn diện (bao gồm TC-MASTER Excel)
```
"Full health check"
"Kiểm tra toàn bộ data"
"Deep validate"
"Health check đầy đủ"
```
**Scope:** Đọc tất cả MEMORY files + parse TC-MASTER Excel + scan fragments.
**Thời gian:** 1-3 phút tuỳ project size.
**Output:** File `09_reports/health-check-[date].md` + inline summary.

### Mode VERSION — Kiểm tra 1 version cụ thể
```
"Health check cho v2.0"
"Validate data version 1.1"
"Kiểm tra v2.0 có nhất quán không"
```
**Scope:** Chỉ data liên quan version chỉ định.

### Detect Logic

```
User message → kiểm tra:

1. User nói "full" / "toàn bộ" / "deep" / "đầy đủ"?
   └── CÓ → Mode FULL

2. User chỉ định version cụ thể?
   └── CÓ → Mode VERSION

3. Else → Mode QUICK
```

---

## Workflow

### Step 1: Đọc Context

```
1. PIPELINE.md (root)                               → skill registry, status protocol
2. CLAUDE.md (root)                                  → project info
3. 02_analyze-requirements/MASTER-MEMORY.md          → version registry, scenario lifecycle, pipeline §8
4. 02_analyze-requirements/Project_rule.md           → naming rules
5. 02_analyze-requirements/[active-version]/MEMORY.md → version data + §9 TC Gen Log (Mode + Techniques cols)
6. 10_source-code/MEMORY.md                          → source code tracking
7. 05_bug-reports/bug-index.md                       → bug data
8. 03_test-cases/[version]/TC-MASTER-v[version].xlsx  → (Mode FULL only) alias của file ISC chính thức
                                                          (xem generate-tc/references/consolidate.md) —
                                                          42 cột A-AP, 1 sheet "Test Cases"/"Test Case N"
                                                          riêng cho mỗi module, + sheet RTM/Dashboard/
                                                          Summary/Bug Data/Report Test/Coverage Matrix
```

Nếu file nào không tồn tại → ghi nhận `[MISSING]`, không báo lỗi — project có thể đang ở early stage.

#### Mode detection (đọc §9 cho mode-aware checks — added 2026-05-29)

Per generate-tc skill v4.1+, MEMORY §9 TC Gen Log có thêm 2 cols `Mode` + `Techniques`:

| Mode value | Implication cho health-check |
|---|---|
| `standard` (default) hoặc trống | TC count = baseline 1-1 mapping. Coverage Matrix sheet KHÔNG expected. Remark column (AP) technique tag KHÔNG expected. |
| `comprehensive` | TC count = baseline + derived (typical 3-12× expansion). Coverage Matrix sheet expected. Remark column technique tag expected per derived TC. |
| `selective` | TC count = baseline + partial derived (per `Techniques` col list). Coverage Matrix sheet expected. Remark technique tag expected. |

Per analyze-requirements skill v4.1+, mỗi REQ/SC/Clarification có 3 fields tách biệt: **Source Quote** + **Source Location** + **Analyst Note**. F-05/F-06 checks validate presence (informational — Part 2 verbatim quoting is opt-in default ON).

**Health-check phải read §9 trước khi run Group C checks** để classify expected behavior.

### Step 2: Chạy Validation Checks

#### Check Group A — Pipeline Status (từ MASTER-MEMORY §8)

| Check ID | Check | Severity | Logic |
|----------|-------|----------|-------|
| A-01 | Skill status = IN_PROGRESS quá lâu | WARNING | Last Run > 1 ngày trước mà vẫn IN_PROGRESS → có thể đã crash |
| A-02 | Skill status = FAILED chưa xử lý | CRITICAL | FAILED status mà downstream skill đã chạy → data risk |
| A-03 | Downstream chạy trước upstream | CRITICAL | Skill N status ≥ PARTIAL nhưng prerequisite skill = NOT_STARTED |
| A-04 | Pipeline §8 thiếu trong MASTER-MEMORY | WARNING | §8 chưa tồn tại → suggest thêm |
| A-05 | Active version trong MASTER-MEMORY khớp version gần nhất | INFO | Kiểm tra version registry vs active version |

#### Check Group B — Scenario Consistency

| Check ID | Check | Severity | Logic |
|----------|-------|----------|-------|
| B-01 | Scenario count match | CRITICAL | MASTER-MEMORY §3 tổng scenarios ≠ Version MEMORY §3 tổng scenarios (filter theo version) |
| B-02 | Scenario ID orphan trong MASTER | WARNING | SC ID có trong MASTER-MEMORY §3 nhưng KHÔNG có trong Version MEMORY §4 |
| B-03 | Scenario ID orphan trong Version MEMORY | WARNING | SC ID có trong Version MEMORY §4 nhưng KHÔNG có trong MASTER-MEMORY §3 |
| B-04 | Lifecycle mismatch | CRITICAL | MASTER-MEMORY §3 ghi `NEW` nhưng Version MEMORY §4 ghi `CARRIED` (hoặc ngược lại) |
| B-05 | Module summary count mismatch | WARNING | Version MEMORY §3 Module Summary tổng SC ≠ đếm thực tế trong §4 Scenario Index |
| B-06 | Priority distribution mismatch | INFO | §3 ghi P1:5, P2:3 nhưng đếm trong §4 ra P1:4, P2:4 |
| B-07 | DEPRECATED scenario vẫn active | WARNING | MASTER-MEMORY §3 Lifecycle = DEPRECATED nhưng Version MEMORY §4 vẫn liệt kê active |

#### Check Group C — TC Consistency (Mode FULL — cần parse Excel)

> **Row label Screen/Block KHÔNG phải TC.** Sheet Test Cases có thể chèn row label Screen/Block xen
> giữa các row TC (`generate-tc/references/generate.md` Step 6.4 — Screen: merge A:I, fill `FF729FCF`;
> Block: merge B:I, fill `FFAFD095`). Nhận diện row là TC bằng cột A (Testcase ID, giá trị đã resolve)
> KHÔNG rỗng — row label có cột A rỗng (do cột C rỗng). **Mọi check C-02/C-05/C-06/C-09 bên dưới đọc
> cột B (Req ID)/AP (Remark) theo từng row PHẢI lọc bỏ row label trước** — Block label có text ở cột B
> (vd `"Block Thông tin filter"`), nếu không lọc sẽ bị C-02 hiểu nhầm thành Req ID lạ → false CRITICAL.

| Check ID | Check | Severity | Logic |
|----------|-------|----------|-------|
| C-01 | Scenario chưa có TC | WARNING | SC ID trong Version MEMORY §4 TC Status = ⏳ nhưng TC-MASTER không có TC nào có Req ID tương ứng scenario đó (theo mapping SC↔REQ ở Version MEMORY) |
| **C-02** | **TC orphan — Req ID không tồn tại** | **CRITICAL** | **(đổi từ "SC ID" — template ISC không còn Scenario ID column)** TC trong 1 sheet TC-MASTER có Req ID (cột B) KHÔNG có row tương ứng trong sheet `RTM`, HOẶC Req ID đó không tồn tại trong Version MEMORY §2 (Document/Requirement registry). Lưu ý: review-tc R2-16 đã check RTM formula fan-out ở mức nội bộ Excel — C-02 check thêm chiều cross-file (Excel ↔ MEMORY) mà review-tc không có phạm vi. |
| **C-03** | **TC count mismatch (mode-aware)** | **WARNING** | **Logic depends on MEMORY §9 Mode column (read in Step 1):**<br>• `standard` / empty → expected = Σ §9 row counts; mismatch = WARNING<br>• `comprehensive` → expected = Σ §9 row counts (skill đã ghi expanded count khi generate); mismatch = WARNING<br>• `selective` → expected = Σ §9 row counts với techniques applied; mismatch = WARNING<br>**Critical:** KHÔNG raise CRITICAL chỉ vì count > baseline — comprehensive expansion (3-12×) là design intent. So sánh actual vs §9 logged count, không vs baseline scenario count. TC count đọc qua sheet `Dashboard` cột "Tổng TC" (đã auto-tính theo formula), KHÔNG tự đếm lại row Excel. |
| C-04 | TC-MASTER vs fragments drift | INFO | Fragments mới hơn TC-MASTER (chưa SYNC) |
| C-05 | CARRIED TC thiếu trong TC-MASTER | WARNING | MASTER-MEMORY §4 Regression Scope liệt kê CARRIED SC cần test nhưng TC-MASTER không có TC nào ghi `Carried từ v[X]` trong Remark (cột AP) ứng với Req ID ánh xạ từ SC đó |
| **C-06** | **CARRIED tag mismatch** | **WARNING** | **(đổi từ "TC Lifecycle mismatch column O" — cột Lifecycle đã bị xoá khỏi template)** TC có Remark (cột AP) chứa `Carried từ v[X]` nhưng MASTER-MEMORY §3 Lifecycle cho scenario/Req liên quan KHÔNG phải `CARRIED`, hoặc ngược lại: MASTER-MEMORY ghi CARRIED cho scenario đó nhưng không TC nào trong sheet tương ứng có tag `Carried từ v[X]`. |
| **C-07** | **Carried-from version mismatch** | **INFO** | **(đổi từ "Version Origin mismatch column N" — cột Version Origin đã bị xoá khỏi template)** TC có Remark chứa `Carried từ v[X]` nhưng `v[X]` KHÔNG khớp version cha thật sự của scenario đó theo MASTER-MEMORY §4 Regression Scope (vd tag ghi `v1.0` nhưng scenario thực ra carry từ `v1.1`). |
| **C-08** | **Coverage Matrix sheet missing** | **WARNING** | MEMORY §9 Mode = `comprehensive` HOẶC `selective` nhưng TC-MASTER `.xlsx` không có sheet `Coverage Matrix`. Per generate-tc skill, sheet này mandatory khi mode active (sheet phụ, KHÔNG thuộc bộ 9 sheet chuẩn ISC). Fix: re-run `/generate-tc --consolidate` để regenerate matrix sheet. Severity WARNING vì TC data vẫn valid, chỉ thiếu report sheet. |
| **C-09** | **Technique tag format invalid** | **INFO** | **(đổi từ "TC Notes column (M)" — template ISC không còn Notes, dùng Remark)** MEMORY §9 Mode = `comprehensive` HOẶC `selective` nhưng TC derived (TC ID sinh sau baseline trong cùng sheet) có **Remark (cột AP)** thiếu pattern `Technique: <B[1-8]>-<subtype>` (per `techniques.md` tag conventions — có thể là 1 phần trong chuỗi Remark nối bằng ` \| `). Severity INFO vì traceability mất một phần, không break logic. |

#### Check Group D — Source Code Consistency

| Check ID | Check | Severity | Logic |
|----------|-------|----------|-------|
| **D-01** | **TC implemented nhưng Source MEMORY không track (mode-aware)** | **WARNING** | **Logic depends on MEMORY §9 Mode column:**<br>• `standard` → expect 1:1 TC ID ↔ §13 entry; missing entry = WARNING<br>• `comprehensive` / `selective` → DERIVED TCs có thể được implement via parameterized test method (1 method covers multiple TCs via DataProvider). §13 entry track SC-level hoặc baseline TC-level OK; missing entry ONLY khi không có baseline TC mapping nào. Severity downgrade INFO nếu derived TCs share parent method. |
| D-02 | Test method orphan | INFO | Source MEMORY §7 Test Registry có method mà §13 không link về TC ID |
| D-03 | Page class mismatch | INFO | Source MEMORY §6 Page Registry liệt kê class nhưng file không tồn tại trên disk (Mode FULL: verify file) |
| D-04 | Locator stale | WARNING | Source MEMORY §12 Locator Registry có entry cũ hơn 30 ngày chưa re-validate |

#### Check Group E — Bug Consistency

| Check ID | Check | Severity | Logic |
|----------|-------|----------|-------|
| E-01 | Bug orphan — Fail ID không tồn tại | CRITICAL | bug-index.md có Fail ID không tồn tại trong Source MEMORY §16 |
| E-02 | Bug count mismatch by version | WARNING | bug-index.md "By Version" tổng ≠ đếm thực tế rows filter theo version |
| E-03 | ASSERTION_FAIL chưa có bug | WARNING | Source MEMORY §16 có ASSERTION_FAIL status = Open mà bug-index.md không có entry tương ứng |
| E-04 | Bug status stale | INFO | Bug status = Open > 14 ngày → cảnh báo |
| E-05 | Bug traceability chain đứt | CRITICAL | Bug thiếu bất kỳ link nào: FAIL ID, RUN ID, TC ID, SC ID |

#### Check Group F — Cross-File References

| Check ID | Check | Severity | Logic |
|----------|-------|----------|-------|
| F-01 | DOC ID orphan | WARNING | Version MEMORY §2 Document Registry có DOC ID mà requirement_traceability.md không reference |
| F-02 | REQ ID orphan | WARNING | requirement_traceability.md có REQ ID mà scenario_map không reference |
| F-03 | DOC ID format sai | INFO | DOC ID không follow pattern `DOC-v[VERSION]-[NN]` |
| F-04 | Naming convention violation | INFO | SC ID, TC ID, BUG ID không follow Project_rule.md §1.2 |
| **F-05** | **Version MEMORY §4.1 Source Detail blocks missing** | **INFO** | **(NEW 2026-05-29 — Part 2 verbatim quoting validation)** Version MEMORY §4 Scenario Index có rows nhưng §4.1 Source Detail (3-field: Source Quote + Source Location + Analyst Note) trống hoặc thiếu cho NEW/MODIFIED scenarios. Per analyze-requirements skill v4.1+, mandatory default (opt-out qua `--no-quote`). **Severity INFO** vì: (1) Part 2 is opt-in default ON, user có thể chủ động `--no-quote`; (2) legacy version (pre-2026-05-29 analyses) không expected có. Only raise INFO khi: version analyzed sau 2026-05-29 + skip `--no-quote` + thiếu blocks. |
| **F-06** | **scenario_map.md per-scenario Source Detail missing** | **INFO** | **(NEW 2026-05-29)** scenario_map.md có rows NEW/MODIFIED scenarios nhưng thiếu block "Source Detail per Scenario" (Source Quote + Source Location + Analyst Note) dưới bảng main per module. Same opt-out rules as F-05. |

---

### Step 3: Tổng hợp & Trình bày

#### Mode QUICK — Inline summary

```
🏥 Health Check — v[VERSION] — [date]

Pipeline Status:
  ✅ 7 skills COMPLETED | ⏳ 1 IN_PROGRESS | ⬜ 5 NOT_STARTED

Findings:
  🔴 CRITICAL: [N] issues
     - [B-01] Scenario count: MASTER-MEMORY = 30, Version MEMORY = 28 (thiếu 2)
     - [E-05] BUG-003 thiếu TC ID trong traceability chain

  🟡 WARNING: [N] issues
     - [C-04] 2 fragments mới chưa SYNC vào TC-MASTER
     - [D-04] 5 locators chưa re-validate > 30 ngày

  🔵 INFO: [N] issues
     - [F-03] DOC-01 thiếu version prefix (nên là DOC-v1.0-01)

Summary: [N] CRITICAL | [N] WARNING | [N] INFO
Recommendation: Fix [N] CRITICAL issues trước khi chạy skill tiếp theo.
```

#### Mode FULL — File report + inline summary

Tạo file `09_reports/health-check-[YYYY-MM-DD].md`:

```markdown
# Health Check Report — v[VERSION]

> Generated: [datetime]
> Mode: FULL
> Files checked: [list]

## Pipeline Status

(copy từ MASTER-MEMORY §8, highlight anomalies)

## Findings by Severity

### 🔴 CRITICAL ([N])

#### [B-01] Scenario count mismatch
- **MASTER-MEMORY §3:** 30 scenarios total
- **Version MEMORY §4:** 28 scenarios listed
- **Missing SC IDs:** SC-DASH-015, SC-DASH-016
- **Impact:** generate-tc có thể bỏ sót 2 scenarios
- **Fix:** Chạy `analyze-requirements Mode UPDATE` để đồng bộ

(tiếp tục cho từng finding...)

### 🟡 WARNING ([N])
...

### 🔵 INFO ([N])
...

## Cross-Reference Matrix

> Cột "TC-MASTER" không còn đọc trực tiếp SC ID từ Excel (template ISC không có cột này) — resolve gián tiếp qua Req ID: SC ID → Req ID (mapping ở Version MEMORY §4) → tra Req ID đó trong sheet `RTM`/`Test Cases`.

| SC ID | MASTER §3 | Version §4 | Req ID (mapping) | TC-MASTER (qua RTM) | Source §13 | Status |
|-------|-----------|-----------|-----------|-----------|-----------|--------|
| SC-LOGIN-001 | ✅ NEW | ✅ | REQ-01 | ✅ TC_01.1 | ✅ testLoginSuccess | OK |
| SC-DASH-015 | ✅ NEW | ❌ MISSING | REQ-15 | ❌ | ❌ | 🔴 |
| SC-DASH-016 | ✅ NEW | ❌ MISSING | REQ-16 | ❌ | ❌ | 🔴 |

## Recommendation

1. [Ưu tiên fix CRITICAL]
2. [Suggest skill nào chạy để fix]
3. [Timeline nếu có deadline context]
```

### Step 4: Cập nhật Pipeline Status

Ghi vào MASTER-MEMORY §8:
```
| 13 | health-check | COMPLETED | [date] | [Quick/Full/Version] | [N] CRITICAL, [N] WARNING | — |
```

---

## Severity Definitions

| Severity | Ý nghĩa | Khi nào dừng pipeline |
|----------|---------|----------------------|
| **CRITICAL** | Data inconsistency ảnh hưởng output downstream. Chạy tiếp sẽ tạo artifact sai. | **KHUYẾN NGHỊ DỪNG** — fix trước khi chạy skill tiếp |
| **WARNING** | Data có gap nhưng downstream vẫn chạy được, output có thể thiếu sót. | Tiếp tục được, nhưng nên fix sớm |
| **INFO** | Convention violation hoặc stale data — không ảnh hưởng logic. | Tiếp tục bình thường, fix khi tiện |

---

## Fix Routing — Finding → Skill nào fix

| Finding Group | Skill chịu trách nhiệm fix | Mode suggest |
|---------------|---------------------------|-------------|
| A (Pipeline Status) | User manual update MASTER-MEMORY §8 | — |
| B (Scenario) | analyze-requirements | Mode UPDATE hoặc REVIEW |
| C (TC) | generate-tc | Mode SYNC hoặc REGENERATE |
| D (Source Code) | scan-source-code hoặc implement-automation | Mode DELTA hoặc UPDATE |
| E (Bug) | log-bug | Mode UPDATE |
| F (Cross-ref) | analyze-requirements | Mode UPDATE |

---

## Checklist

- [ ] Đọc PIPELINE.md trước khi chạy
- [ ] Xác định mode (QUICK / FULL / VERSION)
- [ ] Chạy tất cả checks applicable cho mode
- [ ] Mode FULL: row label Screen/Block (cột A rỗng) đã lọc khỏi tập TC trước khi chạy Group C — không có false C-02 từ text label Block ở cột B
- [ ] Phân loại severity cho mỗi finding
- [ ] Trình bày inline summary (mọi mode)
- [ ] Tạo file report (Mode FULL only)
- [ ] Cập nhật MASTER-MEMORY §8 Pipeline Status
- [ ] KHÔNG sửa bất kỳ file nào — chỉ report

---

## Khi nào NÊN chạy health-check

| Timing | Mode recommend | Lý do |
|--------|---------------|-------|
| Sau analyze-requirements hoàn thành | QUICK | Verify MASTER ↔ Version MEMORY sync |
| Sau generate-tc CONSOLIDATE | FULL | Verify TC-MASTER ↔ MEMORY ↔ scenarios |
| Trước implement-automation | QUICK | Ensure TC-MASTER sẵn sàng |
| Sau execute-maintain + log-bug | FULL | Verify execution ↔ bug ↔ traceability chain |
| Trước test-report | FULL | Ensure all data consistent trước khi report stakeholder |
| Khi user nghi ngờ data sai | VERSION | Targeted check |
| Khi onboard member mới | QUICK | Cho member thấy project health overview |

## Examples

### Example 1: Quick scan
**Input:** `/health-check`
**Behavior:** Read MEMORY files (no Excel parse), run Group A-F checks, inline summary.
**Output:** `🔴 2 CRITICAL · 🟡 3 WARNING · 🔵 2 INFO`

### Example 2: Full scan including Excel
**Input:** `/health-check --full`
**Behavior:** + Parse TC-MASTER Excel + scan fragments, write report to `09_reports/health-check-[date].md`.

### Example 3: Version-specific check
**Input:** `/health-check --version v2.0`
**Behavior:** Only check data liên quan v2.0 (filter out v1.0 noise).

## Common Edge Cases

| Scenario | Handling |
|----------|----------|
| MEMORY files thiếu | Mark `[MISSING]`, không báo error (early-stage project) |
| §8 chưa tồn tại trong MASTER-MEMORY | A-04 WARNING, suggest add |
| Scenario count khác biệt (MASTER §3 vs Version §3) | B-01 CRITICAL, suggest `/analyze-requirements --update` |
| FAIL status > 1 day cũ | A-01 WARNING (có thể crashed) |
| §16 Fails marked Open nhưng PASS in latest run | Stale Fail row — cross-check §15 latest run, suggest mark Fixed |
| TC count drift (Excel vs MEMORY §9) | C-03 WARNING (mode-aware: compare vs §9 logged count, NOT vs baseline scenario count — comprehensive expansion 3-12× là design intent) |
| Locator > 30 days old chưa re-validate | D-04 WARNING |
| ALL findings = 0 | Output "🟢 CLEAN" + skip recommendation section |
| MEMORY §9 Mode = comprehensive nhưng TC-MASTER thiếu Coverage Matrix sheet | C-08 WARNING — suggest `/generate-tc --consolidate` để regenerate |
| MEMORY §9 Mode = comprehensive nhưng TC Remark column (AP) thiếu technique tags | C-09 INFO — không break logic nhưng mất traceability |
| TC Remark có `Carried từ v[X]` nhưng MASTER-MEMORY Lifecycle không khớp | C-06 WARNING — xem `references` generate-tc/consolidate.md Step 2 cho quy tắc tag đúng |
| TC-MASTER là workbook ISC nhưng thiếu 1 trong 8 sheet chuẩn (Cover/Guideline/Revision History/Summary/Dashboard/Report Test/Bug Data/RTM) | WARNING mới — file có thể bị build từ template cũ hoặc bị xoá nhầm sheet, suggest re-run `/generate-tc --consolidate` từ template gốc |
| Version analyzed 2026-05-29+ nhưng MEMORY §4.1 + scenario_map Source Detail thiếu | F-05 + F-06 INFO (cả 2) — verify user có cố tình `--no-quote` không trước khi flag |
| MEMORY §9 Mode column trống (legacy MEMORY pre-2026-05-29) | Treat as `standard` (backward-compat). KHÔNG raise C-08/C-09 vì pre-expansion artifacts. |

