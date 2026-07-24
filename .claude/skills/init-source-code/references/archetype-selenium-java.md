# Archetype: Selenium Java (web)

> **Archetype ID:** `selenium-java`
> **Status:** ⚠️ Manual scaffold (auto-scaffold script deferred — existing GitLab archetype pattern preserved)
> **Use case:** Enterprise web automation với Java/Maven/TestNG stack
> **Pipeline downstream:** Default Java references (no language variant needed)

## Stack specs

| Component | Value | Version |
|---|---|---|
| Language | Java | 21 |
| Framework | Selenium | 4.x |
| Test Runner | TestNG | 7.x |
| Build Tool | Maven | 3.9+ |
| Package Mgr | Maven Central | — |
| Locator API | `@FindBy` + `PageFactory` + By.id/css/xpath | — |
| Async pattern | Synchronous WebDriver | — |
| Report | ExtentReports / Allure | — |
| Browser driver | WebDriverManager (auto-download) | — |
| Core dependency | `<org>:<core-mobile-automation>:1.0.0-SNAPSHOT` (team library) | — |

## Folder structure (target sau scaffold)

```
10_source-code/
├── pom.xml                                 (Maven config + deps)
├── README.md                               (project specific)
├── MEMORY.md                               (§1-§19 Java-flavored)
├── .gitignore                              (target/, .idea/, *.iml)
├── src/
│   ├── main/
│   │   ├── java/<org>/<project>/
│   │   │   ├── screen/ hoặc page/         (Page Objects)
│   │   │   │   └── BasePage.java
│   │   │   └── util/
│   │   │       └── DriverManager.java     (optional, có thể inherit từ core lib)
│   │   └── resources/
│   │       └── env/
│   │           ├── local.properties
│   │           └── stg.properties
│   └── test/
│       ├── java/<org>/<project>/
│       │   ├── testcase/                  (Test classes)
│       │   │   ├── AppBaseTest.java
│       │   │   └── SampleTest.java
│       │   └── data/
│       │       └── TestData.java
│       └── resources/
│           ├── testng.xml
│           └── local_android_device_info.json (nếu mobile)
└── testSuites/                             (TestNG XML suite filters)
    ├── smoke.xml
    └── regression.xml
```

## File specifications

### `pom.xml` (essentials)

```xml
<dependencies>
    <!-- Core library (per-team Nexus) -->
    <dependency>
        <groupId>net.your-org</groupId>
        <artifactId>core-mobile-automation</artifactId>
        <version>1.0.0-SNAPSHOT</version>
    </dependency>

    <!-- Selenium -->
    <dependency>
        <groupId>org.seleniumhq.selenium</groupId>
        <artifactId>selenium-java</artifactId>
        <version>4.x</version>
    </dependency>

    <!-- TestNG -->
    <dependency>
        <groupId>org.testng</groupId>
        <artifactId>testng</artifactId>
        <version>7.10.2</version>
    </dependency>

    <!-- WebDriverManager -->
    <dependency>
        <groupId>io.github.bonigarcia</groupId>
        <artifactId>webdrivermanager</artifactId>
        <version>5.x</version>
    </dependency>

    <!-- Reports -->
    <dependency>
        <groupId>com.aventstack</groupId>
        <artifactId>extentreports</artifactId>
        <version>5.x</version>
    </dependency>
</dependencies>
```

### Conventions (per Page Object pattern)

```java
public class LoginPage extends BasePage {
    @FindBy(id = "email")
    private WebElement textBoxEmail;

    @FindBy(id = "password")
    private WebElement textBoxPassword;

    @FindBy(css = "button[type='submit']")
    private WebElement buttonSubmit;

    public LoginPage(WebDriver driver) {
        super(driver);
        PageFactory.initElements(driver, this);
    }

    public void enterEmail(String email) {
        textBoxEmail.clear();
        textBoxEmail.sendKeys(email);
    }

    public void enterPassword(String password) {
        textBoxPassword.clear();
        textBoxPassword.sendKeys(password);
    }

    public void clickSubmit() {
        buttonSubmit.click();
    }
}
```

### Test class pattern (TestNG)

```java
public class LoginTest extends AppBaseTest {

    @Test(priority = 1, description = "TC-LOGIN-001: User authentication happy path / SC-LOGIN-001")
    public void testLoginSuccess() {
        // Step 1: Navigate
        driver.get(env.getString("baseUrl") + "/login");

        // Step 2: Enter credentials
        LoginPage loginPage = new LoginPage(driver);
        loginPage.enterEmail(System.getenv("TEST_USERNAME"));
        loginPage.enterPassword(System.getenv("TEST_PASSWORD"));

        // Step 3: Submit
        loginPage.clickSubmit();

        // Expected: Dashboard visible
        assertTrue(driver.findElement(By.id("dashboard")).isDisplayed());
    }
}
```

## Naming conventions

| Artifact | Pattern | Example |
|---|---|---|
| Page class | `<Name>Page.java` | `LoginPage.java` |
| Test class | `<Name>Test.java` | `LoginTest.java` |
| Base class | `AppBaseTest.java` | `AppBaseTest extends BaseTest` |
| Element field | descriptive camelCase | `buttonSubmit`, `textBoxEmail`, `linkForgotPassword` |
| Action method | `verb<Target>()` | `clickSubmit()`, `enterEmail(String)`, `getDashboardText()` |
| Test method | `test<Feature><Action>()` | `testLoginSuccess()`, `testLoginInvalidEmail()` |
| TestNG description | `"TC-<MODULE>-<NNN>: <title> / SC-<MODULE>-<NNN>"` | `"TC-LOGIN-001: Happy path / SC-LOGIN-001"` |

## Manual scaffold (current state)

Vì auto-scaffold cho Java archetype chưa implement (deferred), user phải:

1. **Clone team GitLab archetype:**
   ```bash
   cd 10_source-code/
   git clone <team-gitlab-url>/<archetype-repo> .
   # Clean .git history
   rm -rf .git
   ```

2. **Adjust pom.xml:**
   - Update `<groupId>`, `<artifactId>`, `<version>` cho project mới
   - Verify `core-mobile-automation` dependency version match

3. **Update package structure:**
   - Rename `src/main/java/<org>/<project>/` theo project naming
   - Same cho `src/test/java/`

4. **Configure environment:**
   - Edit `src/main/resources/env/stg.properties` với base URL
   - Create `local_android_device_info.json` nếu mobile (xem appium-java archetype)

5. **Populate MEMORY.md §2 Tech Stack manually** (structured format — xem pattern dưới)

## Source MEMORY §2 Tech Stack (structured)

Manually populate sau khi scaffold:

```markdown
## 2. Tech Stack

| Component    | Value                  | Version |
|--------------|------------------------|---------|
| Language     | Java                   | 21      |
| Framework    | Selenium               | 4.x     |
| Test Runner  | TestNG                 | 7.10.2  |
| Build Tool   | Maven                  | 3.9     |
| Package Mgr  | Maven Central          | —       |
| Locator API  | @FindBy PageFactory    | —       |
| Async pattern| Synchronous WebDriver  | —       |
| Core library | core-mobile-automation | 1.0.0-SNAPSHOT |
```

**CRITICAL:** Đặt `Language = Java` để downstream skills route đúng (Java references default).

## Pipeline downstream behavior

Stack detected = Java → downstream skills load existing references (no variant needed):
- `scan-source-code/references/full.md` (Java patterns — existing)
- `implement-automation/references/implement.md` (Java POM templates — existing)
- `execute-maintain/references/run.md` (mvn test — existing)
- `review-src-tc/references/full.md` (Java .java + @Test parsing — existing)

## Future enhancement

Auto-scaffold script `scripts/scaffold-selenium-java.py` có thể implement để remove manual clone step. Pattern tương tự `scaffold-playwright-ts.py`. Deferred — current manual workflow đã proven trên production projects.

## See Also

- [archetypes.md](archetypes.md) — Full registry + comparison matrix
- [archetype-playwright-ts.md](archetype-playwright-ts.md) — Modern web alternative (auto-scaffold)
- [archetype-appium-java.md](archetype-appium-java.md) — Mobile variant của same Java stack
