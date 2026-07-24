# MEMORY §2 Tech Stack — Structured Format Specification

> **Status:** MANDATORY format (2026-05-31)
> **Owner:** `init-source-code` skill populates initial table; downstream skills (`scan-source-code`, `implement-automation`, `execute-maintain`, `review-src-tc`) PARSE table cho stack-aware routing.

## Why structured?

Pre-2026-05-31, Source MEMORY §2 Tech Stack là free-form text (vd "Java 21 + Selenium 4 + TestNG 7"). Downstream skills hardcoded Java assumption → KHÔNG support multi-stack.

Post-2026-05-31, §2 dùng **structured table** với fixed column headers. Skills parse rows reliable, route đúng variant references.

## Schema

```markdown
## 2. Tech Stack

| Component    | Value           | Version |
|--------------|-----------------|---------|
| Language     | <required>      | <ver>   |
| Framework    | <required>      | <ver>   |
| Test Runner  | <required>      | <ver>   |
| Build Tool   | <required>      | <ver>   |
| Package Mgr  | <optional>      | <ver>   |
| Locator API  | <optional>      | —       |
| Async pattern| <optional>      | —       |
| Core library | <optional>      | <ver>   |
| ...          | <extensible>    | ...     |
```

### Required fields (4 rows minimum)

| Field | Allowed values | Used by |
|---|---|---|
| **Language** | `TypeScript` · `Java` · `Python` (future) · `JavaScript` (future) | ALL downstream skills cho routing |
| **Framework** | `Playwright` · `Selenium` · `Appium` · `Cypress` (future) · `Pytest` (future) | scan-source-code (dep detection) · implement-automation (template selection) |
| **Test Runner** | `Playwright Test` · `TestNG` · `JUnit 5` · `Jest` · `Vitest` · `Pytest` | execute-maintain (command format) · review-src-tc (test annotation pattern) |
| **Build Tool** | `npm` · `Maven` · `Gradle` · `pip` · `yarn` · `pnpm` | execute-maintain (build verify command) · scan-source-code (config file parse) |

### Optional fields

Add additional rows tùy stack:

| Stack | Recommended extras |
|---|---|
| Playwright TS | `Package Mgr` · `Locator API` (page.locator) · `Async pattern` (async/await) |
| Selenium Java | `Locator API` (@FindBy PageFactory) · `Async pattern` (Synchronous) · `Core library` (team library) · `Browser driver` (WebDriverManager) |
| Appium Java | `Locator API` (@AndroidFindBy + @iOSXCUITFindBy) · `Mobile target` (UiAutomator2 / XCUITest) · `App platform` |

## Downstream skill parsing logic

Mỗi downstream skill (4 skills) implement parsing như sau:

```python
# Pseudo-code
def detect_stack(memory_md_path):
    """Parse §2 Tech Stack table, return language enum."""
    content = read_file(memory_md_path)
    in_section_2 = False
    for line in content.splitlines():
        if line.startswith("## 2. Tech Stack"):
            in_section_2 = True
            continue
        if in_section_2 and line.startswith("##"):
            break  # Reached next section
        if in_section_2 and "| Language" in line:
            # Parse table row: "| Language | TypeScript | 5.x |"
            parts = [p.strip() for p in line.split("|")]
            if len(parts) >= 3:
                value = parts[2]
                if value in ("TypeScript", "JavaScript"):
                    return "typescript"
                if value == "Java":
                    return "java"
                # ... extensible
    return "java"  # Backward-compat default
```

## Routing decision per skill

```
detect_stack(MEMORY.md §2) → language enum
   ↓
   ├── language == "typescript"
   │     scan-source-code        → references/full-typescript.md
   │     implement-automation    → references/implement-typescript.md
   │     execute-maintain        → references/run-typescript.md
   │     review-src-tc           → references/full-typescript.md
   │
   └── language == "java" (default fallback)
         scan-source-code        → references/full.md (existing)
         implement-automation    → references/implement.md (existing)
         execute-maintain        → references/run.md (existing)
         review-src-tc           → references/full.md (existing)
```

## Backward-compat (legacy MEMORY)

Pre-2026-05-31 MEMORY files có §2 free-form text. Downstream skills handle:

1. **Detect:** Try parse structured table first
2. **Fallback:** Nếu KHÔNG có structured table → assume Java (existing behavior)
3. **Log:** Emit INFO warning: "Source MEMORY §2 missing structured Tech Stack table — falling back to Java mode. Run /init-source-code --status để verify, hoặc update MEMORY §2 với structured format."

Existing Java projects KHÔNG bị disrupted. Chỉ cần update §2 khi muốn switch stack hoặc verify routing.

## Examples

### Example 1: Playwright TypeScript

```markdown
## 2. Tech Stack

| Component    | Value           | Version |
|--------------|-----------------|---------|
| Language     | TypeScript      | 5.3.0   |
| Framework    | Playwright      | 1.42.0  |
| Test Runner  | Playwright Test | 1.42.0  |
| Build Tool   | npm             | 10.2.4  |
| Package Mgr  | npm             | —       |
| Locator API  | page.locator()  | —       |
| Async pattern| async/await     | —       |
```

→ Downstream skills load TypeScript variants.

### Example 2: Selenium Java (typical existing project)

```markdown
## 2. Tech Stack

| Component    | Value                  | Version |
|--------------|------------------------|---------|
| Language     | Java                   | 21      |
| Framework    | Selenium               | 4.20.0  |
| Test Runner  | TestNG                 | 7.10.2  |
| Build Tool   | Maven                  | 3.9.6   |
| Locator API  | @FindBy PageFactory    | —       |
| Async pattern| Synchronous WebDriver  | —       |
| Core library | core-mobile-automation | 1.0.0-SNAPSHOT |
```

→ Downstream skills load existing Java references.

### Example 3: Appium Java mobile

```markdown
## 2. Tech Stack

| Component    | Value                            | Version |
|--------------|----------------------------------|---------|
| Language     | Java                             | 21      |
| Framework    | Appium                           | 3.4.2   |
| Test Runner  | TestNG                           | 7.10.2  |
| Build Tool   | Maven                            | 3.9     |
| Locator API  | @AndroidFindBy + @iOSXCUITFindBy | —       |
| Mobile target| Android UiAutomator2 + iOS XCUITest | —    |
| App platform | native iOS/Android               | —       |
```

→ Downstream skills load existing Java references (same as Selenium — language determines routing, not framework).

### Example 4: Future Python Pytest (not implemented yet)

```markdown
## 2. Tech Stack

| Component    | Value      | Version |
|--------------|------------|---------|
| Language     | Python     | 3.11    |
| Framework    | Selenium   | 4.x     |
| Test Runner  | Pytest     | 8.x     |
| Build Tool   | pip        | 24.x    |
```

→ Downstream skills would load Python variants (deferred).

## Validation rules

`health-check` skill có thể validate §2 structured format:

| Check | Severity | Logic |
|---|---|---|
| §2 Tech Stack table present | INFO (warning) | Nếu missing → suggest run `/init-source-code --status` để check + update |
| Required fields present (Language, Framework, Test Runner, Build Tool) | INFO | Missing any required → warn |
| Language value recognized (TypeScript/Java/etc.) | INFO | Unknown value → log warning + fallback Java |
| Stack consistency với file extensions | INFO | Vd Language=TypeScript nhưng `10_source-code/` toàn `.java` files → contradiction warning |

## Update triggers

§2 cần được update khi:
- Major framework upgrade (Playwright 1.x → 2.x): update Framework + Version
- Build tool change: update Build Tool row
- Language change (rare — usually means new project scaffold): re-run `/init-source-code --force`
- Core library version bump: update `Core library` row

`init-source-code --status` skill command đọc §2, display detected stack — user verify periodically.
