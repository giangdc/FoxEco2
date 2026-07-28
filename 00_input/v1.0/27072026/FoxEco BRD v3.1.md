# FoxEco — BRD v3.1 · 01 Gửi Hàng

## A1 · Tổng quan & Bối cảnh

FoxEco là mạng xã hội nội bộ tương trợ của FPT Telecom: nơi CBNV đăng tin cần gửi hàng và tin sẵn sàng nhận giao giúp khi tiện đường — dựa trên lòng tin đồng nghiệp. Phạm vi tài liệu này: chức năng Gửi Hàng (~20.000 CBNV, 34 tỉnh/thành; ghép tin theo địa lý; định danh SSO nội bộ; mô hình tương trợ, không thu phí qua app).

## A2 · Nguyên tắc sản phẩm (áp cho cả 3 chức năng)

| # | Nguyên tắc | Diễn giải |
| --- | --- | --- |
| NT-01 | Hai chiều đăng tin | Mỗi chức năng đều có tin NEED — cần và OFFER — giúp; hệ thống ghép 2 chiều |
| NT-02 | KHÔNG có chat | Hai bên kết nối bằng lộ liên hệ sau khi chấp nhận; trao đổi diễn ra ngoài app |
| NT-03 | KHÔNG có thanh toán | Không ví, không cổng thanh toán. Chi phí (nếu có) hai bên tự đối soát offline; app chỉ ghi nhận (tùy chọn) |
| NT-04 | App = nơi GHI NHẬN tương tác 2 chiều | Bảng tin + ghép nối + nhật ký tương tác (ai đăng, ai nhận, chấp nhận, hoàn thành, đánh giá) |
| NT-05 | Tự chịu trách nhiệm pháp lý | Hai bên tự thỏa thuận & chịu trách nhiệm; hàng giá trị → bảo hiểm bên thứ 3 (phase sau) |
| NT-06 | Ghép theo địa lý | Chỉ ghép tin cùng phạm vi hợp lý (cùng tỉnh/khu vực/văn phòng) |
| NT-07 | Định danh & tin cậy | SSO; hiển thị phòng ban, đánh giá, tier để hai bên tự cân nhắc |

> Ranh giới scope cốt lõi: Đăng tin → Ghép nối → Lộ liên hệ → Hai bên tự thực hiện ngoài app → Ghi nhận & xác nhận hoàn thành 2 chiều → Đánh giá. Các thao tác trong app (ảnh, vị trí, các bước xác nhận) là bản ghi tương tác/bằng chứng, KHÔNG biến FoxEco thành đơn vị vận chuyển.

## A3 · Bộ sản phẩm & Thứ tự ưu tiên

| Service | Tên hiển thị | File | Ưu tiên phát triển | MVP Status |
| --- | --- | --- | --- | --- |
| DELIVERY | 🟠 Gửi hàng | 01 | #1 | Core — làm trước |

Tagline: "Tiện đường — Đồng nghiệp giúp nhau" · Nền tảng: Mobile App (iOS/Android) + Admin Web Portal.

## A4 · Mô hình "Tin Đăng" (Post) — 2 chiều NEED/OFFER

Cả 3 chức năng dùng chung khái niệm Tin đăng với 2 chiều và một vòng đời thống nhất; mỗi feature mở rộng thêm trường đặc thù.

### Vòng đời Tin đăng (status chung)

```
[DRAFT]       Người dùng soạn tin
   ↓ Đăng
[POSTED]      Hiển thị bảng tin, chờ ghép
   ↓ Chủ tin chấp nhận 1 người quan tâm
[MATCHED]     Đã ghép 2 chiều → 🔓 lộ liên hệ
   ↓ Hai bên thực hiện (ngoài app)
[IN_PROGRESS] Đang thực hiện (app ghi nhận tương tác/bằng chứng)
   ↓ Hai bên xác nhận hoàn thành
[COMPLETED]   Đóng tin + tặng gift ảo trên app (người gửi cảm ơn người vận chuyển)

--- Ngoài luồng ---  [CANCELLED]  [EXPIRED]
```

post_id · author_id · service_type · direction (NEED/OFFER) · title/description · area_scope · time_window · status · created_at/expires_at · visibility

Ghép ngược chiều cùng loại (NEED↔OFFER) · cùng phạm vi địa lý · khớp khung giờ · loại người khóa khỏi ghép · ưu tiên theo độ gần/đánh giá/cùng phòng. MVP = bảng tin (feed) + tìm kiếm/lọc thủ công; ghép tự động nâng cao là phase sau.

## A5 · Tương tác 2 chiều & Cơ chế kết nối (không chat)

Giá trị trung tâm của app (NT-04): ghi lại toàn bộ tương tác giữa 2 CBNV quanh một tin đăng.

### Cơ chế kết nối khi KHÔNG có chat

```
[Người B] thấy tin của [Người A] → bấm "Tôi mang giúp được"
        ↓
HỆ THỐNG GHÉP NGAY (không cần bước chủ tin duyệt)
        ↓
🔓 LỘ SĐT cho cả hai: Họ tên · Phòng ban · SĐT · (tùy chọn) Workplace/email
        ↓
Hai bên tự liên hệ NGOÀI APP để thống nhất chi tiết
        ↓
App GHI NHẬN: trạng thái · mốc thời gian · xác nhận hoàn thành
        ↓
KHÔNG đánh giá sao — người gửi gửi QUÀ ẢO cảm ơn người vận chuyển
```

| Rule | Mô tả |
| --- | --- |
| BR-CON-01 | Người B bấm "Tôi mang giúp được" → hệ thống ghép ngay, không cần bước chủ tin duyệt |
| BR-CON-02 | Sau khi ghép: lộ SĐT + kênh liên hệ cho đúng 2 người trong cặp ghép; trước khi ghép không lộ SĐT |
| BR-INT-03 | Hoàn thành cần người nhận xác nhận đã nhận hàng; nếu không xác nhận → nhắc + admin hỗ trợ |
| BR-INT-04 | Timeline tương tác không sửa được sau khi ghi (audit) |
| BR-INT-05 | Huỷ sau khi MATCHED phải có lý do (bắt buộc), ghi rõ ai huỷ + đồng bộ realtime cả 3 bên |
| BR-INT-06 | Không đánh giá sao; ghi nhận thiện chí bằng quà ảo người gửi tặng người vận chuyển sau khi hoàn tất |

## A6 · Actors & Hồ sơ (chung)

| Actor | Code | Mô tả |
| --- | --- | --- |
| Người đăng tin | POSTER | CBNV đăng tin NEED hoặc OFFER |
| Người ghép tin | RESPONDER | CBNV bày tỏ quan tâm / đề nghị giúp một tin |
| Admin/Ops | ADMIN | Kiểm duyệt, xử lý báo cáo, can thiệp, audit |
| System/Worker | SYSTEM | Thông báo, hết hạn tin, tổng hợp số đơn & số quà ảo nhận được, dọn dữ liệu |

> Vai trò theo tin, không cố định: cùng một CBNV vừa có thể đăng tin (POSTER) vừa ghép tin người khác (RESPONDER). Mỗi feature ánh xạ thành cặp cụ thể: sender↔carrier · driver↔passenger · parent↔helper.

### Tài khoản & Hồ sơ (USR)

| ID | Yêu cầu |
| --- | --- |
| USR-01 | Đăng nhập SSO nội bộ FPT → JWT, role, profile |
| USR-02 | Xem/cập nhật hồ sơ: tên, SĐT, avatar, phòng ban, khu vực/văn phòng, kênh liên hệ |
| USR-04 | Hiển thị phòng ban + khu vực/tỉnh (tin cậy + ghép địa lý) |
| USR-05 | Hiển thị tổng số đơn đã giúp + tổng số quà ảo đã nhận (không tính điểm/CO₂) |
| USR-07 | Cấu hình kênh liên hệ sẽ lộ: SĐT (bắt buộc), Workplace/email (tùy chọn) |

## A7 · Phần thưởng — Quà ảo

- Sau khi đơn hoàn tất, người gửi tặng quà ảo cảm ơn người vận chuyển
- 4 loại quà: bông hoa, ly cà phê, gấu bông, vương miện — biểu tượng phi vật chất
- Gửi ngay, không cần bước xác nhận; người nhận thấy thông báo "Bạn nhận được một món quà cảm ơn"
- Trang cá nhân tổng hợp tổng số đơn đã giúp + số quà ảo đã nhận (đếm theo loại) + lịch sử nhận quà
- Không tính điểm, không tier/xếp hạng, không CO₂, không quy đổi tiền / thanh toán in-app

## A8 · Pháp lý, Trách nhiệm & Trust/Safety

> Pháp lý (quan trọng): FoxEco là nền tảng kết nối nội bộ, KHÔNG phải đơn vị vận chuyển/giữ trẻ/vận tải. Hai bên tự thỏa thuận & tự chịu trách nhiệm. App không xử lý tiền. Hàng/tài sản giá trị cao → khuyến nghị bảo hiểm bên thứ 3 (phase sau). App hiển thị điều khoản miễn trừ + buộc consent trước khi đăng/ghép. Hàng cấm (thuốc, vũ khí, chất nguy hiểm, phi pháp) không được đăng.

### Trust & Safety (chung)

| ID | Yêu cầu |
| --- | --- |
| TS-01 | Ghi log toàn bộ tương tác: ai đăng, ai nhận, mốc thời gian, đổi trạng thái, huỷ (kèm lý do + ai huỷ) |
| TS-02 | Log không sửa được sau khi ghi (audit trail) |
| TS-03 | Admin có quyền can thiệp hỗ trợ khi có vướng mắc (dựa trên log) |

> Phạm vi hiện tại: chỉ ghi log + admin can thiệp hỗ trợ. KHÔNG có chấm sao/đánh giá, KHÔNG có chặn (block) người dùng.

## A10 · KPIs chung & Roadmap phát triển

| KPI nền tảng | Mục tiêu | KPI nền tảng | Mục tiêu |
| --- | --- | --- | --- |
| Time to post | < 2 phút | Completion rate (2 phía) | > 85% |
| Match rate | > 60% | Rating average | > 4.0/5.0 |
| Response rate | > 70% | Report rate | < 3% |
| Admin intervention | < 3% | Reward redemption | > 20% (tháng 2) |

```
Phase 1 (Core)  → Nền tảng chung + GỬI HÀNG
                  Auth/Profile · Đăng tin NEED/OFFER · Feed/Tìm kiếm ·
                  Ghép + lộ liên hệ · Ghi nhận tương tác · Đánh giá · Admin
Phase sau       → Bảo hiểm bên thứ 3 · Ghép tự động nâng cao · Mở rộng 34 tỉnh
```

## D1 · Tổng quan & Hai chiều đăng tin

CBNV A cần gửi món đồ cho CBNV B. A đăng tin lên FoxEco; CBNV C đang đi thuận đường nhận mang hộ. App kết nối A–C, ghi nhận quá trình và đánh giá.

| Chiều | Ai đăng | Nội dung tin | Người ghép |
| --- | --- | --- | --- |
| NEED "Tôi cần gửi" | SENDER | Món hàng, điểm lấy, điểm giao, khung giờ, người nhận | CARRIER thuận đường: "Tôi mang giúp được" |
| OFFER "Tôi nhận giao hàng" | CARRIER | Điểm xuất phát → điểm đến, khung giờ, tên & SĐT (tuyến không công khai lên bảng tin) | Hệ thống tự khớp với tin NEED trùng điểm lấy & điểm giao → gửi thông báo để CARRIER duyệt "Nhận giao" |

Vai trò: SENDER · CARRIER · RECEIVER · ADMIN. Scope: đăng tin 2 chiều · feed/tìm kiếm · ghép + lộ liên hệ · nhận hàng (ảnh tùy chọn) · chia sẻ vị trí tùy chọn · xác nhận 2 phía · đánh giá · (tùy chọn) ghi nhận chi phí đối soát offline. Ngoài scope: thanh toán/ví in-app · bảo hiểm bên thứ 3 (phase sau) · chat (thay bằng lộ liên hệ).

> Prototype tham chiếu (as-built): tài liệu này đồng bộ với bản demo tương tác 3 vai trò trên cùng một app — Người gửi (Đồng Công Chí Linh), Người vận chuyển (Nguyễn Anh Tuấn), Người nhận (Phan Văn Hưng). Ba màn dùng chung một bộ dữ liệu đơn hàng & đồng bộ realtime: thao tác trên một máy lập tức cập nhật trạng thái ở hai máy còn lại. Giao diện của 3 vai trò giống hệt nhau, chỉ khác nội dung theo vai trò với đơn.

## D1b · User Story — Gửi Hàng (toàn bộ vòng đời)

Viết theo mẫu "Là [vai trò], tôi muốn [hành động], để [lợi ích]", bám sát flow & màn hình hiện có (Tin mới, Bảng tin "Hàng cần chuyển", wizard đăng tin, Theo dõi đơn, Đơn của tôi, Trang cá nhân).

### Nhóm 1 — SENDER: Đăng nhu cầu & theo dõi

| ID | User Story | Acceptance Criteria |
| --- | --- | --- |
| US-D01 | Là Sender, tôi muốn đăng tin "Cần gửi" qua wizard ngắn (loại hàng → điểm lấy/giao chỉ bằng 1 ô nhập địa chỉ → xác nhận), để đăng tin nhanh mà không phải điền nhiều bước rườm rà. | Wizard 3 bước; mỗi điểm lấy/giao chỉ có 1 input địa chỉ (không chip gợi ý); B3 bắt buộc tick đồng ý điều khoản mới cho phép đăng |
| US-D02 | Là Sender, tôi muốn thấy ngay tin của mình trên trang chủ ("Tin mới") sau khi đăng, để yên tâm tin đã lên hệ thống thành công. | Sau khi bấm "Đăng tin ngay" → màn "Đăng tin thành công" (KHÔNG hiển thị mã đơn — mã kỹ thuật vô nghĩa với người dùng); tin xuất hiện ở "Đơn của tôi" trên trang chủ |
| US-D04 | Là Sender, tôi muốn tin tự động chuyển trạng thái "Hết hạn" và quay về mục Đơn của tôi nếu quá thời gian không ai nhận mang giúp, để biết cần đăng lại hoặc đổi phương án. | Quá hạn cấu hình mà chưa MATCHED → tự chuyển EXPIRED, hiển thị badge "Hết hạn" ở tab hoàn tất kèm lý do "Không có ai nhận mang giúp trong thời gian đăng" |
| US-D05 | Là Sender, tôi muốn xem đầy đủ thông tin người nhận (tên, SĐT, địa chỉ) xuyên suốt quá trình giao, để chủ động hỗ trợ nếu Carrier cần xác minh lại. | Thông tin người nhận hiển thị cố định trên màn Theo dõi đơn ở mọi trạng thái (MATCHED → IN_TRANSIT → DELIVERED) |
| US-D18 | Là Sender, tôi muốn nhập email công ty của người nhận để hệ thống tự điền tên, SĐT và địa chỉ từ danh bạ nội bộ, để khỏi gõ tay và tránh sai thông tin. | Ô "Email công ty người nhận" nằm đầu mục Người nhận; nhập email có trong hệ thống → tự điền tên/SĐT/địa chỉ + báo "Đã tìm thấy trong hệ thống nội bộ"; không có → báo "Không tìm thấy · nhập thủ công" |
| US-D19 | Là Sender, tôi muốn chỉnh sửa đơn khi đơn còn "Chờ ghép", để cập nhật thông tin trước khi có người nhận. | Nút "Chỉnh sửa" chỉ hiện ở trạng thái Chờ ghép (POSTED); mở màn giống tạo đơn nhưng đã điền sẵn; có nút "Cập nhật" & "Huỷ chỉnh sửa"; sau IN_TRANSIT không cho sửa |

### Nhóm 2 — CARRIER: Nhận mang giúp (chiều NEED)

| ID | User Story | Acceptance Criteria |
| --- | --- | --- |
| US-D06 | Là Carrier, tôi muốn xem tối đa 5 tin cần gửi mới nhất ngay trên trang chủ, để nhanh chóng biết có ai cần giúp mà không cần vào sâu Bảng tin. | Trang chủ hiển thị đúng 5 tin mới nhất; nếu còn tin khác hiện nút "Xem thêm trên Bảng tin" dẫn sang màn Bảng tin |
| US-D07 | Là Carrier, tôi muốn bấm "Tôi mang giúp được" ngay tại thẻ tin hoặc màn chi tiết, để gửi đề nghị nhanh cho Sender. | Đề nghị gửi push + in-app tới Sender; trạng thái tin cập nhật chờ chấp nhận |
| US-D08 | Là Carrier, tôi muốn có đầy đủ thông tin cả người gửi và người nhận (tên, SĐT, địa chỉ) ngay sau khi được ghép, để đến lấy hàng đúng người và giao đúng nơi. | Sau MATCHED, màn Theo dõi đơn gom 2 cụm "Người gửi" & "Người nhận" (tên/SĐT/địa chỉ) hiển thị xuyên suốt tới khi hoàn tất; SĐT chỉ lộ sau khi ghép |
| US-D09 | Là Carrier, tôi muốn bấm "Tôi đã lấy hàng" rồi "Đã giao cho người nhận" theo đúng thứ tự, để hệ thống ghi nhận mốc thời gian minh bạch cho cả hai bên. | Không thể bấm "Đã giao" trước khi "Tôi đã lấy hàng"; timeline theo dõi 5 mốc (Chờ ghép · Lấy hàng · Đang giao · Đã giao · Hoàn thành), mỗi bước ghi timestamp |

### Nhóm 3 — CARRIER: "Tôi nhận giao hàng" (chiều OFFER — hệ thống tự khớp)

| ID | User Story | Acceptance Criteria |
| --- | --- | --- |
| US-D10 | Là Carrier đang có nhu cầu di chuyển, tôi muốn đăng tin "Tôi nhận giao hàng" với điểm xuất phát, điểm đến, khung giờ và tên/SĐT, để báo rằng tôi có thể nhận giao giúp đồng nghiệp trên đường đi. | Màn đăng tin OFFER 1 màn duy nhất, các trường: Điểm xuất phát, Điểm đến, Khung giờ, Tên, SĐT + tick đồng ý điều khoản; có dòng chú thích mô tả đang di chuyển & có thể nhận giao hộ |
| US-D11 | Là Carrier, tôi muốn tuyến đường của mình không hiển thị công khai lên bảng tin mà chỉ lưu vào hệ thống chờ khớp, để giữ riêng tư và để hệ thống chủ động tìm người gửi phù hợp. | Sau khi đăng → màn "Đã ghi nhận tuyến đường" giải thích: tuyến được lưu (không công khai), khi có người cần gửi trùng điểm lấy & điểm giao hệ thống sẽ gửi thông báo để bạn xem xét |
| US-D12 | Là Carrier đã đăng tuyến, tôi muốn được thông báo khi có tin cần gửi trùng tuyến của mình, để kịp thời xem xét nhận giao. | Khi một tin NEED trùng điểm lấy & điểm giao với tuyến → hệ thống đẩy thông báo "Tìm thấy đơn hàng phù hợp tuyến của bạn"; bấm vào thông báo → mở màn chi tiết tin cần vận chuyển đó |
| US-D13 | Là Carrier, tôi muốn từ thông báo mở chi tiết đơn phù hợp và bấm "Nhận giao", để nhận đơn và bắt đầu quá trình giao. | Tại chi tiết tin NEED phù hợp có nút "Nhận giao"; bấm → ghép (MATCHED) → lộ liên hệ 2 bên → vào màn Theo dõi đơn |

### Nhóm 4 — Hoàn tất, đánh giá & ngoài luồng chính

| ID | User Story | Acceptance Criteria |
| --- | --- | --- |
| US-D14 | Là Receiver/Sender, tôi muốn xác nhận "Đã nhận" sau khi Carrier báo đã giao, để đóng tin và kích hoạt bước đánh giá. | Chỉ xác nhận được sau khi Carrier đã bấm "Đã giao"; quá 2 giờ không xác nhận → hệ thống nhắc, thêm 2 giờ → admin hỗ trợ |
| US-D15 | Là Sender, tôi muốn "Tặng quà cảm ơn" người vận chuyển sau khi hoàn tất (bông hoa, ly cà phê, gấu bông, vương miện), để tri ân theo cách thân thiện thay cho việc chấm sao. | Màn hoàn tất của Sender hiển thị 4 loại quà; chọn quà → gửi ngay không cần bước xác nhận → popup "Cảm ơn của bạn đã được gửi" → nút "Về trang chủ"; Carrier nhận thông báo "Bạn nhận được một món quà cảm ơn" → mở Trang cá nhân |
| US-D16 | Là Sender/Carrier/Receiver, tôi muốn huỷ đơn (kèm lý do) và biết rõ ai đã huỷ, để minh bạch khi kế hoạch thay đổi. | Huỷ được ở POSTED/MATCHED; popup huỷ bắt buộc nhập lý do (nút Xác nhận khoá tới khi có lý do); đơn huỷ ghi rõ ai huỷ (Người gửi/Người vận chuyển/Người nhận) + lý do, đồng bộ realtime cho cả 3 bên; Carrier huỷ nhận → đơn trả lại bảng tin (về "Chờ ghép"); sau IN_TRANSIT phải tạo báo cáo sự cố |
| US-D20 | Là Carrier, tôi muốn xem tổng hợp "Quà đã nhận" (đếm theo loại + lịch sử) và "Đơn đã giúp" trong Trang cá nhân, để theo dõi ghi nhận từ đồng nghiệp. | Trang cá nhân có mục "Đơn đã giúp" & "Quà đã nhận"; màn Quà đã nhận hiển thị 1 card đếm số bông hoa/ly cà phê/gấu bông/vương miện + danh sách lịch sử nhận quà |
| US-D21 | Là Receiver, tôi muốn có app đầy đủ để nhận thông báo, theo dõi đơn đang tới và xác nhận "Đã nhận hàng", để chủ động biết hàng đang đến và đóng đơn. | Receiver có đủ Trang chủ/Bảng tin/Đơn hàng/Cá nhân/Thông báo; theme màu xanh lá để phân biệt; chỉ Receiver mới thấy & bấm được "Xác nhận đã nhận hàng" |

## D2 · Workflow & Status Flow

```
[SENDER] (chiều NEED)
  └→ Đăng tin "Cần gửi": mô tả hàng, ảnh tùy chọn, điểm lấy/giao, khung giờ, người nhận
        ↓
[FEED] Hiển thị cho CBNV cùng khu vực/thuận tuyến (ghép theo địa lý)
        ↓
[CARRIER] Duyệt feed / nhận thông báo → "Tôi mang giúp được"
        ↓
[SENDER] Xem hồ sơ tin cậy CARRIER → "Chấp nhận"
        ↓
🔓 LỘ LIÊN HỆ → tự liên hệ ngoài app  → Tin MATCHED
        ↓
[NHẬN HÀNG] CARRIER gặp SENDER → (tùy chọn) chụp ảnh hàng → "Đã nhận hàng" → IN_TRANSIT
        ↓
[ĐANG GIAO] (tùy chọn) chia sẻ vị trí cho SENDER/RECEIVER
        ↓
[GIAO HÀNG] CARRIER trao hàng → "Đã giao" → (tùy chọn) ảnh tại điểm giao
        ↓
[XÁC NHẬN] RECEIVER/SENDER "Xác nhận đã nhận"
        ↓
[HOÀN TẤT] Đánh giá 2 chiều → (tùy chọn) ghi chi phí offline → CO₂ + điểm → COMPLETED
```

> Nguyên tắc tin cậy: CBNV định danh rõ ràng. Trách nhiệm đảm bảo qua (1) danh tính thật + phòng ban, (2) ảnh/timestamp/vị trí tùy chọn làm bằng chứng, (3) đánh giá 2 chiều. Không QR/OTP, không thanh toán/chat trong app.

```
[DRAFT] → [POSTED] → [MATCHED]
                        ↓ Carrier "Tôi đã lấy hàng" (+ ảnh tùy chọn)
                     [IN_TRANSIT]
                        ↓ "Đã giao" + RECEIVER "Xác nhận đã nhận"
                     [DELIVERED "Đã giao"] → Receiver "Xác nhận đã nhận hàng" → [COMPLETED "Hoàn thành"] → Sender tặng quà cảm ơn Carrier
Timeline theo dõi 5 mốc: Chờ ghép · Lấy hàng · Đang giao · Đã giao · Hoàn thành
Ngoài luồng: [CANCELLED "Đã huỷ"] — bắt buộc lý do; ghi rõ ai huỷ (Sender/Carrier/Receiver); đồng bộ realtime cả 3 bên; Carrier huỷ → trả đơn về "Chờ ghép" · [EXPIRED] · [INCIDENT]
```

## D3 · Functional Requirements — Gửi Hàng

| ID | Yêu cầu | Acceptance Criteria |
| --- | --- | --- |
| ORD-01 | Đăng tin gửi hàng (NEED/OFFER) | NEED: mô tả, ảnh tùy chọn, điểm lấy/giao, giá trị, loại hàng, khung giờ, người nhận. OFFER: điểm xuất phát→đến, khung giờ, tên/SĐT — không công khai lên bảng tin |
| ORD-02 | Wizard đăng tin ngắn | B1 Loại tin+hàng → B2 Địa điểm/lộ trình+thời gian → B3 Xác nhận + đồng ý điều khoản |
| ORD-04 | Tin có timeline trạng thái | Lịch sử đầy đủ với timestamp |
| ORD-06 | Tin hết hạn | Quá hạn chưa ghép → gửi thông báo để người đăng tự gỡ/đăng lại; hệ thống không tự can thiệp ở phase này |
| ORD-09 | Consent điều khoản trước khi đăng | Bắt buộc tick "đồng ý tự chịu trách nhiệm" |
| LOC-03 | Quick-select văn phòng FPT | Hiển thị preset 6 văn phòng (+ mở rộng theo tỉnh) |
| ASN-01 | Bày tỏ quan tâm / đề nghị mang giúp | Gửi tới chủ tin push + in-app |
| ASN-02 | Chủ tin chấp nhận 1 người | MATCHED + lộ liên hệ |
| ASN-03 | Chống ghép trùng | 1 tin chỉ 1 cặp active (DB constraint + tx lock) |
| PUP-03 | Chụp ảnh hàng lúc nhận | Tùy chọn (khuyến nghị) — lưu S3, gắn timeline làm bằng chứng |
| GPS-01 | Chia sẻ vị trí khi đang giao | Tùy chọn; chỉ active khi đang giao; xóa sau khi đóng |
| DLV-03 | RECEIVER/SENDER xác nhận đã nhận | Quá N giờ chưa xác nhận → nhắc → admin hỗ trợ |
| RAT-01/02 | Đánh giá 2 chiều | 1–5 sao + nhận xét |
| COST-01 | (Tùy chọn) ghi nhận chi phí | Bản ghi tham khảo; app KHÔNG thanh toán; đối soát offline |
| ORD-10 | Chỉnh sửa tin khi "Chờ ghép" | Form điền sẵn; chỉ trạng thái POSTED; có "Cập nhật" & "Huỷ chỉnh sửa" |
| USR-EML | Tự điền người nhận từ email công ty | Tra danh bạ nội bộ; khớp → tự điền tên/SĐT/địa chỉ; không khớp → nhập tay |
| MTCH-01 | Tự khớp tuyến OFFER ↔ NEED | Trùng điểm lấy & điểm giao → đẩy thông báo cho Carrier duyệt "Nhận giao" |
| CNL-01 | Huỷ đơn kèm lý do | Lý do bắt buộc; ghi actor (Sender/Carrier/Receiver); đồng bộ realtime; Carrier huỷ → về POSTED |
| GIFT-01 | Tặng quà cảm ơn Carrier | 4 loại quà phi vật chất (KHÔNG thanh toán); gửi không cần xác nhận; tổng hợp ở "Quà đã nhận" |

## D4 · Business Rules & Permission Matrix

| Rule | Mô tả |
| --- | --- |
| BR-ORD-03 | Giá trị hàng trong ngưỡng cấu hình; trên ngưỡng → cảnh báo nên mua bảo hiểm (phase sau) |
| BR-ORD-04 | Hàng cấm không được đăng |
| BR-ASN-03 | Sau khi nhận hàng (IN_TRANSIT) không hủy thường → phải tạo sự cố |
| BR-CNF-01 | Ảnh hàng lúc nhận tùy chọn nhưng khuyến nghị mạnh — bằng chứng chính khi tranh chấp |
| BR-CNF-04 | RECEIVER không xác nhận 2 giờ → nhắc; thêm 2 giờ → admin hỗ trợ |
| BR-COST-01 | App không xử lý tiền; chỉ ghi con số hai bên tự khai (tùy chọn) |
| BR-CNL-01 | Huỷ đơn bắt buộc có lý do; hệ thống ghi rõ vai trò người huỷ + đồng bộ cho cả 3 bên |
| BR-EDIT-01 | Chỉ được chỉnh sửa tin khi còn "Chờ ghép" (POSTED); đã MATCHED trở đi khoá chỉnh sửa |
| BR-MTCH-01 | OFFER khớp NEED khi trùng điểm lấy & điểm giao; tuyến OFFER không hiển thị công khai |
| BR-GIFT-01 | Quà cảm ơn là biểu tượng phi vật chất, không quy đổi tiền, không qua thanh toán in-app |

| Chức năng | Sender | Carrier | Receiver | Admin |
| --- | --- | --- | --- | --- |
| Đăng tin gửi hàng | ✓ | ✓ | ✕ | ✓ |
| Bày tỏ quan tâm / nhận mang giúp | — | ✓ | — | ✕ |
| Chấp nhận người ghép | ✓ chủ tin | ✓ chủ tin | ✕ | ✓ override |
| "Đã nhận hàng" / "Đã giao" | ✕ | ✓ | ✕ | ✓ override |
| Chụp ảnh / chia sẻ vị trí | ✕ | ✓ | ✕ | ✕ |
| Xác nhận "Đã nhận" | ✓ nếu nhận | ✕ | ✓ | ✓ override |
| Huỷ đơn (bắt buộc lý do) | ✓ trước IN_TRANSIT | ✓ → về Chờ ghép | ✓ trước IN_TRANSIT | ✓ |
| Chỉnh sửa tin (khi Chờ ghép) | ✓ chủ tin | ✓ chủ tin OFFER | ✕ | ✓ |
| Tặng quà cảm ơn | ✓ tặng | ★ nhận | ✕ | ✕ |
| Báo sự cố | ✓ | ✓ | ✓ | ✓ |

## D5 · Edge Cases · Data Model · KPI

| Edge case | Xử lý |
| --- | --- |
| Tin không ai nhận | EXPIRED sau timeout, gợi ý đăng lại / mở rộng khu vực |
| Nhiều người cùng nhận 1 tin | Chủ tin chọn; chống double-accept bằng tx lock |
| Sau khi nhận, hàng hỏng/mất | Tạo sự cố, không cho COMPLETED thường; dùng timeline + ảnh làm bằng chứng |
| Người nhận vắng mặt | "Đã giao" + ảnh hiện trường; 2 giờ không xác nhận → admin hỗ trợ |
| Tranh chấp tình trạng hàng | Admin cung cấp ảnh + timeline; hai bên tự giải quyết |
| Hàng giá trị cao | Cảnh báo nên mua bảo hiểm bên thứ 3 (phase sau) |

```
delivery.delivery_details(post_id, item_*,
  pickup_*, dropoff_*, receiver_*, allow_inspect)
delivery.assignments(id, post_id, carrier_id,
  status, picked_up_at, delivered_at)
delivery.proof_photos(id, post_id, phase,
  s3_key, taken_at, latlng)
delivery.incidents(id, post_id, reporter_id, ...)
```

Match rate > 65% · Pickup success > 95% · Delivery success > 90% · Proof attach rate > 60% · Incident rate < 5%

Ngưỡng giá trị hàng? Ảnh bắt buộc cho hàng > ngưỡng? Chia sẻ vị trí mặc định bật/tắt? Ai được xác nhận "đã nhận"? Hạn tin mặc định?

## D6 · Thông báo (Notifications)

Danh sách sự kiện bắn thông báo dựa trên flow & màn hình hiện có của prototype. Nháp — chờ BA review & bổ sung. Kênh: in-app + push (SĐT chỉ lộ sau khi ghép, không đưa vào nội dung push).

| ID | Sự kiện kích hoạt | Người nhận | Nội dung (mẫu) |
| --- | --- | --- | --- |
| NTF-01 | Có người bấm "Tôi mang giúp được" → ghép ngay | Người gửi | "Đã có người nhận mang giúp đơn của bạn — SĐT đã được lộ để liên hệ" |
| NTF-02 | Đơn được ghép (MATCHED) | Người nhận | "Đơn gửi tới bạn đã có người vận chuyển nhận giao" |
| NTF-03 | Hệ thống khớp tuyến OFFER với 1 tin NEED | Người vận chuyển | "Tìm thấy đơn hàng phù hợp tuyến của bạn — xem chi tiết để nhận giao" |
| NTF-04 | Carrier bấm "Tôi đã lấy hàng" (IN_TRANSIT) | Người gửi · Người nhận | "Người vận chuyển đã lấy hàng và bắt đầu giao" |
| NTF-05 | Carrier bấm "Đã giao cho người nhận" (DELIVERED) | Người nhận · Người gửi | "Đơn đã được giao — vui lòng xác nhận đã nhận hàng" |
| NTF-06 | Người nhận "Xác nhận đã nhận hàng" (COMPLETED) | Người gửi · Người vận chuyển | "Đơn đã hoàn tất — cảm ơn bạn!" |
| NTF-07 | Người gửi tặng quà ảo | Người vận chuyển | "Bạn nhận được một món quà cảm ơn 🎁 — mở Trang cá nhân để xem" |
| NTF-08 | Đơn bị huỷ (kèm lý do) | Các bên còn lại của đơn | "Đơn đã bị huỷ bởi [vai trò] — lý do: […]" |
| NTF-09 | Tin quá hạn chưa ghép | Người đăng tin | "Tin của bạn đã quá hạn — gỡ hoặc đăng lại nếu vẫn cần" |

> Chờ BA bổ sung: ngưỡng thời gian nhắc, gộp/không gộp thông báo, thông báo cho người thứ 3 (VD người nhận khi carrier huỷ), cấu hình bật/tắt theo loại.

## D7 · Rule vận hành (Operating Rules)

Quy tắc điều phối khi hệ thống khớp tin & gửi thông báo. Nháp — chờ BA review & bổ sung.

| ID | Rule | Mô tả |
| --- | --- | --- |
| OPR-01 | Trần số tin gợi ý cho 1 carrier | Mỗi người vận chuyển chỉ nhận thông báo tối đa 5 tin cần gửi phù hợp (mới & gần tuyến nhất); tránh làm phiền/spam |
| OPR-02 | Điều kiện khớp | Chỉ khớp khi trùng điểm lấy & điểm giao (cùng khu vực/tuyến) và giao nhau về khung giờ |
| OPR-03 | 1 tin — 1 cặp ghép | Ghép ngay cho người bấm "Tôi mang giúp được" đầu tiên; ngay khi có người nhận, tin bị ẩn khỏi bảng tin và không ai bấm "Tôi mang giúp được" được nữa (chống double-accept) |
| OPR-04 | Ưu tiên gợi ý | Sắp xếp theo độ gần tuyến → thời gian đăng (mới trước); tin quá hạn loại khỏi luồng khớp |
| OPR-05 | Không tự khớp với chính mình | Không gợi ý tin do chính người đó đăng; người gửi ≠ người vận chuyển của cùng một đơn |
| OPR-06 | Trần thông báo khớp / ngày | Giới hạn số lần bắn thông báo khớp cho mỗi carrier trong ngày (ngưỡng admin cấu hình) |
| OPR-07 | Lộ liên hệ có kiểm soát | SĐT chỉ lộ sau khi ghép, chỉ cho đúng 2 người trong cặp; không đưa SĐT vào nội dung push |
| OPR-08 | Vòng đời tin trong luồng khớp | Tin đang MATCHED/IN_TRANSIT không xuất hiện ở gợi ý cho carrier khác; tin huỷ bởi carrier quay lại "Chờ ghép" và được khớp lại |
| OPR-09 | Carrier huỷ khi chưa lấy hàng → trả đơn về bảng tin | Người vận chuyển huỷ ở trạng thái Đã ghép (chưa "Tôi đã lấy hàng") → đơn tự động về "Chờ ghép" và hiển thị lại trên bảng tin cho người khác nhận |
| OPR-10 | Điều kiện chỉnh sửa đơn | Chỉ được sửa đơn khi chưa có ai nhận (trạng thái "Chờ ghép"); ngay khi đã có người nhận (Đã ghép trở đi) → khoá chỉnh sửa hoàn toàn |
| OPR-11 | Điều kiện huỷ đơn | Chỉ được huỷ khi chưa ai nhận ("Chờ ghép") hoặc đang "Lấy hàng" (đã ghép, chưa lấy được hàng); đã lấy hàng → sang "Đang giao" thì KHÔNG ai được huỷ |

> Chờ BA bổ sung: bán kính/định nghĩa "cùng tuyến", độ lệch khung giờ cho phép, chu kỳ quét khớp, hạ ưu tiên người huỷ nhiều lần, quy tắc ưu tiên khi nhiều carrier cùng tuyến.