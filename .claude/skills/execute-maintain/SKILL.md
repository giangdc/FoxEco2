---
name: execute-maintain
description: Chạy automation test (mvn test), parse pass/fail results, classify failures (LOCATOR_STALE/ASSERTION_FAIL/ENV_ERROR/UNKNOWN), dùng Playwright MCP để recheck locator KHÔNG auto-fix, ghi §15-§16 trong source MEMORY. Version-aware execution log. Use when user mentions 'chạy test', 'run test', 'execute automation', 'test fail', 'recheck locator', 'maintain test', 'debug fail', or runs /execute-maintain command (alias /execute).
license: Proprietary — FPT QA Toolkit v1.0 (qc-claude-v1)
compatibility: Designed for Claude Code QA projects with 00_..11_ folder structure (qc-claude-v1). Requires Claude Code or compatible agent runtime.
metadata:
  toolkit: qc-claude-v1
  pipeline-position: "10"
  status-section: MASTER-MEMORY-section-8
  owner: QC Team
  version: "1.0"
  released: "2026-06-05"
  updated: "2026-05-28 — Mandatory Step 0 DOC re-validate trong recheck mode"
---

# Execute & Maintain

Chạy test suite, thu thập pass/fail, classify failures, Playwright recheck.

> **⚠️ NEW 2026-05-28 — RECHECK mode now MANDATES Step 0 DOC re-validate** (per BUG-002 spec-evolution case). KHÔNG được copy-paste old bug repro mà bỏ qua check DOC hiện tại first. See `references/recheck.md` §Step 0.

## Command

| Command | Mode | Mô tả |
|---------|------|-------|
| `/execute-maintain --run LoginTest` | RUN | Chạy 1 test class |
| `/execute-maintain --run-all` | RUN | Chạy toàn bộ |
| `/execute-maintain --diagnose FAIL-001` | DIAGNOSE | Phân tích failure |
| `/execute-maintain --recheck FAIL-001` | RECHECK | Recheck locator bằng Playwright |
| `/execute-maintain --status` | STATUS | Xem execution history |

Options: `--version vX.Y`

## Prerequisites

| Cần có | Check |
|--------|-------|
| Source MEMORY §4-§7 | scan-source-code ≥ COMPLETED |
| Test classes compiled | implement-automation ≥ PARTIAL |

## Pipeline

`implement-automation` → **★ execute-maintain ★** → `log-bug` → `test-report`

**Ghi vào:** Source MEMORY §15 (Execution Log) + §16 (Fail Registry)

## Mode Routing

| Condition | → Load |
|-----------|--------|
| `--status` | `references/status.md` |
| `--diagnose` | `references/diagnose.md` |
| `--recheck` | `references/recheck.md` |
| Default run — Java stack | `references/run.md` |
| Default run — TypeScript stack | `references/run-typescript.md` — **stack-aware**, xem dưới |

## Stack-Aware Mode Routing (added 2026-05-31)

> Khi run mode active, skill detect stack từ `10_source-code/MEMORY.md` §2 Tech Stack `Language` field. Route đến variant tương ứng (mvn test vs npx playwright test).

### Detection logic

```python
def detect_stack(memory_path):
    """Parse §2 Tech Stack Language field."""
    if not memory_path.exists():
        return "java"  # No MEMORY → Java default (backward-compat)
    in_section_2 = False
    for line in memory_path.read_text().splitlines():
        if line.startswith("## 2. Tech Stack"):
            in_section_2 = True
            continue
        if in_section_2 and line.startswith("##") and not line.startswith("## 2"):
            break
        if in_section_2 and "| Language" in line:
            parts = [p.strip() for p in line.split("|")]
            if len(parts) >= 3 and parts[2] in ("TypeScript", "JavaScript"):
                return "typescript"
    return "java"
```

### Route table

| Detected stack | Run command | Reference loaded |
|---|---|---|
| `typescript` | `npx playwright test` | `references/run-typescript.md` |
| `java` (default + backward-compat fallback) | `mvn test` | `references/run.md` (existing) |

### Override flag

`/execute-maintain --stack typescript` HOẶC `/execute-maintain --stack java` cho explicit override.

### Diagnose + Recheck modes (stack-agnostic)

`diagnose.md` + `recheck.md` references KHÔNG có TS variant — logic generic:
- **Diagnose:** Đọc §16 Fail Registry, classify, suggest fix — language-neutral
- **Recheck:** Use Playwright MCP để observe (works cho cả web Java và TS)

### Backward-compat

1. Existing Java projects (mvn test workflow) — no change
2. Legacy MEMORY §2 free-form text → fallback Java + INFO warning
3. TS projects (Language=TypeScript trong §2): auto-load run-typescript.md

### Key behavioral differences

| Aspect | Java variant | TypeScript variant |
|---|---|---|
| Run command | `mvn test -Dtest=LoginTest` | `npx playwright test login.spec.ts` |
| Filter by test name | `-Dtest=LoginTest#testLoginSuccess` | `-g "TC-LOGIN-001"` |
| Output format | Maven Surefire XML (`target/surefire-reports/*.xml`) | Playwright JSON (`test-results/results.json`) |
| Failure artifacts | Stack trace text | Trace .zip + screenshot.png + video.webm |
| Parallel | TestNG config (manual) | Built-in workers (parallel default) |
| Locator stale msg | `NoSuchElementException` / `StaleElementReferenceException` | `locator.click: Target page closed` / `TimeoutError: locator.waitFor` |
| Assertion fail msg | `AssertionError: Expected X but was Y` | `Error: expect(received).toBe(expected)` |
| Build verify | `mvn compile` | `npx tsc --noEmit` |

## Nguyên tắc (Project_rule.md §7)

- **Chạy test thật** (`mvn test`), parse output thật.
- **Classify:** LOCATOR_STALE / ASSERTION_FAIL / ENV_ERROR / UNKNOWN.
- **Playwright CHỈ observe:** navigate + snapshot + screenshot. KHÔNG interact. KHÔNG sửa code.
- **KHÔNG auto-fix.** Report → user/implement-automation sửa.

## 🔐 Credential Safety (MANDATORY 2026-05-29)

Một số test suite cần SSO env vars (`SSO_USERNAME` / `SSO_PASSWORD`). Để tránh leak password vào Bash tool transcript / report-claude tracking:

- **NEVER** inline password vào Bash command. Cấm tuyệt đối pattern `SSO_PASSWORD="<actual>" mvn test ...` — assistant đọc credentials file rồi nhét literal vào command args sẽ làm password xuất hiện trong tool invocation log.
- **NEVER** đọc nội dung file credentials (`credentials.local.md`, `~/.dashboard-report/credentials.env`, `.env`) và copy giá trị password ra context.
- **MUST** assume env vars đã được user export trước khi gọi `mvn test`. Check qua:
  ```bash
  test -n "$SSO_USERNAME" && test -n "$SSO_PASSWORD" && echo "ENV_OK" || echo "ENV_MISSING"
  ```
  KHÔNG echo `$SSO_PASSWORD` value.
- Nếu `ENV_MISSING`, **ask user** chạy trong cùng session:
  ```
  ! source ~/.dashboard-report/credentials.env
  ```
  Prefix `!` ensures env vars persist cho các Bash call tiếp theo trong session. KHÔNG tự source rồi inline trong cùng một Bash invocation chứa `mvn test` — vì nếu user chưa có file, error message có thể leak path/content.
- **MUST** dùng pattern `source ~/.dashboard-report/credentials.env && mvn test ...` ONLY khi assistant đã verify file tồn tại VÀ session sẽ flush ngay (one-shot). Preferred: rely on user-sourced env, command chỉ chứa `mvn test ...`.
- Nếu user paste password vào chat → **politely refuse to record**, ask them put it in `~/.dashboard-report/credentials.env` instead. Don't echo back.

## Status Protocol

§8 = PARTIAL (1 class) → COMPLETED (full suite). Notes: "RUN-xxx: NP/NF/NS, N% pass".

## Examples

### Example 1: Run single test class
**Input:** `/execute-maintain --run LoginTest`
**Behavior:**
1. Đọc Source MEMORY §4 (BaseTest config)
2. Run `mvn test -Dtest=LoginTest`
3. Parse output → §15 Execution Log
4. Classify failures → §16 Fail Registry

**Output:** `RUN-NNN: 5P/1F/1S, 71% pass rate`

### Example 2: Run full suite
**Input:** `/execute-maintain --run-all -PSmoke`
**Behavior:** `mvn test -PSmoke -Dsurefire.suiteXmlFiles=testSuites/smoke.xml` → parse all classes.

### Example 3: Diagnose specific failure
**Input:** `/execute-maintain --diagnose FAIL-001`
**Behavior:** Đọc §16, classify (LOCATOR_STALE/ASSERTION_FAIL/ENV_ERROR/UNKNOWN), suggest fix without auto-applying.

### Example 4: Recheck locator via Playwright MCP
**Input:** `/execute-maintain --recheck FAIL-001`
**Behavior:** Open browser, navigate to URL, verify if locator still matches. Report findings (KHÔNG auto-fix code).

## Common Edge Cases

| Scenario | Handling |
|----------|----------|
| Maven not installed | Báo user install Maven, exit |
| No test classes in `10_source-code/` | Suggest `/scan-source-code` + `/implement-automation` trước |
| Appium server offline (mobile tests) | Try start server, fallback ADB, hoặc skip mobile tests |
| Selenium ContextAware error | Check Appium client version compatibility |
| All tests SKIP (no @Test methods) | Check `<test>` block trong suite XML |
| Out of memory (large suite) | Suggest split suite, run partial |
| Network timeout for Grid URL | Fallback to local Chrome |
| Flaky test (1 run pass, next fail) | Mark as FLAKE in §16 with multi-run evidence |
| **RECHECK without DOC re-read** | ❌ BANNED 2026-05-28+. MUST execute Step 0 in `references/recheck.md` before any actual test run. |
| Bug repro entities not in current DOC whitelist | Step 0 outcome → Close FP (Spec Evolution), skip recheck, document closure citing DOC §section |
| User asks "rerun BUG-NNN quickly" | Politely require Step 0 DOC verify first — saves wasted recheck cycles (BUG-002 precedent 2026-05-28) |

