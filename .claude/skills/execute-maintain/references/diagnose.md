# Execute — Mode DIAGNOSE

> `/execute-maintain --diagnose FAIL-001`
> Phân tích root cause cho 1 failure cụ thể.

## Workflow

### Step 1: Đọc failure context
```
1. Source MEMORY §16 → lấy FAIL-001:
   - Run ID, Date, Version
   - Class.Method: LoginTest.testLoginInvalidEmail
   - SC ID: SC-LOGIN-002
   - Fail Type: ASSERTION_FAIL
   - Error: AssertionError: expected "Email không hợp lệ" but was "Invalid email"
   - Stack trace (nếu có)

2. Source MEMORY §13 → TC mapping:
   - TC ID: TC-LOGIN-002
   - Steps Mapped: 3/3
   - Expected Mapped: 3/3

3. TC-MASTER → TC-LOGIN-002:
   - Expected 3: "Hiển thị text 'Email không hợp lệ' bên dưới field Email"
```

### Step 2: Đọc source code
```bash
cat 10_source-code/[repo]/src/test/java/.../LoginTest.java
```
Tìm method `testLoginInvalidEmail` → đọc assertion code + data.

### Step 3: Phân tích theo fail type

**ASSERTION_FAIL analysis:**
```
TC expected: "Email không hợp lệ" (tiếng Việt)
Code assertion: assertEquals(getText(), "Email không hợp lệ")
App actual: "Invalid email" (tiếng Anh)

Root cause options:
  (a) App bug: text hiển thị sai ngôn ngữ → BUG
  (b) TC sai: expected đã thay đổi, TC chưa update → UPDATE TC
  (c) Env issue: locale setting sai trên STG → ENV CONFIG
  (d) Code bug: assertion so sánh sai → FIX CODE
```

**LOCATOR_STALE analysis:**
```
Locator: @FindBy(id = "email-error")
Error: NoSuchElementException

Root cause options:
  (a) Element đổi id: inspect page → tìm id mới → UPDATE LOCATOR
  (b) Element bị remove: feature thay đổi → BLOCK TC
  (c) Page chưa load: timing issue → ADD WAIT
  (d) Redirect: URL thay đổi → CHECK NAVIGATION
```

**ENV_ERROR analysis:**
```
Error: ConnectionRefusedException / TimeoutException

Root cause options:
  (a) Server down → CHECK ENV STATUS
  (b) Network issue → RETRY
  (c) Config sai (URL/port) → CHECK MEMORY §3 config
```

### Step 4: Present diagnosis

```
🔍 Diagnosis — FAIL-001

| Field | Value |
|-------|-------|
| Fail ID | FAIL-001 |
| Type | ASSERTION_FAIL |
| Method | LoginTest.testLoginInvalidEmail |
| TC | TC-LOGIN-002 |
| SC | SC-LOGIN-002 |

## Error
Expected: "Email không hợp lệ"
Actual: "Invalid email"

## Analysis
App trả về text tiếng Anh thay vì tiếng Việt.

## Possible Root Causes
  (a) 🐛 App bug — locale chưa set cho STG → /log-bug
  (b) 📝 TC sai — expected cũ, app đã đổi → /analyze-requirements --update
  (c) 🔧 Env config — locale setting STG → check 07_environments/

## Recommended Action
  → /log-bug (most likely app bug — ASSERTION_FAIL pattern)
  → Verify: mở app trên STG, check ngôn ngữ hiển thị
```

### Constraints
- KHÔNG sửa code
- KHÔNG sửa TC
- KHÔNG auto-log bug — chỉ suggest
