# Vibe Test — Mode RETEST

> `/vibe-test --retest TC_01.3`
> `/vibe-test --retest --module Login` (tất cả FAIL/BLOCKED của module)

## Khi nào
- TC BLOCKED → app đã fix/deploy, cần test lại
- TC FAIL → TC đã sửa (expected), cần verify lại

## Workflow
1. Đọc vibe-log cũ → lấy TC đã FAIL/BLOCKED
2. Re-parse TC-MASTER (có thể đã update steps/expected)
3. **Xác định round ghi kết quả (khác mặc định của EXECUTE mode):**
   - **Mặc định RETEST: GHI ĐÈ round gần nhất đã có dữ liệu cho TC đó** (round chứa kết quả FAIL/
     BLOCKED đang muốn test lại) — KHÔNG mở round mới. Lý do: retest là "hoàn thiện nốt round đang
     dang dở" (app vừa fix trong CÙNG chu kỳ test), không phải bắt đầu chu kỳ test mới.
   - `--new-round` (opt-in): mở round tiếp theo còn trống thay vì ghi đè — dùng khi retest này thực
     sự đại diện cho 1 vòng test mới (vd sau khi cả team đã chuyển sang Round 2 chính thức).
   - Áp dụng cùng luật "hết 5 round → báo lỗi, không tự ý mở round 6" như execute.md Step 3b.
4. Thực thi lại TC (giống execute mode)
5. **Re-capture locators** (element trước đó NOT FOUND → giờ có thể found)
6. So sánh kết quả mới vs cũ
7. Ghi đè (hoặc thêm mới nếu `--new-round`) đúng round: cột Vibe-test=Yes, Kết quả, Executed By, ID
   Bugs (xoá nếu retest PASS — bug coi như fixed, giữ nguyên nếu vẫn Fail) — xem `execute.md` Step 7a
   cho chi tiết từng cột.
8. Cập nhật vibe-report + vibe-log + vibe-locators.md + Version MEMORY §4 (cache)

```
🔄 Retest TC_01.3 (ghi đè Round 1, không mở round mới):
  Before: 🚫 Block tại Step 2 (SSO button missing)
  After:  ✅ Pass (4/4 steps)
  New locators: SSO button → css=[data-testid='btn-sso-google']
  TC-MASTER Round 1: Kết quả Block→Pass, ID Bugs xoá (nếu có)
  → Ready for automation
```
