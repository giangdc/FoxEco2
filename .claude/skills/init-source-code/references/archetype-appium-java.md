# Archetype: Appium Java (mobile native)

> **Archetype ID:** `appium-java`
> **Status:** ⚠️ Manual scaffold (auto-scaffold script deferred — existing GitLab archetype pattern preserved)
> **Use case:** Native mobile automation (iOS + Android) với Appium 3.x + Java/Maven/TestNG
> **Pipeline downstream:** Default Java references (no language variant needed)

## Stack specs

| Component | Value | Version |
|---|---|---|
| Language | Java | 21 |
| Framework | Appium | 3.x |
| Test Runner | TestNG | 7.x |
| Build Tool | Maven | 3.9+ |
| Package Mgr | Maven Central | — |
| Locator API | `@AndroidFindBy` + `@iOSXCUITFindBy` PageFactory | — |
| Async pattern | Synchronous Appium client | — |
| Mobile driver | UiAutomator2 (Android) + XCUITest (iOS) | — |
| Local server | Appium server `:4723` | 3.4.2+ |
| Core dependency | `<org>:<core-mobile-automation>:1.0.0-SNAPSHOT` (team library) | — |

## Folder structure (target)

```
10_source-code/
├── pom.xml                                 (Maven config + Appium deps)
├── README.md                               (project specific, mobile env setup)
├── MEMORY.md                               (§1-§19 mobile-flavored)
├── .gitignore                              (target/, .idea/, *.iml, *.apk locally)
├── src/
│   ├── main/
│   │   ├── java/<org>/<project>/
│   │   │   ├── screen/                     (Page Objects — "Screen" thay vì "Page" cho mobile)
│   │   │   │   ├── BaseScreen.java
│   │   │   │   ├── LoginScreen.java
│   │   │   │   └── ShellScreen.java
│   │   │   └── util/
│   │   │       └── DriverManager.java     (inherits từ core lib)
│   │   └── resources/
│   │       └── device/
│   │           ├── local_android_device_info.json   (appPackage, appActivity, udid, ...)
│   │           └── local_ios_device_info.json
│   └── test/
│       ├── java/<org>/<project>/
│       │   ├── testcase/
│       │   │   ├── AppBaseTest.java       (Mobile base với beforeMethodHook auto-login etc.)
│       │   │   └── SampleTest.java
│       │   └── data/
│       │       └── TestData.java
│       └── resources/
│           └── testng.xml
└── testSuites/                             (TestNG XML filters)
    ├── smoke.xml                           (mobile-specific suite)
    └── regression.xml
```

## File specifications

### `pom.xml` (mobile-specific deps)

```xml
<dependencies>
    <!-- Core mobile library -->
    <dependency>
        <groupId>net.your-org</groupId>
        <artifactId>core-mobile-automation</artifactId>
        <version>1.0.0-SNAPSHOT</version>
    </dependency>

    <!-- Appium Java client -->
    <dependency>
        <groupId>io.appium</groupId>
        <artifactId>java-client</artifactId>
        <version>9.x</version>
    </dependency>

    <!-- Selenium (transitive — required by Appium) -->
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
</dependencies>
```

### `local_android_device_info.json` (device config)

```json
{
  "platformName": "Android",
  "appium:automationName": "UiAutomator2",
  "appium:deviceName": "<emulator-id or device UDID>",
  "appium:udid": "<emulator-id>",
  "appium:appPackage": "com.example.myapp",
  "appium:appActivity": "com.example.myapp.MainActivity",
  "appium:noReset": false,
  "appium:fullReset": false,
  "appium:newCommandTimeout": 300
}
```

Get values qua:
- `appPackage` + `appActivity`: `aapt dump badging path/to/app.apk | grep package`
- `udid` / `deviceName`: `adb devices`

### Conventions (mobile Page Object)

```java
public class LoginScreen extends BaseScreen {

    @AndroidFindBy(accessibility = "email-input")
    @iOSXCUITFindBy(accessibility = "email-input")
    private WebElement textBoxEmail;

    @AndroidFindBy(accessibility = "password-input")
    @iOSXCUITFindBy(accessibility = "password-input")
    private WebElement textBoxPassword;

    @AndroidFindBy(accessibility = "submit-button")
    @iOSXCUITFindBy(accessibility = "submit-button")
    private WebElement buttonSubmit;

    public LoginScreen(AppiumDriver driver) {
        super(driver);
    }

    public void enterEmail(String email) {
        textBoxEmail.clear();
        textBoxEmail.sendKeys(email);
    }

    public void clickSubmit() {
        buttonSubmit.click();
    }
}
```

### Test class với mobile fixture

```java
public class LoginTest extends AppBaseTest {

    @Test(priority = 1, description = "TC-LOGIN-001: SSO login happy path / SC-LOGIN-001")
    public void testLoginSuccess() {
        LoginScreen loginScreen = injector.getInstance(LoginScreen.class);
        // (Note: Guice DI via injector — pattern từ core-mobile-automation library)

        loginScreen.enterEmail(System.getenv("TEST_USERNAME"));
        loginScreen.enterPassword(System.getenv("TEST_PASSWORD"));
        loginScreen.clickSubmit();

        ShellScreen shell = injector.getInstance(ShellScreen.class);
        assertTrue(shell.isBottomNavVisible(), "Expected: bottom nav after login");
    }
}
```

## Locator strategy priority (mobile)

| Priority | Strategy | Why |
|---|---|---|
| 1 | `accessibility id` | Cross-platform (Android `content-desc` / iOS `accessibilityIdentifier`), stable |
| 2 | `id` | Android resource id, fast |
| 3 | `xpath` | Last resort — verbose, fragile to UI changes |
| 4 | `uiautomator` (Android) | Power user, multi-line content-desc, descendant queries |

## Naming conventions

| Artifact | Pattern | Example |
|---|---|---|
| Screen class | `<Name>Screen.java` | `LoginScreen.java`, `ShellScreen.java` |
| Test class | `<Name>Test.java` | `LoginTest.java`, `ShellNavigationTest.java` |
| Element field | descriptive camelCase | `buttonSubmit`, `textBoxEmail`, `tabSales` |
| Action method | `tap<Target>()`, `enter<Target>()`, `get<Target>Text()` | `tapSubmit()`, `enterEmail()`, `getDashboardText()` |
| Test description | `"TC-<MODULE>-<NNN>: <title> / SC-<MODULE>-<NNN>"` | (same Java pattern) |

## Manual scaffold (current state)

1. **Clone team GitLab archetype:**
   ```bash
   cd 10_source-code/
   git clone <team-gitlab-url>/<mobile-archetype-repo> .
   rm -rf .git
   ```

2. **Adjust pom.xml** (groupId, artifactId, core lib version)

3. **Configure device info:**
   - Edit `src/main/resources/device/local_android_device_info.json` với app's `appPackage`, `appActivity`, device `udid`
   - Cho iOS, edit `local_ios_device_info.json` với `bundleId`, simulator UDID

4. **Setup Appium server:**
   ```bash
   appium server -p 4723
   # Verify connection in another terminal:
   curl http://localhost:4723/status
   ```

5. **Setup emulator/device:**
   - Android: `emulator -list-avds` + start AVD
   - iOS: `xcrun simctl list devices`

6. **Populate MEMORY.md §2 Tech Stack manually** (structured format)

## Source MEMORY §2 Tech Stack (structured)

```markdown
## 2. Tech Stack

| Component    | Value                       | Version |
|--------------|-----------------------------|---------|
| Language     | Java                        | 21      |
| Framework    | Appium                      | 3.4.2   |
| Test Runner  | TestNG                      | 7.10.2  |
| Build Tool   | Maven                       | 3.9     |
| Package Mgr  | Maven Central               | —       |
| Locator API  | @AndroidFindBy + @iOSXCUITFindBy | —  |
| Async pattern| Synchronous Appium client   | —       |
| Mobile target| Android UiAutomator2 + iOS XCUITest | — |
| App platform | <native iOS/Android app name>| —      |
| Core library | core-mobile-automation      | 1.0.0-SNAPSHOT |
```

**CRITICAL:** Đặt `Language = Java` để downstream skills route đúng.

## Pipeline downstream behavior

Stack detected = Java → downstream skills load existing references (no variant needed). Same với Selenium Java — Appium chỉ khác library, framework JVM-side và file extensions/patterns không đổi.

## Future enhancement

Auto-scaffold script `scripts/scaffold-appium-java.py` deferred. Mobile setup phức tạp hơn web (emulator setup, signing, device configs) — manual workflow tốt hơn cho lần đầu, scaffold cho repeating pattern.

## See Also

- [archetypes.md](archetypes.md) — Full registry
- [archetype-selenium-java.md](archetype-selenium-java.md) — Web variant của same Java stack
- [archetype-playwright-ts.md](archetype-playwright-ts.md) — Web alternative (TypeScript, modern)
