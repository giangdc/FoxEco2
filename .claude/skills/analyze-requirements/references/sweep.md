# Analyze Requirements — Mode SWEEP (Completeness Sweep)

> `/analyze-requirements --sweep`
> `/analyze-requirements --sweep --version v1.0`
> `/analyze-requirements --sweep --doc DOC-v1.0-04`
> Khi nào: Đã có REQ inventory (INIT/DELTA đã chạy). Muốn rà lượt 2 để tìm requirement bị bỏ sót khỏi REQ inventory — đặc biệt các đoạn **văn xuôi** (nguyên tắc, quy ước, mục tiêu kỹ thuật, NFR mô tả, glossary-rule, default value rải rác) mà lượt INIT (vốn bias theo bảng requirement có đánh số — FR/VR/AC... tuỳ ký hiệu dự án) dễ miss.

## Tại sao cần SWEEP?

INIT/DELTA trích REQ chủ yếu từ **cấu trúc có sẵn** (bảng FR §3, VR §4, MSG, AC §7). Các phát biểu kiểm-thử-được nằm trong **văn xuôi** (vd "Mọi thông báo phải bằng tiếng Việt, có hướng dẫn khắc phục"; "Toast tự ẩn sau 5 giây") không có ID bảng → dễ lọt. SWEEP là **lượt rà ngược (completeness-critic)**: thay vì "đọc bảng → tạo REQ", nó hỏi *"câu nào trong toàn văn doc phát biểu hành vi/ràng buộc kiểm-thử-được mà CHƯA có REQ?"*.

**SWEEP chỉ PHÁT HIỆN (đọc) — KHÔNG tự sửa.** Vá gap route sang Mode UPDATE (thêm REQ/SC) + `generate-tc` (thêm TC).

## Input (chỉ đọc)

```
1. 00_input/[version]/*                              → TOÀN VĂN tài liệu gốc (không chỉ bảng)
2. 02_analyze-requirements/[version]/MEMORY.md       → REQ inventory hiện có (§4.1) + scenario index (§4)
3. 02_analyze-requirements/[version]/requirement_traceability.md → REQ↔SC map
```

## Output (tạo)

```
02_analyze-requirements/[version]/coverage-gap-report.md
```

## Workflow

### Step 1: Guard + context
```
1. MASTER-MEMORY §8 → check analyze-requirements ≥ COMPLETED (cần REQ inventory để diff)
   - Nếu chưa INIT → báo user chạy /analyze-requirements --init trước, exit.
2. Đọc REQ inventory hiện có: tập REQ-ID + section mỗi REQ trỏ tới (từ §4.1 + traceability).
3. Liệt kê docs trong 00_input/[version]/ (hoặc --doc lọc 1 doc).
4. Ghi MASTER-MEMORY §8 note: analyze-requirements = IN_PROGRESS (SWEEP).
```

### Step 2: Exhaustive atomic-statement extraction (fan-out per doc)

Cho mỗi doc, dùng 1 independent agent (lens "completeness-critic", khác lens INIT) đọc **toàn văn theo từng §** — mọi đoạn/bullet/ô bảng/heading — và liệt kê **atomic requirement statement**: mọi câu phát biểu hành vi, ràng buộc, NFR, default value, quy ước hiển thị, ô ma trận quyền, business rule trong glossary, điều kiện hiển thị… (KHÔNG bỏ qua văn xuôi).

> Agent KHÔNG được "tin" REQ inventory là đủ — phải quét độc lập rồi mới diff. Ưu tiên scan Source Quote-able text (verbatim).

### Step 3: Diff với REQ inventory + phân loại

Map mỗi atomic statement → REQ-ID hiện có (COVERED) hoặc **UNCOVERED**. Phân loại UNCOVERED:

| Loại | Ý nghĩa | Hành động |
|---|---|---|
| **A — Functional gap** | Hành vi/validation kiểm-thử-được, chưa có REQ/SC | ➜ Cần thêm REQ + SC + TC |
| **B — NFR gap** | Yêu cầu phi chức năng (perf/security/a11y) chưa có REQ | ➜ Thêm REQ; TC tùy khả năng test |
| **C — Out-of-scope / Phase sau** | Doc ghi rõ ngoài phạm vi | ➜ Xác nhận loại trừ **có chủ ý** (ghi nhận, không tạo TC) |
| **D — Descriptive only** | Mô tả bối cảnh/định nghĩa, không kiểm-thử-được | ➜ Bỏ qua (ghi nhận đã xét) |

### Step 4: Output coverage-gap-report.md

Dùng template `assets/coverage-gap-report-template.md`. Mỗi gap loại A/B có: Source Quote (verbatim) + Source Location + đề xuất REQ/SC ID + severity (High/Med/Low theo rủi ro).

### Step 5: Present + route fix
```
📊 Completeness Sweep v[X]:
   Atomic statements quét: [N]
   COVERED: [n] | UNCOVERED: A=[n] B=[n] C=[n] D=[n]
   Gap loại A/B (cần vá): [n]

Vá ngay? → /analyze-requirements --update "thêm REQ-… cho <gap>" rồi /generate-tc --module <M>
```
- Ghi MASTER-MEMORY §8 = COMPLETED (SWEEP) + số gap A/B vào Notes.
- **KHÔNG tự thêm REQ/TC** — chờ user confirm từng gap (tránh tạo scenario ngoài requirement, giữ nguyên tắc cốt lõi #4).

## Checklist
- [ ] REQ inventory hiện có đã đọc (diff base)
- [ ] Quét TOÀN VĂN từng doc (không chỉ bảng requirement đánh số kiểu FR/VR/AC)
- [ ] Mỗi UNCOVERED có Source Quote verbatim + Location + phân loại A/B/C/D
- [ ] `coverage-gap-report.md` tạo
- [ ] §8 = COMPLETED (SWEEP) + đếm gap
- [ ] KHÔNG tự sửa REQ/SC/TC — chỉ report + route

## Anti-patterns
| Anti-pattern | Fix |
|---|---|
| Tin REQ inventory đủ rồi chỉ "xác nhận" | Phải quét độc lập toàn văn TRƯỚC khi diff |
| Gắn mọi câu mô tả thành gap | Phân loại D (descriptive) — chỉ A/B mới actionable |
| Tự thêm REQ/TC trong SWEEP | SWEEP chỉ detect; fix qua UPDATE + generate-tc |
| Bỏ qua Out-of-scope | Loại C phải ghi nhận "loại trừ có chủ ý" để chứng minh đã xét |
