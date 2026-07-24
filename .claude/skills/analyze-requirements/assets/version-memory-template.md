# MEMORY — Analyze Requirements Output — v[VERSION]

> Tạo bởi: skill analyze-requirements
> Cập nhật lần cuối: [date] — [lý do]
> Parent version: v[PARENT] (hoặc "— version đầu tiên")

## 0. Version Context
- **Version:** v[VERSION]
- **Parent:** v[PARENT]
- **Delta type:** [Major / Minor / Hotfix]
- **Input folder:** 00_input/v[VERSION]/
- **Shared docs applied:** [list hoặc "Không"]
- **Analysis mode:** [INIT / DELTA]

## 1. Project Overview
- **Dự án:** [tên]
- **Mô tả:** [2-3 câu]
- **Môi trường:** [DEV/STG/UAT] — URL: [url]

## 2. Document Registry (version-scoped)
| DOC ID | File | Loại | Ngày phân tích | Status | Modules liên quan |
|--------|------|------|---------------|--------|-------------------|

## 3. Module Summary
| Module | DOC Source | Tổng Req | Tổng SC | NEW | MODIFIED | CARRIED | DEPRECATED | P1 | P2 | P3 | Risk Level |
|--------|-----------|----------|---------|-----|----------|---------|-----------|----|----|----|-----------:|

## 4. Scenario Index
| SC ID | Tên ngắn | Module | DOC Source | Priority | Test Type | Lifecycle | TC Status | Vibe Status | Vibe Date |
|-------|----------|--------|-----------|----------|-----------|-----------|-----------|-------------|-----------|

### 4.1. Source Detail (verbatim quotes — mandatory per `references/quoting-guide.md`)

Đặt 1 block per REQ + per SC + per Clarification. Format:

```markdown
#### REQ-[MODULE]-[NNN] / SC-[MODULE]-[NNN] — <tên ngắn>

**Source Quote:**
> "<verbatim text from doc>"

**Source Location:** `<DOC-ID> §<section> · "<heading>" · <paragraph/table/figure ref> · page <N>`

**Analyst Note:** <Vietnamese paraphrase + implicit assumptions + cross-references>
```

**Lifecycle rules:**
- NEW → mandatory full 3 fields.
- MODIFIED → 2 Source Quotes (old + new) + diff trong Analyst Note.
- CARRIED → reference parent: `Source Quote: see v[PARENT] REQ-XXX-NNN`.
- DEPRECATED → keep parent quote + add deprecation reason.
- Implicit requirements → `Source Quote: *(Implicit — no direct quote)*` + derivation trong Analyst Note.

Long quote (>500 chars) → sidecar `02_analyze-requirements/v[VERSION]/quotes/REQ-XXX-NNN.md`, inline first 80 chars + reference.

## 5. Test Data Summary
| Module | DOC Source | Fields chính | Số bộ valid | Số bộ invalid | Có boundary? |
|--------|-----------|-------------|-------------|---------------|-------------|

## 6. Clarifications & Blockers
| # | Req ID | DOC Source | Vấn đề | Answer | Status | Ngày resolve | Ảnh hưởng |
|---|--------|-----------|--------|--------|--------|-------------|-----------|

### 6.1. Clarification Source Detail (per `references/quoting-guide.md` EC6)

Đặt 1 block per Clarification. Quote exact ambiguous text từ doc gốc:

```markdown
#### C<N> — <topic>

**Source Quote (ambiguous):**
> "<verbatim ambiguous text>"

**Source Location:** `<DOC-ID> §<section> · paragraph N · page <N>`

**Analyst Note:** <giải thích ambiguity + proposed resolution>
```

## 7. Automation Context (nếu có)
- **Framework:** [Java 21 + TestNG 7 + Selenium 4 + Maven]
- **POM path:** [src/main/java/page/]
- **Naming convention:** [buttonLogin, textBoxEmail, popupError, labelTitle]

## 8. Deliverable Files Reference
| File | Đường dẫn | Mô tả |
|------|-----------|-------|
| Requirement Traceability | `02_.../v[VERSION]/requirement_traceability.md` | Ma trận truy vết |
| Test Scenario Map | `02_.../v[VERSION]/test_scenario_map.md` | Chi tiết scenarios |
| Test Data Catalog | `02_.../v[VERSION]/test_data_catalog.md` | Dữ liệu test |
| Risk Assessment | `02_.../v[VERSION]/risk_assessment.md` | Đánh giá rủi ro |

## 9. TC Generation Log
> Header khớp generate-tc (Mode + Techniques cols, added 2026-05-29). Mode ∈ standard/comprehensive/selective; Techniques = N/A (standard) hoặc danh sách B-ID (B1..B8). Priority = breakdown P1/P2/P3 (generate-tc ghi); Review Status (review-tc ghi: ⏳/✅/score).

| DOC ID | Ngày generate | Tổng TC | File output | Priority | Mode | Techniques | Review Status |
|--------|--------------|---------|-------------|----------|------|------------|---------------|
