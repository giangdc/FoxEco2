# Scan Source Code — Mode CHECK

> `/scan-source-code --check`

## Workflow

Đọc MEMORY.md → trình bày tổng quan:

```
📊 Source Code Overview

Framework: Java 21 + Selenium 4 + TestNG 7
Build: Maven (pom.xml)

Files: [N] .java files
  Page classes: [N] (§6)
  Test classes: [N] (§7)
  Base classes: 2 (BaseTest, BasePage)
  Utilities: [N] (§8)

Elements indexed: [N] total
Test methods indexed: [N] total
SC coverage: [N]/[total] scenarios mapped ([%])

Naming conventions:
  Elements: [type][Name] (buttonLogin, textBoxEmail)
  Methods: [action][Target] (clickLogin, enterEmail)
  Tests: test[Feature][Case] (testLoginSuccess)

Last scan: [date] ([FULL/DELTA])
```

KHÔNG scan lại, KHÔNG sửa.
