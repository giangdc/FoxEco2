# Generate TC — Mode SYNC

> `/generate-tc --sync`
> Đồng bộ fragment mới vào TC-MASTER (workbook ISC) đã tồn tại.

## Workflow

### Step 1: Đọc TC-MASTER + scan fragments

```
1. TC-MASTER-v[X] (file ISC, xem consolidate.md) → đọc hiện tại: sheet Dashboard (danh sách module
   đã có), sheet RTM
2. Scan fragments/ → so sánh modified date vs TC-MASTER date
3. Hoặc đọc CHANGELOG → fragments chưa sync
```

### Step 2: Xác định loại thay đổi

| Fragment | Module đã có sheet trong TC-MASTER? (đối chiếu Dashboard cột D) | Action |
|----------|------------------------------------------------------------------|--------|
| MỚI | ❌ | APPEND — tạo sheet mới (duplicate template "Test Cases"), thêm row Dashboard, mở rộng RTM — theo đúng quy trình `consolidate.md` Step 3.2b–3.2d |
| CẬP NHẬT | ✅ | REPLACE — ghi đè rows trong sheet module đó |

### Step 3: Merge

**APPEND (module mới):** làm đúng `consolidate.md` Step 3.2b (tạo sheet, gán Mã chức năng, copy formula), 3.2c (thêm row Dashboard), 3.2d (mở rộng RTM — cả Req ID mới lẫn nối thêm term vào Req ID đã tồn tại ở sheet khác).

**REPLACE (module đã có):**
```
1. Trong sheet module đó: xoá TOÀN BỘ row 7 đến row cuối đang có dữ liệu — bao gồm CẢ row label
   Screen/Block (merge A:I/B:I, fill màu — không chỉ riêng row TC) lẫn row TC (cột B–M; giữ nguyên
   formula cột A/AM/AN/AO, không xoá, chỉ để chúng tự trả rỗng khi cột C rỗng). Lý do xoá cả label:
   fragment mới có thể đã đổi tên/thêm/bớt/sắp lại Block so với lần sync trước — không thể patch
   riêng cột B–M mà giữ nguyên label cũ (label cũ nằm ở cột B, dễ lẫn với dữ liệu TC nếu chỉ xoá theo
   cột thay vì theo row).
   ⚠️ Nếu TC đã có kết quả execution ở cột N–AL (round data) và TC ID đó VẪN CÒN trong fragment
   mới (cùng vị trí/nội dung logic) → PHẢI giữ nguyên round data, chỉ update cột B–M. Nếu TC bị xoá
   khỏi fragment (không còn tương ứng) → xoá cả round data của row đó (TC không còn tồn tại).
   Match TC cũ ↔ TC mới bằng cặp (DOC Source, Test Title) vì Testcase ID là formula tự sinh, không
   dùng làm khoá so khớp ổn định qua các lần regenerate. Round data match theo TC, di chuyển theo
   TC đó tới vị trí row mới nếu group Screen/Block làm đổi số thứ tự row.
2. Ghi lại toàn bộ vùng row 7 trở đi từ fragment mới — cả row label Screen/Block (copy nguyên
   merge cell + fill màu + text, xem `generate.md` Step 6.4) lẫn row TC (cột B–M, copy-down formula
   cột A/AM/AN/AO theo số row).
3. Re-validate: Mã chức năng sheet không đổi, tên tab sheet không đổi.
```

**Sau cả 2 nhánh:**
```
4. Re-check RTM: nếu module REPLACE làm thay đổi tập Req ID xuất hiện (thêm/bớt) → cập nhật lại
   theo consolidate.md Step 3.2d (Req ID mới cần row RTM mới; Req ID bị loại bỏ khỏi mọi sheet thì
   giữ row RTM nhưng count sẽ tự về 0 qua formula — không cần xoá row RTM).
5. Update Summary!C12 tự động qua formula — không cần ghi tay.
```

### Step 4: Save + update

```
1. TC-MASTER ISC file overwrite (đường dẫn 03_test-cases/v[X]/ISC_[Project]_[X]_TC_[TCVersion]_R[Round].xlsx)
2. Re-copy alias: TC-MASTER-v[X].xlsx + TC-MASTER-LATEST.xlsx (tương thích downstream — xem
   consolidate.md "Bối cảnh")
3. MASTER-MEMORY §6 update
4. CHANGELOG: action = SYNC, scope = [modules merged]
5. §8 = COMPLETED
```

## Checklist
- [ ] Module mới → sheet mới tạo đúng quy trình consolidate.md (Mã CN, Dashboard row, RTM)
- [ ] Module cập nhật → REPLACE cả row label Screen/Block lẫn cột B–M của TC, round data (N–AL) của TC còn tồn tại được giữ nguyên (di chuyển theo TC nếu đổi row), TC bị xoá thì xoá cả round data
- [ ] RTM cập nhật đủ term cho mọi sheet hiện có
- [ ] Alias TC-MASTER-v[X].xlsx + TC-MASTER-LATEST.xlsx đã re-copy
