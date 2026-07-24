# Technique Rubric — Auto-detection cho generate-tc

> Load khi `/generate-tc --mode comprehensive` hoặc `--techniques X,Y,Z` flag active. Default invocation does NOT load — preserves backward-compat.

Skill phân tích mỗi scenario theo 4 dimensions (#inputs, #states, #conditions, #parameters) → output list applicable techniques. Reviewer/user approve hoặc reject từng technique trước khi generate. Source: scenario text + verbatim Source Quote (if Part 2 verbatim quoting enabled).

---

## Decision matrix

| Scenario property | Detection rule (search trong Given/When/Then + Source Quote) | Technique applicable |
|---|---|---|
| Input field domain **discrete** (enum, role, category) | Keywords: `∈ {…}`, `role: …`, `type: …`, `chọn 1 trong …`, `accepted values: …`, `one of` | **B1 EP** |
| Numeric range / date range / length constraint | Keywords: `min`, `max`, `≥`, `≤`, `between X and Y`, `length N..M`, `from X to Y` | **B2 BVA** |
| ≥2 binary conditions ảnh hưởng output | Count `if X and Y`, `nếu A và B`, `provided that …`, multiple `must`/`shall` clauses linked với AND/OR | **B3 DT** |
| Explicit state lifecycle | Keywords: `pending`, `active`, `draft`, `submitted`, `approved`, `closed`, `state transition`, lifecycle nouns + verbs (`submit`, `approve`, `revert`) | **B4 ST** |
| ≥3 multiplicative parameters | Count distinct selectable params trong When (vd `period × service × channel × region`), `combination of`, `cross-product` | **B5 PW** |
| **Any** user-input field | Trivially true if scenario có text/number/file/paste input từ user | **B6 EG** (always) |
| Persistent entity CRUD ops | Verbs: `create`, `save`, `delete`, `update`, `list`, `search`, `tạo mới`, `lưu`, `xóa`, `quản lý preset/profile/list/preferences` | **B7 CRUD** |
| Complex multi-output logic | Auto-escalate from **B3** khi truth-table rules >16, hoặc manual flag bởi user khi scenario có ≥4 causes + ≥2 effects với non-trivial logical relationships | **B8 CEG** |

---

## Rubric output format

Khi mode active, skill chạy rubric per scenario và present user trước generate:

```
🔍 Rubric output for SC-LOGIN-001:

  Scenario: "User authenticates via SSO with email/password credentials"

  4-dimension analysis:
    • Inputs detected: 2 (email field, password field)
    • States detected: 0
    • Conditions detected: 0
    • Parameters detected: 0

  Applicable techniques:
    ✓ B1 EP — email domain partition (valid/invalid format), password presence
    ✓ B2 BVA — password length boundary (if min/max specified)
    ✓ B6 EG — 10-pattern checklist per field (email + password)

  Not applicable:
    ✗ B3 DT — single condition (auth success)
    ✗ B4 ST — no state lifecycle in this scenario
    ✗ B5 PW — fewer than 3 multiplicative params
    ✗ B7 CRUD — not entity CRUD
    ✗ B8 CEG — only DT escalation, N/A here

  Estimated TC count: 4 (EP) + 6 (BVA password) + 10 (EG email) + 10 (EG password) = ~30 TCs

  Proceed? (y/n/edit)
```

User có thể edit: remove technique không muốn apply, add manual technique flag.

---

## Sample rubric outputs (5 mock scenarios)

### Sample 1: Login form

**Scenario:** "User authenticates via SSO with email/password credentials"

| Dim | Detection |
|---|---|
| Inputs | 2 (email, password) |
| States | 0 |
| Conditions | 0 |
| Parameters | 0 |

**Applicable:** B1 (email domain), B2 (password length if spec'd), B6 (per field × 10 patterns).
**TC estimate:** ~26-30 TCs (vs 1 trong standard mode).

### Sample 2: Pagination list

**Scenario:** "User browses paginated list of records, 20 per page, with sort by date/name/size"

| Dim | Detection |
|---|---|
| Inputs | 1 (page number) |
| States | 0 |
| Conditions | 0 |
| Parameters | 2 (page × sort_field) |

**Applicable:** B2 (page boundary: 0, 1, last, last+1, negative, very large), B1 (sort_field enum: date/name/size — 3 partitions).
**Not applicable:** B5 (only 2 params, threshold ≥3), B6 (page number không phải user free-text), B7 (read-only listing).
**TC estimate:** ~9 TCs.

### Sample 3: Role-based view

**Scenario:** "Dashboard shows different widgets based on user role: admin/editor/viewer/guest"

| Dim | Detection |
|---|---|
| Inputs | 0 (role from session, not user-typed) |
| States | 0 |
| Conditions | 1 (role check) |
| Parameters | 0 |

**Applicable:** B1 (4 valid partitions + invalid like null/unknown).
**Not applicable:** B2 (no range), B3 (single condition), B4 (no lifecycle), B5 (single param), B6 (no user input), B7 (no CRUD).
**TC estimate:** ~6 TCs (4 valid + 2 invalid).

### Sample 4: Document wizard flow

**Scenario:** "Document goes through 5-step wizard: draft → submit → review → approve → publish. Each step has Back button (except first)."

| Dim | Detection |
|---|---|
| Inputs | 0 |
| States | 5 (draft/submit/review/approve/published) |
| Conditions | 1 (back button availability) |
| Parameters | 0 |

**Applicable:** B4 (4 valid transitions forward + 4 back; invalid: skip-step, reverse-from-terminal).
**Not applicable:** B1/B2 (no input domain), B3 (only 1 condition), B5/B6/B7.
**TC estimate:** ~12 TCs (4 forward + 3 back + 5 invalid).

### Sample 5: Search filter

**Scenario:** "Search records by: query string (free text), date range (from/to), category (enum 5 values), status (enum 3 values)"

| Dim | Detection |
|---|---|
| Inputs | 1 (query string — free text) |
| States | 0 |
| Conditions | 0 |
| Parameters | 4 (date_from × date_to × category × status) — query là free-text Input cho B6, không tính param nhân |

**Applicable:** B1 (category enum × status enum partitions), B2 (date range boundary), B5 (4 params — pairwise reduce), B6 (query field free-text → 10-pattern).
**Not applicable:** B3 (no conditional logic), B4 (no state), B7 (search read-only — unless saved-search CRUD).
**TC estimate:** ~30-40 TCs (B1: 8, B2: 6, B5: 12, B6: 10).

---

## Edge cases trong rubric

| Edge case | Handling |
|---|---|
| Scenario có 0 dimensions detected | Hiếm: vì B6 EG áp cho MỌI field input (xem Decision matrix), scenario có bất kỳ input nào KHÔNG phải 0-dim. Chỉ hạ về 1-1 khi thật sự 0 input + 0 state + 0 condition + 0 param. **PHẢI log** ở Remark column: `Technique: N/A — 0-dim (no input/state/condition/param)`. |
| Multiple techniques generate same TC variant | Dedupe **chỉ khi trùng CHÍNH XÁC** (cùng input + cùng expected). KHÔNG dùng dedupe để gộp output khác nhau giữa các technique. Tag primary, Remark mention secondary, **log số TC đã dedupe**. |
| Source Quote (Part 2) reveals dimension that paraphrase missed | Re-run rubric using Source Quote text (verbatim) — typically catches edge cases analyst paraphrased away. |
| User overrides rubric (force apply / force skip) | Honor user choice. Document in Remark column: `Technique: <X> (user-forced)` hoặc `Technique: <X> · N/A: user-skipped`. |
| Rubric output >50 TCs per single scenario | **Cảnh báo user + yêu cầu user quyết định** (giảm param values / chọn pattern bỏ). AI **KHÔNG tự ý** skip pattern; pattern bị bỏ phải do user chỉ định + log `user-skipped`. |
| Non-interactive run (không có user để confirm rubric) | Auto-apply TẤT CẢ technique applicable theo rubric — KHÔNG hạ về standard. Log tập auto-apply (Coverage Matrix + Remark `(auto)`) + nêu summary cuối để review. |
| Cross-technique conflict (vd EP partition value violates BVA boundary) | Allow — they're orthogonal. Each TC carries primary technique tag. |

---

## Integration với Part 2 verbatim quoting

Khi project áp dụng `/analyze-requirements` Part 2 (verbatim Source Quote), rubric **PREFER** scan Source Quote text vì:

1. Analyst paraphrase có thể strip keywords (vd "user picks 1 trong 4 roles" có thể bị paraphrase thành "user has a role" — mất EP trigger).
2. Source Quote giữ nguyên technical terms (`enum`, `between X and Y`, `if A and B`) — reliable detection.
3. Cross-validate: nếu rubric output từ Source Quote ≠ output từ Given/When/Then, flag inconsistency cho user review (analyst có thể drift).

Implementation: rubric scan `Source Quote` field FIRST, then `Given/When/Then` as fallback. Log source.

---

## Cross-references

- Full technique definitions: `techniques.md`.
- TC structure: `generate.md` Step 3.
- Coverage Matrix output: `assets/coverage-matrix-template.md`.
- Part 2 quoting integration: `~/.claude/skills/analyze-requirements/references/quoting-guide.md`.
