# Archetype: Playwright TypeScript (web)

> **Archetype ID:** `playwright-ts`
> **Status:** ✅ Auto-scaffold ready — `scripts/scaffold-playwright-ts.py`
> **Use case:** Modern web automation với TypeScript + Playwright + parallel-first execution
> **Pipeline downstream:** Loads TypeScript variant references (`*-typescript.md`)

## Stack specs

| Component | Value | Version |
|---|---|---|
| Language | TypeScript | 5.x (strict mode) |
| Framework | Playwright | 1.x (latest stable) |
| Test Runner | Playwright Test (built-in) | 1.x |
| Build Tool | npm | 10.x |
| Package Mgr | npm (or yarn/pnpm — npm default) | — |
| Locator API | `page.locator()` + chainable filters | — |
| Async pattern | async/await natively | — |
| Browser support | Chromium + Firefox + WebKit | (auto-installed) |
| Report | HTML reporter (built-in) + JSON | — |
| Parallel execution | Workers (built-in, parallel-by-default) | — |

## Folder structure (target sau scaffold)

```
10_source-code/
├── package.json                            (deps + scripts + project metadata)
├── tsconfig.json                           (TypeScript strict mode, target ES2022)
├── playwright.config.ts                    (Playwright config: baseURL, retries, reporters, workers)
├── .gitignore                              (node_modules, test-results, playwright-report)
├── .npmrc                                  (registry config — optional)
├── README.md                               (project-specific autofill)
├── MEMORY.md                               (§1-§19 với §2 Tech Stack TS-structured)
├── src/
│   ├── pages/
│   │   ├── BasePage.ts                     (abstract base với common methods)
│   │   └── .gitkeep                        (placeholder cho future page objects)
│   ├── tests/
│   │   ├── fixtures.ts                     (Playwright test fixtures — custom fixtures)
│   │   ├── setup.ts                        (global setup — credentials env, auth state)
│   │   └── .gitkeep
│   └── utils/
│       ├── api-helpers.ts                  (REST helpers cho UI ↔ API cross-validation)
│       └── data-helpers.ts                 (vi-VN format parsers, test data utilities)
└── playwright-suites/                      (equivalent of testSuites/ Java)
    ├── smoke.config.ts                     (smoke tests config filter)
    └── regression.config.ts                (regression suite config)
```

## File specifications

### `package.json`

```json
{
  "name": "<project-slug>-automation",
  "version": "1.0.0",
  "description": "Automation test suite for <project-name> (Playwright + TypeScript)",
  "private": true,
  "scripts": {
    "test": "playwright test",
    "test:smoke": "playwright test --config=playwright-suites/smoke.config.ts",
    "test:regression": "playwright test --config=playwright-suites/regression.config.ts",
    "test:headed": "playwright test --headed",
    "test:debug": "playwright test --debug",
    "test:ui": "playwright test --ui",
    "typecheck": "tsc --noEmit",
    "report": "playwright show-report",
    "codegen": "playwright codegen"
  },
  "devDependencies": {
    "@playwright/test": "^1.42.0",
    "@types/node": "^20.0.0",
    "typescript": "^5.3.0"
  },
  "engines": {
    "node": ">=18.0.0",
    "npm": ">=10.0.0"
  }
}
```

### `tsconfig.json`

```json
{
  "compilerOptions": {
    "target": "ES2022",
    "module": "CommonJS",
    "lib": ["ES2022", "DOM"],
    "strict": true,
    "noImplicitAny": true,
    "strictNullChecks": true,
    "esModuleInterop": true,
    "skipLibCheck": true,
    "forceConsistentCasingInFileNames": true,
    "resolveJsonModule": true,
    "moduleResolution": "node",
    "baseUrl": ".",
    "paths": {
      "@pages/*": ["src/pages/*"],
      "@utils/*": ["src/utils/*"],
      "@tests/*": ["src/tests/*"]
    }
  },
  "include": ["src/**/*", "playwright.config.ts", "playwright-suites/**/*"],
  "exclude": ["node_modules", "test-results", "playwright-report"]
}
```

### `playwright.config.ts`

```typescript
import { defineConfig, devices } from '@playwright/test';

export default defineConfig({
  testDir: './src/tests',
  fullyParallel: true,
  forbidOnly: !!process.env.CI,
  retries: process.env.CI ? 2 : 0,
  workers: process.env.CI ? 4 : undefined,
  reporter: [
    ['html', { outputFolder: 'playwright-report' }],
    ['json', { outputFile: 'test-results/results.json' }],
    ['list'],
  ],
  use: {
    baseURL: process.env.BASE_URL || 'http://localhost:3000',
    trace: 'on-first-retry',
    screenshot: 'only-on-failure',
    video: 'retain-on-failure',
    actionTimeout: 15_000,
    navigationTimeout: 30_000,
  },
  projects: [
    {
      name: 'chromium',
      use: { ...devices['Desktop Chrome'] },
    },
    {
      name: 'firefox',
      use: { ...devices['Desktop Firefox'] },
    },
    {
      name: 'webkit',
      use: { ...devices['Desktop Safari'] },
    },
  ],
});
```

### `src/pages/BasePage.ts`

```typescript
import { Page, Locator, expect } from '@playwright/test';

/**
 * BasePage — abstract base cho mọi Page Object.
 * Provides shared utility methods: waitFor, scroll, screenshot, common assertions.
 */
export abstract class BasePage {
  constructor(protected readonly page: Page) {}

  /**
   * Navigate to relative path (uses baseURL từ playwright.config.ts).
   */
  async goto(path: string = '/'): Promise<void> {
    await this.page.goto(path);
  }

  /**
   * Wait cho element visible với configurable timeout.
   */
  async waitForVisible(locator: Locator, timeout = 10_000): Promise<void> {
    await expect(locator).toBeVisible({ timeout });
  }

  /**
   * Get current URL.
   */
  async getURL(): Promise<string> {
    return this.page.url();
  }

  /**
   * Take screenshot với named filename.
   */
  async screenshot(name: string): Promise<void> {
    await this.page.screenshot({ path: `test-results/${name}.png`, fullPage: true });
  }

  /**
   * Scroll element vào view.
   */
  async scrollIntoView(locator: Locator): Promise<void> {
    await locator.scrollIntoViewIfNeeded();
  }

  /**
   * Wait cho network idle.
   */
  async waitForNetworkIdle(timeout = 5_000): Promise<void> {
    await this.page.waitForLoadState('networkidle', { timeout });
  }
}
```

### `src/tests/fixtures.ts`

```typescript
import { test as base } from '@playwright/test';
import { BasePage } from '../pages/BasePage';

/**
 * Custom fixtures — extend Playwright base test với project-specific fixtures.
 * Vd: authenticated page, API helper, test data factory.
 */
type CustomFixtures = {
  // Add custom fixtures here. Examples:
  // authenticatedPage: Page;
  // apiHelper: ApiHelper;
};

export const test = base.extend<CustomFixtures>({
  // Implement fixtures here. Example:
  // authenticatedPage: async ({ page }, use) => {
  //   await page.goto('/login');
  //   await page.fill('#email', process.env.TEST_USERNAME!);
  //   await page.fill('#password', process.env.TEST_PASSWORD!);
  //   await page.click('button[type=submit]');
  //   await use(page);
  // },
});

export { expect } from '@playwright/test';
```

### `src/tests/setup.ts`

```typescript
/**
 * Global setup — runs once before all tests.
 * Use cho: load credentials env, setup test data, authenticate to capture storage state, etc.
 */
import { FullConfig } from '@playwright/test';

async function globalSetup(config: FullConfig) {
  // Verify required env vars
  const required = ['TEST_USERNAME', 'TEST_PASSWORD', 'BASE_URL'];
  for (const env of required) {
    if (!process.env[env]) {
      console.warn(`⚠️ Missing env var: ${env} — some tests may fail`);
    }
  }

  // Add additional global setup logic here:
  // - Pre-warm DB seed data
  // - Capture authenticated storage state (saves time per test)
  // - Validate API health endpoint
}

export default globalSetup;
```

### `src/utils/api-helpers.ts`

```typescript
import { APIRequestContext, request } from '@playwright/test';

/**
 * API helpers cho UI ↔ API cross-validation (per R-001 hoặc tương đương).
 * Wraps Playwright APIRequestContext với common patterns.
 */
export class ApiHelper {
  constructor(private readonly api: APIRequestContext) {}

  static async create(baseURL?: string): Promise<ApiHelper> {
    const ctx = await request.newContext({
      baseURL: baseURL || process.env.API_BASE_URL,
      extraHTTPHeaders: {
        'Content-Type': 'application/json',
      },
    });
    return new ApiHelper(ctx);
  }

  async get<T>(path: string, headers?: Record<string, string>): Promise<T> {
    const res = await this.api.get(path, { headers });
    if (!res.ok()) throw new Error(`GET ${path} failed: ${res.status()}`);
    return res.json() as Promise<T>;
  }

  async post<T>(path: string, body: unknown, headers?: Record<string, string>): Promise<T> {
    const res = await this.api.post(path, { data: body, headers });
    if (!res.ok()) throw new Error(`POST ${path} failed: ${res.status()}`);
    return res.json() as Promise<T>;
  }

  async dispose(): Promise<void> {
    await this.api.dispose();
  }
}
```

### `src/utils/data-helpers.ts`

```typescript
/**
 * Data helpers — parsers/formatters cho test data (vi-VN, en-US, ISO dates, etc.)
 */

/**
 * Parse vi-VN number format: "1.234,56" → 1234.56
 */
export function parseViVNNumber(str: string): number {
  return parseFloat(str.replace(/\./g, '').replace(',', '.'));
}

/**
 * Format number to vi-VN: 1234.56 → "1.234,56"
 */
export function formatViVNNumber(num: number, decimals = 0): string {
  return num.toLocaleString('vi-VN', {
    minimumFractionDigits: decimals,
    maximumFractionDigits: decimals,
  });
}

/**
 * Parse ISO date string.
 */
export function parseISODate(str: string): Date {
  return new Date(str);
}

/**
 * Tolerance comparison cho float values (e.g. percentage assertions).
 */
export function approxEqual(actual: number, expected: number, tolerance = 0.01): boolean {
  return Math.abs(actual - expected) <= tolerance;
}
```

### `playwright-suites/smoke.config.ts`

```typescript
import { defineConfig } from '@playwright/test';
import baseConfig from '../playwright.config';

export default defineConfig({
  ...baseConfig,
  testMatch: /.*\.smoke\.spec\.ts/,
  workers: 4,
  retries: 0,
  reporter: [
    ['html', { outputFolder: 'playwright-report-smoke' }],
    ['json', { outputFile: 'test-results/smoke-results.json' }],
  ],
});
```

### `playwright-suites/regression.config.ts`

```typescript
import { defineConfig } from '@playwright/test';
import baseConfig from '../playwright.config';

export default defineConfig({
  ...baseConfig,
  testMatch: /.*\.(spec|regression)\.ts/,
  workers: 8,
  retries: 1,
  reporter: [
    ['html', { outputFolder: 'playwright-report-regression' }],
    ['json', { outputFile: 'test-results/regression-results.json' }],
  ],
});
```

### `.gitignore`

```gitignore
node_modules/
test-results/
playwright-report/
playwright-report-smoke/
playwright-report-regression/
playwright/.cache/
*.log
.env.local
.DS_Store
.idea/
.vscode/settings.json
```

### `MEMORY.md` template (§1-§19, TS-flavored §2)

Scaffold script populates `10_source-code/MEMORY.md` với standard §1-§19 structure. **§2 Tech Stack** dùng structured table (CRITICAL cho downstream skill routing):

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

Other sections (§1 Project Structure, §3-§19) generic — populated bởi `scan-source-code` sau scaffold.

## Conventions (TypeScript Page Object)

```typescript
import { Page, Locator } from '@playwright/test';
import { BasePage } from './BasePage';

export class LoginPage extends BasePage {
  // Locators declared as readonly properties (initialized in constructor)
  private readonly email: Locator;
  private readonly password: Locator;
  private readonly submitButton: Locator;
  private readonly errorMessage: Locator;

  constructor(page: Page) {
    super(page);
    this.email = page.locator('#email');
    this.password = page.locator('#password');
    this.submitButton = page.locator('button[type="submit"]');
    this.errorMessage = page.locator('.error-message');
  }

  // Action methods — async/await, return Promise<void> trừ khi cần return value
  async enterEmail(value: string): Promise<void> {
    await this.email.fill(value);
  }

  async enterPassword(value: string): Promise<void> {
    await this.password.fill(value);
  }

  async clickSubmit(): Promise<void> {
    await this.submitButton.click();
  }

  async login(email: string, password: string): Promise<void> {
    await this.enterEmail(email);
    await this.enterPassword(password);
    await this.clickSubmit();
  }

  // Getters — return Promise<string|boolean>
  async getErrorMessage(): Promise<string> {
    return (await this.errorMessage.textContent()) || '';
  }

  async isErrorVisible(): Promise<boolean> {
    return await this.errorMessage.isVisible();
  }
}
```

## Test class pattern

```typescript
import { test, expect } from '@playwright/test';
import { LoginPage } from '../pages/LoginPage';

test.describe('SC-LOGIN-001 — User authentication', () => {
  let loginPage: LoginPage;

  test.beforeEach(async ({ page }) => {
    loginPage = new LoginPage(page);
    await loginPage.goto('/login');
  });

  test('TC-LOGIN-001: Happy path / SC-LOGIN-001', async ({ page }) => {
    // Step 1: Enter email
    await loginPage.enterEmail(process.env.TEST_USERNAME!);

    // Step 2: Enter password
    await loginPage.enterPassword(process.env.TEST_PASSWORD!);

    // Step 3: Click submit
    await loginPage.clickSubmit();

    // Expected: Redirect to dashboard
    await expect(page).toHaveURL(/dashboard/);
  });

  test('TC-LOGIN-002: Invalid email format / SC-LOGIN-002 / Technique: EP-malformed-email', async () => {
    // Step 1: Enter malformed email
    await loginPage.enterEmail('not-an-email');

    // Step 2: Enter valid password
    await loginPage.enterPassword('Password123');

    // Step 3: Click submit
    await loginPage.clickSubmit();

    // Expected: Error message
    expect(await loginPage.isErrorVisible()).toBe(true);
    expect(await loginPage.getErrorMessage()).toContain('Email không hợp lệ');
  });
});
```

## Comprehensive mode — DataProvider equivalent

Replace TestNG `@DataProvider` với Playwright loop pattern:

```typescript
import { test, expect } from '@playwright/test';
import { LoginPage } from '../pages/LoginPage';

const passwordBoundary = [
  { length: 7,  expected: false, tcId: 'TC-AUTH-014', technique: 'BVA-min-1' },
  { length: 8,  expected: true,  tcId: 'TC-AUTH-015', technique: 'BVA-min' },
  { length: 9,  expected: true,  tcId: 'TC-AUTH-016', technique: 'BVA-min+1' },
  { length: 31, expected: true,  tcId: 'TC-AUTH-017', technique: 'BVA-max-1' },
  { length: 32, expected: true,  tcId: 'TC-AUTH-018', technique: 'BVA-max' },
  { length: 33, expected: false, tcId: 'TC-AUTH-019', technique: 'BVA-max+1' },
  { length: 0,  expected: false, tcId: 'TC-AUTH-020', technique: 'BVA-empty' },
];

test.describe('SC-AUTH-002 — Password length boundary (BVA suite)', () => {
  for (const data of passwordBoundary) {
    test(`${data.tcId} (${data.technique}): length ${data.length} → ${data.expected ? 'accept' : 'reject'}`, async ({ page }) => {
      const loginPage = new LoginPage(page);
      await loginPage.goto('/login');
      await loginPage.enterEmail('user@example.com');
      await loginPage.enterPassword('p'.repeat(data.length));
      await loginPage.clickSubmit();

      if (data.expected) {
        await expect(page).toHaveURL(/dashboard/);
      } else {
        expect(await loginPage.isErrorVisible()).toBe(true);
      }
    });
  }
});
```

**Alternative pattern (cleaner for large datasets):** Use `test.describe.parallel.each()` hoặc external JSON data file.

## Naming conventions

| Artifact | Pattern | Example |
|---|---|---|
| Page class file | `<Name>Page.ts` | `LoginPage.ts`, `DashboardPage.ts` |
| Test file | `<feature>.spec.ts` or `<feature>.<suite>.spec.ts` | `login.spec.ts`, `sales.smoke.spec.ts` |
| Locator property | descriptive camelCase | `submitButton`, `emailInput`, `errorMessage` |
| Action method | `verb<Target>()` (camelCase) | `clickSubmit()`, `enterEmail(value)`, `getErrorMessage()` |
| Test name | `'TC-<MODULE>-<NNN>: <title> / SC-<MODULE>-<NNN>'` (optional ` / Technique: <tag>`) | `'TC-LOGIN-001: Happy path / SC-LOGIN-001'` |
| Describe block | `'SC-<MODULE>-<NNN> — <feature name>'` | `'SC-LOGIN-001 — User authentication'` |

## Locator strategy priority (Playwright)

| Priority | API | When |
|---|---|---|
| 1 | `page.getByRole(role, options)` | Accessibility-friendly, preferred for buttons, headings, links |
| 2 | `page.getByLabel(text)` | Form fields with labels |
| 3 | `page.getByPlaceholder(text)` | Inputs với placeholder |
| 4 | `page.getByText(text)` | Visible text content |
| 5 | `page.getByTestId(testId)` | data-testid attribute (best for stable locators) |
| 6 | `page.locator('#id')` | CSS selector by id |
| 7 | `page.locator('.css-selector')` | CSS selector general |
| 8 | `page.locator('xpath=//...')` | XPath — last resort |

**Best practice:** Prefer `getByRole` + `getByLabel` for accessibility-friendly tests. Use `data-testid` when no semantic option exists.

## Required env vars (typical)

```bash
BASE_URL=http://localhost:3000          # Web app base URL
API_BASE_URL=http://localhost:8080      # Backend API base
TEST_USERNAME=test@example.com          # SSO/login test account
TEST_PASSWORD=<from credentials env>    # Sensitive — never inline
```

Source: `~/.<project-slug>/credentials.env` (per ONBOARDING §3d security guideline).

## Pipeline downstream behavior

Stack detected = TypeScript → downstream skills load TypeScript variants:

| Skill | Reference loaded |
|---|---|
| scan-source-code | `references/full-typescript.md` (file: `.ts` + `package.json` parse) |
| implement-automation | `references/implement-typescript.md` (Page class template + test() syntax) |
| execute-maintain | `references/run-typescript.md` (`npx playwright test` + JSON parsing) |
| review-src-tc | `references/full-typescript.md` (`.ts` file detection + test name TC ID parse) |

## Build verify (post-scaffold)

```bash
cd 10_source-code
npm install                              # Install deps (~50 MB → node_modules)
npx playwright install                   # Install browser binaries (~200 MB)
npx tsc --noEmit                         # TypeScript compile check
npx playwright test --list               # Verify Playwright can list tests (no tests yet, OK)
```

Expected: All commands exit 0. Nếu fail → check Node.js version (≥18), network (for npm download), disk space.

## See Also

- [archetypes.md](archetypes.md) — Full registry + comparison
- [archetype-selenium-java.md](archetype-selenium-java.md) — Java alternative cho web (enterprise)
- [archetype-appium-java.md](archetype-appium-java.md) — Mobile archetype (different stack)
- Scaffold script: [`../scripts/scaffold-playwright-ts.py`](../scripts/scaffold-playwright-ts.py)
- Playwright docs: https://playwright.dev/docs/intro
