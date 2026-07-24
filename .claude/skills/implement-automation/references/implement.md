# Implement Automation — Mode IMPLEMENT

> `/implement-automation --module Login` | `/implement-automation --tc TC_01.1,TC_01.5`
> Chuyển TC-MASTER Excel → Java Selenium code (Page Object + Test class).

## Input

```
1. CLAUDE.md (root)                              → project info, env URL
2. 02_analyze-requirements/Project_rule.md       → coding rules (§5)
3. 10_source-code/MEMORY.md                      → ★ conventions, page registry
4. 03_test-cases/[version]/TC-MASTER-v[version].xlsx  → ★★ SOURCE OF TRUTH cho code
                                                     (alias của file ISC chính thức — xem
                                                     generate-tc/references/consolidate.md.
                                                     42 cột A-AP, 1 sheet "Test Cases"/"Test Case N"
                                                     riêng cho mỗi module — --module chọn đúng sheet
                                                     theo C3 "Tên chức năng" hoặc tên tab)
5. 08_test-runs/vibe/vibe-locators-latest.md     → ★ locators đã verified (nếu có)
6. 02_analyze-requirements/[version]/MEMORY.md   → supplementary context
```

## Output

```
10_source-code/[repo]/src/main/java/[pkg]/page/[Name]Page.java    ← Page Object (new/update)
10_source-code/[repo]/src/test/java/[pkg]/testcase/[Module]Test.java  ← Test class (new/update)
10_source-code/MEMORY.md §6, §7, §12, §13                        ← Registry updates
```

---

## Workflow

### Step 1: Đọc context + guard

```
1. PIPELINE.md → check:
   - scan-source-code ≥ COMPLETED (Source MEMORY phải có)
   - generate-tc ≥ PARTIAL (TC-MASTER phải có)
2. MASTER-MEMORY §8:
   - vibe-test status? Nếu COMPLETED → đọc vibe-locators-latest.md
   - Nếu NOT_STARTED → ⚠️ "Recommend /vibe-test trước để validate TC + capture locators"
3. Đọc Source MEMORY:
   - §4a BaseTest → lifecycle, driver init, page access pattern
   - §4b BasePage → constructor, common methods
   - §5 Conventions → element naming, method naming, locator style
   - §6 Page Registry → pages đã tồn tại (KHÔNG recreate)
   - §7 Test Registry → test methods đã tồn tại
4. Ghi §8 implement-automation = IN_PROGRESS
```

### Step 2: Parse TC-MASTER Excel

Đọc đúng sheet module (`openpyxl`, `data_only=True` để lấy giá trị đã resolve của cột A/AM/AN/AO — formula, KHÔNG gõ tay). Cột thật theo template ISC (xem `generate-tc/references/generate.md` §"TC Structure — 42 cột"):

| Field parse | Cột Excel | Ghi chú |
|---|---|---|
| tc_id | A (formula) | `[Mã CN].[STT]` — vd `TC_01.2`. KHÔNG có ý nghĩa semantic (không phải `TC-LOGIN-002`), chỉ là số thứ tự trong sheet |
| req_id | B | có thể nhiều giá trị, phân cách dấu phẩy |
| doc_source | C | |
| group | D | `Functional`/`UI`/`Integration`/`Database Test Case` (KHÔNG còn `Validation`/`Business Rule` như enum cũ) |
| priority | E | `High`/`Medium`/`Low` (KHÔNG còn hậu tố P1/P2/P3 trong cell) |
| title | F | |
| precondition | G | |
| steps | H | Tiếng Việt, đánh số — **test data nằm inline trong text, không có cột riêng** |
| expected | I | 1:1 với steps |
| origin | J | `AI`/`QC` |
| review | K | `Pending`/`Reviewed`/`N/A` |
| automated | L | `Yes`/`No` — implement-automation ghi lại `Yes` sau khi implement xong (Step 8) |
| script | M | Path script — implement-automation ghi path file vừa tạo vào đây (Step 8) |
| remark | AP | Có thể chứa `Technique: <tag>` (comprehensive/selective mode), `Carried từ v[X]`, hoặc ghi chú khác nối bằng ` \| ` |

```python
# Parse mỗi TC row thành structured data:
tc = {
    "tc_id": "TC_01.2",              # cột A, đã resolve — KHÔNG tự đặt/đoán
    "req_id": "REQ-02",              # cột B — có thể là "REQ-02, REQ-03"
    "doc_source": "DOC-v2.0-01",     # cột C
    "group": "Functional",           # cột D
    "priority": "High",              # cột E
    "title": "Email sai format",     # cột F
    "precondition": "Đang ở trang Login",  # cột G
    "steps": [
        {"num": 1, "text": "Nhập \"user@\" vào field Email"},
        {"num": 2, "text": "Nhập \"Test@123\" vào field Password"},
        {"num": 3, "text": "Nhấn button Đăng nhập"}
    ],                                # cột H — test data đã nằm sẵn trong text (vd "user@", "Test@123")
    "expected": [
        {"num": 1, "text": "Field Email hiển thị viền đỏ"},
        {"num": 2, "text": "Field Password giữ nguyên giá trị \"Test@123\""},
        {"num": 3, "text": "Hiển thị text \"Email không hợp lệ\" bên dưới field Email"}
    ],                                # cột I
    "origin": "AI",                  # cột J
    "remark": "",                    # cột AP — parse "Technique: <tag>" nếu có
}
```

> **Đã bỏ so với schema 16-cột cũ:** không còn `scenario_id` (không có cột riêng — nếu cần, resolve qua Version MEMORY §9 mapping, KHÔNG bịa), không còn `test_data` tách riêng (giá trị đã nằm trong `steps`/`expected` text — parse literal value trực tiếp từ đó khi cần, vd cho `@DataProvider`), không còn `lifecycle`/`version` field trong Excel (lifecycle NEW/CARRIED/MODIFIED chỉ có trong Version MEMORY §4, không map trực tiếp vào code).

**Filter theo scope:**
- `--module Login` → chọn đúng sheet TC (match `C3` Tên chức năng, hoặc tên tab nếu không khớp — xem sheet `Dashboard` cột D để đối chiếu)
- `--tc TC_01.1,TC_01.5` → chỉ TCs có giá trị cột A (đã resolve) khớp danh sách chỉ định

**Nếu có vibe-report → filter thêm:**
- TC PASS trong vibe-report → implement
- TC BLOCKED → skip + log: `"[tc_id] BLOCKED trong vibe-test, skip."`
- TC FAIL → warn: `"[tc_id] FAIL trong vibe-test, implement nhưng có thể cần sửa."`

**Quy tắc ưu tiên:**
- TC Excel **luôn thắng** khi conflict với scenario
- Nếu TC nói `Email: user@` → code dùng `"user@"`, không dùng giá trị khác
- Nếu TC có 3 steps → code có 3 groups of action lines
- Nếu TC có 3 expected → code có 3 assertions

### Step 3: Lấy Locator

**3 nguồn locator theo priority:**

```
Kiểm tra: 08_test-runs/vibe/vibe-locators-latest.md tồn tại?
├── CÓ → đọc locators đã verified
│   ├── Element có locator ✅ → dùng trực tiếp (KHÔNG mở Playwright)
│   ├── Element ❌ NOT FOUND → skip, ghi: // BLOCKED in vibe-test
│   └── Element không có trong vibe-locators → Playwright lấy mới (Step 3b)
│
├── KHÔNG CÓ → kiểm tra Source MEMORY §12 Locator Registry
│   ├── Locator tồn tại → dùng (nhưng có thể stale)
│   └── Không có → Playwright lấy mới (Step 3b)
│
└── Step 3b: Playwright MCP lấy locator mới
    browser_navigate(URL) → browser_snapshot() → extract elements
```

**Locator strategy priority (Project_rule.md §5.8):**

| Ưu tiên | Strategy | Khi nào | Code |
|---------|----------|---------|------|
| 1 | `id` | Element có id unique | `@FindBy(id = "email")` |
| 2 | `data-testid` / `data-qa` | Có test attribute | `@FindBy(css = "[data-testid='login-btn']")` |
| 3 | `name` | Form fields | `@FindBy(name = "email")` |
| 4 | `css` (class-based) | Stable CSS selector | `@FindBy(css = ".login-form .btn-primary")` |
| 5 | Text + role | Buttons, links | `@FindBy(xpath = "//button[text()='Đăng nhập']")` |
| 6 | `xpath` | Last resort | `@FindBy(xpath = "//div[@class='error']//span")` |

**TUYỆT ĐỐI KHÔNG dùng:**
- Index-dependent xpath (`div[3]/span[2]`) trừ khi không có cách khác
- Style-based locator
- Locator tự đoán không verify qua Playwright hoặc vibe-test

### Step 4: Generate / Update Page Object

Đọc MEMORY §4 (Base Classes) + §5 (Conventions) + §6 (Page Registry).

**Nếu Page class đã tồn tại** (MEMORY §6 có entry) → ADD elements + methods, KHÔNG recreate.
**Nếu Page class mới** → CREATE theo template:

```java
// File: [path từ MEMORY §1]/page/[Name]Page.java
package [package từ MEMORY §5e];

import org.openqa.selenium.*;
import org.openqa.selenium.support.FindBy;
import org.openqa.selenium.support.PageFactory;

public class LoginPage extends [BasePage từ MEMORY §4b] {

    // === Elements — naming: [type][Name] (MEMORY §5a) ===

    // Locator source: vibe-locators-latest.md (verified 2026-05-24)
    @FindBy(id = "email")
    private WebElement textBoxEmail;

    // Locator source: vibe-locators-latest.md (verified 2026-05-24)
    @FindBy(id = "password")
    private WebElement textBoxPassword;

    // Locator source: vibe-locators-latest.md (verified 2026-05-24)
    @FindBy(css = "[data-testid='login-btn']")
    private WebElement buttonLogin;

    // Locator source: Playwright live (vibe-locators không có element này)
    @FindBy(css = ".error-message.email")
    private WebElement labelEmailError;

    // === Constructor — pattern từ MEMORY §4b ===
    public LoginPage(WebDriver driver) {
        super(driver);
        PageFactory.initElements(driver, this);
    }

    // === Action methods — naming: [action][Target] (MEMORY §5b) ===

    public void enterEmail(String email) {
        textBoxEmail.clear();
        textBoxEmail.sendKeys(email);
    }

    public void enterPassword(String password) {
        textBoxPassword.clear();
        textBoxPassword.sendKeys(password);
    }

    public void clickLogin() {
        buttonLogin.click();
    }

    // === Composite method ===
    public void loginWith(String email, String password) {
        enterEmail(email);
        enterPassword(password);
        clickLogin();
    }

    // === Verification methods (cho TC expected results) ===

    public boolean isEmailErrorDisplayed() {
        try { return labelEmailError.isDisplayed(); }
        catch (NoSuchElementException e) { return false; }
    }

    public String getEmailErrorText() {
        return labelEmailError.getText();
    }

    public boolean isEmailFieldErrorHighlighted() {
        return textBoxEmail.getAttribute("class").contains("error");
    }
}
```

**Quy tắc Page Object:**
- TC step cần action mà Page chưa có method → TẠO method mới
- TC expected cần verify mà Page chưa có method → TẠO method mới
- Method naming theo MEMORY §5b conventions
- Element naming theo MEMORY §5a conventions
- Locator style theo MEMORY §5d (`@FindBy` PageFactory hoặc `By` constants)

### Step 5: Generate / Update Test Class

```java
// File: [path từ MEMORY §1]/testcase/[Module]Test.java
package [package từ MEMORY §5e];

import org.testng.annotations.*;
import static org.testng.Assert.*;

public class LoginTest extends [BaseTest từ MEMORY §4a] {

    // TC_01.2 / REQ-02: Email sai format
    @Test(priority = 1, description = "TC_01.2 / REQ-02: Email sai format")
    public void testLoginInvalidEmail() {
        // Pre-condition: Đang ở trang Login

        // Step 1: Nhập "user@" vào field Email
        loginPage().enterEmail("user@");

        // Step 2: Nhập "Test@123" vào field Password
        loginPage().enterPassword("Test@123");

        // Step 3: Nhấn button Đăng nhập
        loginPage().clickLogin();

        // Expected 1: Field Email hiển thị viền đỏ
        assertTrue(loginPage().isEmailFieldErrorHighlighted(),
            "Expected 1: Field Email phải hiển thị viền đỏ");

        // Expected 2: Field Password giữ nguyên giá trị "Test@123"
        assertEquals(loginPage().getPasswordFieldValue(), "Test@123",
            "Expected 2: Field Password phải giữ nguyên giá trị");

        // Expected 3: Hiển thị text "Email không hợp lệ" bên dưới field Email
        assertEquals(loginPage().getEmailErrorText(), "Email không hợp lệ",
            "Expected 3: Phải hiển thị text lỗi email");
    }
}
```

**Quy tắc bắt buộc (Project_rule.md §5):**

| Rule | Chi tiết |
|------|---------|
| Comment `// Step N:` | Trước MỖI group of action lines. Text copy từ TC **column H** (Test Steps). |
| Comment `// Expected N:` | Trước MỖI assertion. Text copy từ TC **column I** (Expected Result). |
| `@Test description` | Chứa TC ID + Req ID: `"TC_01.2 / REQ-02: ..."`. Template không còn Scenario ID column — nếu project có mapping SC↔TC ở Version MEMORY §9, có thể thêm `/ SC-xxx` optional cuối chuỗi, KHÔNG bắt buộc. |
| `priority` | `High`=1, `Medium`=2, `Low`=3 (map từ TC **column E** — giá trị cell không có hậu tố P1/P2/P3) |
| Test data | ĐÚNG giá trị **inline trong TC column H** (Test Steps) — template KHÔNG có cột Test Data riêng. Không tự bịa, không lấy từ cột nào khác. |
| Assertion message | Chứa `"Expected N: "` + mô tả từ TC **column I** |
| 1 method = 1 TC | Mỗi test method implement ĐÚNG 1 TC row |
| Manual verify | Nếu expected không thể automation → comment MANUAL VERIFY |

**Xử lý Expected không thể automation:**

```java
// Expected 3: Màu button = #1890FF — MANUAL VERIFY REQUIRED (visual check)
// TODO: Verify visually or use screenshot comparison tool
```

Ghi nhận vào MEMORY §13: `Manual Verify = 1`

### Step 6: Multi-page scenario handling

Khi TC navigate qua nhiều trang (ví dụ checkout flow):

```
1. Xác định pages: ProductPage → CartPage → CheckoutPage → OrderConfirmPage

2. Generate NHIỀU Page classes (hoặc update existing):
   - ProductPage.java: addToCart(), clickGoToCart()
   - CartPage.java: clickCheckout()
   - CheckoutPage.java: enterAddress(), selectPaymentCOD(), submitOrder()
   - OrderConfirmPage.java: isOrderSuccessDisplayed(), getOrderId()

3. Generate 1 Test method (end-to-end):

   @Test(description = "TC_05.1 / REQ-12: Checkout COD")
   public void testCheckoutCODSuccess() {
       // Step 1: Thêm sản phẩm vào giỏ
       productPage().clickAddToCart();
       // Step 2: Vào giỏ hàng
       productPage().clickGoToCart();
       // Step 3: Nhấn Checkout
       cartPage().clickCheckout();
       // Step 4: Nhập địa chỉ
       checkoutPage().enterAddress("123 Test St");
       // Step 5: Chọn thanh toán COD
       checkoutPage().selectPaymentCOD();
       // Step 6: Submit order
       checkoutPage().submitOrder();
       // Expected 1: Hiển thị "Đặt hàng thành công"
       assertTrue(orderConfirmPage().isOrderSuccessDisplayed());
   }

4. BaseTest cần thêm page accessors (nếu chưa có):
   → Thêm vào BaseTest theo pattern MEMORY §4a
```

### Step 7: Verify code compiles

```bash
cd 10_source-code/[repo] && mvn compile -q
```

Nếu compile fail → fix syntax errors trước khi tiếp.

### Step 8: Cập nhật MEMORY source-code

**§6 Page Registry:** Thêm/update rows cho page classes

| Class | File | Elements | Methods | Status |
|-------|------|----------|---------|--------|
| LoginPage | page/LoginPage.java | 4 | 6 | ✅ Updated |

**§7 Test Registry:** Thêm rows cho test methods (cột "SC ID" đổi thành "Req ID" — template ISC không còn Scenario ID column, Req ID mới là khóa truy vết thật có trong Excel)

| Class | Method | TC ID | Req ID | Priority | Status |
|-------|--------|-------|-------|----------|--------|
| LoginTest | testLoginInvalidEmail | TC_01.2 | REQ-02 | High | ✅ New |

**§12 Locator Registry:** Cập nhật locators + source

| Element | Strategy | Value | Source | Date |
|---------|----------|-------|--------|------|
| textBoxEmail | id | email | vibe-locators | 2026-05-24 |
| buttonLogin | css | [data-testid='btn-login'] | vibe-locators | 2026-05-24 |
| labelEmailError | css | .error-message.email | playwright-live | 2026-05-25 |

**§13 Implementation Log** (cột "SC ID" đổi thành "Req ID" — lý do như §7):

```markdown
## 13. Implementation Log

| TC ID | Req ID | Method | Steps Mapped | Expected Mapped | Manual Verify | Locator Source | Date |
|-------|-------|--------|-------------|-----------------|---------------|---------------|------|
| TC_01.2 | REQ-02 | testLoginInvalidEmail | 3/3 ✅ | 3/3 ✅ | 0 | vibe-locators | 2026-05-25 |
| TC_01.3 | REQ-03 | — | — | — | — | — | BLOCKED (vibe-test) |
```

**Đồng thời ghi ngược vào TC-MASTER Excel** (mới so với schema cũ — template ISC có cột Automated/Script dành riêng cho việc này, trước đây implement-automation không ghi lại Excel):
- Cột L (Automated) của TC vừa implement → đổi `No` → `Yes`
- Cột M (Script) → ghi path file test method vừa tạo (vd `src/test/java/.../LoginTest.java#testLoginInvalidEmail`)
- KHÔNG động vào cột A/AM/AN/AO (formula) hay cột N-AL (round data, thuộc execution scope)

### Step 9: Present + handoff

```
✅ Implement automation hoàn tất:

☕ Page classes: LoginPage.java (4 elements, 6 methods) — updated
🧪 Test methods: 3 new (testLoginInvalidEmail, testLoginEmptyFields, testLoginSuccess)
📝 Locator source: 3 từ vibe-locators ✅, 1 từ Playwright live
⚠️ Manual verify: 1 expected (visual check)
🚫 Skipped: TC_01.3 (BLOCKED in vibe-test)
📊 TC-MASTER: cột Automated/Script đã cập nhật cho 3 TC vừa implement

Next:
  /review-src-tc --module Login     ← verify code match TC
  /execute-maintain --run LoginTest          ← chạy test
```

Ghi §8 = PARTIAL (chưa hết TCs) hoặc COMPLETED.

---

## Edge Cases

### Comprehensive mode — DataProvider parameterization (2026-05-29)

Khi Version MEMORY §9 (TC Gen Log) Mode = `comprehensive` hoặc `selective`, derived TCs từ B1 EP, B2 BVA, B6 EG thường có pattern lặp lại (cùng Req ID, khác data — các TC này thường nằm liên tiếp trong cùng sheet vì derived TC sinh ngay sau baseline TC, nên ID thường là 1 dải liên tục vd `TC_03.14..TC_03.20`, nhưng KHÔNG được giả định điều này — luôn đọc đúng giá trị cột A đã resolve). Recommend `@DataProvider` để giảm code duplication:

**Anti-pattern (verbose 1:1):**
```java
@Test(description = "TC_03.14 / Technique: BVA-min-1")
public void testPasswordLength7() { /* len=7, expect=reject */ }

@Test(description = "TC_03.15 / Technique: BVA-min")
public void testPasswordLength8() { /* len=8, expect=accept */ }

// ... 5 more methods, all near-duplicate
```

**Recommended (1:N parameterized):**
```java
@DataProvider(name = "passwordBoundary")
public Object[][] passwordBoundaryData() {
    return new Object[][] {
        {7,  false, "TC_03.14", "BVA-min-1"},
        {8,  true,  "TC_03.15", "BVA-min"},
        {9,  true,  "TC_03.16", "BVA-min+1"},
        {31, true,  "TC_03.17", "BVA-max-1"},
        {32, true,  "TC_03.18", "BVA-max"},
        {33, false, "TC_03.19", "BVA-max+1"},
        {0,  false, "TC_03.20", "BVA-empty"},
    };
}

@Test(dataProvider = "passwordBoundary",
      description = "REQ-08 / BVA suite (TC_03.14..TC_03.20)")
public void testSsoLoginPasswordBoundary(int len, boolean expectedAccept,
                                          String tcId, String technique) {
    loginPage().enterPassword(generatePassword(len));
    loginPage().tapSubmit();
    if (expectedAccept) {
        assertTrue(mainScreen().isVisible(), 
                   tcId + " (" + technique + "): expected accept");
    } else {
        assertTrue(loginPage().hasError(), 
                   tcId + " (" + technique + "): expected reject");
    }
}
```

**Source MEMORY §13 Implementation Log entry:**
```
| 2026-05-29 | REQ-08 | TC_03.14..TC_03.20 | LoginTest.testSsoLoginPasswordBoundary | DataProvider 7 rows | BVA boundary |
```

**Decision rule:**

| Technique | Recommended pattern |
|---|---|
| B1 EP (Equivalence Partitioning) | DataProvider — each partition = 1 row |
| B2 BVA (Boundary Value) | DataProvider — 6-8 boundary points per field |
| B3 DT (Decision Table) | DataProvider — each truth-table rule = 1 row |
| B4 ST (State Transition) | Usually 1:1 (state transitions need different setup) |
| B5 PW (Pairwise) | DataProvider — pairs as rows |
| B6 EG (Error Guessing) | DataProvider — 10-pattern checklist per field |
| B7 CRUD Matrix | Sometimes 1:1 (CRUD ops differ) |
| B8 CEG | Usually 1:1 (cause-effect graphs differ) |

**Tradeoff:** DataProvider reduces LOC ~80% nhưng debug khó hơn (1 method fail trên N data rows → cần `Reporter.log(tcId)` để truy nguồn). Recommend DataProvider khi patterns đồng nhất, 1:1 khi setup khác nhau.

### Element not found trên UI
```
"Không thấy element [X] trên trang hiện tại.
 URL: [url]. Navigate đến trang khác? Hoặc cho URL cụ thể."
→ User cung cấp URL → browser_navigate → re-snapshot
```

### Multiple matching elements
```
"Tìm thấy 3 elements match 'button Submit':
  (a) <button id='submit-form'> text='Submit' — trong form chính
  (b) <button class='btn-submit'> text='Submit' — trong modal
  (c) <input type='submit'> value='Submit' — hidden form
Chọn element nào?"
```

### Page load chậm / Dynamic content
```
1. browser_navigate → URL
2. Chờ 3 giây (hoặc explicit wait pattern từ MEMORY §4)
3. browser_snapshot → kiểm tra content loaded
4. Loading spinner vẫn còn → chờ thêm + re-snapshot
5. Timeout 15s → cảnh báo user
```

### Authentication required
```
"Trang [URL] yêu cầu đăng nhập. Cần:
  (a) Credentials để login trước?
  (b) URL direct không cần auth?
  (c) Cookie/token inject?"
```

---

## Constraints

- **KHÔNG sáng tạo** step/expected ngoài TC-MASTER
- **KHÔNG auto-run** `mvn test` — đó là việc execute-maintain
- **KHÔNG modify** files ngoài: `page/`, `testcase/`, MEMORY files
- **KHÔNG tự tạo convention mới** — follow MEMORY §5
- **KHÔNG sửa BaseTest/BasePage** — chỉ THÊM page accessors nếu cần
- Locator chỉ có xpath → flag warning: `// FRAGILE: only xpath available`
- Muốn sửa conventions → redirect: `/scan-source-code --delta`

---

## Checklist

- [ ] Source MEMORY §4-§5 đã đọc (conventions, base classes)
- [ ] TC-MASTER parsed cho scope
- [ ] vibe-locators-latest.md đã đọc (nếu có)
- [ ] Locators verified (vibe/playwright/MEMORY)
- [ ] Page class tạo/update đúng conventions
- [ ] Test class tạo với `// Step N:` + `// Expected N:` comments (copy đúng từ cột H/I, không phải I/J)
- [ ] `@Test description` chứa TC ID (cột A) + Req ID (cột B)
- [ ] Test data ĐÚNG giá trị inline trong TC column H (Test Steps) — không có cột Test Data riêng
- [ ] MANUAL VERIFY ghi cho expected không thể automate
- [ ] TC-MASTER: cột Automated (L) + Script (M) đã ghi ngược cho TC vừa implement
- [ ] `mvn compile` thành công
- [ ] MEMORY §6, §7, §12, §13 cập nhật
- [ ] §8 = PARTIAL / COMPLETED
