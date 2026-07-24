# Create Test Plan — Mode RETRO

> `/create-test-plan --retro`
> Khi nào: Project đã chạy (có MEMORY, TC, code), chưa có test plan.

## Workflow

### Step 1: Đọc existing artifacts → auto-extract

| Artifact | Extract gì |
|----------|-----------|
| CLAUDE.md | Project info, env, team, automation |
| MASTER-MEMORY | Version, modules, scenario counts |
| Version MEMORY §3 | Module list, risk levels |
| TC-MASTER | TC counts per module, priority distribution |
| Source MEMORY §1-§2 | Tech stack, framework |
| 07_environments/ | Env configs |

### Step 2: Compile auto-extracted test plan

Trình bày cho user:
```
📋 Auto-extracted từ project hiện có:

- Version: v[X] (từ MASTER-MEMORY)
- Modules in-scope: [list] (từ Version MEMORY §3)
- Test types: Functional, Regression (từ CLAUDE.md)
- Approach: Combined — Auto: [modules có code] | Manual: [modules chưa có]
- Quality Gates: G1-G7 defaults (từ Project_rule.md §8.3)

Thiếu thông tin:
  - Schedule (start/end dates)?
  - Risks cụ thể?
  - Resources assignment? (Team mode)

Confirm auto-extracted info + bổ sung thiếu?
```

### Step 3: Hỏi phần thiếu + generate

Chỉ hỏi phần không thể auto-extract (thường 2-3 câu thay vì 10).
Generate test plan giống Mode CREATE.

### Step 4: CLAUDE.md + §8 = COMPLETED
