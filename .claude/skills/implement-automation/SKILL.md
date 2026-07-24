---
name: implement-automation
description: Implement automation Java Selenium POM từ TC-MASTER Excel (source of truth). Code phải match steps + expected của TC. Uses Playwright/Appium MCP để lấy locator từ web/app thật. Use when user mentions 'implement automation', 'viết code test', 'tạo page object', 'lấy locator', 'implement POM', 'code selenium', 'auto test', or runs /implement-automation command (alias /implement).
license: Proprietary — FPT QA Toolkit v1.0 (qc-claude-v1)
compatibility: Designed for Claude Code QA projects with 00_..11_ folder structure (qc-claude-v1). Requires Claude Code or compatible agent runtime.
metadata:
  toolkit: qc-claude-v1
  pipeline-position: "8"
  status-section: MASTER-MEMORY-section-8
  owner: QC Team
  version: "1.1"
  released: "2026-06-05"
  updated: "2026-07-21 — migrated TC column mapping sang template ISC (42-cột, xem generate-tc/references/consolidate.md)"
---

# Implement Automation

TC-MASTER Excel → Java Selenium code (Page Object + Test class). **TC Excel là contract.**

## Command

| Command | Mode | Mô tả |
|---------|------|-------|
| `/implement-automation --module Login` | IMPLEMENT | Implement TC → code cho module (match theo `C3` Tên chức năng của sheet, hoặc tên tab nếu không khớp) |
| `/implement-automation --tc TC_01.2,TC_01.5` | IMPLEMENT | Implement TCs cụ thể — dùng đúng ID hiển thị trong cột A (formula-derived `[Mã CN].[STT]`, KHÔNG phải ID tự đặt) |
| `/implement-automation --locator @URL` | LOCATOR | Chỉ lấy locator từ web |
| `/implement-automation --update "thêm element X"` | UPDATE | Cập nhật code hiện có |

Options: `--version vX.Y` `--module NAME` `--tc TC-ID,...`

## Prerequisites

| Cần có | Check |
|--------|-------|
| Source MEMORY.md | scan-source-code §8 = COMPLETED |
| TC-MASTER-v[X].xlsx (alias của file ISC chính thức — 42 cột, 1 sheet/module) | generate-tc §8 ≥ PARTIAL |
| Playwright MCP (nếu KHÔNG có vibe-locators) | Connected |
| **vibe-locators.md (khuyến nghị)** | vibe-test §8 ≥ PARTIAL → locators đã verified |

## Pipeline

`scan-source-code` + `generate-tc` + **`vibe-test`** → **★ implement-automation ★** → `review-src-tc`, `execute-maintain`

**Folder sở hữu:** `10_source-code/` (code files)

**Data flow từ vibe-test:**
```
vibe-test output:
  08_test-runs/vibe/vibe-locators-latest.md  → implement-automation ĐỌC locators (file duy nhất)
  08_test-runs/vibe/VR-[NNN]-[date]/vibe-report.md → implement-automation ĐỌC TC pass/blocked status
```

## Mode Routing

| Condition | → Load |
|-----------|--------|
| `--locator` | `references/locator.md` |
| `--update` | `references/update.md` |
| Default implement — Java stack | `references/implement.md` |
| Default implement — TypeScript stack | `references/implement-typescript.md` — **stack-aware**, xem dưới |

## Stack-Aware Mode Routing (added 2026-05-31)

> Khi implement mode active, skill detect stack từ `10_source-code/MEMORY.md` §2 Tech Stack `Language` field. Route đến variant tương ứng (Java/Selenium POM vs TypeScript/Playwright Page class).

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

| Detected stack | Reference loaded | Code generation target |
|---|---|---|
| `typescript` | `references/implement-typescript.md` | Playwright Page class (TS) + `test()` spec file |
| `java` (default + backward-compat fallback) | `references/implement.md` (existing) | Selenium PageFactory POM (Java) + TestNG class |

### Override flag

`/implement-automation --stack typescript` HOẶC `/implement-automation --stack java` cho explicit override.

### Backward-compat

1. Existing Java projects (Selenium POM workflow) — no change
2. Legacy MEMORY §2 free-form text → fallback Java + INFO warning
3. TS projects (Language=TypeScript trong §2): auto-load implement-typescript.md

### Code generation patterns (TS vs Java side-by-side)

| Pattern | Java/Selenium (existing) | TypeScript/Playwright (NEW) |
|---|---|---|
| **Page Object class** | `public class LoginPage extends BasePage { @FindBy(id="email") private WebElement textBoxEmail; }` | `export class LoginPage extends BasePage { private readonly email: Locator; constructor(page: Page) { super(page); this.email = page.getByLabel('Email'); } }` |
| **Action method** | `public void enterEmail(String email) { textBoxEmail.clear(); textBoxEmail.sendKeys(email); }` | `async enterEmail(value: string): Promise<void> { await this.email.fill(value); }` |
| **Test method** | `@Test(description = "TC_01.1 / REQ-01: ...") public void testLoginSuccess() { ... }` | `test('TC_01.1: ... / REQ-01', async ({ page }) => { ... });` |
| **Test class structure** | `class LoginTest extends AppBaseTest { ... }` | `test.describe('REQ-01 — ...', () => { let loginPage; test.beforeEach(...); test(...); });` |
| **Assertions** | `assertEquals(actual, expected)` / `assertTrue(condition)` | `await expect(locator).toHaveText(expected)` / `expect(value).toBe(true)` |
| **Comprehensive mode loop** | `@DataProvider(name="passwords") + @Test(dataProvider="passwords")` | `for (const data of passwordBoundary) { test(\`${data.tcId}\`, ...); }` |
| **Build verify** | `mvn compile -q` | `npx tsc --noEmit` |
| **Locator API** | `@FindBy(id="email")` PageFactory | `page.getByLabel('Email')` / `page.locator('#email')` |

### Edge cases (TS-specific in implement-typescript.md)

- TC count > 50 cho 1 SC (comprehensive mode) → use loop pattern (Pattern A `for...of`)
- Multi-page scenarios → instantiate Page Objects upfront, chain async calls
- Strict mode violation (Playwright matches multiple elements) → refine locator với `getByRole + name`
- File upload → `setInputFiles(path)`
- Download → `page.waitForEvent('download')`
- iframe → `page.frameLocator(...)`

Xem đầy đủ trong `references/implement-typescript.md`.

## Nguyên tắc (Project_rule.md §5)

- **TC Excel là contract.** Code match TC steps (cột H) 1:1, expected (cột I) 1:1.
- **`// Step N:` + `// Expected N:`** comment bắt buộc.
- **`@Test(description = "[Testcase ID] / [Req ID]: [Title]")`** — vd `"TC_01.2 / REQ-02: Email sai format"`. Template ISC không còn cột Scenario ID; nếu project có mapping SC↔TC ở Version MEMORY §9, có thể thêm `/ SC-xxx` optional vào cuối description, nhưng KHÔNG bắt buộc.
- **Test data ĐÚNG giá trị inline trong TC Steps (cột H).** Template không có cột Test Data riêng — parse giá trị cụ thể trực tiếp từ text Steps, KHÔNG tự bịa, KHÔNG lấy từ cột nào khác.
- **Tuân thủ conventions từ Source MEMORY.** KHÔNG tự tạo pattern mới.
- **Locator từ web thực (Playwright).** KHÔNG đoán.

## Status Protocol

§8 = PARTIAL (per module) → COMPLETED (tất cả TCs implemented).

## Examples

### Example 1: Implement automation for module
**Input:** `/implement-automation --module Login`
**Behavior:**
1. Đọc Source MEMORY (conventions) + TC-MASTER Excel (Login sheet)
2. Lấy locator từ Playwright MCP (open URL từ CLAUDE.md)
3. Generate `LoginPage.java` + `LoginTest.java`
4. Map TC steps → method calls 1:1
5. Map TC expected → assertions 1:1
6. Update Source MEMORY §6 (Page Registry) + §7 (Test Registry) + §13 (Implementation Log)

### Example 2: Implement specific TCs
**Input:** `/implement-automation --tc TC_01.1,TC_01.5`
**Behavior:** Generate code cho 2 TCs cụ thể (match theo giá trị cột A đã resolve, không phải chuỗi tự đặt).

### Example 3: Locator-only mode
**Input:** `/implement-automation --locator @https://stg.example.com/login`
**Behavior:** Open browser, snapshot, extract locators only → §12 Locator Registry. KHÔNG generate code.

### Example 4: Update existing
**Input:** `/implement-automation --update "thêm element buttonOTP vào LoginPage"`
**Behavior:** Append new field to existing class, KHÔNG rewrite cả file.

## Common Edge Cases

| Scenario | Handling |
|----------|----------|
| Source MEMORY chưa có | Block, suggest `/scan-source-code` trước |
| TC-MASTER chưa có | Block, suggest `/generate-tc` |
| Playwright MCP disconnected | Try Appium fallback, hoặc skip locator (use TBD placeholder) |
| Locator NOT FOUND on web/app | Log warning, generate code với commented locator |
| TC test data có giá trị invalid (e.g., null) | Use placeholder + comment "TODO: real data" |
| Naming conflict existing class | Append `_v2` suffix, log warning |
| Multi-page TC requires navigation | Generate sequential method calls per page transition |
| Manual verify step (visual check) | Comment `// MANUAL VERIFY REQUIRED`, KHÔNG generate assertion |
| TC count > 100 cho 1 module | Suggest split into multiple Test classes by Group (Functional/UI/Integration/Database Test Case) |
| **TC count > 50 cho 1 sheet module (comprehensive mode)** | **(NEW 2026-05-29)** Comprehensive mode có thể expand 3-12× per module. Strategy options:<br>• **A. 1:1 mapping** — mỗi derived TC có method riêng (clear traceability, verbose code).<br>• **B. Parameterized via `@DataProvider`** — 1 method covers N derived TCs (e.g., BVA boundaries 6 TCs → 1 method với 6 data rows). Recommended cho BVA/EP/EG patterns.<br>• **Hybrid** — baseline TC + parameterized for derived. Document trong Source MEMORY §13: cột "Test method" có thể là single hoặc TC ID range (`testFooBoundary` covers `TC_03.14..TC_03.20`). |
| **Remark column (AP) chứa `Technique: <tag>`** | **(cập nhật 2026-07-21, trước đây gọi "Notes column")** Khi parsing TC Excel, đọc Remark column (cột 42/AP) — technique tag là informational, không affect code generation logic, nhưng nên include trong `@Test description` để traceback (e.g., `@Test(description = "TC_03.14 / REQ-05 / Technique: BVA-min-1")`). Remark cũng có thể chứa `Carried từ v[X]` hoặc ghi chú khác nối bằng ` \| ` — chỉ lấy phần `Technique:` khi parse. Per `review-src-tc` M4-04. |
| **Coverage Matrix sheet trong TC-MASTER** | **(NEW 2026-05-29)** Sheet này informational cho implement-automation — KHÔNG parse rows, chỉ trace mode active. Per `~/.claude/skills/generate-tc/assets/coverage-matrix-template.md`. |
| **scenario_map.md có Source Detail blocks (Part 2 verbatim quoting)** | **(NEW 2026-05-29)** Khi đọc scenario_map.md cho supplementary context, prefer Source Quote text khi resolve ambiguity vs analyst paraphrase — Source Quote chính xác hơn. KHÔNG affect code generation directly. |

