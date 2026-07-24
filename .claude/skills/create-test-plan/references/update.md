# Create Test Plan — Mode UPDATE

> `/create-test-plan --update "thêm module Payment"`
> `/create-test-plan --update "đổi schedule phase 2"`

## Workflow

### Step 1: Đọc test plan hiện tại

### Step 2: Sửa sections bị ảnh hưởng
KHÔNG tạo lại từ đầu — chỉ sửa phần thay đổi.

### Step 3: Increment version trong Revision History
```markdown
| 1.1 | [date] | [name] | Thêm module Payment vào scope |
```

### Step 4: Cảnh báo downstream nếu scope thay đổi
```
⚠️ Scope thay đổi. Ảnh hưởng:
  - analyze-requirements: cần analyze thêm module Payment
  - generate-tc: cần generate TC cho Payment
```

### Step 5: CLAUDE.md update + §8 = COMPLETED
