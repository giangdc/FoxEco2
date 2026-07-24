---
name: review-tc
description: "Review chất lượng TC-MASTER bằng independent reviewer agent (tránh self-review bias). 4 chiều: structural, coverage, content, consistency. Output review report + quality score 0-100. Use when user mentions 'review TC', 'review test case', 'kiểm tra TC', 'đánh giá test case', 'check quality TC', 'validate test cases', or runs /review-tc command."
license: Proprietary — FPT QA Toolkit v1.0 (qc-claude-v1)
compatibility: Designed for Claude Code QA projects with 00_..11_ folder structure (qc-claude-v1). Requires Claude Code or compatible agent runtime.
metadata:
  toolkit: qc-claude-v1
  pipeline-position: "5"
  status-section: MASTER-MEMORY-section-8
  owner: QC Team
  version: "1.1"
  released: "2026-06-05"
  updated: "2026-07-21 — migrated checks to template ISC (42-column TC-MASTER, xem generate-tc/references/consolidate.md)"
---

# Review Test Cases

Đọc TC-MASTER Excel + analyze output → gọi **independent reviewer agent** (Anthropic API) → tạo review report.

## Command

| Command | Mode | Mô tả |
|---------|------|-------|
| `/review-tc` | FULL | Review toàn bộ TC-MASTER |
| `/review-tc --module Login` | MODULE | Review 1 module |
| `/review-tc --recheck` | RECHECK | Review lại sau khi sửa |
| `/review-tc --direct` | FULL (no agent) | Review trực tiếp, skip agent |

Options: `--version vX.Y` `--module NAME` `--direct`

## Prerequisites

| Cần có | Check |
|--------|-------|
| TC-MASTER-v[X].xlsx (alias của file ISC chính thức `ISC_[Project]_[Version]_TC_[TCVersion]_R[Round].xlsx`) | generate-tc §8 ≥ PARTIAL |

## Pipeline

`generate-tc` → **★ review-tc ★** → (user action: sửa TC)

**Folder sở hữu:** `11_tc-review/`

## Mode Routing

| Condition | → Load |
|-----------|--------|
| `--recheck` | `references/recheck.md` |
| `--module` | `references/module.md` |
| Default | `references/full.md` |

## Agent Protocol

> Xem `review-agent/AGENT.md` cho system prompt + API pattern.

**Khi nào dùng agent:**
- generate-tc §8 ≥ PARTIAL (TC được tạo trong pipeline → dùng agent)
- User gõ `/review-tc` không có `--direct` flag

**Khi nào KHÔNG dùng agent:**
- User gõ `/review-tc --direct` (explicit skip)
- API call fail → fallback direct + disclaimer

**Flow:**
```
Main Claude                          Reviewer Agent (API)
  │                                        │
  ├─ Parse TC-MASTER (openpyxl)            │
  ├─ Parse analyze output (scenarios)      │
  ├─ Serialize → JSON ──────────────→ Receive data
  │                                  ├─ Apply R1-R4 checks
  │                                  └─ Return findings JSON
  ├─ Receive JSON ←─────────────────┘
  ├─ Format review report
  └─ Present to user
```

## Nguyên tắc

- **Agent = independent reviewer.** Không biết TC do AI hay human tạo.
- **4 chiều:** R1 Structural, R2 Coverage, R3 Content, R4 Consistency.
- **Score = 100 - (Critical×5 + Major×3 + Minor×1).** Pass threshold: ≥ 70.
- **KHÔNG sửa TC.** Chỉ report.

## Status Protocol

§8 = COMPLETED. Output: `11_tc-review/review-report-v[X].md`

## Examples

### Example 1: Full TC review
**Input:** `/review-tc`
**Behavior:**
1. Đọc TC-MASTER (mọi sheet TC: Test Cases, Test Case 2, ...) + scenario_map + data_catalog
2. Call independent reviewer agent (R1-R4 checks, 60 checks total)
3. Output `11_tc-review/review-report-v[X].md` + Excel

**Output:** Quality score 0-100, findings categorized Critical/Major/Minor/Info.

### Example 2: Module review
**Input:** `/review-tc --module Login`
**Behavior:** Review 1 module sheet only.

### Example 3: Recheck after TC fix
**Input:** `/review-tc --recheck`
**Behavior:** Re-run on previous findings, update score.

## Common Edge Cases

| Scenario | Handling |
|----------|----------|
| TC-MASTER chưa có | Block, suggest `/generate-tc --consolidate` |
| Score < 70 | Mark REJECTED, list Critical+Major findings, block downstream |
| 70 ≤ Score < 90 | CONDITIONAL, recommend fix Major first |
| Score ≥ 90 | APPROVED |
| TC count > 200 | Pagination warning, suggest split modules |
| Duplicate Testcase ID | Critical R1-02, block until resolved |
| Testcase ID (cột A) bị gõ tay thay vì formula | Critical R1-01, block — phá auto-numbering |
| Steps hoặc Expected trống (empty TC) | R1-08/R1-09 Major |
| Step reference data nhưng không ghi giá trị cụ thể inline | R3-03 Major |
| Req ID không có row trong RTM (orphan) | R2-16 Critical |
| Independent reviewer API fail | Fallback direct review, disclaimer + score cap 85 |

