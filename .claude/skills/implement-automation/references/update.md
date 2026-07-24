# Implement Automation — Mode UPDATE

> `/implement-automation --update "thêm element buttonOTP vào LoginPage"`
> `/implement-automation --update "thêm test method cho TC_01.10"`
> `/implement-automation --update "locator buttonLogin đã đổi, cập nhật lại"`

## Khi nào dùng

- Thêm element mới vào Page class có sẵn
- Thêm test method cho TC mới (không cần generate cả class)
- Cập nhật locator bị stale
- Thêm verification method cho expected result mới

## Workflow

### Step 1: Đọc context
Source MEMORY §6 (Page Registry) + §7 (Test Registry) + §12 (Locator Registry).
Xác định: file nào cần sửa, element/method nào cần thêm/sửa.

### Step 2: Xác định scope thay đổi

| User nói | Skill hiểu | Action |
|----------|-----------|--------|
| "Thêm element X vào PageY" | Thêm `@FindBy` + field vào PageY.java | Lấy locator (vibe/playwright) → thêm vào class |
| "Thêm method cho TC-xxx" | Thêm `@Test` method vào TestClass.java | Parse TC-xxx từ TC-MASTER → generate method |
| "Locator X đã đổi" | Update `@FindBy` value | Playwright verify → sửa locator value |
| "Thêm verify method" | Thêm boolean/String method vào Page | Tạo method theo MEMORY §5b convention |

### Step 3: Sửa file

- Đọc file hiện tại
- Tìm vị trí chèn (sau elements section / sau methods section)
- Thêm code mới theo conventions
- KHÔNG sửa code hiện có (trừ locator value khi stale)

### Step 4: Verify + cập nhật MEMORY

```bash
mvn compile -q   # verify không break
```

Cập nhật MEMORY §6/§7/§12/§13 tương ứng.

### Constraints

- **KHÔNG recreate file** — chỉ thêm/sửa phần cụ thể
- **KHÔNG sửa conventions** — muốn đổi convention → `/scan-source-code --delta`
- **KHÔNG sửa BaseTest/BasePage** — chỉ sửa Page/Test classes
