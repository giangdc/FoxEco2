---
name: generate-tc
description: Tạo bộ test case manual Excel (.xlsx) từ kết quả analyze-requirements, hỗ trợ fragments per-module + TC-MASTER consolidate cross-version. Version-aware output. Supports 3 modes (standard 1-1 default / comprehensive applies all 8 test design techniques B1-B8 / selective opt-in via --techniques flag). Tier B techniques include equivalence partitioning (EP), boundary value analysis (BVA), decision table (DT), state transition (ST), pairwise (PW), error guessing (EG), CRUD matrix, cause-effect graph (CEG). Generates optional Coverage Matrix sheet showing technique × scenario heatmap. Use when user mentions 'viết test case', 'tạo TC', 'generate TC', 'xuất Excel test case', 'gộp TC', 'consolidate TC', 'tổng hợp TC', 'sync TC', 'comprehensive mode', 'test design techniques', 'equivalence partitioning', 'boundary value analysis', 'coverage matrix', 'mở rộng test case', or runs /generate-tc command.
license: Proprietary — FPT QA Toolkit v1.0 (qc-claude-v1)
compatibility: Designed for Claude Code QA projects with 00_..11_ folder structure (qc-claude-v1). Requires Claude Code or compatible agent runtime.
metadata:
  toolkit: qc-claude-v1
  pipeline-position: "4"
  status-section: MASTER-MEMORY-section-8
  owner: QC Team
  version: "1.1"
  released: "2026-06-05"
  updated: "2026-07-21"
  tc-template: "ISC_Template_SDLC_TestCase_Report_Version.xlsx (QA template, mặc định /home/giangdc2/AI/Template/)"
---

# Generate Test Cases

Chuyển scenarios + test data → file Excel TC vào `03_test-cases/[version]/`.

## Command

| Command | Mode | Mô tả |
|---------|------|-------|
| `/generate-tc` | GENERATE | Tạo TC cho active version (tất cả modules) — **Standard 1-1 mapping (backward-compat default)** |
| `/generate-tc --mode comprehensive` | GENERATE+Techniques | Apply tất cả test design techniques applicable (B1-B8) per scenario. Output thêm sheet `Coverage Matrix`. |
| `/generate-tc --techniques EP,BVA,EG` | GENERATE+Techniques | Selective opt-in chỉ techniques user list. Combinations: EP/BVA/DT/ST/PW/EG/CRUD/CEG. |
| `/generate-tc --module NAME` | GENERATE | Tạo TC cho 1 module |
| `/generate-tc --priority P1` | GENERATE | Chỉ tạo P1 |
| `/generate-tc --direct --name "X" --id N --spec "..."` | DIRECT | Viết TC nhanh không qua analyze |
| `/generate-tc --regenerate --module NAME` | REGENERATE | Tạo lại TC sau khi analyze update |
| `/generate-tc --consolidate` | CONSOLIDATE | Gộp fragments → TC-MASTER |
| `/generate-tc --sync` | SYNC | Đồng bộ fragment mới vào TC-MASTER |
| `/generate-tc --review` | REVIEW | Xem tổng quan TC đã tạo |

Options: `--version vX.Y` `--priority P1|P2|P3` (map sang giá trị cell thật `High|Medium|Low` — xem `references/generate.md`) `--module NAME` `--dry-run` `--mode {standard,comprehensive}` `--techniques <list>`

> **3 modes (Tier B test design techniques, added 2026-05-29):**
> - **Standard (default, no flag):** Hiện tại 1-1 mapping. **No regression risk** — output identical to pre-2026-05-29 behavior.
> - **Comprehensive:** Per scenario chạy rubric → apply tất cả 8 techniques applicable → expand TC count ~3-5x. Output thêm sheet `Coverage Matrix`. **Enforced bằng compliance gate** (xem `references/generate.md` — Step 3a Contract + Checklist gate); AI KHÔNG được tự hạ về standard.
> - **Selective:** `--techniques BVA,EG` chỉ apply techniques user list. Useful cho incremental adoption.
>
> Backward-compat: Excel structure (42-cột ISC) unchanged khi no-flag · Group enum không mở rộng (technique tag đi vào Remark column, xem `references/generate.md`).

## Prerequisites

| Cần có | Check |
|--------|-------|
| Version MEMORY.md + scenario_map + data_catalog | analyze-requirements §8 = COMPLETED |
| MASTER-MEMORY.md | Regression scope |
| `03_test-cases/_template/ISC_Template_SDLC_TestCase_Report_Version.xlsx` | Nếu chưa có, skill tự copy từ Project_rule.md `tc-template-path` (mặc định `/home/giangdc2/AI/Template/`) — xem `references/generate.md` Step 0 |

## Pipeline

`analyze-requirements` → **★ generate-tc ★** → `review-tc`, `implement-automation`, `review-src-tc`

**Folder sở hữu:** `03_test-cases/`

## Mode Routing

| Condition | → Load |
|-----------|--------|
| `--consolidate` | `references/consolidate.md` |
| `--sync` | `references/sync.md` |
| `--regenerate` | `references/regenerate.md` |
| `--direct` hoặc không có MEMORY | `references/direct.md` |
| `--review` hoặc nhắc xem | `references/review.md` |
| `--mode comprehensive` HOẶC `--techniques <list>` | `references/generate.md` + `references/techniques.md` + `references/technique-rubric.md` (load thêm techniques + rubric) |
| Default (tạo TC, no mode flag) | `references/generate.md` (KHÔNG load techniques/rubric — preserve backward-compat) |

## Nguyên tắc

- **Đọc từ analyze output, không hỏi lại.** MEMORY + scenario_map + data_catalog là input.
- **Traceability bắt buộc.** TC → REQ ID + DOC ID (cột B, C — template ISC không còn cột Scenario ID riêng; mapping SC↔TC vẫn lưu ở Version MEMORY §9). Khi project áp dụng Part 2 verbatim quoting, TC Remark column có thể reference Source Quote (link sang scenario-map anchor).
- **TC-MASTER là single source of truth** cho downstream.
- **Output vào fragments/ trước**, CONSOLIDATE/SYNC vào TC-MASTER sau.
- **Bám sát template ISC QA ban hành — không tự dựng sheet/cột.** Mọi Excel output dựa trên `03_test-cases/_template/ISC_Template_SDLC_TestCase_Report_Version.xlsx` (copy 1 lần từ Project_rule.md `tc-template-path`, mặc định `/home/giangdc2/AI/Template/`). 42 cột A-AP, generate-tc chỉ ghi cột B-M (+ AP có điều kiện); cột A (Testcase ID) và AM/AN/AO là formula tự sinh, KHÔNG gõ tay. 1 sheet Test Cases/module, cộng 8 sheet workbook-level cố định (Cover/Guideline/Revision History/Summary/Dashboard/Report Test/Bug Data/RTM). Chi tiết đầy đủ: `references/generate.md`.
- **File naming theo Guideline QA:** `ISC_[Tên dự án]_[Version]_TC_[Version TC]_R[Round].xlsx`. `review-tc` đã migrate (đọc thẳng alias, hiểu đúng schema 42-cột). Các skill downstream còn lại (implement-automation, review-src-tc, health-check, test-report, log-bug, vibe-test) chưa migrate theo template mới, nên generate-tc **vẫn phải** xuất thêm alias `TC-MASTER-v[X].xlsx` / `TC-MASTER-LATEST.xlsx` trỏ tới cùng nội dung — gỡ bỏ dần khi từng skill đó được cập nhật.
- **Backward-compat default.** No mode flag → 1-1 scenario→TC mapping (current behavior). Opt-in techniques qua `--mode comprehensive` hoặc `--techniques <list>`.
- **Field/Column/Dropdown-Option completeness check là BẮT BUỘC, mọi mode (kể cả standard).** Bất kỳ requirement nào liệt kê ≥2 trường/cột hiển thị cho 1 màn hình (bảng danh sách, form, card, dialog) — HOẶC ≥2 option cụ thể trong 1 dropdown/select/filter (enum cố định, không phải free-text) — phải có ≥1 TC riêng verify ĐỦ + ĐÚNG toàn bộ danh sách đó — không được coi là "cover" chỉ vì có TC test hành vi hẹp của từng field/option riêng lẻ (vd TC "chọn template A → lọc đúng" KHÔNG thay thế được TC "dropdown có đủ 5 template"). Xem `references/generate.md` Step 3b (có 2 case study thật giải thích vì sao rule này tồn tại — 1 về cột bảng, 1 về dropdown option).

## Status Protocol

§8: GENERATE xong 1 module = PARTIAL. CONSOLIDATE xong = COMPLETED.

## Examples

### Example 1: Generate TC for new version
**Input:** `/generate-tc --version v2.0`
**Behavior:**
1. Đọc Version MEMORY §3-§4 (scenarios)
2. Generate fragments per module → `03_test-cases/v2.0/fragments/`
3. Hỏi consolidate vào TC-MASTER

**Output:** `fragments/TC-DASHBOARD-v2.0.xlsx (12 TCs High:5/Medium:4/Low:3)` — 1 sheet dựa trên template "Test Cases", cột A/AM/AN/AO formula copy-down.

### Example 2: Filter by module + priority
**Input:** `/generate-tc --module Dashboard --priority High`
**Behavior:** Generate chỉ TCs Priority=High cho Dashboard module.

### Example 3: Direct mode (no analyze)
**Input:** `/generate-tc --direct --name "Đăng nhập" --id 11 --spec "paste spec..."`
**Behavior:** Skip analyze, viết TC trực tiếp từ user spec. Hỏi 6 câu (env, version, type).

### Example 4: Consolidate fragments
**Input:** `/generate-tc --consolidate`
**Behavior:** Merge all `fragments/*.xlsx` vào TC-MASTER — workbook dựng từ template ISC (Cover/Guideline/Revision History/Summary/Dashboard/Report Test/Bug Data/RTM + 1 sheet Test Cases/module). Output chính `ISC_[Project]_[VERSION]_TC_[TCVersion]_R[Round].xlsx`, cộng alias `TC-MASTER-v[VERSION].xlsx` + `TC-MASTER-LATEST.xlsx` cho downstream skill chưa migrate.

### Example 5: Sync after update
**Input:** `/generate-tc --sync`
**Behavior:** Detect fragment updates since last consolidate → merge only changed modules.

### Example 6: Comprehensive mode (Tier B techniques)
**Input:** `/generate-tc --mode comprehensive --module Auth`
**Behavior:**
1. Đọc Version MEMORY §3-§4 + Source Quotes (nếu Part 2 verbatim quoting enabled).
2. Per SC chạy rubric (`references/technique-rubric.md`) → list applicable techniques (B1-B8).
3. Present rubric output to user → confirm/edit each technique application.
4. Apply techniques per `references/techniques.md` → expand TCs.
5. Output fragment Excel với Remark column ghi `Technique: <tag>` per derived TC.
6. Output additional sheet `Coverage Matrix` (schema: `assets/coverage-matrix-template.md`).

**Output:** `TC-AUTH-v2.0.xlsx (30 TCs High:20/Medium:10, từ 6 SC × techniques B1+B2+B6)` + Coverage Matrix sheet.

### Example 7: Selective techniques opt-in
**Input:** `/generate-tc --techniques BVA,EG --module Registration`
**Behavior:** Apply chỉ B2 (Boundary Value Analysis) + B6 (Error Guessing). Useful incremental adoption — sprint sau thêm techniques khác.

### Example 8: Field/Column/Dropdown-Option completeness check (mọi mode, kể cả standard)
**Tình huống A (cột bảng):** Requirement cho màn "Danh sách X" liệt kê 8 cột bảng (Source Quote đánh số STT 12-19: Loại gói, Gói bán, Kênh bán, SKU, Thời gian/Người cập nhật, Thời gian/Người tạo). Nếu chỉ generate 2 TC hẹp (vd "cột SKU hiện — khi rỗng", "định dạng datetime") mà KHÔNG có TC nào verify cả 8 cột cùng lúc → **VI PHẠM Step 3b**, cần bổ sung ngay TC riêng "Kiểm tra đầy đủ 8 cột hiển thị tại Danh sách X" liệt kê rõ tên từng cột.
**Tình huống B (dropdown option, case thật CMS v1.4 LDP):** SC "chọn 1 template ở dropdown 'Tất cả template' → danh sách lọc đúng" chỉ test hành vi filter, không test bản thân dropdown có đủ 5 template hay không (enum định nghĩa ở REQ khác). Nếu module có ≥1 SC dạng "chọn dropdown X → hành vi Y" nhưng KHÔNG có SC/TC nào verify "dropdown X hiển thị đủ/đúng option" → **VI PHẠM Step 3b**, bổ sung TC riêng "Check đầy đủ N option dropdown [tên field]".
**Behavior:** Trước khi báo generate xong module, tự grep Version MEMORY tìm mọi Source Quote/Analyst Note liệt kê ≥2 field/cột/option cho 1 màn hình hoặc 1 dropdown, đối chiếu đã có TC completeness riêng chưa, bổ sung nếu thiếu — kể cả khi option list của dropdown được định nghĩa ở REQ khác với REQ mô tả hành vi dùng dropdown đó.

## Common Edge Cases

| Scenario | Handling |
|----------|----------|
| Version MEMORY chưa có | Suggest `/analyze-requirements --init` trước |
| Scenario count > 100 | Generate per-module, suggest break into multi-sheet |
| Template gốc (`_template/ISC_...xlsx`) chưa có, không tìm thấy path cấu hình | DỪNG, báo user cần cung cấp template — không tự dựng schema thay thế |
| Duplicate Mã chức năng (C2) giữa các sheet | Block consolidate, report conflicts — không phải TC ID nữa (ID giờ là formula) |
| Tên module > 31 ký tự hoặc chứa `: \ / ? * [ ]` | Sanitize/rút gọn khi đặt tên tab sheet (Excel giới hạn 31 ký tự) |
| Missing test data trong catalog | Dùng placeholder rõ trong Steps + flag ở Remark column |
| MASTER-MEMORY active version conflict | Override via `--version` flag, log warning |
| CARRIED scenarios không có TC-MASTER-v[parent] | Skip regression, log warning |
| Fragment file corrupt (openpyxl error) | Backup + skip, suggest user re-export |
| Excel write permission denied | Suggest close Excel, retry |
| TC content > 32K chars per cell | Split steps into multi-cell |
| RTM đã có nhiều sheet, thêm sheet mới quên nối formula | Validate Step 4 (consolidate.md) chặn trước khi báo done — RTM sẽ báo sai coverage nếu thiếu term |

## See Also

### Pipeline references
- [PIPELINE.md](../../PIPELINE.md) — Skill registry + prerequisites matrix + §6 Mode Quick-Reference
- [COMMANDS.md](../../COMMANDS.md) — Cheat sheet với syntax examples cho 3 modes

### Upstream skill
- [`analyze-requirements`](../analyze-requirements/SKILL.md) — produces input MEMORY + scenario_map + data_catalog
  - [`references/quoting-guide.md`](../analyze-requirements/references/quoting-guide.md) — verbatim Source Quote enables better technique rubric (Part 2 synergy)

### Downstream skills
- [`review-tc`](../review-tc/SKILL.md) — quality gate G1; R1-17 + R2-13/14 + R3-13 checks mode-aware (60 checks total, template ISC 42-cột)
- [`implement-automation`](../implement-automation/SKILL.md) — generates Java code; supports DataProvider pattern cho derived TCs (B1/B2/B6)
- [`review-src-tc`](../review-src-tc/SKILL.md) — compares code vs TC; M4-04 + parameterization allowance
- [`test-report`](../test-report/SKILL.md) — reads Coverage Matrix sheet cho §8 Test Design Technique Coverage
- [`health-check`](../health-check/SKILL.md) — mode-aware C-03 + C-08/C-09 validate technique tags + matrix presence

### Internal references (Tier B techniques, added 2026-05-29)
- [`references/techniques.md`](references/techniques.md) — 8 ISTQB-aligned techniques (B1-B8): EP, BVA, Decision Table, State Transition, Pairwise, Error Guessing, CRUD Matrix, Cause-Effect Graph
- [`references/technique-rubric.md`](references/technique-rubric.md) — auto-detection heuristics (4-dim scenario analysis → applicable techniques)
- [`assets/coverage-matrix-template.md`](assets/coverage-matrix-template.md) — Excel sheet schema cho Coverage Matrix output

