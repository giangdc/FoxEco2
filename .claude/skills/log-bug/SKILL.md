---
name: log-bug
description: Tạo và quản lý bug reports từ execute-maintain ASSERTION_FAIL, tracking full defect lifecycle, version-aware bug-index, và đẩy/đồng bộ bug lên Jira qua Atlassian MCP (cấu hình per-project đọc từ Project_rule.md — KHÔNG hardcode site/project trong skill). Use when user mentions 'log bug', 'tạo bug report', 'báo lỗi', 'raise defect', 'cập nhật bug', 'close bug', 'retest bug', 'bug status', 'push jira', 'đẩy bug lên jira', 'pull jira', 'đồng bộ jira', or runs /log-bug command.
license: Proprietary — FPT QA Toolkit v1.0 (qc-claude-v1)
compatibility: Designed for Claude Code QA projects with 00_..11_ folder structure (qc-claude-v1). Requires Claude Code or compatible agent runtime.
metadata:
  toolkit: qc-claude-v1
  pipeline-position: "11"
  status-section: MASTER-MEMORY-section-8
  owner: QC Team
  version: "1.1"
  released: "2026-06-05"
  updated: "2026-07-21 — align với template ISC: severity nhãn High→Major (khớp Bug Data sheet), thêm fields platform/defect/effect/round_found/round_closed/rework_number/wont_fix_reason, sync 2 chiều bug md ↔ Bug Data sheet trong TC-MASTER (xem references/sync-excel.md). Trước đó (2026-05-28): STATUS mode Aging Report."
---

# Log Bug

Bug report từ test failures, full defect lifecycle tracking.

> **⚠️ NEW 2026-05-28 — `--status` mode now includes Aging Report** flagging bugs Open >7 days (per BUG-002 17-day spec-evolution case). See `references/status.md` §Aging Report.

## Command

| Command | Mode | Mô tả |
|---------|------|-------|
| `/log-bug` | LOG | Tạo bug từ ASSERTION_FAIL chưa log |
| `/log-bug --update BUG-001 --status "Fixed"` | UPDATE | Cập nhật status |
| `/log-bug --close BUG-001` | CLOSE | Close bug (phải Verified) |
| `/log-bug --status` | STATUS | Xem tổng quan bugs |
| `/log-bug --push-jira [BUG-001\|--all]` | PUSH-JIRA | Đẩy bug md → Jira (DQ): tạo issue + attach + ghi key về |
| `/log-bug --pull-jira [BUG-001\|--all]` | PULL-JIRA | Kéo status Jira → cập nhật md + bug-index (đồng bộ 2 chiều) |

## Prerequisites

| Cần có | Check |
|--------|-------|
| Source MEMORY §16 có ASSERTION_FAIL | execute-maintain ≥ COMPLETED |
| (chỉ `--push-jira`/`--pull-jira`) Atlassian MCP đã auth | `/mcp` → Atlassian OAuth; bug md có YAML front-matter |
| TC-MASTER-v[X].xlsx có sheet `Bug Data` (để đồng bộ) | generate-tc ≥ PARTIAL, alias file ISC — nếu thiếu sheet, log-bug vẫn chạy bình thường (md là nguồn chính) nhưng skip sync Excel, xem `references/sync-excel.md` |

## Pipeline

`execute-maintain` → **★ log-bug ★** → `test-report`

**Folder sở hữu:** `05_bug-reports/`

## Mode Routing

| Condition | → Load |
|-----------|--------|
| `--update` | `references/update.md` |
| `--close` | `references/close.md` |
| `--status` | `references/status.md` |
| `--push-jira` / `--pull-jira` | `references/push-jira.md` |
| Default | `references/log.md` |

> `references/sync-excel.md` không phải mode riêng — được `log.md`/`update.md`/`close.md`/`push-jira.md` gọi chung mỗi khi bug md thay đổi, để mirror vào sheet `Bug Data` của TC-MASTER.

## Nguyên tắc (Project_rule.md §7)

- **Bug từ evidence** (ASSERTION_FAIL), không suy đoán.
- **Traceability:** Bug → FAIL → RUN → Method → TC ID → Req ID. Chuỗi không đứt. (Template ISC không còn Scenario ID column trong TC-MASTER — SC vẫn truy được qua Version MEMORY nếu cần, nhưng không phải liên kết bắt buộc trong Excel.)
- **LOCATOR_STALE ≠ app bug** (trừ khi UI changed).
- **Lifecycle:** Open → In Progress → Fixed → Verified → Closed. KHÔNG skip.
- **KHÔNG tự verify.** Retest = `/execute-maintain --run`.
- **Jira sync:** bug md là source-of-truth lifecycle; `--push-jira` tạo/cập nhật issue Jira (theo `project_key` trong config) + ghi `jira_key` về (idempotent), `--pull-jira` kéo status Jira về. Mapping ở `references/push-jira.md` + `05_bug-reports/jira-<KEY>-fields.md` (KEY = project_key của workspace).
- **Bug Data sheet (TC-MASTER) là bản mirror, không phải nguồn chính.** Mọi thay đổi status/severity/... luôn sửa bug md trước, rồi đồng bộ ngược vào Bug Data sheet — không bao giờ ngược lại. Xem `references/sync-excel.md`.

## Status Protocol

§8 = COMPLETED. Output: `05_bug-reports/BUG-NNN-*.md` + `bug-index.md` updated.

## Examples

### Example 1: Auto-log từ §16 ASSERTION_FAIL
**Input:** `/log-bug`
**Behavior:**
1. Scan Source MEMORY §16 → tìm ASSERTION_FAIL chưa có Bug ID
2. Generate BUG-NNN report từ template
3. Update bug-index.md
4. Update §16 Fail Registry với Bug ID link

### Example 2: Update bug status
**Input:** `/log-bug --update BUG-001 --status "Fixed"`
**Behavior:** Update BUG-001 file + bug-index status column.

### Example 3: Close bug after retest
**Input:** `/log-bug --close BUG-001`
**Behavior:** Verify §16 FAIL-001 status = Rechecked PASS → close BUG-001.

### Example 4: View status overview
**Input:** `/log-bug --status`
**Behavior:** Inline summary: P1 open / P2 fixed / total trend.

## Common Edge Cases

| Scenario | Handling |
|----------|----------|
| Không có ASSERTION_FAIL trong §16 | "Không có bug để log", exit |
| BUG ID đã tồn tại | Skip duplicate, suggest `--update` |
| Missing TC ID link trong FAIL | Hỏi user manual map TC ID |
| Bug fix rate thấp (>14 days open) | Flag warning trong status |
| **Aging report findings** (2026-05-28+) | `--status` mode auto-flags bugs Open >7d (INFO 8-14d / WARNING 15-30d / CRITICAL >30d). User prompted re-validate via `/execute-maintain --recheck` workflow. See references/status.md §Aging Report. |
| Bug Open quá lâu (>30d) chưa close | 🔴 CRITICAL aging flag — recommend block GO decision until triage. Possible spec evolution rendered test obsolete (BUG-002 precedent). |
| Multi-version bug (carry từ v1.0 → v2.0) | Add "By Version" rows trong bug-index |
| Bug close không có retest evidence | Block close, require RUN ID reference |
| Screenshot evidence thiếu | Suggest user attach via adb screencap |
| Priority unclear (P1 vs P2) | Default P2, document criteria trong template-bug-report |
| TC-MASTER thiếu sheet `Bug Data` (file build từ template cũ) | Log bug md bình thường (md là nguồn chính), skip sync Excel + warning, suggest `/generate-tc --consolidate` |
| `round_found` không xác định được (execute-maintain/vibe-test chưa round-aware) | Để trống cột Sprint/Round trong Bug Data sheet, KHÔNG tự đoán round |
| Severity nhập `High` (nhãn cũ, trước 2026-07-21) | Auto-map `High`→`Major` khi sync Excel (backward-compat), nhưng khuyến nghị sửa lại md dùng nhãn mới |

