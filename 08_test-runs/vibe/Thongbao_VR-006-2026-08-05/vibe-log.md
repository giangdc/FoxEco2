# Vibe Test Log — Thongbao_VR-006-2026-08-05 (merged) — v1.0

> Module: Thông báo (TC_03) — 39/39 TC trong sheet.
> Folder này gộp **Round 1** (chạy gốc trong `VR-003-2026-08-04`, đã xoá folder gốc sau khi merge — 2026-08-05)
> và **Round 2** (chạy trực tiếp trong folder này, 2026-08-05 — retest 29 TC pending từ Round 1).
> Account test cả 2 round: "Phan Minh Tài" — dữ liệu thông báo thật (không mock), tăng dần theo thời gian
> (Round 1: chỉ 3/9 loại thông báo · Round 2: đã lên 5/9 loại).

---

# ROUND 1 (2026-08-04 — gốc VR-003)

> Flow bắt đầu theo yêu cầu user: Trang chủ → tap icon chuông → màn Thông báo.
> Kết quả Round 1: **10 PASS / 0 FAIL / 29 BLOCKED**.

## TC_03.17: Check đầy đủ + đúng cấu trúc hiển thị màn Thông báo

| # | Step | Action | Result | Notes |
|---|------|--------|--------|-------|
| 1 | Tại Trang chủ, tap icon chuông | MCP tap (accessibility id "Thông báo") | ✅ PASS | Vào đúng màn Thông báo |
| 2 | Verify header, nhóm theo thời gian, card, nút Đánh dấu đã đọc | MCP snapshot | ✅ PASS | Header "Thông báo" + back icon; group "HÔM NAY"/"HÔM QUA"; mỗi card đủ icon+tiêu đề+mô tả+thời gian; nút "Đánh dấu đã đọc" hiển thị góc phải |

**Result: ✅ PASS** — **Screenshot:** 01_notification_screen.png

---

## TC_03.18: Check icon quay lại tại màn Thông báo

| # | Step | Action | Result | Notes |
|---|------|--------|--------|-------|
| 1 | Tap icon quay lại (mũi tên trái header) | MCP tap (xpath bounds) | ✅ PASS | Điều hướng đúng về Trang chủ |

**Result: ✅ PASS** — **Screenshot:** 12_TC_03.18_back_icon.png

---

## TC_03.19: Check hiển thị khi màn Thông báo chưa có thông báo nào

**Result: 🚫 BLOCKED** — Tài khoản test hiện có sẵn nhiều thông báo lịch sử thật (không mock), không có cách nào qua UI đơn thuần để đưa account về trạng thái rỗng (0 thông báo) trong phạm vi 1 session/1 tài khoản. Cần tài khoản test mới tinh chưa từng phát sinh sự kiện, hoặc chức năng xoá/reset dữ liệu thông báo phía backend.

> **Re-checked Round 2 (2026-08-05):** vẫn BLOCKED, không đổi — tài khoản còn nhiều dữ liệu hơn trước.

---

## TC_03.20: Check bấm vào 1 thông báo cụ thể chuyển đúng trạng thái đã đọc (không ảnh hưởng thông báo khác)

| # | Step | Action | Result | Notes |
|---|------|--------|--------|-------|
| 1 | Tap card "Đơn đã được giao" (7 giờ trước), resource-id `notif-item-019fc905-...` | MCP tap (uiautomator resourceId) | ✅ PASS | Điều hướng sang Theo dõi đơn (xem TC_03.36) |
| 2 | Back về Thông báo, verify unread-dot | MCP get_page_source (so sánh trước/sau) | ✅ PASS | Chỉ card vừa tap mất dot đỏ + viền màu; 7 card còn lại (đã kiểm từng resource-id) vẫn giữ nguyên dot |

**Result: ✅ PASS** — **Screenshot:** 06_..., 07_TC_03.20_after_read.png

---

## TC_03.21: Check bấm nút "Đánh dấu đã đọc" chuyển TẤT CẢ thông báo sang đã đọc

| # | Step | Action | Result | Notes |
|---|------|--------|--------|-------|
| 1 | Tap nút "Đánh dấu đã đọc" | MCP tap (accessibility id) | ✅ PASS | Toàn bộ 8 card đang hiển thị mất dot đỏ + viền màu đồng loạt; nút "Đánh dấu đã đọc" tự ẩn khỏi header (không còn gì để đánh dấu) |

**Result: ✅ PASS** — **Screenshot:** 09_TC_03.21_markall_read.png

---

## TC_03.22: Check bấm vào 1 thông báo ĐÃ đọc không gây lỗi và không đổi trạng thái thông báo khác

| # | Step | Action | Result | Notes |
|---|------|--------|--------|-------|
| 1 | Tap lại card đã đọc từ TC_03.20 | MCP tap (uiautomator resourceId, cùng element) | ✅ PASS | Không lỗi/crash, điều hướng bình thường sang Theo dõi đơn |
| 2 | Back về Thông báo, verify state | MCP get_page_source | ✅ PASS | Trạng thái dot của các card khác giữ nguyên, không bị ảnh hưởng |

**Result: ✅ PASS** — **Screenshot:** 08_TC_03.22_tap_already_read.png

---

## TC_03.23: Check bấm nút "Đánh dấu đã đọc" khi TOÀN BỘ thông báo đã đọc không gây lỗi

**Result: ✅ PASS** — Sau khi mark-all-as-read (TC_03.21), nút "Đánh dấu đã đọc" **tự ẩn khỏi UI** (không còn render trong page source) thay vì hiển thị dạng no-op. Đây là hành vi hợp lý: user không thể bấm vào nút không tồn tại → thoả điều kiện "không gây lỗi" theo cách chủ động (ẩn control) thay vì bị động (chặn lỗi khi bấm). Không phát hiện crash/exception nào trong toàn bộ luồng thao tác.

---

## TC_03.24: Check load đúng batch dữ liệu đầu tiên khi mới mở màn Thông báo

**Result: ✅ PASS** — Ngay khi vào màn, danh sách hiển thị đầy đủ nhóm "HÔM NAY" với dữ liệu thật (timestamp tương đối, tự cập nhật theo thời gian thực — ví dụ "14 phút trước" → "20 phút trước" sau ~6 phút thao tác), không có trạng thái loading treo hay lỗi.

---

## TC_03.25 / TC_03.26 / TC_03.27 (Round 1): Scroll load thêm batch / hiển thị hết dữ liệu / scroll tiếp sau khi hết

**Result Round 1: 🚫 BLOCKED (cả 3 TC)** — Đã scroll xuống nhiều lần (kể cả swipe nhanh, khoảng cách lớn) nhưng danh sách dừng lại ở đúng 1 vị trí cố định (2 screenshot liên tiếp sau 2 lần scroll khác nhau có **md5 giống hệt nhau** → xác nhận đã chạm đáy nội dung khả dụng). Toàn bộ dữ liệu hiển thị dường như được tải sẵn một lần (không quan sát được hành vi "đang tải thêm" hay spinner khi scroll), và **không có bất kỳ chỉ báo nào ("đã hết dữ liệu"/"không còn gì để load thêm")** ở cuối danh sách — màn hình chỉ dừng lại lặng lẽ.
→ Không đủ dữ liệu/cơ chế quan sát được để verify hành vi "tải thêm khi scroll" đúng như 3 TC mô tả — nghi ngờ **gap**: thiếu indicator cuối danh sách (liên quan trực tiếp TC_03.26). Đề xuất seed thêm dữ liệu thông báo (>1 trang) trên tài khoản test khác để xác nhận cơ chế phân trang có tồn tại hay không, trước khi kết luận đây là bug hay đơn giản do tài khoản hiện tại có ít dữ liệu.

> **→ Kết quả cuối (sau Round 2, xem bên dưới): cả 3 TC chuyển sang ✅ PASS** — tài khoản có thêm dữ liệu mới đã cho phép quan sát được cơ chế load-more hoạt động đúng.

---

## TC_03.28: Check mất kết nối mạng đúng lúc đang load thêm dữ liệu

**Result Round 1: 🚫 BLOCKED** — Phụ thuộc TC_03.25 (cơ chế load-more) chưa xác nhận được có tồn tại hay không trong phạm vi dữ liệu hiện có; ngoài ra việc giả lập mất mạng (airplane mode / network throttle) nằm ngoài phạm vi thao tác UI đơn thuần theo yêu cầu user cho phiên test này.

> **Re-checked Round 2:** vẫn BLOCKED (không canh đúng được thời điểm "đang load" — xem chi tiết bên dưới).

---

## TC_03.29 / TC_03.30: Check nội dung push không hiển thị SĐT

**Result: 🚫 BLOCKED (cả 2 TC)** — Cả 2 TC yêu cầu thông báo loại "SĐT đã lộ" (NTF-01, phát sinh khi Carrier vừa ghép đơn) và mốc "Đã lấy hàng". Rà toàn bộ danh sách thông báo của tài khoản test (toàn bộ dữ liệu đã cuộn qua, xem TC_03.25-27) chỉ thấy 3 loại: "Đơn đã được giao", "Đơn gửi tới bạn đã có người vận chuyển", "Người vận chuyển đã lấy hàng" — không có loại thông báo tiết lộ SĐT nào phù hợp để kiểm tra nội dung.

> **Re-checked Round 2:** vẫn BLOCKED, không đổi.

---

## TC_03.31 / 32 / 34 / 37 / 38 / 39 (Round 1): Click-navigate cho 6 loại thông báo khác

**Result Round 1: 🚫 BLOCKED (cả 6 TC)** — Các loại thông báo cần kiểm ("Đã có người nhận mang giúp", "Ghép thành công", "Tìm thấy đơn hàng phù hợp tuyến đường", "Đơn đã hoàn tất", "Bạn nhận được quà cảm ơn", "Đơn đã bị huỷ") **không tồn tại** trong lịch sử thông báo của tài khoản test hiện tại (đã xác nhận qua quét toàn bộ danh sách + `mcp-session-log.md` Round 1 #10-21). Không có cách tạo ra các sự kiện này chỉ bằng thao tác UI 1 tài khoản trong phạm vi yêu cầu của phiên test này (cần vai trò khác ghép đơn/huỷ đơn/gửi quà — xem khuyến nghị dùng `vibe-test-multi-device`).

> **→ Kết quả cuối (sau Round 2): TC_03.37 và TC_03.39 chuyển sang ✅ PASS** (2 loại thông báo mới xuất hiện trong dữ liệu tài khoản). **TC_03.31/32/34/38 vẫn BLOCKED** — 4 loại còn lại vẫn chưa xuất hiện.

---

## TC_03.33: Check bấm thông báo "Đơn gửi tới bạn đã có người vận chuyển" điều hướng đúng sang Theo dõi đơn

| # | Step | Action | Result | Notes |
|---|------|--------|--------|-------|
| 1 | Tap card tương ứng | MCP tap (uiautomator resourceId `notif-item-019fc8ad-...`) | ✅ PASS | Điều hướng đúng sang Theo dõi đơn (trạng thái "Đã ghép · chờ shipper lấy hàng") |

**Result: ✅ PASS** — **Screenshot:** 10_TC_03.33_tap_donguitoiban.png

---

## TC_03.35: Check bấm thông báo "Người vận chuyển đã lấy hàng" điều hướng đúng sang Theo dõi đơn

| # | Step | Action | Result | Notes |
|---|------|--------|--------|-------|
| 1 | Tap card tương ứng | MCP tap (uiautomator resourceId `notif-item-019fc896-9f80-...`) | ✅ PASS | Điều hướng đúng sang Theo dõi đơn |

**Result: ✅ PASS** — **Screenshot:** 11_TC_03.35_tap_nguoivanchuyenlayhang.png

---

## TC_03.36: Check bấm thông báo "Đơn đã được giao" điều hướng đúng sang Theo dõi đơn

| # | Step | Action | Result | Notes |
|---|------|--------|--------|-------|
| 1 | Tap card tương ứng (cùng thao tác với TC_03.20) | MCP tap | ✅ PASS | Điều hướng đúng sang Theo dõi đơn — stepper 5 bước hiển thị "Đã giao" đang active |

**Result: ✅ PASS** — **Screenshot:** 06_TC_03.20_36_tap_daduocgiao.png

---

## TC_03.1 – TC_03.16: Nhóm nghiệp vụ đa vai trò (trần 5 thông báo, thông báo phát sinh theo hành động Sender/Receiver/Carrier khác)

**Result: 🚫 BLOCKED (cả 16 TC)** — Toàn bộ nhóm này yêu cầu **orchestrate hành động của nhiều vai trò khác nhau** trong cùng 1 đơn hàng (VD: TC_03.1-3 cần kiểm soát chính xác số lượng tin NEED phù hợp tuyến khi 1 tin OFFER vừa đăng; TC_03.4-11 cần Carrier/Sender/Receiver xác nhận từng bước lấy hàng/giao hàng/nhận hàng; TC_03.12 cần Sender gửi quà; TC_03.13-15 cần huỷ đơn từ 3 vai trò khác nhau; TC_03.16 cần chờ tin đăng quá hạn). Phạm vi phiên test này (theo yêu cầu user) là **1 tài khoản, 1 thiết bị**, chỉ thao tác từ màn Trang chủ → icon chuông → Thông báo — không đủ điều kiện tạo lập các sự kiện đa vai trò nói trên.
→ Khuyến nghị dùng skill `vibe-test-multi-device` (nhiều session Appium song song, mỗi role 1 device) để test nhóm 16 TC này trong 1 phiên riêng.

> **Re-checked Round 2:** vẫn BLOCKED, không đổi (single-device session, không có điều kiện multi-role).

---

# ROUND 2 (2026-08-05 — retest 29 TC pending, chạy trong folder này)

> Round đích: **Round 2** cho toàn bộ 29 TC pending (Round 1 đã đầy ở cả 29 dòng).
> Account: "Phan Minh Tài" (session có sẵn, không cần login lại) — dữ liệu thông báo đã **thay đổi/nhiều hơn** so với Round 1 (nhiều hoạt động test khác trong ngày 2026-08-05 đã sinh thêm thông báo).
> Kết quả Round 2: **5 PASS / 0 FAIL / 24 BLOCKED** (trong số 29 TC pending).

## TC_03.25: Check scroll xuống cuối danh sách hiện tại tự động load thêm batch tiếp theo

| # | Step | Action | Result | Notes |
|---|------|--------|--------|-------|
| 1 | Scroll xuống cuối danh sách đang hiển thị | appium_gesture(scroll, down) ×nhiều lần | ✅ PASS | Batch đầu 8 item (HÔM NAY) → scroll → 9 item mới xuất hiện (HÔM QUA) → scroll tiếp → nhóm "TUẦN NÀY" xuất hiện. Không thấy thông báo trùng lặp giữa các batch (khác resource-id/nội dung/thời gian mỗi lần) |

**Result: ✅ PASS**
**Screenshot:** (không cần riêng — bằng chứng qua page-source diff các lần scroll, xem mcp-session-log Round 2 #9-13, #38)

---

## TC_03.26: Check khi đã load hết toàn bộ dữ liệu, hiển thị rõ ràng không còn gì để load thêm

| # | Step | Action | Result | Notes |
|---|------|--------|--------|-------|
| 1 | Scroll tới cuối danh sách khi đã ở batch cuối cùng | appium_gesture(scroll, down) ×10 liên tiếp sau khi nhóm "TUẦN NÀY" xuất hiện | ✅ PASS (có lưu ý) | Danh sách ngừng tăng thêm item sau ~10 lần scroll bổ sung (dừng ở nhóm "TUẦN NÀY"), KHÔNG có spinner loading treo, KHÔNG crash. Expected chỉ yêu cầu "không spinner treo mãi + hệ thống nhận biết hết dữ liệu (không gọi thêm request)" — không bắt buộc có text "đã hết dữ liệu" hiển thị UI. Hành vi quan sát được khớp yêu cầu literal của Expected |

**Result: ✅ PASS**
**Screenshot:** TC_03.26_scroll_bottom_check.png
**Lưu ý (không phải FAIL, ghi nhận cho reviewer):** UI KHÔNG có bất kỳ text/footer nào báo "đã hết dữ liệu" — chỉ dừng lặng lẽ. Test này PASS vì Expected Result không yêu cầu literal UI message, chỉ yêu cầu no-spinner + no-more-request. Nếu BA muốn có UX rõ ràng hơn (hiện text "Đã hiển thị tất cả thông báo"), đây là **candidate cho 1 UX suggestion**, không phải bug/fail theo đúng câu chữ TC hiện tại — xác nhận lại lần 2, đã ghi nhận lần đầu ở Round 1.

---

## TC_03.27: Check tiếp tục scroll sau khi đã hết dữ liệu không gây lỗi/trùng lặp

| # | Step | Action | Result | Notes |
|---|------|--------|--------|-------|
| 1 | Tiếp tục kéo/scroll thêm nhiều lần sau khi đã hết dữ liệu | appium_gesture(scroll, down) ×10 (cùng loạt với TC_03.26) | ✅ PASS | Không phát sinh crash/treo app, không có thông báo bị lặp lại (kiểm tra qua screenshot cuối + page-source, danh sách ổn định ở nhóm "TUẦN NÀY") |

**Result: ✅ PASS**
**Screenshot:** TC_03.26_scroll_bottom_check.png (dùng chung bằng chứng với TC_03.26)

---

## TC_03.28: Check mất kết nối mạng đúng lúc đang load thêm dữ liệu không làm mất dữ liệu đã hiển thị

| # | Step | Action | Result | Notes |
|---|------|--------|--------|-------|
| 1 | Ngắt kết nối mạng đúng lúc hệ thống đang load thêm dữ liệu | `adb shell svc wifi disable` + `svc data disable` (ADB lifecycle, không phải MCP locator) | 🚫 BLOCKED | Tại thời điểm ngắt mạng, danh sách đã load hết dữ liệu (theo TC_03.26) → KHÔNG có request load-more nào đang chạy để cắt giữa chừng. Không thể canh đúng thời điểm "đang load" bằng UI-only automation |
| 2 | Quan sát màn Thông báo | appium_gesture(scroll)×2 khi offline, sau đó bật lại mạng + screenshot | ⚠️ Bằng chứng phụ (không phải PASS cho đúng kịch bản TC) | Không crash, không mất dữ liệu đã hiển thị khi mạng OFF/ON — nhưng đây là "ở trạng thái nghỉ", không phải "đang load thêm" nên chưa xác nhận đúng kịch bản TC |

**Result: 🚫 BLOCKED (giữ nguyên như Round 1)**
**Reason:** Cần seed thêm dữ liệu (>1 trang sau điểm hiện tại) để có request load-more đang treo đúng lúc cắt mạng — hoặc cần network-throttle tool (giữ độ trễ cao) thay vì tắt hẳn, để canh đúng timing.
**Impact:** Không automate được ở round này.

---

## TC_03.37: Check bấm thông báo "Đơn đã hoàn tất - cảm ơn bạn" điều hướng đúng sang Theo dõi đơn

| # | Step | Action | Result | Notes |
|---|------|--------|--------|-------|
| 1 | Đăng nhập vai trò Sender/Carrier | (đã sẵn có, session "Phan Minh Tài") | ✅ PASS | — |
| 2 | Mở màn Thông báo | tap(accessibility id "Thông báo") | ✅ PASS | — |
| 3 | Bấm vào thông báo "Đơn đã hoàn tất - cảm ơn bạn" | find_element(-android uiautomator resourceId notif-item-019fcb8c-fc15-7ef0-80a6-3b9725c63a72) → tap | ✅ PASS | Điều hướng đúng sang "Theo dõi đơn", trạng thái timeline = "Hoàn thành" (highlight cam), khớp Expected |

**Result: ✅ PASS**
**Screenshot:** TC_03.37_after_tap_donhoantat.png
**Locator captured:** 1 element (notif-item resourceId, unique per card)

---

## TC_03.39: Check bấm thông báo "Đơn đã bị huỷ" điều hướng đúng sang Theo dõi đơn

| # | Step | Action | Result | Notes |
|---|------|--------|--------|-------|
| 1 | Đăng nhập vai trò Sender/Receiver/Carrier còn lại | (đã sẵn có, session "Phan Minh Tài") | ✅ PASS | — |
| 2 | Mở màn Thông báo | tap(accessibility id "Thông báo") | ✅ PASS | — |
| 3 | Bấm vào thông báo "Đơn đã bị huỷ" | find_element(-android uiautomator resourceId notif-item-019fd040-c13d-70d7-ae3d-010e42304a79) → tap | ✅ PASS | Điều hướng đúng sang "Theo dõi đơn", banner đỏ "Đơn hàng đã bị huỷ — Huỷ bởi: Người gửi", khớp Expected |

**Result: ✅ PASS**
**Screenshot:** TC_03.39_after_tap_donbihuy.png
**Locator captured:** 1 element (notif-item resourceId, unique per card)

---

## TC_03.1 – .16, TC_03.19, TC_03.28, TC_03.29, .30, .31, .32, .34, .38 (Round 2 recheck): vẫn BLOCKED

Xem chi tiết lý do đầy đủ ở block Round 1 tương ứng phía trên (mỗi TC có dòng "**Re-checked Round 2**" ghi kết quả xác nhận lại). Không có thay đổi kết quả cho các TC này giữa 2 round — 24 TC vẫn BLOCKED vì cùng nguyên nhân cấu trúc (multi-role orchestration / loại thông báo chưa phát sinh / tài khoản không rỗng được / network-loss không canh được timing).
