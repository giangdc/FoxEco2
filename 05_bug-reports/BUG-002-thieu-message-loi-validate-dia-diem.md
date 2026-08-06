---
bug_id: BUG-002
jira_project: FE
jira_issue_type: Bug
jira_key:
jira_url:
priority: P3
severity: Medium
platform: Mobile
defect: Interface
effect: Usability
round_found: 1
round_closed:
rework_number: 1
wont_fix_reason:
components: [Đăng tin, Form OFFER]
affects_versions: [v1.0]
labels: [tc-04.99, tc-04.100, req-ord-012, run-vr-001]
environment: "FoxPro STG — package com.hrisproject.stag, device ZPB66PZLPRBMEAZT (Android, Appium MCP)"
status: Open
attachments: [TC_04.99_final.png, TC_04.100_final.png]
last_synced:
---

# BUG-002 — Thiếu message lỗi khi validate Điểm đến/Điểm xuất phát trên Form OFFER

| Field | Value |
|-------|-------|
| Bug ID | BUG-002 |
| Version | v1.0 |
| Severity / Priority | Medium / P3 |
| Module | Đăng tin — Form OFFER (Tôi nhận giao hàng) |
| Platform | Mobile |
| Status | Open |
| Round found | R1 |
| Traceability | VR-001 (vibe-test) → TC_04.99, TC_04.100 → REQ-ORD-012 |
| Environment | FoxPro STG, package `com.hrisproject.stag` |
| Jira Key | — (chưa push, project chưa cấu hình Jira Integration) |

## Steps to Reproduce

**Case A (TC_04.99 — Điểm đến trùng Điểm xuất phát):**
1. Ở Form OFFER, nhập Điểm xuất phát = Điểm đến = cùng 1 giá trị (vd "Tòa nhà Lô B3, KCX Tân Thuận, Q.7").
2. Tick checkbox điều khoản.
3. Quan sát nút "Đăng tin ngay" và toàn bộ màn hình.

**Case B (TC_04.100 — Điểm xuất phát để trống):**
1. Ở Form OFFER, xoá trống field Điểm xuất phát, các field khác hợp lệ, checkbox đã tick.
2. Quan sát nút "Đăng tin ngay" và toàn bộ màn hình.

## Expected vs Actual
- Expected (Case A): Bị chặn/báo lỗi "Điểm đến phải khác điểm xuất phát".
- Expected (Case B): Bị chặn/báo lỗi (không cho submit).
- Actual (cả 2 case): Nút "Đăng tin ngay" bị disable đúng (chặn submit chính xác), NHƯNG không có
  bất kỳ message lỗi nào hiển thị trên màn hình — quét toàn bộ text qua `appium_get_page_source`
  không tìm thấy dòng lỗi nào. User chỉ thấy nút mờ đi, không biết lý do.
- Đối chiếu: TC_04.101 (Thời gian di chuyển cách nhau <30 phút) — cùng loại validate chặn submit —
  LẠI CÓ hiển thị message rõ ràng ("Giờ đến phải lớn hơn 17:30"). Cho thấy xử lý lỗi không đồng nhất
  giữa nhóm field địa điểm và nhóm field thời gian.

## Evidence
- `08_test-runs/vibe/VR-001-2026-08-03/screenshots/TC_04.99_final.png`
- `08_test-runs/vibe/VR-001-2026-08-03/screenshots/TC_04.100_final.png`
- Chi tiết đầy đủ: `08_test-runs/vibe/VR-001-2026-08-03/vibe-log.md` (mục TC_04.99, TC_04.100).
- MCP audit trail: `08_test-runs/vibe/VR-001-2026-08-03/mcp-session-log.md` (call #36-43).

## Notes
- Không chặn được submit sai (chức năng chặn vẫn đúng) nên xếp Medium/Usability thay vì Major —
  đây là gap về trải nghiệm/thông báo, không phải lỗi logic nghiệp vụ.
- Đề xuất fix: thêm inline error text tương tự pattern đã có ở field Thời gian di chuyển, áp dụng
  cho 2 case Điểm đến/Điểm xuất phát này.
