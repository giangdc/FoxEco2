# Vibe Test Report — VR-002 — v1.0 — 2026-08-03

> Platform: mobile (Android, Appium MCP UiAutomator2)
> Environment: STG — FoxEco SDK trong FoxPro (package `com.hrisproject.stag`), emulator-5554
> Scope run này: module **Hoạt động (TC_01)** — 21/21 TC trong sheet
> (Phần Đăng tin/TC_04.94-103 đã chạy & ghi Excel ở phiên trước cùng ngày — BUG-001, BUG-002 —
> không lặp lại trong report này.)

## Summary

| Result | Count | % |
|--------|-------|---|
| ✅ PASS | 7 | 33% |
| ❌ FAIL | 5 | 24% |
| 🚫 BLOCKED | 9 | 43% |

> Tỷ lệ BLOCKED cao (43%) chủ yếu do **thiếu test data** ở tài khoản test hiện tại: tab "Đã hoàn
> thành" luôn rỗng (không có đơn Hoàn thành/Hết hạn), và không tìm được luồng tạo đơn "Đã huỷ"
> trong phạm vi khảo sát UI. Đây là giới hạn dữ liệu môi trường STG, KHÔNG phải lỗi app.

## Locator Coverage

| Pages visited | Elements captured | Verified ✅ | Not found ❌ |
|--------------|------------------|------------|-------------|
| 3 (Hoạt động, Theo dõi đơn, Bottom Nav) | 14 | 13 | 0 (1 empty-state icon chỉ ⚠️ Inferred do không có accessibility name riêng) |

→ Chi tiết: `vibe-locators.md` (run này) + đã merge vào `vibe-locators-latest.md`.

## Blocked TCs — ⚠️ KHÔNG automate (thiếu data)

| TC ID | Blocked at | Reason | Impact |
|-------|-----------|--------|--------|
| TC_01.5 | Step 3 | Tab "Đã hoàn thành" rỗng, không có đơn Hoàn thành/Hết hạn | Cần seed data hoặc chờ đơn thật hoàn tất |
| TC_01.9 | Step 2 | Cần dàn dựng tin sắp hết hạn + chờ cron backend | Không khả thi qua UI-only |
| TC_01.10 | Step 2 | Cần dàn dựng boundary chính xác tới phút | Không khả thi qua UI-only |
| TC_01.11 | Step 1 | Không có đơn Hoàn thành | Cùng gốc TC_01.5 |
| TC_01.16 | Step 1 | Không có card Hoàn thành để tap | Cùng gốc TC_01.5 |
| TC_01.17 | Step 1 | Không có đơn Đã huỷ; không tìm thấy nút Huỷ đơn trên màn Theo dõi đơn (role/luồng hiện tại) | Cần khảo sát thêm module Huỷ đơn (CNL) hoặc role khác |
| TC_01.18 | Step 1 | Không có card Hết hạn | Cùng gốc TC_01.5 |
| TC_01.19 | Step 2 | Tab "Đang diễn ra" luôn có dữ liệu sẵn, không rỗng | Cần tài khoản test riêng không có đơn nào |
| TC_01.21 | Step 1 | Không tạo được đơn Đã huỷ | Cùng gốc TC_01.17 |

## Failed TCs — Cần review TC hoặc app

| TC ID | Failed at | Expected | Actual | Khuyến nghị |
|-------|----------|----------|--------|-------------|
| TC_01.4 | Step 4 | Tab "Đang diễn ra" chỉ chứa Chờ ghép/Đã ghép/Đang giao/Đã huỷ | Có thêm 1 card badge "Đã giao" (trạng thái không nằm trong set TC quy định) | **Cần BA/PO xác nhận**: "Đã giao" là trạng thái hợp lệ trung gian (theo stepper 5 bước Theo dõi đơn) cần bổ sung vào TC, hay đây là bug phân loại tab sai. Chưa log bug — đề xuất user quyết định hướng xử lý. |
| TC_01.8 | Step 3 | Card có đủ 5 trường: icon, tên tin, tuyến, **ngày**, badge | Card chỉ có 4/5 trường — hoàn toàn thiếu trường ngày | **Ứng viên bug rõ ràng** — đã verify qua content-desc đầy đủ nhiều card, không có ngày ở bất kỳ đâu. Đề xuất `/log-bug` nếu user xác nhận đây đúng là gap cần fix. |
| TC_01.13 | Step 2 | Điều hướng "Chi tiết tin" | Điều hướng **"Theo dõi đơn"** | **Nghi ngờ TC-MASTER ghi sai expected**, không phải app bug — card có UI hint "Chạm để theo dõi đơn của bạn" khớp với hành vi thực tế. Đề xuất `/analyze-requirements --update` sửa expected result cho TC_01.13/14/15 thành "Theo dõi đơn". |
| TC_01.14 | Step 2 | Điều hướng "Chi tiết tin" | Điều hướng "Theo dõi đơn" | Cùng nguyên nhân TC_01.13 |
| TC_01.15 | Step 2 | Điều hướng "Chi tiết tin" | Điều hướng "Theo dõi đơn" | Cùng nguyên nhân TC_01.13 |

## Passed TCs — Sẵn sàng implement automation

| TC ID | Steps | Locators captured | Screenshot |
|-------|-------|-------------------|-----------|
| TC_01.1 | 3 | 5 (bottom nav tabs) | TC_01.1_final.png |
| TC_01.2 | 3 | 2 (tab switcher) | TC_01.2_TC_01.3_TC_01.6_TC_01.7_TC_01.12_final.png |
| TC_01.3 | 3 | (dùng lại) | cùng file trên |
| TC_01.6 | 4 | 1 (card descriptionContains) | cùng file trên |
| TC_01.7 | 4 | 1 | cùng file trên |
| TC_01.12 | 2 | 1 | cùng file trên |
| TC_01.20 | 2 | 2 (empty text + icon) | TC_01.20_empty_final.png |

## ⚠️ Finding ngoài phạm vi TC (phát hiện phụ, đã sửa cục bộ)

Trong lúc ghi kết quả vào TC-MASTER Excel, phát hiện **lỗi công thức có sẵn từ trước** ở cột
AM ("Vibe-test tổng")/AO ("Status") — tham chiếu lệch 1 dòng (off-by-one) tại nhiều vị trí.
Phạm vi ảnh hưởng **rất rộng, xuất hiện ở 8/9 sheet chức năng** (không phải do vibe-test run
này gây ra):

| Sheet | Số dòng bị lỗi công thức |
|-------|---------------------------|
| Hoạt động | 4 (đã fix trong run này — dòng 27-30) |
| Thông báo | 15 |
| Đăng tin | 108 |
| Trang chủ | 12 |
| Bảng tin & Chi tiết tin | 26 |
| Theo dõi đơn | 42 |
| Huỷ đơn | 4 |
| Tặng quà | 15 |
| Cá nhân | 0 (sạch) |

Đã fix riêng 4 dòng thuộc sheet Hoạt động (27-30, ảnh hưởng trực tiếp tới TC_01.18/19/20/21
vừa ghi kết quả trong run này) để đảm bảo Status hiển thị đúng. **KHÔNG động vào 7 sheet còn
lại** (222 dòng) vì ngoài phạm vi yêu cầu "tiếp test Hoạt động" — đề xuất chạy `/health-check`
hoặc 1 lượt sửa công thức riêng cho toàn bộ file trước khi dựa vào cột Status/Dashboard của
các sheet khác.

## Recommendation

- **Automate now:** 7 TC (TC_01.1, 2, 3, 6, 7, 12, 20) — locators sẵn sàng trong `vibe-locators.md`
- **Cần quyết định (bug vs TC-fix) trước automate:** 5 TC FAIL — xem bảng trên
- **Wait for data:** 9 TC BLOCKED — cần seed dữ liệu (đơn Hoàn thành/Hết hạn/Đã huỷ) ở STG hoặc
  tài khoản test rỗng riêng cho TC_01.19
- **Ngoài phạm vi, cần xử lý riêng:** lỗi công thức AM/AO ở 7 sheet khác (222 dòng) — khuyến nghị
  `/health-check`

## ✅ Addendum (2026-08-04) — Resolution của 5 FAIL

User xác nhận trực tiếp qua chat ngay sau khi nhận report này: **cả 5 FAIL đều là gap tài liệu/TC,
KHÔNG phải bug app thật.** Đã sửa lại:

| TC ID | Kết quả cũ | Kết quả mới | Lý do |
|-------|-----------|-------------|-------|
| TC_01.4 | Fail | **Pass** | "Đã giao" là trạng thái trung gian hợp lệ (giữa Đang giao và Hoàn thành) — bổ sung vào TC/scenario, không phải bug |
| TC_01.8 | Fail | **Pass** | Trường "ngày" chỉ có ở card tab "Đã hoàn thành" ("ngày hoàn thành"); tab "Đang diễn ra" vốn không có — TC ghi sai phạm vi, đã sửa |
| TC_01.13 | Fail | **Pass** | "Theo dõi đơn" là đích điều hướng ĐÚNG — TC ghi sai "Chi tiết tin", đã sửa |
| TC_01.14 | Fail | **Pass** | Cùng lý do TC_01.13 |
| TC_01.15 | Fail | **Pass** | Cùng lý do TC_01.13 |

**Kết quả cuối module Hoạt động: 12 PASS / 0 FAIL / 9 BLOCKED** (BLOCKED chờ bổ sung test data —
tab "Đã hoàn thành" và luồng tạo đơn "Đã huỷ"). Không log bug nào. Đã đồng bộ `test_scenario_map.md`
(SC-ORD-017/018/019/021/024 CORRECTED) + `TC-MASTER-LATEST.xlsx` (recalc sạch) +
`02_analyze-requirements/v1.0/MEMORY.md` (bổ sung #27) + `MASTER-MEMORY.md` §8.

## Excel & MEMORY updates

- TC-MASTER Excel: đã ghi Round 1 cho 21/21 TC sheet Hoạt động (cột N/P/Q), Executed By =
  `chaugiag@gmail.com`, đã recalc qua LibreOffice headless — Status (AO) khớp 100% với Kết quả (P).
- Chưa ghi ID Bugs (cột R) cho TC_01.4/8 — chờ quyết định của user (xem Finding trên) trước khi
  chạy `/log-bug`.
