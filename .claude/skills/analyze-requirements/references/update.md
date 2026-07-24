# Analyze Requirements — Mode UPDATE

> `/analyze-requirements --update "BA confirm OTP expire sau 5 phút"`
> `/analyze-requirements --update "Sửa SC-LOGIN-003: expected result sai"`
> Khi nào: Đã có kết quả phân tích, nhận feedback cần sửa (cùng version).

## Input → Output

| Input | Output |
|-------|--------|
| User feedback | Sửa files bị ảnh hưởng (KHÔNG tạo lại từ đầu) |
| Version MEMORY.md | Đồng bộ Version MEMORY.md + MASTER-MEMORY.md |

---

## Xử lý theo loại feedback

| User nói | Skill hiểu | Files cần sửa |
|----------|-----------|---------------|
| "BA confirm [trả lời]" | Resolve clarification | traceability → scenario_map → data_catalog → MEMORY → MASTER |
| "Sửa scenario SC-xxx" | Sửa scenario cụ thể | scenario_map → MEMORY §4 → MASTER §3 |
| "Thêm scenario cho [feature]" | Thêm scenario mới | scenario_map → MEMORY §3+§4 → MASTER §3 |
| "Dev nói [thay đổi kỹ thuật]" | Technical change | scenario_map → data_catalog → MEMORY |
| "Đổi priority/risk module X" | Điều chỉnh risk | risk_assessment → scenario_map → MEMORY §3 |
| "Thêm/đổi Block cho màn hình X" | Cập nhật Block Definitions | scenario_map (Block Definitions) → scenario_map (đồng bộ cột Screen/Block ở bảng Scenarios) → MEMORY §4 → MASTER §3 |

---

## Workflow

### Step 1: Đọc context + xác định scope

```
1. Version MEMORY.md → biết files nào tồn tại
2. Xác định: feedback ảnh hưởng file nào, scenario nào
3. Ghi §8 = IN_PROGRESS
```

### Step 2: Sửa files bị ảnh hưởng

**KHÔNG tạo lại file từ đầu** — chỉ sửa phần bị ảnh hưởng.

### Step 3: Đồng bộ MEMORY

```
1. Cập nhật Version MEMORY.md (header: > Cập nhật lần cuối: [date] — [lý do])
2. Cập nhật MASTER-MEMORY.md §3 (nếu scenario thay đổi)
```

> **Structure-lock (Nguyên tắc cốt lõi #6):** sửa NỘI DUNG trong cấu trúc sẵn có — giữ nguyên header cột + section của template. KHÔNG thêm/bớt/đổi cột khi update.

### Step 4: Kiểm tra downstream impact

Nếu thay đổi ảnh hưởng TC đã generate:
```
⚠️ Thay đổi này ảnh hưởng [N] TC đã tạo. Cần: /generate-tc --regenerate --module [X]
```

Ghi §8 = COMPLETED.

---

## Checklist

- [ ] Chỉ sửa phần bị ảnh hưởng (không tạo lại từ đầu)
- [ ] Version MEMORY + MASTER-MEMORY đồng bộ
- [ ] Cảnh báo downstream nếu TC bị ảnh hưởng
- [ ] §8 = COMPLETED
