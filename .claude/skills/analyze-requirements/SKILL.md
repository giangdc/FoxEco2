---
name: analyze-requirements
description: Phân tích tài liệu yêu cầu (URD, SRS, specs, user stories) trong 00_input/, tạo scenario map, requirement traceability, test data catalog, risk assessment, version-aware MASTER-MEMORY. Enforces mandatory verbatim quoting per requirement/scenario/clarification — 3-field structure: Source Quote (verbatim từ doc, blockquote) + Source Location (DOC-ID §section · paragraph · page) + Analyst Note (paraphrase). Mục đích: text-level traceability để reviewer/QA-lead verify analyze result vs tài liệu gốc mà không phải đọc hết doc. Opt-out qua --no-quote flag (legacy migration only). Use when user mentions "phân tích yêu cầu", "analyze requirements", "đọc SRS", "đọc URD", "tạo scenario", "review specs", "delta analysis", "phân tích version mới", "verbatim quote", "source quote", "source location", "trích dẫn nguyên văn", "traceability", "verify requirement vs document", "completeness sweep", "coverage gap", "tìm requirement bỏ sót", "rà lượt 2", or runs /analyze-requirements command (alias /analyze) (including /analyze-requirements --sweep).
license: Proprietary — FPT QA Toolkit v1.0 (qc-claude-v1)
compatibility: Designed for Claude Code QA projects with 00_..11_ folder structure (qc-claude-v1). Requires Claude Code or compatible agent runtime với file read/write capability.
metadata:
  toolkit: qc-claude-v1
  pipeline-position: "3"
  status-section: MASTER-MEMORY-section-8
  owner: QC Team
  version: "1.0"
  released: "2026-06-05"
---

# Analyze Requirements

Đọc tài liệu requirement từ `00_input/[version]/`, tạo deliverables trong `02_analyze-requirements/[version]/`.

## Command

| Command | Mode | Mô tả |
|---------|------|-------|
| `/analyze-requirements --init @path` | INIT | Phân tích lần đầu |
| `/analyze-requirements --delta --version vX.Y @path` | DELTA | Phân tích version mới (so sánh parent) |
| `/analyze-requirements --update "feedback"` | UPDATE | Cập nhật từ feedback BA/dev |
| `/analyze-requirements --review` | REVIEW | Xem tổng quan, không sửa file |
| `/analyze-requirements --sweep` | SWEEP | Completeness sweep — rà lượt 2 tìm requirement bỏ sót khỏi REQ inventory (văn xuôi: nguyên tắc, quy ước, NFR…). Chỉ phát hiện, không sửa. |
| `/analyze-requirements --migrate` | MIGRATE | Chuyển flat → multi-version structure |
| `/analyze-requirements` | AUTO | Auto-detect mode từ context |
| `/analyze-requirements --help` | HELP | Hiển thị command table (file này) + exit |

**Options:** `--version vX.Y` · `--figma "url"` · `--dry-run` · `--doc DOC-vX.Y-NN` (SWEEP: lọc 1 doc) · `--no-quote` (opt-out verbatim quoting, legacy migration only — default ON)

## Prerequisites

| Cần có | Check |
|--------|-------|
| `CLAUDE.md` | tại root project |
| Docs trong `00_input/[version]/` | ít nhất 1 file |
| `PIPELINE.md` (optional) | đọc để check upstream `create-test-plan` status |
| `Project_rule.md` block `## DOC Notation` (optional) | đọc `req_notation` — ký hiệu requirement của DOC dự án (sinh bởi `/init-project` Q11) |

## Pipeline Position

```
create-test-plan → ★ analyze-requirements ★ → generate-tc → review-tc → vibe-test → implement-automation
```

- **Folder sở hữu (GHI):** `02_analyze-requirements/`
- **Đọc từ:** `00_input/[version]/`, `01_test-plans/`
- **Downstream skills đọc:** `generate-tc`, `implement-automation`, `review-tc`, `vibe-test`

## Mode Routing

> Claude: xác định mode → load `references/[mode].md` tương ứng. KHÔNG đọc tất cả mode files cùng lúc (progressive disclosure).

| Condition | → Load file |
|-----------|-------------|
| `--init` HOẶC chưa có `MASTER-MEMORY.md` | [references/init.md](references/init.md) |
| `--delta` HOẶC có `MASTER-MEMORY` + nhắc version mới | [references/delta.md](references/delta.md) |
| `--update` HOẶC nhắc sửa/feedback/thêm/xóa + SC ID/module | [references/update.md](references/update.md) |
| `--review` HOẶC nhắc xem/tổng quan/so sánh | [references/review.md](references/review.md) |
| `--sweep` HOẶC nhắc "completeness sweep", "tìm requirement bỏ sót", "coverage gap", "rà lượt 2" | [references/sweep.md](references/sweep.md) |
| `--migrate` HOẶC nhắc chuyển cấu trúc (flat → multi-version) | [references/migrate.md](references/migrate.md) |
| Có `MEMORY.md` flat cũ (không version folder) | Suggest `--migrate` to user |
| `--help` flag | Print this Command table + exit (no mode load) |
| Không rõ ý định | Hỏi user: "Bạn muốn phân tích mới, cập nhật, hay xem tổng quan?" |

## Templates (assets/)

Mode files reference these templates khi tạo output:

- [assets/master-memory-template.md](assets/master-memory-template.md) — Cross-version registry → `MASTER-MEMORY.md`
- [assets/version-memory-template.md](assets/version-memory-template.md) — Per-version MEMORY (§4.1 + §6.1 Source Detail) → `[version]/MEMORY.md`
- [assets/scenario-map-template.md](assets/scenario-map-template.md) — Given/When/Then map → `[version]/test_scenario_map.md`
- [assets/requirement-traceability-template.md](assets/requirement-traceability-template.md) — REQ↔DOC↔SC matrix → `[version]/requirement_traceability.md`
- [assets/test-data-catalog-template.md](assets/test-data-catalog-template.md) — Test data valid/invalid/boundary → `[version]/test_data_catalog.md`
- [assets/risk-assessment-template.md](assets/risk-assessment-template.md) — Risk (bảng hợp nhất 1 dạng) → `[version]/risk_assessment.md`
- [assets/coverage-gap-report-template.md](assets/coverage-gap-report-template.md) — SWEEP output (gap A/B/C/D) → `[version]/coverage-gap-report.md`

### Deliverable ↔ Template Registry (structure-lock)
| Deliverable | Template asset (BẮT BUỘC dùng) |
|-------------|--------------------------------|
| `MASTER-MEMORY.md` | `master-memory-template.md` |
| `[version]/MEMORY.md` | `version-memory-template.md` |
| `[version]/test_scenario_map.md` | `scenario-map-template.md` |
| `[version]/requirement_traceability.md` | `requirement-traceability-template.md` |
| `[version]/test_data_catalog.md` | `test-data-catalog-template.md` |
| `[version]/risk_assessment.md` | `risk-assessment-template.md` |
| `[version]/coverage-gap-report.md` (SWEEP) | `coverage-gap-report-template.md` |

## References

- [references/init.md](references/init.md) — INIT mode workflow
- [references/delta.md](references/delta.md) — DELTA mode (version update)
- [references/update.md](references/update.md) — UPDATE mode (feedback application)
- [references/review.md](references/review.md) — REVIEW mode (summary only, no writes)
- [references/migrate.md](references/migrate.md) — MIGRATE mode (flat → multi-version)
- [references/sweep.md](references/sweep.md) — **SWEEP mode** (completeness sweep — detect requirement bỏ sót, phân loại A/B/C/D, chỉ phát hiện không sửa)
- [references/quoting-guide.md](references/quoting-guide.md) — **Verbatim quoting rules** (3-field structure, edge cases, anti-patterns) — mandatory reading khi áp dụng rule

## Nguyên tắc cốt lõi (áp dụng tất cả modes)

1. **Chỉ phân tích, không tạo code.** Output là markdown files trong `02_analyze-requirements/`.
2. **Traceability bắt buộc — 2 levels:**
   - **ID-level:** Mọi scenario trace ngược về REQ ID + DOC Source.
   - **Text-level (NEW 2026-05-29):** Mỗi REQ + SC + Clarification có 3 fields tách biệt: **Source Quote** (verbatim từ doc) + **Source Location** (`<DOC-ID> §<section> · ref · page`) + **Analyst Note** (paraphrase + implicit assumptions). Mục đích: reviewer verify analyze result vs doc gốc không phải đọc hết. Mandatory default; opt-out qua `--no-quote`. Xem [references/quoting-guide.md](references/quoting-guide.md).
3. **Viết tiếng Việt**, giữ tiếng Anh cho thuật ngữ kỹ thuật (e.g., REST, JSON, OAuth). Source Quote PHẢI verbatim — không dịch.
4. **KHÔNG sáng tạo scenario ngoài requirement.** Mơ hồ → ghi vào Clarifications list (với Source Quote ambiguous text), KHÔNG đoán.
5. **Version-aware.** DOC ID prefix version (`DOC-vX.Y-NN`). Output vào folder version cụ thể.
6. **Structure-lock (NEW 2026-06-02 — đảm bảo output đồng nhất mọi session/máy).** Mọi deliverable PHẢI theo ĐÚNG section + header cột của asset template tương ứng (xem "Deliverable ↔ Template Registry"). KHÔNG tự thêm/bớt/đổi tên cột, KHÔNG đổi thứ tự section, KHÔNG dùng nhiều dạng bảng khác nhau cho cùng loại nội dung (vd risk_assessment chỉ 1 dạng bảng cho mọi module). Nếu thực sự cần cột/section mới → cập nhật asset template TRƯỚC rồi mới áp dụng (để lần chạy sau vẫn nhất quán). Đọc template tương ứng trước khi tạo/ghi mỗi file.
7. **Req notation per-project (NEW 2026-06-05 — chống bịa ID).** Trước khi phân tích, đọc `req_notation` từ block `## DOC Notation` trong `Project_rule.md` (sinh bởi `/init-project` Q11) → dùng ĐÚNG ký hiệu đó cho cột `Maps (Ref DOC)` (traceability) và cột `Nguồn` (test-data-catalog):
   - `FR/VR` / `AC` / `UC` / `US-key` → trích đúng ID có thật trong doc theo ký hiệu đó.
   - `none` → doc không đánh số: để `—` ở cột Maps, traceability dựa vào `DOC-ID §section`.
   - `auto` hoặc thiếu block → **tự phát hiện** ký hiệu từ doc ở lần đọc đầu, rồi **GHI NGƯỢC** giá trị thật vào block `## DOC Notation` (tạo block nếu chưa có) để các lần chạy sau nhất quán.
   - **TUYỆT ĐỐI KHÔNG tự bịa số FR/VR/AC** khi doc không có — fallback luôn là `§section`.

## Status Protocol

Mỗi mode invocation phải:

- **Bắt đầu:** Ghi `MASTER-MEMORY §8 Pipeline Status` = `IN_PROGRESS` cho skill này
- **Kết thúc thành công:** Ghi `= COMPLETED` + cập nhật Last Run, Scope, Output, Notes
- **Hoàn thành 1 phần:** Ghi `= PARTIAL` (e.g., analyze 2/3 modules)
- **Lỗi/abort:** Ghi `= FAILED` + Notes mô tả lỗi
- **Nếu UPDATE sửa scenario:** Cảnh báo user reset downstream status (`generate-tc`, `review-tc`, `implement-automation`)

## Examples

### Example 1: Init analyze cho dự án mới

**Input:**
```
/analyze-requirements --init @00_input/v1.0/
```

**Behavior:**
1. Đọc CLAUDE.md, scan 00_input/v1.0/
2. Hỏi user version (default v1.0), Figma link
3. Phân rã: Module → Feature → Requirement → Scenario
4. Tạo 5 files trong `02_analyze-requirements/v1.0/`:
   - `MEMORY.md` (per-version)
   - `requirement_traceability.md`
   - `test_scenario_map.md`
   - `test_data_catalog.md`
   - `risk_assessment.md`
5. Tạo `MASTER-MEMORY.md` (cross-version registry) nếu chưa có
6. Ghi §8 Pipeline Status = COMPLETED

**Output preview:**
```
✅ Analyze v1.0 hoàn tất:
   - 55 requirements identified
   - 57 scenarios extracted (45 functional + 12 UI)
   - 11 clarifications cần BA confirm
   - Risk: 3 modules High, 5 Medium

Next: /generate-tc để tạo Test Case Excel
```

### Example 2: Delta analyze cho version mới

**Input:**
```
/analyze-requirements --delta --version v2.0 @00_input/v2.0/
```

**Behavior:**
1. Đọc MASTER-MEMORY.md → parent version v1.0
2. Đọc v1.0 scenarios (CARRIED baseline)
3. Đọc 00_input/v2.0/ docs mới
4. So sánh:
   - REQ mới → NEW scenarios
   - REQ sửa → MODIFIED scenarios
   - REQ giữ nguyên → CARRIED (reference only)
   - REQ xóa → DEPRECATED
5. Update MASTER-MEMORY §3 Lifecycle + §4 Regression Scope

**Output preview:**
```
✅ Delta v2.0 hoàn tất:
   - NEW: 12 scenarios
   - MODIFIED: 3 scenarios (từ v1.0)
   - CARRIED: 15 scenarios (reference)
   - DEPRECATED: 7 scenarios (removed in v2.0)
```

### Example 3: Update from feedback

**Input:**
```
/analyze-requirements --update "BA confirm OTP expire sau 5 phút, không phải 10"
```

**Behavior:**
1. Detect target SC ID via natural language → SC-AUTH-007 (OTP scenario)
2. Update `test_scenario_map.md` + `test_data_catalog.md`
3. Resolve clarification trong `requirement_traceability.md`
4. Cảnh báo downstream impact: TC-AUTH-007 cần regenerate

**Output preview:**
```
✅ Update applied to SC-AUTH-007 + clarification CL-AUTH-003 resolved.
⚠️ Downstream impact:
   - generate-tc: TC-AUTH-007 cần regenerate (5min thay 10min)
   - review-tc: review cũ không còn valid

Reset downstream status? (Y/N)
```

### Example 4: Completeness sweep

**Input:**
```
/analyze-requirements --sweep --version v1.0
```

**Behavior:**
1. Đọc REQ inventory hiện có (MEMORY §4.1 + traceability) làm diff base.
2. Fan-out 1 agent/doc (lens completeness-critic) quét TOÀN VĂN từng § → liệt kê atomic statements.
3. Diff vs REQ inventory → phân loại UNCOVERED (A Functional / B NFR / C Out-of-scope / D Descriptive).
4. Tạo `coverage-gap-report.md`. KHÔNG tự sửa — route fix qua UPDATE + generate-tc.

**Output preview:**
```
📊 Completeness Sweep v1.0:
   Atomic statements: 142 | COVERED: 130 | UNCOVERED A=4 B=3 C=8 D=-
   Gap actionable (A+B): 7 → xem coverage-gap-report.md
```

## Common Edge Cases

| Scenario | Handling |
|----------|----------|
| `00_input/[version]/` rỗng hoặc không tồn tại | Hỏi user upload docs trước, exit gracefully |
| SWEEP nhưng chưa INIT (không có REQ inventory) | Báo user chạy `/analyze-requirements --init` trước (cần diff base), exit |
| SWEEP tìm 0 gap actionable | Output "🟢 Không gap A/B" — coverage tốt; vẫn ghi report C/D đã xét |
| `MASTER-MEMORY.md` không tồn tại | Auto chọn Mode INIT |
| Có file `MEMORY.md` flat (legacy structure) | Suggest `/analyze-requirements --migrate` thay vì init |
| Multiple docs cùng module nhưng conflict | Ghi vào clarifications list, ưu tiên doc gần nhất (date-based) |
| Docs là PDF/binary không readable | Hỏi user convert sang markdown/docx hoặc skip file |
| Figma link cần auth | Báo user authenticate MCP server trước |
| Active version trong MASTER-MEMORY conflict với `--version` flag | Flag override, log warning |
| Scenario count vượt quá 200 trong 1 version | Hỏi user split thành sub-modules hoặc giảm scope |
| Clarification > 20 items chưa resolve | Suggest user resolve trước khi tiếp generate-tc |
| Version DOC ID format sai (không có `vX.Y`) | Auto-prefix + log warning to user |

## See Also

### Pipeline references
- [PIPELINE.md](../../PIPELINE.md) — Skill registry + prerequisites matrix + §6 Mode Quick-Reference
- [COMMANDS.md](../../COMMANDS.md) — Cheat sheet với `--no-quote` flag syntax

### Upstream skill
- [`create-test-plan`](../create-test-plan/SKILL.md) — drafts Test Plan §2 Scope + §4 Exit Criteria; pre-analyze
- [`fetch-us`](../fetch-us/SKILL.md) — pulls Jira user stories vào `00_input/` (utility, optional)

### Downstream skills (consume MEMORY + scenario_map + Source Detail blocks)
- [`generate-tc`](../generate-tc/SKILL.md) — uses Source Quote text (Part 2) cho technique rubric detection (more reliable hơn paraphrase)
- [`review-tc`](../review-tc/SKILL.md) — R3-13 check TC drift vs Source Quote (mode-aware)
- [`implement-automation`](../implement-automation/SKILL.md) — supplementary context khi resolve ambiguity prefer Source Quote
- [`health-check`](../health-check/SKILL.md) — F-05 + F-06 validate Source Detail blocks presence

### Internal references (verbatim quoting, added 2026-05-29)
- [`references/quoting-guide.md`](references/quoting-guide.md) — **mandatory reading** — full ruleset cho 3-field structure (Source Quote + Source Location + Analyst Note), 6 edge cases (multi-language, table/figure, implicit, multi-source, scenario quote, clarification quote), anti-patterns, generic examples (project-agnostic)
- [`references/init.md`](references/init.md) — INIT mode workflow with embedded quoting rule
- [`references/delta.md`](references/delta.md) — DELTA mode (NEW/MODIFIED/CARRIED/DEPRECATED quote handling)
- [`assets/version-memory-template.md`](assets/version-memory-template.md) — §4.1 Source Detail block per REQ/SC + §6.1 Clarification Source Detail
- [`assets/scenario-map-template.md`](assets/scenario-map-template.md) — per-scenario Source Detail block dưới main table
