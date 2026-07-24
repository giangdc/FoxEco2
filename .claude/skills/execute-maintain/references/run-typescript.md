# Execute — Mode RUN — TypeScript variant

> **Loaded khi:** MEMORY §2 Tech Stack có `Language = TypeScript`.
> **Default (Java) variant:** [`run.md`](run.md) — loaded khi Language = Java hoặc trống.
> **Stack detection:** Xem `~/.claude/skills/init-source-code/references/memory-section-2-format.md`.

## Workflow

### Step 1: Đọc context + guard
Check implement-automation ≥ PARTIAL. Đọc Source MEMORY §4-§7.
Verify §2 Tech Stack: `Language = TypeScript`.
Đọc MASTER-MEMORY → active version. Ghi §8 = IN_PROGRESS.

### Step 2: Chạy test

**🔐 Credential check FIRST** (per security guideline — same as Java variant):

```bash
test -n "$TEST_USERNAME" && test -n "$TEST_PASSWORD" && echo "ENV_OK" || echo "ENV_MISSING"
```

Nếu `ENV_MISSING` → ask user: *"Run `! source ~/.<project>/credentials.env` then retry."* KHÔNG echo password. KHÔNG inline credentials vào npm/playwright command.

**Verify deps installed first time:**

```bash
cd 10_source-code
test -d node_modules || (echo "Installing deps..." && npm install)
test -d ~/.cache/ms-playwright || npx playwright install
```

**Then run** (env vars inherited from sourced session — command KHÔNG chứa secret):

```bash
cd 10_source-code

# Run all tests
npx playwright test

# Run specific test file
npx playwright test src/tests/login.spec.ts

# Run by test name pattern (filter via -g grep)
npx playwright test -g "TC-LOGIN-001"

# Run by describe block
npx playwright test -g "SC-LOGIN-001"

# Run với suite config
npx playwright test --config=playwright-suites/smoke.config.ts

# Run with specific project (browser)
npx playwright test --project=chromium

# Headed mode (visible browser — debugging)
npx playwright test --headed

# Debug mode (Playwright Inspector — step through)
npx playwright test --debug

# UI mode (interactive)
npx playwright test --ui

# Repeat each test N times (flake detection)
npx playwright test --repeat-each=3

# Workers (parallel) override
npx playwright test --workers=4

# Run npm script wrapper
npm test
npm run test:smoke
npm run test:regression
```

### Step 3: Parse output

Playwright Test JSON reporter output: `10_source-code/test-results/results.json` (configured trong `playwright.config.ts`).

**JSON structure (Playwright reporter):**

```json
{
  "config": { ... },
  "suites": [
    {
      "title": "login.spec.ts",
      "specs": [
        {
          "title": "TC-LOGIN-001: Happy path / SC-LOGIN-001",
          "tests": [
            {
              "projectName": "chromium",
              "results": [
                {
                  "status": "passed",     // or "failed", "skipped", "timedOut"
                  "duration": 1234,
                  "retry": 0,
                  "errors": []
                }
              ]
            }
          ]
        }
      ]
    }
  ],
  "stats": {
    "expected": 50,
    "unexpected": 2,    // = failed
    "flaky": 1,
    "skipped": 3,
    "duration": 45000
  }
}
```

**Parse logic:**

```python
import json
with open("10_source-code/test-results/results.json") as f:
    data = json.load(f)

total = data["stats"]["expected"] + data["stats"]["unexpected"]
passed = data["stats"]["expected"]
failed = data["stats"]["unexpected"]
flaky = data["stats"]["flaky"]
skipped = data["stats"]["skipped"]

# Per-test details
for suite in data["suites"]:
    for spec in suite.get("specs", []):
        for test in spec.get("tests", []):
            for result in test.get("results", []):
                # Extract: spec["title"] (test name), result["status"], result["errors"]
                ...
```

**Stdout/console output alternative** (when JSON reporter not configured):

```
Running 50 tests using 4 workers
  ✓  1 [chromium] › login.spec.ts:5:7 › TC-LOGIN-001: Happy path / SC-LOGIN-001 (1.2s)
  ✗  2 [chromium] › login.spec.ts:18:7 › TC-LOGIN-002: Invalid email / SC-LOGIN-002 (3.4s)
  ...
  2 failed
  50 passed (45s)
```

Parse line-by-line: `✓` = pass, `✗` = fail, `↪` = skip.

**Trace + screenshot artifacts:**

- `test-results/<test-name>/trace.zip` — Playwright trace file (timeline + DOM snapshots)
- `test-results/<test-name>/screenshot.png` — failure screenshot (on by default per config)
- `test-results/<test-name>/video.webm` — failure video

Reference these artifacts trong Fail Registry §16.

### Step 4: Classify failures (TS-specific patterns)

| Fail Type | Dấu hiệu (Playwright error messages) | Action | Bug? |
|---|---|---|---|
| **LOCATOR_STALE** | `Error: locator.click: Target page, context or browser has been closed` · `TimeoutError: locator.waitFor: Timeout 30000ms exceeded` · `Error: locator.fill: Element is not visible` · `strict mode violation: locator resolved to N elements` | Cần update locator (`/implement-automation --update`) | ❌ Không (lỗi code/locator drift) |
| **ASSERTION_FAIL** | `Error: expect(received).toBe(expected)` · `expect(locator).toHaveText` failed · `expect(page).toHaveURL` failed · `Expected: "X" Received: "Y"` | Có thể app bug → `/log-bug` | ✅ Có thể |
| **ENV_ERROR** | `Error: connect ECONNREFUSED` · `Error: page.goto: net::ERR_*` · `Error: Browser closed` · `Test timeout exceeded` (env slow) · `HTTP 500/502/503` từ API | Env/network issue | ❌ Không |
| **UNKNOWN** | `TypeError: Cannot read properties of undefined` · `ReferenceError` · `SyntaxError` · custom uncaught exceptions | Manual investigation | ❌ Không |

**TypeScript-specific edge cases:**

- `Error: process.env.X is undefined` → ENV_ERROR (missing credentials.env source)
- `Error: Cannot find module '@pages/...'` → ENV_ERROR (tsconfig paths misconfigured hoặc node_modules missing)
- `tsc errors` trước khi test chạy → block test execution, classify as ENV_ERROR

### Step 5: Ghi Source MEMORY §15 + §16

**§15 Execution Log** (format giống Java variant):

```
| RUN-001 | 2026-05-31 | v1.0 | LoginTest | npx playwright test src/tests/login.spec.ts | 5 | 3 | 1 | 1 | 60% |
```

Cột command ghi đầy đủ `npx playwright test ...` thay vì `mvn test ...`.

**§16 Fail Registry (1 row per failure):**

```
| FAIL-001 | RUN-001 | 2026-05-31 | v1.0 | login.spec.ts › TC-LOGIN-002 | SC-LOGIN-002 | ASSERTION_FAIL | expect(locator).toHaveText: Expected "Email không hợp lệ" Received "Invalid email" | Open | trace: test-results/login-TC-LOGIN-002/trace.zip |
```

Cột "Recheck" có thể link tới Playwright trace file path (more useful than Java stack trace).

### Step 6: Present

```
🏃 RUN-001 (v1.0) — login.spec.ts
   Total: 5 | ✅ Pass: 3 | ❌ Fail: 1 | ⏭ Skip: 1 | Rate: 60%
   Duration: 12.3s
   Artifacts: test-results/, playwright-report/

   Failures:
   FAIL-001 | ASSERTION_FAIL | TC-LOGIN-002: Invalid email / SC-LOGIN-002
     Expected: "Email không hợp lệ"
     Received: "Invalid email" (tiếng Anh)
     File: src/tests/login.spec.ts:18
     Trace: test-results/chromium-login-TC-LOGIN-002/trace.zip
     → Suggest: /log-bug (ASSERTION_FAIL = possible app bug — message localization)

   FAIL-002 | LOCATOR_STALE | TC-LOGIN-003: SSO redirect / SC-LOGIN-003
     Error: locator.click: TimeoutError waiting for locator('button#sso-google')
     File: src/tests/login.spec.ts:35
     → Suggest: /implement-automation --update "locator sso-google needs re-capture"

   View HTML report: npm run report (open playwright-report/index.html)

Next:
  /execute-maintain --diagnose FAIL-001      ← analyze chi tiết
  /log-bug                          ← create bug cho ASSERTION_FAIL
  /execute-maintain --recheck FAIL-002       ← Playwright MCP verify locator state
```

Ghi MASTER-MEMORY §8 = COMPLETED.

## Edge Cases (TypeScript-specific)

### Playwright browsers chưa install

```bash
npx playwright test
# Error: browserType.launch: Executable doesn't exist at ...
```

→ Run `npx playwright install` (downloads Chromium + Firefox + WebKit ~200 MB).
Mark RUN as ENV_ERROR, suggest fix.

### `node_modules/` mismatch package-lock.json

```bash
# Symptom: TypeError unrelated to test logic
```

→ Suggest `npm ci` (clean install based on lock file).

### tsc errors block test execution

```bash
npx tsc --noEmit
# Error: Cannot find module '@pages/LoginPage' from 'src/tests/login.spec.ts'
```

→ Block test run. Classify ENV_ERROR. Suggest:
- Check `tsconfig.json` paths config
- Verify import path matches actual file location
- Run `npm install` để refresh deps

### Headless vs headed mode

- Default headless cho CI/automation
- Headed only khi debug local
- `--headed` flag adds `,headless: false` to projects

### Test timeout vs assertion timeout

- **Test timeout** (per test): default 30s — overall test must complete
- **Action timeout** (`use.actionTimeout`): default 15s — single action (click/fill)
- **Navigation timeout** (`use.navigationTimeout`): default 30s — page.goto/waitForNavigation
- **Expect timeout** (`use.expect.timeout`): default 5s — assertion polling

Khi fail với "Test timeout" → review nếu cần increase via config hoặc test optimization needed.

### Flaky test detection

Playwright tracks flaky tests: passes on retry, fails on first attempt.

```
2 passed
1 flaky
  ↻  login.spec.ts › TC-LOGIN-001: Happy path (retries: 1)
```

→ Mark as FLAKE trong §16 (separate from FAIL). Investigate root cause (timing, race condition, env).

### Parallel workers + shared state

Playwright fully parallel by default. Tests SHOULD be independent (no shared state). Nếu tests có shared state:
- Use `fixtures.ts` với `scope: 'worker'` cho shared resource
- Set `workers: 1` (disable parallel) cho debug
- Use `test.describe.serial(...)` cho sequential test order trong group

Symptom of shared state issue: tests pass solo, fail when parallel.

### Trace viewer (debugging fails)

```bash
npx playwright show-trace test-results/<test-name>/trace.zip
```

Opens interactive viewer với timeline, DOM snapshots, network log. Reference link trong §16 Recheck column.

### Recheck via Playwright MCP (recheck mode)

Khi recheck FAIL-N qua MCP Playwright (analog to Java's Appium MCP recheck):

```bash
# Manual: Use Playwright MCP tools để navigate + verify locator state
# Skill calls MCP browser_navigate → page snapshot → verify if locator still exists
```

Skill `/execute-maintain --recheck FAIL-002` workflow same as Java — but uses Playwright MCP cho web instead of Appium MCP cho mobile.

## TypeScript-specific test command cheat sheet

| Goal | Command |
|---|---|
| Run all tests | `npx playwright test` |
| Run specific file | `npx playwright test src/tests/login.spec.ts` |
| Run specific test by name | `npx playwright test -g "TC-LOGIN-001"` |
| Run smoke suite | `npx playwright test --config=playwright-suites/smoke.config.ts` |
| Run regression | `npx playwright test --config=playwright-suites/regression.config.ts` |
| Run on specific browser | `npx playwright test --project=chromium` (or firefox/webkit) |
| Headed (visible) | `npx playwright test --headed` |
| Debug mode | `npx playwright test --debug` |
| UI mode (interactive) | `npx playwright test --ui` |
| Trace on every run | `npx playwright test --trace=on` |
| Workers override | `npx playwright test --workers=1` (disable parallel) |
| Repeat for flake | `npx playwright test --repeat-each=3` |
| Update snapshots | `npx playwright test --update-snapshots` |
| View HTML report | `npx playwright show-report` (or `npm run report`) |
| View trace | `npx playwright show-trace test-results/.../trace.zip` |

## Checklist

- [ ] `npx playwright test` chạy thật, parse JSON output thật
- [ ] §2 Tech Stack verified (Language = TypeScript)
- [ ] Credentials sourced via env file (KHÔNG inline)
- [ ] `node_modules/` + Playwright browsers installed
- [ ] Mỗi failure classified (LOCATOR/ASSERTION/ENV/UNKNOWN) với TS-specific patterns
- [ ] §15 Execution Log ghi run + version + npx command
- [ ] §16 Fail Registry ghi per failure + version + trace artifact path
- [ ] Flaky tests separated (not counted as FAIL)
- [ ] MASTER-MEMORY §8 = COMPLETED

## See Also

- [`run.md`](run.md) — Java default variant (mvn test)
- [`~/.claude/skills/init-source-code/references/archetype-playwright-ts.md`](../../init-source-code/references/archetype-playwright-ts.md) — TS archetype config (playwright.config.ts reference)
- [`~/.claude/skills/execute-maintain/references/recheck.md`](recheck.md) — Recheck mode (MCP-based, generic)
- Playwright Test docs: https://playwright.dev/docs/test-cli
