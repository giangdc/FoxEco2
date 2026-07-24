# Archetype Registry

> Available archetypes cho `/init-source-code --archetype <name>`. Mỗi archetype có dedicated reference file + (optional) scaffold script.

## Current archetypes (v4.1, 2026-05-31)

| Archetype ID | Stack | Use case | Effort manual | Auto-scaffold | Reference |
|---|---|---|---|---|---|
| `playwright-ts` | TypeScript 5.x + Playwright 1.x + Playwright Test | Web automation modern, parallel-friendly, headless-first | N/A (NEW 2026-05-31) | ✅ Yes — `scripts/scaffold-playwright-ts.py` | [archetype-playwright-ts.md](archetype-playwright-ts.md) |
| `selenium-java` | Java 21 + Selenium 4 + TestNG 7 + Maven 3.9 | Web automation enterprise, mature ecosystem | Manual (clone GitLab archetype) | ⚠️ Partial — manual instructions | [archetype-selenium-java.md](archetype-selenium-java.md) |
| `appium-java` | Java 21 + Appium 3.x + TestNG 7 + Maven | Native mobile (iOS/Android) automation | Manual (clone GitLab archetype) | ⚠️ Partial — manual instructions | [archetype-appium-java.md](archetype-appium-java.md) |

## Choosing the right archetype

| Question | Recommendation |
|---|---|
| App là web hay mobile? | Web → `playwright-ts` (modern) hoặc `selenium-java` (enterprise) · Mobile → `appium-java` |
| Team có quen Java/Maven sẵn? | YES + enterprise constraints → `selenium-java` · NO hoặc start fresh → `playwright-ts` |
| Cần speed + parallel execution? | `playwright-ts` (built-in parallel workers, faster) |
| Project có existing Java stack? | Add new module → `selenium-java`/`appium-java` để consistency |
| CI/CD environment Node.js available? | YES → `playwright-ts` viable; NO + chỉ JVM → `selenium-java` |
| Cần test desktop apps native? | NEITHER — defer (out of scope cả 3 archetypes) |
| Cần API-only testing? | NEITHER — REST testing pattern khác; defer hoặc dùng Postman/Karate (separate project) |

## Comparison matrix

| Aspect | playwright-ts | selenium-java | appium-java |
|---|---|---|---|
| **Language** | TypeScript | Java | Java |
| **Build tool** | npm (or yarn/pnpm) | Maven | Maven |
| **Test runner** | Playwright Test | TestNG | TestNG |
| **Browser support** | Chromium, Firefox, WebKit (built-in) | Chrome/Firefox/Safari/Edge (drivers external) | N/A (mobile) |
| **Mobile support** | Emulation only (limited) | N/A | Native iOS + Android |
| **Locator API** | `page.locator()` + CSS/XPath/role/text | `@FindBy` PageFactory + By.id/css/xpath | Same as Selenium + iOS XCUITest + Android UiAutomator2 |
| **Async pattern** | async/await natively | Blocking (synchronous WebDriver) | Blocking |
| **Parallel execution** | Built-in workers (parallel by default) | TestNG parallel (config required) | TestNG parallel + multi-device (complex) |
| **Setup speed** | Fast (`npm init playwright`) | Medium (Maven archetype + WebDriverManager) | Slow (Appium server + emulator/device setup) |
| **CI/CD complexity** | Low (Node.js image) | Medium (JVM + drivers) | High (emulator infrastructure) |
| **Learning curve** | Medium (TypeScript + async) | Low (Java enterprise familiar) | Medium (Java + mobile concepts) |
| **Community / ecosystem** | Modern, growing | Mature, vast | Mature, mobile-specific |

## Pipeline downstream behavior

Sau khi archetype scaffold, downstream skills tự detect stack qua **MEMORY §2 Tech Stack** structured table:

| Stack detected | Downstream behavior |
|---|---|
| `Language = TypeScript` | scan-source-code/implement-automation/execute-maintain/review-src-tc → load `*-typescript.md` variants |
| `Language = Java` (default fallback) | Load `*.md` Java references (existing) |
| Mixed hoặc undefined | Fallback Java + log INFO warning |

Xem detail trong từng downstream skill SKILL.md §"Mode Routing — Stack-aware".

## Add new archetype (process)

Để add new archetype future (vd Python Pytest, Cypress):

1. Create `references/archetype-<name>.md` (template specs + folder structure + conventions)
2. Create `scripts/scaffold-<name>.py` (file generator)
3. Add row vào table này
4. Trong 4 downstream skills tạo `references/<original>-<lang>.md` variant nếu language khác Java/TS
5. Update Mode Routing trong downstream SKILL.md
6. Test end-to-end trên mock project

**Estimated effort cho new archetype:** ~20-25h (pattern established sau Playwright TS).

## Out of scope (current release)

- ❌ Cypress (web) — defer
- ❌ WebdriverIO (web) — defer
- ❌ Python + Pytest + Selenium — defer
- ❌ K6 / Locust (performance) — different domain
- ❌ Postman / Karate (API-only) — different domain, defer hoặc tách project
- ❌ Detox (React Native mobile) — defer
- ❌ XCTest / Espresso (native mobile non-Appium) — defer

User có thể request add archetypes mới qua issue/feature request.
