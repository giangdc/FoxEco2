# Test Design Techniques — generate-tc Tier B Reference

> Load this file when `/generate-tc --mode comprehensive` or `--techniques X,Y,Z` flag is active. Default invocation (`/generate-tc` no flag) does NOT load this — preserves backward-compat.

8 ISTQB-aligned test design techniques, project-agnostic. Each section: definition · WHEN apply · procedure · generic example · TC tag · min TC count.

---

## B1 — Equivalence Partitioning (EP)

### Định nghĩa
Chia domain input thành các partition (equivalence class) sao cho mọi value trong cùng partition đều cho behavior giống nhau. Test 1 representative value per partition là đủ — testing more values từ cùng partition không tăng coverage.

### WHEN apply (predicate)
Scenario có input field với **discrete domain** (enum, role, category, type) HOẶC **bounded continuous domain** với rule khác nhau cho từng vùng.

Trigger keywords trong Given/When: `∈ {…}`, `role: …`, `type: …`, `chọn 1 trong …`, `accepted values: …`, `enum`.

### Procedure
1. Identify input field từ scenario.
2. Liệt kê partitions:
   - **Valid partitions**: các vùng input hợp lệ với behavior phân biệt.
   - **Invalid partitions**: các vùng input không hợp lệ (mỗi loại reject 1 partition).
3. Generate 1 TC per partition. Mỗi TC dùng 1 representative value.

### Generic example (project-agnostic)

Scenario: "User role determines dashboard access — role ∈ {admin, editor, viewer, guest}."

Partitions:
- Valid: admin / editor / viewer / guest (4 valid partitions — mỗi role thấy dashboard khác)
- Invalid: null / unknown-role (2 invalid partitions)

→ 6 TC total: TC-DASH-001 (admin sees full) · TC-DASH-002 (editor sees readwrite) · TC-DASH-003 (viewer sees readonly) · TC-DASH-004 (guest sees public) · TC-DASH-005 (null → redirect login) · TC-DASH-006 (unknown role → 403).

### TC tag convention
Remark column: `Technique: EP-<partition-name>` (e.g., `Technique: EP-admin`, `Technique: EP-invalid-null`).

### Min TC count contribution
**K TCs per matching scenario** where K = số partitions identified (typically 3-8 per field).

---

## B2 — Boundary Value Analysis (BVA)

### Định nghĩa
Khi domain có ranges (numeric / date / string length / list size), bugs thường ở **biên**. Test các giá trị tại + xung quanh boundary để bắt off-by-one và range errors.

### WHEN apply (predicate)
Input field có **numeric range** (min..max), **date range**, **string length constraint**, hoặc **collection size limit**.

Trigger keywords: `min`, `max`, `≥`, `≤`, `≥0`, `1..N`, `length 8-32`, `between X and Y`, `phải có ít nhất`, `tối đa`.

### Procedure
1. Identify boundary points: `min`, `max`.
2. Generate 6 TC: `min-1` (just below) · `min` (at lower) · `min+1` (just above) · `max-1` · `max` · `max+1`.
3. Cho string: thêm `empty` (length 0) và `max-length+1` (over).
4. Cho date: thêm `before-earliest-valid`, `after-latest-valid`.

### Generic example (project-agnostic)

Scenario: "Password length must be 8-32 characters."

BVA TCs:
- TC-PWD-001: length 7 → reject (BVA-min-1)
- TC-PWD-002: length 8 → accept (BVA-min)
- TC-PWD-003: length 9 → accept (BVA-min+1)
- TC-PWD-004: length 31 → accept (BVA-max-1)
- TC-PWD-005: length 32 → accept (BVA-max)
- TC-PWD-006: length 33 → reject (BVA-max+1)
- TC-PWD-007: length 0 (empty) → reject (BVA-empty)

→ 7 TC total.

### TC tag convention
Remark column: `Technique: BVA-<boundary-name>` (e.g., `Technique: BVA-min-1`, `Technique: BVA-max+1`).

### Min TC count contribution
**6-8 TCs per matching scenario** per range field.

---

## B3 — Decision Table

### Định nghĩa
Khi business logic có nhiều conditions kết hợp → outputs khác nhau, decision table liệt kê tất cả combinations possible (rules). Mỗi rule = 1 TC. Eliminate impossible/redundant rules trước khi generate.

### WHEN apply (predicate)
Scenario có **≥2 binary conditions** ảnh hưởng output, đặc biệt khi output là `if A and B and not C → X else Y else Z`.

Trigger keywords: `if X and Y`, `nếu A và B`, `condition`, `business rule`, multiple `if-else-if`.

### Procedure
1. Identify conditions C₁, C₂, …, Cₙ (binary T/F).
2. Identify actions A₁, A₂, …, Aₘ.
3. Build truth table: 2ⁿ rules.
4. Eliminate impossible rules (vd `logged_in=F and has_permission=T` không thể xảy ra nếu permission đòi hỏi login).
5. Collapse redundant rules (cùng action set → keep 1 representative).
6. 1 TC per remaining rule.

### Generic example (project-agnostic)

Scenario: "User can access resource if: logged in AND has permission AND resource exists."

Truth table:
| Rule | logged_in | has_permission | resource_exists | Action |
|---|---|---|---|---|
| R1 | T | T | T | Show resource |
| R2 | T | T | F | 404 not found |
| R3 | T | F | T | 403 forbidden |
| R4 | T | F | F | 403 (skip 404 check khi đã 403) — collapsible |
| R5 | F | * | * | Redirect login (* = don't care) — collapse to 1 rule |

After collapsing: 4 distinct rules → 4 TCs (TC-ACCESS-001..004).

### TC tag convention
Remark column: `Technique: DT-rule<N>` (e.g., `Technique: DT-rule1` cho rule R1).

### Min TC count contribution
**K TCs** where K = số distinct rules sau collapsing (typically 3-8). Nếu rules > 16 → escalate sang B8 Cause-Effect Graph.

---

## B4 — State Transition

### Định nghĩa
Khi feature có **explicit state machine** (states + transitions), test mỗi valid transition + mỗi invalid attempt từ each state. Bugs thường ở guard conditions hoặc forbidden transitions.

### WHEN apply (predicate)
Scenario có **explicit lifecycle/workflow**: order/cart status, session lifecycle, document approval flow, account state, subscription status.

Trigger keywords: trạng thái `<state1>` → `<state2>`, lifecycle, workflow, status transition, `pending` / `active` / `closed`, `draft` / `submitted` / `approved`.

### Procedure
1. Identify states S = {s₁, s₂, …, sₙ}.
2. Identify valid transitions T = {(s_from, event, s_to)}.
3. Identify invalid transitions (attempt event không hợp lệ tại state).
4. Generate 1 TC per valid transition (verify state change correct).
5. Generate 1 TC per invalid attempt (verify rejection + state unchanged).
6. Optional: 1 TC verify each state's invariant (state visible to user is consistent).

### Generic example (project-agnostic)

Scenario: "Order workflow: draft → submitted → approved → shipped → delivered."

Valid transitions:
- T1: draft → submitted (event: User clicks "Submit")
- T2: submitted → approved (event: Manager approves)
- T3: approved → shipped (event: Warehouse ships)
- T4: shipped → delivered (event: Carrier confirms)

Invalid attempts (sample):
- TC-ORDER-INVALID-001: draft → approved directly (skip submit) → reject
- TC-ORDER-INVALID-002: shipped → draft (revert) → reject
- TC-ORDER-INVALID-003: delivered → shipped → reject (terminal state)

→ 4 valid + 3 invalid = 7 TC minimum.

### TC tag convention
Remark column: `Technique: ST-<from>-<to>` (e.g., `Technique: ST-draft-submitted`) cho valid. `Technique: ST-invalid-<from>-<to>` cho rejected attempts.

### Min TC count contribution
**N+M TCs** where N = valid transitions count, M = invalid attempts count (typically 1-3 invalid per state).

---

## B5 — Pairwise (All-Pairs) Testing

### Định nghĩa
Khi feature có **N parameters** với multiple values, full combinatorial = `|p1| × |p2| × … × |pN|` TC (explosion). Empirical research (NIST) shows hầu hết defects involve interactions của ≤2 parameters. **All-Pairs** generate minimum TC set covers every pair of parameter values ≥1 lần.

### WHEN apply (predicate)
Scenario có **≥3 multiplicative parameters** mà mỗi parameter có ≥2 values.

Trigger keywords: `combination of`, `phối hợp`, `cross-product`, parameters interaction, `OS × Browser × Lang × Resolution`.

### Procedure
1. List N parameters và values: P₁ = {v₁₁, v₁₂, …}, P₂ = {…}, …
2. Compute pairs: for each pair (P_i, P_j), enumerate all value combinations.
3. Use AllPairs algorithm (online tool, e.g. https://www.pairwise.org/ or `allpairs.py`) → output minimum TC set.
4. 1 TC per row in output.
5. Optionally extend nếu specific 3-way combination known critical (vd combination đã từng bug).

### Generic example (project-agnostic)

Scenario: "App must work on: OS × Browser × Language × Resolution."

Parameters:
- OS: {Win10, Win11, macOS}
- Browser: {Chrome, Firefox, Safari, Edge}
- Language: {en, vi, ja}
- Resolution: {1080p, 1440p, 4K, mobile}

Full combinatorial: 3 × 4 × 3 × 4 = **144 TC**. AllPairs output: **~12 TC** vẫn cover mọi pair.

Sample 3 rows:
- TC-COMPAT-001: Win10 + Chrome + en + 1080p
- TC-COMPAT-002: Win10 + Firefox + vi + 1440p
- TC-COMPAT-003: macOS + Safari + en + 4K
- … 9 more rows

### TC tag convention
Remark column: `Technique: PW-row<N>` (e.g., `Technique: PW-row1`).

### Min TC count contribution
**K TCs** where K = output rows từ AllPairs algorithm (typically 10-20× smaller than full combinatorial).

---

## B6 — Error Guessing

### Định nghĩa
Experience-based technique. Tester apply intuition + history of common defects để guess inputs likely cause failures. Đặc biệt useful cho input fields user-facing.

### WHEN apply (predicate)
**Any scenario có user-input field** (text, number, file upload, paste, drag-drop).

Trigger: trivially true if scenario accepts user data.

### Procedure
Apply 10-pattern checklist (+2 optional = 12 rows) per input field. Generate 1 TC per pattern applicable.

### 10-pattern checklist (+2 optional)

| # | Pattern | Test |
|---|---|---|
| 1 | `null` / missing | Field empty, submit |
| 2 | `empty string` (length 0) | "" |
| 3 | `whitespace-only` | " " (spaces/tabs/newlines) |
| 4 | `leading/trailing whitespace` | " value " — auto-trim? |
| 5 | `unicode` (multi-byte) | Emoji 🎉, CJK 测试, accents áéíóú |
| 6 | `very long` (e.g., 10K chars) | Paste huge string |
| 7 | `SQL meta-chars` | `' OR 1=1 --`, `; DROP TABLE` |
| 8 | `XSS meta-chars` | `<script>alert(1)</script>` |
| 9 | `control characters` | `\\0`, `\\n`, `\\r`, `\\t` embedded |
| 10 | `binary paste` | Copy binary file content, paste |
| 11 | (optional) RTL embedded | LTR text với `‫` RTL override |
| 12 | (optional) leading zeros | `007` → preserve or strip? |

### Generic example (project-agnostic)

Scenario: "User enters email at registration form."

Per checklist:
- TC-REG-EG-001: email = null → reject với message
- TC-REG-EG-002: email = "" → reject
- TC-REG-EG-003: email = "   " → reject (whitespace only)
- TC-REG-EG-004: email = " user@example.com " → accept after trim
- TC-REG-EG-005: email = "用户@例子.中国" → accept (IDN support?)
- TC-REG-EG-006: email = 10K-char string → reject (length limit)
- TC-REG-EG-007: email = "user@example.com' OR 1=1 --" → escape, no injection
- TC-REG-EG-008: email = "<script>alert(1)</script>@x.com" → escape, no XSS
- TC-REG-EG-009: email = "user\\n@example.com" → reject newline
- TC-REG-EG-010: email = paste binary → reject

→ 10 TC per input field.

### TC tag convention
Remark column: `Technique: EG-<pattern>` (e.g., `Technique: EG-null`, `Technique: EG-xss`).

### Min TC count contribution
**10 TCs per input field** (some patterns may N/A — document with "N/A: <reason>").

---

## B7 — CRUD Matrix

### Định nghĩa
Cho features quản lý **persistent entity** (database records, user preferences, files), CRUD matrix ensure mọi operation (Create / Read / Update / Delete / List / Search / Bulk) đều có TC. Bugs thường ở less-traveled operations (Bulk, Search edge cases).

### WHEN apply (predicate)
Feature có **persistent entity** với operations user-invokable.

Trigger keywords: `save`, `create`, `delete`, `update`, `list`, `search`, `tạo mới`, `xóa`, `lưu`, persistent verbs.

### Procedure
1. Identify entity (vd User, Order, Filter Preset, Document).
2. Build matrix: entity × {C, R, U, D, L, S, B}.
3. Cho mỗi cell, generate ≥1 happy-path TC + ≥1 edge TC (concurrent, permission, large data).
4. Special focus: Delete + Bulk operations (data integrity).

### CRUD-7 expanded checklist

| Op | Test |
|---|---|
| **Create** | Valid input → entity persisted với correct fields |
| **Read** | Fetch existing entity → all fields returned |
| **Update** | Modify field → persists; concurrent update conflict handled |
| **Delete** | Remove entity → gone from list; cascade dependent records correct |
| **List** | Paginated list returns; sort + filter work |
| **Search** | Query returns matches; partial match; case-insensitive |
| **Bulk** | Multi-select operations (delete N, update N) → all-or-nothing semantics |

### Generic example (project-agnostic)

Scenario: "User can manage saved filter presets."

Matrix:
- TC-PRESET-CRUD-001 (Create): Save new preset → appears in list
- TC-PRESET-CRUD-002 (Read): Open existing preset → fields populate
- TC-PRESET-CRUD-003 (Update): Modify preset → persists; concurrent user sees update
- TC-PRESET-CRUD-004 (Delete): Remove preset → confirm dialog; gone after confirm
- TC-PRESET-CRUD-005 (List): Open preset list → paginated; sort by date works
- TC-PRESET-CRUD-006 (Search): Filter list by name → matches; partial OK
- TC-PRESET-CRUD-007 (Bulk): Multi-select 3 → bulk delete; if 1 fails, transaction rollback

→ 7 TC minimum per entity. Add edge cases per cell (e.g., Delete-last-preset, Create-duplicate-name, Update-while-other-deletes).

### TC tag convention
Remark column: `Technique: CRUD-<op>` (e.g., `Technique: CRUD-Create`, `Technique: CRUD-Bulk`).

### Min TC count contribution
**7 base TCs per entity** + edge cases.

---

## B8 — Cause-Effect Graph (advanced)

### Định nghĩa
Khi business logic quá complex cho Decision Table (>16 rules) hoặc có many-to-many cause-effect relationships, **Cause-Effect Graph** model relationships explicit (causes → intermediate nodes → effects với logical operators AND/OR/NOT). Derived minimum TC set covers all paths from causes to effects.

### WHEN apply (predicate)
- Decision Table B3 đã build nhưng rules > 16, hoặc
- ≥4 causes mapping to ≥2 effects với non-trivial logical relationships.

Trigger: manual escalation from B3 khi truth table phình to.

### Procedure
1. Identify all **causes** (inputs/preconditions).
2. Identify all **effects** (outputs/actions).
3. Draw graph: causes → (optional intermediate nodes) → effects, với operators AND/OR/NOT/XOR.
4. For each effect, identify minimum cause sets sufficient để trigger it.
5. 1 TC per minimum cause set.
6. Add ≥1 TC verify effect NOT triggered khi insufficient causes.

### Generic example (project-agnostic)

Scenario: "Bank loan approval depends on: credit_score ≥ 700, income ≥ $50K, debt_ratio < 30%, no_bankruptcy_5yrs. Approval = (credit + income) AND (debt OR no_bankruptcy). Otherwise reject."

Causes: C1 = credit_score≥700, C2 = income≥50K, C3 = debt_ratio<30%, C4 = no_bankruptcy_5yrs

Effects: E1 = approval, E2 = rejection

Graph:
```
C1 ──┐
     ├── AND ──┐
C2 ──┘         ├── AND ── E1 (approval)
               │
C3 ──┐         │
     ├── OR ───┘
C4 ──┘

NOT(above) → E2 (rejection)
```

Minimum cause sets for E1: {C1, C2, C3} hoặc {C1, C2, C4}.

TCs:
- TC-LOAN-CEG-001 (effect1-path-A): C1 T, C2 T, C3 T, C4 F → approve
- TC-LOAN-CEG-002 (effect1-path-B): C1 T, C2 T, C3 F, C4 T → approve
- TC-LOAN-CEG-003 (effect1-both): C1 T, C2 T, C3 T, C4 T → approve
- TC-LOAN-CEG-004 (effect2-miss-credit): C1 F, C2 T, C3 T, C4 T → reject
- TC-LOAN-CEG-005 (effect2-miss-income): C1 T, C2 F, C3 T, C4 T → reject
- TC-LOAN-CEG-006 (effect2-miss-debt-and-bankruptcy): C1 T, C2 T, C3 F, C4 F → reject

→ 6 TC vs full truth table 2⁴ = 16 rules.

### TC tag convention
Remark column: `Technique: CEG-effect<N>-path<M>` (e.g., `Technique: CEG-effect1-pathA`).

### Min TC count contribution
**K TCs** where K = số minimum cause sets per effect, typically 50-70% smaller than full DT.

---

## Anti-patterns (KHÔNG được làm)

| Anti-pattern | Tại sao sai | Fix |
|---|---|---|
| Apply EP nhưng chỉ 1 valid + 1 invalid TC | Miss multiple invalid partitions (vd null vs empty vs invalid-format) | Identify mọi partition independent |
| BVA chỉ test min + max, skip boundaries ±1 | Off-by-one errors slip past | Always 6 points (min-1/min/min+1/max-1/max/max+1) |
| DT không collapse redundant rules | Bloat TC count, slow execution | Collapse rules cùng action set |
| ST chỉ test valid transitions, skip invalid | Forbidden transitions thường có bug | Always test invalid attempts từ each state |
| Pairwise hand-pick combinations | Miss systematic coverage | Use algorithm/tool, không manual |
| EG checklist không document N/A | Reviewer không biết pattern nào skipped intentional | Mark `Technique: EG-<pattern> · N/A: <reason>` |
| CRUD chỉ test Create + Read, skip Delete | Data integrity bugs lurk | All 7 operations mandatory |
| CEG skip "effect not triggered" TC | False-positive untested | ≥1 negative TC per effect |
| Force-apply 1 technique mà rubric đã đánh **N/A** cho scenario đó | Bloat without value | Comprehensive = apply ĐÚNG tập rubric đánh `applicable`: KHÔNG thừa (không ép technique N/A), KHÔNG thiếu (không bỏ technique applicable). "Applicable" do rubric quyết, KHÔNG phải tự cắt cho gọn |

---

## Cross-references

- Pre-generation decision flow: see `technique-rubric.md` (which technique applies to which scenario).
- TC structure (42 columns, template ISC): see `generate.md` §"TC Structure — 42 cột theo template ISC".
- Coverage Matrix sheet output: see `assets/coverage-matrix-template.md`.
- Source Quote integration (Part 2): rubric scans verbatim quote keywords for technique trigger detection — reliable hơn analyst paraphrase.

## Out-of-scope (deferred)

- **Property-based testing** (QuickCheck-style) — generates random inputs from spec. Defer.
- **Model-based testing** (model → auto-generated TCs) — needs formal spec. Defer.
- **Mutation testing** (introduce bugs to verify tests catch them) — meta-testing, defer.
- **Fuzz testing** — non-functional, see Tier C.
