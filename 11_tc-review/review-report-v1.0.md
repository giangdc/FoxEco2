# TC Review Report — v1.0

> ## ✅ UPDATE 2026-07-30 — ĐÃ FIX TOÀN BỘ 12 FINDING (2 MAJOR + 10 MINOR)
> User yêu cầu fix hết. Đã sửa ở **fragment** rồi consolidate lại (đúng flow `generate-tc`), **không sửa tay vào TC-MASTER**.
> **TC: 321 → 323** (+2 TC đóng gap M1). Verify sau fix: LibreOffice recalc — Dashboard TOTAL **323** · Summary C17 323 · C12 = 9 sheet · High 45 / Medium 187 / Low 91 (=323) · ID liên tục `TC_01.1`→`TC_09.16` (Cá nhân giờ tới `TC_02.17`) · **R1 lại sạch 17/17, 0 finding cơ học** · 9/9 Coverage Matrix có `rowsum == footer == số TC thật` · RTM 41 Req, `SUM(E6:E46)`=357, 1 gap chủ đích `REQ-NTF-002`. 3 file output byte-identical (md5 `02f2a06bba65`).
>
> | Finding | Trạng thái | Đã làm gì |
> |---|---|---|
> | **M1** `R2-15` | ✅ FIXED | +2 TC vào `TC-CANHAN`: `TC_02.16` (completeness 3 thành phần màn "Quà đã nhận" — trạng thái có dữ liệu) và `TC_02.17` (danh sách lịch sử nhận quà). Cả 2 gắn cảnh báo `⚠ chỉ có bằng chứng văn bản US-D20, chưa có ảnh Figma/app STG → cần vibe-test` (Project_rule §10.1); `TC_02.17` Expected nêu rõ: nếu app KHÔNG có danh sách lịch sử thì TC FAIL và mở clarification với BA. Matrix Cá nhân: `SC-GIFT-003` 3→5 TC, footer 15→17 |
> | **M2** `R4-10` | ✅ FIXED | Viết lại Remark `TC_03.1/2/3` → `Trần 5 thông báo cho MỖI tin OFFER — OPR-01 / REQ-ASN-005 / SC-ASN-013, BA xác nhận qua chat 2026-07-29`, ghi rõ test data 3/5/6 tin là **giá trị chốt, không phải mock**. Bỏ sạch `N=3 mock`, `C-NTF-02`, `chưa chốt số` |
> | **m1** `R2-12` | ✅ FIXED | Row `SC-NTF-006` (DEPRECATED) trong `Coverage Matrix - Thông báo` không còn |
> | **m2** `R2-13` | ✅ FIXED | Chính row đó **đổi thành `SC-ASN-013`** (kèm title/source/technique đúng: `✅ 3 (BVA-min-1 / max / max+1 quanh trần 5)`) — vừa xoá scenario deprecated vừa trả 3 TC về đúng chủ sở hữu, footer ghi rõ "8 NTF còn hiệu lực + SC-ASN-013" |
> | **m3** `R2-13` | ✅ FIXED | Footer `Coverage Matrix - Trang chủ` 31 → **32** |
> | **m4** `R2-13` | ✅ FIXED | Tách row gộp `SC-ORD-004/005` → **`SC-ORD-005`** ("Tin tự động Hết hạn…", 2 TC) + note nêu rõ `SC-ORD-004` (Timeline) thuộc matrix Đăng tin. Note `SC-ORD-005` ở matrix Đăng tin: "100% (1/1)" → **"0 TC tại module này — cover tại TC_01 Hoạt động (TC_01.9/TC_01.10)"** |
> | **m5** `R1-17` | ✅ FIXED | `TC_04.81/82`: `Technique: VAL-02-…` → `Technique: N/A — baseline (derive trực tiếp từ rule VAL-02, BRD v3.2 §D8.3; không thuộc rubric B1–B8)`. Quét lại: **0 tag ngoài B1–B8** |
> | **m6** `R3-12` | ✅ FIXED | `TC_04.93` Expected bước 1/3 nêu thẳng giá trị: `'Tòa nhà Lô B3, KCX Tân Thuận, Q.7'` và `17:30–18:30 (BRD v3.2 §D8.2)` |
> | **m7** `R3-12` | ✅ FIXED | `TC_04.106` Expected bước 1 → `Màn hiển thị đúng tin đang mở: tên tin + badge trạng thái 'Đã ghép'` |
> | **m8** `R4-08` | ✅ FIXED | Viết lại `TC_03.8`/`TC_03.10` **chỉ assert vế thông báo** (title + steps + expected), DOC Source về đúng doc thật (`§D1b US-D09 + §D6` / `§A5 BR-CNF-04 + §D6`), Remark thêm dedupe trỏ `TC_07.16` và `TC_07.8/9/10`. Giữ nguyên vị trí sheet để không xáo ID |
> | **m9** `R4-10` | ✅ FIXED | Sửa ID trong `CLAUDE.md` + `MASTER-MEMORY §8` + `CHANGELOG`: **4 TC** `TC_08.7` · `TC_08.10` · `TC_08.22` · `TC_08.23` (kèm ghi chú bản cũ trích sai `TC_08.24/25`) |
> | **m10** `R4-07` | ✅ FIXED | Chuẩn hoá **27 DOC Source** phi-tài-liệu về 1 vocabulary — mọi nhãn giờ đều có (nguồn/ai) + (ngày) + (clarification ID & trạng thái): `QA xác nhận app STG (2026-07-28) · C-ORD-06 Resolved` · `QA đề xuất — Chờ BA/Dev — C-NTF-03 (Open)` · `Chờ BA — C-NTF-01 (Open)` · `BA xác nhận qua chat (2026-07-29)` · `Quan sát thực tế app STG (QA GiangDC2, chat 2026-07-27)` · `DOC-v1.0-01 §D1b (US-D20) + quan sát app STG…`. Quét lại: **0 TC còn nhãn cũ**. Đồng thời sửa 3 TC bị gán sai "Chờ BA bổ sung" dù Remark của chính nó ghi C-ORD-06 **Resolved** |
>
> **6 INFO không sửa (có lý do):** i1/i2 là trạng thái đúng của pipeline · i3 (technique tag dạng `EP-…` thay vì `B1-EP-…`) nhất quán 100% toàn project, sửa thì phải sửa 213 ô + đổi convention ở skill → nên chốt ở `generate.md` trước · i4 rubric khoẻ · i5 badge đã có TC riêng nên không mất coverage · i6 hợp lệ.
>
> **Score sau fix (ước tính):** 0 Critical · 0 Major · 0 Minor trên 12 finding đã đóng → **~100/100** trước cap; nhưng đây vẫn là **self-review** nên điểm chính thức phải chờ `/review-tc --recheck` (và tốt nhất là sau khi bổ sung `review-agent/AGENT.md` để chạy agent mode thật). Phần dưới là **báo cáo gốc trước khi fix**, giữ nguyên để truy vết.

---

> Generated: 2026-07-30
> Mode: **Direct** (⚠ xem Disclaimer)
> TC-MASTER: `03_test-cases/v1.0/TC-MASTER-v1.0.xlsx` (ISC: `ISC_FoxEco_v1.0_TC_v1_R1.xlsx`, alias `03_test-cases/TC-MASTER-LATEST.xlsx` — 3 file byte-identical md5 `153980f417df`)
> Scope: **321 TC / 9 sheet chức năng** (TC_01..TC_09) + 9 sheet Coverage Matrix + 8 sheet chuẩn ISC
> Mode generate: `comprehensive` (R1-17 + R2-13 + R2-14 enforced) · Part 2 verbatim quoting: enabled (R3-13 enforced)
> Score: **84/100 — CONDITIONAL** · Quality Gate G1: **PASS** (≥70)
> Bản review trước (2026-07-29, 175 TC / 4 sheet, score 70→~91 sau fix): `review-report-v1.0-ARCHIVE-2026-07-29-175TC-4sheet.md`

## ⚠ Disclaimer — Direct mode

Skill `review-tc` quy định gọi **independent reviewer agent** qua Anthropic API, đọc system prompt từ `~/.claude/skills/review-tc/review-agent/AGENT.md`. **File này vẫn KHÔNG tồn tại** trong skill đã cài (chỉ có `SKILL.md` + `references/{full,module,recheck}.md`) → không chạy được agent mode. Theo `SKILL.md` ("Independent reviewer API fail → fallback direct + disclaimer"), review này chạy **Direct mode**, tức là **self-review, có bias** vì cùng phiên đã consolidate bộ TC này. Score bị **cap 85**; score tính được là 84 (dưới cap nên không bị điều chỉnh).

Muốn score độc lập thật: bổ sung `review-agent/AGENT.md` vào skill rồi chạy `/review-tc --recheck`.

## Cách kiểm chứng (không đọc từ MEMORY summary)

- Parse trực tiếp bằng `openpyxl` **2 lần**: `data_only=False` (đối chiếu formula cột A/AM/AN/AO có bị gõ đè) và `data_only=True` trên bản **LibreOffice headless recalc** — file gốc do openpyxl ghi nên không có cached value, đọc thẳng sẽ ra `None` cho mọi Testcase ID.
- Duyệt **cả 9 sheet TC**, không chỉ sheet đầu; 321/321 row có DOC Source đều được kiểm.
- Đối chiếu chéo: `MEMORY.md §3/§4/§6/§9`, `test_scenario_map.md` (41 Block Definition + Source Quote), `test_data_catalog.md`, `requirement_traceability.md`, `BRD v3.2 §D8`, sheet `RTM` / `Dashboard` / 9 `Coverage Matrix`.

## Summary

| Severity | Count |
|----------|-------|
| 🔴 CRITICAL | **0** |
| 🟠 MAJOR | **2** |
| 🟡 MINOR | **10** |
| 🔵 INFO | 6 |

## Findings

### 🔴 CRITICAL — không có

R1 Structural Integrity **sạch 17/17 check** — chi tiết ở §Version-Specific Checks.

### 🟠 MAJOR

#### M1 · `R2-15` — Field/Column completeness gap: "Danh sách lịch sử" màn "Quà đã nhận" chưa có TC nào
- **Sheet/TC:** `Test Case 2` (TC_02 Cá nhân) — thiếu TC
- **Nguồn:** `test_scenario_map.md` → Block Definition `GIFT / Cá nhân (mục Quà đã nhận) / Quà đã nhận (màn riêng)` — 4 thành phần: (1) Icon quay lại, (2) Card đếm số, (3) **Danh sách lịch sử**, (4) Empty state. Source Quote #1 (US-D20, verbatim): *"tôi muốn xem tổng hợp 'Quà đã nhận' (**đếm theo loại + lịch sử**)"*.
- **Issue:** TC hiện có chỉ phủ 3/4 thành phần — TC_02.15 (icon quay lại), TC_02.12/13/14 (card đếm số), TC_02.11 (empty state). **Thành phần "Danh sách lịch sử" = 0 TC**, và KHÔNG có TC completeness nào liệt kê đủ 4 thành phần của màn này (TC_02.3 là completeness cho *header màn Cá nhân*, khác màn).
- **Suggestion:** bổ sung 2 TC vào `fragments/TC-CANHAN-v1.0.xlsx` — (a) `Check đầy đủ + đúng 4 thành phần hiển thị tại màn "Quà đã nhận"` (Group=UI), (b) `Check danh sách lịch sử nhận quà hiển thị đúng ...` — rồi `/generate-tc --sync`. Nếu "lịch sử" thực tế KHÔNG có trên UI STG thì phải mở clarification + ghi Analyst Note, không im lặng bỏ qua.

#### M2 · `R4-10` — Remark của TC_03.1/2/3 mâu thuẫn chính nội dung TC và trái Version MEMORY
- **Sheet/TC:** `Test Case 3` — `TC_03.1`, `TC_03.2`, `TC_03.3` · field **AP (Remark)**
- **Issue:** Title/Pre-condition/Steps/Expected của 3 TC đã viết theo **trần 5 thông báo / 1 tin** (rule BA đã chốt: `OPR-01` → `REQ-ASN-005` → `SC-ASN-013`, xem `MEMORY.md` bổ sung #11 và #12 ngày 2026-07-29). Nhưng Remark vẫn là bản cũ:
  - TC_03.1 — `Technique: BVA-min-1 (test lần thứ N-1=2, N=3 giá trị mock — C-NTF-02 Partially Resolved, ngưỡng thật chưa chốt số)`
  - TC_03.2 — `Technique: BVA-max (test đúng tại ngưỡng N=3 giá trị mock — ...)`
  - TC_03.3 — `... | Ngưỡng cụ thể (bao nhiêu lần/ngày) vẫn Open (C-NTF-02, Partially Resolved) — cần BA chốt số trước khi coi test data là final`
- **Sai 3 điểm:** (1) ngưỡng `N=3 mock` ≠ `5` đang dùng thật trong Steps/Expected; (2) trích **sai clarification** — `C-NTF-02` là về *điều kiện khớp tuyến* (độ lệch khung giờ + chu kỳ quét), không phải trần thông báo; (3) sai **trạng thái** — nói "chưa chốt số / vẫn Open" trong khi BA đã chốt, và chính vì đã chốt nên `SC-NTF-006` (trần theo NGÀY) mới bị DEPRECATED.
- **Hệ quả:** người execute đọc Remark sẽ dựng test data 3 tin thay vì 5, hoặc treo TC chờ BA vô ích.
- **Suggestion:** viết lại Remark 3 TC → `Technique: BVA-min-1|max|max+1 (trần 5 thông báo/1 tin — OPR-01/REQ-ASN-005, BA xác nhận 2026-07-29; SC-ASN-013)`, bỏ mọi tham chiếu `C-NTF-02` và "chưa chốt số".

### 🟡 MINOR

| # | Check | Sheet / TC | Field | Issue | Suggestion |
|---|-------|-----------|-------|-------|-----------|
| m1 | `R2-12` | `Coverage Matrix - Thông báo` row 7 | SC ID | Vẫn có row `SC-NTF-006` **(DEPRECATED 2026-07-29)** và ghi nhận **3 TC** cho nó | Xoá row (hoặc đánh dấu DEPRECATED, 0 TC) trong `fragments/TC-NTF-v1.0.xlsx` |
| m2 | `R2-13` | Toàn bộ 9 Coverage Matrix | SC ID | **`SC-ASN-013` — chủ sở hữu thật của TC_03.1-3 — không có row ở BẤT KỲ matrix nào.** Cùng gốc với m1/M2: TC đã đổi scenario nhưng matrix chưa theo | Thêm row `SC-ASN-013` (3 TC, B2 BVA ×3) vào matrix Thông báo. Cặp m1+m2 làm `test-report §8` và `health-check C-08/C-09` báo sai coverage cho 2 scenario |
| m3 | `R2-13` | `Coverage Matrix - Trang chủ` footer | Total TCs | Footer ghi `Total TCs derived: 31` nhưng per-row sum = **32** và sheet TC_05 có **32 TC** thật (stale sau khi thêm 1 TC ngày 2026-07-30) | Sửa footer → 32 |
| m4 | `R2-13` | `Coverage Matrix` (Hoạt động) | SC ID | Row gộp **`SC-ORD-004/005`** — 2 SC ID trong 1 dòng, phá parse SC↔TC của tool downstream. Hệ quả kèm theo: `SC-ORD-005` ở matrix Đăng tin ghi **0 TC** nhưng note "100% (1/1)" → parser naive kết luận SC-ORD-005 chưa có TC | Tách thành 2 row `SC-ORD-004` / `SC-ORD-005` với số TC đúng; sửa note của `SC-ORD-005` ở matrix Đăng tin thành dạng "cover tại TC_01 (Hoạt động)" |
| m5 | `R1-17` | `Test Case 4` — TC_04.81, TC_04.82 | AP | Gắn `Technique: VAL-02-inline-blur` / `VAL-02-scroll-to-first-error` — **`VAL-02` là rule ID của BRD v3.2 §D8.3**, không thuộc bộ technique `B1..B8` mà R1-17 yêu cầu | Đổi sang technique thật (2 TC này là EP/EG của cơ chế báo lỗi), đẩy `VAL-02` sang phần nguồn: `Technique: EG-error-display | Rule: VAL-02 (BRD v3.2 §D8.3)` |
| m6 | `R3-12` | `Test Case 4` — TC_04.93 | I | Expected bước **1 và 3** = "Field hiển thị đúng giá trị mặc định" — không nêu giá trị nên tự nó không verify được. Steps thì có (`'Tòa nhà Lô B3, KCX Tân Thuận, Q.7'`, `17:30–18:30`). TC_04.63 cùng chủ đề lại ghi rõ giá trị → **không nhất quán trong cùng sheet** | Nêu thẳng giá trị vào Expected (đã verify khớp `BRD v3.2 §D8.2` + `test_data_catalog.md` dòng "Thời gian di chuyển (OFFER, D8.2)") |
| m7 | `R3-12` | `Test Case 4` — TC_04.106 | I | Expected bước 1 "Màn hiển thị đúng thông tin tin" mơ hồ (assert thật nằm ở bước 2: không còn nút 'Chỉnh sửa') | Bỏ bước 1 hoặc nêu cụ thể trường cần thấy |
| m8 | `R4-08` | `Test Case 3` — TC_03.8, TC_03.10 | D/F/H/I | 2 TC nằm trong sheet **Thông báo** nhưng assertion chính là **state-transition guard của màn Theo dõi đơn** (chặn MATCHED→DELIVERED bỏ bước; Receiver không chốt được khi chưa DELIVERED); phần thông báo chỉ là mệnh đề phụ. Trùng lõi với `TC_07.16` (`ST-invalid-matched-delivered`) và `TC_07.8/9/10` (Receiver confirm bị chặn ở 3 trạng thái). **Đúng loại đã bị xoá có chủ đích** ở `TC_03.12` ngày 2026-07-28 với cùng lý do | Hoặc viết lại 2 TC chỉ assert phần thông báo ("KHÔNG phát sinh thông báo X khi transition bị chặn"), hoặc xoá và để `TC_07` giữ. Nếu giữ thì ghi Remark dedupe trỏ `TC_07.16` / `TC_07.8-10` |
| m9 | `R4-10` | Doc ↔ Excel | — | `CLAUDE.md` + `MASTER-MEMORY §8` + `CHANGELOG` ghi *"3 TC dự kiến FAIL có chủ đích: TC_08.7, TC_08.24/25"*. Thực tế trong TC-MASTER là **4 TC: `TC_08.7`, `TC_08.10`, `TC_08.22`, `TC_08.23`** (cả 4 đều đã ghi rõ ⚠ trong Remark — **phía Excel ĐÚNG, phía doc SAI**). `TC_08.24/25` là 2 TC khác hẳn (Carrier huỷ nhận → đơn về "Chờ ghép"). ID lệch vì fragment thêm 2 TC sau khi note được viết | Sửa 3 file doc về đúng 4 ID. Nếu không, người execute mở sai TC và log bug sai |
| m10 | `R4-07` | 27 TC / 9 sheet | C | DOC Source dùng **5 cách diễn đạt khác nhau cho nguồn phi-tài-liệu**: `Chờ BA bổ sung` ×11, `BA xác nhận qua trao đổi (chat), 2026-07-29` ×7, `UI nền tảng (scroll-load)` ×5, `QA đề xuất hành vi` ×2, `DOC-v1.0-04 / QA đề xuất hành vi` ×2 → không filter được khi rà traceability, và `Chờ BA bổ sung` không cho biết đang chờ clarification nào | Chuẩn hoá 1 vocabulary kèm ID clarification, vd `QA đề xuất — C-ORD-06 (Resolved)` / `Chờ BA — C-NTF-01 (Open)` |

### 🔵 INFO

| # | Check | Nội dung |
|---|-------|----------|
| i1 | `R2-07` | **Coverage 85/92 scenario (92.4%)**. 7 scenario chưa có TC, tất cả đều có lý do đã ghi trong MEMORY: `SC-TS-001/002/003` (Admin/Trust&Safety — `C-TS-01` Resolved/Deferred, out of scope v1.0) · `SC-ASN-006/009` (engine tự quét khớp tuyến — Phase 1 Scope, **chờ PM chốt**) · `SC-USR-001` (đăng nhập SSO — thuộc host app FoxPro) · `SC-NTF-006` (DEPRECATED). **Không phát sinh R2-01/R2-02** — không NEW/MODIFIED scenario nào bị bỏ sót ngoài danh sách trên. |
| i2 | `R2-09` `R2-10` | RTM `% phủ` = **0% cho cả 41 Req** — đúng trạng thái pipeline (chưa chạy round execution nào). RTM tổng "Số TC" = 355 > 321 là ĐÚNG: 1 TC gắn nhiều Req được đếm cho từng Req (đã ghi rõ ở dòng ghi chú RTM). |
| i3 | `R1-17` (format) | **213/213 technique tag** dùng dạng `EP-…`/`BVA-…`/`ST-…`/`EG-…`/`DT-…` thay vì `B1-EP-…` như `generate.md` quy định. Nhất quán 100% toàn project (không phải lỗi ngẫu nhiên) → nên chốt lại convention ở skill hoặc chuẩn hoá 1 lượt, không tính lỗi từng TC. |
| i4 | `R2-14` | Phân bố technique: **EP 106 (50%)** · BVA 48 · ST 30 · EG 19 · DT 8. Không technique nào >70% → rubric KHÔNG bị over-apply. PW/CRUD/CEG = 0, đều đã log `N/A` kèm lý do per-cột trong Coverage Matrix. |
| i5 | `R2-15` | TC_06.1 (completeness card Bảng tin) liệt kê 5 trường, **không gồm badge "Tin của bạn"** dù Block Definition có. Không mất coverage — badge có 2 TC riêng `TC_06.2`/`TC_06.3` (có/không) — chỉ là enumeration chưa trọn. |
| i6 | `R1-17` | **55 TC có Remark trống** = baseline TC (không phải derived) → hợp lệ với comprehensive mode; footer matrix Hoạt động/Cá nhân ("baseline 13 + derived 7", "baseline 10 + derived 5") xác nhận quy ước Total = baseline + derived. |

## Version-Specific Checks

| Check | Result |
|-------|--------|
| CARRIED TCs included (Remark tag) | **N/A** — v1.0 là version đầu, MASTER-MEMORY §4 regression scope rỗng (0/0). R2-11 / R4-09 / R4-10-carried không áp dụng |
| DEPRECATED TCs removed | **Y ở sheet TC** (0/321 TC gắn `SC-NTF-006`) · **N ở Coverage Matrix** → xem m1 |
| RTM: mọi Req ID có row + đủ term COUNTIF | **Y** — 40/40 Req ID xuất hiện trong sheet TC đều có row; 41 row × 4 công thức (E/F/G/H) đều nối đủ **9 term** cho 9 sheet; 0 orphan |
| RTM: row "Tổng" range SUM bao hết Req ID | **Y** — `SUM(E6:E46)` phủ đúng data row 6→46, không sót 18 Req ID mới thêm |
| Dashboard: mọi sheet TC có row tương ứng | **Y** — 9/9, cột D khớp **100%** tên tab thật; TOTAL recalc = 321 |
| Cột A / AM / AN / AO vẫn là formula | **Y** — 321/321 row, 0 ô bị gõ giá trị tĩnh (R1-01 & R4-11 sạch) |
| Round data N–AL trống | **Y** — 321 row × 25 cột, 0 ô có dữ liệu (R1-15 sạch) |
| Enum Group / Priority / Origin / Review | **Y** — 100% hợp lệ. Group: Functional 208 · UI 112 · Integration 1. Priority: High 45 · Medium 185 · Low 91 (=321, khớp Summary C19/20/21) |
| Testcase ID liên tục, không trùng | **Y** — `TC_01.1`→`TC_01.20`, `TC_02.1`→`TC_02.15`, … `TC_09.1`→`TC_09.16`; 0 duplicate, 0 nhảy số, 0 phantom row |
| Steps ↔ Expected numbering | **Y** — 321/321 hợp lệ theo convention project (Expected đánh số theo *step có kết quả cần assert*, là subset của step numbers): 0 TC tham chiếu step không tồn tại, 0 TC thiếu Expected cho step cuối |
| Title bắt đầu bằng "Check" (Guideline mục 3) | **Y** — 321/321 |
| Pre-condition / Steps / Expected trống | **0** (R1-07 / R1-08 / R1-09 sạch) |
| Automated / Script consistency | **Y** — 321 TC đều `Automated=No`, Script trống |
| R3-13 verbatim drift vs Source Quote | **Sạch trên mẫu kiểm** (TC_08.1 popup Huỷ nhận đơn · TC_06.1 card Bảng tin · TC_09.3/9.4 màn + chip Tặng quà · TC_04.63 default Thời gian · TC_01.9 dòng lý do Hết hạn) — Expected trích đúng verbatim từ Source Quote / ảnh Figma; default `17:00–18:30` (NEED §D8.1) vs `17:30–18:30` (OFFER §D8.2) dùng đúng cho từng form |
| R3-03 test data inline trong Steps | **Y** — 0/321 TC có bước "nhập/điền" mà thiếu giá trị cụ thể inline |
| R3-08 Pre-condition trùng Steps | **0** — pattern "Pre = trạng thái đã đăng nhập / Steps = điều hướng" dùng nhất quán, không phải duplication |
| R3-11 Step > 200 ký tự | **0** |
| R4-06 Duplicate TC (trùng Title) | **0** trùng tuyệt đối; 1 cặp trùng *lõi assertion* → xem m8 |
| R2-03 / R2-08 negative + happy path per module | **Y** — 9/9 module đều có cả TC positive và negative |
| R2-05 UI TC per module | **Y** — 9/9 module đều có ≥2 TC Group=UI |
| R2-15 Field/Column completeness | **42 TC completeness** phủ **32/33 block có ≥2 field** → 1 gap = M1. Block `DLV / Xác nhận đã nhận hàng (đầy đủ)` cố ý 0 TC (`C-DLV-03` Resolved — out of scope v1.0); block `USR / Kênh liên hệ` cố ý 0 TC hành vi (`C-USR-02` Resolved — phase sau, chỉ có TC_02.10 xác nhận GAP) |

## Score Breakdown

```
Score = 100 - (CRITICAL×5 + MAJOR×3 + MINOR×1)
      = 100 - (0×5 + 2×3 + 10×1)
      = 100 - 16
      = 84
```

| | |
|---|---|
| **Verdict** | **CONDITIONAL** (70–89 — fix recommended) |
| **Quality Gate G1** | **PASS** (≥70) → downstream KHÔNG bị block |
| Direct-mode cap | 85 (score 84 dưới cap → không bị điều chỉnh) |

So với bản review trước (2026-07-29): scope tăng 175 → **321 TC**, sheet 4 → **9**, Critical **4 → 0**, Major **3 → 2**, score **70 → 84**. Toàn bộ finding cấu trúc/RTM/Dashboard của lần trước đã đóng; 2 Major còn lại là **gap coverage mới phát hiện** (M1) và **metadata drift** (M2), không phải finding cũ tái diễn.

## Recommendations — thứ tự nên làm

1. **Fix M2 + m1 + m2 cùng lúc** (1 gốc: TC_03.1-3 đã đổi scenario `SC-NTF-006` → `SC-ASN-013` ngày 2026-07-29 nhưng Remark + Coverage Matrix chưa theo). Sửa ở `fragments/TC-NTF-v1.0.xlsx` rồi `/generate-tc --sync`.
2. **Fix M1** — bổ sung 2 TC màn "Quà đã nhận" (completeness 4 thành phần + danh sách lịch sử) vào `fragments/TC-CANHAN-v1.0.xlsx`. Đây là **gap coverage thật duy nhất** tìm được trong 321 TC.
3. **Fix m9 ngay** (rẻ nhất, rủi ro cao nhất khi execute): sửa 4 ID TC dự kiến FAIL trong `CLAUDE.md` / `MASTER-MEMORY §8` / `CHANGELOG`.
4. Nhóm matrix/metadata: m3, m4, m5, m10.
5. Nhóm nội dung: m6, m7, m8.
6. **Trước khi execute:** chốt với PM 2 scenario `SC-ASN-006/009` (auto-match) và 5 nhánh phụ DLV (`SC-DLV-001/002/003/004/008`) — TC đã viết sẵn nhưng scope chưa chốt; xác nhận với Dev/DevOps khả năng **mock thời gian** trên STG cho `TC_07.35/36/37` (BVA ngưỡng 2h/4h), nếu không mock được thì 3 TC này phải chuyển sang kiểm thử tầng backend/log.
7. Chạy `/review-tc --recheck` sau khi fix — muốn score độc lập thật thì bổ sung `review-agent/AGENT.md` vào skill trước.
