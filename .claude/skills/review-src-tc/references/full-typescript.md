# Review SRC-TC — Mode FULL — TypeScript variant

> **Loaded khi:** MEMORY §2 Tech Stack có `Language = TypeScript`.
> **Default (Java) variant:** [`full.md`](full.md).
> **Stack detection:** Xem `~/.claude/skills/init-source-code/references/memory-section-2-format.md`.

## Workflow

### Step 1: Đọc context + guard
Check implement-automation ≥ PARTIAL + generate-tc ≥ PARTIAL.
Đọc Source MEMORY §7 (Test Registry), §13 (Implementation Log).
Verify §2 Tech Stack: `Language = TypeScript`.
Ghi MASTER-MEMORY §8 review-src-tc = IN_PROGRESS.

### Step 2: Parse TC-MASTER

Template ISC (42 cột A-AP). Extract per TC: TC ID (**cột A**, formula `[Mã CN].[STT]` — vd `TC_01.2`), Req ID (**cột B** — thay cho SC ID, template không còn Scenario ID column), Steps (**cột H**), Expected (**cột I** — test data inline trong text, không có cột Test Data riêng), Remark (**cột AP** — technique tag nếu có).
(Same logic as Java variant — xem `full.md` Step 2 cho bảng map cột đầy đủ; TC parsing language-neutral.)

### Step 3: Read test files

```bash
find 10_source-code/src/tests/ -name "*.spec.ts" -not -name "fixtures.ts" -not -name "setup.ts"
```

Extract per `test()` call:
- **Test name:** parse pattern `'[TC ID]: <title> / [Req ID]'` (vd `'TC_01.1: Happy path / REQ-01'`; optional ` / Technique: <tag>`)
- **`// Step N:` comments** → paired with action lines below (TypeScript inline comments)
- **`// Expected N:` comments** → paired with assertion lines below
- **Hardcoded data values** (string literals trong test body)
- **Page class usage** (vd `await loginPage.enterEmail(...)`)

### Step 4: Pair TC ↔ test() call

**Match strategy:**
1. Test name chứa TC ID (pattern `TC_[Mã CN].[STT]:` — formula-derived, KHÔNG semantic) → direct match
2. Source MEMORY §13 mapping (TC ID → test file + test name)
3. Test name has scenario hint → fuzzy match (last resort)

**Results:**
- **MATCHED:** TC có test() call tương ứng
- **NOT_IMPLEMENTED:** TC không có test → gap
- **ORPHAN_TEST:** test() call không link về TC nào → dead test hoặc undocumented

### Step 5: Agent review (hoặc direct)

**Agent mode** (when reviewer agent available):

Agent payload (TypeScript variant):
```json
{
    "language": "typescript",
    "pairs": [
        {
            "tc_id": "TC_01.1",
            "req_id": "REQ-01",
            "tc_steps": [
                "1. Nhập 'user@test.com' vào field Email",
                "2. Nhập 'Test@123' vào field Password",
                "3. Nhấn button Đăng nhập"
            ],
            "tc_expected": [
                "1. Redirect về trang Dashboard",
                "2. Hiển thị username 'user@test.com' trên header"
            ],
            "tc_data": {"Email": "user@test.com", "Password": "Test@123"},
            "test_file": "src/tests/login.spec.ts",
            "test_name": "TC_01.1: Happy path / REQ-01",
            "code_steps": [
                "// Step 1: Nhập 'user@test.com' vào field Email\nawait loginPage.enterEmail('user@test.com');",
                "// Step 2: Nhập 'Test@123' vào field Password\nawait loginPage.enterPassword('Test@123');",
                "// Step 3: Nhấn button Đăng nhập\nawait loginPage.clickSubmit();"
            ],
            "code_assertions": [
                "// Expected 1: Redirect về trang Dashboard\nawait expect(page).toHaveURL(/dashboard/);"
            ],
            "code_data": {"email": "user@test.com", "password": "Test@123"}
        }
    ],
    "not_implemented": ["TC_01.5", "TC_01.6"],
    "orphan_tests": ["testOldFeature"]
}
```

> `tc_data` parse trực tiếp từ text `tc_steps`/`tc_expected` — template không có cột Test Data riêng, không phải trường Excel thật, chỉ dùng nội bộ để đối chiếu M3.

Agent applies M1-M4 checks (same definitions as Java variant — logic identical, syntax patterns adapted):

**M1: Step Coverage**
| Check | Severity | Logic (TS) |
|---|---|---|
| M1-01 | Critical | TC step thiếu code → `// Step N` comment hoặc await action không có |
| M1-02 | Major | Code có step thừa → action không match TC step nào |
| M1-03 | Minor | Step comment text khác TC → `// Step 1: Login` vs TC "Nhấn Đăng nhập" |
| M1-04 | Minor | Step numbering sai → `// Step 3` nhảy qua `// Step 2` |

**M2: Assertion Coverage**
| Check | Severity | Logic (TS) |
|---|---|---|
| M2-01 | Critical | TC expected thiếu assertion → `// Expected N` hoặc `expect(...)` không có |
| M2-02 | Major | Expected không thể automate nhưng thiếu `// MANUAL VERIFY` comment |
| M2-03 | Minor | Assertion message không chứa "Expected N:" prefix trong fail message |
| M2-04 | Minor | Assertion type mismatch → `expect(x).toBe(true)` khi cần `expect(x).toEqual(value)` · `expect(locator).toBeVisible()` khi cần `toHaveText()` · etc. |

**M3: Data Accuracy**
| Check | Severity | Logic (TS) |
|---|---|---|
| M3-01 | Critical | Hardcoded data ≠ giá trị inline trong TC **Steps (cột H)** → code dùng `'admin'` nhưng TC nói `'user@test.com'`. Template không có cột Test Data riêng. |
| M3-02 | Major | Data hardcoded thay vì parameterized (khi cần loop pattern) — vd password boundary suite nên dùng `for (const data of [...])` thay vì 7 test() calls riêng |
| M3-03 | Minor | Data format khác → code `'user@test.com'` vs TC `'user@test.com '` (trailing space) |
| M3-04 | Minor | Env var reference thiếu non-null assertion → `process.env.TEST_USERNAME` (lỗi TS) thay vì `process.env.TEST_USERNAME!` hoặc check |

**M4: Traceability**
| Check | Severity | Logic (TS) |
|---|---|---|
| M4-01 | Major | Test name thiếu TC ID (cột A) → `test('Happy path', ...)` thay vì `test('TC_01.1: Happy path / REQ-01', ...)` |
| M4-02 | Major | Test name thiếu Req ID (cột B) — bắt buộc include `/ REQ-XX` part. Template ISC không còn Scenario ID column, Req ID là khóa truy vết thay thế. |
| M4-03 | Minor | Test name không reflect scenario — vague title |
| M4-04 | Minor | **(cập nhật 2026-07-21, trước đây "Notes column")** Khi Version MEMORY §9 (TC Gen Log) Mode = `comprehensive`/`selective` và TC **Remark (cột AP)** có `Technique: <tag>`: test name nên include `/ Technique: <tag>` để truy nguồn (vd `'TC_03.14: Password length 7 / REQ-08 / Technique: BVA-min-1'`). Missing = Minor info. |

**Direct mode:** Main Claude runs M1-M4 + disclaimer + score capped 85.

### 🆕 Comprehensive mode awareness (TS-specific)

Khi Version MEMORY §9 (TC Gen Log) Mode = `comprehensive` HOẶC `selective`, derived TCs có thể được implement bằng 2 cách trong TypeScript:

**A. 1:1 mapping** — mỗi derived TC có test() riêng:
```typescript
test('TC_03.14: Password length 7 / REQ-08 / Technique: BVA-min-1', async ({ page }) => {
  // ... test logic for length 7
});

test('TC_03.15: Password length 8 / REQ-08 / Technique: BVA-min', async ({ page }) => {
  // ... test logic for length 8
});

// ... 5 more test() calls
```

**B. 1:N parameterized loop** — `for...of` loop với inline test data:
```typescript
const passwordBoundary = [
  { length: 7,  expected: false, tcId: 'TC_03.14', technique: 'BVA-min-1' },
  { length: 8,  expected: true,  tcId: 'TC_03.15', technique: 'BVA-min' },
  // ... 5 more rows
];

test.describe('REQ-08 — Password length boundary (BVA suite)', () => {
  for (const data of passwordBoundary) {
    test(`${data.tcId}: length ${data.length} / REQ-08 / Technique: ${data.technique}`, async ({ page }) => {
      // ... test logic using data.length, data.expected
    });
  }
});
```

**Reviewer xử lý (TS-specific):**

| Pattern | M1 (Step Coverage) behavior | Orphan-test classification |
|---|---|---|
| Pattern A (1:1) | Apply M1 chuẩn — verify mỗi test() có TC ID trong name | test() không có TC ID match TC-MASTER = orphan |
| Pattern B (1:N loop) | Verify loop array size = derived TC count; mỗi item có `tcId` field (giá trị đúng cột A đã resolve, KHÔNG tự đặt); test name template chứa `${tcId}` interpolation | Loop array items mapping vào TC IDs → KHÔNG flag orphan; Source MEMORY §13 entry: cột "Test method" can be range (`testFooBoundary` covers `TC_03.14..TC_03.20`) |
| Hybrid | Document trong Source MEMORY §13: cột "Test method" có thể là single hoặc range | Per case |

**Edge cases (TS-specific additions):**

| Scenario | Handling |
|---|---|
| Comprehensive mode + loop parameterized | M1 PASS nếu loop array size = derived TC count. Verify test name template chứa `${data.tcId}` + `${data.technique}` interpolation. |
| Test count < TC count (post-comprehensive) | Acceptable nếu loop parameterized — log INFO instead of WARNING |
| Test name template chứa "Technique:" interpolation | M4-04 PASS — improved traceability |
| Test name thiếu "Technique:" (Mode=comprehensive) | M4-04 Minor — suggest add for traceback |
| Source MEMORY §13 entry list TC ID range (`TC_03.14..TC_03.20`) | Treat as 1:N parameterized, accept |
| Inline data array trong test file (not external JSON) | OK — Pattern B. Verify data shape complete. |
| External JSON data file imported | Verify JSON file content matches expected TC range; trace import path |
| `tcId` trong loop array không khớp giá trị cột A thật (bị tự đặt/đoán) | M4-01 Major — traceability giả, phải sửa lại đúng giá trị resolve từ Excel |

## TypeScript-specific patterns

### Comment conventions

```typescript
test('TC_01.1: Happy path / REQ-01', async ({ page }) => {
  // Step 1: Navigate to login page
  await page.goto('/login');

  // Step 2: Enter email
  const loginPage = new LoginPage(page);
  await loginPage.enterEmail('user@test.com');

  // Step 3: Enter password
  await loginPage.enterPassword('Test@123');

  // Step 4: Click submit
  await loginPage.clickSubmit();

  // Expected 1: Redirect to dashboard
  await expect(page).toHaveURL(/dashboard/);

  // Expected 2: Username displayed
  await expect(page.locator('.user-greeting')).toContainText('user@test.com');
});
```

### Assertion type mapping (M2-04 reference)

| TC Expected says | Correct Playwright assertion |
|---|---|
| "Hiển thị text X" | `await expect(locator).toHaveText('X')` |
| "Hiển thị element" | `await expect(locator).toBeVisible()` |
| "Element chứa text X" | `await expect(locator).toContainText('X')` |
| "URL redirect to /X" | `await expect(page).toHaveURL(/X/)` |
| "Element disabled" | `await expect(locator).toBeDisabled()` |
| "Element count = N" | `await expect(locator).toHaveCount(N)` |
| "Element attribute X = Y" | `await expect(locator).toHaveAttribute('X', 'Y')` |
| "Element value = X" | `await expect(locator).toHaveValue('X')` |
| Boolean truthy | `expect(value).toBeTruthy()` (KHÔNG dùng `toBe(true)` trừ khi exact boolean) |
| Value equals | `expect(actual).toEqual(expected)` (deep) hoặc `toBe(expected)` (reference) |

### Page Object usage pattern (good vs bad)

**✅ GOOD (M3 PASS):**
```typescript
const loginPage = new LoginPage(page);
await loginPage.enterEmail('user@test.com');  // matches TC step
```

**❌ BAD (M3 fail):**
```typescript
// Inline locator — bypass Page Object
await page.locator('#email').fill('user@test.com');  // KHÔNG dùng LoginPage
```

→ M3-02 Major: "Should use Page Object pattern (LoginPage class), found inline locator"

### Env var usage (M3-04)

**✅ GOOD:**
```typescript
await loginPage.enterEmail(process.env.TEST_USERNAME!);  // non-null assertion
```

**⚠️ Acceptable nhưng safer:**
```typescript
const username = process.env.TEST_USERNAME ?? 'fallback@example.com';
await loginPage.enterEmail(username);
```

**❌ BAD:**
```typescript
await loginPage.enterEmail(process.env.TEST_USERNAME);  // TS error: undefined assignable to string
```

→ M3-04 Minor: "Missing non-null assertion on env var; TypeScript strict mode will error"

## Edge Cases

### Test file uses `test.describe.only()` hoặc `test.only()`

```
⚠️ Test file có `.only()` modifier — sẽ skip tất cả tests khác khi run.
Mark as anti-pattern trong M1 findings: "Remove .only() before committing"
```

### Test bị `.skip()` không kèm reason

```typescript
test.skip('TC_02.5: Auto-refresh / REQ-05', ...);  // ⚠️ No reason
```

→ M1-Info: "Skipped test thiếu reason comment. Add `// SKIPPED: timing-dependent, defer post-mock`"

### Test name không follow pattern

Vd `test('login works', ...)` thay vì `test('TC_01.1: ... / REQ-01', ...)`:
→ M4-01 Major: "Test name thiếu TC ID, KHÔNG traceable"

### Test có `expect()` nhưng KHÔNG await

```typescript
expect(page).toHaveURL(/dashboard/);  // ⚠️ Missing await
```

→ M2-Critical: "Missing await on async assertion — assertion KHÔNG actually execute"

## Quy tắc

- **KHÔNG sửa code** — issues → ghi findings + recommendations, user fix
- **KHÔNG run tests** — review = static analysis only
- **TC ID convention giống nhau giữa Java và TS** — cả 2 đều dùng nguyên giá trị cột A đã resolve (`[Mã CN].[STT]`, vd `TC_01.1`), KHÔNG tự đặt chuỗi semantic ở bất kỳ stack nào
- **Score 0-100** — deduction 100 − (Critical×5 + Major×3 + Minor×1), giống R-score review-tc. LƯU Ý: Java variant (full.md) dùng **Match Rate %** làm metric chính — 2 metric KHÁC nhau, mỗi bên gate G7 ≥ 70 riêng, không so trực tiếp cross-stack.
- **G7 gate:** SRC-TC score ≥ 70 cho release

## Checklist

- [ ] §2 Tech Stack verified (Language = TypeScript)
- [ ] TC-MASTER parsed
- [ ] All `.spec.ts` files read
- [ ] TC ↔ test() pairs identified (MATCHED / NOT_IMPLEMENTED / ORPHAN_TEST)
- [ ] M1-M4 checks applied per pair
- [ ] Comprehensive mode awareness (loop pattern detection)
- [ ] Score computed (Critical × 5 + Major × 3 + Minor × 1)
- [ ] Report output: `11_tc-review/src-tc-review-v[X].md`
- [ ] MASTER-MEMORY §8 = COMPLETED

## See Also

- [`full.md`](full.md) — Java default variant
- [`~/.claude/skills/init-source-code/references/archetype-playwright-ts.md`](../../init-source-code/references/archetype-playwright-ts.md) — TS conventions reference
- [`~/.claude/skills/implement-automation/references/implement-typescript.md`](../../implement-automation/references/implement-typescript.md) — TS code generation patterns (when implemented, Phase D)
