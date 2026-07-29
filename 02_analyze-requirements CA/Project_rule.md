# Project Rule — FoxEco

> Đọc bởi: analyze-requirements, generate-tc, log-bug, fetch-us, review-tc, review-src-tc.
> Cập nhật lần cuối: 2026-07-28 (đã thêm Custom Rule #7-12: 13-loại TC checklist bắt buộc, Group enum 4 giá trị, Expected Result không chèn note, sheet ALL bắt buộc, Steps bắt đầu bằng đăng nhập, droplist/EG/validate được gộp)

## 1. Thông tin dự án
| Field | Value |
|---|---|
| Tên dự án | FoxEco |
| Môi trường | DEMO (static HTML, chạy local) |
| URL | http://localhost:8765/ |
| Loại kiểm thử | Functional, Regression |
| Team mode | Solo |
| Ngôn ngữ viết TC | Tiếng Việt |
| Automation | Không có |
| Version hiện tại | v1.0 |
| QC phụ trách | anhdc4 |

## 2. Naming Conventions
- Documents: `DOC-v[VERSION]-[NN]`
- Scenarios: `SC-[MODULE]-[NNN]`
- Test cases: `TC-[MODULE]-[NNN]`
- TC Master: `TC-MASTER-v[VERSION].xlsx`
- Bug reports: `BUG-[NNN]-[short-title].md`

## 3. Module List (khởi tạo — sẽ bổ sung khi analyze-requirements chạy)
| Module | Mô tả |
|---|---|
| SENDER | Luồng người gửi hàng (đăng tin, theo dõi đơn) |
| CARRIER | Luồng người vận chuyển (xem tin, nhận giao, cập nhật trạng thái) |
| RECEIVER | Luồng người nhận hàng (xác nhận đã nhận) |
| ORDER | Trạng thái đơn hàng dùng chung (posted/matched/in_transit/delivered/completed) |

## 4. Priority Rule
- P1: chặn luồng chính (đăng tin, nhận đơn, xác nhận giao/nhận, đồng bộ trạng thái 3 vai trò)
- P2: validate input, dữ liệu biên
- P3: UI/UX, nội dung tĩnh

## 5. Test Data Rule
- Không dùng dữ liệu thật (SĐT, tên) — dùng data giả định đã có sẵn trong demo (Đồng Công Chí Linh, Nguyễn Anh Tuấn, Phan Văn Hưng).

## 6. Environment Note
Đây là **prototype HTML standalone** (xuất từ design tool), không có backend thật:
- 3 "điện thoại" (sender/carrier/receiver) là 3 instance của cùng 1 app, đồng bộ qua `window.FoxEcoStore` (state client-side, không persist).
- Nút "↺ Chạy lại từ đầu" reset store về trạng thái ban đầu (`posted`).
- Đăng tin qua wizard không tạo listing mới độc lập trong feed — chỉ ghi đè 1 order slot có sẵn. Đây là giới hạn đã biết của bản demo, không phải bug — ghi nhận trong Known Limitations, không log bug P1/P2 cho hành vi này.

**⚠️ Platform thật ≠ platform demo (user xác nhận 2026-07-27):**
- File HTML (`FoxEco Demo 3 vai tro (standalone)/...html`) **chỉ là bản demo** dùng để phân tích requirement/hành vi nghiệp vụ — KHÔNG phải target platform thật.
- **App thật là Mobile App riêng biệt, có icon cài trên điện thoại** (native hoặc packaged app) — KHÔNG phải web/browser.
- Ảnh hưởng downstream: khi app thật sẵn sàng để test/automate — dùng **Appium** (mobile), KHÔNG dùng Playwright/Chrome MCP (web) cho automation thật; `init-source-code` khi chạy cho automation thật nên chọn archetype Appium Java, không phải Playwright TypeScript. `vibe-test` trên app thật cũng nên dùng `/vibe-mobile` thay vì `/vibe-web`.
- TC-MASTER hiện tại viết theo hành vi quan sát từ demo HTML — cần rà soát lại khi có app thật để đảm bảo step/UI element khớp platform Mobile (vd: "click" → "tap", browser dialog → native alert, không còn khái niệm URL/tab).

## 7. Known Limitations (loại trừ khỏi bug report)
| # | Hiện tượng | Lý do |
|---|---|---|
| 1 | Đăng đơn mới qua wizard không xuất hiện thành tin riêng trong "Tin mới" của Carrier/Receiver | Demo dùng 1 order slot cố định trong store, không phải multi-order backend |
| 2 | Nhánh "Huỷ đơn" (mô tả trong Figma board) chưa có UI trong bản HTML | Chưa được implement trong bản export này |
| 3 | Nhánh "Tặng quà cảm ơn cho người vận chuyển" (menu Cá nhân/Quà đã nhận) chưa có UI | Chưa được implement trong bản export này |

## 8. Custom Rules
| # | Rule | Ghi chú |
|---|---|---|
| 1 | **Test Title** phải bắt đầu bằng "Kiểm tra" | Áp dụng từ 2026-07-24 (user yêu cầu khi review TC-MASTER v1.0) |
| 2 | **Expected Result** vẫn là 1 TC = 1 hành vi cần verify, KHÔNG đánh số 1/2/3. Nếu Expected có ≥2 mệnh đề/ý độc lập (phân cách bởi `;`, `.`, `—`, hoặc liệt kê bằng dấu phẩy) → **tách mỗi ý thành 1 dòng gạch đầu dòng `-`** trong cùng 1 ô (không tách thành nhiều TC, không dùng số 1/2/3). Ý ngắn chỉ 1 mệnh đề (không có dấu phân cách) → giữ nguyên 1 dòng, không ép tách. **Không tách nếu các mệnh đề chia sẻ chung 1 vị ngữ ở cuối câu** (vd "A, B, và C khớp với dữ liệu X" — tách sẽ làm "A" và "B" mất vị ngữ, chỉ "C" giữ được) — trường hợp này giữ nguyên 1 đoạn. | Đổi từ rule "1 câu/đoạn duy nhất" (2026-07-24) sang "gạch đầu dòng cho ý dài/nhiều mệnh đề" (2026-07-29, user yêu cầu khi thấy Expected v1.1 quá dài/nhiều chữ dồn 1 đoạn). Case gộp nhiều sub-case (Custom Rule #12, EG/Validation cùng field) vẫn ưu tiên dùng `-` thay vì số 1/2/3 luôn từ nay, không còn là ngoại lệ riêng. Steps vẫn đánh số bình thường — rule này chỉ áp cho cột Expected Result. |
| 3 | **TC ID** luôn liên tục `TC-[MODULE]-[NNN]`, KHÔNG dùng suffix mô tả (vd `-EP01`, `-EG-GC-001`, `-ST-GATE-01`) | Suffix/nhãn kỹ thuật (EP/EG/ST/...) chỉ được ghi trong cột Notes (`Technique: <tag>`), không đưa vào ID. Đây vốn đã là rule sẵn có trong generate-tc (Step 3a) — ghi lại đây để tránh lặp lỗi. |
| 4 | **KHÔNG generate TC cho case có Expected Result "chưa xác định"** — phải hỏi lại user để xác nhận hành vi thật trước, CHỈ generate sau khi có câu trả lời | Áp dụng từ 2026-07-27 (user phản hồi sau khi thấy TC-MASTER có nhiều case ghi "⚠️ Chưa xác định — cần vibe-test..."). Trước đây generate-tc vẫn tạo TC placeholder kèm cảnh báo cho case chưa rõ hành vi (theo tinh thần "không tự bịa" nhưng vẫn ghi ra file) — nay ĐỔI LẠI: khi rubric/phân tích phát hiện 1 case không đủ dữ liệu để viết Expected Result chắc chắn, DỪNG lại, liệt kê rõ case đó cho user xác nhận trước (qua câu hỏi trực tiếp hoặc AskUserQuestion), CHƯA ghi vào TC-MASTER cho tới khi có câu trả lời. Không tự ý ghi "⚠️ Chưa xác định" vào Excel rồi mới hỏi sau. |
| 5 | **KHÔNG hardcode giá trị cụ thể (địa chỉ, loại hàng, mốc thời gian tương đối...) vào Expected Result như thể đó là kết quả cố định đúng duy nhất** — với field hiển thị dữ liệu do user tự nhập (loại hàng, giá trị, địa chỉ, ghi chú, mốc thời gian tương đối...), Expected Result phải diễn đạt theo QUY TẮC binding ("khớp chính xác với dữ liệu đã nhập/đã đăng"), KHÔNG khẳng định 1 chuỗi cụ thể là "đúng". Giá trị quan sát được (nếu có) chỉ ghi ở cột Test Data với nhãn rõ "Ví dụ minh hoạ, không phải giá trị bắt buộc" | Áp dụng từ 2026-07-27 (user phản hồi: "data trong UI chỉ là tương đối, user có thể nhập khác đi, nên những case như 6.9 expected như v sẽ không đúng"). Đặc biệt lưu ý mốc thời gian tương đối (vd "15 phút trước") — giá trị này đổi liên tục theo thời gian thực, TUYỆT ĐỐI không hardcode 1 con số cố định làm Expected. |
| 6 | **`analyze-requirements` (mọi mode — INIT/DELTA/UPDATE) BẮT BUỘC phải có bước truy cập trực tiếp app FoxEco thật** (qua Chrome MCP hoặc tương đương — serve local bằng `python3 -m http.server` nếu file là bundler HTML cần origin http/https), KHÔNG được chỉ đọc tài liệu (BRD/Design/Figma) rồi suy luận hành vi UI | Áp dụng từ 2026-07-28 (user yêu cầu). Lý do: tài liệu và UI thật liên tục lệch nhau — đã phát hiện nhiều lần trong các đợt phân tích trước (field Email công ty người nhận không có trong BRD cũ nhưng có trong UI; validation gate mới ở wizard bước 1; danh mục Loại hàng BRD nói 5 mục nhưng UI vẫn 8; rule 5-ký-tự cho lý do huỷ có trong BRD nhưng UI không enforce; v.v.). Nếu chỉ đọc doc mà không verify UI, các discrepancy này sẽ bị bỏ sót hoàn toàn. Áp dụng cho cả DOC Registry: mỗi version PHẢI có ít nhất 1 DOC ID gắn với UI Confirmation qua Chrome MCP (không chỉ toàn văn bản). |
| 7 | **`generate-tc` phải áp dụng đủ 13-loại TC checklist cố định thứ tự** cho mỗi scenario/UI block: Permission/Role → UI/UX → Business Rules → Happy Path → Negative → Boundary → Validation → Combination → State → CRUD → Error Message → Performance → Data Consistency. Chỉ tạo TC cho loại có căn cứ thật trong spec (KHÔNG tự thêm để "lấp đầy" thứ tự). Edge case của chức năng nào → gom vào TC của loại tương ứng, KHÔNG tách thành loại/group riêng | Áp dụng từ 2026-07-28 (user yêu cầu, dán nguyên bảng 13-loại). Đây chính là §2 của `generate-tc/references/qc7-analysis.md` — dùng làm khung coverage bắt buộc dù project đang chạy mode `comprehensive` (8 kỹ thuật B1-B8 vẫn áp dụng để sinh data cho từng loại, vd Boundary dùng B3 BVA, Negative dùng B6 EG — 2 trục bổ sung cho nhau, không thay thế nhau). |
| 8 | **Cột Group trong TC-MASTER dùng đúng enum 4 giá trị `Functional / UI / Integration / Database`** — gán theo phạm vi test (bao nhiêu màn hình/hệ thống TC chạm vào), KHÔNG suy 1-1 từ loại QC7-Type. Quy tắc gán: Bước 1 ưu tiên cao nhất — `Integration` nếu Steps thao tác ở màn/hệ thống A rồi verify ở màn/hệ thống B; `Database` nếu verify thẳng data layer (không qua UI render) hoặc CRUD trực tiếp lên entity. Nếu không rơi vào 2 case trên → Bước 2: `UI` nếu TC chỉ verify hiển thị/layout (không có hành động thay đổi trạng thái); `Functional` nếu có hành động tương tác (click/nhập/chuyển tab...) dù QC7-Type là gì. Khi convert qua `skillconvert` (target `sheet`), map thẳng enum 4 giá trị này vào cột Group đích — KHÔNG cần đổi thêm | Áp dụng từ 2026-07-28 (user yêu cầu). Chi tiết đầy đủ + bảng tham chiếu QC7-Type→Group: `generate-tc/references/qc7-analysis.md §4`. Cột Notes (M) luôn ghi `QC7-Type: <TypeName>` song song, độc lập với Group — xem §5 cùng file. |
| 9 | **Cột Expected Result CHỈ ghi đúng nội dung kết quả mong đợi — KHÔNG chèn note, lưu ý cá nhân, hay bình luận (vd "(cần verify thêm)", "(lưu ý: ...)")** vào trong câu Expected | Áp dụng từ 2026-07-28 (user yêu cầu, mở rộng thêm cho Rule #2). Mọi ghi chú/cảnh báo/trạng thái-chưa-chắc-chắn phải đưa vào cột Notes (M), không trộn vào Expected Result — Expected chỉ mô tả kết quả hệ thống thật sự trả về. |
| 10 | **TC-MASTER Excel BẮT BUỘC có sheet `ALL`** gộp phẳng toàn bộ TC từ mọi sheet module/tab (giữ nguyên block-title row, thêm divider `═══ SHEET: <tên> ═══` trước mỗi sheet gốc) | Áp dụng từ 2026-07-28 (user yêu cầu — TC-MASTER v1.1 lần đầu thiếu sheet này). Đặt sau `Overview`/`Coverage Matrix`, trước các sheet module/tab riêng lẻ (khớp đúng thứ tự đã có ở TC-MASTER v1.0). |
| 11 | **Cột Steps của MỌI TC phải bắt đầu bằng bước đăng nhập FoxEco** (step 1 = "Đăng nhập thành công vào FoxEco (đúng vai trò tương ứng với TC), vào màn Trang chủ"), các step nghiệp vụ còn lại renumber tiếp theo sau | Áp dụng từ 2026-07-28 (user yêu cầu). Áp dụng cho toàn bộ TC-MASTER, không riêng sheet nào. |
| 12 | **Droplist/chip-select không cần liệt kê hết mọi giá trị** — chỉ cần 1 TC đại diện "chọn 1 giá trị bất kỳ" nếu các giá trị có hành vi hệ thống tương đương nhau; giá trị nào có hành vi khác biệt thật (business rule riêng) thì vẫn tách TC riêng. **Error Guessing (B6) và các case Validation cùng field/cùng nhóm được phép GỘP nhiều pattern vào 1 TC** (nhiều sub-step trong Steps + Expected Result nhiều dòng gạch đầu dòng `-` 1:1 theo sub-step, xem Rule #2) thay vì tách mỗi pattern 1 TC riêng | Áp dụng từ 2026-07-28 (user yêu cầu, sau khi TC-MASTER v1.1 lần đầu sinh quá nhiều TC lặp — vd Loại hàng 8 chip → 8 TC, EG 10-pattern/field → 10 TC/field). Từ 2026-07-29, Expected nhiều dòng dùng gạch đầu dòng `-` thống nhất với Rule #2 (không còn đánh số 1/2/3 kể cả case gộp này). |
| 13 | **Nếu màn hình cần test (theo Pre-condition) KHÁC màn Trang chủ** — do Rule #11 luôn cố định Step 1 kết thúc ở Trang chủ — **BẮT BUỘC chèn 1 Step 2 duy nhất mô tả gộp đường điều hướng thật** từ Trang chủ tới đúng màn đó (vd `Bấm "+" → "Tôi cần gửi hàng" → hoàn tất Wizard bước 1 với Loại hàng/Giá trị hàng hợp lệ, bấm "Tiếp theo" để sang Wizard bước 2`), rồi mới renumber tiếp các step nghiệp vụ còn lại từ 3. KHÔNG tách thành nhiều step nhỏ từng thao tác điền field trung gian | Áp dụng từ 2026-07-28 (user phát hiện: sau khi áp Rule #11, TC ở sheet Bảng tin/Đăng tin có Step 1 luôn dừng ở Trang chủ nhưng Step 2 lại thao tác thẳng ở màn khác — vd "1. ...vào Trang chủ / 2. Quan sát toàn bộ màn Bảng tin" — thiếu bước mở Bảng tin). Đã fix thủ công cho toàn bộ 86 TC (Bảng tin 14 + Đăng tin 72) ở TC-MASTER-v1.1 — mức độ điều hướng tăng dần theo độ sâu UI block (vd Wizard bước 3 cần mô tả đủ cả Wizard bước 1 + bước 2 đã hoàn tất). Expected Result KHÔNG đánh số cho step điều hướng này (numbering Expected tiếp tục quy ước cũ: chỉ đếm step nghiệp vụ thật, bỏ qua cả step 1 login lẫn step 2 điều hướng — xem case gộp ở Rule #12). |
| 14 | **Test Title cho case validation/error KHÔNG dùng nhãn kỹ thuật chung chung ("Kiểm tra Validation — ...")** — viết thẳng hành động/tình huống cụ thể (vd "Kiểm tra nhập sai định dạng email" thay vì "Kiểm tra Validation — nhập email sai định dạng"). **Expected Result CHỈ ghi đúng kết quả mong đợi, KHÔNG kèm giải thích/ghi chú nguồn gốc** (vd "(spec-only theo BRD D8.1, chưa tự verify UI enforce)", "(VAL-03 quy định...)", "(xem thêm TC Boundary riêng)") — **KHÔNG trích mã tham chiếu kiểu BRD/VAL-xx vào Expected**. Nếu hành vi thật sự chưa xác định rõ (không có cách diễn đạt chắc chắn nào), vẫn phải hỏi lại user theo Custom Rule #4, không tự ý viết Expected mơ hồ kèm ghi chú | Áp dụng từ 2026-07-28 (user yêu cầu, sau khi rà lại 82 TC sheet Đăng tin có quá nhiều note/mã tham chiếu làm rối Expected). Áp dụng cho toàn bộ TC-MASTER. |

## DOC Notation
req_notation: none
# none: doc không đánh số → traceability dùng DOC-ID §section
# Nguồn yêu cầu chính: sơ đồ luồng Figma board "Fox Eco Doc"
#   (https://www.figma.com/board/SEu9ekmu2wh1XxZCJkqAbP/Fox-Eco-Doc)
#   + bản HTML standalone thực thi được (FoxEco Demo 3 vai tro (standalone) (2).html)
