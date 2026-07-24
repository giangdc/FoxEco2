# Create Test Plan — Mode CREATE

> `/create-test-plan --create` | `/create-test-plan --create --version v2.0`

## Input → Output

| Input | Output |
|-------|--------|
| CLAUDE.md, Project_rule.md, MASTER-MEMORY (nếu có) | `01_test-plans/TP-[TYPE]-[PROJECT]-v[X].md` |
| 00_input/[version]/ (quick scan), 07_environments/ | CLAUDE.md (append) |

## Workflow

### Step 1: Đọc context

```
1. CLAUDE.md (root)                               → project info, env, team
2. 02_analyze-requirements/Project_rule.md        → rules, naming, version conventions
3. 02_analyze-requirements/MASTER-MEMORY.md       → version registry (nếu có)
4. 07_environments/                               → env configs
5. 00_input/v[VERSION]/ (quick scan)              → list files, identify modules
```

Xác định version:
- MASTER-MEMORY có → dùng active version
- Không có → hỏi user
- Quick scan `00_input/v[VERSION]/` để list documents (KHÔNG deep analysis)

Ghi §8 = IN_PROGRESS.

### Step 2: Thu thập decisions từ user

Hỏi **từng câu một**, skip câu đã có từ CLAUDE.md/MASTER-MEMORY:

| # | Câu hỏi | Nguồn auto | Default |
|---|---------|-----------|---------|
| Q1 | Test plan type? (Master / Release / Sprint / Feature) | — | Master |
| Q2 | Objectives? (Verify requirements, Regression, UAT, Performance) | — | Verify requirements |
| Q3 | Modules in-scope / out-of-scope? | Quick scan 00_input/ | All in-scope |
| Q4 | Test types? (Functional, UI, Integration, Regression, Smoke, UAT) | CLAUDE.md | Functional, Regression |
| Q5 | Approach per module? (Manual / Automation / Combined) | CLAUDE.md automation info | Combined nếu có automation |
| Q6 | Entry criteria? | — | Build deployed + data ready |
| Q7 | Exit criteria / Quality Gates? | Project_rule.md §8.3 | G1-G7 defaults |
| Q8 | Schedule? (Start → End, milestones) | — | Hỏi user |
| Q9 | Resources? (Team mode) | CLAUDE.md team info | — |
| Q10 | Risks? | — | Hỏi user |

### Step 3: Generate test plan

**File:** `01_test-plans/TP-[TYPE]-[PROJECT]-v[VERSION].md`

```markdown
# Test Plan: [Project Name] — v[VERSION]

## 1. Giới thiệu
- **Dự án:** [tên]
- **Version:** v[VERSION]
- **Loại:** [Master / Release / Sprint]
- **Mục tiêu:** [từ Q2]
- **Ngày tạo:** [date]

## 2. Phạm vi (Scope)

### 2.0. Version Context
- **Version:** v[VERSION]
- **Parent version:** v[PARENT] (nếu có)
- **Delta:** [mô tả thay đổi so với parent]

### 2.1. Trong phạm vi (In Scope)
| # | Module | Mô tả | Test Approach |
|---|--------|-------|--------------|
| 1 | [module] | [mô tả] | Manual / Auto / Combined |

### 2.2. Ngoài phạm vi (Out of Scope)
| # | Module / Feature | Lý do |
|---|-----------------|-------|

## 3. Test Approach
| Module | Manual | Automation | Priority | Ghi chú |
|--------|--------|-----------|----------|---------|

## 4. Entry & Exit Criteria

### Entry Criteria
- Build đã deploy lên [environment]
- Test data đã chuẩn bị xong
- [custom criteria]

### Exit Criteria / Quality Gates
| # | Gate | Criteria | Source |
|---|------|----------|--------|
| G1 | TC Review | Score ≥ 70 | review-tc |
| G2 | P1 Pass | 100% | execute-maintain |
| G3 | Overall Pass | ≥ 90% | execute-maintain |
| G4 | P1 Bugs | 0 open | log-bug |
| G5 | Bug Fix Rate | ≥ 80% | log-bug |
| G6 | Blocked | ≤ 0 | execute-maintain |
| G7 | SRC-TC Match | Score ≥ 70 | review-src-tc |

## 5. Test Environment
| Environment | URL | Purpose |
|------------|-----|---------|
| [từ CLAUDE.md / 07_environments/] |

## 6. Resources & Schedule
### Schedule
| Giai đoạn | Bắt đầu | Kết thúc | Owner |
|-----------|---------|----------|-------|

### Resources (Team mode)
| Thành viên | Vai trò | Module phụ trách |
|-----------|---------|-----------------|

## 7. Risk Assessment
| # | Rủi ro | Mức ảnh hưởng | Xác suất | Biện pháp |
|---|--------|-------------|----------|-----------|

## 8. Deliverables
| # | Deliverable | Folder | Status |
|---|------------|--------|--------|
| 1 | Test Plan | 01_test-plans/ | ✅ |
| 2 | Requirement Analysis | 02_analyze-requirements/v[VERSION]/ | ⏳ |
| 3 | TC-MASTER | 03_test-cases/v[VERSION]/TC-MASTER-v[VERSION].xlsx | ⏳ |
| 4 | TC Review Report | 11_tc-review/ | ⏳ |
| 5 | Vibe Test Report | 08_test-runs/vibe/ | ⏳ |
| 6 | SRC-TC Review Report | 11_tc-review/ | ⏳ |
| 7 | Test Run Log | 08_test-runs/ | ⏳ |
| 8 | Summary Report | 09_reports/ | ⏳ |

## 9. Approval
| Vai trò | Tên | Ngày | Chữ ký |
|---------|-----|------|--------|

## 10. Revision History
| Version | Date | Changed By | Changes |
|---------|------|-----------|---------|
| 1.0 | [date] | [name/Claude AI] | Initial creation |
```

### Step 4: Update CLAUDE.md

```markdown
## Test Plan — v[VERSION]
- **Document:** `01_test-plans/TP-[TYPE]-[PROJECT]-v[VERSION].md`
- **Scope IN:** [list modules]
- **Scope OUT:** [list + reason]
- **Approach:** Manual: [modules] | Automation: [modules]
- **Exit criteria (= Quality Gates):** G1-G7 (xem test plan)
```

### Step 5: Present + handoff

```
✅ Test Plan v[VERSION] created: 01_test-plans/TP-[TYPE]-[PROJECT]-v[VERSION].md

📋 Next:
  /analyze-requirements --init @00_input/v[VERSION]/
  → analyze-requirements sẽ đọc §2 Scope từ test plan.
```

Ghi §8 = COMPLETED.

## Checklist

- [ ] Test plan file trong 01_test-plans/ với version suffix
- [ ] Version context section (§2.0)
- [ ] Scope In/Out clearly defined per version
- [ ] Entry/Exit criteria measurable → Quality Gates G1-G7
- [ ] Risk register có mitigation
- [ ] Deliverable paths version-aware
- [ ] CLAUDE.md append scope + criteria
- [ ] §8 = COMPLETED
