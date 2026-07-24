# Scan Source Code — Mode FULL — TypeScript variant

> **Loaded khi:** MEMORY §2 Tech Stack có `Language = TypeScript` (vd Playwright TS archetype scaffolded bởi `init-source-code`).
> **Default (Java) variant:** [`full.md`](full.md) — loaded khi Language = Java hoặc trống.
> **Stack detection:** Xem `~/.claude/skills/init-source-code/references/memory-section-2-format.md`.

## Output: `10_source-code/MEMORY.md` (§1-§19, TS conventions)

## Workflow

### Step 1: Đọc CLAUDE.md + verify stack

Project info, automation framework info. Confirm §2 Tech Stack có `Language = TypeScript`. Ghi MASTER-MEMORY §8 scan-source-code = IN_PROGRESS.

### Step 2: Scan project structure

```bash
# TypeScript source files
find 10_source-code/ -type f \( -name "*.ts" -o -name "*.tsx" \) -not -path "*/node_modules/*" | head -100

# Config + manifest files
find 10_source-code/ -maxdepth 2 -type f \( -name "*.json" -o -name "*.yml" -o -name "*.yaml" \) -not -path "*/node_modules/*"

# Detect package manager
ls 10_source-code/package-lock.json 2>/dev/null && echo "npm"
ls 10_source-code/yarn.lock 2>/dev/null && echo "yarn"
ls 10_source-code/pnpm-lock.yaml 2>/dev/null && echo "pnpm"

# Detect Playwright presence
grep -l '"@playwright/test"' 10_source-code/package.json 2>/dev/null && echo "Playwright detected"

# Count TypeScript files
find 10_source-code/ -name "*.ts" -not -path "*/node_modules/*" | wc -l
```

→ Ghi vào MEMORY §1 Project Structure (tree + file statistics, exclude `node_modules/`, `test-results/`, `playwright-report/`).

### Step 3: Analyze dependencies & config

**3a. `package.json` — extract dependencies:**

```bash
cat 10_source-code/package.json | python3 -m json.tool
```

Identify từ `dependencies` + `devDependencies`:

| Dependency | Cần extract | Ghi vào MEMORY |
|---|---|---|
| `@playwright/test` | Version (1.x) | Framework version + Playwright Test runner |
| `typescript` | Version (5.x) | Language version |
| `@types/node` | Version | Type definitions |
| `eslint` + `@typescript-eslint/*` | Có/không | Linting setup |
| `prettier` | Có/không | Code formatter |
| `jest` / `vitest` | Có/không | Alternative test runners (rare với Playwright) |
| `dotenv` | Có/không | Env file loading |
| `@faker-js/faker` | Có/không | Test data generation |

→ MEMORY §2 Tech Stack (verify match scaffolded values) + §3 Configuration.

**3b. `tsconfig.json` — extract TS compiler options:**

```bash
cat 10_source-code/tsconfig.json
```

Key fields:
- `target` (e.g., ES2022) — Module syntax level
- `strict` — Strictness mode (true expected)
- `paths` — Path aliases (vd `@pages/*`, `@utils/*`)
- `module` — CommonJS hoặc ESNext
- `include`/`exclude`

→ MEMORY §3a TypeScript Config.

**3c. `playwright.config.ts` — extract Playwright settings:**

```bash
cat 10_source-code/playwright.config.ts
```

Extract:
- `baseURL` env var name (vd `process.env.BASE_URL`)
- `projects` — browser matrix (Chromium, Firefox, WebKit)
- `workers` — parallel concurrency
- `retries` — retry policy
- `reporter` — HTML, JSON, list, allure-playwright, etc.
- `use.actionTimeout`, `use.navigationTimeout` — timeouts
- `globalSetup` — setup file path

→ MEMORY §3b Playwright Config.

**3d. Suite configs (`playwright-suites/*.config.ts`):**

```bash
ls 10_source-code/playwright-suites/*.config.ts 2>/dev/null
```

Each suite config: `testMatch` pattern + worker count + reporter override.

→ MEMORY §10 Suite Definitions.

### Step 4: Analyze Base Classes ★ QUAN TRỌNG NHẤT

**4a. BasePage (`src/pages/BasePage.ts`):**

```bash
cat 10_source-code/src/pages/BasePage.ts
```

Extract — ĐỌC RẤT KỸ:

| Cần extract | Tại sao | Ví dụ TypeScript |
|---|---|---|
| Class structure | `abstract class` vs `class` | `export abstract class BasePage { }` |
| Constructor pattern | Page injection | `constructor(protected readonly page: Page) {}` |
| Common methods | Reusable utilities | `goto(path)`, `waitForVisible(locator)`, `screenshot(name)` |
| Async pattern | Promise return | `async goto(): Promise<void>` |
| Imports | Playwright API surface | `import { Page, Locator, expect } from '@playwright/test'` |

→ MEMORY §4 Base Classes.

**4b. Fixtures (`src/tests/fixtures.ts`):**

```bash
cat 10_source-code/src/tests/fixtures.ts
```

Extract:
- Custom fixtures defined (vd `authenticatedPage`, `apiHelper`)
- Extended `test` export pattern: `export const test = base.extend<CustomFixtures>({ ... })`
- `expect` re-export

→ MEMORY §4 Base Classes (sub-section Fixtures).

**4c. Global setup (`src/tests/setup.ts`):**

```bash
cat 10_source-code/src/tests/setup.ts
```

Extract:
- Required env vars check (vd `TEST_USERNAME`, `TEST_PASSWORD`, `BASE_URL`)
- Auth state capture pattern (nếu có)
- Test data pre-warming logic

→ MEMORY §4 Base Classes (sub-section Global Setup).

### Step 5: Analyze Page Classes

```bash
find 10_source-code/src/pages/ -name "*.ts" -not -name "BasePage.ts" -not -name "index.ts" | sort
```

Mỗi Page class extract:

- **Class metadata:** name, file path, extends BasePage (verify), imports
- **Locator properties:** TypeScript readonly fields với type `Locator`
  ```typescript
  private readonly emailInput: Locator;
  private readonly submitButton: Locator;
  ```
- **Constructor:** locator initialization patterns
  ```typescript
  constructor(page: Page) {
    super(page);
    this.emailInput = page.locator('#email');
    this.submitButton = page.getByRole('button', { name: 'Submit' });
  }
  ```
- **Action methods:** name, return type (`Promise<void>` / `Promise<string>` / etc.), params, async signature
  ```typescript
  async enterEmail(value: string): Promise<void> { ... }
  async getErrorMessage(): Promise<string> { ... }
  ```
- **Locator strategy detection:** parse `page.locator(...)` / `page.getByRole(...)` / `page.getByLabel(...)` / `page.getByTestId(...)` calls → classify per Playwright priority

**Naming convention analysis — frequency count (TypeScript):**

```
Locator naming patterns:
  emailInput, submitButton, errorMessage     → 15 occurrences ✅
  email_input, submit_button                  → 0 occurrences (snake_case rare in TS)
  EmailInput, SubmitButton                    → 0 occurrences (PascalCase rare for instances)

Method naming patterns:
  enter[Target](), click[Target](), get[Target]() → 30 occurrences ✅ (verb-based)
  set[Target](), do[Target]()                     → 2 occurrences ⚠️ inconsistent
```

→ MEMORY §5 Conventions + §6 Page Registry.

### Step 6: Analyze Test Files

```bash
find 10_source-code/src/tests/ -name "*.spec.ts" -not -name "fixtures.ts" -not -name "setup.ts" | sort
```

Mỗi test file extract:

- **File path + import statements** (Page classes imported)
- **`test.describe()` blocks** — group test by SC ID
  ```typescript
  test.describe('SC-LOGIN-001 — User authentication', () => { ... });
  ```
- **`test(name, async ({ page, ... }) => {...})` calls** — individual TCs
  ```typescript
  test('TC-LOGIN-001: Happy path / SC-LOGIN-001', async ({ page }) => { ... });
  ```
- **`test.beforeEach()` / `test.afterEach()` hooks**
- **DataProvider equivalent loops:**
  ```typescript
  for (const data of passwordBoundary) {
    test(`${data.tcId}: ${data.technique}`, async ({ page }) => { ... });
  }
  ```
- **Assertions used** (`expect()`, `expect.toHaveURL()`, `expect.toBeVisible()`, etc.)

Coverage mapping: parse test name pattern `'TC-XXX-NNN: ... / SC-XXX-NNN'` → extract SC ID + TC ID → MEMORY §7 Test Registry.

### Step 7: Generate MEMORY.md

Tổng hợp §1-§11 vào `10_source-code/MEMORY.md` (giữ §2 Tech Stack structured nguyên — đã populated bởi init-source-code).

§12-§19 để placeholder (populated by implement-automation, execute-maintain).

Append CLAUDE.md:

```markdown
## Source Code Analysis

- **Framework:** TypeScript X.X + Playwright X.X
- **Page classes:** [N] | Test files: [N] | Test() calls: [N]
- **Coverage:** [N]/[Total] scenarios ([%])
- **Conventions:** [type][Name] camelCase / async verb[Target]() / test name TC-ID-SC-ID pattern
```

Ghi MASTER-MEMORY §8 scan-source-code = COMPLETED.

## Edge Cases

### Source code rỗng nhưng package.json có

```
⚠️ Folder 10_source-code/ có package.json nhưng src/ rỗng.
Có thể là scaffold mới chưa code.
(a) Tạo Page Object skeleton từ archetype template?
(b) Để implement-automation tạo từ scratch?
```

### `node_modules/` chưa install

```
⚠️ node_modules/ không tồn tại. Run `npm install` trước khi scan deps.
Skip §3 Dependencies analysis, populate sau khi install.
```

### Mixed JavaScript + TypeScript

Phát hiện cả `.ts` và `.js` files (không phải build output):
```
⚠️ Phát hiện mixed .ts + .js source. Project có thể đang migrate.
Scan .ts files; report .js files trong §11 Notes.
```

### Playwright version mismatch với MEMORY §2

```
⚠️ MEMORY §2 ghi Playwright 1.42.0 nhưng package.json hiện tại 1.50.0.
Update §2 Tech Stack Version field.
```

### Custom fixtures phức tạp (>5 fixtures)

Document từng fixture trong §4 sub-section, including dependency chain (fixture A uses fixture B).

### Path aliases trong tsconfig.json

Nếu có `@pages/*` aliases, resolve khi scan imports để verify Page class references đúng.

### TestMatch pattern không match files

Suite config `testMatch: /.*\.smoke\.spec\.ts/` nhưng không có file match → warn trong §10 Suite Definitions.

### >100 TypeScript files

Hỏi user: "Source code có [N] .ts files. Scan toàn bộ hay focus subset?"
Ưu tiên: BasePage → fixtures.ts → setup.ts → Page classes → utils → test files.

## Quy tắc

- **KHÔNG đoán convention** — chỉ ghi pattern thực sự từ code
- **KHÔNG sửa code** — issues → ghi §11 Notes, không fix
- **KHÔNG ghi password/secret** plaintext → `[REDACTED]`
- **KHÔNG scan vào `node_modules/`** — exclude path
- **KHÔNG modify package.json** — read-only
- Luôn có timestamp `Cập nhật lần cuối` ở header
- **Verify §2 Tech Stack consistency** với package.json deps — nếu mismatch, warn user

## TypeScript-specific scanning patterns

### Pattern A: Constructor-based locator init (most common)

```typescript
export class LoginPage extends BasePage {
  private readonly email: Locator;
  private readonly password: Locator;

  constructor(page: Page) {
    super(page);
    this.email = page.locator('#email');
    this.password = page.locator('#password');
  }
}
```

→ Extract locators FROM constructor body (`page.locator('selector')` calls assigned to `this.X`).

### Pattern B: Getter-based lazy locators (alternative)

```typescript
export class LoginPage extends BasePage {
  get email() { return this.page.locator('#email'); }
  get password() { return this.page.locator('#password'); }
}
```

→ Extract from getter return statements.

### Pattern C: Inline locators (anti-pattern but possible)

```typescript
async enterEmail(value: string) {
  await this.page.locator('#email').fill(value);
}
```

→ Less ideal — locators not centralized. Flag trong §11 Notes as "anti-pattern", suggest refactor to Pattern A.

### Test description parsing — extract TC + SC IDs

Regex pattern cho test names:
```
^TC-([A-Z\-]+)-(\d+):.+/\s*SC-\1-\2\s*(?:/\s*Technique:\s*(.+))?$
```

Examples that match:
- `TC-LOGIN-001: Happy path / SC-LOGIN-001`
- `TC-AUTH-014: Password length 7 / SC-AUTH-002 / Technique: BVA-min-1`

Extract: TC ID, SC ID, optional Technique tag → MEMORY §7 Test Registry + §13 Implementation Log (if implement-automation đã chạy).

## Checklist

- [ ] §2 Tech Stack verified (Language = TypeScript)
- [ ] Tất cả .ts files (exclude node_modules/) đã đọc
- [ ] package.json + tsconfig.json + playwright.config.ts extracted
- [ ] Suite configs (playwright-suites/*.config.ts) listed
- [ ] BasePage analysis đầy đủ (constructor, methods, imports)
- [ ] Fixtures + setup.ts analyzed
- [ ] Page classes indexed (locators + methods)
- [ ] Test files indexed (test.describe blocks + test() calls + coverage)
- [ ] Naming conventions extracted + frequency count
- [ ] Locator strategy frequency (locator vs getByRole vs getByLabel vs getByTestId)
- [ ] Coverage gap analysis (nếu có Version MEMORY)
- [ ] MEMORY.md updated (preserve §2 structured table)
- [ ] CLAUDE.md append
- [ ] Không có password plaintext
- [ ] MASTER-MEMORY §8 = COMPLETED

## See Also

- [`full.md`](full.md) — Java default variant (loaded when Language ≠ TypeScript)
- [`~/.claude/skills/init-source-code/references/archetype-playwright-ts.md`](../../init-source-code/references/archetype-playwright-ts.md) — Playwright TS archetype specs (conventions reference)
- [`~/.claude/skills/init-source-code/references/memory-section-2-format.md`](../../init-source-code/references/memory-section-2-format.md) — Stack detection logic
