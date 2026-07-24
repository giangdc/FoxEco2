# Analyze Requirements — Mode DELTA

> `/analyze-requirements --delta --version v2.0 @00_input/v2.0/`
> Khi nào: Đã có MASTER-MEMORY.md + parent version, bắt đầu phân tích version mới.

## Input → Output

| Input (đọc) | Output (tạo/cập nhật) |
|-------------|----------------------|
| CLAUDE.md, PIPELINE.md | `02_.../v[NEW]/MEMORY.md` (tạo mới) |
| MASTER-MEMORY.md | `02_.../v[NEW]/requirement_traceability.md` |
| `02_.../v[PARENT]/MEMORY.md` (baseline) | `02_.../v[NEW]/test_scenario_map.md` |
| `00_input/v[NEW]/*` | `02_.../v[NEW]/test_data_catalog.md` |
| | `02_.../v[NEW]/risk_assessment.md` |
| | MASTER-MEMORY.md (update §1-§5, §7, §8) |

---

## Workflow

### Step 1: Đọc context + guard

```
1. PIPELINE.md → check prerequisites
2. MASTER-MEMORY.md → parent version, existing scenarios (§3 Lifecycle)
3. Parent MEMORY: 02_.../v[PARENT]/MEMORY.md → baseline scenarios
4. Ghi §8 = IN_PROGRESS
```

Hỏi version mới: **"Version mới là gì? (ví dụ: v2.0)"**
Tạo folder: `mkdir -p 00_input/v[NEW]/ 02_analyze-requirements/v[NEW]/`

### Step 2: Scan + đọc docs mới

```
1. Scan 00_input/v[NEW]/
2. Liệt kê docs mới
3. Hỏi: "Có docs từ version cũ cần xem lại không?"
```

### Step 3: Phân tích incremental — classify scenarios

```
Mỗi requirement trong docs MỚI:
  1. Tìm requirement tương ứng trong PARENT
     ├── KHÔNG tìm thấy → NEW (tạo scenario mới)
     ├── Tìm thấy + GIỐNG → CARRIED (reference only)
     └── Tìm thấy + KHÁC → MODIFIED (duplicate + sửa)

Mỗi requirement trong PARENT KHÔNG có trong docs mới:
  → Feature bị xóa? → DEPRECATED
  → Feature không thay đổi? → CARRIED
  → Không rõ → hỏi user
```

**Quy tắc CARRIED:**
- KHÔNG duplicate Given/When/Then — chỉ 1 dòng reference
- `SC-LOGIN-001 | CARRIED(v1.0) | → xem 02_.../v1.0/test_scenario_map.md`
- TC Status = `✅ v1.0`
- **Source Quote**: KHÔNG re-quote, reference parent: `Source Quote: see v1.0 REQ-LOGIN-001`. Location field link parent doc.

**Quy tắc MODIFIED:**
- PHẢI duplicate Given/When/Then + sửa theo thay đổi
- Ghi: `MODIFIED from v1.0: [mô tả thay đổi]`
- TC cũ cần REGENERATE
- **Source Quote**: capture **2 quotes** — parent + new version. Show diff trong Analyst Note. Format:
  ```
  Source Quote (old) — DOC-v1.0-NN §X · paragraph 2
  > "<old text>"

  Source Quote (new) — DOC-v2.0-NN §Y · paragraph 2
  > "<new text>"

  Analyst Note (diff): <what changed and why>
  ```

#### 🔖 Verbatim quoting (MANDATORY — đọc `references/quoting-guide.md`)

Cùng rule với INIT mode: mỗi NEW/MODIFIED REQ + SC + Clarification cần 3 phần (Source Quote + Source Location + Analyst Note). CARRIED reference parent quote, KHÔNG re-quote. DEPRECATED keep parent quote + add deprecation reason vào Analyst Note.

Long quote (>500 chars) → sidecar `02_analyze-requirements/v[NEW]/quotes/REQ-XXX-NNN.md`.

Opt-out: `--no-quote` flag.

Xem `references/quoting-guide.md` §"DELTA mode" cho table-form summary.

### Step 4: Tạo deliverables cho version mới

5 files trong `02_.../v[NEW]/`. Chỉ chứa data cho NEW + MODIFIED.
CARRIED scenarios → reference parent version.

> **Structure-lock (Nguyên tắc cốt lõi #6):** mỗi file theo đúng asset template tương ứng (xem SKILL.md "Deliverable ↔ Template Registry" / init.md Step 4 bảng map) — copy header cột + section verbatim, KHÔNG đổi cột. MODIFIED scenarios: 2 Source Quote (old+new).

### Step 5: Cập nhật MASTER-MEMORY.md

- §1: thêm row version mới
- §2: thêm DOC IDs mới
- §3: cập nhật Lifecycle cho tất cả scenarios
- §4: tạo Regression Scope:

```markdown
### v[NEW] — Regression Scope

**Phải test (new + modified):**
| SC ID | Type | Lý do |

**Nên regression (carried — high risk):**
| SC ID | Type | Lý do |

**Không cần test (carried — low risk, stable):**
| SC ID | Type | Lý do |
```

- §5: thêm Version Comparison (new vs parent)
- §7: update Active Version Path
- §8: ghi = COMPLETED

### Step 6: Present + handoff

```
📊 Kết quả phân tích v[NEW] (delta từ v[PARENT]):

Scenarios:
  - NEW: [N] | MODIFIED: [N] | CARRIED: [N] | DEPRECATED: [N]
  - Tổng active: [N] | P1: [n] | P2: [n] | P3: [n]

Regression scope: [N] scenarios cần test

Bước tiếp: /generate-tc --version v[NEW]
```

---

## Checklist

- [ ] Parent MEMORY đã đọc
- [ ] Mỗi scenario classified: NEW / MODIFIED / CARRIED / DEPRECATED
- [ ] CARRIED: chỉ reference, không duplicate
- [ ] MODIFIED: duplicate + sửa + ghi rõ thay đổi
- [ ] **Structure-lock verified (BLOCKING):** deliverable version mới khớp header cột + thứ tự section của asset template — KHÔNG tự thêm/bớt/đổi tên cột, KHÔNG đổi thứ tự section.
- [ ] MASTER-MEMORY §3 Lifecycle cập nhật
- [ ] MASTER-MEMORY §4 Regression Scope tạo
- [ ] MASTER-MEMORY §5 Version Comparison thêm
- [ ] §8 = COMPLETED
- [ ] CLAUDE.md append
