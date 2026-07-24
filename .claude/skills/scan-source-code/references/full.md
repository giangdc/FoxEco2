# Scan Source Code — Mode FULL

> `/scan-source-code`
> Khi nào: MEMORY.md chưa tồn tại, hoặc cần scan lại từ đầu.

## Output: `10_source-code/MEMORY.md` (§1-§17 — Java stack; bao gồm §17 SRC-TC Review do review-src-tc ghi. TS stack dùng numbering riêng §1-§19, xem `full-typescript.md`)

## Workflow

### Step 1: Đọc CLAUDE.md
Project info, automation framework info, naming conventions.
Ghi §8 = IN_PROGRESS.

### Step 2: Scan project structure
```bash
find 10_source-code/ -type f -name "*.java" -o -name "*.xml" -o -name "*.properties" -o -name "*.yml" -o -name "*.yaml" -o -name "*.json" -o -name "*.gradle" | head -100

# Detect build tool
ls 10_source-code/pom.xml 2>/dev/null && echo "Maven"
ls 10_source-code/build.gradle 2>/dev/null && echo "Gradle"

# Count files
find 10_source-code/ -name "*.java" | wc -l
```

→ Ghi vào MEMORY §1 Project Structure (tree + file statistics).

### Step 3: Analyze dependencies & config

**3a. Build file (pom.xml / build.gradle):**

| Dependency | Cần extract | Ghi vào MEMORY |
|-----------|-------------|----------------|
| Selenium | Version (3.x vs 4.x) | API differences: RemoteWebDriver vs ChromeDriver |
| TestNG | Version | Test framework annotations |
| JUnit | Version (4 vs 5) | Nếu dùng thay TestNG |
| WebDriverManager | Có/không | Auto driver management |
| ExtentReports / Allure | Có/không | Reporting framework |
| Log4j / SLF4J | Có/không | Logging |
| Apache POI | Có/không | Excel data-driven |
| RestAssured | Có/không | API testing |
| Cucumber | Có/không | BDD — thay đổi cách viết test |

→ MEMORY §2 Tech Stack + §3 Configuration.

**3b. Config files:**
```bash
cat 10_source-code/src/main/resources/configs.properties 2>/dev/null
```
Extract: base URL, browser, headless, grid URL, timeouts, test accounts.
→ MEMORY §3a Environment Config.

**3c. TestNG/JUnit config:**
```bash
find 10_source-code/ -name "testng*.xml" -exec cat {} \;
```
→ MEMORY §3b TestNG Suite Config.

### Step 4: Analyze Base Classes ★ QUAN TRỌNG NHẤT

**4a. BaseTest:**
```bash
find 10_source-code/ -name "*Base*Test*" -o -name "*Test*Base*" | head -5
cat [path]
```

Extract — ĐỌC RẤT KỸ:

| Cần extract | Tại sao | Ví dụ |
|-------------|---------|-------|
| WebDriver init | Driver type | `new RemoteWebDriver(gridUrl, options)` |
| Setup/Teardown | Lifecycle | `@BeforeClass: init driver` |
| Page access pattern | ★ Pattern implement-automation PHẢI follow | `loginPage()` returns `new LoginPage(driver)` |
| Driver options | Chrome options | `options.addArguments("--headless")` |
| Config loading | Cách đọc config | `Properties.load()` |
| Soft/Hard assert | Assert pattern | `Assert.assertEquals()` vs `SoftAssert` |

**Page access patterns (ghi nhận CHÍNH XÁC):**
```java
// Pattern A: Method mới mỗi lần
protected LoginPage loginPage() { return new LoginPage(driver); }

// Pattern B: Lazy init
private LoginPage loginPage;
protected LoginPage loginPage() { if (loginPage == null) loginPage = new LoginPage(driver); return loginPage; }

// Pattern C: Init all in @BeforeClass
@BeforeClass void initPages() { loginPage = new LoginPage(driver); }
```

→ MEMORY §4a BaseTest (code snippets CHÍNH XÁC).

**4b. BasePage:** Constructor, common methods (wait, scroll, isDisplayed, getText).
→ MEMORY §4b BasePage.

### Step 5: Analyze Page Classes

```bash
find 10_source-code/ -path "*/page*" -name "*.java" -not -name "*Base*" | sort
```

Mỗi Page class extract:
- Class name, file path, package, extends
- Elements: `@FindBy` declarations (name, strategy, value)
- Methods: public/protected (name, return, params, description)

**Naming convention analysis — frequency count:**
```
button[Name]  → 15 lần ✅
btn[Name]     → 2 lần  ⚠️ Inconsistent
textBox[Name] → 10 lần ✅
input[Name]   → 1 lần  ⚠️
```

→ MEMORY §5 Conventions + §6 Page Registry.

### Step 6: Analyze Test Classes

```bash
find 10_source-code/ -path "*/test*" -name "*Test.java" -not -name "*Base*" | sort
```

Mỗi Test class extract:
- Class name, extends, annotations
- Test methods: name, `@Test` params, priority, groups, description
- Data providers (nếu có)
- Coverage mapping: SC ID → test method

→ MEMORY §7 Test Registry.

### Step 7: Generate MEMORY.md

Tổng hợp §1-§11 vào `10_source-code/MEMORY.md`.
§12-§17 để placeholder (populated by implement-automation, execute-maintain, review-src-tc §17). (Java stack; TS numbering khác — xem full-typescript.md)

Append CLAUDE.md:
```markdown
## Source Code Analysis
- **Framework:** [Java XX + Selenium X + TestNG X]
- **Page classes:** [N] | Test classes: [N] | Methods: [N]
- **Coverage:** [N]/[Total] scenarios ([%])
- **Conventions:** [type][Name] / [action][Target] / test[Feature][Case]
```

Ghi §8 = COMPLETED.

## Edge Cases

### Source code rỗng
```
⚠️ Folder 10_source-code/ chưa có source code.
(a) Tạo project skeleton (BaseTest, BasePage, pom.xml)?
(b) Copy source code vào rồi scan lại?
(c) Tạo MEMORY rỗng cho implement-automation tạo từ scratch?
```

### Non-Java source
```
⚠️ Phát hiện [Python/JS/...], không phải Java.
MEMORY vẫn tạo nhưng conventions khác. Framework: [pytest/Playwright/Cypress]
```

### >100 files
Hỏi: "Source code có [N] files. Scan toàn bộ hay focus modules cụ thể?"
Ưu tiên: Base classes → Page classes → Test classes → Utilities.

## Quy tắc

- **KHÔNG đoán convention** — chỉ ghi pattern thực sự từ code
- **KHÔNG sửa code** — issue → ghi §11, không fix
- **KHÔNG ghi password/secret** plaintext → `[REDACTED]`
- Luôn có timestamp `Cập nhật lần cuối` ở header

## Checklist
- [ ] Tất cả .java files đã đọc
- [ ] pom.xml/build.gradle extracted
- [ ] Config files extracted
- [ ] BaseTest analysis đầy đủ (lifecycle, page access pattern)
- [ ] Page classes indexed (elements + methods)
- [ ] Test classes indexed (methods + coverage)
- [ ] Naming conventions extracted + frequency count
- [ ] Coverage gap analysis (nếu có Version MEMORY)
- [ ] MEMORY.md tạo tại 10_source-code/MEMORY.md
- [ ] CLAUDE.md append
- [ ] Không có password plaintext
- [ ] §8 = COMPLETED
