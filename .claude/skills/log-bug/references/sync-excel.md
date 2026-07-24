# Log Bug — Đồng bộ Bug Data sheet (TC-MASTER Excel)

> Dùng chung cho `log.md` Step 3b, `update.md`, `close.md`, `push-jira.md` Step 7 — bất kỳ khi nào
> bug md thay đổi, mirror lại đúng 1 row tương ứng trong sheet `Bug Data` của TC-MASTER
> (`03_test-cases/v[X]/TC-MASTER-v[X].xlsx`, alias của file ISC chính thức — xem
> `generate-tc/references/consolidate.md`).

## Nguyên tắc

- **Bug md + bug-index.md vẫn là source-of-truth cho lifecycle.** Bug Data sheet là bản mirror phục
  vụ Report Test/Dashboard tính KPI (%Bug Fixed, Critical+Major, %Bug do AI phát hiện...) — KHÔNG
  bao giờ sửa Bug Data sheet rồi đọc ngược lại vào bug md.
- **KHÔNG hardcode danh mục Won't Fix Reason trong skill.** Đọc trực tiếp cột Y của sheet `Bug Data`
  tại thời điểm sync (danh mục có thể khác nhau giữa các bản copy template) — nếu `wont_fix_reason`
  trong bug md không khớp mã nào trong cột Y, cảnh báo user thay vì tự bịa mã.
- **Cột O "Bug Status" là FORMULA tự tính từ cột D (Status Jira) — KHÔNG BAO GIỜ ghi tay.** Per
  Guideline sheet: "CÔNG THỨC tự tính từ D (To Do/In Progress/In Review→Open; Pending/Cancel/Done
  giữ nguyên)".

## Column mapping (Bug Data sheet, header row 1, data từ row 2)

**Khối A — Jira export (cột A-K, chỉ điền đầy đủ SAU khi có `jira_key` từ `--push-jira`):**

| Cột | Field | Nguồn trong bug md |
|---|---|---|
| A | Key | `jira_key` front-matter |
| B | Type | `jira_issue_type` front-matter |
| C | Summary | H1 title (bỏ prefix `BUG-NNN:`) |
| D | Status (Jira) | Jira status hiện tại (đọc qua `--pull-jira`, hoặc suy từ `status` front-matter qua `config.status_map` ngược) |
| E | Priority (Jira) | `priority` front-matter map qua `config.priority_map` (giống logic push-jira.md) |
| F | Assignee | Jira assignee (nếu track) |
| G | Reporter | Jira reporter / mặc định user hiện tại |
| H | Created | Ngày tạo bug md |
| I | Resolved | Ngày status chuyển `Done`/`Fixed` (để trống nếu chưa) |
| J | Fix Version | `affects_versions` front-matter |
| K | Sprint | Round hiện tại dạng `R[N]` — LẤY TỪ `round_found` front-matter (vd `round_found: 2` → `R2`), KHÔNG phải tên sprint tự do |

**Khối B — QC phân tích (cột L-U, log-bug tự điền từ bug md, không phụ thuộc Jira):**

| Cột | Field | Nguồn trong bug md |
|---|---|---|
| L | Severity | Map `severity` front-matter → số: `Critical=20 · Major=10 · Medium=5 · Low=2` |
| M | Function | Module/tên chức năng (khớp `C3` sheet TC tương ứng) |
| N | Platform | `platform` front-matter (`Web`/`Mobile`) |
| O | Bug Status | **FORMULA — KHÔNG ghi.** Tự tính từ cột D. |
| P | Resolution | Suy từ `status`: `Fixed` (nếu status=Fixed/Verified/Closed do dev sửa) / `Won't fix` / để trống nếu đang mở |
| Q | Won't Fix Reason | Chỉ điền khi cột P = `Won't fix` — lấy `wont_fix_reason` front-matter, PHẢI khớp 1 mã trong cột Y hiện có của sheet (đọc trước khi ghi — xem Nguyên tắc) |
| R | Defect | `defect` front-matter |
| S | Effect | `effect` front-matter |
| T | Rework number | `rework_number` front-matter |
| U | Round | `round_found` front-matter (số nguyên 1-5, KHÔNG phải chuỗi `R2`) |
| V | Round closed bug | `round_closed` front-matter (để trống nếu bug chưa Done) |

## Workflow

```
1. Đọc bug md front-matter đầy đủ (bug_id, jira_key nếu có, severity, platform, defect, effect,
   round_found, round_closed, rework_number, wont_fix_reason, status, priority, affects_versions).
2. Mở TC-MASTER (nếu chưa có sheet Bug Data — nghĩa là TC-MASTER build từ template cũ hoặc thiếu
   sheet, DỪNG + báo user re-run /generate-tc --consolidate từ template gốc).
3. Tìm row có cột A (Key) = jira_key (nếu đã push) HOẶC row đã gắn trước đó bằng bug_id ở comment/
   cell note nội bộ (nếu chưa push, dùng bug_id làm khoá tạm — khi push xong, update lại cột A).
   - Chưa tồn tại row → append row mới cuối bảng dữ liệu hiện có.
   - Đã tồn tại → update tại chỗ (không tạo row trùng).
4. Ghi cột L-V (khối QC) luôn luôn. Ghi cột A-K (khối Jira) CHỈ khi đã có jira_key — nếu chưa push,
   để trống khối A, sync lại đầy đủ sau khi push-jira chạy xong.
5. KHÔNG ghi cột O (Bug Status — formula) và cột 25 (Y, danh mục lookup — đây là dữ liệu tĩnh của
   template, không phải cột ghi theo bug).
6. Lưu file — dùng cùng cơ chế alias TC-MASTER-v[X].xlsx / TC-MASTER-LATEST.xlsx như generate-tc.
```

## Bước bổ sung — cập nhật cột "ID Bugs" ở sheet Test Cases (KHÁC sheet Bug Data)

> Đây là cột "ID Bugs" trong block round (N-AL) của sheet `Test Cases`/`Test Case N` — nơi vibe-test/
> execute-maintain ghi `BUG-[NNN]` tạm thời ngay khi TC fail (xem `vibe-test/references/execute.md`
> Step 7a). log-bug là nơi DUY NHẤT có `jira_key`, nên log-bug chịu trách nhiệm thay `BUG-[NNN]` bằng
> `jira_key` thật sau khi push thành công — KHÔNG skill nào khác được sửa cột này.

```
1. Parse bug md front-matter `labels` → lấy giá trị `tc-[xxx]` (Testcase ID gắn với bug này).
2. Tìm đúng sheet + row có cột A (đã resolve) = TC ID đó.
3. Quét 5 block round (N-AL) của row đó, tìm cell "ID Bugs" đang chứa đúng `bug_id` (dạng `BUG-NNN`)
   — có thể xuất hiện ở nhiều round nếu TC fail lặp lại nhiều lần với cùng bug.
4. Thay giá trị cell đó bằng `jira_key` (giữ nguyên, không xoá) — CHỈ làm bước này sau khi
   `--push-jira` thành công (có jira_key thật); trước đó cell vẫn giữ `BUG-NNN`.
5. Không tìm thấy TC ID nào khớp (label thiếu/sai, hoặc TC đã bị xoá khỏi sheet) → log warning, KHÔNG
   chặn phần còn lại của push-jira (Bug Data sheet vẫn sync bình thường).
```

## Khi nào chạy bước này

| Trigger | Hành động |
|---|---|
| `log.md` Step 3b (bug mới tạo) | Append row mới trong Bug Data, khối Jira để trống (chưa có jira_key) |
| `push-jira.md` PUSH Step 7 (vừa có jira_key) | Update khối A đầy đủ cho row Bug Data đã append trước đó **+ chạy "Bước bổ sung" thay `BUG-NNN`→`jira_key` ở cột ID Bugs sheet Test Cases** |
| `push-jira.md` PULL Step 3 (status Jira đổi) | Update cột D + O tự tính theo, cập nhật I (Resolved) nếu chuyển Done |
| `update.md` (status/severity/... đổi tay) | Update lại toàn bộ row Bug Data (cả 2 khối nếu có đủ dữ liệu) |
| `close.md` (bug đóng) | Update cột D→Done tương ứng, I (Resolved), V (Round closed bug) = round hiện tại |

## Edge cases

| Tình huống | Xử lý |
|---|---|
| TC-MASTER chưa có sheet `Bug Data` (file cũ/thiếu sheet) | DỪNG bước sync, KHÔNG chặn log bug md (md vẫn là nguồn chính) — báo warning, suggest `/generate-tc --consolidate` |
| `wont_fix_reason` không khớp mã nào trong cột Y hiện có | Cảnh báo + để trống cột Q, KHÔNG tự bịa/chọn mã gần đúng |
| `round_found` trống (bug log trước khi có round context, vd từ execute-maintain cũ chưa round-aware) | Để trống cột K/U, ghi Remark nội bộ "round chưa xác định — cần bổ sung tay" |
| Nhiều bug cùng `jira_key` (trùng do lỗi) | Block, báo conflict — không ghi đè ngẫu nhiên |
| Excel đang mở (write permission denied) | Suggest user đóng Excel, retry |
