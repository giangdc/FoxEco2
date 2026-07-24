# Test Data Catalog — v[VERSION]

> Tạo bởi: analyze-requirements. Dữ liệu test (valid / invalid / boundary) per module, trích từ tài liệu gốc **theo đúng ký hiệu của DOC dự án** (vd FR/VR, AC, UC, US key, hoặc §section nếu doc không đánh số). Input cho generate-tc (BVA/EP/...).
>
> **Structure-lock:** giữ nguyên 5 cột `| Field | Valid | Invalid | Boundary | Nguồn |` cho mọi module. KHÔNG đổi cột.

## Module [MODULE] — <tên module> (DOC-v[VERSION]-[NN])

| Field | Valid | Invalid | Boundary | Nguồn |
|-------|-------|---------|----------|-------|
| <tên field> | <giá trị hợp lệ (mô tả)> | <giá trị sai (→mã MSG nếu có/hệ quả)> | **<giá trị biên (hợp lệ/chặn)>** | <ref DOC: vd FR-[NNN]/VR-[NNN], AC-[NNN], §[N]> |

(lặp bảng cho mỗi module)

## Ghi chú chung
- Giá trị "master data" (danh mục từ hệ thống nguồn) phụ thuộc môi trường — xác nhận giá trị thực khi vibe-test/automation.
- Boundary values (in **đậm**) là ứng viên chính cho BVA ở generate-tc.

### Quy ước cell (giữ nhất quán)
- **Valid:** `value (mô tả)` — vd `ABC1234567 (10 ký tự)`, `hôm nay (default)`.
- **Invalid:** `value (→ hệ quả/MSG)` — vd `rỗng (→MSG-001)`, `"abc" (→MSG-E-002)`. Dự án không có mã MSG → ghi mô tả hệ quả (vd `rỗng (→ báo lỗi bắt buộc nhập)`).
- **Boundary:** **bold** giá trị biên + (hợp lệ/chặn) — vd `**500 ký tự (hợp lệ), 501 (chặn)**`.
- **Nguồn:** dùng **đúng ký hiệu của DOC dự án** theo `req_notation` trong block `## DOC Notation` của `Project_rule.md` — vd `FR-NNN/VR-NNN` (dự án có đánh số FR/VR), `AC-NNN`, `UC-NNN`, `US key (Jira)`, hoặc `DOC-ID §section` khi `req_notation: none`. **KHÔNG tự bịa ID** nếu doc không có — fallback luôn là `§section`.
- Set literal `{0=…, 1=…}`; `→` = hệ quả; `⟷` = quan hệ 2 chiều; `[…]` = ID pattern.
