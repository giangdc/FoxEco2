# Generate TC — Mode REVIEW

> `/generate-tc --review` | `/generate-tc --review --version v2.0`

## Workflow

1. Đọc MEMORY §9 (TC Gen Log) + MASTER-MEMORY §6 (TC Files Registry)
2. Nếu TC-MASTER (file ISC — xem `consolidate.md`) tồn tại → parse sheet **Dashboard** (không còn
   sheet `Overview` trong template mới; Dashboard đã có sẵn breakdown Tổng TC/Pass/Fail/Priority/Group
   per sheet-module qua formula) + sheet **RTM** (coverage gap theo Req ID)
3. NEW/CARRIED/MODIFIED không còn trong Excel (template không có cột lifecycle) — lấy từ Version
   MEMORY §4 Scenario Index, không parse từ file Excel.
4. Trình bày:

```
📊 TC Status — v2.0

TC-MASTER: ISC_[Project]_v2.0_TC_v1_R1.xlsx (consolidated, alias TC-MASTER-v2.0.xlsx)
Total TCs: 45 (nguồn: Dashboard!F4:F33 tổng)

| Module (Dashboard) | NEW¹ | CARRIED¹ | MODIFIED¹ | Total | High | Medium | Low | Pass % |
|--------|-----|---------|----------|-------|----|----|-----|-----|
| Login | 0 | 8 | 0 | 8 | 3 | 3 | 2 | 100% |
| Dashboard | 12 | 3 | 2 | 17 | 8 | 6 | 3 | 82% |
| Profile | 5 | 4 | 1 | 10 | 3 | 4 | 3 | 90% |
| Payment | 10 | 0 | 0 | 10 | 5 | 3 | 2 | 100% |

¹ NEW/CARRIED/MODIFIED lấy từ Version MEMORY §4, không có trong Excel.

RTM gap (Req ID chưa có TC): 2 (xem sheet RTM — trạng thái "Chưa có TC (gap)")
Fragments chưa sync: 0
Scenarios chưa có TC: 2 (SC-DASH-018, SC-DASH-019 — Blocked)

Next: /review-tc → /vibe-test → /implement-automation
```

KHÔNG sửa file.
