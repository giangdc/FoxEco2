# MASTER-MEMORY — Cross-Version Registry

> Cập nhật lần cuối: 2026-07-28
> Active version: v1.1

## 1. Version Registry
| Version | Release Date | Input Folder | Analyze Folder | Status | Tổng DOC | Tổng SC (all) | Tổng SC (new+mod) | Parent |
|---------|-------------|-------------|----------------|--------|----------|--------------|-------------------|--------|
| v1.0 | — (chưa release, đang QA) | `00_input/v1.0/` | `02_analyze-requirements/v1.0/` | Analyzed | 3 | 51 | 51 | — |
| v1.1 | — (chưa release, đang QA) | `00_input/v1.1/` | `02_analyze-requirements/v1.1/` | Analyzed | 3 | 51 | 13 | v1.0 |

## 2. DOC ID Registry (Global)
| DOC ID | Version | File | Loại | Modules |
|--------|---------|------|------|---------|
| DOC-v1.0-01 | v1.0 | `00_input/v1.0/DOC-v1.0-01-FoxEco-Flow-Spec.md` | Markdown (tổng hợp Figma board + verified UI behavior) — nguồn phụ, superseded bởi DOC-v1.1-01/02 | SENDER, CARRIER, RECEIVER, ORDER, GENERAL |
| DOC-v1.0-02 | v1.0 | `00_input/v1.0/FoxEco BRD/FoxEco BRD v3.1 (1).html` | HTML — BRD FPT Telecom v3.1 (23/07/2026) — superseded bởi DOC-v1.1-01 (BRD v3.2) | SENDER, CARRIER, RECEIVER, OFFER, CANCEL, GIFT, NOTIFICATION, ORDER, ADMIN, MEDIA, GENERAL |
| DOC-v1.0-03 | v1.0 | `00_input/v1.0/DOC-v1.0-03-FoxEco-Design-Updated-Prototype.html` | HTML prototype — bản cập nhật của DOC-v1.0-01, verify qua Chrome MCP 2026-07-27 — superseded bởi DOC-v1.1-02 (Design v3.2) | GENERAL (bottom nav), NOTIFICATION, GIFT, ORDER (EXPIRED UI) |
| DOC-v1.1-01 | v1.1 | `00_input/v1.1/DOC-v1.1-01-FoxEco-BRD-v3.2.html` | HTML (bundler format) — BRD v3.2 (cập nhật 27/07/2026) — **nguồn chính thức hiện hành cho business rule**, thay thế DOC-v1.0-02 | SENDER, CARRIER, RECEIVER, OFFER, CANCEL, GIFT, NOTIFICATION, ORDER, ADMIN, MEDIA, GENERAL |
| DOC-v1.1-02 | v1.1 | `00_input/v1.1/DOC-v1.1-02-FoxEco-Design-v3.2.html` | HTML (bundler format) — Design/prototype v3.2, verify đầy đủ qua Chrome MCP 2026-07-28 (order lifecycle end-to-end, gift, cancel, profile) — **nguồn chính thức hiện hành cho UI thật**, thay thế DOC-v1.0-03 | SENDER, CARRIER, RECEIVER, ORDER, GIFT, GENERAL |
| DOC-v1.1-03 | v1.1 | Figma board "Fox Eco Doc" `SEu9ekmu2wh1XxZCJkqAbP` node 23:153 (pull qua Figma MCP) | FigJam board — design intent gốc, dùng re-verify (đặc biệt vai trò màn "Quà đã nhận") | GIFT, CANCEL, OFFER, ORDER |

## 3. Scenario Lifecycle (Cross-Version)
> Version ĐẦU (v1.0, tất cả NEW) dùng roll-up gọn. Từ v1.1 (delta) trở đi: liệt kê per-SC cho MODIFIED; CARRIED roll-up theo module (không đổi nội dung, xem `v1.0/test_scenario_map.md` cho chi tiết gốc).

### v1.0 (roll-up gốc — không đổi)
| Module | Origin | Lifecycle | Count |
|--------|--------|-----------|-------|
| SENDER | v1.0 | NEW | 10 |
| CARRIER | v1.0 | NEW | 9 |
| RECEIVER | v1.0 | NEW | 4 |
| OFFER | v1.0 | NEW | 4 |
| CANCEL | v1.0 | NEW | 4 |
| GIFT | v1.0 | NEW | 4 |
| NOTIFICATION | v1.0 | NEW | 2 |
| ORDER | v1.0 | NEW | 7 |
| ADMIN | v1.0 | NEW | 1 |
| MEDIA | v1.0 | NEW | 2 |
| GENERAL | v1.0 | NEW | 4 |

### v1.1 (delta từ v1.0) — per-SC cho MODIFIED
| SC ID | Origin | Lifecycle (v1.1) |
|-------|--------|-------------------|
| SC-SENDER-003 | v1.0 | MODIFIED |
| SC-SENDER-004 | v1.0 | MODIFIED |
| SC-SENDER-009 | v1.0 | MODIFIED (UNBLOCK) |
| SC-SENDER-010 | v1.0 | MODIFIED (UNBLOCK) |
| SC-RECEIVER-003 | v1.0 | MODIFIED |
| SC-ORDER-005 | v1.0 | MODIFIED (UNBLOCK partial) |
| SC-ORDER-006 | v1.0 | MODIFIED (UNBLOCK partial) |
| SC-ORDER-007 | v1.0 | MODIFIED (ngưỡng "Đến ngày" resolved; vẫn 🚫 Blocked cho TC thật vì thiếu backend/worker) |
| SC-GENERAL-003 | v1.0 | MODIFIED |
| SC-CANCEL-001 | v1.0 | MODIFIED |
| SC-GIFT-002 | v1.0 | MODIFIED |
| SC-GIFT-003 | v1.0 | MODIFIED (C-GIFT-2 resolved) |
| SC-GIFT-004 | v1.0 | MODIFIED (C-GIFT-2 resolved) |

**CARRIED (v1.1, 38 SC — không đổi nội dung):** SC-SENDER-001/002/005/006/007/008 (6), SC-CARRIER-001..009 (9), SC-RECEIVER-001/002/004 (3), SC-ORDER-001/002/003/004 (4), SC-GENERAL-001/002/004 (3), SC-OFFER-001..004 (4), SC-CANCEL-002/003/004 (3), SC-GIFT-001 (1), SC-NOTIFICATION-001/002 (2), SC-ADMIN-001 (1), SC-MEDIA-001/002 (2).

> **Cập nhật 2026-07-24 (v1.0):** +20 scenario mới (6 module mới + SENDER/ORDER mở rộng) sau khi tích hợp BRD v3.1 làm nguồn chính thức.
> **Cập nhật 2026-07-28 (v1.1, delta):** thay thế toàn bộ nguồn (BRD v3.2 + Design v3.2 + Figma re-check) — 0 SC mới/deprecated, 13/51 SC nâng CARRIED→MODIFIED (validation rule mới ở BRD §D8, 2 unblock — Chỉnh sửa đơn + Email autofill, 1 role-bug fix — Gift history). Chi tiết: `v1.1/MEMORY.md §4`.

## 4. Regression Scope
### v1.0
**Phải test (new + modified):**
| SC ID | Type | Lý do |
|-------|------|-------|
| SC-SENDER-005, SC-SENDER-006 | Functional/Validation | Gate điều khoản + happy path đăng tin |
| SC-CARRIER-002, SC-CARRIER-004, SC-CARRIER-005, SC-CARRIER-006 | Functional/Permission | Toàn bộ chuỗi transition + permission-boundary Carrier |
| SC-RECEIVER-003, SC-RECEIVER-004 | Functional/Permission | Transition cuối + permission-boundary Receiver |
| SC-ORDER-002, SC-ORDER-003 | Functional | Reset + đồng bộ real-time — differentiator chính của app |

**Nên regression (carried — high risk):**
| SC ID | Type | Lý do |
|-------|------|-------|
| _(không có — v1.0 là version đầu tiên, chưa có carried)_ | | |

**Không cần test (carried — low risk, stable):**
| SC ID | Type | Lý do |
|-------|------|-------|
| _(không có — v1.0 là version đầu tiên)_ | | |

### v1.1
**Phải test (new + modified):**
| SC ID | Type | Lý do |
|-------|------|-------|
| SC-SENDER-003 | Functional/Validation | Validation gate mới hoàn toàn đảo ngược hành vi v1.0 (trước "luôn khả dụng", nay có gate) |
| SC-SENDER-004, SC-SENDER-009, SC-SENDER-010 | Functional | Field Email công ty người nhận hoàn toàn mới trong UI |
| SC-RECEIVER-003 | Functional | SLA nhắc/admin cụ thể hoá — thêm nhánh test mới |
| SC-ORDER-005, SC-ORDER-006 | Functional/Permission | Unblock từ 🚫 Blocked — nút Chỉnh sửa đơn nay có UI |
| SC-ORDER-007 | State | Ngưỡng "Đến ngày" đã resolve — vẫn 🚫 Blocked cho TC thật vì thiếu cơ chế backend/worker trong prototype |
| SC-GENERAL-003 | UI/Functional | Cap-5 mới + phát hiện Sender cũng có "Tin mới" (C-GENERAL-4) |
| SC-CANCEL-001 | Validation | Discrepancy đã verify (BRD 5-ký-tự vs UI chỉ chặn rỗng) |
| SC-GIFT-002 | Functional | Verify đầy đủ lần đầu, text popup cuối khác nhẹ BRD |
| SC-GIFT-003, SC-GIFT-004 | Functional | C-GIFT-2 resolved — đổi precondition sang Carrier, không còn là case "kỳ vọng bug" |

**Nên regression (carried — high risk):**
| SC ID | Type | Lý do |
|-------|------|-------|
| SC-CARRIER-002, SC-CARRIER-004, SC-CARRIER-005, SC-CARRIER-006, SC-CARRIER-007 | Functional/Permission | Core order lifecycle — đã re-verify end-to-end ở v1.1 nhưng nên giữ trong regression suite vì là luồng chính của app |
| SC-ORDER-001, SC-ORDER-002, SC-ORDER-003, SC-ORDER-004 | Functional | Status machine + sync real-time — differentiator chính, rủi ro cao nếu regress |
| SC-CANCEL-002, SC-CANCEL-003, SC-CANCEL-004 | Functional/State | Cùng nhóm với SC-CANCEL-001 vừa phát hiện discrepancy — nên regression cùng đợt dù bản thân chưa đổi |

**Không cần test (carried — low risk, stable):**
| SC ID | Type | Lý do |
|-------|------|-------|
| SC-GENERAL-001, SC-GENERAL-002 | UI Content/Navigation | Nội dung tĩnh/navigation đơn giản, không có delta nào chạm tới |
| SC-NOTIFICATION-001, SC-NOTIFICATION-002 | Functional | Không có delta trong BRD v3.2/Design v3.2 cho module này |
| SC-ADMIN-001, SC-MEDIA-001, SC-MEDIA-002 | Permission/Functional | Vẫn 🚫 Blocked (không có UI), không đổi |

## 5. Version Comparison
### v1.1 vs v1.0
| Khía cạnh | v1.0 | v1.1 |
|-----------|------|------|
| Nguồn | DOC-v1.0-01 (Figma tổng hợp) + DOC-v1.0-02 (BRD v3.1) + DOC-v1.0-03 (Design prototype) | DOC-v1.1-01 (BRD v3.2) + DOC-v1.1-02 (Design v3.2) + DOC-v1.1-03 (Figma re-check) — **thay thế hoàn toàn**, không dùng lại nội dung 3 DOC cũ |
| Tổng REQ/SC | 38 REQ / 51 SC | 38 REQ / 51 SC (không đổi số lượng) |
| NEW/MODIFIED/CARRIED/DEPRECATED | 51/0/0/0 (version đầu) | 0/13/38/0 |
| Module mới | — | Không có (BRD v3.2 vẫn cùng phạm vi "01 Gửi Hàng", chỉ bổ sung validation rule chi tiết §D8) |
| Clarification mới | 7 (5 non-blocking + C-ORDER-2 + C-GENERAL-2 BLOCKER) | +4 mới, **cả 4 đã Resolved cùng ngày** (C-ORDER-2 đảo ngược v1.0 → "Đến ngày", C-SENDER-3 → giữ 8 category, C-CANCEL-1 → theo BRD, C-GENERAL-4 → áp dụng cả 2 vai trò); C-GIFT-2 đóng (Resolved); C-GENERAL-3 chuyển Partially Resolved (tier badge vẫn Open) |
| Blocker nghiêm trọng nhất | C-GENERAL-2 (rating vs quà ảo) — đã resolve trong version | Không còn blocker — 4/4 clarification mới đã resolve cùng ngày phát hiện (2026-07-28). Còn 1 action-item thật (không phải ambiguity): **C-CANCEL-1** — UI thiếu enforce rule 5-ký-tự theo BRD, cần dev fix. Còn 1 Open thật: **C-GENERAL-3** (tier badge) — chưa được hỏi trong đợt resolve này |
| TC-MASTER | 113 TC (v1.0, đã review 97-100/100) | Chưa generate — 13 SC MODIFIED cần TC mới/regenerate trước khi coi TC-MASTER hợp lệ cho v1.1 |

## 6. TC Files Registry
| Version | TC-MASTER File | Tổng TC | Ngày consolidate | Status |
|---------|---------------|---------|-------------------|--------|
| v1.0 | `03_test-cases/v1.0/TC-MASTER-v1.0.xlsx` | 113 (P1:20, P2:53, P3:40) — sheet "Trang chủ" (15 TC) + "Bảng tin" (19 TC) sau 2 vòng mở rộng field-level/data-binding, phần còn lại (SENDER/CARRIER/RECEIVER/ORDER/GENERAL cũ) chưa đổi ngoài việc di chuyển 3 TC CARRIER→Bảng tin | 2026-07-27 | ⚠️ Chưa review lại phần mới (Trang chủ/Bảng tin) — bản gốc 82 TC vẫn giữ nguyên trạng thái 97/100 APPROVED. **Base cho v1.1 nhưng 13 SC MODIFIED cần regenerate trước khi coi hợp lệ.** |
| v1.1 | `03_test-cases/v1.1/TC-MASTER-v1.1.xlsx` | 111 (P1:19, P2:52, P3:40) — sheet "Trang chủ" (25) + "Bảng tin" (14) + "Đăng tin" (72, sau khi gộp EG/EP/Validation theo yêu cầu user) + sheet `ALL` (gộp phẳng) | 2026-07-28 | ⚠️ PARTIAL — chỉ 3/6 sheet (Trang chủ/Bảng tin/Đăng tin); Hoạt động/Cá nhân/Thông báo chưa generate. Chưa review-tc. |

## 7. Downstream Path Registry
| Skill | Active Version Path |
|-------|-------------------|
| generate-tc | `03_test-cases/v1.1/TC-MASTER-v1.1.xlsx` (3/6 sheet xong — Trang chủ/Bảng tin/Đăng tin; v1.0 output vẫn tại `03_test-cases/v1.0/`) |
| review-tc | `11_tc-review/` |
| vibe-test | `08_test-runs/vibe/` |
| log-bug | `05_bug-reports/` |
| test-report | `09_reports/` |

## 8. Pipeline Status — v1.1
> Thứ tự + tên skill khớp PIPELINE.md. Status ∈ NOT_STARTED / IN_PROGRESS / PARTIAL / COMPLETED / SKIPPED / FAILED.
> **Lịch sử pipeline v1.0 đầy đủ** (init-project → generate-tc 113 TC → review-tc 95-100/100 → vibe-test partial) không lặp lại ở đây — xem git history của file này (commit trước 2026-07-28) hoặc `v1.0/MEMORY.md §8-9`.

| # | Skill | Status | Last Run | Scope | Output | Notes |
|---|-------|--------|----------|-------|--------|-------|
| 0.5 | init-source-code | SKIPPED | — | — | — | Automation = Không có |
| 1 | init-project | COMPLETED | 2026-07-24 | v1.0 (không đổi ở v1.1) | CLAUDE.md/PIPELINE.md/COMMANDS.md/Project_rule.md | — |
| 2 | create-test-plan | NOT_STARTED | — | — | — | — |
| 3 | analyze-requirements | **COMPLETED** | 2026-07-28 | v1.1 | `v1.1/MEMORY.md`, `requirement_traceability.md`, `test_scenario_map.md`, `test_data_catalog.md`, `risk_assessment.md`, `MASTER-MEMORY.md` | **Delta v1.1 từ v1.0.** Thay thế hoàn toàn nguồn (BRD v3.2 + Design v3.2 verify qua Chrome MCP + Figma re-check qua Figma MCP). 0 REQ/SC mới, 0 deprecated, **13/51 SC nâng CARRIED→MODIFIED**. Điểm nổi bật: (1) BRD v3.2 bổ sung khối §D8 validation rule chi tiết (char limit, format SĐT, boundary...) resolve nhiều "chưa xác định" cũ; (2) UNBLOCK 2 SC (Chỉnh sửa đơn) + 2 SC (Email autofill) nhờ UI mới xác nhận tồn tại; (3) **C-GIFT-2 RESOLVED** — bug role "Quà đã nhận" đã sửa, verify khớp Figma. **Cập nhật (lần 2, cùng ngày):** user resolve toàn bộ 4 clarification còn Open — (a) C-ORDER-2: ngưỡng EXPIRED = "Đến ngày" (đảo ngược resolution v1.0 "Từ ngày"); (b) C-SENDER-3: giữ 8 category Loại hàng theo UI, "Thuốc/Y tế" KHÔNG phải hàng cấm (đóng nghi vấn P1 kế thừa v1.0); (c) C-CANCEL-1: lấy theo BRD (tối thiểu 5 ký tự) làm target — UI hiện tại là gap thật cần dev fix; (d) C-GENERAL-4: "Tin mới" cap-5 áp dụng cho cả Sender lẫn Carrier. Còn lại 1 clarification Open thật (C-GENERAL-3 — tier badge "Hạng Đồng hành", chưa hỏi trong đợt này). |
| 4 | generate-tc | **PARTIAL** | 2026-07-28 | v1.1 | `03_test-cases/v1.1/TC-MASTER-v1.1.xlsx` | **111 TC — 3/6 sheet** (Trang chủ 25, Bảng tin 14, Đăng tin 72), theo cơ cấu sheet-by-bottom-nav-tab + sheet `ALL` gộp phẳng. Mode kết hợp `comprehensive` (B1 EP đại diện, B3 BVA, B6 EG gộp 3-nhóm) + 13-loại checklist qc7 (Custom Rule #7-9). Steps mọi TC bắt đầu bằng bước đăng nhập FoxEco (Custom Rule #10). 2 case để trống Expected có chủ đích (Trang chủ rỗng, Bảng tin rỗng — chờ user bổ sung). SC-CARRIER-009 (ảnh vắng mặt) KHÔNG generate (Expected vẫn chưa xác định, chưa có ngoại lệ). Còn thiếu sheet Hoạt động/Cá nhân/Thông báo. |
| 5 | review-tc | NOT_STARTED | — | v1.1 | — | Chờ generate-tc xong đủ 6 sheet, hoặc có thể review-tc từng phần cho 3 sheet đã xong |
| 6 | scan-source-code | SKIPPED | — | — | — | Automation = Không có |
| 7 | implement-automation | SKIPPED | — | — | — | Automation = Không có |
| 8 | review-src-tc | SKIPPED | — | — | — | Automation = Không có |
| 9 | vibe-test | NOT_STARTED | — | v1.1 | — | Verify UI đã làm trực tiếp trong lúc analyze-requirements (xem MEMORY.md §4.1 UI Confirmation) nhưng chưa chạy `vibe-test` chính thức với evidence lưu `08_test-runs/vibe/` cho v1.1 |
| 10 | execute-maintain | SKIPPED | — | — | — | Automation = Không có, dùng vibe-test thay thế |
| 11 | log-bug | NOT_STARTED | — | — | — | Ứng viên log-bug khi tới giai đoạn: UI leftover "★★★★★ Đã đánh giá" (C-GENERAL-2), tier badge (C-GENERAL-3) nếu user xác nhận cần bỏ |
| 12 | test-report | NOT_STARTED | — | — | — | — |
| 13 | health-check | NOT_STARTED | — | — | — | Khuyến nghị chạy sau khi generate-tc v1.1 để đối chiếu MEMORY/TC-MASTER/bug-index |

## 9. Notes
- **2026-07-28 (lần 2) — user resolve 4/4 clarification mới của v1.1.** Trả lời trực tiếp trong chat: (1) "Den ngay dung" → C-ORDER-2 = "Đến ngày" (đảo ngược v1.0); (2) "van 8 loai hang nhu UI nha, thuoc/y te khong phai hang cam" → C-SENDER-3 = giữ 8 category, Thuốc/Y tế không phải hàng cấm; (3) "lay theo rule BRD nha" → C-CANCEL-1 = theo BRD (5 ký tự tối thiểu), UI hiện tại là gap cần fix; (4) "viet theo UI luon nha" → C-GENERAL-4 = Tin mới áp dụng cả Sender lẫn Carrier. Đã cập nhật đồng bộ cả 5 file `v1.1/*.md` + `MASTER-MEMORY.md`. Còn lại 1 clarification thật sự Open (C-GENERAL-3, tier badge) chưa được hỏi trong đợt này.
- **2026-07-28 — analyze-requirements v1.1 DELTA = COMPLETED.** User cung cấp bộ tài liệu mới (BRD v3.2, Design v3.2, Figma board `SEu9ekmu2wh1XxZCJkqAbP`) yêu cầu KHÔNG dùng nội dung 3 DOC v1.0 cũ làm nguồn. Sau khi thảo luận, tạo version mới v1.1 (thay vì ghi đè v1.0) để giữ nguyên traceability review 97-100/100 + 113 TC đã làm cho v1.0. Quy trình: (1) 2 file BRD/Design v3.2 là "bundler" HTML tự giải nén qua JS — trích text bằng cách parse script tag `__bundler/template` cho BRD (đọc trực tiếp được), và serve local qua `python3 -m http.server 8767` + Chrome MCP để render Design (bundler cần origin http, không chạy qua `file://`); (2) verify UI trực tiếp toàn bộ order lifecycle posted→completed, gift flow, cancel flow, profile tab; (3) pull lại Figma board qua Figma MCP `get_figjam` để đối chiếu design intent gốc. Kết quả: 0 REQ/SC mới, 13/51 SC MODIFIED, quan trọng nhất là phát hiện **C-ORDER-2 cần re-confirm** (ngưỡng EXPIRED "Từ ngày" vs "Đến ngày") — đây là điểm cần user quyết định sớm nhất vì chặn trực tiếp SC-ORDER-007. Đầy đủ: `v1.1/MEMORY.md`.
- **2026-07-24 — INIT analyze-requirements:** Dự án chưa có SRS/URD chính thức. Nguồn requirement = tổng hợp Figma board "Fox Eco Doc" (flow diagram) + hành vi thực tế đã verify qua Chrome MCP (2 lần full-flow, PASS) trên bản HTML prototype `FoxEco Demo 3 vai tro (standalone)/...html`. Đã viết lại thành `DOC-v1.0-01-FoxEco-Flow-Spec.md` làm input chính thức trước khi phân tích, để đảm bảo có văn bản verbatim quote được thay vì suy diễn trực tiếp từ hội thoại.
- **Known scope limitation (không phải bug):** 3 nhánh nghiệp vụ mô tả trong Figma board — (1) Carrier tự đăng tin "Tôi nhận giao hàng", (2) Huỷ đơn, (3) Tặng quà cảm ơn — đều **chưa có UI** trong bản HTML prototype v1.0, đã ghi Clarification non-blocking (C-SENDER-1, C-CARRIER-1, C-CARRIER-2) và loại khỏi scope generate-tc v1.0.
- **2026-07-24 — Tích hợp BRD v3.1 (DOC-v1.0-02):** User cung cấp file BRD chính thức của FPT Telecom (`00_input/v1.0/FoxEco BRD/FoxEco BRD v3.1 (1).html`), đăng ký làm **nguồn chính thức** (ưu tiên cao hơn DOC-v1.0-01 tự tổng hợp trước đó khi có mâu thuẫn). Kết quả:
  - **Resolved 3 clarification cũ** (C-SENDER-1, C-CARRIER-1, C-CARRIER-2): cả 3 nhánh "chưa rõ scope" đều được BRD xác nhận **CÓ trong scope chính thức**, đặc tả rất chi tiết → nâng cấp từ Clarification thành 3 module mới (OFFER, CANCEL, GIFT) với đầy đủ REQ/SC.
  - **+6 module hoàn toàn mới:** OFFER (Carrier tự đăng tuyến), CANCEL (Huỷ đơn), GIFT (Tặng quà), NOTIFICATION (9 sự kiện), ADMIN (permission override, không có Admin Portal), MEDIA (ảnh bằng chứng + GPS).
  - **SENDER +1 REQ** (tự điền người nhận qua email công ty), **ORDER +2 REQ** (Chỉnh sửa đơn, Hết hạn tin EXPIRED).
  - **2 clarification mới:** C-ORDER-2 (ngưỡng hết hạn tin chưa xác định — BRD tự nêu là câu hỏi mở cho BA) và **C-GENERAL-2 (BLOCKER)** — mâu thuẫn nội bộ thật trong chính BRD giữa "không có rating sao" (§A7/BR-INT-06) và "Đánh giá 2 chiều 1-5 sao" (§D2/D3 RAT-01/02) — cần BA xác nhận trước khi viết TC cho bước ngay sau "Hoàn thành".
- **2026-07-27 — RESOLVED C-ORDER-2 & C-GENERAL-2 (user xác nhận trực tiếp):** (1) C-GENERAL-2: KHÔNG có rating sao — quà ảo (GIFT) thay thế hoàn toàn, §D2/§D3 RAT-01/02 là spec cũ không implement. (2) C-ORDER-2: ngưỡng EXPIRED = mốc tuyệt đối "Từ ngày" (field chọn ở wizard bước 2), KHÔNG phải duration cố định. Cả 2 module (rating step sau Hoàn thành, ORDER expiry) vẫn 🚫 Blocked cho TC thật vì thiếu UI, nhưng business rule đã đủ rõ để viết TC ngay khi dev implement. Chi tiết: `v1.0/MEMORY.md §6`.
- **2026-07-27 — LƯU Ý QUAN TRỌNG VỀ PLATFORM (user):** File HTML prototype hiện tại (`FoxEco Demo 3 vai tro (standalone)/`) **chỉ là bản demo** dùng để phân tích requirement/behavior. **App thật sẽ là Mobile App riêng (có icon riêng trên điện thoại)**, KHÔNG phải web. → Khi lên TC chính thức và implement automation sau này, phải viết theo platform **Mobile App** (dùng Appium, không phải Playwright/Chrome web), không phải theo hành vi browser/HTML của bản demo. Cần cập nhật `Project_rule.md` khi có thêm thông tin app thật (tên app, OS, cách cài) trước khi chạy `init-source-code`/`vibe-test` cho automation thật.
  - **Toàn bộ 20 SC mới đều 🚫 Blocked** cho generate-tc/vibe-test — BRD mô tả nhưng bản HTML prototype hiện tại (`FoxEco Demo 3 vai tro (standalone)`) chưa implement UI tương ứng. TC-MASTER hiện tại (26 TC) vẫn giữ nguyên, chỉ cover 24 scenario gốc — cần generate-tc lần 2 sau khi dev implement các module mới.
- **req_notation:** `none` — DOC-v1.0-01 không đánh số kiểu FR/VR/AC/UC; traceability dựa hoàn toàn vào `DOC-ID §section`.
