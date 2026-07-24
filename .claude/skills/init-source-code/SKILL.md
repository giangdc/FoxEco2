---
name: init-source-code
description: Scaffold `10_source-code/` với chosen archetype — auto-generate automation project structure thay vì manual clone từ GitLab. Supports 3 archetypes: Playwright TypeScript (web), Selenium Java (web), Appium Java (mobile). Sinh đầy đủ build config, base Page Object, test fixtures, MEMORY.md với structured §2 Tech Stack. Multi-stack ready cho future archetypes (Python Pytest, Cypress, etc.). Use when user mentions 'init source code', 'tạo source code', 'scaffold automation project', 'init playwright', 'init typescript', 'create automation scaffold', 'generate source code archetype', or runs /init-source-code command.
license: Proprietary — FPT QA Toolkit v1.0 (qc-claude-v1)
compatibility: Designed for Claude Code QA projects with 00_..11_ folder structure (qc-claude-v1). Requires Claude Code or compatible agent runtime với file write capability + Python 3 cho scaffold scripts.
metadata:
  toolkit: qc-claude-v1
  pipeline-position: "0.5"
  status-section: MASTER-MEMORY-section-8
  owner: QC Team
  version: "1.0"
  released: "2026-06-05"
---

# Init Source Code — Multi-Stack Archetype Scaffolder

Scaffold `10_source-code/` folder với automation project template tương ứng stack lựa chọn. Replace manual clone từ GitLab archetype với auto-generation. Mỗi archetype tạo đầy đủ build config + Page Object base + test fixtures + MEMORY.md.

---

## Command

| Command | Mode | Mô tả |
|---------|------|-------|
| `/init-source-code` | INTERACTIVE | Hỏi user chọn archetype + run scaffold |
| `/init-source-code --archetype playwright-ts` | SCAFFOLD | Direct scaffold Playwright TypeScript (web) |
| `/init-source-code --archetype selenium-java` | SCAFFOLD | Direct scaffold Selenium Java (web) |
| `/init-source-code --archetype appium-java` | SCAFFOLD | Direct scaffold Appium Java (mobile) |
| `/init-source-code --list` | LIST | Show available archetypes + descriptions |
| `/init-source-code --status` | STATUS | Show current `10_source-code/` archetype detected từ MEMORY §2 |

**Options:**
- `--force` — overwrite existing `10_source-code/` (default: refuse nếu folder không empty)
- `--from-gitlab <url>` — clone archetype từ GitLab repo thay vì inline template (deferred — Phase 1 dùng inline)
- `--dry-run` — preview file list không write
- `--project-name <name>` — override project name (default: read from CLAUDE.md)

---

## Prerequisites

| Cần có | Check |
|--------|-------|
| `CLAUDE.md` tại project root | `init-project` ≥ COMPLETED |
| Project folder structure (00_..11_) | `init-project` đã scaffold |
| Python 3.9+ trên máy | `python3 --version` (cho scaffold scripts) |
| Build tool tương ứng archetype | Java 21 + Maven (cho `*-java`) · Node.js 18+ (cho `playwright-ts`) |

**Note:** init-source-code KHÔNG yêu cầu skills upstream khác (analyze-requirements, create-test-plan) chạy trước. Standalone — chạy bất kỳ lúc nào để setup automation project.

---

## Pipeline Position

```
init-project → ★ init-source-code ★ (optional, standalone)
                       ↓
            10_source-code/ scaffolded
                       ↓
            scan-source-code → implement-automation → execute-maintain → review-src-tc
            (downstream skills detect stack via MEMORY §2)
```

**Skill số 0.5** — between init-project và create-test-plan conceptually, nhưng standalone (KHÔNG gate downstream). User có thể chạy init-source-code TRƯỚC analyze-requirements hoặc SAU khi đã có test plan + scenarios — không matter.

**Folder sở hữu (GHI):** `10_source-code/` (scaffold time only — sau đó scan-source-code + implement-automation own).

---

## Mode Routing

| Condition | → Load |
|-----------|--------|
| `--list` | `references/archetypes.md` (registry) |
| `--archetype playwright-ts` | `references/archetype-playwright-ts.md` + `scripts/scaffold-playwright-ts.py` |
| `--archetype selenium-java` | `references/archetype-selenium-java.md` (document existing manual pattern) |
| `--archetype appium-java` | `references/archetype-appium-java.md` (document existing manual pattern) |
| `--status` | Read `10_source-code/MEMORY.md` §2 Tech Stack, report detected stack |
| Default (no flag) HOẶC `--archetype <unknown>` | Interactive prompt — list archetypes, ask user choose |

---

## Nguyên tắc cốt lõi

1. **Backward-compat default.** Existing Java projects (manual scaffold pre-2026-05-31) KHÔNG bị disrupted — init-source-code chỉ tạo mới, không modify existing.
2. **Opt-in skill.** Không auto-trigger. User explicit run khi muốn scaffold.
3. **Stack-aware metadata.** MEMORY §2 Tech Stack structured table → downstream skills auto-route.
4. **Self-contained templates** (Phase 1). Inline trong skill references — không dependency GitLab. `--from-gitlab` flag deferred future iteration.
5. **Idempotent guards.** Refuse overwrite existing files trừ khi `--force`. Verify build OK sau scaffold (TypeScript compile / Maven compile).

---

## Workflow

### Step 1: Guard + context check

```
1. PIPELINE.md → check init-project ≥ COMPLETED (required prerequisite)
2. CLAUDE.md → đọc project info (name, app type, environment)
3. 02_analyze-requirements/Project_rule.md → check existing automation context (nếu có)
4. ls 10_source-code/ → nếu non-empty + KHÔNG có --force → REFUSE với explanation
5. Ghi MASTER-MEMORY §8 init-source-code = IN_PROGRESS
```

### Step 2: Choose archetype

**Interactive mode (default):**
```
Available archetypes:
  (a) playwright-ts  — Playwright + TypeScript (web)        [Modern, fast, parallel]
  (b) selenium-java  — Selenium + Java + TestNG (web)       [Enterprise, stable]
  (c) appium-java    — Appium + Java + TestNG (mobile)      [Native iOS/Android]

Chọn archetype: _
```

**Direct mode:** `--archetype <value>` skips prompt.

### Step 3: Pre-scaffold validation

- Check build tool installed (`mvn --version` cho Java · `npm --version` + `node --version` cho TS)
- Check disk space (>50 MB cho TS với `node_modules`)
- Check network nếu archetype cần download deps (skip nếu --dry-run)

### Step 4: Run scaffold

Load archetype-specific reference + script. Per `--archetype` value:

| Archetype | Reference loaded | Script run |
|---|---|---|
| `playwright-ts` | `references/archetype-playwright-ts.md` | `scripts/scaffold-playwright-ts.py` |
| `selenium-java` | `references/archetype-selenium-java.md` | (manual instructions — document existing pattern) |
| `appium-java` | `references/archetype-appium-java.md` | (manual instructions) |

Script generates files vào `10_source-code/`. Per archetype, see archetype reference cho file list.

### Step 5: Populate Source MEMORY.md §2 Tech Stack (structured)

Script writes structured table:

```markdown
## 2. Tech Stack

| Component    | Value           | Version |
|--------------|-----------------|---------|
| Language     | TypeScript      | 5.x     |
| Framework    | Playwright      | 1.x     |
| Test Runner  | Playwright Test | 1.x     |
| Build Tool   | npm             | 10.x    |
| Package Mgr  | npm             | —       |
| Locator API  | page.locator()  | —       |
| Async pattern| async/await     | —       |
```

> **CRITICAL:** Structured format này là source-of-truth cho downstream skills (scan-source-code, implement-automation, execute-maintain, review-src-tc) routing logic. KHÔNG chỉnh sửa header tên cột hoặc field "Language" — skills parse exact pattern.

### Step 6: Update Project_rule.md §10 Automation Context

Append/replace section:

```markdown
## 10. Automation Context (scaffolded by init-source-code on YYYY-MM-DD)

- **Stack:** <Archetype name>
- **Build tool:** <e.g., npm | Maven>
- **Test framework:** <e.g., Playwright Test | TestNG>
- **Language:** <TypeScript | Java>
- **Source code path:** `10_source-code/`
- **Locator strategy:** <per archetype>
- **Run command:** <e.g., `npx playwright test` | `mvn test`>
```

### Step 7: Present output summary

```
✅ Source code scaffold complete: archetype = <playwright-ts>

Files created (10):
  📁 10_source-code/
  📄 package.json (deps: @playwright/test 1.x, typescript 5.x)
  📄 tsconfig.json (strict mode, target ES2022)
  📄 playwright.config.ts (default workers, retries, reporters)
  📄 MEMORY.md (§1-§19 with TS structured §2)
  📄 README.md (project-specific)
  📁 src/pages/ (BasePage.ts)
  📁 src/tests/ (fixtures.ts, setup.ts)
  📁 src/utils/ (api-helpers.ts, data-helpers.ts)
  📁 playwright-suites/ (smoke.config.ts, regression.config.ts)
  📄 .gitignore

Verified:
  ✅ npm install — deps resolved
  ✅ npx tsc --noEmit — TypeScript compile clean

Next steps:
  1. /scan-source-code → populate MEMORY §3-§19 với scaffold conventions
  2. /create-test-plan → draft Test Plan nếu chưa có
  3. /analyze-requirements --init @00_input/v1.0/ → start QA pipeline
```

### Step 8: Update §8 Pipeline Status

```
| 0.5 | init-source-code | COMPLETED | <date> | archetype=<value> | 10_source-code/ scaffold (10 files) | <archetype> stack ready cho downstream skills |
```

---

## Status Protocol

- **Bắt đầu:** Ghi MASTER-MEMORY §8 init-source-code = IN_PROGRESS
- **Hoàn thành:** Ghi = COMPLETED + ghi archetype value + Output
- **Lỗi/abort:** Ghi = FAILED + Notes mô tả (e.g., "build verify failed: npm install error")
- **--dry-run:** KHÔNG update §8 status

---

## Examples

### Example 1: Interactive scaffold cho project mới

**Input:** `/init-source-code`

**Behavior:**
1. List 3 archetypes available
2. User chọn "a" (playwright-ts)
3. Run `scripts/scaffold-playwright-ts.py`
4. Output 10 files + MEMORY.md với §2 structured
5. Run `npm install` + `npx tsc --noEmit` để verify
6. Update Project_rule.md §10

**Output:** Same as Step 7 summary above.

### Example 2: Direct Playwright TS scaffold

**Input:** `/init-source-code --archetype playwright-ts`

**Behavior:** Skip interactive prompt, jump to Step 4.

### Example 3: Status check

**Input:** `/init-source-code --status`

**Behavior:**
1. Read `10_source-code/MEMORY.md` §2 Tech Stack
2. Parse Language + Framework values
3. Output:
   ```
   📊 Current source-code stack:
      Language: TypeScript 5.x
      Framework: Playwright 1.x
      Test Runner: Playwright Test
      Build Tool: npm 10.x

   ✅ Downstream skills sẽ auto-route to TypeScript variants.
   ```

### Example 4: List available archetypes

**Input:** `/init-source-code --list`

**Behavior:** Read `references/archetypes.md`, display registry table.

### Example 5: Force overwrite existing scaffold

**Input:** `/init-source-code --archetype playwright-ts --force`

**Behavior:**
1. Warn user: "10_source-code/ has existing files — they will be overwritten"
2. Ask confirm (unless `--dry-run`)
3. Backup existing to `10_source-code.bak.<timestamp>/`
4. Proceed scaffold

---

## Common Edge Cases

| Scenario | Handling |
|----------|----------|
| `10_source-code/` đã có files (non-empty) | Refuse without --force; suggest --force để backup + overwrite |
| Python 3 không có | Block, suggest install (cần cho scaffold scripts) |
| `npm`/`mvn` không có (theo archetype) | Block, suggest install build tool tương ứng |
| Disk space < 100 MB | Warn (TS với node_modules có thể ~200 MB) |
| User chọn archetype không tồn tại | List available archetypes, ask re-choose |
| `--from-gitlab <url>` flag | Phase 1: log INFO "deferred to future release, using inline template instead" |
| MEMORY.md đã tồn tại trong 10_source-code/ | Backup as MEMORY.md.bak.<timestamp> trước khi overwrite (preserve any manual entries) |
| Scaffold completed nhưng `npm install` fail | Mark §8 = PARTIAL với note; user fix deps manually và re-run verify |
| TypeScript compile fail (tsc errors) | Mark §8 = PARTIAL; output errors; suggest manual fix template |
| Project_rule.md §10 đã có content khác | Append `## 10.1 Automation Context (auto-scaffolded)` sub-section thay vì overwrite |
| Multiple archetypes cùng `10_source-code/` (cố tình mix) | NOT supported — 1 project = 1 archetype. User scaffold separate projects nếu cần multi-stack. |
| User muốn convert Java → TS sau scaffold | Use `--force` để scaffold mới; **không support in-place migration**. Manual port code required. |
| Symlink hoặc shared `10_source-code/` | Detect via stat; warn user về implications (changes ảnh hưởng tất cả projects sharing). |

---

## See Also

### Pipeline references
- [PIPELINE.md](../../PIPELINE.md) — Skill registry + prerequisites matrix
- [COMMANDS.md](../../COMMANDS.md) — Cheat sheet

### Upstream skill
- [`init-project`](../init-project/SKILL.md) — creates folder structure 00_..11_; init-source-code chỉ populate 10_source-code/

### Downstream skills (read MEMORY §2 to auto-route)
- [`scan-source-code`](../scan-source-code/SKILL.md) — populate §3-§19 với scaffold conventions
- [`implement-automation`](../implement-automation/SKILL.md) — generate code (TS variant cho playwright-ts archetype)
- [`execute-maintain`](../execute-maintain/SKILL.md) — run tests (npm/playwright cho TS, mvn cho Java)
- [`review-src-tc`](../review-src-tc/SKILL.md) — TC↔code review (file pattern theo archetype)

### Internal references
- [`references/archetypes.md`](references/archetypes.md) — Registry list available archetypes
- [`references/archetype-playwright-ts.md`](references/archetype-playwright-ts.md) — Playwright TS full guide
- [`references/archetype-selenium-java.md`](references/archetype-selenium-java.md) — Selenium Java legacy pattern
- [`references/archetype-appium-java.md`](references/archetype-appium-java.md) — Appium Java mobile pattern
- [`scripts/scaffold-playwright-ts.py`](scripts/scaffold-playwright-ts.py) — Playwright TS scaffold logic
