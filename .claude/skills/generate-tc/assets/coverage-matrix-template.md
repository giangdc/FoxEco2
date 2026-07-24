# Coverage Matrix Sheet Template

> Generated khi `/generate-tc --mode comprehensive` hoặc `--techniques` flag active. Output: 1 sheet `Coverage Matrix` thêm vào TC-MASTER Excel (workbook template ISC — sheet phụ, không thuộc bộ 9 sheet chuẩn Cover/Guideline/Revision History/Summary/Dashboard/Report Test/Bug Data/RTM/Test Cases×N).

## Sheet name
`Coverage Matrix`

## Purpose
Visual heat-map cho stakeholders thấy mỗi scenario được cover bằng những kỹ thuật nào, technique nào N/A (và lý do). Reviewer dễ phát hiện gap.

## Schema (13 columns)

| Col | Field | Width | Type | Nội dung |
|---|---|---:|---|---|
| A | SC ID | 16 | text | `SC-[MODULE]-[NNN]` |
| B | Scenario Title | 40 | text | Tên ngắn scenario (copy từ scenario-map) |
| C | Source Hint | 50 | text | First 80 chars Source Quote (truncate) + `…` (link sang verbatim trong scenario-map nếu Part 2 enabled) |
| D | B1 EP | 10 | text | `✅ N` (N TCs generated) · `N/A: <reason>` · trống nếu chưa run |
| E | B2 BVA | 10 | text | Same format |
| F | B3 DT | 10 | text | Same format |
| G | B4 ST | 10 | text | Same format |
| H | B5 PW | 10 | text | Same format |
| I | B6 EG | 10 | text | Same format |
| J | B7 CRUD | 10 | text | Same format |
| K | B8 CEG | 10 | text | Same format |
| L | Total TCs | 10 | number | Sum TCs derived from scenario across techniques |
| M | Coverage % | 10 | percent | `(techniques applied count) / (techniques applicable count) × 100%` |

Note: 8 technique columns (D-K) = exactly cols B1-B8 từ `techniques.md`. Order phải match.

## Cell value conventions

| Value | Meaning |
|---|---|
| `✅ N` | Technique applied, N TCs generated (e.g., `✅ 6`) |
| `N/A: <short reason>` | Technique not applicable (e.g., `N/A: no input field`, `N/A: single condition`) |
| `❌ skipped: <reason>` | User explicit skip (e.g., `❌ skipped: out of scope sprint`) |
| trống | Not yet decided (rubric chưa chạy) |

## Formatting rules

- **Header row (1):** bold, fill `#4472C4`, font white, freeze.
- **Alternating rows:** `#D9E2F3` / white.
- **Conditional formatting cho cols D-K:**
  - `✅ <N>` cell → green background `#C6EFCE`
  - `N/A: …` cell → grey background `#D9D9D9`
  - `❌ skipped: …` cell → red background `#FFC7CE`
  - trống → no fill
- **Col M (Coverage %):**
  - ≥80% → green
  - 50-79% → yellow `#FFEB9C`
  - <50% → red `#FFC7CE`
- **Auto-filter:** ON cho header row.
- **Text wrap:** ON cho cols B + C.

## Summary footer rows (after last SC row)

```
Total scenarios: <N>
Total TCs derived: <SUM col L>
Average coverage %: <AVG col M>
Most-applied technique: <max count col D-K>
Least-applied technique: <min count col D-K>
```

## Sample 4 rows (generic project-agnostic)

| SC ID | Scenario Title | Source Hint | B1 EP | B2 BVA | B3 DT | B4 ST | B5 PW | B6 EG | B7 CRUD | B8 CEG | Total | Coverage % |
|---|---|---|---|---|---|---|---|---|---|---|---:|---:|
| SC-LOGIN-001 | User SSO authenticates | "User must authenticate via cor…" | ✅ 4 | ✅ 6 | N/A: single condition | N/A: no state | N/A: <3 params | ✅ 20 | N/A: not CRUD | N/A: B3 escalation | 30 | 100% (3/3) |
| SC-LIST-001 | Paginated record list | "User browses paginated list of…" | ✅ 3 | ✅ 6 | N/A | N/A | N/A: 2 params | N/A: no free-text | N/A: read-only | N/A | 9 | 100% (2/2) |
| SC-LOAN-001 | Loan approval decision | "Approval = (credit AND income…" | N/A | N/A | ❌ skipped: see B8 | N/A | N/A | N/A | N/A | ✅ 6 | 6 | 100% (1/1) |
| SC-DRAFT-001 | Document wizard 5-step | "Document goes through 5-step w…" | N/A | N/A | N/A | ✅ 12 | N/A | N/A | N/A | N/A | 12 | 100% (1/1) |

## Integration notes

### With Part 2 verbatim quoting

Cột C (`Source Hint`) **link tới** verbatim quote nếu `/analyze-requirements` Part 2 enabled:
- Format: `<first 80 chars>… [→]` với link sang scenario-map.md anchor `#SC-MODULE-NNN`.
- Nếu Part 2 disabled (no Source Quote available): use scenario title từ scenario-map main table.

### With TC main sheets

Mỗi TC trong main module sheets (template ISC) có `Technique: <tag>` trong **Remark column (AP, cột 42)** — template ISC không có cột Notes riêng. Coverage Matrix là roll-up summary. Lưu ý Remark cũng dùng chung cho execution remarks sau này — downstream skill khi ghi Remark phải nối thêm, không ghi đè (xem `references/generate.md` Step 3a).

### Backward compat

- Sheet **chỉ generate** khi `--mode comprehensive` hoặc `--techniques` flag active.
- Standard mode (no flag) → sheet KHÔNG appear. Existing TC-MASTER unchanged.
- Sheet này KHÔNG thuộc bộ 9 sheet chuẩn của template ISC (Cover/Guideline/Revision History/Summary/Dashboard/Report Test/Bug Data/RTM/Test Cases×N) — là phụ lục kỹ thuật nội bộ, giữ nguyên khi copy vào TC-MASTER (xem `references/consolidate.md`).

## Cross-references

- Techniques definitions: `~/.claude/skills/generate-tc/references/techniques.md`
- Rubric: `~/.claude/skills/generate-tc/references/technique-rubric.md`
- TC main sheet structure: `references/generate.md` §"TC Structure — 42 cột theo template ISC"
