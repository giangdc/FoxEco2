---
bug_id: BUG-001
jira_project: FE
jira_issue_type: Bug
jira_key:
jira_url:
priority: P2
severity: Major
platform: Mobile
defect: Logic
effect: Functionality
round_found: 1
round_closed:
rework_number: 1
wont_fix_reason:
components: [Đăng tin, Form OFFER]
affects_versions: [v1.0]
labels: [tc-04.94, tc-04.95, req-ord-001, req-ord-002, run-vr-001]
environment: "FoxPro STG — package com.hrisproject.stag, device ZPB66PZLPRBMEAZT (Android, Appium MCP)"
status: Open
attachments: [TC_04.94_final.png, TC_04.95_final.png]
last_synced:
---

# BUG-001 — Form OFFER không auto-fill "Điểm xuất phát" + default "Thời gian di chuyển" sai

| Field | Value |
|-------|-------|
| Bug ID | BUG-001 |
| Version | v1.0 |
| Severity / Priority | Major / P2 |
| Module | Đăng tin — Form OFFER (Tôi nhận giao hàng) |
| Platform | Mobile |
| Status | Open |
| Round found | R1 |
| Traceability | VR-001 (vibe-test) → TC_04.94, TC_04.95 → REQ-ORD-001, REQ-ORD-002 |
| Environment | FoxPro STG, package `com.hrisproject.stag` |
| Jira Key | — (chưa push, project chưa cấu hình Jira Integration) |

## Steps to Reproduce
1. Đăng nhập app FoxPro STG, đang ở Trang chủ.
2. Bấm nút [+] "Đăng tin" ở bottom nav → màn "Đăng tin mới".
3. Bấm card "Tôi nhận giao hàng" → chuyển sang Form đăng ký tuyến (OFFER), form MỚI/SẠCH.
4. Quan sát field "Điểm xuất phát (A)" và field "Thời gian di chuyển".

## Expected vs Actual
- **Điểm xuất phát:**
  - Expected: auto-fill sẵn giá trị (địa điểm mặc định của người dùng), sửa được.
  - Actual: field trống, chỉ hiển thị placeholder "Bạn đang ở đâu / xuất phát từ đâu" — không có giá trị auto-fill nào.
- **Thời gian di chuyển:**
  - Expected: mặc định 17:30–18:30 (theo BRD v3.2 §D8.2).
  - Actual: mặc định = giờ hiện tại lúc mở form + 30 phút (lúc test: 09:55–10:25) — không phải giá trị cố định 17:30–18:30.
- Hệ quả liên đới: TC_04.95 (đăng ký tuyến với dữ liệu hợp lệ) vẫn submit thành công về mặt chức năng, nhưng không thể "giữ mặc định" như bước TC mô tả vì không có default đúng — phải nhập thủ công để bù trừ.

## Evidence
- `08_test-runs/vibe/VR-001-2026-08-03/screenshots/TC_04.94_final.png` — form mới/sạch, Điểm xuất phát trống, giờ di chuyển 09:55–10:25.
- `08_test-runs/vibe/VR-001-2026-08-03/screenshots/TC_04.95_final.png` — màn "Đã ghi nhận tuyến đường!" sau khi nhập thủ công.
- Chi tiết đầy đủ: `08_test-runs/vibe/VR-001-2026-08-03/vibe-log.md` (mục TC_04.94, TC_04.95).
- MCP audit trail: `08_test-runs/vibe/VR-001-2026-08-03/mcp-session-log.md` (call #10-24).

## Notes
- 2 field lỗi cùng xuất hiện trên cùng 1 form, khả năng cùng 1 root cause (module tính default value
  chưa chạy/chưa map đúng dữ liệu nguồn) — đề xuất dev kiểm tra chung 1 lần.
- KHÔNG chặn chức năng chính (đăng ký tuyến vẫn hoạt động đúng nếu user tự nhập tay) — vì vậy xếp
  Major thay vì Critical.
