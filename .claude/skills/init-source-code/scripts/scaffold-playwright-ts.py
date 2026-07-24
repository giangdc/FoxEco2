#!/usr/bin/env python3
"""
scaffold-playwright-ts.py — Auto-generate Playwright TypeScript archetype vào 10_source-code/

Usage:
    python3 scaffold-playwright-ts.py <project_root> [--project-name NAME] [--force] [--dry-run]

Args:
    project_root      Absolute path tới project root (chứa 00_input/, 01_test-plans/, etc.)
    --project-name    Override project name (default: read từ CLAUDE.md hoặc folder name)
    --force           Overwrite existing 10_source-code/ (backup as 10_source-code.bak.<timestamp>/)
    --dry-run         Print file list, don't write

Output:
    10_source-code/ populated với:
    - package.json, tsconfig.json, playwright.config.ts
    - src/pages/BasePage.ts
    - src/tests/fixtures.ts, setup.ts
    - src/utils/api-helpers.ts, data-helpers.ts
    - playwright-suites/{smoke,regression}.config.ts
    - MEMORY.md (§1-§19, §2 structured Tech Stack)
    - .gitignore, README.md

Exit codes:
    0  Success
    1  Bad args
    2  10_source-code/ non-empty + no --force
    3  Write error (permission, disk full)
"""
import argparse
import os
import shutil
import sys
from datetime import datetime, timezone
from pathlib import Path


# =============================================================================
# Template content
# =============================================================================

PACKAGE_JSON = '''{{
  "name": "{project_slug}-automation",
  "version": "1.0.0",
  "description": "Automation test suite for {project_name} (Playwright + TypeScript)",
  "private": true,
  "scripts": {{
    "test": "playwright test",
    "test:smoke": "playwright test --config=playwright-suites/smoke.config.ts",
    "test:regression": "playwright test --config=playwright-suites/regression.config.ts",
    "test:headed": "playwright test --headed",
    "test:debug": "playwright test --debug",
    "test:ui": "playwright test --ui",
    "typecheck": "tsc --noEmit",
    "report": "playwright show-report",
    "codegen": "playwright codegen"
  }},
  "devDependencies": {{
    "@playwright/test": "^1.42.0",
    "@types/node": "^20.0.0",
    "typescript": "^5.3.0"
  }},
  "engines": {{
    "node": ">=18.0.0",
    "npm": ">=10.0.0"
  }}
}}
'''


TSCONFIG_JSON = '''{
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
'''


PLAYWRIGHT_CONFIG = '''import { defineConfig, devices } from '@playwright/test';

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
'''


BASE_PAGE = '''import { Page, Locator, expect } from '@playwright/test';

/**
 * BasePage — abstract base cho mọi Page Object.
 * Provides shared utility methods: waitFor, scroll, screenshot, navigation.
 */
export abstract class BasePage {
  constructor(protected readonly page: Page) {}

  async goto(path: string = '/'): Promise<void> {
    await this.page.goto(path);
  }

  async waitForVisible(locator: Locator, timeout = 10_000): Promise<void> {
    await expect(locator).toBeVisible({ timeout });
  }

  async getURL(): Promise<string> {
    return this.page.url();
  }

  async screenshot(name: string): Promise<void> {
    await this.page.screenshot({ path: `test-results/${name}.png`, fullPage: true });
  }

  async scrollIntoView(locator: Locator): Promise<void> {
    await locator.scrollIntoViewIfNeeded();
  }

  async waitForNetworkIdle(timeout = 5_000): Promise<void> {
    await this.page.waitForLoadState('networkidle', { timeout });
  }
}
'''


FIXTURES_TS = '''import { test as base } from '@playwright/test';

/**
 * Custom fixtures — extend Playwright base test với project-specific fixtures.
 * Example fixtures (commented — uncomment + implement khi cần):
 *   - authenticatedPage: Page already logged in
 *   - apiHelper: ApiHelper instance
 *   - testDataFactory: factory function tạo test data
 */

type CustomFixtures = {
  // Define custom fixtures here (commented out cho boilerplate clean)
  // authenticatedPage: Page;
  // apiHelper: ApiHelper;
};

export const test = base.extend<CustomFixtures>({
  // Implement fixtures here. Example pattern:
  //
  // authenticatedPage: async ({ page }, use) => {
  //   await page.goto('/login');
  //   await page.fill('#email', process.env.TEST_USERNAME!);
  //   await page.fill('#password', process.env.TEST_PASSWORD!);
  //   await page.click('button[type=submit]');
  //   await page.waitForURL(/dashboard/);
  //   await use(page);
  // },
});

export { expect } from '@playwright/test';
'''


SETUP_TS = '''import { FullConfig } from '@playwright/test';

/**
 * Global setup — runs once before all tests.
 * Use cho: verify env vars, pre-warm data, capture auth storage state, validate API health.
 */
async function globalSetup(config: FullConfig): Promise<void> {
  const required = ['TEST_USERNAME', 'TEST_PASSWORD', 'BASE_URL'];
  for (const env of required) {
    if (!process.env[env]) {
      console.warn(`⚠️ Missing env var: ${env} — some tests may fail`);
    }
  }

  // Add additional global setup here.
}

export default globalSetup;
'''


API_HELPERS_TS = '''import { APIRequestContext, request } from '@playwright/test';

/**
 * ApiHelper — wraps Playwright APIRequestContext cho UI ↔ API cross-validation.
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
'''


DATA_HELPERS_TS = '''/**
 * Data helpers — parsers/formatters cho test data (vi-VN, en-US, etc.)
 */

/**
 * Parse vi-VN number format: "1.234,56" → 1234.56
 */
export function parseViVNNumber(str: string): number {
  return parseFloat(str.replace(/\\./g, '').replace(',', '.'));
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
 * Tolerance comparison cho float values.
 */
export function approxEqual(actual: number, expected: number, tolerance = 0.01): boolean {
  return Math.abs(actual - expected) <= tolerance;
}
'''


SMOKE_CONFIG = '''import { defineConfig } from '@playwright/test';
import baseConfig from '../playwright.config';

export default defineConfig({
  ...baseConfig,
  testMatch: /.*\\.smoke\\.spec\\.ts/,
  workers: 4,
  retries: 0,
  reporter: [
    ['html', { outputFolder: 'playwright-report-smoke' }],
    ['json', { outputFile: 'test-results/smoke-results.json' }],
  ],
});
'''


REGRESSION_CONFIG = '''import { defineConfig } from '@playwright/test';
import baseConfig from '../playwright.config';

export default defineConfig({
  ...baseConfig,
  testMatch: /.*\\.(spec|regression)\\.ts/,
  workers: 8,
  retries: 1,
  reporter: [
    ['html', { outputFolder: 'playwright-report-regression' }],
    ['json', { outputFile: 'test-results/regression-results.json' }],
  ],
});
'''


GITIGNORE = '''node_modules/
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
'''


README_TEMPLATE = '''# {project_name} — Automation (Playwright TypeScript)

> Scaffolded by `/init-source-code --archetype playwright-ts` on {date}.

## Quick Start

```bash
# 1. Install dependencies
npm install

# 2. Install Playwright browsers (Chromium + Firefox + WebKit ~200 MB)
npx playwright install

# 3. Source credentials (per project security guideline)
source ~/.{project_slug}/credentials.env

# 4. Run tests
npm test                          # All tests
npm run test:smoke                # Smoke suite only
npm run test:headed               # Headed mode (visible browser)
npm run test:debug                # Debug mode (Playwright Inspector)
npm run test:ui                   # Interactive UI mode

# 5. View report
npm run report
```

## Folder structure

```
src/
├── pages/        # Page Objects (BasePage + per-page classes)
├── tests/        # Test specs (.spec.ts) + fixtures + setup
└── utils/        # Helpers (API, data parsers, formatters)

playwright-suites/  # Suite configs (smoke, regression)
playwright.config.ts  # Default config
tsconfig.json         # TypeScript strict mode
```

## Environment vars (required)

| Var | Purpose | Source |
|---|---|---|
| `BASE_URL` | Web app base URL | Per environment |
| `API_BASE_URL` | Backend API base | Per environment |
| `TEST_USERNAME` | SSO/login test account | `~/.{project_slug}/credentials.env` |
| `TEST_PASSWORD` | Test account password | `~/.{project_slug}/credentials.env` |

## Next steps

1. `/scan-source-code` — Populate MEMORY §3-§19 với scaffold conventions
2. `/analyze-requirements --init @00_input/v1.0/` — Start QA pipeline (nếu chưa)
3. `/implement-automation --module <MODULE>` — Generate Page Objects + Test specs từ TC-MASTER

## See also

- Toolkit ONBOARDING: `~/.claude/skills/ONBOARDING.md`
- Playwright docs: https://playwright.dev/docs/intro
- Project context: `../CLAUDE.md`
'''


MEMORY_TEMPLATE = '''# MEMORY — 10_source-code/ — Automation Project

> Tạo bởi: skill `init-source-code` (archetype = playwright-ts)
> Cập nhật lần đầu: {date}
> Updated bởi: scan-source-code, implement-automation, execute-maintain skills

## 1. Project Structure

```
10_source-code/
├── package.json
├── tsconfig.json
├── playwright.config.ts
├── playwright-suites/
│   ├── smoke.config.ts
│   └── regression.config.ts
├── src/
│   ├── pages/       (Page Objects)
│   ├── tests/       (Test specs + fixtures + setup)
│   └── utils/       (Helpers)
└── MEMORY.md
```

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

> **CRITICAL:** Đừng đổi header column hoặc field "Language" — downstream skills (scan-source-code, implement-automation, execute-maintain, review-src-tc) parse exact format này để route variant references.

## 3. Dependencies

Read from `package.json`:
- `@playwright/test` (latest 1.x)
- `typescript` (5.x)
- `@types/node` (20.x)

(scan-source-code skill sẽ populate full list khi run.)

## 4. Base Classes

- `BasePage` (src/pages/BasePage.ts) — abstract base với common methods: goto, waitForVisible, screenshot, etc.

## 5. Naming Conventions

- Page class file: `<Name>Page.ts` (vd `LoginPage.ts`)
- Test file: `<feature>.spec.ts` (vd `login.spec.ts`)
- Suite test file: `<feature>.<suite>.spec.ts` (vd `sales.smoke.spec.ts`)
- Locator property: descriptive camelCase (vd `submitButton`, `emailInput`)
- Action method: `verb<Target>()` (vd `clickSubmit()`, `enterEmail(value)`)
- Test name: `'TC-<MODULE>-<NNN>: <title> / SC-<MODULE>-<NNN>'`

## 6. Page Registry

| Page class | File | Status |
|---|---|---|
| BasePage | src/pages/BasePage.ts | ✅ Scaffolded |
| (more populated by scan-source-code) | — | — |

## 7. Test Registry

| Test file | Tests count | Status |
|---|---|---|
| (populated by scan-source-code after first scan) | — | — |

## 8. Pipeline Status

(see MASTER-MEMORY §8)

## 9. Locator Registry

| Page | Element | Strategy | Selector | Last verified |
|---|---|---|---|---|
| (populated by scan-source-code / vibe-test) | — | — | — | — |

## 10. Suite Definitions

| Suite | Config | Test files |
|---|---|---|
| smoke | playwright-suites/smoke.config.ts | `*.smoke.spec.ts` |
| regression | playwright-suites/regression.config.ts | `*.{{spec,regression}}.ts` |

## 11. Build Verification History

| Date | Command | Status | Notes |
|---|---|---|---|
| {date} | npm install + npx tsc --noEmit | ⏳ Pending verify | scaffold output |

## 12. Locator Strategy Priority

1. `page.getByRole(role, options)` — accessibility-friendly (preferred)
2. `page.getByLabel(text)` — form fields
3. `page.getByPlaceholder(text)` — inputs
4. `page.getByText(text)` — visible text
5. `page.getByTestId(testId)` — `data-testid` attribute (stable)
6. `page.locator('#id')` — CSS by id
7. `page.locator('.css-selector')` — CSS general
8. `page.locator('xpath=//...')` — XPath last resort

## 13. Implementation Log

| Date | SC | TC ID | Test file | Method/test name | Notes |
|---|---|---|---|---|---|
| (populated by implement-automation) | — | — | — | — | — |

## 14. Locator Issues / Fixes

| Date | Element | Issue | Fix | By |
|---|---|---|---|---|
| (populated by execute-maintain recheck) | — | — | — | — |

## 15. Execution Log

| Run ID | Date | Version | Test scope | Command | Total | Pass | Fail | Skip | Pass% |
|---|---|---|---|---|---|---|---|---|---|
| (populated by execute-maintain) | — | — | — | — | — | — | — | — | — |

## 16. Fail Registry

| FAIL ID | RUN | Version | Test method | SC ID | Type | Error | Recheck | Status | Fix |
|---|---|---|---|---|---|---|---|---|---|
| (populated by execute-maintain) | — | — | — | — | — | — | — | — | — |

## 17. SRC-TC Review

| Date | Version | Reviewer | Score | Findings | Report |
|---|---|---|---|---|---|
| (populated by review-src-tc) | — | — | — | — | — |

## 18. Scan History

| Date | Mode | Version | Coverage | Notes |
|---|---|---|---|---|
| (populated by scan-source-code) | — | — | — | — |

## 19. Notes

- Scaffolded từ archetype `playwright-ts` on {date}
- Downstream skills (scan/implement/execute/review-src-tc) sẽ auto-route to TypeScript variants based on §2 Tech Stack
'''


# =============================================================================
# Scaffold logic
# =============================================================================

def parse_project_info(project_root: Path, override_name: str | None) -> tuple[str, str]:
    """Read project name + slug from CLAUDE.md or folder name."""
    project_name = override_name
    if not project_name:
        # Try CLAUDE.md
        claude_md = project_root / "CLAUDE.md"
        if claude_md.exists():
            for line in claude_md.read_text(encoding="utf-8").splitlines()[:30]:
                line = line.strip()
                # Look for "Tên dự án:" or "Project name:" patterns
                if "Tên dự án" in line or "Project name" in line:
                    # Extract value after colon, strip markdown
                    parts = line.split(":", 1)
                    if len(parts) == 2:
                        project_name = parts[1].strip().strip("`*").strip()
                        break
        if not project_name:
            project_name = project_root.name

    # Slugify
    slug = project_name.lower().replace(" ", "-").replace("_", "-")
    slug = "".join(c if c.isalnum() or c == "-" else "" for c in slug)
    return project_name, slug


def write_file(path: Path, content: str, dry_run: bool) -> None:
    """Write file with parent dirs. Dry-run: log only."""
    if dry_run:
        print(f"  [DRY-RUN] Would write: {path}")
        return
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8")
    print(f"  ✅ Wrote: {path.relative_to(path.parent.parent.parent)}")


def backup_existing(src_dir: Path, dry_run: bool) -> Path | None:
    """Move existing 10_source-code/ to backup with timestamp."""
    if not src_dir.exists() or not any(src_dir.iterdir()):
        return None
    ts = datetime.now(timezone.utc).strftime("%Y%m%d-%H%M%S")
    backup = src_dir.parent / f"{src_dir.name}.bak.{ts}"
    if dry_run:
        print(f"  [DRY-RUN] Would backup: {src_dir} → {backup}")
        return backup
    shutil.move(str(src_dir), str(backup))
    print(f"  📦 Backed up existing: {src_dir.name} → {backup.name}")
    return backup


def scaffold(project_root: Path, project_name: str, project_slug: str, dry_run: bool) -> int:
    """Generate all files. Returns count of files written."""
    src_dir = project_root / "10_source-code"
    date_str = datetime.now(timezone.utc).strftime("%Y-%m-%d")

    files = [
        # Top-level config
        (src_dir / "package.json", PACKAGE_JSON.format(project_slug=project_slug, project_name=project_name)),
        (src_dir / "tsconfig.json", TSCONFIG_JSON),
        (src_dir / "playwright.config.ts", PLAYWRIGHT_CONFIG),
        (src_dir / ".gitignore", GITIGNORE),
        (src_dir / "README.md", README_TEMPLATE.format(project_name=project_name, project_slug=project_slug, date=date_str)),
        (src_dir / "MEMORY.md", MEMORY_TEMPLATE.format(date=date_str)),

        # src/pages/
        (src_dir / "src" / "pages" / "BasePage.ts", BASE_PAGE),
        (src_dir / "src" / "pages" / ".gitkeep", ""),

        # src/tests/
        (src_dir / "src" / "tests" / "fixtures.ts", FIXTURES_TS),
        (src_dir / "src" / "tests" / "setup.ts", SETUP_TS),
        (src_dir / "src" / "tests" / ".gitkeep", ""),

        # src/utils/
        (src_dir / "src" / "utils" / "api-helpers.ts", API_HELPERS_TS),
        (src_dir / "src" / "utils" / "data-helpers.ts", DATA_HELPERS_TS),

        # playwright-suites/
        (src_dir / "playwright-suites" / "smoke.config.ts", SMOKE_CONFIG),
        (src_dir / "playwright-suites" / "regression.config.ts", REGRESSION_CONFIG),
    ]

    count = 0
    for path, content in files:
        write_file(path, content, dry_run)
        count += 1
    return count


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Scaffold Playwright TypeScript archetype into 10_source-code/",
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    parser.add_argument("project_root", type=Path, help="Absolute path tới project root")
    parser.add_argument("--project-name", default=None, help="Override project name")
    parser.add_argument("--force", action="store_true", help="Overwrite existing 10_source-code/ (with backup)")
    parser.add_argument("--dry-run", action="store_true", help="Print file list, don't write")
    args = parser.parse_args()

    project_root = args.project_root.resolve()

    if not project_root.exists() or not project_root.is_dir():
        print(f"❌ project_root không tồn tại hoặc không phải directory: {project_root}", file=sys.stderr)
        return 1

    # Check 00_input/ exists (rough check that project is initialized)
    if not (project_root / "00_input").exists():
        print(f"⚠️ Warning: '{project_root}/00_input/' not found. Project có thể chưa run /init-project.", file=sys.stderr)
        print(f"   Continuing anyway...", file=sys.stderr)

    src_dir = project_root / "10_source-code"

    # Check existing
    if src_dir.exists() and any(src_dir.iterdir()):
        if not args.force:
            print(f"❌ '{src_dir}' đã có files. Use --force để backup + overwrite.", file=sys.stderr)
            return 2
        backup_existing(src_dir, args.dry_run)

    # Read project info
    project_name, project_slug = parse_project_info(project_root, args.project_name)
    print(f"📦 Scaffolding Playwright TypeScript archetype")
    print(f"   Project: {project_name} (slug: {project_slug})")
    print(f"   Target: {src_dir}")
    print(f"   Mode: {'DRY-RUN' if args.dry_run else 'WRITE'}")
    print()

    try:
        count = scaffold(project_root, project_name, project_slug, args.dry_run)
    except OSError as e:
        print(f"❌ Write error: {e}", file=sys.stderr)
        return 3

    print()
    print(f"{'[DRY-RUN] Would create' if args.dry_run else '✅ Created'} {count} files.")
    if not args.dry_run:
        print()
        print("Next steps:")
        print(f"  1. cd {src_dir}")
        print(f"  2. npm install              # Install deps (~50 MB)")
        print(f"  3. npx playwright install   # Install browsers (~200 MB)")
        print(f"  4. npx tsc --noEmit         # Verify TypeScript compile")
        print(f"  5. /scan-source-code        # Populate MEMORY §3-§19")
        print()
        print("Pipeline now stack-aware: downstream skills auto-route to TypeScript variants.")

    return 0


if __name__ == "__main__":
    sys.exit(main())
