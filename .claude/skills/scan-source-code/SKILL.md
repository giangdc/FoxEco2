---
name: scan-source-code
description: Scan source code automation, extract project structure, conventions, Page Object classes, test classes, config, dependencies → 10_source-code/MEMORY.md. Bắt buộc chạy trước implement-automation lần đầu. Use when user mentions 'scan source code', 'đọc source', 'analyze source', 'cập nhật MEMORY source code', 'index source code', or runs /scan-source-code command (alias /scan-source).
license: Proprietary — FPT QA Toolkit v1.0 (qc-claude-v1)
compatibility: Designed for Claude Code QA projects with 00_..11_ folder structure (qc-claude-v1). Requires Claude Code or compatible agent runtime.
metadata:
  toolkit: qc-claude-v1
  pipeline-position: "6"
  status-section: MASTER-MEMORY-section-8
  owner: QC Team
  version: "1.0"
  released: "2026-06-05"
---

# Scan Source Code

Đọc toàn bộ source code trong `10_source-code/`, tạo/cập nhật `10_source-code/MEMORY.md`.

## Command

| Command | Mode | Mô tả |
|---------|------|-------|
| `/scan-source-code` | FULL | Scan toàn bộ lần đầu (hoặc scan lại) |
| `/scan-source-code --delta` | DELTA | Cập nhật thay đổi |
| `/scan-source-code --check` | CHECK | Xem tổng quan (không scan lại) |
| `/scan-source-code --validate` | VALIDATE | So sánh MEMORY với code thực |

## Prerequisites

| Cần có | Check |
|--------|-------|
| `10_source-code/` có .java files | Source code tồn tại |

## Pipeline

**★ scan-source-code ★** → `implement-automation`, `execute-maintain`

**Folder sở hữu:** `10_source-code/` (MEMORY.md only — READ-ONLY đối với code)

## Mode Routing

| Condition | → Load |
|-----------|--------|
| `--check` hoặc nhắc xem/liệt kê | `references/check.md` |
| `--validate` hoặc nhắc so sánh/verify | `references/validate.md` |
| `--delta` hoặc có MEMORY + nhắc cập nhật | `references/delta.md` |
| Default hoặc chưa có MEMORY | `references/full.md` (Java default) HOẶC `references/full-typescript.md` (TS) — **stack-aware routing**, xem dưới |

## Stack-Aware Mode Routing (added 2026-05-31)

> Khi `10_source-code/MEMORY.md` đã tồn tại + có §2 Tech Stack structured table, skill detect Language và route đến variant tương ứng. Backward-compat: legacy MEMORY không có §2 structured → fallback Java.

### Step 1a: Detect stack từ MEMORY §2 (chạy SAU Step 1 đọc context)

```python
# Pseudo-code parse §2 Tech Stack table
def detect_stack(memory_path):
    if not memory_path.exists():
        return "java"  # No MEMORY yet → assume Java default (existing behavior)
    in_section_2 = False
    for line in memory_path.read_text().splitlines():
        if line.startswith("## 2. Tech Stack"):
            in_section_2 = True
            continue
        if in_section_2 and line.startswith("##") and not line.startswith("## 2"):
            break
        if in_section_2 and "| Language" in line:
            parts = [p.strip() for p in line.split("|")]
            if len(parts) >= 3:
                value = parts[2]
                if value in ("TypeScript", "JavaScript"):
                    return "typescript"
                if value == "Java":
                    return "java"
                # Future: "Python", etc.
    return "java"  # Fallback
```

### Step 1b: Route to variant reference

| Detected stack | Load reference |
|---|---|
| `typescript` | [`references/full-typescript.md`](references/full-typescript.md) — Playwright TS patterns (file `.ts`, `package.json`, `page.locator()`, `test()` calls) |
| `java` (default + backward-compat fallback) | [`references/full.md`](references/full.md) — Java/Selenium/TestNG patterns (file `.java`, `pom.xml`, `@FindBy`, `@Test`) |
| Other (Python, etc.) | Fallback Java + log INFO warning: "Unsupported Language value, falling back to Java mode" |

### Override flag (manual)

User có thể force variant qua flag:
- `/scan-source-code --stack typescript` → force TS variant
- `/scan-source-code --stack java` → force Java variant
- (Default: auto-detect from §2)

Useful khi mixed-stack project hoặc migrating.

### Backward-compat behavior

1. **No MEMORY.md yet** (first scan): skill cần CLAUDE.md hoặc command flag để biết stack. Default = Java (existing behavior, preserve cho legacy projects). Suggest user run `/init-source-code` trước nếu muốn TS scaffold.
2. **Legacy MEMORY §2 free-form text** (pre-2026-05-31): detection fails parse → fallback Java + log INFO warning "Source MEMORY §2 missing structured Tech Stack table — falling back to Java. Update §2 với structured format để enable TS routing."
3. **§2 structured table có Language=Java**: explicit Java, load `full.md` (no change vs existing).
4. **§2 structured table có Language=TypeScript**: load `full-typescript.md`.

### Verify routing decision

Sau khi detect + load, log first line:
```
🔍 scan-source-code: detected stack = typescript → loading references/full-typescript.md
```
or
```
🔍 scan-source-code: detected stack = java (default fallback) → loading references/full.md
```

## Nguyên tắc

- **Chỉ đọc, không sửa code.** Output duy nhất = MEMORY.md.
- **Extract chính xác, không suy diễn.** Ghi đúng pattern từ code.
- **MEMORY.md = single source of truth** cho source code context (§1-§11).

## Status Protocol

§8 = COMPLETED (FULL/DELTA) | N/A (CHECK/VALIDATE).

## Examples

### Example 1: Full scan (first time)
**Input:** `/scan-source-code`
**Behavior:**
1. Scan `10_source-code/` recursively
2. Extract (§ numbers = Java stack; TS stack đánh số khác — resolve theo TÊN section): project structure (§1), tech stack (§2), config (§3), Base classes (§4), conventions (§5), Page Registry (§6), Test Registry (§7), Coverage Gap (§9), Locator Registry (§12)
3. Write `10_source-code/MEMORY.md` (§1-§11 sections)

### Example 2: Delta update
**Input:** `/scan-source-code --delta`
**Behavior:** Detect new/modified files since last scan, update relevant sections only (incremental).

### Example 3: Validate MEMORY vs disk
**Input:** `/scan-source-code --validate`
**Behavior:** Cross-check MEMORY §6/§7 entries vs actual files on disk, report inconsistencies.

### Example 4: Check status (no scan)
**Input:** `/scan-source-code --check`
**Behavior:** Display MEMORY summary without scanning files.

## Common Edge Cases

| Scenario | Handling |
|----------|----------|
| No `pom.xml` / `build.gradle` | Detect raw Java project, partial scan |
| Mixed Maven + Gradle | Prefer pom.xml, warn user |
| Empty `10_source-code/` | Generate skeleton MEMORY with TODO placeholders |
| Naming conventions inconsistent (Page vs page) | Report dominant pattern, flag outliers |
| Test classes without @Test | Skip, log warning |
| BaseTest with multiple inheritance | Document chain in §4 |
| Custom annotations / frameworks | Best-effort extraction, manual review needed |
| Config file in non-standard location | Search common paths, ask user if missing |

