# Implement Automation — Mode LOCATOR

> `/implement-automation --locator @https://stg.example.com/login`
> `/implement-automation --locator @https://stg.example.com/dashboard`
> Chỉ lấy locator từ web thực, KHÔNG generate code.

## Khi nào dùng

- Trước khi implement, muốn survey UI trước
- Locator cũ stale, cần refresh
- Trang mới chưa có trong vibe-locators hoặc MEMORY §12

## Workflow

### Step 1: Đọc context
Source MEMORY §5 (conventions) + §12 (existing locators).
Ghi §8 = IN_PROGRESS.

### Step 2: Playwright navigate + snapshot

```
browser_navigate(URL)
→ chờ page load (3-5s hoặc explicit wait)
browser_snapshot() → accessibility tree
browser_take_screenshot() → visual reference
```

### Step 3: Extract locators

Scan accessibility tree → tìm tất cả interactive elements:
- Inputs (text, password, email, number)
- Buttons (submit, button, link-as-button)
- Dropdowns (select, custom dropdown)
- Checkboxes, radios
- Links
- Text elements (headings, labels, error messages)

Mỗi element → xác định locator strategy (priority table từ implement.md Step 3).

### Step 4: Map với naming convention

```
Element: <input id="email" type="text">
→ Name: textBoxEmail (MEMORY §5a: [type][Name])
→ Locator: @FindBy(id = "email")
→ Strategy: id (priority 1)
```

### Step 5: Present locators cho user review

```
📍 Locators extracted — [URL] ([N] elements):

| Element | Type | Strategy | Value | Suggested Name |
|---------|------|----------|-------|---------------|
| Email input | text input | id | email | textBoxEmail |
| Password input | password | id | password | textBoxPassword |
| Login button | button | css | [data-testid='btn-login'] | buttonLogin |
| Error message | div | css | .error-message | labelError |
| Forgot link | anchor | xpath | //a[text()='Quên mật khẩu'] | linkForgotPassword |

Confirm? Hoặc chỉnh sửa tên/locator nào?
```

### Step 6: Cập nhật Source MEMORY §12

```markdown
| Element | Strategy | Value | Source | Page | Date |
|---------|----------|-------|--------|------|------|
| textBoxEmail | id | email | playwright-live | Login | 2026-05-25 |
| buttonLogin | css | [data-testid='btn-login'] | playwright-live | Login | 2026-05-25 |
```

Ghi §8 = COMPLETED (mode LOCATOR).

**KHÔNG generate Page class hay Test class.** Chỉ populate MEMORY §12.
