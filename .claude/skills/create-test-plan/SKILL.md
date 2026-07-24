---
name: create-test-plan
description: Tạo Test Plan tổng thể với scope, approach, criteria, resources, schedule, risks cho release/sprint/feature. Use when user mentions 'tạo test plan', 'create test plan', 'viết kế hoạch test', 'test strategy', 'test approach', 'lập kế hoạch kiểm thử', or runs /create-test-plan command (alias /test-plan).
license: Proprietary — FPT QA Toolkit v1.0 (qc-claude-v1)
compatibility: Designed for Claude Code QA projects with 00_..11_ folder structure (qc-claude-v1). Requires Claude Code or compatible agent runtime.
metadata:
  toolkit: qc-claude-v1
  pipeline-position: "2"
  status-section: MASTER-MEMORY-section-8
  owner: QC Team
  version: "1.0"
  released: "2026-06-05"
---

# Create Test Plan

Tạo Test Plan — kim chỉ nam cho toàn bộ quá trình testing.

## Command

| Command | Mode | Mô tả |
|---------|------|-------|
| `/create-test-plan --create` | CREATE | Tạo mới |
| `/create-test-plan --create --version v2.0` | CREATE | Tạo cho version cụ thể |
| `/create-test-plan --retro` | RETRO | Tạo cho project đã chạy (auto-extract) |
| `/create-test-plan --update "thay đổi"` | UPDATE | Cập nhật test plan hiện có |
| `/create-test-plan --review` | REVIEW | Xem test plan |

Options: `--version vX.Y`

## Prerequisites

| Cần có | Check |
|--------|-------|
| CLAUDE.md | root project |

## Pipeline

`init-project` → **★ create-test-plan ★** → `analyze-requirements`

**Folder sở hữu:** `01_test-plans/`
**Downstream đọc:** analyze-requirements (§2 Scope), implement-automation (§3 Approach), test-report (§4 Exit Criteria)

## Mode Routing

| Condition | → Load |
|-----------|--------|
| `--create` hoặc chưa có test plan | `references/create.md` |
| `--retro` hoặc "project đang chạy" | `references/retro.md` |
| `--update` hoặc nhắc sửa/cập nhật | `references/update.md` |
| `--review` hoặc nhắc xem | `references/review.md` |

## Nguyên tắc

- **Quick scan, không deep analysis.** Phân tích chi tiết là việc analyze-requirements.
- **User-driven.** Approach, priority, schedule — hỏi user, không tự quyết.
- **Exit criteria → Quality Gates.** Truyền sang test-report cho GO/NO-GO.

## Status Protocol

§8 = IN_PROGRESS → COMPLETED. Nếu UPDATE → cảnh báo downstream.

## Examples

### Example 1: Create new test plan for version
**Input:** `/create-test-plan --create --version v1.0`
**Behavior:**
1. Đọc `CLAUDE.md` + `00_input/v1.0/` (quick scan)
2. Hỏi từng câu: type, objectives, scope, approach, schedule, risks
3. Generate `01_test-plans/TP-master-{project}-v1.0.md`
**Output:** Test plan with 10 sections + version context (§2.0) + deliverable paths.

### Example 2: Update existing plan
**Input:** `/create-test-plan --update "thêm module Payment vào scope"`
**Behavior:** Đọc current plan → add Payment row to §2 Scope → bump version → log §11 Revision History
**Output:** Plan version v1.0 → v1.1 with Payment in scope.

### Example 3: Retro mode (project đã chạy)
**Input:** `/create-test-plan --retro`
**Behavior:** Auto-extract từ existing MEMORY/CLAUDE.md → only ask thiếu fields (~50% fewer questions).

## Common Edge Cases

| Scenario | Handling |
|----------|----------|
| `00_input/` rỗng | Vẫn create plan với scope = TBD, log warning |
| Multi-version active (v1.0 + v2.0) | Hỏi version specific, default = active version từ MASTER-MEMORY |
| Team mode chưa biết members | Default Solo, có thể update sau qua `--update` |
| Conflict scope với existing analyze-requirements | Cảnh báo + suggest sync via `/analyze-requirements --review` |
| No test environment URL | Skip §5, ghi "TBD" placeholder |
| Quality Gates không clear | Default 7 gates (G1-G7), user override sau |
| Risk list quá dài (>15 risks) | Suggest split high-risk → separate sprint |

