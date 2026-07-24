# Vibe Test — Mode STATUS

> `/vibe-test --status`

Đọc vibe-report + TC-MASTER Excel (nguồn thật — cột AM Vibe-test tổng, AO Status, và block round nào
gần nhất có Vibe-test=Yes) → trình bày tổng quan. Version MEMORY §4 Vibe Status chỉ dùng làm fallback
nhanh nếu không mở được Excel. KHÔNG thực thi, KHÔNG sửa file.

```
📊 Vibe Test Status — v[X] — [platform]

| Status | Count | TCs |
|--------|-------|-----|
| ✅ PASS | 12 | TC_01.1, ... |
| ❌ FAIL | 1 | TC_01.5 |
| 🚫 BLOCKED | 2 | TC_01.3, TC_02.8 |
| ⏳ Pending | 5 | TC_02.9, ... |

Locators ready: 35 elements / 4 pages
Ready for /implement-automation: 12/20 TCs (60%)
```
