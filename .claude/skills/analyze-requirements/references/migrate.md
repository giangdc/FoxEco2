# Analyze Requirements — Mode MIGRATE

> `/analyze-requirements --migrate`
> Khi nào: Project có 00_input/ và 02_analyze-requirements/ dạng flat (không version folders), cần chuyển sang multi-version.

## Workflow

### Step 1: Kiểm tra cấu trúc hiện tại

Xác nhận: có files flat trong `00_input/` và `02_analyze-requirements/` (không nằm trong subfolder v[X]/).

### Step 2: Migrate

```
1. Tạo 00_input/v1.0/ → move files hiện tại vào
2. Tạo 02_analyze-requirements/v1.0/ → move files hiện tại vào
3. MEMORY.md → v1.0/MEMORY.md + thêm §0 Version Context
4. Tạo MASTER-MEMORY.md từ data trong MEMORY.md (bao gồm §8 Pipeline Status)
5. Update DOC IDs: DOC-01 → DOC-v1.0-01 (trong tất cả files)
6. Tạo Project_rule.md nếu chưa có
7. Update CLAUDE.md với version info
```

### Step 3: Verify + present

Liệt kê files đã move, confirm structure mới.
Ghi §8 = COMPLETED.

---

## Checklist

- [ ] Files move vào v1.0/ folders
- [ ] DOC IDs rename sang prefix version
- [ ] MASTER-MEMORY.md tạo
- [ ] CLAUDE.md update
