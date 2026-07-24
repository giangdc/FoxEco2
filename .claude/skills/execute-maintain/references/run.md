# Execute — Mode RUN

> `/execute-maintain --run LoginTest` | `/execute-maintain --run-all`

## Workflow

### Step 1: Đọc context + guard
Check implement-automation ≥ PARTIAL. Đọc Source MEMORY §4-§7.
Đọc MASTER-MEMORY → active version. Ghi §8 = IN_PROGRESS.

### Step 2: Chạy test

**🔐 Credential check FIRST** (nếu suite cần SSO):
```bash
test -n "$SSO_USERNAME" && test -n "$SSO_PASSWORD" && echo "ENV_OK" || echo "ENV_MISSING"
```
Nếu `ENV_MISSING` → ask user: *"Run `! source ~/.dashboard-report/credentials.env` then retry."* KHÔNG echo password value. KHÔNG inline `SSO_PASSWORD="..."` vào mvn command.

**Then run** (env vars inherited from sourced session — Bash command KHÔNG chứa secret):
```bash
cd 10_source-code/[repo]
mvn test -Dtest=LoginTest                    # 1 class
mvn test                                      # all
mvn test -Dtest=LoginTest#testLoginSuccess    # 1 method
mvn test -Dgroups=smoke                       # by group
mvn test -PSmoke -Dsurefire.suiteXmlFiles=testSuites/smoke.xml   # full smoke
```

### Step 3: Parse output
Extract từ Maven/TestNG output:
- Total tests, passed, failed, skipped, errors
- Per-method: name, status, duration, error message + stack trace (if fail)
- Surefire reports: `target/surefire-reports/*.xml`

### Step 4: Classify failures

| Fail Type | Dấu hiệu | Action | Bug? |
|-----------|----------|--------|------|
| LOCATOR_STALE | NoSuchElementException, StaleElementReferenceException | Cần update locator (`/implement-automation --update`) | ❌ Không (lỗi code) |
| ASSERTION_FAIL | AssertionError, ComparisonFailure | Có thể app bug → `/log-bug` | ✅ Có thể |
| ENV_ERROR | ConnectionException, TimeoutException, HTTP 500 | Env issue | ❌ Không |
| UNKNOWN | Khác (NullPointer, ClassNotFound...) | Manual investigation | ❌ Không |

### Step 5: Ghi Source MEMORY §15 + §16

**§15 Execution Log:**
```
| RUN-001 | 2026-05-25 | v2.0 | LoginTest | mvn test -Dtest=LoginTest | 5 | 3 | 1 | 1 | 60% |
```

**§16 Fail Registry (1 row per failure):**
```
| FAIL-001 | RUN-001 | 2026-05-25 | v2.0 | LoginTest.testLoginInvalidEmail | SC-LOGIN-002 | ASSERTION_FAIL | Expected "Email không hợp lệ" got "Invalid email" | Open | — |
```

### Step 6: Present

```
🏃 RUN-001 (v2.0) — LoginTest
   Total: 5 | ✅ Pass: 3 | ❌ Fail: 1 | ⏭ Skip: 1 | Rate: 60%

   Failures:
   FAIL-001 | ASSERTION_FAIL | testLoginInvalidEmail
     Expected: "Email không hợp lệ"
     Actual: "Invalid email" (tiếng Anh)
     → Suggest: /log-bug (ASSERTION_FAIL = possible app bug)

   FAIL-002 | LOCATOR_STALE | testLoginSSO
     Error: NoSuchElementException: button#sso-google
     → Suggest: /implement-automation --update "locator sso-google đổi"

Next:
  /execute-maintain --diagnose FAIL-001      ← phân tích chi tiết
  /log-bug                          ← tạo bug cho ASSERTION_FAIL
  /execute-maintain --recheck FAIL-002       ← Playwright verify locator
```

Ghi §8 = COMPLETED.

## Checklist
- [ ] `mvn test` chạy thật, parse output thật
- [ ] Mỗi failure classified (LOCATOR/ASSERTION/ENV/UNKNOWN)
- [ ] §15 Execution Log ghi run + version
- [ ] §16 Fail Registry ghi per failure + version
- [ ] §8 = COMPLETED
