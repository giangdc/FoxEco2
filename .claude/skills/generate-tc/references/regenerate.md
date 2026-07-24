# Generate TC — Mode REGENERATE

> `/generate-tc --regenerate --module Login`
> Khi nào: analyze đã update (feedback/clarification), TC cũ cần tạo lại.

## Workflow

### Step 1: So sánh MEMORY §9 vs §4

```
MEMORY §9 (TC Gen Log) — last generate date per DOC/module
MEMORY §4 (Scenario Index) — current scenarios

Tìm:
  - Scenarios MODIFIED sau lần generate gần nhất
  - Scenarios mới (thêm từ analyze --update)
  - Clarifications resolved → scenarios unblocked
```

### Step 2: Xác định affected TCs

```
📋 Regenerate scope — v2.0:

Module Login — 3 scenarios thay đổi:
  SC-LOGIN-003: MODIFIED (OTP expire 3→5 phút) → TC-LOGIN-003~005 cần regenerate
  SC-LOGIN-010: NEW (SSO login, thêm từ update) → TC mới cần tạo
  SC-LOGIN-007: Unblocked (clarification resolved) → TC mới

Confirm? (Y/N)
```

### Step 3: Tạo lại TC cho affected scenarios

Giống GENERATE Step 3-6 nhưng:
- Chỉ cho affected scenarios
- TC ID KHÔNG reuse thủ công — cột A là formula tự sinh theo STT row (xem `generate.md` "TC ID không tự đặt tay"). Match TC cũ ↔ TC thay thế bằng cặp (DOC Source, Test Title), không dùng ID.

### Step 4: Auto SYNC vào TC-MASTER

```
1. Mở TC-MASTER (file ISC — xem consolidate.md)
2. Trong đúng sheet module: match TCs cũ bằng (DOC Source, Test Title), REPLACE cột B–M; nếu TC cũ
   đã có round data (cột N–AL) và scenario chỉ MODIFIED (không đổi ý nghĩa TC) → giữ nguyên round
   data cũ (cần retest lại nhưng không bắt buộc xoá lịch sử); nếu TC bị thay thế hoàn toàn (thay
   đổi bản chất case) → xoá round data cũ, TC coi như mới cần test lại từ đầu.
3. TCs mới (scenarios mới) → chèn vào ĐÚNG nhóm label Screen/Block tương ứng (xem `generate.md`
   Step 6.4), KHÔNG append rời ở cuối sheet phá vỡ thứ tự group; copy-down formula cột A/AM/AN/AO
   theo row mới.
4. Re-validate: xem sync.md Step 3
5. Save TC-MASTER + alias TC-MASTER-v[X].xlsx / TC-MASTER-LATEST.xlsx
```

### Step 5: Cập nhật MEMORY

- §4: TC Status update
- §9: TC Gen Log thêm row (action = REGENERATE)
- CHANGELOG: action = REGENERATE, scope = [affected TCs]

## Checklist
- [ ] Affected scenarios identified
- [ ] TCs regenerated theo scenarios mới
- [ ] TC-MASTER updated (replace + append)
- [ ] MEMORY §4 + §9 sync
