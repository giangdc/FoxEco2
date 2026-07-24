---
name: test-report
description: "Tổng hợp tất cả test sources thành stakeholder report. Hỗ trợ multi-version + cross-version comparison + GO/NO-GO recommendation. 5 modes: SPRINT, RELEASE, ADHOC, CROSS-VERSION, TREND. Use when user mentions 'tạo báo cáo test', 'test report', 'summary report', 'GO NO-GO', 'test summary', 'xuất report', 'so sánh version', or runs /test-report command (alias /report)."
license: Proprietary — FPT QA Toolkit v1.0 (qc-claude-v1)
compatibility: Designed for Claude Code QA projects with 00_..11_ folder structure (qc-claude-v1). Requires Claude Code or compatible agent runtime.
metadata:
  toolkit: qc-claude-v1
  pipeline-position: "12"
  status-section: MASTER-MEMORY-section-8
  owner: QC Team
  version: "1.1"
  released: "2026-06-05"
  updated: "2026-07-21 — align với template ISC: đọc KPI trực tiếp từ sheet Report Test/Dashboard/RTM (pre-computed formula) thay vì tự tính lại từ raw parse; Priority label High/Medium/Low (giữ P1-3 làm shorthand hiển thị); Bug severity Critical/Major/Medium/Low (khớp log-bug/Bug Data sheet)."
---

# Test Report

Aggregation skill — đọc mọi thứ, tổng hợp thành báo cáo cho stakeholders.

## Command

| Command | Mode | Mô tả |
|---------|------|-------|
| `/test-report --sprint S05` | SPRINT | Báo cáo sprint |
| `/test-report --release --version v2.0` | RELEASE | GO/NO-GO report |
| `/test-report --cross-version v1.0 v2.0` | CROSS-VERSION | So sánh versions |
| `/test-report --adhoc` | ADHOC | Report tại thời điểm hiện tại |
| `/test-report --trend` | TREND | Xu hướng pass rate, bug rate |

Options: `--version vX.Y`

## Prerequisites

| Cần có | Check |
|--------|-------|
| Ít nhất 1 execution run trong §15 | execute-maintain ≥ COMPLETED |

## Pipeline

Skill cuối: `execute-maintain` + `log-bug` → **★ test-report ★**

**Folder sở hữu:** `08_test-runs/`, `09_reports/`

## Mode Routing

| Condition | → Load |
|-----------|--------|
| `--sprint` | `references/sprint.md` |
| `--release` hoặc "GO NO-GO" | `references/release.md` |
| `--cross-version` | `references/cross-version.md` |
| `--trend` | `references/trend.md` |
| Default | `references/adhoc.md` |

## Sources (đọc tất cả, version-filtered)

CLAUDE.md, Project_rule.md §8, MASTER-MEMORY, Version MEMORY, **TC-MASTER (alias file ISC — ưu tiên đọc KPI đã tính sẵn ở sheet `Report Test`/`Dashboard`/`RTM` thay vì tự parse lại từng row Test Cases, xem `references/release.md` §Sources)**, TC review report, SRC-TC review, Source MEMORY §15-§16, bug-index (+ `Bug Data` sheet trong TC-MASTER), risk_assessment, test plan (exit criteria).

## Nguyên tắc (Project_rule.md §8)

- **Aggregation, không generation.** KHÔNG estimate, KHÔNG project.
- **Trung thực.** NO-GO nếu NO-GO.
- **Quality Gates measurable:** G1-G7 từ Project_rule.md §8.3.

## Status Protocol

§8 = COMPLETED. Output: `08_test-runs/TR-*.md` + `09_reports/REPORT-*.md`

## Examples

### Example 1: Sprint report
**Input:** `/test-report --sprint S05`
**Behavior:** Aggregate sprint 5 runs → `09_reports/REPORT-SPRINT-S05-[date].md/xlsx`. 7 Quality Gates check.

### Example 2: Release GO/NO-GO
**Input:** `/test-report --release --version v2.0`
**Behavior:** Cross-paradigm aggregation (Java + Python vibe) → release report với GO/NO-GO recommendation.

### Example 3: Cross-version comparison
**Input:** `/test-report --cross-version v1.0 v2.0`
**Behavior:** Side-by-side metrics, trend analysis, regression coverage.

### Example 4: Ad-hoc point-in-time
**Input:** `/test-report --adhoc`
**Behavior:** Snapshot current state of all sources, dùng cho mid-sprint review.

### Example 5: Trend analysis
**Input:** `/test-report --trend`
**Behavior:** Multi-sprint pass rate + bug rate over time + chart.

## Common Edge Cases

| Scenario | Handling |
|----------|----------|
| No execution data trong §15 | Block, suggest `/execute-maintain --run-all` |
| 0 bugs logged | Report "✅ No bugs" trong defect summary |
| Active version unclear | Hỏi user explicit `--version` |
| Quality Gates incomplete | Report partial, mark missing gates |
| Mixed languages (Java + Python tests) | Separate paradigm sections |
| Single TC executed (insufficient data) | Block with warning, suggest more runs |
| Stakeholder audience không chỉ định | Default tester, suggest `--audience CEO/CFO/PM` |
| Cross-version với 1 version only | Reject, need ≥ 2 versions |

