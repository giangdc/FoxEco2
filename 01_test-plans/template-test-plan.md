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
- [x] Functional
- [x] Regression
- [x] Smoke
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
