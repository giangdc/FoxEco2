# Test Scenario Map — v[VERSION]

## Tổng quan
- Tổng số scenarios: [N] (NEW: [n], MODIFIED: [n], CARRIED: [n])
- Phân bổ priority: P1: [n] | P2: [n] | P3: [n]
- Tổng số màn hình (Screen): [N] | Tổng số block: [N]

## Block Definitions (Screen → Block → Fields/Rules) — NEW (2026-07-21)

> **Mục đích:** Formalize đơn vị review nhỏ nhất mà QA dùng để check "TC đã đủ chưa" — thay vì chỉ
> phát hiện ad-hoc lúc generate-tc (Step 3b cũ), Block được xác định NGAY tại bước phân tích, là 1
> nguồn sự thật cố định mà generate-tc/review-tc dùng lại mọi lần (generate lại không đổi ranh giới
> Block, trừ khi user chủ động update). Mỗi Block = 1 khu vực chức năng riêng biệt trên 1 màn hình
> (vd: bảng danh sách, bộ lọc tìm kiếm, form tạo/sửa, khu vực actions, dialog xác nhận, summary card).
>
> **Khi nào tách 1 Block riêng:** gộp field/cột/action vào cùng 1 Block theo 1 trong 3 tiêu chí (ưu
> tiên gộp hơn tách nhỏ — hạn chế Block chỉ có 1 Scenario/TC): (1) **field/cột liên quan chặt** — ≥2
> field/cột nằm gần nhau, test được "đủ/thiếu" như 1 đơn vị (vd 8 cột 1 bảng = 1 Block; 5 field 1 form
> = 1 Block); (2) **nút/action gần nhau hoặc cùng nhóm thao tác** (vd Khóa + Mở khóa + Xóa trong 1
> dòng bảng → 1 Block "Thao tác trên danh sách"); (3) **chức năng tương tự cùng chủ đề**, dù rải rác
> nhiều chỗ trong CÙNG 1 Screen (vd validate email trùng + rule mật khẩu mặc định → 1 Block "Bảo mật
> tài khoản"). Khu vực chỉ có 1 field/action đơn lẻ, không khớp tiêu chí nào → KHÔNG tách Block riêng,
> gộp vào Block cha gần nhất theo tiêu chí phù hợp nhất hoặc bỏ qua (Screen-level). **1 Block chỉ
> thuộc đúng 1 Screen — KHÔNG gộp xuyên Screen** (xem `analyze-requirements/references/init.md`
> §Xác định Screen/Block để biết cách xử lý khi nhiều Screen nhỏ cùng chủ đề — sửa ranh giới Screen,
> không biến Screen thành Block).

### [Module Name]

#### Screen: [Tên màn hình] (vd "Danh sách chính sách giá")

##### Block: [Tên block] (vd "Bảng danh sách", "Bộ lọc tìm kiếm", "Form tạo mới")

| # | Field/Cột/Action | Rule ngắn (bắt buộc/optional, format, default...) |
|---|-------------------|----------------------------------------------------|
| 1 | | |
| 2 | | |

**Source Quote:**
> "<verbatim đoạn liệt kê field/cột/action của block này>"

**Source Location:** `<DOC-ID> §<section> · "<heading>" · <ref> · page <N>`

**Scenarios liên quan:** SC-[MODULE]-[NNN], SC-[MODULE]-[NNN], ...

<!-- Lặp lại 1 block "##### Block: ..." cho mỗi Block trong Screen này -->

<!-- Lặp lại 1 block "#### Screen: ..." cho mỗi Screen trong module -->

<!-- Lặp lại 1 block "### [Module Name]" cho mỗi module — PHẢI khớp đúng tên module dùng ở section "Scenarios — NEW & MODIFIED" bên dưới -->

## Scenarios — NEW & MODIFIED (chi tiết đầy đủ)

### [Module Name]

| Scenario ID | Feature | Screen | Block | Req ID | DOC Source | Given | When | Then | Priority | Test Type | Lifecycle |
|-------------|---------|--------|-------|--------|-----------|-------|------|------|----------|-----------|-----------|

> Cột **Screen** = tên màn hình (khớp `#### Screen:` ở Block Definitions phía trên, cùng Module).
> Cột **Block** = tên block scenario này thuộc về (khớp `##### Block:` — PHẢI có trong Block
> Definitions, không tự bịa tên block mới ở đây). Để trống/`—` = scenario áp dụng CHUNG cho cả Screen,
> không gắn riêng 1 Block nào — đây là case bình thường, phổ biến (theo ví dụ thật ở template QA:
> TC nằm ngay dưới label Screen, trước khi có label Block đầu tiên), KHÔNG phải trường hợp hiếm.
> Scenario xuyên nhiều Screen/Module (nếu phát sinh) chưa có quy ước chính thức từ QA — ghi chú tạm ở
> Remark, không tự đặt tên nhóm mới.

#### Source Detail per Scenario (verbatim quotes — `references/quoting-guide.md`)

Đặt 1 block dưới bảng main, per scenario. Quote justify Given/When/Then design:

```markdown
##### SC-[MODULE]-[NNN] — <tên ngắn>

**Source Quote:**
> "<verbatim doc text justify Given/When/Then>"

**Source Location:** `<DOC-ID> §<section> · "<heading>" · <ref> · page <N>`

**Analyst Note:** <Vietnamese paraphrase + Given/When/Then derivation rationale + cross-refs>
```

- MODIFIED scenarios: 2 quotes (old + new) + diff note.
- Long quote (>500 chars) → sidecar `02_analyze-requirements/v[VERSION]/quotes/SC-XXX-NNN.md`.
- Multiple sources per SC: number `Source Quote #1`, `#2`, …

## Scenarios — CARRIED (reference only)

| Scenario ID | Tên ngắn | Module | Screen | Block | Origin Version | Priority | Reference |
|-------------|----------|--------|--------|-------|---------------|----------|-----------|

## Scenarios — DEPRECATED

| Scenario ID | Tên ngắn | Module | Deprecated ở | Lý do |
|-------------|----------|--------|-------------|-------|
