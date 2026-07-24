#!/usr/bin/env python3
"""
Scaffold a manual testing project with version-aware folder structure and starter templates.
Usage:
    python3 scaffold.py \
        --project-name "my-project" \
        --environments "DEV,STG" \
        --urls "https://dev.example.com,https://stg.example.com" \
        --test-types "Functional,Regression,Smoke" \
        --team-size "solo" \
        --automation "Java 21 + Selenium 4 + TestNG 7" \
        --version "v1.0" \
        --output-dir "/mnt/user-data/outputs"
"""

import argparse
import os
from datetime import date


def parse_args():
    parser = argparse.ArgumentParser(description="Scaffold a manual testing project")
    parser.add_argument("--project-name", required=True, help="Project name (kebab-case)")
    parser.add_argument("--environments", required=True, help="Comma-separated: DEV,STG,UAT,PROD")
    parser.add_argument("--urls", default="", help="Comma-separated URLs matching environments")
    parser.add_argument("--test-types", required=True,
                        help="Comma-separated: Functional,Regression,Smoke,UAT,Exploratory,Performance")
    parser.add_argument("--team-size", default="solo", choices=["solo", "team"],
                        help="solo or team")
    parser.add_argument("--automation", default="",
                        help="Automation framework, e.g. 'Java 21 + Selenium 4 + TestNG 7' or empty")
    parser.add_argument("--version", default="v1.0",
                        help="Initial version (default: v1.0)")
    parser.add_argument("--output-dir", default=".", help="Parent directory for the project")
    return parser.parse_args()


def mkdir(path):
    os.makedirs(path, exist_ok=True)


def write(path, content):
    with open(path, "w", encoding="utf-8") as f:
        f.write(content)


# ---------------------------------------------------------------------------
# Templates
# ---------------------------------------------------------------------------

def build_team_fields_tc():
    return """| Assigned to  |                              |
| Reviewed by  |                              |
"""


def build_team_fields_plan():
    return """
## Phân công (Assignments)
| Thành viên | Vai trò | Module phụ trách |
|------------|---------|-----------------|
|            |         |                 |
"""


def template_test_plan(project_name, test_types, team_size):
    checks = ""
    for tt in ["Functional", "Regression", "Smoke", "UAT", "Exploratory", "Performance"]:
        mark = "x" if tt in test_types else " "
        checks += f"- [{mark}] {tt}\n"

    team_section = build_team_fields_plan() if team_size == "team" else ""

    return f"""# Test Plan: [Feature / Release Name]

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
{checks}
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
{team_section}"""


def template_test_case(team_size):
    team_rows = build_team_fields_tc() if team_size == "team" else ""
    return f"""# TC-[MODULE]-[NNN]: [Tên Test Case]

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
{team_rows}
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
"""


def template_bug_report():
    return """# BUG-[NNN]: [Mô tả ngắn]

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
"""


def template_smoke_checklist(project_name):
    return f"""# Smoke Test Checklist — {project_name}

> Chạy trước mỗi chu kỳ kiểm thử. Nếu bất kỳ mục nào fail, chặn testing và thông báo cho dev.

## Xác thực (Authentication)
- [ ] Người dùng có thể đăng nhập với thông tin hợp lệ
- [ ] Người dùng không thể đăng nhập với thông tin không hợp lệ
- [ ] Luồng quên mật khẩu hoạt động

## Luồng chính (Core Flows)
- [ ] [Luồng quan trọng 1]
- [ ] [Luồng quan trọng 2]
- [ ] [Luồng quan trọng 3]

## Hạ tầng (Infrastructure)
- [ ] Ứng dụng load không có lỗi console
- [ ] API endpoints phản hồi (kiểm tra network tab)
- [ ] Không có hình ảnh bị hỏng hoặc tài nguyên bị thiếu

---
Kiểm thử bởi: ___________  Ngày: ___________  Build: ___________
"""


def template_release_checklist():
    return """# Release Checklist — [Version]

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
"""


def template_environments(envs, urls):
    env_url_map = {}
    for i, env in enumerate(envs):
        env_url_map[env.strip().upper()] = urls[i].strip() if i < len(urls) else ""

    sections = ""
    env_configs = {
        "DEV": ("Không ổn định, chỉ dành cho developer testing", True),
        "STG": ("Dữ liệu mirror từ production (đã ẩn danh)", True),
        "UAT": ("Môi trường cho User Acceptance Testing", True),
        "PROD": ("Chỉ chạy smoke test read-only", False),
    }

    for env in envs:
        env_key = env.strip().upper()
        note, full = env_configs.get(env_key, ("", True))
        url = env_url_map.get(env_key, "")
        if full:
            sections += f"""
## {env_key}
| Field    | Value |
|----------|-------|
| URL      | {url} |
| API URL  |       |
| Database |       |
| Ghi chú | {note} |
"""
        else:
            sections += f"""
## {env_key}
| Field    | Value |
|----------|-------|
| URL      | {url} |
| Ghi chú | {note} |
"""

    return f"""# Test Environments
{sections}
## Tài khoản kiểm thử (Test Accounts)
> Không lưu mật khẩu thực ở đây. Sử dụng password manager của team.

| Vai trò | Username | Ghi chú |
|---------|----------|---------|
| Admin   |          |         |
| User    |          |         |
"""


def template_test_run():
    return """# Test Run — [Sprint / Release] — [Ngày]

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
"""


def template_summary_report():
    return """# Báo cáo Tổng kết Kiểm thử — [Release / Sprint]

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
"""


def template_readme(project_name, test_types, envs, default_env, version):
    tt_str = ", ".join(test_types)
    return f"""# {project_name} — Manual Testing Project

## Mục đích (Purpose)
Dự án kiểm thử thủ công cho **{project_name}**.

## Loại kiểm thử (Test Types)
{tt_str}

## Initial Version
{version}

## Cấu trúc thư mục (Folder Structure)
| Thư mục | Mục đích |
|---------|----------|
| `00_input/[version]/` | Tài liệu đầu vào theo version |
| `00_input/shared/` | Tài liệu dùng chung mọi version |
| `01_test-plans/` | Kế hoạch kiểm thử theo release/feature |
| `02_analyze-requirements/` | MASTER-MEMORY + Project_rule + version analysis |
| `02_analyze-requirements/[version]/` | Kết quả phân tích theo version |
| `03_test-cases/[version]/` | TC-MASTER + fragments theo version |
| `04_test-data/` | Dữ liệu kiểm thử (valid/invalid) |
| `05_bug-reports/` | Báo cáo lỗi |
| `06_checklists/` | Checklist smoke test & release |
| `07_environments/` | Cấu hình môi trường |
| `08_test-runs/` | Log kết quả chạy test theo sprint |
| `09_reports/` | Báo cáo tổng kết cho stakeholders |
| `10_source-code/` | Automation source code + MEMORY tracking |
| `11_tc-review/` | TC review + SRC-TC review reports |

## Quy tắc đặt tên (Naming Conventions)
- Documents: `DOC-v[VERSION]-[NN]`
- Scenarios: `SC-[MODULE]-[NNN]`
- Test cases: `TC-[MODULE]-[NNN]`
- TC Master: `TC-MASTER-v[VERSION].xlsx`
- Bug reports: `BUG-[NNN]-[short-title].md`
- Test runs: `TR-v[VERSION]-[YYYY-MM-DD].md`
- Reports: `REPORT-[TYPE]-v[VERSION]-[DATE].md`

## Môi trường mặc định (Default Environment)
**{default_env}**

## Ngôn ngữ (Language)
- Nội dung test case, mô tả, bước thực hiện: **Tiếng Việt**
- Thuật ngữ kỹ thuật, keywords, status: **Tiếng Anh**

## Project Rules
→ Chi tiết: `02_analyze-requirements/Project_rule.md`

## Liên hệ (Contacts)
- QA Lead:
- Dev Lead:
- PM:
"""


def template_claude_md(project_name, test_types, envs, urls, version, team_size, automation=""):
    tt_str = ", ".join(test_types)
    env_str = ", ".join(envs)
    url_str = ", ".join(urls) if urls else "N/A"
    today = date.today().isoformat()

    auto_section = ""
    if automation:
        auto_section = f"""
## Automation
- **Framework:** {automation}
- **Source code:** `10_source-code/`
- **MEMORY (source-code):** `10_source-code/MEMORY.md`
"""

    workflow_auto = ""
    if automation:
        workflow_auto = """
Nếu có automation:
  → 10_source-code/ (scan-source → implement-auto → fix-sonar)
  → 11_tc-review/ (review-src-tc: compare TC ↔ code)
  → execute-maintain → log-bug → test-report
"""

    return f"""# {project_name} — Project Context

## Thông tin dự án (Project Info)
- **Tên dự án:** {project_name}
- **Loại kiểm thử:** {tt_str}
- **Môi trường:** {env_str}
- **URL:** {url_str}
- **Team:** {"Team" if team_size == "team" else "Solo"}

## Version Info
- **Current version:** {version}
- **Version history:** {version} (initial)
- **MASTER-MEMORY:** `02_analyze-requirements/MASTER-MEMORY.md`
- **Project Rules:** `02_analyze-requirements/Project_rule.md`

## Quy trình làm việc (Workflow)
```
00_input/{version}/ (tài liệu gốc)
  → 01_test-plans/ (create-test-plan)
    → 02_analyze-requirements/{version}/ (analyze-requirements)
      → 03_test-cases/{version}/ (generate-tc → consolidate → TC-MASTER)
        → 11_tc-review/ (review-tc + review-src-tc)
          → 08_test-runs/ (execute)
            → 05_bug-reports/ (log bugs)
              → 09_reports/ (summary report)
{workflow_auto}```

## MEMORY Files
- **MASTER-MEMORY:** `02_analyze-requirements/MASTER-MEMORY.md` — cross-version registry
- **Version MEMORY:** `02_analyze-requirements/{version}/MEMORY.md` — version-scoped analysis
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
| 00 | input/{version}/ | Tài liệu đầu vào (theo version) | analyze-requirements |
| 00 | input/shared/ | Tài liệu dùng chung | analyze-requirements |
| 01 | test-plans/ | Test plan tổng thể | create-test-plan |
| 02 | analyze-requirements/ | MASTER-MEMORY + Project_rule | analyze-requirements |
| 02 | analyze-requirements/{version}/ | Analysis output theo version | analyze-requirements |
| 03 | test-cases/{version}/ | TC-MASTER + fragments | generate-tc |
| 04 | test-data/ | Dữ liệu test | — |
| 05 | bug-reports/ | Báo cáo lỗi | log-bug |
| 06 | checklists/ | Smoke + release checklists | — |
| 07 | environments/ | Config môi trường | — |
| 08 | test-runs/ | Logs chạy test | test-report |
| 09 | reports/ | Báo cáo tổng hợp | test-report |
| 10 | source-code/ | Automation code + MEMORY | scan-source, implement-auto |
| 11 | tc-review/ | Review reports (TC + SRC-TC) | review-tc, review-src-tc |
{auto_section}
## Project Rules
→ Xem chi tiết: `02_analyze-requirements/Project_rule.md`

## Tools
- Manual testing project scaffolded by `init-manual-project` skill
- Framework version: Multi-Version (MASTER-MEMORY enabled)
- Created on: {today}
"""


def template_source_code_memory(project_name, automation):
    today = date.today().isoformat()
    return f"""# MEMORY — Source Code Context

> File này tracking cấu trúc source code automation.
> Tách biệt với 02_analyze-requirements/[version]/MEMORY.md (tracking requirement analysis).
> Cập nhật lần cuối: {today}

## 1. Project Structure
> Chạy skill scan-source-code để tự động điền section này.

```
10_source-code/
├── (chưa có source code — copy hoặc clone source code vào đây)
└── MEMORY.md
```

## 2. Tech Stack
| Component | Version | Ghi chú |
|-----------|---------|---------|
| Framework | {automation} | |

> Chạy scan-source-code để extract versions từ pom.xml/build.gradle.

## 3. Config
> Sẽ được extract tự động từ source code.

## 4. Base Classes
> Sẽ được extract tự động.

## 5. Conventions
> Sẽ được extract tự động từ source code hiện có khi chạy scan-source-code.

## 6. Page Classes Registry
| Page Class | File Path | Elements | Methods | Scenarios Cover | Last Updated |
|------------|-----------|----------|---------|-----------------|-------------|

## 7. Test Classes Registry
| Test Class | File Path | Test Methods | Scenarios Cover | Status |
|------------|-----------|-------------|-----------------|--------|

## 8. Utilities
> Sẽ được extract tự động.

## 9. Coverage Gap
> Sẽ được tạo bởi scan-source-code.

## 10. Scan History
| Ngày | Mode | Scope | Ghi chú |
|------|------|-------|---------|

## 11. Issues
| # | Issue | Severity | Status |
|---|-------|----------|--------|

## 12. Locator Registry
> Sử dụng MCP Playwright để lấy locator từ web thực.

| Element | Strategy | Value | Page | Date |
|---------|----------|-------|------|------|

## 13. Implementation Log
| TC ID | SC ID | Test Method | Steps Mapped | Expected Mapped | Manual Verify | Member | Date |
|-------|-------|-------------|-------------|----------------|--------------|--------|------|

## 14. Locator Issues
| Element | Page | Issue | Status | Ngày phát hiện |
|---------|------|-------|--------|---------------|

## 15. Execution Log
| Run ID | Date | Version | Scope | Command | Total | Pass | Fail | Skip | Pass Rate |
|--------|------|---------|-------|---------|-------|------|------|------|-----------|

## 16. Fail Registry
| Fail ID | Run ID | Date | Version | Class.Method | SC ID | Fail Type | Error | Status | Bug ID |
|---------|--------|------|---------|-------------|-------|-----------|-------|--------|--------|

## 17. SRC-TC Review
| Date | Version | Mode | Score | Step Cov | Assert Cov | Verdict |
|------|---------|------|-------|----------|------------|---------|
"""


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main():
    args = parse_args()

    project = args.project_name
    envs = [e.strip() for e in args.environments.split(",") if e.strip()]
    urls = [u.strip() for u in args.urls.split(",") if u.strip()] if args.urls else []
    test_types = [t.strip() for t in args.test_types.split(",") if t.strip()]
    team = args.team_size
    version = args.version.strip()
    root = os.path.join(args.output_dir, project)
    automation = args.automation.strip() if args.automation else ""

    # --- Create version-aware folder structure ---

    # 00_input — version folders
    mkdir(os.path.join(root, "00_input", version))
    mkdir(os.path.join(root, "00_input", "shared"))

    # 01_test-plans
    mkdir(os.path.join(root, "01_test-plans"))

    # 02_analyze-requirements — root + version folder
    mkdir(os.path.join(root, "02_analyze-requirements", version))

    # 03_test-cases — version folder with fragments
    mkdir(os.path.join(root, "03_test-cases", version, "fragments"))
    # Also create type subfolders inside version if needed for manual TCs
    mkdir(os.path.join(root, "03_test-cases", version, "functional"))

    # 04_test-data
    mkdir(os.path.join(root, "04_test-data", "valid"))
    mkdir(os.path.join(root, "04_test-data", "invalid"))

    # 05-09
    mkdir(os.path.join(root, "05_bug-reports"))
    mkdir(os.path.join(root, "06_checklists"))
    mkdir(os.path.join(root, "07_environments"))
    mkdir(os.path.join(root, "08_test-runs"))
    mkdir(os.path.join(root, "09_reports"))

    # 10_source-code (if automation)
    if automation:
        mkdir(os.path.join(root, "10_source-code"))
        write(os.path.join(root, "10_source-code", "MEMORY.md"),
              template_source_code_memory(project, automation))

    # 11_tc-review
    mkdir(os.path.join(root, "11_tc-review"))

    # --- Write template files ---

    write(os.path.join(root, "01_test-plans", "template-test-plan.md"),
          template_test_plan(project, test_types, team))

    # TC template in version/functional/
    tc_dir = os.path.join(root, "03_test-cases", version, "functional")
    write(os.path.join(tc_dir, "TC-001-template.md"), template_test_case(team))

    write(os.path.join(root, "05_bug-reports", "template-bug-report.md"), template_bug_report())
    write(os.path.join(root, "06_checklists", "smoke-checklist.md"), template_smoke_checklist(project))
    write(os.path.join(root, "06_checklists", "release-checklist.md"), template_release_checklist())
    write(os.path.join(root, "07_environments", "environments.md"), template_environments(envs, urls))
    write(os.path.join(root, "08_test-runs", "template-test-run.md"), template_test_run())
    write(os.path.join(root, "09_reports", "template-summary-report.md"), template_summary_report())

    default_env = envs[0] if envs else "DEV"
    write(os.path.join(root, "README.md"),
          template_readme(project, test_types, envs, default_env, version))
    write(os.path.join(root, "CLAUDE.md"),
          template_claude_md(project, test_types, envs, urls, version, team, automation))

    # --- Add .gitkeep to empty dirs ---
    for gk_dir in [
        os.path.join(root, "00_input", version),
        os.path.join(root, "00_input", "shared"),
        os.path.join(root, "02_analyze-requirements", version),
        os.path.join(root, "03_test-cases", version, "fragments"),
        os.path.join(root, "11_tc-review"),
    ]:
        contents = os.listdir(gk_dir) if os.path.exists(gk_dir) else []
        if not contents:
            write(os.path.join(gk_dir, ".gitkeep"), "")

    # --- Print summary ---
    print(f"✅ Project scaffolded successfully: {root}")
    print(f"   Version: {version}")
    print(f"   Environments: {', '.join(envs)}")
    print(f"   Test types: {', '.join(test_types)}")
    print(f"   Team mode: {team}")
    if automation:
        print(f"   Automation: {automation}")
        print(f"   Source-code MEMORY: 10_source-code/MEMORY.md (§1-§17)")
    print(f"\n📁 Folder structure:")
    for dirpath, dirnames, filenames in sorted(os.walk(root)):
        level = dirpath.replace(root, "").count(os.sep)
        indent = "│   " * level
        basename = os.path.basename(dirpath)
        if level == 0:
            print(f"   {project}/")
        else:
            print(f"   {indent}├── {basename}/")
        subindent = "│   " * (level + 1)
        for f in sorted(filenames):
            print(f"   {subindent}├── {f}")

    print(f"\n📋 Next steps:")
    print(f"   1. Đặt tài liệu requirement vào 00_input/{version}/")
    print(f"   2. Chạy: 'Tạo test plan cho {version}'")
    print(f"   3. Chạy: 'Phân tích tài liệu {version}'")


if __name__ == "__main__":
    main()
