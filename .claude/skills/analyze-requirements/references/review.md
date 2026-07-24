# Analyze Requirements — Mode REVIEW

> `/analyze-requirements --review`
> `/analyze-requirements --review --version v1.0`
> `/analyze-requirements --review "module nào risk cao nhất?"`
> Khi nào: Xem tổng quan kết quả phân tích. KHÔNG sửa file.

## Input (chỉ đọc)

```
MASTER-MEMORY.md + Version MEMORY.md + deliverable files (nếu cần chi tiết)
```

## Workflow

### Step 1: Đọc MASTER-MEMORY + Version MEMORY

### Step 2: Trình bày theo câu hỏi user

| User hỏi | Trình bày |
|----------|-----------|
| "Xem tổng quan" | Summary: modules, scenario counts, clarification status |
| "Module nào risk cao?" | risk_assessment.md → rank modules |
| "Còn clarification nào?" | MEMORY §6 → filter Status = Open |
| "So sánh v1.0 với v2.0" | MASTER-MEMORY §5 Version Comparison |
| "Bao nhiêu scenario P1?" | MEMORY §4 → filter Priority |

### Step 3: KHÔNG sửa file. Nếu user muốn sửa → chuyển Mode UPDATE.

---

## Checklist

- [ ] Chỉ đọc, KHÔNG sửa bất kỳ file nào
- [ ] Trả lời đúng câu hỏi user
- [ ] Nếu phát hiện inconsistency → suggest `/health-check`
