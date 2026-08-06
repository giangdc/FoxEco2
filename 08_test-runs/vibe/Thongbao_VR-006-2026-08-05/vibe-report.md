# Vibe Test Report — Thongbao_VR-006-2026-08-05 (merged Round 1 + Round 2) — v1.0

> Platform: mobile (Android, FoxEco SDK trong FoxPro `com.hrisproject.stag`), emulator-5554 (Pixel 6)
> Module: **Thông báo (TC_03)** — 39/39 TC trong sheet
> Folder này gộp **Round 1** (gốc `VR-003-2026-08-04`, 2026-08-04 — đã merge và xoá folder gốc theo yêu
> cầu user, 2026-08-05) + **Round 2** (`Thongbao_VR-006-2026-08-05`, 2026-08-05 — retest 29 TC pending).
> Account: "Phan Minh Tài" — dữ liệu thông báo thật (không mock), tăng dần qua thời gian giữa 2 round.

## Summary tích luỹ (39 TC, sau 2 round)

| Result | Count | % |
|--------|-------|---|
| ✅ PASS | 15 | 38% |
| ❌ FAIL | 0 | 0% |
| 🚫 BLOCKED | 24 | 62% |

| Round | PASS | FAIL | BLOCKED | Scope |
|-------|------|------|---------|-------|
| Round 1 (2026-08-04) | 10 | 0 | 29 | Full sheet 39/39 TC |
| Round 2 (2026-08-05) | 5 | 0 | 24 | 29 TC pending từ Round 1 |

> 5 TC chuyển từ BLOCKED (R1) → PASS (R2): TC_03.25, .26, .27, .37, .39 — nhờ dữ liệu tài khoản tự
> nhiên phát sinh thêm (KHÔNG phải do sửa app hay seed thủ công): 2 loại thông báo mới xuất hiện
> ("Đơn đã bị huỷ", "Đơn đã hoàn tất") + xác nhận được cơ chế load-more hoạt động đúng qua nhiều lần
> scroll khi list đủ sâu hơn.

## Locator Coverage (tích luỹ)

| Pages visited | Elements captured | Verified ✅ | Not found 🚫 |
|--------------|------------------|------------|-------------|
| 3 (Trang chủ, Thông báo, Theo dõi đơn) | 11 (bell icon, header, back icon, mark-all-read, group headers ×3, notif-item pattern + 2 loại mới, unread-dot, Theo dõi đơn header + banner huỷ + timeline hoàn thành) | 11 | 4 loại push-content không tồn tại (không tính là "not found" locator mà là "data không tồn tại") |

→ Chi tiết: `vibe-locators.md` (merged) + đã merge vào `vibe-locators-latest.md`.

## Finding đáng chú ý (không phải FAIL, nhưng cần lưu ý)

| # | Quan sát | Đánh giá |
|---|----------|----------|
| 1 | Icon quay lại ở header Thông báo có `content-desc=""` (rỗng) — không có accessibility label | Gap nhỏ về a11y, không chặn chức năng (vẫn tap được qua bounds), nhưng nên bổ sung label cho tool đọc màn hình + automation ổn định hơn |
| 2 | Danh sách thông báo KHÔNG có bất kỳ text/footer nào báo "đã hết dữ liệu" khi load hết — chỉ dừng lặng lẽ | Không phải FAIL (Expected TC_03.26 không yêu cầu literal UI message) nhưng là **candidate UX suggestion** cho BA — xác nhận lại 2 lần (Round 1 + Round 2), nhất quán qua cả 2 lần chạy |
| 3 | Nút "Đánh dấu đã đọc" tự ẩn khi không còn thông báo chưa đọc (thay vì hiện + no-op) | Hành vi hợp lý, PASS cho TC_03.23, nêu ra để implement-automation biết selector này là conditional (không phải lúc nào cũng có mặt trên DOM) |
| 4 | `resource-id` mỗi card thông báo dạng `notif-item-<uuid>` là unique, nhưng `content-desc` (tiêu đề) trùng lặp giữa nhiều card cùng loại | Automation PHẢI dùng resource-id hoặc vị trí, KHÔNG dùng content-desc để định vị 1 card cụ thể |
| 5 | TC_03.28 (mất mạng giữa lúc load) không thể canh đúng timing vì danh sách đã load hết dữ liệu trước khi kịp ngắt mạng | Không phải bug — giới hạn kỹ thuật của UI-only automation khi dữ liệu hữu hạn; cần seed thêm dữ liệu hoặc dùng network-throttle (giữ độ trễ) thay vì tắt hẳn |
| 6 | Dữ liệu thông báo tài khoản "Phan Minh Tài" tăng đáng kể giữa 2 ngày test (từ ~10 item ở Round 1 lên vượt qua nhóm "TUẦN NÀY" ở Round 2) | Tài khoản dùng chung nhiều tester → dữ liệu không ổn định giữa các round, cần lưu ý khi so sánh kết quả round-to-round |

## Blocked TCs — ⚠️ KHÔNG automate (thiếu data/orchestration, không phải bug — đã re-check ở Round 2, không đổi)

| TC ID | Lý do | Đề xuất |
|-------|-------|---------|
| TC_03.1, .2, .3 | Cần kiểm soát chính xác số tin NEED phù hợp/tin OFFER (trần 5) | Multi-device: 1 Carrier đăng OFFER + N Sender đăng NEED matching |
| TC_03.4 – .11 | Cần Carrier/Sender/Receiver xác nhận từng bước (ghép/lấy hàng/giao hàng/nhận hàng) | `vibe-test-multi-device` — 3 role, 3 device song song |
| TC_03.12 | Cần Sender gửi quà cảm ơn cho Carrier | Multi-device, sau khi đơn hoàn tất |
| TC_03.13, .14, .15 | Cần huỷ đơn từ 3 vai trò khác nhau | Multi-device |
| TC_03.16 | Cần chờ tin đăng quá hạn (thời gian thực hoặc cron backend) | Không khả thi UI-only, cần fixture/backend trigger |
| TC_03.19 | Cần tài khoản/trạng thái rỗng | Seed tài khoản test mới hoàn toàn sạch |
| TC_03.28 | Không canh được đúng timing "đang load thêm" (list đã hết dữ liệu trước khi cắt mạng) | Seed thêm dữ liệu hoặc dùng network-throttle giữ độ trễ thay vì tắt hẳn |
| TC_03.29, .30 | Loại thông báo "SĐT đã lộ"/NTF-04 không có trong lịch sử tài khoản, cần trigger thời gian thực | Cần tài khoản Carrier vừa ghép đơn thật, multi-device |
| TC_03.31, .32, .34, .38 | 4 loại thông báo không tồn tại trong tài khoản test (đã rà soát qua cả 2 round) | Multi-device hoặc tài khoản khác có đủ lịch sử đa dạng hơn |

## Passed TCs — Sẵn sàng implement automation (15 TC tích luỹ)

| TC ID | Round | Steps | Locators captured | Screenshot |
|-------|-------|-------|-------------------|-----------|
| TC_03.17 | R1 | 2 | header, group header, card pattern, mark-all-read button | 01_notification_screen.png |
| TC_03.18 | R1 | 1 | back icon (xpath bounds) | 12_TC_03.18_back_icon.png |
| TC_03.20 | R1 | 2 | notif-item resourceId, unread-dot | 06_..., 07_TC_03.20_after_read.png |
| TC_03.21 | R1 | 1 | mark-all-read button | 09_TC_03.21_markall_read.png |
| TC_03.22 | R1 | 2 | (dùng lại notif-item resourceId) | 08_TC_03.22_tap_already_read.png |
| TC_03.23 | R1 | 1 | (verify absence of button) | — (đã verify qua page-source) |
| TC_03.24 | R1 | 1 | (verify initial render) | 01_notification_screen.png |
| TC_03.33 | R1 | 1 | notif-item resourceId khác | 10_TC_03.33_tap_donguitoiban.png |
| TC_03.35 | R1 | 1 | notif-item resourceId khác | 11_TC_03.35_tap_nguoivanchuyenlayhang.png |
| TC_03.36 | R1 | 1 | (dùng lại của TC_03.20) | 06_TC_03.20_36_tap_daduocgiao.png |
| TC_03.25 | R2 | 1 | (page-source diff qua các lần scroll) | — |
| TC_03.26 | R2 | 1 | (page-source diff) | TC_03.26_scroll_bottom_check.png |
| TC_03.27 | R2 | 1 | (dùng chung bằng chứng TC_03.26) | TC_03.26_scroll_bottom_check.png |
| TC_03.37 | R2 | 3 | notif-item resourceId (Đơn đã hoàn tất) | TC_03.37_after_tap_donhoantat.png |
| TC_03.39 | R2 | 3 | notif-item resourceId (Đơn đã bị huỷ) | TC_03.39_after_tap_donbihuy.png |

## Recommendation

- **Automate now:** 15 TC — locators sẵn sàng trong `vibe-locators.md`, đủ ổn định (resource-id unique per card)
- **Wait for multi-role data:** 16 TC (TC_03.1-16) — chạy `/vibe-test-multi-device` riêng cho nhóm này
- **Wait for more diverse data:** 6 TC (TC_03.29-32, 34, 38) — cần tài khoản/lịch sử thông báo đa dạng hơn hoặc multi-device trigger
- **Wait for empty account:** 1 TC (TC_03.19) — cần tài khoản test sạch
- **Wait for precise network-loss timing:** 1 TC (TC_03.28) — cần seed thêm dữ liệu hoặc network-throttle tool

## Excel & MEMORY updates

- TC-MASTER Excel: Round 1 (39/39 TC, cột N-R) đã ghi từ trước (2026-08-04). Round 2 (29/29 TC pending, cột S-W) — ghi sau khi file được đóng trong LibreOffice.
- **Đã fix dứt điểm 15 dòng lỗi công thức off-by-one cột AM/AO** của sheet Thông báo ở Round 1 (2026-08-04) — không lặp lại việc fix ở Round 2 vì đã sạch từ trước.
- **2026-08-05: Đã merge folder `VR-003-2026-08-04` (Round 1 gốc) vào folder này (`Thongbao_VR-006-2026-08-05`) theo yêu cầu user** — gộp đầy đủ 4 file (vibe-report/vibe-log/vibe-locators/mcp-session-log) + 13 screenshot Round 1 vào đây, sau đó đã xoá folder `VR-003-2026-08-04` gốc. Toàn bộ lịch sử 2 round giờ nằm trong 1 folder duy nhất.
