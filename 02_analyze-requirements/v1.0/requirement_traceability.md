# Requirement Traceability — v1.0

> Tạo bởi: analyze-requirements. Ma trận truy vết REQ ↔ DOC ↔ Scenario ↔ Clarification.
> Text-level traceability: Source Quote per REQ ở `MEMORY.md §4.1`, per SC ở `test_scenario_map.md`.
> `req_notation` (xem `Project_rule.md §9`): tài liệu dự án đã có ID module-prefixed riêng (vd `ORD-01`, `BR-CNL-01`, `US-D16`) — cột **Maps (Ref DOC)** dùng ĐÚNG ID gốc đó, không quy đổi sang FR/VR/AC/UC.
>
> **Structure-lock:** giữ nguyên header cột + section dưới đây. KHÔNG tự thêm/bớt/đổi tên cột.

## 1. Traceability Matrix (REQ → DOC → SC)

### Module USR — DOC-v1.0-01
| REQ ID | Maps (Ref DOC) | DOC §section | Scenarios | Clarification |
|--------|----------------|--------------|-----------|---------------|
| REQ-USR-001 | USR-01 | §A6 | SC-USR-001 | — |
| REQ-USR-002 | USR-02 | §A6 | SC-USR-002 | — |
| REQ-USR-003 | USR-04 | §A6 | SC-USR-003 | — |
| REQ-USR-004 | USR-05 | §A6, §A7 + DOC-v1.0-04 | SC-USR-004, SC-USR-006, SC-USR-007 | C-USR-01 (Resolved — Deferred, 2026-07-27) |
| REQ-USR-005 | USR-07 | §A6 | SC-USR-005 | C-USR-02 (Resolved — Deferred, 2026-07-27) |

### Module ORD — DOC-v1.0-01
| REQ ID | Maps (Ref DOC) | DOC §section | Scenarios | Clarification |
|--------|----------------|--------------|-----------|---------------|
| REQ-ORD-001 | ORD-01 | §D3 + DOC-v1.0-04 | SC-ORD-001, SC-ORD-002, SC-ORD-003 | C-ORD-05 |
| REQ-ORD-002 | ORD-02 | §D3 | SC-ORD-001, SC-ORD-002, SC-ORD-007 | C-ORD-01 (Resolved, 2026-07-27) |
| REQ-ORD-003 | ORD-04 | §D3 | SC-ORD-004 | — |
| REQ-ORD-004 | ORD-06, US-D04 | §D3, §D1b | SC-ORD-005 | C-ORD-03 (Resolved, 2026-07-27) |
| REQ-ORD-005 | ORD-09 | §D3 | SC-ORD-006 | — |
| REQ-ORD-006 | ORD-10, BR-EDIT-01, OPR-10 | §D3, §D4, §D7 | SC-ORD-008, SC-ORD-009 | — |
| REQ-ORD-007 | LOC-03 | §D3 | SC-ORD-010 | — |
| REQ-ORD-008 | USR-EML, US-D18 | §D3, §D1b | SC-ORD-011, SC-ORD-012 | — |
| REQ-ORD-009 | BR-ORD-03 | §D4 | SC-ORD-013 | C-ORD-02 (Resolved — Deferred, 2026-07-27) |
| REQ-ORD-010 | BR-ORD-04 | §D4 | SC-ORD-014 | C-ORD-04 (Resolved, 2026-07-27) |
| REQ-ORD-011 | Quan sát thực tế app (không có ID doc gốc) | — | SC-ORD-015..026 | — |
| REQ-ORD-012 | D8.1/D8.2 (không có ID row riêng — BRD v3.2 mới) | §D8.1, §D8.2 | SC-ORD-013, SC-ORD-027, SC-ORD-028 | C-ORD-01 (Resolved đầy đủ, 2026-07-28) |
| REQ-ORD-013 | VAL-01..05 | §D8.3 | SC-ORD-029, SC-ORD-030 | — |
| REQ-ORD-014 | Quan sát thực tế app (không có ID doc gốc) | — | SC-ORD-031, SC-ORD-032 | — |
| REQ-ORD-015 | Không có ID doc gốc (bảng "Thành phần chung", không đánh số) | §2, §3.1 | SC-ORD-033 | — |

### Module ASN — DOC-v1.0-01
| REQ ID | Maps (Ref DOC) | DOC §section | Scenarios | Clarification |
|--------|----------------|--------------|-----------|---------------|
| REQ-ASN-001 | ASN-01 | §D3 | SC-ASN-001 | — |
| REQ-ASN-002 | ASN-02, BR-CON-01, BR-CON-02 | §D3, §A5 | SC-ASN-002, SC-ASN-003 | C-ASN-01 (Resolved, 2026-07-27) |
| REQ-ASN-003 | ASN-03, OPR-03 | §D3, §D7 | SC-ASN-004, SC-ASN-005 | — |
| REQ-ASN-004 | MTCH-01, BR-MTCH-01 | §D3, §D4 | SC-ASN-006, SC-ASN-007 | — |
| REQ-ASN-005 | OPR-01 | §D7 | SC-ASN-008, SC-ASN-013 | — |
| REQ-ASN-006 | OPR-02 | §D7 | SC-ASN-009 | C-NTF-02 (Partially Resolved, 2026-07-27) |
| REQ-ASN-007 | OPR-04 | §D7 | SC-ASN-010 | — |
| REQ-ASN-008 | OPR-05 | §D7 | SC-ASN-011 | C-ASN-02 (Resolved, 2026-07-27) |
| REQ-ASN-009 | OPR-08 | §D7 | SC-ASN-005, SC-ASN-012 | — |
| REQ-ASN-010 | Không có ID doc gốc (không đánh số) | §3.3 | SC-ASN-014 | — |

### Module DLV — DOC-v1.0-01
| REQ ID | Maps (Ref DOC) | DOC §section | Scenarios | Clarification |
|--------|----------------|--------------|-----------|---------------|
| REQ-DLV-001 | PUP-03, BR-CNF-01 | §D3, §D4 | SC-DLV-001, SC-DLV-002 | — |
| REQ-DLV-002 | GPS-01 | §D3 | SC-DLV-003, SC-DLV-004 | C-DLV-02 (Open — default deferred) |
| REQ-DLV-003 | DLV-03, BR-CNF-04, BR-INT-03 | §D3, §D4, §A5 + DOC-v1.0-04 | SC-DLV-005, SC-DLV-006, SC-DLV-007, SC-DLV-011, SC-DLV-012, SC-DLV-013, SC-DLV-014 | C-DLV-01 (Resolved), C-DLV-03 (Resolved 2026-07-27) |
| REQ-DLV-004 | COST-01, BR-COST-01 | §D3, §D4 | SC-DLV-008 | — |
| REQ-DLV-005 | BR-ASN-03 | §D4 | SC-DLV-009 | C-CNL-01 (Resolved — Deferred, 2026-07-27) |
| REQ-DLV-006 | US-D09 | §D1b | SC-DLV-010, SC-DLV-011 | — |

### Module GIFT — DOC-v1.0-01
| REQ ID | Maps (Ref DOC) | DOC §section | Scenarios | Clarification |
|--------|----------------|--------------|-----------|---------------|
| REQ-GIFT-001 | GIFT-01, BR-GIFT-01 | §D3, §D4 | SC-GIFT-001, SC-GIFT-002, SC-GIFT-003, SC-GIFT-005, SC-GIFT-006, SC-GIFT-007 | C-ORD-06 (Resolved — QA xác nhận empty state text đúng UI thật, 2026-07-28) |
| REQ-GIFT-002 | RAT-01/02 | §D3 + DOC-v1.0-04 | — (Deferred — BA/PO xác nhận 2026-07-27: rating 1-5 sao là phase sau, out of scope v1.0) | C-GIFT-01 (Resolved — Deferred, 2026-07-27) |
| REQ-GIFT-003 | — (Quan sát thực tế app STG, QA GiangDC2) | Quan sát thực tế app STG · 2026-07-24 | SC-GIFT-004 | — |

### Module CNL — DOC-v1.0-01
| REQ ID | Maps (Ref DOC) | DOC §section | Scenarios | Clarification |
|--------|----------------|--------------|-----------|---------------|
| REQ-CNL-001 | CNL-01, BR-CNL-01, BR-INT-05, US-D16 | §D3, §D4, §A5, §D1b | SC-CNL-001, SC-CNL-003, SC-CNL-005 | — |
| REQ-CNL-002 | OPR-09 | §D7 | SC-CNL-004 | — |
| REQ-CNL-003 | OPR-11 | §D7 | SC-CNL-002 | — |

### Module NTF — DOC-v1.0-01
| REQ ID | Maps (Ref DOC) | DOC §section | Scenarios | Clarification |
|--------|----------------|--------------|-----------|---------------|
| REQ-NTF-001 | NTF-01..09 | §D6 + DOC-v1.0-04 | SC-NTF-001, SC-NTF-002, SC-NTF-003, SC-NTF-004, SC-NTF-005, SC-NTF-007, SC-NTF-008, SC-NTF-009 | C-NTF-01 (Open — bảng unified 3 nguồn bổ sung 2026-07-27, chờ BA chọn); C-ORD-06 (Resolved — QA xác nhận empty state text đúng UI thật, mở rộng sang NTF, 2026-07-28); C-NTF-03 (Resolved — QA xác nhận cơ chế đánh dấu đã đọc + phân trang đúng UI thật, 2026-07-28) |
| REQ-NTF-002 | OPR-06, OPR-07 | §D7 | SC-NTF-006 (DEPRECATED 2026-07-29 — không có ngưỡng ngày) | C-NTF-02 (Partially Resolved, 2026-07-27) |

### Module TS — DOC-v1.0-01
| REQ ID | Maps (Ref DOC) | DOC §section | Scenarios | Clarification |
|--------|----------------|--------------|-----------|---------------|
| REQ-TS-001 | TS-01, TS-02, BR-INT-04 | §A8, §A5 | SC-TS-001, SC-TS-002 | — |
| REQ-TS-002 | TS-03 | §A8 | SC-TS-003 | C-TS-01 (Resolved — Deferred, 2026-07-27) |

## 2. Coverage Summary
- **Scenario có REQ + DOC source:** 92/92 (100%).
- **REQ có ≥1 scenario:** 45/46 (~98%) — mọi REQ core functional/business-rule đều có ≥1 scenario.
- **REQ chưa có scenario (gap có chủ đích):** `REQ-GIFT-002` (RAT-01/02) — **Deferred (Resolved 2026-07-27)**: BA/PO xác nhận rating 1-5 sao là phase sau, out of scope v1.0 — không derive scenario cho tới khi tính năng vào scope ở version sau.
- **REQ đánh dấu Deferred/Out-of-scope v1.0 (BA/PO xác nhận 2026-07-27, vẫn giữ scenario hiện có làm tham khảo, KHÔNG mở rộng TC cho phần deferred):** `REQ-USR-004` (tier/hạng), `REQ-USR-005` (cấu hình kênh liên hệ), `REQ-ORD-009` (ngưỡng giá trị hàng/BVA), `REQ-GIFT-002` (rating sao), `REQ-TS-002` (Admin Portal — chỉ test hệ quả end-user), `REQ-DLV-005` phần "Báo sự cố" (chỉ test lối thoát tồn tại, không test field chi tiết).
- **(Mốc cập nhật):** 2026-07-24 — INIT v1.0, phân tích lần đầu từ DOC-v1.0-01/02/03.
- **(Mốc cập nhật #2):** 2026-07-24 — UPDATE, bổ sung DOC-v1.0-04 (82 ảnh Figma) — resolve C-DLV-01, C-DLV-03; cập nhật C-USR-01, C-GIFT-01; +1 clarification C-ORD-05.
- **(Mốc cập nhật #3, health-check fix):** 2026-07-24 — đồng bộ lại +1 REQ (`REQ-GIFT-003`) + SC-DLV-014 vào REQ-DLV-003 — cả 2 đã có trong `MEMORY.md`/`test_scenario_map.md` từ đợt bổ sung ma trận nhãn nút (SC-DLV-012/013/014, SC-GIFT-004) nhưng chưa sync sang file này.
- **(Mốc cập nhật #4):** 2026-07-27 — UPDATE, BA/PO trả lời batch 16 clarification qua chat trực tiếp. Resolve/Deferred 13 items (gỡ BLOCKER cứng C-ORD-02); Partially Resolved C-NTF-02; còn Open thực sự: C-ORD-05, C-NTF-01 (bổ sung bảng unified), C-DLV-02 (default value). Chi tiết đầy đủ từng clarification: `MEMORY.md §6/§6.1`.
- **(Mốc cập nhật #5):** 2026-07-27 — UPDATE, rescan UI riêng màn Thông báo (`00_input/v1.0/27072026/`) — không có bằng chứng mới; +1 scenario `SC-NTF-007` (empty state), mở rộng `C-ORD-06` sang `REQ-NTF-001`.
- **(Mốc cập nhật #6):** 2026-07-27 — UPDATE, gap phát hiện khi review TC-NTF — +2 scenario `SC-NTF-008` (đánh dấu đã đọc), `SC-NTF-009` (scroll load thêm dữ liệu), +1 clarification mới `C-NTF-03` (Open, cơ chế chưa BA/Dev confirm).
- **(Mốc cập nhật #7):** 2026-07-27 — UPDATE, fix finding từ health-check — Coverage Summary 65/65 → **82/82** (SC-ORD-015..026 đã có sẵn ở bảng REQ-ORD-011 dòng trên từ trước, chỉ dòng Coverage Summary tổng hợp bị stale, không sync theo). Data-repair, không thêm scenario mới.
- **(Mốc cập nhật #8):** 2026-07-28 — UPDATE, BRD v3.2 mới (`00_input/v1.0/27072026/FoxEco BRD v3.2.md`) — chỉ thêm `§D8 Validate & Giá trị mặc định (Form Rules)` so với v3.1 (còn lại giữ nguyên). +2 REQ (`REQ-ORD-012`, `REQ-ORD-013`), +4 SC ORD (`SC-ORD-027..030`), +1 SC CNL (`SC-CNL-005`), 1 SC MODIFIED (`SC-ORD-013`, un-deferred). Resolve dứt điểm phần maxlength TBD của `C-ORD-01`. Coverage Summary 82/82 → **87/87**; REQ 41 → **43** (dòng "Tổng" ở `MEMORY.md §3` vốn đã lệch 40 vs tổng thật per-module 41 từ trước, tiện thể data-repair cùng lúc). Chi tiết đầy đủ: `MEMORY.md` header + §6.1 (C-ORD-01, C-ORD-02, C-NTF-02).
- **(Mốc cập nhật #9):** 2026-07-29 — UPDATE, QA GiangDC2 rà lại TC Đăng tin qua chat — phát hiện Block "Người gửi" (Wizard NEED) chưa test editability (Tên read-only/SĐT+Địa chỉ editable) và chưa có TC cho hành vi autocomplete địa chỉ theo text nhập (case-insensitive, quan sát trực tiếp app STG, không có trong tài liệu). +1 REQ mới (`REQ-ORD-014`), +2 SC ORD (`SC-ORD-031`, `SC-ORD-032`). Coverage Summary 87/87 → **89/89**; REQ 43 → **44**. Chi tiết đầy đủ: `MEMORY.md` header #10 + REQ-ORD-002 addendum + REQ-ORD-014.
- **(Mốc cập nhật #10):** 2026-07-29 — UPDATE, BA xác nhận rõ cơ chế trần thông báo khớp tin (OPR-01/`REQ-ASN-005`) qua QA GiangDC2 — là notification-firing cap (Carrier chỉ NHẬN tối đa 5 thông báo khớp/lượt quét), tách biệt khỏi UI cap Trang chủ (`SC-ASN-008`, US-D06) đã có sẵn. +1 SC (`SC-ASN-013`). Coverage Summary 89/89 → **90/90**.
- **(Mốc cập nhật #11):** 2026-07-29 — UPDATE, chuẩn bị merge phần "chi tiết + flow" từ 1 QC khác trong team (project riêng `02_analyze-requirements CA`, đã tự phân tích trên demo HTML) — trước khi generate-tc cho các màn còn thiếu, rà lại thấy 2 màn dùng chung (Trang chủ, Bảng tin) vốn đã có sẵn text mô tả đầy đủ trong `DOC-v1.0-02 §2`/`§3.1`/`§3.3` (đăng ký từ INIT 2026-07-24) nhưng CHƯA từng được capture thành Block Definition/scenario riêng — chỉ có scenario cho 2 block con của Trang chủ ("Đơn của tôi"/"Tin mới", SC-ORD-003/004) và vài scenario business-rule tham chiếu tên màn Bảng tin (SC-ASN-005/010/012), chưa có scenario nào verify cấu trúc khung 2 màn này. Bổ sung: +2 REQ (`REQ-ORD-015` Trang chủ, `REQ-ASN-010` Bảng tin), +2 SC (`SC-ORD-033`, `SC-ASN-014`), +2 Block Definition mới trong `test_scenario_map.md` (Header/Banner&Card/Bottom-nav dưới Screen Trang chủ; Danh sách tin đăng dưới Screen Bảng tin, module ASN). Nguồn tham khảo cấu trúc field bổ sung: TC do QC khác (`03_test-cases/TestCases-CA.xlsx` sheet Trang chủ/Bảng tin) — CHỈ dùng làm checklist field, mọi Source Quote/Location trong 2 REQ/SC mới đều trích trực tiếp từ `DOC-v1.0-02` (đã đăng ký sẵn trong project này), không trích từ TC của CA. **Chưa có cross-check ảnh Figma (DOC-v1.0-04)/app STG riêng cho field Header/Banner/Card** — theo Project_rule.md §10.1, nên vibe-test xác nhận trước khi coi Expected Result final (xem Analyst Note SC-ORD-033 trong `test_scenario_map.md`). Coverage Summary 90/90 → **92/92**; REQ 44 → **46**.
- **(Mốc cập nhật #11):** 2026-07-29 — UPDATE, BA xác nhận thêm: KHÔNG có ngưỡng thông báo theo NGÀY (OPR-06/`REQ-NTF-002`) — chỉ có trần theo TỪNG TIN (OPR-01/`REQ-ASN-005`), đăng N tin → tối đa 5×N thông báo. `SC-NTF-006` chuyển **DEPRECATED**. Viết lại 3 TC (`TC_03.1-3` trong `TC-NTF-v1.0.xlsx`, đồng bộ TC-MASTER) từ "trần/ngày mock N=3" sang đúng "trần 5/tin", gán cho `SC-ASN-013`.

## 3. Clarifications — Source Quote (ambiguous text)

> Trích nguyên văn đoạn mơ hồ per clarification (quoting-guide EC6). Tóm tắt + status: xem `MEMORY.md §6`.
> **Cập nhật 2026-07-27:** 13/16 clarification đã có câu trả lời BA/PO (batch qua chat) — xem Analyst Note đầy đủ + "Update 2026-07-27" trong `MEMORY.md §6.1`. Header dưới đây chỉ cập nhật status ngắn gọn để đồng bộ, KHÔNG lặp lại toàn bộ nội dung trả lời (tránh trùng lặp — single source of truth = MEMORY.md).

#### C-USR-01 — Demo hiển thị tier/điểm/CO2, BRD nói không có (Resolved — Deferred, 2026-07-27)
**Source Quote (ambiguous):**
> "USR-05 Hiển thị tổng số đơn đã giúp + tổng số quà ảo đã nhận (không tính điểm/CO₂)" (DOC-v1.0-01 §A6) — đối lập — "Hạng thành viên | 🔒 'Hạng Đồng hành' — cơ chế tier/gamification... 3 chỉ số | Đơn đã giúp (12) · Điểm uy tín (4.8) · Điểm ECO (540)" (DOC-v1.0-02 Table 10, §3.9) — bổ sung DOC-v1.0-04 (ảnh Figma "Cá nhân"): CÓ badge tier text "🏆 Hạng Đồng hành", KHÔNG có điểm ECO/uy tín dạng số.

**Source Location:** `DOC-v1.0-01 §A6/§A7 · DOC-v1.0-02 §1.2, §3.9 Table 10 · DOC-v1.0-04 images/570ad9d32e3dbdf44c72d6140826f0e6f9a3393e, e5764b10a94b0d51fab023c1a92b6f25732cb402`
**Analyst Note:** BRD (mới hơn) loại bỏ điểm/tier/CO2 khỏi scope v1.0; prototype tham chiếu (mà BRD tự nhận "đồng bộ với") vẫn có đầy đủ. Ảnh Figma thực tế cho kết quả trung gian: CÓ tier (text, không phải điểm số), KHÔNG có điểm ECO/CO2. Không còn BLOCKER cứng cho SC-USR-004, nhưng vẫn cần BA xác nhận cơ chế lên hạng trước khi viết boundary test.

#### C-ORD-01 — Wizard đăng tin không có validate bắt buộc (Resolved, 2026-07-27)
**Source Quote (ambiguous):**
> "⚠ Lưu ý: Không có trường nào bắt buộc (*) — có thể bấm 'Tiếp theo' mà không chọn Loại hàng/Giá trị." · "Có thể bỏ trống toàn bộ thông tin Người nhận mà vẫn qua được Bước 3 — không có validate bắt buộc trong bản demo."

**Source Location:** `DOC-v1.0-02 §3.5.1, §3.5.2`
**Analyst Note:** Hành vi quan sát trên prototype, chưa rõ là đặc tả chính thức hay gap của demo. Non-blocking — generate-tc ghi nhận cả 2 khả năng.

#### C-ORD-02 — Ngưỡng giá trị hàng chưa xác định (Resolved — Deferred, 2026-07-27 — gỡ BLOCKER)
**Source Quote (ambiguous):**
> "Câu hỏi mở cho BA — Ngưỡng giá trị hàng? Ảnh bắt buộc cho hàng > ngưỡng?"

**Source Location:** `DOC-v1.0-01 §D5 "Câu hỏi mở cho BA"`
**Analyst Note:** BRD tự liệt kê là câu hỏi mở. BLOCKER cho BVA giá trị hàng (REQ-ORD-009/SC-ORD-013).

#### C-ORD-03 — Hạn tin mặc định chưa xác định (Resolved, 2026-07-27)
**Source Quote (ambiguous):**
> "Hạn tin mặc định?" (mục Câu hỏi mở cho BA)

**Source Location:** `DOC-v1.0-01 §D5 "Câu hỏi mở cho BA"`
**Analyst Note:** Blocker cho test đúng THỜI ĐIỂM chuyển EXPIRED (cần môi trường mock thời gian), không blocker cho happy-path.

#### C-ORD-04 — Chip "Thuốc/Y tế" vẫn hợp lệ dù cấm gửi thuốc (Resolved, 2026-07-27)
**Source Quote (ambiguous):**
> "Loại hàng | Chip chọn 1: ... Thuốc/Y tế ... " (Table 6) — đối chiếu — "Cấm gửi: thuốc, vũ khí, chất nguy hiểm, hàng phi pháp." (§1.4)

**Source Location:** `DOC-v1.0-02 §3.5.1 Table 6, §1.4`
**Analyst Note:** Ranh giới "Thuốc/Y tế" hợp lệ vs "thuốc" bị cấm cần BA làm rõ.

#### C-ASN-01 — Thời điểm lộ SĐT chưa nhất quán (Resolved, 2026-07-27)
**Source Quote (ambiguous):**
> "Màn 'Đăng tin mới' cam kết SĐT chỉ lộ SAU KHI ghép, nhưng thực tế Chi tiết tin đã hiển thị sẵn SĐT + nút Gọi của Người gửi ngay từ trạng thái 'Chờ ghép'"

**Source Location:** `DOC-v1.0-02 §3.4 "Màn hình Chi tiết tin"`
**Analyst Note:** Mâu thuẫn với BR-CON-02. Test theo rule BRD (SĐT không lộ trước ghép) — bản hiện tại có thể fail khi vibe-test.

#### C-ASN-02 — Chủ tin/Người nhận có thể tự "nhận mang giúp" (Resolved, 2026-07-27)
**Source Quote (ambiguous):**
> "Chi tiết tin cho phép chính chủ tin hoặc Người nhận của đơn tự bấm 'Tôi mang giúp được' trên tin liên quan đến mình"

**Source Location:** `DOC-v1.0-02 §7 Table 17 row 9`
**Analyst Note:** Vi phạm OPR-05. Test theo rule đúng (nút phải ẩn) — bằng chứng thực tế cho thấy bản hiện tại vi phạm.

#### C-DLV-01 — Ai được xác nhận "Đã nhận" (Resolved — Receiver-only)
**Source Quote (ambiguous):**
> "DLV-03 RECEIVER/SENDER xác nhận đã nhận" (§D3) — đối lập — "BR-INT-03 Hoàn thành cần người nhận xác nhận đã nhận hàng" (§A5) — và — "quyền hạn ĐẶC BIỆT DUY NHẤT của vai trò Người nhận" (DOC-v1.0-02 §5.2) — xác nhận bởi DOC-v1.0-04 (ảnh Figma, 7 ảnh độc lập): Receiver có nút active "Xác nhận đã nhận hàng", Sender/Carrier chỉ thấy nhãn disabled.

**Source Location:** `DOC-v1.0-01 §D3 row DLV-03, §A5 row BR-INT-03 · DOC-v1.0-02 §5.2 · DOC-v1.0-04 (xem MEMORY.md §6.1 danh sách ảnh đầy đủ)`
**Analyst Note:** 3/4 nguồn (đa số, gồm nguồn ảnh thiết kế UI thực tế có độ tin cậy cao nhất) đồng thuận Receiver-only. Resolved — dùng Receiver làm actor cho REQ-DLV-003.

#### C-DLV-02 — Chia sẻ vị trí mặc định bật/tắt (Open — default deferred to future phase)
**Source Quote (ambiguous):**
> "Chia sẻ vị trí mặc định bật/tắt?"

**Source Location:** `DOC-v1.0-01 §D5 "Câu hỏi mở cho BA"`
**Analyst Note:** Ảnh hưởng Given ban đầu SC-DLV-003, non-blocking cho happy-path chức năng.

#### C-DLV-03 — 2 phiên bản màn "Xác nhận đã nhận hàng" chưa chốt (Resolved, 2026-07-27 — modal đơn giản chính thức)
**Source Quote (ambiguous):**
> "Cần xác nhận với đội thiết kế: bản chính thức dùng form đầy đủ này (có ảnh bằng chứng) hay modal xác nhận đơn giản như ở Mục 5.2" — 82 ảnh Figma (DOC-v1.0-04) đã quét chỉ thấy bản modal đơn giản, KHÔNG thấy form đầy đủ.

**Source Location:** `DOC-v1.0-02 §5.3 · DOC-v1.0-04 (toàn bộ 82 ảnh)`
**Analyst Note:** Nghiêng mạnh về modal đơn giản là thiết kế chính thức. generate-tc ưu tiên viết theo bản này.

#### C-GIFT-01 — RAT-01/02 mâu thuẫn nguyên tắc "không đánh giá sao" (Resolved — Deferred, 2026-07-27)
**Source Quote (ambiguous):**
> "RAT-01/02 Đánh giá 2 chiều 1–5 sao + nhận xét" (§D3) — đối lập — "BR-INT-06 Không đánh giá sao..." (§A5) — "...KHÔNG có chấm sao/đánh giá..." (§A8) — nhưng — "Rating average > 4.0/5.0" (§A10 KPI) — bổ sung DOC-v1.0-04 (ảnh Figma "Thông báo"): CÓ notification "Bạn nhận được đánh giá 5 sao" kèm comment cụ thể, nhưng KHÔNG thấy màn thao tác chấm sao (chỉ thấy màn Gift dùng icon quà).

**Source Location:** `DOC-v1.0-01 §D3 row RAT-01/02, §A5 row BR-INT-06, §A8, §A10 · DOC-v1.0-04 images/db4dfb7e4f07138be5712aff5cb7dea61d983353, 1c6c57c1a6356fee121b59007f85478d244d43d2`
**Analyst Note:** Mâu thuẫn nội bộ BRD ở 4 vị trí. Ảnh Figma xác nhận rating TỒN TẠI (đối lập BR-INT-06) nhưng chưa xác định được màn thao tác — vẫn Blocked cho REQ-GIFT-002 nhưng không còn hoàn toàn mù thông tin.

#### C-ORD-05 — 2 biến thể màn "Đăng tin thành công!" (có/không "Mã tin") — NEW 2026-07-24
**Source Quote (ambiguous):**
> Biến thể A (2 ảnh): title+nội dung+2 nút, KHÔNG có "Mã tin" — khớp US-D02 ("KHÔNG hiển thị mã đơn"). Biến thể B (2 ảnh): giống hệt + thêm dòng "Mã tin: #ECO-2026-0451" — mâu thuẫn US-D02.

**Source Location:** `DOC-v1.0-04 images/1cc41f87de9f6f9aa41e31eb1e783234771fa554, b2807d958cc82bbe871a43566a8b1c54ff02c462 (A) · 53410b9a9962e145550cf91680a13bbabaf9b47c, c8a72f19d00292f5776ea53759535937bc8f9b9e (B)`
**Analyst Note:** Số ảnh ngang nhau (2 vs 2) — không đủ cơ sở chọn bản "mới hơn". Dùng biến thể A (không Mã tin) làm baseline vì khớp US-D02, note lại cho BA/design xác nhận biến thể B có phải leftover chưa gỡ hay không.

#### C-NTF-01 — Nội dung 9 thông báo demo khác BRD (Open — bảng unified 3 nguồn bổ sung 2026-07-27)
**Source Quote (ambiguous):**
> "Bạn nhận được đánh giá 5 sao | ... · Cộng đồng FoxEco vừa đạt mốc X đơn | Thông điệp 'tiết kiệm Y kg CO₂'"

**Source Location:** `DOC-v1.0-02 §3.2 Table 4`
**Analyst Note:** Test theo danh sách BRD D6 (nguồn mới hơn); củng cố thêm C-GIFT-01/C-USR-01.

#### C-NTF-02 — Nhiều tham số vận hành "Chờ BA bổ sung" (Partially Resolved, 2026-07-27)
**Source Quote (ambiguous):**
> "Chờ BA bổ sung: bán kính/định nghĩa 'cùng tuyến', độ lệch khung giờ cho phép, chu kỳ quét khớp..." (§D7) · "Chờ BA bổ sung: ngưỡng thời gian nhắc, gộp/không gộp thông báo..." (§D6)

**Source Location:** `DOC-v1.0-01 §D7, §D6`
**Analyst Note:** Doc tự đánh dấu chưa hoàn thiện. Non-blocking cho happy-path.

#### C-TS-01 — Admin Web Portal chưa có đặc tả UI (Resolved — Deferred, 2026-07-27)
**Source Quote (ambiguous):**
> "Nền tảng: Mobile App (iOS/Android) + Admin Web Portal." (không có mô tả màn hình/field nào khác)

**Source Location:** `DOC-v1.0-01 §A3`
**Analyst Note:** Non-blocking cho v1.0 (test scope giới hạn hệ quả quan sát từ end-user).

#### C-CNL-01 — Màn "Báo sự cố" chưa có đặc tả field (Resolved — Deferred, 2026-07-27)
**Source Quote (ambiguous):**
> "Báo sự cố | Cả 3 vai trò | —" (chỉ liệt kê tên màn, không có field cụ thể)

**Source Location:** `DOC-v1.0-02 §8 Table 18`
**Analyst Note:** Đủ để test "đường huỷ thường bị khoá + có lối thoát thay thế", cần bổ sung khi có thiết kế chi tiết.
