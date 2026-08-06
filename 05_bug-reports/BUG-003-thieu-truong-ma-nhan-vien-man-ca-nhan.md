---
bug_id: BUG-003
jira_project: FE
jira_issue_type: Bug
jira_key: FE-148
jira_url: https://foxproject.atlassian.net/browse/FE-148
priority: P3
severity: Medium
platform: Mobile
defect: Interface
effect: Usability
round_found: 1
round_closed:
rework_number: 1
wont_fix_reason:
components: [Cá nhân]
affects_versions: [v1.0]
labels: [tc-02.1, tc-02.2, tc-02.3, req-usr-002, req-usr-003, req-usr-004, run-vr-004]
environment: "FoxPro STG — package com.hrisproject.stag, emulator-5554 (Pixel, Android, Appium MCP)"
status: Open
attachments: [R1_TC_02.1-05_10_canhan_home.png, R2_TC_02.1-06_10_canhan_home.png]
last_synced: 2026-08-04
---

# BUG-003 — Header màn Cá nhân thiếu MNV (mã nhân viên) + badge tier "🏆 Hạng Đồng hành"

| Field | Value |
|-------|-------|
| Bug ID | BUG-003 |
| Version | v1.0 |
| Severity / Priority | Medium / P3 |
| Module | Cá nhân |
| Platform | Mobile |
| Status | Open |
| Round found | R1 |
| Traceability | VR-004 (vibe-test) → TC_02.1, TC_02.2, TC_02.3 → REQ-USR-002, REQ-USR-003, REQ-USR-004 |
| Environment | FoxPro STG, package `com.hrisproject.stag` |
| Jira Key | [FE-148](https://foxproject.atlassian.net/browse/FE-148) |

> **Cập nhật 2026-08-04:** gộp từ 2 bug riêng (`BUG-003` gốc + `BUG-004`, đã xoá) theo yêu cầu user — cùng 1 màn hình, cùng 1 lần phát hiện. Xem mục "Notes" bên dưới về khác biệt severity/root-cause giữa 2 phần.

## Steps to Reproduce
1. Đăng nhập app FoxPro STG (đã thử với 2 account: stag_TaiPM@fpt.com và stag_giangdc2@fpt.com).
2. Tab "Chức năng" → tile "FoxEco" → vào SDK FoxEco.
3. Bấm tab "Cá nhân" ở bottom nav.
4. Quan sát toàn bộ header cam đầu màn (dòng phòng ban ngay dưới tên user, và khu vực badge).

## Expected vs Actual

**Phần 1 — MNV (mã nhân viên):**
- Expected (theo `TC_02.2`/`TC_02.3`): dòng phòng ban hiển thị đúng định dạng `"Phòng [ban] · MNV: [mã NV]"` — ví dụ `"Phòng Kỹ thuật · MNV: FTEL2291"`.
- Actual: chỉ hiển thị tên phòng ban, KHÔNG có phần `"· MNV: ..."` nào. Xác nhận trên cả 2 tài khoản test:
  - stag_TaiPM@fpt.com → `"Phòng Phát triển Phần mềm số 8"`
  - stag_giangdc2@fpt.com → `"Ban Giám đốc"`

**Phần 2 — badge tier "Hạng Đồng hành":**
- Expected (theo `TC_02.3`, header đủ 6 phần tử): có badge tier dạng text tĩnh `"🏆 Hạng Đồng hành"` — theo `C-USR-01` (Resolved): v1.0 chưa có LOGIC tính hạng, nhưng badge NÊN hiển thị dạng display-only tĩnh (không kèm cơ chế tính toán).
- Actual: KHÔNG có badge nào trên header, ở cả 2 tài khoản test.

## Evidence
- `08_test-runs/vibe/Profile_VR-007-2026-08-05/screenshots/R1_TC_02.1-05_10_canhan_home.png` (tài khoản stag_TaiPM@fpt.com)
- `08_test-runs/vibe/Profile_VR-007-2026-08-05/screenshots/R2_TC_02.1-06_10_canhan_home.png` (tài khoản stag_giangdc2@fpt.com)
- MCP page-source dump xác nhận không có text nào chứa "MNV" hoặc "Hạng Đồng hành" trên màn — `08_test-runs/vibe/Profile_VR-007-2026-08-05/mcp-session-log.md` (section "ROUND 1 + ROUND 2", call #11, #25).
- Chi tiết đầy đủ: `08_test-runs/vibe/Profile_VR-007-2026-08-05/vibe-log.md` (section "ROUND 1 + ROUND 2", mục TC_02.1, TC_02.2, TC_02.3). ⚠ 2026-08-05: folder gốc `VR-004-2026-08-04` đã được merge vào `Profile_VR-007-2026-08-05` và xoá theo yêu cầu user — bug này vẫn Open/tái xác nhận qua Round 3.

## Notes
- **Đã push Jira 2026-08-04 → `FE-148`.** Ảnh đính kèm lúc push KHÔNG tự upload được qua MCP (không có tool upload attachment) — **user đã tự đính tay 1 ảnh trực tiếp trên Jira UI ngay sau đó (14:45)**. Cùng lúc đã setup `~/.config/jira/.env` (JIRA_URL/JIRA_USERNAME/JIRA_API_TOKEN, quyền 600) cho REST fallback — verify token OK (`GET /rest/api/3/myself` → 200) — các lần push bug sau log-bug có thể tự upload attachment qua REST, không cần user đính tay nữa.
- Ban đầu vibe-test log 2 bug riêng vì khác severity (MNV=Medium, badge=Low) và nhiều khả năng khác root cause (MNV = data/SSO chưa map, badge = UI element chưa build — nên có thể được fix ở 2 thời điểm khác nhau bởi 2 phần code khác nhau). **User xác nhận muốn gộp làm 1 (2026-08-04)** vì cùng 1 màn hình, cùng 1 lần phát hiện.
- **Khi retest/verify, cần check ĐỦ CẢ 2 phần** (MNV + badge tier) trước khi chuyển bug sang Verified/Closed — nếu dev chỉ fix 1 trong 2 phần, giữ bug ở trạng thái mở (không đóng non nửa vời), ghi rõ trong comment Jira phần nào đã fix/chưa.
- Chưa rõ root cause chi tiết của từng phần: MNV thiếu do SSO không trả field, hay app nhận field nhưng chưa build UI hiển thị; badge tier là UI element hoàn toàn mới. Cần dev kiểm tra riêng từng phần dù chung 1 ticket.
- Ban đầu vibe-test nghi ngờ thêm 3 field khác cũng thiếu (SĐT, khu vực, kênh liên hệ) — user xác nhận trực tiếp qua chat (2026-08-04) đây KHÔNG phải gap thật (Expected Result gốc trích BRD text lỗi thời), đã sửa lại `TC_02.1`/`TC_02.2` để chỉ còn đúng gap MNV này. Xem `C-USR-04` (clarification, Open) trong `02_analyze-requirements/v1.0/MEMORY.md` §6.
- Không chặn chức năng chính (xem/điều hướng vẫn hoạt động) — xếp Medium/P3 (lấy mức cao hơn giữa 2 phần gộp).
