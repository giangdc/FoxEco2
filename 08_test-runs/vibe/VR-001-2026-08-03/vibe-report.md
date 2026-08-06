# Vibe Test Report — VR-001 — v1.0 — 2026-08-03

> Platform: mobile (Appium MCP, Android)
> Environment: FoxPro STG — package `com.hrisproject.stag`, device ZPB66PZLPRBMEAZT
> Scope: luồng "Đăng tin OFFER (Tôi nhận giao hàng)" — TC_04.94 → TC_04.103 (10 TC), Round 1

## Summary

| Result | Count | % |
|--------|-------|---|
| ✅ PASS | 6 | 60% |
| ❌ FAIL | 4 | 40% |
| 🚫 BLOCKED | 0 | 0% |

## Locator Coverage

| Pages visited | Elements captured | Verified ✅ | Not found 🚫 |
|--------------|------------------|------------|-------------|
| 4 (Trang chủ, Đăng tin mới, Form OFFER, Time Picker dialog) | ~20 | 18 | 2 (1 locator strategy fallback + 1 error-msg-not-existing case) |

→ implement-automation có thể bắt đầu với 18 locators đã verified cho các TC PASS. Lưu ý: 2 field
Điểm xuất phát/Điểm đến dùng `instance(2)`/`instance(3)` trên className EditText (không có
resource-id) — dễ vỡ nếu app thêm/bớt field phía trên; đề xuất backend/dev team gắn thêm
`testTag`/content-desc cho các field quan trọng.

## Blocked TCs — ⚠️ KHÔNG automate

*(không có TC nào BLOCKED trong run này)*

## Failed TCs — Cần review TC hoặc fix app

| TC ID | Failed at | Expected | Actual |
|-------|----------|----------|--------|
| TC_04.94 | Bước quan sát field | Điểm xuất phát auto-fill; Thời gian di chuyển default 17:30–18:30 | Điểm xuất phát trống (không auto-fill); Thời gian di chuyển default = giờ hiện tại+30p |
| TC_04.95 | Bước 1 & 3 (giữ default) | Điểm xuất phát default = 'Tòa nhà Lô B3...'; Thời gian di chuyển default 17:30–18:30 | Không có default cho Điểm xuất phát (phải nhập thủ công); Thời gian di chuyển default khác — chức năng submit vẫn hoạt động đúng |
| TC_04.99 | Bước 2 (bấm gửi) | Bị chặn + báo lỗi "Điểm đến phải khác điểm xuất phát" | Bị chặn đúng (nút disabled) nhưng KHÔNG có message lỗi hiển thị |
| TC_04.100 | Bước 2 (bấm gửi) | Bị chặn + báo lỗi | Bị chặn đúng (nút disabled) nhưng KHÔNG có message lỗi hiển thị |

**Root cause phân nhóm:**
- TC_04.94, TC_04.95 → cùng 1 nguồn: thiếu auto-fill Điểm xuất phát + sai default giờ di chuyển (đề xuất log 1 bug chung, Major).
- TC_04.99, TC_04.100 → cùng 1 nguồn: thiếu message lỗi validate cho field địa điểm (đề xuất log 1 bug chung, Minor — đối chiếu TC_04.101 cùng khối "Thời gian di chuyển" LẠI CÓ message, cho thấy xử lý lỗi không đồng nhất giữa các field).

## Passed TCs — Sẵn sàng implement automation

| TC ID | Steps | Locators captured | Screenshot |
|-------|-------|-------------------|-----------|
| TC_04.96 | 1 | Điểm xuất phát (EditText instance 2) | — (page-source evidence) |
| TC_04.97 | 1 | Điểm xuất phát (EditText instance 2) | — (page-source evidence) |
| TC_04.98 | 1 | Điểm xuất phát (EditText instance 2) | — (page-source evidence) |
| TC_04.101 | 2 | Time picker wheel (coordinate-based), error text locator | TC_04.101_final.png |
| TC_04.102 | 2 | Time picker wheel, nút Đăng tin ngay | TC_04.102_final.png |
| TC_04.103 | 2 | Điểm đến (EditText instance 3), nút Đăng tin ngay | TC_04.103_final.png |

## Recommendation

- **Automate now:** 6 TCs (96, 97, 98, 101, 102, 103) — locators sẵn sàng trong `vibe-locators.md`.
  Lưu ý riêng: TC_04.101/102 dùng time-picker wheel coordinate-swipe — brittle, cân nhắc đề xuất
  QA lead thêm content-desc cho wheel trước khi automate để tránh flaky test.
- **Log bug trước khi automate:** 4 TCs (94, 95, 99, 100) — 2 bug root-cause riêng biệt (xem trên).
  Chạy `/log-bug` cho từng TC FAIL để tạo bug record, sau đó ID Bugs sẽ được ghi vào TC-MASTER.
- **Không có TC nào phải chờ app fix mới test được** — tất cả 10 TC đã chạy được qua MCP, không có
  BLOCKED.

## Next steps đề xuất

```
1. /log-bug --tc TC_04.94,TC_04.95 "Điểm xuất phát không auto-fill + Thời gian di chuyển default sai"
2. /log-bug --tc TC_04.99,TC_04.100 "Thiếu message lỗi khi validate Điểm đến/Điểm xuất phát"
3. /implement-automation --module "Đăng tin" --tc TC_04.96,TC_04.97,TC_04.98,TC_04.101,TC_04.102,TC_04.103
```
