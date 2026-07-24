# MASTER-MEMORY — Cross-Version Registry

> Cập nhật lần cuối: 2026-07-24
> Active version: v1.0

## 1. Version Registry
| Version | Release Date | Input Folder | Analyze Folder | Status | Tổng DOC | Tổng SC (all) | Tổng SC (new+mod) | Parent |
|---------|-------------|-------------|----------------|--------|----------|--------------|-------------------|--------|
| v1.0 | TBD | `00_input/v1.0/` | `02_analyze-requirements/v1.0/` | Analyzed | 4 | 62 | 62 | — (version đầu tiên) |

## 2. DOC ID Registry (Global)
| DOC ID | Version | File | Loại | Modules |
|--------|---------|------|------|---------|
| DOC-v1.0-01 | v1.0 | `FoxEco BRD/FoxEco BRD v3.1 (1).html` | HTML (BRD v3.1) | USR, ORD, ASN, DLV, GIFT, CNL, NTF, TS |
| DOC-v1.0-02 | v1.0 | `FoxEco Demo 3 vai tro (standalone)/tổng hợp từ file demo.docx` | Word (PRD tái dựng từ demo) | USR, ORD, ASN, DLV, GIFT, NTF |
| DOC-v1.0-03 | v1.0 | `FoxEco Demo 3 vai tro (standalone)/FoxEco Demo 3 vai tro (standalone) (2).html` | HTML (prototype tương tác, reference-only) | ASN, DLV |
| DOC-v1.0-04 | v1.0 | `Fox Eco Doc/images/*` (82 ảnh, FigJam board `canvas.fig`) | Figma UI design mockup (status bar "9:41" — mẫu chuẩn Apple design, KHÔNG phải screenshot chụp máy thật) — nguồn thiết kế UI text/button chi tiết nhất hiện có | USR, ORD, ASN, DLV, GIFT, CNL, NTF |

## 3. Scenario Lifecycle (Cross-Version)
> Version ĐẦU (tất cả NEW) — dùng roll-up gọn theo Module.

| Module | Origin | Lifecycle | Count |
|--------|--------|-----------|-------|
| USR | v1.0 | NEW | 5 |
| ORD | v1.0 | NEW | 14 |
| ASN | v1.0 | NEW | 12 |
| DLV | v1.0 | NEW | 14 |
| GIFT | v1.0 | NEW | 4 |
| CNL | v1.0 | NEW | 4 |
| NTF | v1.0 | NEW | 6 |
| TS | v1.0 | NEW | 3 |

## 4. Regression Scope
### v1.0
**Phải test (new + modified):** toàn bộ 62 scenario NEW (version đầu tiên, chưa có regression scope).

**Nên regression (carried — high risk):** — (chưa có version trước)

**Không cần test (carried — low risk, stable):** — (chưa có version trước)

## 5. Version Comparison
(Từ v2 trở đi)

## 6. TC Files Registry
| Version | TC-MASTER File | Tổng TC | Ngày consolidate | Status |
|---------|---------------|---------|-------------------|--------|

## 7. Downstream Path Registry
| Skill | Active Version Path |
|-------|-------------------|
| generate-tc | `02_analyze-requirements/v1.0/` → `03_test-cases/v1.0/` |
| review-tc | `03_test-cases/v1.0/` |
| vibe-test | `03_test-cases/v1.0/` → `08_test-runs/vibe/` |
| log-bug | `05_bug-reports/` |
| test-report | `09_reports/` |

## 8. Pipeline Status — v1.0
> Thứ tự + tên skill khớp PIPELINE.md. Status ∈ NOT_STARTED / IN_PROGRESS / PARTIAL / COMPLETED / SKIPPED / FAILED.

| # | Skill | Status | Last Run | Scope | Output | Notes |
|---|-------|--------|----------|-------|--------|-------|
| 1 | init-project | COMPLETED | 2026-07-24 | — | CLAUDE.md/PIPELINE.md/COMMANDS.md | — |
| 2 | create-test-plan | NOT_STARTED | — | — | — | — |
| 3 | analyze-requirements | COMPLETED | 2026-07-24 | v1.0 | 5 file `02_analyze-requirements/v1.0/` + MASTER-MEMORY.md | UPDATE — bổ sung DOC-v1.0-04 (Fox Eco Doc, 82 ảnh Figma). Kết quả: resolve C-DLV-01 (Receiver-only) + C-DLV-03 (modal đơn giản); Partially Resolved C-USR-01 (có tier text, không điểm số) + C-GIFT-01 (rating tồn tại ở notification, chưa rõ màn thao tác); +1 clarification mới C-ORD-05 (2 biến thể "Đăng tin thành công" có/không "Mã tin"); cập nhật verbatim text/button chính xác cao cho NTF/USR/GIFT/DLV/CNL/ORD screens. Không phát sinh scenario mới. UPDATE #2 (cùng ngày): +1 clarification mới C-USR-03 (Resolved) — QA xác nhận app STG thật KHÔNG có chức năng cập nhật hồ sơ cá nhân (view-only), sửa lại scope REQ-USR-002/SC-USR-002. |
| 4 | generate-tc | NOT_STARTED | — | — | — | — |
| 5 | review-tc | NOT_STARTED | — | — | — | — |
| 6 | scan-source-code | NOT_STARTED | — | — | — | N/A (no automation) |
| 7 | implement-automation | NOT_STARTED | — | — | — | N/A (no automation) |
| 8 | review-src-tc | NOT_STARTED | — | — | — | N/A (no automation) |
| 9 | vibe-test | NOT_STARTED | — | — | — | — |
| 10 | execute-maintain | NOT_STARTED | — | — | — | N/A (no automation) |
| 11 | log-bug | NOT_STARTED | — | — | — | — |
| 12 | test-report | NOT_STARTED | — | — | — | — |
| 13 | health-check | COMPLETED | 2026-07-24 | Quick | 1 CRITICAL, 4 WARNING, 2 INFO | Đã fix toàn bộ 7 finding theo yêu cầu user — xem chi tiết trong chat |

## 9. Notes
- 2026-07-24: INIT analyze v1.0 hoàn tất từ 3 tài liệu (BRD v3.1 + PRD tái dựng từ demo + prototype tương tác). Phát hiện ban đầu 4 clarification cần BA/PO xác nhận: (1) C-USR-01 tier/điểm ECO/CO2, (2) C-ORD-02 ngưỡng giá trị hàng, (3) C-DLV-01 ai được xác nhận "Đã nhận", (4) C-GIFT-01 tính năng đánh giá sao (RAT-01/02).
- **Cập nhật 2026-07-24 (sau đợt bổ sung DOC-v1.0-04 + health-check):** chỉ còn **1 BLOCKER cứng — `C-ORD-02`** (Open, chưa có con số ngưỡng giá trị hàng). 3 điểm còn lại đã hạ mức: `C-DLV-01` = **Resolved** (Receiver-only, xác nhận qua ảnh Figma), `C-USR-01` = **Partially Resolved** (có tier text, không điểm số — không còn BLOCKER cứng cho SC-USR-004), `C-GIFT-01` = **Partially Resolved** (rating tồn tại ở notification, chưa rõ màn thao tác — vẫn Blocked riêng cho REQ-GIFT-002 nhưng không chặn toàn bộ module GIFT). Khuyến nghị: chỉ cần chốt `C-ORD-02` với BA/PO trước khi `/generate-tc` viết BVA cho ngưỡng giá trị hàng; các TC khác có thể chạy bình thường, đánh dấu riêng phần liên quan C-USR-01/C-GIFT-01 là "GAP/Partially Resolved — xem MEMORY.md §6" thay vì "Blocked" toàn bộ. Chi tiết đầy đủ + status mới nhất từng clarification: `02_analyze-requirements/v1.0/MEMORY.md §6`.
- Chưa có `create-test-plan` (Test Plan §01) — generate-tc/review-tc vẫn chạy được độc lập vì không phải hard prerequisite, nhưng khuyến nghị tạo Test Plan trước để xác định rõ scope/exit criteria cho FoxEco v1.0.
