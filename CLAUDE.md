# FoxEco — Project Context

## Thông tin dự án (Project Info)
- **Tên dự án:** FoxEco
- **Loại sản phẩm:** SDK tích hợp vào app mobile **FoxPro** có sẵn (không phải web app độc lập)
- **Loại kiểm thử:** Smoke, Functional, Regression
- **Môi trường:** STG
- **URL:** N/A — xem `07_environments/environments.md` (host app, SDK version, platform)
- **Team:** Solo
- **QC phụ trách:** GiangDC2

## Version Info
- **Current version:** v1.0
- **Version history:** v1.0 (initial)
- **MASTER-MEMORY:** `02_analyze-requirements/MASTER-MEMORY.md`
- **Project Rules:** `02_analyze-requirements/Project_rule.md`

## Quy trình làm việc (Workflow)
```
00_input/v1.0/ (tài liệu gốc)
  → 01_test-plans/ (create-test-plan)
    → 02_analyze-requirements/v1.0/ (analyze-requirements)
      → 03_test-cases/v1.0/ (generate-tc → consolidate → TC-MASTER)
        → 11_tc-review/ (review-tc + review-src-tc)
          → 08_test-runs/ (execute)
            → 05_bug-reports/ (log bugs)
              → 09_reports/ (summary report)
```

## MEMORY Files
- **MASTER-MEMORY:** `02_analyze-requirements/MASTER-MEMORY.md` — cross-version registry
- **Version MEMORY:** `02_analyze-requirements/v1.0/MEMORY.md` — version-scoped analysis
- **Source-code MEMORY:** `10_source-code/MEMORY.md` — locators, page classes, implementation log

## Naming Conventions
- Documents: `DOC-v[VERSION]-[NN]`
- Scenarios: `SC-[MODULE]-[NNN]`
- Test cases: `TC-[MODULE]-[NNN]`
- TC Master: `TC-MASTER-v[VERSION].xlsx`
- Bug reports: `BUG-[NNN]-[short-title].md`
- Test runs: `TR-v[VERSION]-[YYYY-MM-DD].md`
- Reports: `REPORT-[TYPE]-v[VERSION]-[DATE].md`

## Folder Reference
| # | Folder | Mục đích | Skill liên quan |
|---|--------|----------|----------------|
| 00 | input/v1.0/ | Tài liệu đầu vào (theo version) | analyze-requirements |
| 00 | input/shared/ | Tài liệu dùng chung | analyze-requirements |
| 01 | test-plans/ | Test plan tổng thể | create-test-plan |
| 02 | analyze-requirements/ | MASTER-MEMORY + Project_rule | analyze-requirements |
| 02 | analyze-requirements/v1.0/ | Analysis output theo version | analyze-requirements |
| 03 | test-cases/v1.0/ | TC-MASTER + fragments | generate-tc |
| 04 | test-data/ | Dữ liệu test | — |
| 05 | bug-reports/ | Báo cáo lỗi | log-bug |
| 06 | checklists/ | Smoke + release checklists | — |
| 07 | environments/ | Config môi trường | — |
| 08 | test-runs/ | Logs chạy test | test-report |
| 09 | reports/ | Báo cáo tổng hợp | test-report |
| 10 | source-code/ | Automation code + MEMORY | scan-source, implement-auto |
| 11 | tc-review/ | Review reports (TC + SRC-TC) | review-tc, review-src-tc |

## Project Rules
→ Xem chi tiết: `02_analyze-requirements/Project_rule.md`

## Pipeline & Commands
- **PIPELINE.md** (root) — bản đồ pipeline QA, skill registry, prerequisites
- **COMMANDS.md** (root) — cheat-sheet lệnh gọi từng skill theo thứ tự pipeline

## Tools
- Manual testing project scaffolded by `init-manual-project` skill
- Framework version: Multi-Version (MASTER-MEMORY enabled)
- Created on: 2026-07-24

## Analyze Requirements — v1.0 (2026-07-24)
- **Nguồn:** DOC-v1.0-01 (BRD v3.1 · Gửi Hàng + Nền tảng chung), DOC-v1.0-02 (PRD tái dựng từ demo), DOC-v1.0-03 (prototype tương tác, reference-only).
- **Kết quả:** 8 module (USR, ORD, ASN, DLV, GIFT, CNL, NTF, TS) — 40 requirement, 62 scenario (P1:20 · P2:28 · P3:14), 16 clarification.
- **Cập nhật 2026-07-24 (bổ sung):** +4 scenario (SC-DLV-012/013/014, SC-GIFT-004) + REQ-GIFT-003, nguồn "Quan sát thực tế app STG" (QA GiangDC2) — ma trận nhãn nút/trạng thái theo vai trò tại màn Theo dõi đơn, xem `test_scenario_map.md` block "Theo dõi đơn — Ma trận nhãn nút theo trạng thái".
- **Cập nhật 2026-07-24 (bổ sung #3):** +1 clarification **C-USR-03 (Resolved)** — QA xác nhận app STG thật KHÔNG có chức năng cập nhật hồ sơ cá nhân (chỉ view-only), sửa lại scope REQ-USR-002/SC-USR-002.
- **⚠️ Cập nhật 2026-07-24 (health-check):** chỉ còn **1 clarification BLOCKER cứng cần BA/PO xác nhận trước `/generate-tc`:**
  1. `C-ORD-02` — Ngưỡng giá trị hàng kích hoạt cảnh báo bảo hiểm (chưa có con số, Open — BLOCKER cho BVA).
- **3 điểm còn lại đã hạ mức (không còn chặn generate-tc toàn bộ):**
  - `C-USR-01` — Partially Resolved: có tier text ("Hạng Đồng hành"), không có điểm số ECO/CO2. Vẫn cần hỏi BA cơ chế tính tier trước khi viết BVA cho ngưỡng lên hạng.
  - `C-DLV-01` — Resolved: Receiver-only (xác nhận qua ảnh Figma DOC-v1.0-04).
  - `C-GIFT-01` — Partially Resolved: rating tồn tại ở notification, chưa rõ màn thao tác chấm sao — chỉ Blocked riêng cho REQ-GIFT-002, không chặn cả module GIFT.
- Chi tiết đầy đủ + status mới nhất từng clarification (gồm cả `C-USR-02`, `C-USR-03` mới phát hiện): `02_analyze-requirements/v1.0/MEMORY.md` §6 Clarifications, `risk_assessment.md`.
