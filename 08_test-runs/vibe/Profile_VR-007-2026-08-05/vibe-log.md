# Vibe Test Log — Profile_VR-007-2026-08-05 (merged) — v1.0

> Module: **Cá nhân (TC_02)** — 17/17 TC trong sheet.
> Folder này gộp **Round 1 + Round 2** (chạy gốc trong `VR-004-2026-08-04`, đã xoá folder gốc sau khi
> merge — 2026-08-05) và **Round 3** (chạy trực tiếp trong folder này, 2026-08-05 — retest 9 TC pending
> từ Round 1+2).
> Account Round 1: `stag_TaiPM@fpt.com` (Phan Minh Tài, 0 đơn/0 quà) · Round 2: `stag_giangdc2@fpt.com`
> (Đặng Châu Giang, 1 đơn/1 quà) · Round 3: switch Giang (5 đơn/5 quà) ↔ TaiPM (0/0) tuỳ TC.

---

# ROUND 1 + ROUND 2 (2026-08-04 — gốc VR-004)

> Round 1 = stag_TaiPM@fpt.com (Phan Minh Tài) — data thực tế lúc test: 0 đơn đã giúp / 0 quà đã nhận
> Round 2 = stag_giangdc2@fpt.com (Đặng Châu Giang) — data thực tế lúc test: 1 đơn đã giúp / 1 quà đã nhận (1x Ly cà phê, từ Phạm Nguyễn Huy Tâm)
> Kết quả: **R1: 6 PASS/4 FAIL/7 BLOCKED · R2: 9 PASS/3 FAIL/5 BLOCKED**

## TC_02.1: Check xem hồ sơ cá nhân (view-only), đủ 6 trường, không có nút chỉnh sửa

| # | Step | Round 1 (taipm) | Round 2 (giangdc2) |
|---|------|------------------|---------------------|
| 1-2 | Mở app → bấm Cá nhân | ✅ vào đúng màn | ✅ vào đúng màn |
| 3 | Quan sát khu vực hồ sơ | ❌ chỉ thấy 3/6 trường: avatar, tên, phòng ban. **Thiếu SĐT, khu vực, kênh liên hệ** | ❌ giống Round 1 — chỉ 3/6 trường |
| 4 | Tìm nút Chỉnh sửa/Cập nhật | ✅ không có nút nào (đúng expected view-only) | ✅ không có nút nào |

**Result: ❌ FAIL (cả 2 round)** — Expected gốc yêu cầu đủ 6 trường (tên, SĐT, avatar, phòng ban, khu vực, kênh liên hệ) nhưng UI thật chỉ hiển thị 3 trường. Step 4 (view-only) đúng.
**[CẬP NHẬT 2026-08-04 — user xác nhận qua chat]:** SĐT/khu vực/kênh liên hệ KHÔNG phải gap thật (6-field list gốc trích BRD lỗi thời) — đã sửa Expected còn 4 trường (tên, avatar, phòng ban, MNV). Gap thật DUY NHẤT = thiếu MNV. Verdict vẫn FAIL, lý do hẹp lại. Xem `C-USR-04` (Open).
**Screenshot:** R1_TC_02.1-05_10_canhan_home.png / R2_TC_02.1-06_10_canhan_home.png

---

## TC_02.2: Check hiển thị đúng phòng ban + khu vực/tỉnh trên hồ sơ

| Round | Actual |
|-------|--------|
| R1 (taipm) | Chỉ hiện "Phòng Phát triển Phần mềm số 8". Không có khu vực/tỉnh riêng, không có định dạng "· MNV: ..." |
| R2 (giangdc2) | Chỉ hiện "Ban Giám đốc". Cùng vấn đề: thiếu khu vực/tỉnh, thiếu MNV |

**Result: ❌ FAIL (cả 2 round)** — thiếu định dạng MNV so với Expected.
**[CẬP NHẬT 2026-08-04]:** user xác nhận qua chat "khu vực/tỉnh" KHÔNG phải yêu cầu thật — đã sửa Title/Expected TC_02.2 thành "phòng ban + MNV" (khớp đúng ví dụ mẫu "Phòng Kỹ thuật · MNV: FTEL2291" vốn đã có sẵn). Gap thật = thiếu MNV. Xem `C-USR-04` (Open).

---

## TC_02.3: Check đầy đủ + đúng 6 phần tử hiển thị tại header màn Cá nhân

Expected: (1) avatar (2) tên (3) "Phòng [ban] · MNV: [mã NV]" (4) badge tier "🏆 Hạng Đồng hành" (5) 2 chỉ số (6) menu Đơn của tôi/Quà đã nhận

| Phần tử | R1 (taipm) | R2 (giangdc2) |
|---------|------------|----------------|
| (1) avatar | ✅ (initials "PM") | ✅ (initials "ĐC") |
| (2) tên | ✅ | ✅ |
| (3) "Phòng · MNV" | ⚠️ chỉ có "Phòng ...", KHÔNG có "· MNV: ..." | ⚠️ giống R1 |
| (4) badge tier | ❌ KHÔNG có | ❌ KHÔNG có |
| (5) 2 chỉ số | ✅ | ✅ |
| (6) 2 menu | ✅ (nằm ở card riêng bên dưới, không phải trong header cam) | ✅ |

**Result: ❌ FAIL (cả 2 round)** — thiếu (3) MNV + (4) badge tier.
**[CẬP NHẬT 2026-08-04 — user xác nhận qua chat]:** CẢ 2 phần tử thiếu (MNV + badge tier "Hạng Đồng hành") đều là **gap thật**, KHÔNG phải TC lỗi thời. Đánh giá ban đầu ("badge tier là TC drift vì mâu thuẫn C-USR-01") đã bị RÚT LẠI — `C-USR-01` chỉ cấm viết TC test logic phân hạng, không cấm hiển thị badge dạng tĩnh; badge NÊN xuất hiện. TC_02.3 giữ nguyên KHÔNG sửa (Expected đã đúng từ đầu). Đã mở `C-USR-04` (Open) cho cả 2 gap này, cần dev xác nhận trước khi `/log-bug`.

---

## TC_02.4: Check 2 chỉ số đóng góp, không hiện điểm ECO/tier/CO2

| Round | Actual |
|-------|--------|
| R1 (taipm) | "0 đơn đã giúp" / "0 quà đã nhận" — không có điểm ECO/CO2/tier nào khác |
| R2 (giangdc2) | "1 đơn đã giúp" / "1 quà đã nhận" — không có điểm ECO/CO2/tier nào khác |

**Result: ✅ PASS (cả 2 round)**

---

## TC_02.5: Check hiển thị đúng khi chỉ số = 0

| Round | Actual |
|-------|--------|
| R1 (taipm) | Data thực tế = 0/0, hiển thị đúng "0 đơn đã giúp"/"0 quà đã nhận", số 0 rõ ràng, không ẩn/gạch ngang |
| R2 (giangdc2) | Data thực tế = 1/1 — **precondition "chưa từng giúp đơn/nhận quà" KHÔNG thoả** với account này |

**Result: R1 ✅ PASS · R2 🚫 BLOCKED** (data account không đáp ứng precondition =0; đã verify đủ ở R1)

---

## TC_02.6: Check hiển thị đúng khi chỉ số = 1 (boundary)

| Round | Actual |
|-------|--------|
| R1 (taipm) | Data = 0/0 — precondition "đúng 1 đơn/1 quà" KHÔNG thoả |
| R2 (giangdc2) | Data thực tế = 1/1 (khớp chính xác boundary=1). Hiển thị "1 đơn đã giúp"/"1 quà đã nhận" đúng |

**Result: R1 🚫 BLOCKED · R2 ✅ PASS**

---

## TC_02.7: Check số liệu lớn (≥999) không cắt/tràn UI

**Result: 🚫 BLOCKED (cả 2 round)** — không có tài khoản STG nào có ≥999 đơn/quà, không dàn dựng được qua UI/vibe-test. Cần QA lead chuẩn bị dữ liệu test riêng hoặc seed DB.

---

## TC_02.8: Check menu "Đơn của tôi" điều hướng sang Hoạt động

| Round | Actual |
|-------|--------|
| R1 | Tap `profile-menu-activity` → điều hướng đúng sang màn "Đơn của tôi" (list đơn, tab Đang diễn ra/Đã hoàn thành) |
| R2 | Tương tự, điều hướng đúng, hiện đơn thật "Nhận giao hàng Thuận đường" |

**Result: ✅ PASS (cả 2 round)**
**Locator:** accessibility id `profile-menu-activity`

---

## TC_02.9: Check menu "Quà đã nhận" điều hướng sang màn Quà đã nhận

| Round | Actual |
|-------|--------|
| R1 | Tap `profile-menu-gifts` → điều hướng đúng, màn riêng có header + nút back |
| R2 | Tương tự, điều hướng đúng |

**Result: ✅ PASS (cả 2 round)**
**Locator:** accessibility id `profile-menu-gifts`

---

## TC_02.10: Check GAP — không có UI cấu hình kênh liên hệ

Quét toàn bộ page source (MCP `appium_get_page_source`) màn Cá nhân cả 2 round: không có bất kỳ text/toggle nào liên quan "kênh liên hệ"/"Workplace"/"email".

**Result: ✅ PASS (cả 2 round)**

---

## TC_02.11: Check màn "Quà đã nhận" rỗng khi chưa nhận quà nào

Expected (tại thời điểm R1): icon hộp quà + title **"Chưa có quà nào"** + subtitle "Quà bạn nhận được từ đồng nghiệp sẽ hiện ở đây"

| Round | Actual |
|-------|--------|
| R1 (taipm, 0 quà) | Icon hộp quà ✅. Title thực tế = **"Hiện tại chưa có dữ liệu"** (❌ khác Expected lúc đó). Subtitle = "Quà bạn nhận được từ đồng nghiệp sẽ hiện ở đây" ✅ khớp |
| R2 (giangdc2) | Account có 1 quà → không rỗng, không thể verify empty state |

**Result (tại thời điểm R1): R1 ❌ FAIL (title text sai) · R2 🚫 BLOCKED (data không rỗng)**
**⚠️ Đáng chú ý (lúc đó):** MASTER-MEMORY §Update 2026-07-31 đã ghi nhận ảnh chụp THẬT app STG xác nhận text chính thức "Chưa có quà nào" cho màn Quà đã nhận — nhưng build STG hiện tại (lúc vibe-test 2026-08-04) lại hiển thị text generic "Hiện tại chưa có dữ liệu". Đã đề xuất log bug + báo dev kiểm tra lại text empty-state.
**[CẬP NHẬT 2026-08-05, Round 3]:** user xác nhận trực tiếp text "Hiện tại chưa có dữ liệu" là ĐÚNG, KHÔNG phải bug/regression — đã sửa lại Expected Result khớp thực tế. Verdict R1 giữ nguyên lịch sử (đúng theo spec tại thời điểm test), xem chi tiết verdict cuối cùng ở phần ROUND 3 bên dưới.
**Screenshot:** R1_TC_02.9_11_quadanhan_empty.png

---

## TC_02.12: Check card "Quà đã nhận" chỉ load đúng loại đã nhận

Precondition cần: đã nhận ≥1 quà nhưng không đủ 4 loại.

| Round | Actual |
|-------|--------|
| R1 (0 quà) | Không thoả precondition |
| R2 (1x Ly cà phê) | Card CHỈ hiện "☕ Ly cà phê — 1", không hiện 3 loại còn lại (hoa/gấu bông/vương miện). Bên dưới "LỊCH SỬ NHẬN QUÀ": "Ly cà phê · Phạm Nguyễn Huy Tâm · Hôm nay · 11:21" |

**Result: R1 🚫 BLOCKED · R2 ✅ PASS**
**Screenshot:** R2_TC_02.12_16_17_quadanhan_withdata.png

---

## TC_02.13: Check đủ 4/4 loại quà khi đã nhận đủ tất cả

**Result: 🚫 BLOCKED (cả 2 round)** — không có tài khoản STG nào có đủ 4 loại quà (hoa/cà phê/gấu bông/vương miện), không dàn dựng được qua UI.

---

## TC_02.14: Check số lượng lớn của 1 loại quà (≥12) không cắt/tràn UI

**Result: 🚫 BLOCKED (cả 2 round)** — account nhiều nhất chỉ có 1 quà, không có data ≥12.

---

## TC_02.15: Check icon quay lại tại màn "Quà đã nhận"

| Round | Actual |
|-------|--------|
| R1 | Tap back (content-desc "Quay lại") → quay đúng về Cá nhân |
| R2 | Tương tự, quay đúng về Cá nhân |

**Result: ✅ PASS (cả 2 round)**
**Locator:** accessibility id `Quay lại`

---

## TC_02.16: Check đủ 3 thành phần màn "Quà đã nhận" (trạng thái có dữ liệu)

| Round | Actual |
|-------|--------|
| R1 (0 quà) | Không thoả precondition (màn đang ở trạng thái rỗng) |
| R2 (1 quà) | Đủ 3 thành phần: (1) icon quay lại header ✅ (2) card đếm số theo loại (chỉ "Ly cà phê") ✅ (3) danh sách lịch sử ✅ |

**Result: R1 🚫 BLOCKED · R2 ✅ PASS**

---

## TC_02.17: Check danh sách lịch sử nhận quà hiển thị đúng các lần đã nhận

Precondition cần ≥2 quà từ ≥2 đơn khác nhau để verify "không thiếu, không trùng lặp".

| Round | Actual |
|-------|--------|
| R1 (0 quà) | Không thoả |
| R2 (1 quà) | Danh sách hiện đúng 1/1 record khớp dữ liệu thật (Ly cà phê · Phạm Nguyễn Huy Tâm · 11:21), nhưng chỉ có 1 item nên **chưa đủ dữ liệu để verify đầy đủ ý đồ TC** (multi-item, dedup, nhiều người tặng) |

**Result: 🚫 BLOCKED (cả 2 round)** — cần QA lead dàn dựng ≥2 record từ ≥2 người tặng khác nhau để test đầy đủ. (Xem verdict cuối ở Round 3 — đã đủ data.)

---

### Tổng kết Round 1 + 2

| Round | PASS | FAIL | BLOCKED |
|-------|------|------|---------|
| R1 (stag_TaiPM@fpt.com) | 6 | 4 | 7 |
| R2 (stag_giangdc2@fpt.com) | 9 | 3 | 5 |

---

# ROUND 3 (2026-08-05 — Profile_VR-007, retest 9 TC pending từ Round 1+2)

> Account chính: `stag_giangdc2@fpt.com` (Đặng Châu Giang, 5 đơn/5 quà)
> Account phụ (switch để phủ precondition "0 đơn/0 quà"): `stag_TaiPM@fpt.com` (Phan Minh Tài, 0 đơn/0 quà)

## TC_02.1: Check xem hồ sơ cá nhân (view-only), đủ 4 trường, không có nút chỉnh sửa

| # | Step | Action | Result | Notes |
|---|------|--------|--------|-------|
| 1 | Mở app FoxEco | (đã sẵn ở SDK) | ✅ PASS | — |
| 2 | Bấm "Cá nhân" tại bottom nav | tap(accessibility id "Cá nhân") | ✅ PASS | — |
| 3 | Quan sát khu vực hồ sơ | get_page_source | ❌ FAIL | Chỉ có 3/4 trường: tên "Đặng Châu Giang" ✅, avatar "ĐC" ✅, phòng ban "Ban Giám đốc" ✅ nhưng **KHÔNG có MNV** (mã nhân viên) |
| 4 | Tìm nút "Chỉnh sửa"/"Cập nhật" | find_element textContains("Chỉnh sửa") | ✅ PASS | 🚫 NOT FOUND đúng kỳ vọng — không có nút edit nào |

**Result: ❌ FAIL** (thiếu MNV ở step 3) — trùng khớp **BUG-003 / FE-148** (đã Open từ Round 1, R1/R2 cũng Fail)
**Screenshot:** TC_02.1_final.png
**ID Bugs:** BUG-003 (FE-148)

---

## TC_02.2: Check hiển thị đúng phòng ban + MNV trên hồ sơ

| # | Step | Action | Result | Notes |
|---|------|--------|--------|-------|
| 1-2 | Mở app, vào Cá nhân | (đã ở màn) | ✅ PASS | — |
| 3 | Quan sát trường phòng ban + MNV | page_source text nodes | ❌ FAIL | Hiển thị "Ban Giám đốc" — KHÔNG đúng định dạng "Phòng [ban] · MNV: [mã NV]", thiếu hẳn phần "· MNV: ..." |

**Result: ❌ FAIL** — cùng root cause BUG-003/FE-148
**Screenshot:** TC_02.1_final.png (cùng màn với TC_02.1)
**ID Bugs:** BUG-003 (FE-148)

---

## TC_02.3: Check đầy đủ + đúng 6 phần tử hiển thị tại header màn Cá nhân

| # | Step | Action | Result | Notes |
|---|------|--------|--------|-------|
| 1-2 | Mở app, vào Cá nhân | (đã ở màn) | ✅ PASS | — |
| 3 | Quan sát toàn bộ header cam | page_source + screenshot | ❌ FAIL | (1) avatar ✅ (2) tên ✅ (3) "Phòng...·MNV" ❌ THIẾU MNV (4) badge tier "🏆 Hạng Đồng hành" ❌ KHÔNG có (5) 2 chỉ số ✅ (6) menu 2 mục ✅ — thiếu 2/6 phần tử |

**Result: ❌ FAIL** (2/6 phần tử thiếu) — cùng BUG-003/FE-148 (đã gộp 2 phần MNV + badge tier)
**Screenshot:** TC_02.1_final.png
**ID Bugs:** BUG-003 (FE-148)

---

## TC_02.5: Check hiển thị đúng khi chỉ số đóng góp = 0

**Precondition cần:** tài khoản CHƯA từng giúp đơn / CHƯA từng nhận quà (0/0). Account chính (Giang) đang có 5/5 → không thoả. **Chủ động switch sang account `stag_TaiPM@fpt.com`** (Phan Minh Tài) — logout host app → login OTP → xác nhận có đúng data 0/0.

| # | Step | Action | Result | Notes |
|---|------|--------|--------|-------|
| 1-2 | Mở app (account TaiPM), vào Cá nhân | login flow + tap Cá nhân | ✅ PASS | — |
| 3 | Quan sát 2 chỉ số tại header | screenshot + page_source | ✅ PASS | Hiển thị đúng **"0 đơn đã giúp"** và **"0 quà đã nhận"** — số 0 rõ ràng, KHÔNG ẩn/không thay bằng gạch ngang |

**Result: ✅ PASS**
**Screenshot:** TC_02.5_final.png
**Account dùng:** stag_TaiPM@fpt.com (Phan Minh Tài)

---

## TC_02.7: Check hiển thị số liệu lớn tại chỉ số đóng góp không bị cắt/tràn UI

**Precondition cần:** tài khoản có ≥999 đơn/quà. Không có account nào trên STG đạt ngưỡng này (Giang=5, TaiPM=0; cộng đồng FoxEco toàn hệ thống chỉ 46 đơn).

**Result: 🚫 BLOCKED** — không dàn dựng được dữ liệu qua UI/vibe-test, cần QA lead chuẩn bị tài khoản test riêng hoặc seed DB. (Trùng lý do BLOCKED của R1/R2.)

---

## TC_02.11: Check màn "Quà đã nhận" rỗng khi chưa nhận quà nào

**Precondition:** account TaiPM (0 quà) — dùng luôn state từ TC_02.5.

| # | Step | Action | Result | Notes |
|---|------|--------|--------|-------|
| 1-2 | Vào Cá nhân → "Quà đã nhận" | tap(accessibility id "profile-menu-gifts") | ✅ PASS | — |
| 3 | Quan sát nội dung màn | screenshot + page_source | ✅ PASS | Icon hộp quà ✅ đúng. Subtitle "Quà bạn nhận được từ đồng nghiệp sẽ hiện ở đây" ✅ đúng. Title thực tế = **"Hiện tại chưa có dữ liệu"** — user xác nhận đây KHÔNG phải bug, chấp nhận đúng như hiện tại |

**Result: ✅ PASS** — Expected Result đã sửa lại khớp hành vi thực tế ("Hiện tại chưa có dữ liệu" thay cho "Chưa có quà nào"). Ghi chú: R1 (2026-08-04) từng ghi FAIL dưới Expected cũ — giữ nguyên lịch sử round đó (đúng theo spec tại thời điểm), không rewrite.
**Screenshot:** TC_02.11_final.png

---

## TC_02.13: Check card "Quà đã nhận" hiển thị đủ cả 4/4 loại khi đã nhận đủ tất cả

**Account:** Giang (5 quà, đủ cả 4 loại theo dữ liệu thực tế)

| # | Step | Action | Result | Notes |
|---|------|--------|--------|-------|
| 1-2 | Vào Cá nhân → "Quà đã nhận" | tap profile-menu-gifts | ✅ PASS | — |
| 3 | Quan sát card đếm số | screenshot + page_source | ✅ PASS | "Tổng quà đã nhận: 5 món" — đủ 4/4 loại: 🌷 Bông hoa=1, ☕ Ly cà phê=1, 🧸 Gấu bông=2, 👑 Vương miện=1 — không loại nào bị ẩn |

**Result: ✅ PASS**
**Screenshot:** TC_02.13_final.png

---

## TC_02.14: Check số lượng lớn của 1 loại quà (≥12) không bị cắt/tràn UI

**Precondition cần:** ≥12 lần nhận 1 loại quà. Dữ liệu thực tế cao nhất hiện có = 2 (Gấu bông, account Giang). Không có account/dữ liệu nào đạt ngưỡng ≥12.

**Result: 🚫 BLOCKED** — không dàn dựng được qua UI/vibe-test, cần seed DB riêng. (Trùng lý do BLOCKED của R1/R2.)

---

## TC_02.17: Check danh sách lịch sử nhận quà hiển thị đúng các lần đã nhận

**Account:** Giang (5 quà từ 5 lần nhận riêng biệt, cùng người tặng "Phạm Nguyễn Huy Tâm" nhưng khác loại quà + thời điểm)

| # | Step | Action | Result | Notes |
|---|------|--------|--------|-------|
| 1-3 | Vào Cá nhân → "Quà đã nhận" → quan sát lịch sử | screenshot + page_source | ✅ PASS | Danh sách "LỊCH SỬ NHẬN QUÀ" liệt kê đủ 5 dòng, mỗi dòng có tên quà + người tặng + mốc thời gian riêng biệt (Bông hoa "Hôm nay 13:55", Gấu bông "Hôm nay 10:22", Gấu bông "Hôm qua 18:20", Vương miện "Hôm qua 13:55", Ly cà phê "Hôm qua 11:21") — khớp với tổng 5 món ở card phía trên, không trùng lặp |

**Result: ✅ PASS**
**Screenshot:** TC_02.17_final.png

---

### Tổng kết Round 3 (9 TC)

| Result | TCs |
|--------|-----|
| ✅ PASS | TC_02.5, TC_02.11 (Expected sửa lại khớp thực tế, user xác nhận không phải bug), TC_02.13, TC_02.17 (4) |
| ❌ FAIL | TC_02.1, TC_02.2, TC_02.3 (→ BUG-003/FE-148) (3) |
| 🚫 BLOCKED | TC_02.7, TC_02.14 (thiếu test data ≥999 / ≥12) (2) |

---

## Tổng kết tích luỹ toàn bộ (17/17 TC, sau 3 round)

| Result | TCs | Count |
|--------|-----|-------|
| ✅ PASS | TC_02.4, .5, .6, .8, .9, .10, .11, .12, .13, .15, .16, .17 | 12 |
| ❌ FAIL | TC_02.1, .2, .3 (BUG-003/FE-148, Open) | 3 |
| 🚫 BLOCKED | TC_02.7, .14 (thiếu test data ≥999 / ≥12 trên STG) | 2 |

17/17 TC đã chạy ít nhất 1 lần — phần còn "chưa Pass" đều có lý do rõ ràng (bug thật đã log, hoặc thiếu test data cần QA lead seed riêng), không phải chưa test.
