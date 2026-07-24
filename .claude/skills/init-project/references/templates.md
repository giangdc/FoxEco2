# Templates Reference (Multi-Version Framework)

All starter templates for the manual testing project scaffold.
Updated for multi-version support with MASTER-MEMORY, TC-MASTER, and Project_rule.md.

> ⚠️ **Canonical source = `scripts/scaffold.py`** (runtime sinh file thật từ các hàm `template_*`). File này là bản minh hoạ/đối chiếu — khi sửa template, sửa trong `scaffold.py` để tránh drift giữa 2 nơi.

## Table of Contents
1. [Test Plan](#test-plan)
2. [Test Case](#test-case)
3. [Bug Report](#bug-report)
4. [Smoke Checklist](#smoke-checklist)
5. [Release Checklist](#release-checklist)
6. [Environments](#environments)
7. [Test Run Log](#test-run-log)
8. [Summary Report](#summary-report)
9. [README](#readme)
10. [CLAUDE.md](#claudemd)
11. [Source Code MEMORY](#source-code-memory)

---

## Test Plan

File: `01_test-plans/template-test-plan.md`

**Thay đổi so với cũ:**
- Thêm section "Version Context"
- Exit Criteria → Quality Gates (G1-G7) — measurable
- Thêm section "Deliverables" với version-aware paths
- Thêm G7 SRC-TC Match gate

```markdown
# Test Plan: [Feature / Release Name]

## Mục tiêu (Objective)
Mô tả những gì đang được kiểm thử và lý do.

## Version Context
- **Version:** [version]
- **Parent version:** — (hoặc version trước)
- **Delta:** [Mô tả thay đổi so với version trước]

## Phạm vi (Scope)
### Trong phạm vi (In Scope)
-

### Ngoài phạm vi (Out of Scope)
-

## Loại kiểm thử (Test Types)
- [ ] Functional
- [ ] Regression
- [ ] Smoke
- [ ] UAT
- [ ] Exploratory
- [ ] Performance

## Điều kiện bắt đầu (Entry Criteria)
- Build đã deploy lên [environment]
- Test data đã chuẩn bị xong

## Điều kiện kết thúc (Exit Criteria / Quality Gates)
- G1: TC Review score ≥ 70
- G2: P1 pass rate = 100%
- G3: Overall pass rate ≥ 90%
- G4: No P1 bugs open
- G5: Bug fix rate ≥ 80%
- G6: Blocked ≤ 0
- G7: SRC-TC match score ≥ 70 (nếu có automation)

## Rủi ro & Biện pháp (Risks & Mitigations)
| Rủi ro | Mức ảnh hưởng | Biện pháp |
|--------|---------------|-----------|
|        |               |           |

## Lịch trình (Schedule)
| Giai đoạn | Bắt đầu | Kết thúc |
|-----------|---------|----------|
|           |         |          |

## Nguồn lực (Resources)
- Tester(s):
- Environment:
- Test data owner:

## Deliverables
| # | Deliverable | Folder | Status |
|---|------------|--------|--------|
| 1 | Test Plan | 01_test-plans/ | ✅ |
| 2 | Requirement Analysis | 02_analyze-requirements/[version]/ | ⏳ |
| 3 | TC-MASTER | 03_test-cases/[version]/TC-MASTER-[version].xlsx | ⏳ |
| 4 | TC Review Report | 11_tc-review/ | ⏳ |
| 5 | SRC-TC Review Report | 11_tc-review/ | ⏳ |
| 6 | Test Run Log | 08_test-runs/ | ⏳ |
| 7 | Summary Report | 09_reports/ | ⏳ |
```

### Team mode additions (giữ nguyên)
```markdown
## Phân công (Assignments)
| Thành viên | Vai trò | Module phụ trách |
|------------|---------|-----------------|
|            |         |                 |
```

---

## Test Case

File: `03_test-cases/[version]/functional/TC-001-template.md`

**Thay đổi so với cũ:**
- Thêm fields: Testcase ID, Scenario ID, Req ID, DOC Source, Group, Version Origin, Lifecycle
- DOC Source format mới: `DOC-v[VERSION]-[NN]`
- Steps và Expected tách riêng (1:1 mapping)

```markdown
# TC-[MODULE]-[NNN]: [Tên Test Case]

| Field        | Value                        |
|--------------|------------------------------|
| Testcase ID  | TC-[MODULE]-[NNN]            |
| Scenario ID  | SC-[MODULE]-[NNN]            |
| Req ID       | REQ-[MODULE]-[NNN]           |
| DOC Source   | DOC-v[VERSION]-[NN]          |
| Module       |                              |
| Group        | Functional / Validation / UI |
| Priority     | P1 / P2 / P3                 |
| Version Origin |                            |
| Lifecycle    | NEW / CARRIED / MODIFIED     |

## Điều kiện tiên quyết (Preconditions)
-

## Dữ liệu kiểm thử (Test Data)
| Field    | Value |
|----------|-------|
|          |       |

## Các bước thực hiện (Steps)
| # | Hành động | Kết quả mong đợi |
|---|-----------|-------------------|
| 1 |           |                   |
| 2 |           |                   |

## Ghi chú (Notes)
-
```

### Team mode additions
```markdown
| Assigned to  |                              |
| Reviewed by  |                              |
```

---

## Bug Report

File: `05_bug-reports/template-bug-report.md`

**Thay đổi so với cũ:**
- Thêm Version field
- Thêm Traceability section đầy đủ (REQ → SC → TC → Method → Fail → Run)
- Steps to Reproduce = copy từ TC-MASTER
- Expected Result = copy từ TC-MASTER

```markdown
# BUG-[NNN]: [Mô tả ngắn]

## Thông tin chung
| Field         | Value                              |
|---------------|------------------------------------|
| Bug ID        | BUG-[NNN]                          |
| Version       |                                    |
| Severity      | Critical / High / Medium / Low     |
| Priority      | P1 / P2 / P3 / P4                 |
| Status        | Open / In Progress / Fixed / Closed |
| Environment   |                                    |
| Build/Version |                                    |
| Reported by   |                                    |
| Reported on   |                                    |
| Assigned to   |                                    |

## Traceability
| Link | ID |
|------|----|
| Requirement | REQ-[MODULE]-[NNN] |
| Scenario | SC-[MODULE]-[NNN] |
| Test Case | TC-[MODULE]-[NNN] |
| Test Method | [Class#method] |
| Fail ID | FAIL-[NNN] |
| Run ID | RUN-[NNN] |

## Tóm tắt (Summary)
Mô tả ngắn gọn về bug trong một dòng.

## Các bước tái hiện (Steps to Reproduce)
(Copy từ TC-MASTER column Steps)
1.
2.
3.

## Kết quả mong đợi (Expected Result)
(Copy từ TC-MASTER column Expected Result)

## Kết quả thực tế (Actual Result)
Mô tả điều gì thực sự xảy ra.

## Đính kèm (Attachments)
- [ ] Screenshot
- [ ] Video
- [ ] Log file

## Ghi chú (Notes)
-
```

---

## Smoke Checklist

File: `06_checklists/smoke-checklist.md`

(Giữ nguyên — không thay đổi)

---

## Release Checklist

File: `06_checklists/release-checklist.md`

**Thay đổi so với cũ:**
- Thêm SRC-TC review check
- Thêm TC Review score check
- Thêm step update MASTER-MEMORY

```markdown
# Release Checklist — [Version]

## Trước Release (Pre-Release)
- [ ] Tất cả bug P1/P2 đã được giải quyết
- [ ] Bộ test Regression đã pass
- [ ] UAT đã được sign-off
- [ ] Release notes đã soạn xong
- [ ] Kế hoạch rollback đã được ghi nhận
- [ ] SRC-TC review score ≥ 70 (nếu có automation)
- [ ] TC Review score ≥ 70

## Ngày Release (Release Day)
- [ ] Smoke test trên production sau khi deploy
- [ ] Theo dõi error logs trong 30 phút
- [ ] Thông báo cho các stakeholders

## Sau Release (Post-Release)
- [ ] Đóng các bug đã resolved trong tracker
- [ ] Lưu trữ kết quả test run
- [ ] Ghi nhận retrospective notes
- [ ] Update MASTER-MEMORY.md version status → "✅ Released"
```

---

## Environments

File: `07_environments/environments.md`

(Giữ nguyên — không thay đổi)

---

## Test Run Log

File: `08_test-runs/template-test-run.md`

**Thay đổi so với cũ:**
- Thêm Version header và Version field
- Thêm SC ID và Version columns trong Fail table

```markdown
# Test Run — [Sprint / Release] — [Ngày]

> Version: [version]

| Field       | Value |
|-------------|-------|
| Version     |       |
| Environment |       |
| Build       |       |
| Tester(s)   |       |
| Ngày bắt đầu |     |
| Ngày kết thúc |     |

## Tổng kết (Summary)
| Tổng | Passed | Failed | Blocked | Skipped |
|------|--------|--------|---------|---------|
|      |        |        |         |         |

## Test Case bị Fail
| TC ID | SC ID | Tiêu đề | Bug ID | Version | Ghi chú |
|-------|-------|---------|--------|---------|---------|
|       |       |         |        |         |         |

## Mục bị Block
| TC ID | Lý do | Người phụ trách |
|-------|-------|-----------------|
|       |       |                 |

## Ghi chú (Notes)
-
```

---

## Summary Report

File: `09_reports/template-summary-report.md`

**Thay đổi so với cũ:**
- Thêm Version header
- Thêm Quality Gates table (G1-G7)
- Thêm Scenario Lifecycle breakdown (NEW/MODIFIED/CARRIED/DEPRECATED)

```markdown
# Báo cáo Tổng kết Kiểm thử — [Release / Sprint]

> Version: [version]

## Tổng quan (Overview)
| Chỉ số            | Giá trị |
|--------------------|---------|
| Version            |         |
| Thời gian kiểm thử |        |
| Environment        |         |
| Build đã test      |         |
| Tổng TC đã chạy   |         |
| Tỷ lệ Pass        |         |
| Bug đã tạo        |         |
| Bug đã resolved    |         |
| Bug P1/P2 còn mở  |         |

## Quality Gates
| # | Gate | Criteria | Result | Status |
|---|------|----------|--------|--------|
| G1 | TC Review | Score ≥ 70 | | ⬜ |
| G2 | P1 Pass | 100% | | ⬜ |
| G3 | Overall Pass | ≥ 90% | | ⬜ |
| G4 | P1 Bugs | 0 open | | ⬜ |
| G5 | Bug Fix Rate | ≥ 80% | | ⬜ |
| G6 | Blocked | ≤ 0 | | ⬜ |
| G7 | SRC-TC Match | Score ≥ 70 | | ⬜ |

## Đánh giá chất lượng (Quality Assessment)
Chất lượng tổng thể: **GO / NO-GO / CONDITIONAL GO**

Lý do:

## Scenario Lifecycle (version breakdown)
| Lifecycle | Count | With TC | Executed | Pass |
|-----------|-------|---------|----------|------|
| NEW       |       |         |          |      |
| MODIFIED  |       |         |          |      |
| CARRIED   |       |         |          |      |
| DEPRECATED|       |         |          |      |

## Rủi ro còn mở (Open Risks)
-

## Khuyến nghị (Recommendation)
- [ ] Chấp nhận release
- [ ] Release với known issues (liệt kê bên dưới)
- [ ] Chặn release
```

---

## README

File: `README.md`

**Thay đổi so với cũ:**
- Folder structure updated (version paths, shared/, 11_tc-review/)
- Naming conventions updated (DOC-v[VERSION]-[NN], TC-MASTER-v[VERSION].xlsx)
- Thêm link đến Project_rule.md

---

## CLAUDE.md

File: `CLAUDE.md`

**Thay đổi so với cũ:**
- Thêm "Version Info" section (current version, MASTER-MEMORY path, Project_rule path)
- Workflow paths version-aware (`00_input/v1.0/`, `02_.../v1.0/`, `03_.../v1.0/`)
- MEMORY Files: 3 files (MASTER-MEMORY, Version MEMORY, Source MEMORY)
- Naming Conventions: DOC-v[VERSION]-[NN], TC-MASTER-v[VERSION].xlsx
- Folder Reference: 13 rows (thêm shared/, version subfolders, 11_tc-review/)

---

## Source Code MEMORY

File: `10_source-code/MEMORY.md` (chỉ khi có automation)

**Thay đổi so với cũ:**
- §1-§11: giữ nguyên structure (populated bởi scan-source-code)
- §12: Locator Registry (populated bởi implement-automation)
- §13: Implementation Log — **MỚI** (TC ID, SC ID, Steps Mapped, Expected Mapped, Manual Verify)
- §14: Locator Issues (populated bởi implement-automation)
- §15: Execution Log — thêm cột Version
- §16: Fail Registry — thêm cột Version
- §17: SRC-TC Review — **MỚI** (populated bởi review-src-tc)

Chi tiết xem trong scaffold.py function `template_source_code_memory()`.
