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
- **✅ Cập nhật 2026-07-27 (BA/PO trả lời batch clarifications qua chat):** **Không còn BLOCKER cứng nào.** `C-ORD-02` (ngưỡng giá trị hàng) đã gỡ BLOCKER — BA/PO xác nhận phase này chưa làm, out of scope v1.0. Tổng cộng 13/16 clarification đã Resolved/Deferred:
  - **Resolved — Out of scope v1.0 (deferred to future phase):** `C-ORD-02` (ngưỡng giá trị hàng), `C-USR-01` (tier "Hạng Đồng hành"), `C-USR-02` (cấu hình kênh liên hệ), `C-GIFT-01` (rating 1-5 sao), `C-TS-01` (Admin Web Portal), `C-CNL-01` (màn Báo sự cố).
  - **Resolved — rule mới áp dụng ngay ở v1.0:** `C-ORD-01` (validate bắt buộc B1/B2, maxlength TBD), `C-ORD-03` (hạn tin = giá trị user chọn lúc đăng), `C-ORD-04` (không chặn "Thuốc/Y tế" ở v1.0), `C-ASN-01` (SĐT lộ SAU khi ghép — theo BRD), `C-ASN-02` (cấm tự nhận mang giúp đơn của mình), `C-DLV-03` (modal đơn giản là UI chính thức).
  - **Partially Resolved:** `C-NTF-02` (khớp tuyến = trùng địa chỉ giao + khung giờ phù hợp; còn thiếu định nghĩa độ lệch khung giờ + chu kỳ quét).
  - **Còn Open thực sự (chưa có câu trả lời):** `C-ORD-05` (biến thể "Mã tin" ở màn Đăng tin thành công), `C-NTF-01` (danh sách 9 loại thông báo chính thức — đã bổ sung bảng unified 3 nguồn để BA chọn, xem `MEMORY.md §6.1`), `C-DLV-02` (default bật/tắt chia sẻ vị trí).
- Chi tiết đầy đủ + status mới nhất từng clarification: `02_analyze-requirements/v1.0/MEMORY.md` §6/§6.1 Clarifications, `requirement_traceability.md` §2/§3, `risk_assessment.md`.
- **Cập nhật 2026-07-27 (rescan UI riêng màn Thông báo):** +1 scenario `SC-NTF-007` (empty state danh sách thông báo — chưa có bằng chứng UI, áp dụng lại pattern "Hiện tại chưa có dữ liệu" đã dùng ở SC-ORD-023/SC-GIFT-006, mở rộng `C-ORD-06`).
- **Cập nhật 2026-07-27 (gap khi review TC-NTF):** +2 scenario `SC-NTF-008` (đánh dấu đã đọc), `SC-NTF-009` (scroll load thêm dữ liệu), +1 clarification `C-NTF-03` (Open).
- **Cập nhật 2026-07-27 (fix finding health-check):** SC-ORD-015..026 (màn Hoạt động, đã có từ trước trong `test_scenario_map.md`) bị thiếu khỏi `MEMORY.md` §4 Scenario Index — đã sync lại. Tổng: 82 scenario (P1:19 · P2:37 · P3:26).
- **Cập nhật 2026-07-28 (BA cập nhật BRD lên v3.2):** so với v3.1, chỉ thêm 1 section mới `§D8 Validate & Giá trị mặc định (Form Rules)` — resolve dứt điểm maxlength còn TBD của `C-ORD-01`, hé lộ cơ chế cảnh báo "Giá trị hàng = Cao" (khác ngưỡng số tiền BR-ORD-03 vẫn deferred). +2 requirement, +5 scenario (4 ORD, 1 CNL), 1 scenario modified. Tổng hiện tại: **87 scenario** (P1:20 · P2:39 · P3:28), **43 requirement**.
