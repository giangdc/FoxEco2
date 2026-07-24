# Coverage Gap Report — v[VERSION]

> Tạo bởi: analyze-requirements Mode SWEEP
> Ngày: [date]
> Scope: [tất cả docs / DOC-vX.Y-NN]
> Diff base: REQ inventory hiện có (MEMORY §4.1, [N] REQ)

## Tổng quan
| Chỉ số | Giá trị |
|--------|---------|
| Atomic statements quét | [N] |
| COVERED (đã có REQ) | [n] |
| UNCOVERED — A Functional gap | [n] |
| UNCOVERED — B NFR gap | [n] |
| UNCOVERED — C Out-of-scope (loại trừ chủ ý) | [n] |
| UNCOVERED — D Descriptive (không test được) | [n] |
| **Gap actionable (A+B)** | **[n]** |

## Gap loại A — Functional (cần thêm REQ + SC + TC)

### GAP-A-01 — <tên ngắn>
**Source Quote:**
> "<verbatim text từ doc>"

**Source Location:** `DOC-vX.Y-NN §<section> "<heading>"`
**Phân loại:** A — Functional · **Severity:** High/Med/Low
**Đề xuất:** REQ-<MODULE>-<NNN> + SC-<MODULE>-<NNN> + ~<k> TC
**Analyst Note:** <vì sao kiểm-thử-được + ảnh hưởng>

(lặp cho mỗi gap A…)

## Gap loại B — NFR

### GAP-B-01 — <tên ngắn>
**Source Quote:**
> "<verbatim>"

**Source Location:** `DOC-vX.Y-NN §…`
**Đề xuất:** REQ-<MODULE>-NFR-<NNN> · TC: [có thể test / cần môi trường / defer]

(lặp…)

## Loại C — Out-of-scope (xác nhận loại trừ có chủ ý)
| Statement | Source Location | Lý do loại trừ (doc ghi) |
|-----------|-----------------|--------------------------|
| … | DOC §8 | Phase 2 |

## Loại D — Descriptive (đã xét, không actionable)
| Statement | Source Location | Ghi chú |
|-----------|-----------------|---------|

## Route fix
| Gap | Skill | Lệnh đề xuất |
|-----|-------|--------------|
| A-01 | analyze-requirements + generate-tc | `/analyze-requirements --update "..."` → `/generate-tc --module <M>` |

> SWEEP chỉ phát hiện. Vá phải qua Mode UPDATE (thêm REQ/SC) + generate-tc (thêm TC), sau đó `/review-tc --recheck` + `/health-check --full`.
