# Generate TC — Mode DIRECT

> `/generate-tc --direct --name "Đăng nhập" --id 11 --spec "paste đặc tả"`
> Viết TC nhanh không qua analyze. Dùng khi chưa có MEMORY.md.

## Workflow

### Step 1: Thu thập info

Hỏi 6 câu (skip nếu có trong command/context):

| # | Câu hỏi | Ví dụ |
|---|---------|-------|
| 1 | Tên chức năng? | Đăng nhập |
| 2 | Function ID? | 11 |
| 3 | Menu path (navigate)? | Login → /login |
| 4 | Đặc tả? (paste hoặc file đính kèm) | "Email + Password, validate..." |
| 5 | Environment URL? | https://stg.example.com |
| 6 | Version? | v2.0 |

### Step 2: Phân tích đặc tả → scenarios

Xác định từ đặc tả:
- Happy path (positive scenarios)
- Required field validation (negative)
- Format validation (negative)
- Business rule (positive + negative)
- Boundary values
- Edge cases

Liệt kê scenarios cho user confirm:
```
📋 Scenarios from đặc tả "Đăng nhập":
  1. Đăng nhập thành công (P1)
  2. Email rỗng (P1)
  3. Password rỗng (P1)
  4. Email sai format (P1)
  5. Password sai (P1)
  6. Email không tồn tại (P2)
  7. Account bị lock (P2)

Confirm? Thêm/bớt scenario nào?
```

### Step 3-6: Viết TC + xuất Excel

Giống Mode GENERATE Step 3-6 nhưng:
- Req ID (cột B): để trống hoặc tạo tạm (prefix `DIRECT-`)
- DOC Source (cột C): `DIRECT-[date]` — **không được để trống** dù là tạm, vì formula cột A (Testcase ID) dựa vào cột C để đếm STT
- Fragment vẫn dựng từ template (`generate.md` Step 6) — 1 sheet, cột B–M ghi, TC ID vẫn để formula tự sinh
- Output: `03_test-cases/v[X]/fragments/TC-[MODULE]-direct-[date].xlsx`

### Step 7: Cập nhật

Ghi §8 = PARTIAL.
```
⚠️ TC tạo bằng DIRECT không có traceability đầy đủ.
Khuyến nghị:
  /analyze-requirements --init @00_input/v[X]/   → tạo REQ IDs
  Sau đó: /generate-tc --sync       → merge vào TC-MASTER
```

## Quy tắc
- **KHÔNG bịa Req ID** — để trống hoặc prefix `DIRECT-` nếu không có
- **DOC Source luôn phải có giá trị** (kể cả tạm `DIRECT-[date]`) — formula ID cần cột này
- Steps/Expected vẫn phải 1:1, cụ thể, verifiable; test data ghi thẳng trong Steps (không có cột Test Data riêng)
- Coverage checklist vẫn áp dụng
