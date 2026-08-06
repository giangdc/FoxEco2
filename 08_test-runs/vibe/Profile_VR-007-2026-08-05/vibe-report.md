# Vibe Test Report — Profile_VR-007-2026-08-05 (merged Round 1+2 + Round 3) — v1.0

> Platform: mobile (Appium MCP, Pixel 6 emulator `emulator-5554`)
> App: FoxPro `com.hrisproject.stag` (FoxEco SDK)
> Module: **Cá nhân (TC_02)** — 17/17 TC trong sheet
> Folder này gộp **Round 1 + Round 2** (gốc `VR-004-2026-08-04`, 2026-08-04 — đã merge và xoá folder gốc
> theo yêu cầu user, 2026-08-05) + **Round 3** (`Profile_VR-007-2026-08-05`, 2026-08-05 — retest 9 TC
> pending từ Round 1+2).
> Account Round 1: `stag_TaiPM@fpt.com` (0 đơn/0 quà) · Round 2: `stag_giangdc2@fpt.com` (1 đơn/1 quà) ·
> Round 3: switch Giang (5 đơn/5 quà) ↔ TaiPM (0/0) tuỳ TC.

## Summary tích luỹ (17 TC, sau 3 round)

| Result | Count | % |
|--------|-------|---|
| ✅ PASS | 12 | 71% |
| ❌ FAIL | 3 | 18% |
| 🚫 BLOCKED | 2 | 12% |

| Round | PASS | FAIL | BLOCKED | Scope |
|-------|------|------|---------|-------|
| Round 1 (2026-08-04, TaiPM) | 6 | 4 | 7 | Full sheet 17/17 TC |
| Round 2 (2026-08-04, Giang) | 9 | 3 | 5 | Full sheet 17/17 TC (retest cùng ngày, account khác) |
| Round 3 (2026-08-05) | 4 | 3 | 2 | 9 TC pending sau R1+2 |

> Status cuối (theo round mới nhất có dữ liệu cho từng TC, tự động rollup trong Excel): **12 Pass / 3 Fail / 2 Block**.
> 4 TC chuyển FAIL→PASS ở Round 3: `TC_02.5` (re-confirm 0/0 qua TaiPM), `TC_02.13` (đủ 4/4 loại quà, dữ liệu thật account Giang tích luỹ theo thời gian), `TC_02.17` (danh sách lịch sử 5 record đủ điều kiện verify), `TC_02.11` (Expected Result được sửa lại khớp hành vi thật sau khi user xác nhận KHÔNG phải bug).

## Locator Coverage (tích luỹ)

| Pages visited | Elements captured | Verified ✅ | Inferred ⚠️ | Not found (expected) 🚫 |
|--------------|------------------|------------|-------------|-------------|
| 6 (Login, Host Cá nhân, FoxEco bottom-nav, FoxEco Cá nhân, Quà đã nhận, Đơn của tôi) | 29 | 27 | 2 | 2 (đúng kỳ vọng — không phải lỗi) |

→ implement-automation có thể bắt đầu ngay với 27 locator đã verified — chi tiết đầy đủ (theo round) trong `vibe-locators.md`.

## Failed TCs — Cần review TC hoặc fix app (tích luỹ, không đổi từ R1/R2/R3)

| TC ID | Expected | Actual | Ghi chú |
|-------|----------|--------|---------|
| TC_02.1 | Đủ 4 trường hồ sơ (tên, avatar, phòng ban, MNV) | Chỉ 3/4 trường — thiếu MNV | `BUG-003`/`FE-148` (Open, đã push Jira 2026-08-04), không đổi qua cả 3 round |
| TC_02.2 | "Phòng [ban] · MNV: [mã NV]" | Chỉ có phòng ban, thiếu MNV | Cùng root cause `BUG-003`/`FE-148` |
| TC_02.3 | Đủ 6 phần tử header, gồm badge tier "Hạng Đồng hành" | Thiếu MNV + thiếu badge tier — 2/6 phần tử | Cùng root cause `BUG-003`/`FE-148`, user xác nhận cả 2 đều là gap thật (không phải TC lỗi thời) |

## Blocked TCs — Thiếu dữ liệu dàn dựng (không phải lỗi app, tích luỹ cả 3 round)

| TC ID | Lý do |
|-------|-------|
| TC_02.7 | Không có account/dữ liệu STG nào ≥999 đơn/quà (cao nhất hiện có = 46 đơn toàn cộng đồng, 5 đơn cá nhân) |
| TC_02.14 | Không có dữ liệu 1 loại quà ≥12 (cao nhất hiện có = 2, Gấu bông) |

## Passed TCs — Sẵn sàng implement automation (12 TC tích luỹ)

| TC ID | Round chuyển Pass | Locators captured |
|-------|-------|-------------------|
| TC_02.4 | R1+R2 | — (verify text 2 chỉ số) |
| TC_02.5 | R1, re-confirm R3 | profile stat "0 đơn đã giúp"/"0 quà đã nhận" |
| TC_02.6 | R2 | — (boundary=1) |
| TC_02.8 | R1+R2 | `profile-menu-activity` |
| TC_02.9 | R1+R2 | `profile-menu-gifts` |
| TC_02.10 | R1+R2 | — (verify absence) |
| TC_02.11 | R3 (Expected sửa lại khớp thực tế, user xác nhận không phải bug) | empty-state title/subtitle/icon |
| TC_02.12 | R2 | card + list "Lịch sử nhận quà" |
| TC_02.13 | R3 (đủ 4/4 loại quà, dữ liệu thật account Giang) | card 4 loại quà (accessibility text nodes) |
| TC_02.15 | R1+R2 | `Quay lại` |
| TC_02.16 | R2 | `gifts-received-title` + list |
| TC_02.17 | R3 (danh sách lịch sử 5 record đủ điều kiện verify) | danh sách lịch sử nhận quà (text nodes) |

## Recommendation

- **Automate now:** 12 TC PASS — locators sẵn sàng trong `vibe-locators.md` (đặc biệt `profile-menu-activity`, `profile-menu-gifts`, `Quay lại`, `gifts-received-title` — accessibility id/id ổn định)
- **Đã có bug, chờ dev fix:** 3 TC (TC_02.1/02.2/02.3) — BUG-003/FE-148 (Open, đã push Jira từ 2026-08-04)
- **Chờ test data (không phải app bug):** 2 TC (TC_02.7, TC_02.14) — cần QA lead seed dữ liệu số lượng lớn trên STG

## Ghi chú khác

- Entry point FoxEco SDK: tab "Chức năng" (host app FoxPro) → tile "FoxEco" — **không phải** tile "FoxGrowth" (module điểm thưởng khác, dễ nhầm do cùng ở vị trí gần nhau trong list "Cá nhân" của host app).
- Login STG dùng OTP flow (không phải password cố định): nhập email → "NHẬN MÃ OTP" → nhập mã (`123QWE`, giá trị cố định môi trường STG, không phải OTP gửi email thật) → "ĐĂNG NHẬP".
- Round 1+2 (2026-08-04) chủ động dùng 2 account cố định theo round (TaiPM→Giang, không quay lại account gốc cuối run). Round 3 (2026-08-05) chủ động switch cả 2 chiều (Giang→TaiPM→Giang) để vừa phủ precondition vừa khôi phục môi trường gốc trước khi kết thúc.
- **TC_02.11 — cập nhật quan trọng 2026-08-05:** Empty-state title thật của màn "Quà đã nhận" là "Hiện tại chưa có dữ liệu" (đã xác nhận nhất quán qua cả Round 1 và Round 3, 2 ngày khác nhau). Ban đầu (R1) đánh giá đây là regression so với ảnh chụp thật STG (2026-07-31, ghi "Chưa có quà nào") và đề xuất log-bug. Ở Round 3, **user xác nhận trực tiếp đây KHÔNG phải bug — chấp nhận text hiện tại là đúng.** Đã sửa lại Expected Result của TC_02.11 (Excel + fragment) khớp hành vi thật, không tạo bug report. Xem `MEMORY.md` §6 `C-ORD-06` (nhánh GIFT) cho chi tiết đầy đủ.

## Excel & MEMORY updates

- TC-MASTER Excel: Round 1 (cột N-R) + Round 2 (cột S-W) đã ghi từ 2026-08-04. Round 3 (cột X-AB, 9 TC pending) ghi 2026-08-05 sau khi user xác nhận đóng LibreOffice (đang mở lúc bắt đầu run). Sau đó sửa thêm Expected Result (cột I) + DOC Source (cột C) của `TC_02.11` theo xác nhận không-phải-bug — đã recalc LibreOffice sạch (AO23 = Pass).
- **2026-08-05: Đã merge folder `VR-004-2026-08-04` (Round 1+2 gốc) vào folder này (`Profile_VR-007-2026-08-05`) theo yêu cầu user** — gộp đầy đủ 4 file (vibe-report/vibe-log/vibe-locators/mcp-session-log) + 5 screenshot Round 1+2 vào đây, sau đó đã xoá folder `VR-004-2026-08-04` gốc. Toàn bộ lịch sử 3 round giờ nằm trong 1 folder duy nhất.
