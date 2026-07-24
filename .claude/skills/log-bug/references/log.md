# Log Bug — Mode LOG

> `/log-bug`

## Workflow

### Step 1: Đọc Source MEMORY §16 → filter ASSERTION_FAIL + Status = Open + Bug ID = —
### Step 2: Tạo bug report cho mỗi unlogged ASSERTION_FAIL

Dùng `05_bug-reports/template-bug-report.md` làm chuẩn. Mỗi bug PHẢI mở đầu bằng khối
YAML front-matter (máy đọc — cho `--push-jira`/`--pull-jira`) khớp với bảng người-đọc:

```markdown
---
bug_id: BUG-[NNN]
jira_project:              # = project_key từ Project_rule.md (## Jira Integration) — KHÔNG hardcode
jira_issue_type: Bug       # default; override từ Project_rule.md nếu project dùng issue-type khác
jira_key:                  # tự điền sau push
jira_url:                  # tự điền sau push
priority: P[1-3]
severity: [Critical|Major|Medium|Low]     # đổi nhãn "High"→"Major" (2026-07-21) khớp đúng dropdown
                                            # Bug Data!Y cột Severity của template ISC — xem bảng mã bên dưới
platform: [Web|Mobile]                     # mới — khớp Bug Data cột "Platform"
defect: [Logic|Interface|Server|Data|Other]           # mới — khớp Bug Data cột "Defect"
effect: [Functionality|Usability|Performance|Security|Serviceability]  # mới — khớp Bug Data cột "Effect"
round_found: [1-5]                         # mới — round test phát hiện bug (khớp block Round trong TC-MASTER)
round_closed:                              # mới — điền round khi bug Done, để trống nếu chưa đóng
rework_number: 1                           # mới — số lần sửa lại tính đến hiện tại
wont_fix_reason:                           # mới — CHỈ điền khi resolution = "Won't fix"; mã lấy từ
                                            # Bug Data sheet cột Y (danh mục lookup) — đọc trực tiếp
                                            # từ workbook lúc sync, KHÔNG hardcode/đoán mã trong skill
components: []
affects_versions: [v[X]]
labels: [tc-[xxx], req-[xxx], fail-[xxx], run-[xxx]]
environment: "[URL/emulator/build]"
status: Open
attachments: []
last_synced:
---

# BUG-[NNN] — [Short title tiếng Việt]

| Field | Value |
|-------|-------|
| Bug ID | BUG-[NNN] |
| Version | v[X] |
| Severity / Priority | [Severity] / [P1-P3] |
| Module | [name] |
| Platform | [Web/Mobile] |
| Status | Open |
| Round found | R[1-5] |
| Traceability | FAIL-xxx → RUN-xxx → TC-xxx → REQ-xxx |
| Environment | [URL] |
| Jira Key | — (điền sau khi push) |

## Steps to Reproduce
(copy từ TC steps — cột H "Test Steps" trong TC-MASTER, template ISC không còn cột Test Data riêng nên giá trị đã nằm sẵn trong text)

## Expected vs Actual
- Expected: [từ TC expected — cột I]
- Actual: [từ error message trong §16]

## Evidence
[screenshot nếu có]
```

> Front-matter `labels` mang chuỗi traceability để truy ngược 2 chiều với Jira. **Đã bỏ `sc-[xxx]` khỏi labels** — template ISC không còn Scenario ID column trong TC-MASTER, traceability qua TC ID + Req ID.
> Severity code (mapping cố định, không hỏi user): `Critical=20 · Major=10 · Medium=5 · Low=2` — dùng khi ghi cột Severity của Bug Data sheet (xem Step 3b).
> Đẩy bug lên Jira: `/log-bug --push-jira BUG-[NNN]` (xem `references/push-jira.md`).

### Step 3: Cập nhật bug-index.md + Source MEMORY §16 (Bug ID column)

### Step 3b: Đồng bộ vào Bug Data sheet (TC-MASTER Excel) — mới, xem `references/sync-excel.md`

Sau khi tạo bug md, mirror ngay 1 row vào sheet `Bug Data` của TC-MASTER (khối QC PHÂN TÍCH, cột L-U — khối Jira A-K chỉ điền đầy đủ sau khi `--push-jira` có `jira_key`). Chi tiết cột + rule đầy đủ ở `references/sync-excel.md` — dùng chung cho log/update/close/push-jira.

### Step 4: Ghi §8 = COMPLETED
