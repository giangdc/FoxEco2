# Bug Index — FoxEco

> Nguồn chính cho lifecycle bug. Bug Data sheet (TC-MASTER Excel) là bản mirror — xem
> `references/sync-excel.md` trong skill log-bug. Cập nhật status ở đây trước, KHÔNG bao giờ ngược lại.

| Bug ID | Title | Severity | Priority | Status | Module | TC IDs | Round Found | Version | Created | Jira Key |
|--------|-------|----------|----------|--------|--------|--------|--------------|---------|---------|----------|
| BUG-001 | Form OFFER không auto-fill "Điểm xuất phát" + default "Thời gian di chuyển" sai | Major | P2 | Open | Đăng tin — Form OFFER | TC_04.94, TC_04.95 | R1 | v1.0 | 2026-08-03 | — |
| BUG-002 | Thiếu message lỗi khi validate Điểm đến/Điểm xuất phát | Medium | P3 | Open | Đăng tin — Form OFFER | TC_04.99, TC_04.100 | R1 | v1.0 | 2026-08-03 | — |
| BUG-003 | Header màn Cá nhân thiếu MNV (mã nhân viên) + badge tier "🏆 Hạng Đồng hành" | Medium | P3 | Open | Cá nhân | TC_02.1, TC_02.2, TC_02.3 | R1 | v1.0 | 2026-08-04 | [FE-148](https://foxproject.atlassian.net/browse/FE-148) |

## By Version

### v1.0
- BUG-001 (Open) — Major
- BUG-002 (Open) — Medium
- BUG-003 (Open) — Medium

## Summary
- Total: 3 (0 Closed, 3 Open)
- By Severity: Major=1, Medium=2
- By Priority: P2=1, P3=2

> **2026-08-04:** BUG-004 (thiếu badge tier "Hạng Đồng hành") đã gộp vào BUG-003 theo yêu cầu user — cùng 1 màn hình, cùng 1 lần phát hiện vibe-test VR-004. Xem "Notes" trong `BUG-003-*.md` về việc verify đủ cả 2 phần trước khi đóng bug.
