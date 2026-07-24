# Scan Source Code — Mode DELTA

> `/scan-source-code --delta`
> Cập nhật MEMORY.md khi source code thay đổi (thêm/sửa/xóa files).

## Khi nào dùng
- Sau implement-automation tạo Page/Test classes mới
- Developer commit code mới
- Refactor (rename, move files)

## Workflow

### Step 1: Đọc MEMORY hiện tại
Ghi §8 = IN_PROGRESS.

### Step 2: Scan files → diff với MEMORY

```bash
# Tìm tất cả .java files hiện tại
find 10_source-code/ -name "*.java" | sort > /tmp/current_files.txt

# So sánh với MEMORY §1 (files đã biết):
# → NEW files: có trên disk nhưng không có trong MEMORY
# → DELETED files: có trong MEMORY nhưng không có trên disk
# → MODIFIED files: content changed (so sánh method count, element count)
```

### Step 3: Analyze changes

| Loại thay đổi | Action |
|---------------|--------|
| New Page class | Đọc file → thêm vào §6 Page Registry |
| New Test class | Đọc file → thêm vào §7 Test Registry |
| Modified Page class | Đọc lại → update §6 (elements, methods) |
| Modified Test class | Đọc lại → update §7 (methods, TC mapping) |
| Deleted file | Remove từ §6/§7, ghi warning |
| New utility class | Thêm vào §8 Utilities |
| pom.xml changed | Update §2 Tech Stack |

### Step 4: Update MEMORY sections bị ảnh hưởng
KHÔNG ghi đè toàn bộ — chỉ update sections thay đổi.
Ghi header: `> Cập nhật lần cuối: [date] — DELTA scan: [N] new, [N] modified, [N] deleted`

### Step 5: Present summary
```
🔄 Delta scan results:
  NEW: LoginPage.java (4 elements, 6 methods)
  MODIFIED: DashboardTest.java (+2 methods: testFilterByDate, testExportCSV)
  DELETED: OldReportPage.java (removed from §6)

MEMORY updated: §6, §7
```

Ghi §8 = COMPLETED.

## Constraints
- KHÔNG đọc lại files unchanged — chỉ diff
- KHÔNG sửa code — chỉ update MEMORY
