---
name: init-project
description: Initialize project QA mới với folder structure (00_..11_, version-aware), CLAUDE.md, Project_rule.md, PIPELINE.md, COMMANDS.md, README. Use when user mentions 'init project', 'new test project', 'manual testing setup', 'QA project scaffold', 'test folder structure', or runs /init-project command.
license: Proprietary — FPT QA Toolkit v1.0 (qc-claude-v1)
compatibility: Designed for Claude Code QA projects with 00_..11_ folder structure (qc-claude-v1). Requires Claude Code or compatible agent runtime.
metadata:
  toolkit: qc-claude-v1
  pipeline-position: "1"
  status-section: MASTER-MEMORY-section-8
  owner: QC Team
  version: "1.0"
  released: "2026-06-05"
---

# Init Manual Project

Tạo folder structure + starter files cho project QA mới, version-aware từ đầu.

## Command

| Command | Mô tả |
|---------|-------|
| `/init-project` | Scaffold project mới, Claude hỏi từng bước |

## Prerequisites

Không có — đây là skill đầu tiên trong pipeline.

## Pipeline

**★ init-project ★** → `create-test-plan` → `analyze-requirements` → ...

**Folder sở hữu:** root, `00_`–`11_`

## Workflow

> Skill đơn giản — không tách modes. Toàn bộ logic trong file này.

### Step 1: Gather Project Info

Hỏi **từng câu một**, skip nếu đã rõ từ context:

| # | Câu hỏi | Default |
|---|---------|---------|
| Q1 | Tên dự án? (kebab-case) | — |
| Q2 | Môi trường test? (DEV, STG, UAT, PROD) | STG |
| Q3 | URL từng môi trường? | — |
| Q4 | Loại kiểm thử? (Functional, Regression, Smoke...) | Functional, Regression |
| Q5 | Solo hay Team? | Solo |
| Q6 | Ngôn ngữ viết TC? | Tiếng Việt |
| Q7 | Automation? Framework gì? | Không có |
| Q8 | Version đầu tiên? | v1.0 |
| Q9 | Tên QC phụ trách workspace này? | — |
| Q10 | Link Jira dự án? (vd `https://<site>.atlassian.net/browse/PRJ-1` — để map site + project key) | Không dùng Jira |
| Q11 | Tài liệu dự án đánh số requirement kiểu gì? (`FR/VR` · `AC` · `UC` · `US-key` · `none` = không đánh số) | Chưa rõ (`auto`) |

Confirm summary trước khi scaffold.

> **Per-workspace mapping (2026-06-05):** Q9/Q10 giúp skill **tự map theo workspace mỗi người** —
> mỗi member tự init, tự khai tên + link Jira → `fetch-us`/`log-bug` đọc config từ workspace của chính họ,
> không dùng chung file mẫu hardcode. Parse Q10: `site` = `https://<site>.atlassian.net`,
> `project_key` = mã project trong link (vd `PRJ`).

### Step 2: Scaffold folder structure

```
<project>/
├── 00_input/v[X]/, shared/
├── 01_test-plans/
├── 02_analyze-requirements/v[X]/, Project_rule.md
├── 03_test-cases/v[X]/functional/, fragments/
├── 04_test-data/valid/, invalid/
├── 05_bug-reports/
├── 06_checklists/
├── 07_environments/
├── 08_test-runs/vibe/
├── 09_reports/
├── 10_source-code/ (nếu automation = yes)
├── 11_tc-review/
├── CLAUDE.md
├── README.md
├── PIPELINE.md          ★ AUTO-GENERATED
├── COMMANDS.md          ★ AUTO-GENERATED
```

### Step 3: Generate PIPELINE.md

Đọc template từ `root/PIPELINE.md` (trong skill package) → customize:
- Skill registry: giữ nguyên 13 pipeline skills
- Prerequisites: giữ nguyên
- §8 Pipeline Status: tạo table với init-project = COMPLETED, rest = NOT_STARTED
- Nếu automation = no → đánh dấu scan-source-code, implement-automation, review-src-tc = "N/A (no automation)"

### Step 4: Generate COMMANDS.md

Đọc template từ `root/COMMANDS.md` (trong skill package) → customize:
- Nếu automation = no → ẩn section 5 (Automation), section 6 (Review SRC-TC)
- Nếu solo mode → ẩn `--member` flags
- Pipeline flow section: adjust theo automation yes/no

### Step 5: Generate Project_rule.md
Tạo `02_analyze-requirements/Project_rule.md` — điền từ Q1-Q11.
Section §10 Custom Rules: để trống cho user bổ sung sau.

**Block `## Jira Integration` (NEW 2026-06-05):**
- Nếu Q10 có link Jira → sinh block theo template `references/jira-block-template.md`:
  điền `qc_name` (Q9), `site` + `project_key` (parse từ Q10); các field còn lại để default/TBD
  (log-bug tự khám phá khi chạy `--push-jira` lần đầu rồi ghi ngược vào block).
- Nếu Q10 = "Không dùng Jira" → KHÔNG sinh block (fetch-us/log-bug sẽ tự chỉ dẫn bổ sung sau).

**Block `## DOC Notation` (NEW 2026-06-05):**
- Luôn sinh block sau từ Q11 — `analyze-requirements` đọc để dùng đúng ký hiệu requirement của dự án
  (cột `Maps (Ref DOC)` trong traceability, cột `Nguồn` trong test-data-catalog):
  ```
  ## DOC Notation
  req_notation: <FR/VR | AC | UC | US-key | none | auto — từ Q11>
  # FR/VR: doc đánh số Functional/Validation Rule (vd kiểu FCP)
  # none:  doc không đánh số → traceability dùng DOC-ID §section
  # auto:  chưa rõ → analyze-requirements tự phát hiện từ doc ở lần chạy đầu rồi GHI NGƯỢC giá trị thật vào đây
  ```

### Step 6: Generate CLAUDE.md
Project info (gồm **QC phụ trách** từ Q9), automation config, naming conventions, workflow overview, folder reference.
Thêm: "PIPELINE.md và COMMANDS.md ở root — tester đọc COMMANDS.md để biết cách gọi skill."

### Step 7: Generate starter files
Chạy `scripts/scaffold.py` (hoặc tương đương) để tạo template files:
- template-test-plan.md, template-bug-report.md, etc.
- environments.md
- README.md

### Step 8: Present + next steps
```
✅ Project [name] scaffolded — version v[X]

📁 Root files:
  CLAUDE.md ✅ | PIPELINE.md ✅ | COMMANDS.md ✅ | README.md ✅

📋 Tester chỉ cần đọc: COMMANDS.md → copy-paste lệnh

Next steps:
  1. /create-test-plan --create → /analyze-requirements --init @00_input/v[X]/
  2. (Khi tới Phase automation) /init-source-code --archetype <stack> ← NEW 2026-05-31
     Available archetypes: playwright-ts (web), selenium-java (web), appium-java (mobile)
     Tự động scaffold 10_source-code/ với build config + Page Object base + MEMORY §2 Tech Stack.
     Thay vì manual clone từ GitLab archetype.
```

**Note 2026-05-31:** Nếu user chọn automation = "Có" trong Q7, suggest run `/init-source-code` ngay sau init-project. Skill `init-source-code` standalone — KHÔNG cần chạy ngay, có thể defer đến khi cần. Xem `~/.claude/skills/init-source-code/SKILL.md`.

## Status Protocol

init-project tạo §8 lần đầu (trong PIPELINE.md).
Khi analyze-requirements chạy → tạo MASTER-MEMORY với §8 table.

## Examples

### Example 1: Solo manual testing project
**Input:** `/init-project`
**Behavior:** Hỏi 11 câu (name, env, URL, test types, mode, language, automation, version, tên QC, link Jira, ký hiệu requirement)
**Output:** 12 folders + CLAUDE.md + PIPELINE.md + COMMANDS.md + README.md + Project_rule.md (kèm block `## Jira Integration` nếu có link Jira + block `## DOC Notation`)

### Example 2: Team mode với automation
**Input:** `/init-project` → answer: Team, Selenium Java
**Behavior:** Same scaffolding + `10_source-code/` skeleton + member assignment columns in TC template.

### Example 3: Mobile project
**Input:** `/init-project` → answer: app type=mobile, Appium
**Behavior:** Skip env URL, add appPackage to CLAUDE.md, suggest emulator setup.

## Common Edge Cases

| Scenario | Handling |
|----------|----------|
| Folder name đã tồn tại | Hỏi user overwrite hoặc rename |
| Project name có dấu/space | Auto convert kebab-case (e.g., "Báo Cáo" → "bao-cao") |
| Không có env URL ban đầu | Skip, dùng TBD placeholder, update sau |
| Solo nhưng có ý định scale Team | Default Solo, document path để upgrade |
| Automation = "Chưa quyết định" | Skip `10_source-code/`, có thể add sau |
| Version chưa biết | Default v1.0 |
| Existing folder structure khác convention | Suggest `/analyze-requirements --migrate` thay vì init từ đầu |

