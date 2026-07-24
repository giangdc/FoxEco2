# PIPELINE — FoxEco

> Bản đồ pipeline QA cho dự án **FoxEco** (SDK tích hợp vào app mobile **FoxPro** có sẵn — Solo, **chưa có automation**).
> Tester đọc `COMMANDS.md` để biết cú pháp gọi từng skill.
> **Trạng thái sống (per-version) nằm ở `02_analyze-requirements/MASTER-MEMORY.md` §8** — bảng ở §8 dưới đây chỉ là snapshot tổng quan cross-version, không phải nguồn cập nhật real-time. Khi cần biết trạng thái chính xác nhất của 1 skill cho 1 version cụ thể, luôn tra MASTER-MEMORY.md trước.

## 1. Pipeline Flow

```
init-project ✅
  → create-test-plan
    → analyze-requirements
      → generate-tc (bao gồm --consolidate/--sync → TC-MASTER)
        → review-tc
          → vibe-test (chạy TC qua Appium MCP trên app FoxPro — thay manual tester)
            → log-bug
              → test-report

health-check: cross-cutting, chạy bất kỳ lúc nào để đối chiếu consistency giữa các file trên.
```

> Nhánh automation (scan-source-code → implement-automation → review-src-tc) hiện **N/A (no automation)**.
> Khi cần bật automation cho FoxEco SDK: chạy `/init-source-code --archetype appium-java` (SDK mobile → Appium Java phù hợp nhất), sau đó cập nhật lại flow trên.

## 2. Skill Registry (13 pipeline skills)

| # | Skill | Vai trò | Folder sở hữu |
|---|-------|---------|---------------|
| 1 | init-project | Scaffold project | root, `00_`–`11_` |
| 2 | create-test-plan | Lập test plan | `01_test-plans/` |
| 3 | analyze-requirements | Phân tích requirement, MASTER-MEMORY | `02_analyze-requirements/` |
| 4 | generate-tc | Sinh test case + consolidate/sync vào TC-MASTER | `03_test-cases/[v]/` |
| 5 | review-tc | Review chất lượng TC (independent reviewer agent) | `11_tc-review/` |
| 6 | scan-source-code | N/A (no automation) | `10_source-code/` |
| 7 | implement-automation | N/A (no automation) | `10_source-code/` |
| 8 | review-src-tc | N/A (no automation) | `11_tc-review/` |
| 9 | vibe-test | Chạy TC qua Appium MCP trên app FoxPro — AI thay manual tester | `08_test-runs/vibe/` |
| 10 | execute-maintain | N/A (no automation) | `08_test-runs/` |
| 11 | log-bug | Ghi nhận bug (+ push Jira nếu bật sau) | `05_bug-reports/` |
| 12 | test-report | Báo cáo tổng kết stakeholder | `09_reports/` |
| 13 | health-check | Validate consistency cross-file, cross-cutting | inline / `09_reports/` |

> `fetch-us` (kéo User Story từ Jira) là **skill tiện ích độc lập**, KHÔNG nằm trong 13 skill pipeline chính ở trên — chưa dùng được vì dự án chưa cấu hình Jira (xem §Jira Integration trong `Project_rule.md`).

## 3. Prerequisites

- Skill chỉ chạy khi prerequisite phía trước đã hoàn tất (theo flow §1).
- `analyze-requirements` cần tài liệu trong `00_input/[version]/`.
- `generate-tc` cần output của `analyze-requirements`.
- `vibe-test` cần TC-MASTER (từ `generate-tc --consolidate`) và app FoxPro đã tích hợp SDK FoxEco (build test) sẵn sàng trên thiết bị/emulator.
- Nhánh automation (`implement-automation`, `execute-maintain`) tạm N/A cho tới khi chạy `/init-source-code`.

## 8. Pipeline Status (snapshot tổng quan cross-version — xem MASTER-MEMORY.md để có chi tiết per-version)

| # | Skill | Đã dùng ở version nào | Ghi chú |
|---|-------|------------------------|---------|
| 1 | init-project | v1.0 | ✅ COMPLETED |
| 2 | create-test-plan | — | ⬜ NOT_STARTED |
| 3 | analyze-requirements | v1.0 | ✅ COMPLETED — 2026-07-24, 40 REQ/62 SC (8 module), 16 clarification (1 BLOCKER cứng còn lại: C-ORD-02 — C-USR-01/C-DLV-01/C-GIFT-01 đã Resolved/Partially Resolved — xem `02_analyze-requirements/v1.0/MEMORY.md §6`) |
| 4 | generate-tc | — | ⬜ NOT_STARTED |
| 5 | review-tc | — | ⬜ NOT_STARTED |
| 6 | scan-source-code | — | N/A (no automation) |
| 7 | implement-automation | — | N/A (no automation) |
| 8 | review-src-tc | — | N/A (no automation) |
| 9 | vibe-test | — | ⬜ NOT_STARTED |
| 10 | execute-maintain | — | N/A (no automation) |
| 11 | log-bug | — | ⬜ NOT_STARTED |
| 12 | test-report | — | ⬜ NOT_STARTED |
| 13 | health-check | — | ⬜ NOT_STARTED |
