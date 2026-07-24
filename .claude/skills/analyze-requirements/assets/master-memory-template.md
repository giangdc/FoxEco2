# MASTER-MEMORY — Cross-Version Registry

> Cập nhật lần cuối: [date]
> Active version: v[VERSION]

## 1. Version Registry
| Version | Release Date | Input Folder | Analyze Folder | Status | Tổng DOC | Tổng SC (all) | Tổng SC (new+mod) | Parent |
|---------|-------------|-------------|----------------|--------|----------|--------------|-------------------|--------|

## 2. DOC ID Registry (Global)
| DOC ID | Version | File | Loại | Modules |
|--------|---------|------|------|---------|

## 3. Scenario Lifecycle (Cross-Version)
> Canonical = per-SC (theo dõi lifecycle từng SC qua các version). Version ĐẦU (tất cả NEW) có thể dùng roll-up gọn `| Module | Origin | Lifecycle | Count |`; từ delta version trở đi, liệt kê per-SC cho MODIFIED/CARRIED/DEPRECATED.

| SC ID | Tên ngắn | Module | Origin | Lifecycle |
|-------|----------|--------|--------|-----------|

## 4. Regression Scope
### v[VERSION]
**Phải test (new + modified):**
| SC ID | Type | Lý do |

**Nên regression (carried — high risk):**
| SC ID | Type | Lý do |

**Không cần test (carried — low risk, stable):**
| SC ID | Type | Lý do |

## 5. Version Comparison
(Từ v2 trở đi)

## 6. TC Files Registry
| Version | TC-MASTER File | Tổng TC | Ngày consolidate | Status |
|---------|---------------|---------|-------------------|--------|

## 7. Downstream Path Registry
| Skill | Active Version Path |
|-------|-------------------|

## 8. Pipeline Status — v[ACTIVE_VERSION]
> Thứ tự + tên skill khớp PIPELINE.md (toolkit qc-claude-v1: 0.5 init-source-code + 13 skill). Status ∈ NOT_STARTED / IN_PROGRESS / PARTIAL / COMPLETED / SKIPPED / FAILED.

| # | Skill | Status | Last Run | Scope | Output | Notes |
|---|-------|--------|----------|-------|--------|-------|
| 0.5 | init-source-code | NOT_STARTED | — | — | — | archetype (playwright-ts/selenium-java/appium-java) — optional, standalone |
| 1 | init-project | COMPLETED | [date] | — | CLAUDE.md/PIPELINE.md/COMMANDS.md | — |
| 2 | create-test-plan | NOT_STARTED | — | — | — | — |
| 3 | analyze-requirements | IN_PROGRESS | [date] | v[X] | — | — |
| 4 | generate-tc | NOT_STARTED | — | — | — | — |
| 5 | review-tc | NOT_STARTED | — | — | — | — |
| 6 | scan-source-code | NOT_STARTED | — | — | — | — |
| 7 | implement-automation | NOT_STARTED | — | — | — | — |
| 8 | review-src-tc | NOT_STARTED | — | — | — | — |
| 9 | vibe-test | NOT_STARTED | — | — | — | — |
| 10 | execute-maintain | NOT_STARTED | — | — | — | — |
| 11 | log-bug | NOT_STARTED | — | — | — | — |
| 12 | test-report | NOT_STARTED | — | — | — | — |
| 13 | health-check | NOT_STARTED | — | — | — | — |

## 9. Notes
- Ghi mốc lifecycle cross-version, quyết định scope, blocker BA, sweep/health-check results không suy ra được từ code/§khác. Convert ngày tương đối → tuyệt đối.
