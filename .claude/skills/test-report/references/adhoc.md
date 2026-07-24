# Test Report — Mode ADHOC

> `/test-report --adhoc` | `/test-report --adhoc --version v2.0`

## Khi nào dùng
Stakeholder hỏi "test đến đâu rồi?" — cần snapshot nhanh, không cần formal report.

## Workflow

### Step 1: Đọc sources nhanh
MASTER-MEMORY §8 (pipeline status), Version MEMORY §3-§4, latest §15 run, bug-index — cộng `Dashboard`/`Report Test` sheet trong TC-MASTER nếu file mở nhanh được (ưu tiên số liệu pre-computed, xem `release.md` §Sources); nếu Excel không mở kịp (ADHOC ưu tiên tốc độ) → fallback bug-index.md/MEMORY như cũ, ghi rõ trong output là "chưa đối chiếu Excel".

### Step 2: Present inline (không tạo file)

```
📊 Test Status Snapshot — v[X] — [date]

Pipeline: [N]/13 skills completed
Scenarios: [N] total | NEW: [n] | MODIFIED: [n] | CARRIED: [n]
TCs: [N] total (Dashboard) | Generated: [n] | Vibe-tested: [n] (cột Vibe-test tổng=Yes) | Automated: [n] (cột Automated=Yes)

Latest run: RUN-[NNN] ([date])
  Pass: [N] ([%]) | Fail: [N] | Blocked: [N]

Bugs: [N] open (Priority P1: [n], P2: [n] — theo Jira Priority; Critical: [n], Major: [n] theo Severity)

Quality Gates:
  ✅ G1: TC Review 82/100
  ❌ G2: P1 Pass 90% (target 100%)
  ⚠️ G3: Overall 87% (target 90%)
  ❌ G4: 1 P1 bug open
  ...

Overall: NOT READY for release
```

KHÔNG tạo file — chỉ inline. Nếu user muốn file → suggest `/test-report --release`.
