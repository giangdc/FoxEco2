# Risk Assessment — v[VERSION]

> Tạo bởi: analyze-requirements. Đánh giá rủi ro per module + định hướng test focus cho generate-tc/vibe-test.
>
> **Structure-lock:** dùng DUY NHẤT 1 dạng bảng chi tiết hợp nhất bên dưới cho MỌI module (KHÔNG dùng nhiều dạng bảng khác nhau giữa các module). KHÔNG đổi cột.

## Tổng quan
| Module | Risk Level | Rủi ro chính |
|--------|-----------|--------------|
| [MODULE] | High / Medium / Low | <tóm tắt 1 dòng rủi ro lớn nhất> |

## Chi tiết rủi ro (bảng hợp nhất — 1 dạng cho mọi module)
| Risk ID | Module/Area | Rủi ro | Severity | Why (Source) | Test Focus | REQ/SC |
|---------|-------------|--------|----------|--------------|------------|--------|
| RISK-[MODULE]-[NN] | [MODULE] / <area> | <mô tả rủi ro> | High / Medium / Low | <doc §section + ref ID nếu DOC có (FR/VR/AC... tuỳ dự án)> | <điểm cần test> | SC-[MODULE]-[NNN], REQ-[MODULE]-[NNN] |

> Risk ID format: `RISK-<MODULE>-<NN>` (vd `RISK-PV-01`). Severity = High / Medium / Low (có thể Medium-High).

## Khuyến nghị tổng thể
1. **Resolve blocker clarifications trước generate-tc** các scenario liên quan: [list C-IDs].
2. **Ưu tiên test P1 high-risk:** [list SC-IDs].
3. **Performance / cần môi trường:** [list SC-IDs] — defer tới khi có env + dữ liệu lớn.
4. **ID/text cleanup (non-blocking, cần trước automation):** [list — vd ID trùng, nhãn không nhất quán].
