# FoxEco — Project Context

## Thông tin dự án (Project Info)
- **Tên dự án:** FoxEco
- **Loại sản phẩm:** SDK tích hợp vào app mobile **FoxPro** có sẵn (không phải web app độc lập)
- **Loại kiểm thử:** Smoke, Functional, Regression
- **Môi trường:** STG
- **URL:** N/A — xem `07_environments/environments.md` (host app, SDK version, platform)
- **Team:** Solo
- **QC phụ trách:** GiangDC2

## Version Info
- **Current version:** v1.0
- **Version history:** v1.0 (initial)
- **MASTER-MEMORY:** `02_analyze-requirements/MASTER-MEMORY.md`
- **Project Rules:** `02_analyze-requirements/Project_rule.md`

## Quy trình làm việc (Workflow)
```
00_input/v1.0/ (tài liệu gốc)
  → 01_test-plans/ (create-test-plan)
    → 02_analyze-requirements/v1.0/ (analyze-requirements)
      → 03_test-cases/v1.0/ (generate-tc → consolidate → TC-MASTER)
        → 11_tc-review/ (review-tc + review-src-tc)
          → 08_test-runs/ (execute)
            → 05_bug-reports/ (log bugs)
              → 09_reports/ (summary report)
```

## MEMORY Files
- **MASTER-MEMORY:** `02_analyze-requirements/MASTER-MEMORY.md` — cross-version registry
- **Version MEMORY:** `02_analyze-requirements/v1.0/MEMORY.md` — version-scoped analysis
- **Source-code MEMORY:** `10_source-code/MEMORY.md` — locators, page classes, implementation log

## Naming Conventions
- Documents: `DOC-v[VERSION]-[NN]`
- Scenarios: `SC-[MODULE]-[NNN]`
- Test cases: `TC-[MODULE]-[NNN]`
- TC Master: `TC-MASTER-v[VERSION].xlsx`
- Bug reports: `BUG-[NNN]-[short-title].md`
- Test runs: `TR-v[VERSION]-[YYYY-MM-DD].md`
- Reports: `REPORT-[TYPE]-v[VERSION]-[DATE].md`

## Folder Reference
| # | Folder | Mục đích | Skill liên quan |
|---|--------|----------|----------------|
| 00 | input/v1.0/ | Tài liệu đầu vào (theo version) | analyze-requirements |
| 00 | input/shared/ | Tài liệu dùng chung | analyze-requirements |
| 01 | test-plans/ | Test plan tổng thể | create-test-plan |
| 02 | analyze-requirements/ | MASTER-MEMORY + Project_rule | analyze-requirements |
| 02 | analyze-requirements/v1.0/ | Analysis output theo version | analyze-requirements |
| 03 | test-cases/v1.0/ | TC-MASTER + fragments | generate-tc |
| 04 | test-data/ | Dữ liệu test | — |
| 05 | bug-reports/ | Báo cáo lỗi | log-bug |
| 06 | checklists/ | Smoke + release checklists | — |
| 07 | environments/ | Config môi trường | — |
| 08 | test-runs/ | Logs chạy test | test-report |
| 09 | reports/ | Báo cáo tổng hợp | test-report |
| 10 | source-code/ | Automation code + MEMORY | scan-source, implement-auto |
| 11 | tc-review/ | Review reports (TC + SRC-TC) | review-tc, review-src-tc |

## Project Rules
→ Xem chi tiết: `02_analyze-requirements/Project_rule.md`

## Pipeline & Commands
- **PIPELINE.md** (root) — bản đồ pipeline QA, skill registry, prerequisites
- **COMMANDS.md** (root) — cheat-sheet lệnh gọi từng skill theo thứ tự pipeline

## Tools
- Manual testing project scaffolded by `init-manual-project` skill
- Framework version: Multi-Version (MASTER-MEMORY enabled)
- Created on: 2026-07-24

## Analyze Requirements — v1.0 (2026-07-24)
- **Nguồn:** DOC-v1.0-01 (BRD v3.1 · Gửi Hàng + Nền tảng chung), DOC-v1.0-02 (PRD tái dựng từ demo), DOC-v1.0-03 (prototype tương tác, reference-only).
- **Kết quả:** 8 module (USR, ORD, ASN, DLV, GIFT, CNL, NTF, TS) — 40 requirement, 62 scenario (P1:20 · P2:28 · P3:14), 16 clarification.
- **Cập nhật 2026-07-24 (bổ sung):** +4 scenario (SC-DLV-012/013/014, SC-GIFT-004) + REQ-GIFT-003, nguồn "Quan sát thực tế app STG" (QA GiangDC2) — ma trận nhãn nút/trạng thái theo vai trò tại màn Theo dõi đơn, xem `test_scenario_map.md` block "Theo dõi đơn — Ma trận nhãn nút theo trạng thái".
- **Cập nhật 2026-07-24 (bổ sung #3):** +1 clarification **C-USR-03 (Resolved)** — QA xác nhận app STG thật KHÔNG có chức năng cập nhật hồ sơ cá nhân (chỉ view-only), sửa lại scope REQ-USR-002/SC-USR-002.
- **✅ Cập nhật 2026-07-27 (BA/PO trả lời batch clarifications qua chat):** **Không còn BLOCKER cứng nào.** `C-ORD-02` (ngưỡng giá trị hàng) đã gỡ BLOCKER — BA/PO xác nhận phase này chưa làm, out of scope v1.0. Tổng cộng 13/16 clarification đã Resolved/Deferred:
  - **Resolved — Out of scope v1.0 (deferred to future phase):** `C-ORD-02` (ngưỡng giá trị hàng), `C-USR-01` (tier "Hạng Đồng hành"), `C-USR-02` (cấu hình kênh liên hệ), `C-GIFT-01` (rating 1-5 sao), `C-TS-01` (Admin Web Portal), `C-CNL-01` (màn Báo sự cố).
  - **Resolved — rule mới áp dụng ngay ở v1.0:** `C-ORD-01` (validate bắt buộc B1/B2, maxlength TBD), `C-ORD-03` (hạn tin = giá trị user chọn lúc đăng), `C-ORD-04` (không chặn "Thuốc/Y tế" ở v1.0), `C-ASN-01` (SĐT lộ SAU khi ghép — theo BRD), `C-ASN-02` (cấm tự nhận mang giúp đơn của mình), `C-DLV-03` (modal đơn giản là UI chính thức).
  - **Partially Resolved:** `C-NTF-02` (khớp tuyến = trùng địa chỉ giao + khung giờ phù hợp; còn thiếu định nghĩa độ lệch khung giờ + chu kỳ quét).
  - **Còn Open thực sự (chưa có câu trả lời):** `C-ORD-05` (biến thể "Mã tin" ở màn Đăng tin thành công), `C-NTF-01` (danh sách 9 loại thông báo chính thức — đã bổ sung bảng unified 3 nguồn để BA chọn, xem `MEMORY.md §6.1`), `C-DLV-02` (default bật/tắt chia sẻ vị trí).
- Chi tiết đầy đủ + status mới nhất từng clarification: `02_analyze-requirements/v1.0/MEMORY.md` §6/§6.1 Clarifications, `requirement_traceability.md` §2/§3, `risk_assessment.md`.
- **Cập nhật 2026-07-27 (rescan UI riêng màn Thông báo):** +1 scenario `SC-NTF-007` (empty state danh sách thông báo — chưa có bằng chứng UI, áp dụng lại pattern "Hiện tại chưa có dữ liệu" đã dùng ở SC-ORD-023/SC-GIFT-006, mở rộng `C-ORD-06`).
- **Cập nhật 2026-07-27 (gap khi review TC-NTF):** +2 scenario `SC-NTF-008` (đánh dấu đã đọc), `SC-NTF-009` (scroll load thêm dữ liệu), +1 clarification `C-NTF-03` (Open).
- **Cập nhật 2026-07-27 (fix finding health-check):** SC-ORD-015..026 (màn Hoạt động, đã có từ trước trong `test_scenario_map.md`) bị thiếu khỏi `MEMORY.md` §4 Scenario Index — đã sync lại. Tổng: 82 scenario (P1:19 · P2:37 · P3:26).
- **Cập nhật 2026-07-28 (BA cập nhật BRD lên v3.2):** so với v3.1, chỉ thêm 1 section mới `§D8 Validate & Giá trị mặc định (Form Rules)` — resolve dứt điểm maxlength còn TBD của `C-ORD-01`, hé lộ cơ chế cảnh báo "Giá trị hàng = Cao" (khác ngưỡng số tiền BR-ORD-03 vẫn deferred). +2 requirement, +5 scenario (4 ORD, 1 CNL), 1 scenario modified.
- **Cập nhật 2026-07-29 (chuẩn bị merge với QC khác trong team):** Team 2 người — người còn lại (anhdc4) tự phân tích + generate TC trên project riêng (dựa trên demo HTML), quyết định lấy project GiangDC2 (project này) làm base để gộp thành 1 project tổng, phần "chi tiết + flow" (Chi tiết tin/Theo dõi đơn/Huỷ đơn/Tặng quà) sẽ generate-tc từ scenario ASN/DLV/GIFT/CNL đã có sẵn. Trước đó bổ sung 2 màn dùng chung còn thiếu Block Definition (Trang chủ: Header/Banner/Card/bottom-nav; Bảng tin: danh sách card) từ nguồn `DOC-v1.0-02` đã có sẵn — +2 requirement, +2 scenario. Tổng hiện tại: **92 scenario** (P1:20 · P2:42 · P3:29 — đã trừ 1 DEPRECATED `SC-NTF-006`), **46 requirement**.
- **Cập nhật 2026-07-30 (HOÀN TẤT merge 2 project + generate TC 5 module mới):** Đã generate xong 5 module TC còn thiếu (`TC_05` Trang chủ 32 · `TC_06` Bảng tin & Chi tiết tin 31 · `TC_07` Theo dõi đơn 44 · `TC_08` Huỷ đơn 27 · `TC_09` Tặng quà 16 = **150 TC**), cộng 4 module cũ (171 TC) → **9 fragment / 321 TC**, tất cả `--mode comprehensive` + Coverage Matrix. Coverage: **85/92 scenario đã có TC**; 7 scenario còn lại đều có lý do (out of scope v1.0 / chờ PM chốt scope auto-match / SSO thuộc host app / DEPRECATED). **Đã rà đủ 15/15 clarification của project QC anhdc4 và merge nốt 5 gap** → `MEMORY.md §6` nay có **25 clarification** (thêm `C-ORD-07`, `C-CNL-02`, `C-ORD-08`, `C-ASN-03`, `C-GIFT-02`). **Folder `02_analyze-requirements CA` và `03_test-cases/TestCases-CA.xlsx` đã XOÁ** (2026-07-30) sau khi merge xong — nội dung gốc còn trong git commit `6f0b0cd`; mọi tham chiếu tới 2 path này trong CHANGELOG/Analyst Note chỉ là ghi chú xuất xứ lịch sử. **Chưa consolidate** — `generate-tc` §8 = PARTIAL, bước tiếp theo là `/generate-tc --consolidate` rồi `/review-tc` trên bộ 321 TC. **4 TC dự kiến FAIL có chủ đích** (ID đã đối chiếu lại với Excel ngày 2026-07-30 sau finding review-tc m9 — bản ghi cũ trích sai `TC_08.24/25`): `TC_08.7` (lý do huỷ 4 ký tự vẫn bật nút — CA live-verify UI chỉ chặn rỗng), `TC_08.10` (lý do huỷ 5 dấu cách vẫn bật nút — không trim trước khi đếm), `TC_08.22` + `TC_08.23` (huỷ đơn không ghi log LỊCH SỬ).24/25` (huỷ đơn không ghi log LỊCH SỬ). Chi tiết đầy đủ: `03_test-cases/v1.0/CHANGELOG.md` + `MASTER-MEMORY.md §8`.
- **Cập nhật 2026-07-30 (CONSOLIDATE — TC-MASTER hoàn chỉnh 9/9 module):** `/generate-tc --consolidate` đã gộp đủ 9 fragment → `03_test-cases/v1.0/ISC_FoxEco_v1.0_TC_v1_R1.xlsx` (alias `TC-MASTER-v1.0.xlsx`, `03_test-cases/TC-MASTER-LATEST.xlsx`) — **321 TC / 9 sheet chức năng** (TC_01 Hoạt động 20 · TC_02 Cá nhân 15 · TC_03 Thông báo 27 · TC_04 Đăng tin 109 · TC_05 Trang chủ 32 · TC_06 Bảng tin & Chi tiết tin 31 · TC_07 Theo dõi đơn 44 · TC_08 Huỷ đơn 27 · TC_09 Tặng quà 16), 9 sheet Coverage Matrix, RTM 41 Req ID, Dashboard 9 dòng. Verify LibreOffice recalc sạch (High 45/Medium 185/Low 91 = 321, ID `TC_01.1`→`TC_09.16` liên tục, round data trống, 0 diff so với fragment). **§8 generate-tc = COMPLETED.** Bước tiếp theo: `/review-tc` trên bộ 321 TC. Chi tiết: `03_test-cases/v1.0/CHANGELOG.md` (dòng cuối) + `MASTER-MEMORY.md §6/§8 Update 18`.
- **Cập nhật 2026-07-30 (REVIEW-TC + FIX toàn bộ finding):** `/review-tc` FULL trên 321 TC → **84/100 CONDITIONAL** (0 Critical · 2 Major · 10 Minor · 6 Info), G1 PASS — report `11_tc-review/review-report-v1.0.md`. **Đã fix hết 12 finding ngay sau đó** (sửa ở fragment rồi consolidate lại): +2 TC màn "Quà đã nhận" đóng gap coverage duy nhất (`TC_02.16` completeness, `TC_02.17` danh sách lịch sử — **cần vibe-test xác nhận** vì chỉ có bằng chứng văn bản US-D20) → **TC 321 → 323**; Remark `TC_03.1/2/3` về đúng trần 5 thông báo/tin đã chốt; Coverage Matrix `SC-NTF-006` (DEPRECATED) → `SC-ASN-013`; tách row gộp `SC-ORD-004/005`; chuẩn hoá 27 DOC Source; sửa ID 4 TC dự kiến FAIL. Verify: R1 sạch 17/17 · 9/9 matrix khớp số TC thật · Dashboard 323 · md5 `02f2a06bba65`. Bước tiếp theo: `/review-tc --recheck` để lấy điểm chính thức, rồi `/vibe-test`. ⚠ `review-tc` vẫn chạy **Direct mode** (skill thiếu `review-agent/AGENT.md`) nên score bị cap 85 và mang bias self-review.
- **Cập nhật 2026-07-31 (empty-state text từ ảnh chụp thật app STG + notification click-navigate):** User bổ sung 4 ảnh chụp THẬT app STG (`00_input/v1.0/Ảnh danh sách rỗng app stag thật/`) xác nhận text empty-state chính thức cho 3 màn (Hoạt động = "Chưa có đơn nào", Thông báo = "Chưa có thông báo nào", Quà đã nhận = "Chưa có quà nào" + subtitle) — thay bản placeholder generic cũ. `C-ORD-06` chuyển lại **Resolved** (có bằng chứng ảnh, khác lần Resolved 2026-07-28 đã bị revert vì thiếu bằng chứng). +9 TC mới (`TC_03.31..39`, sheet Thông báo) — click thông báo → điều hướng, mở rộng `SC-NTF-001..005`; cố ý không thêm case "Tin quá hạn"/"Nhắc khung giờ hẹn giao" theo yêu cầu user, `C-NTF-01` vẫn Open (baseline tạm). **KHÔNG đụng module Trang chủ** — còn chờ user trả lời câu hỏi khác (hành vi ẩn/hiện block "Đơn của tôi" khi rỗng + nguồn text "Tin mới" rỗng). TC-MASTER 337→**346**. Bước tiếp theo: `/review-tc --recheck` cho baseline mới nhất, rồi tiếp tục module Trang chủ khi có câu trả lời.
- **Cập nhật 2026-07-31 (module Trang chủ — ảnh chụp thật, CORRECTED rule sai):** User bổ sung ảnh chụp thật màn Trang chủ, trả lời nốt câu hỏi còn treo. Phát hiện quan trọng: rule gốc `DOC-v1.0-02` cho block "Đơn của tôi" ("chỉ hiện khi có đơn hoạt động") **SAI** so với UI thật — section LUÔN hiển thị, khi rỗng hiện text "Chưa có đơn nào" thay vì ẩn cả section. Sửa `TC_05.15` theo đúng hành vi (scenario mới `SC-ORD-037`, CORRECTED). Block "Tin mới" trước đây chưa từng có TC rỗng — +1 TC mới `TC_05.34` (scenario mới `SC-ASN-015`), text "Chưa có tin mới. Hiện chưa có tin nào gần bạn, quay lại sau nhé". TC-MASTER 346→**347**. Bước tiếp theo: `/review-tc --recheck` cho baseline mới nhất (347 TC).
- **Cập nhật 2026-07-31 (data hygiene toàn dự án — dọn Expected + chuẩn hoá DOC ID, theo yêu cầu user):** Xoá ghi chú/citation clarification ID lẫn trong Expected Result của 16 TC (6 sheet). Chuẩn hoá 108 cell "DOC Source" tự do về mã ID chuẩn — thêm 2 DOC ID mới vào Registry: `DOC-v1.0-07` (ảnh chụp thật app STG, file cụ thể lưu `00_input/`) và `DOC-v1.0-08` (gap marker — QA đề xuất, chưa có nguồn/xác nhận chính thức). RTM kiểm tra theo policy "chỉ thêm ID mới khi chiếm phần lớn TC của REQ" — không REQ nào đạt ngưỡng nên giữ nguyên. TC-MASTER vẫn = **347 TC** (không đổi số lượng, chỉ đổi nội dung/nguồn). Bước tiếp theo: `/review-tc --recheck`.
