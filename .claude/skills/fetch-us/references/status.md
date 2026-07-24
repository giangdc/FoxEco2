# Fetch User Stories — Mode STATUS

> `/fetch-us --status [--version vX | --all]`
> Gap report so sánh JQL Jira vs `00_input/<v>/`. Read-only, không ghi gì.

## Workflow

### Step 0 — Load config
Như `fetch.md` Step 0 (chỉ cần MCP auth + block Jira Integration; KHÔNG cần env attachment).

### Step 1 — Thu thập 2 nguồn

**Local:** đọc tất cả `00_input/<v>/*/<KEY>.md` có front-matter `us_key`. Build set `local[v] = { key → {summary, status, last_synced, jira_updated} }`.

**Jira:** với mỗi version `v` (hoặc tất cả từ config), search bằng `jql_template`. Build set `jira[v] = { key → {summary, status, updated, fixVersions} }`.

### Step 2 — Phân loại

Cho mỗi key, đối chiếu 4 nhóm:

| Nhóm | Định nghĩa |
|---|---|
| ✅ **In sync** | local có + jira có + `local.jira_updated ≥ jira.updated` |
| 🟡 **Stale** | local có + jira có + `jira.updated > local.jira_updated` (Jira mới hơn) |
| 🔵 **Missing** | jira có + local KHÔNG có (chưa fetch lần nào) |
| 🟠 **Orphan** | local có + jira KHÔNG trả về (US đã xoá / đổi version / sửa JQL) |

### Step 3 — Báo cáo

```
📋 Status — version v1.3.5   (JQL: project=PRJ AND issuetype in (Story) AND fixVersion="1.0")

✅ In sync (5)
  PRJ-50  Đăng nhập SSO         (To Do)
  PRJ-51  ...

🟡 Stale — Jira mới hơn (2)
  PRJ-53  Dashboard widget       (jira_updated 2026-05-29 vs local 2026-05-25)
       → fix: /fetch-us --sync --keys PRJ-53
  PRJ-54  ...

🔵 Missing — chưa fetch (3)
  PRJ-60  Notification setting   (Story, Medium, fixVersion 1.0)
  PRJ-61  ...
       → fix: /fetch-us --keys PRJ-60,PRJ-61

🟠 Orphan — local có, JQL không trả về (1)
  PRJ-45  (file 00_input/v1.3.5/PRJ-45/) — kiểm tra: issue có thể đã chuyển version hoặc bị xoá
       → fix: /fetch-us --sync --keys PRJ-45  (sẽ move folder nếu đổi version)

──────
Tổng: 5 ok / 2 stale / 3 missing / 1 orphan = 11 US in scope
```

### Step 4 — Suggestions
In một block "Đề xuất hành động" gom lệnh sync/fetch theo nhóm để user copy-paste:

```
# Cập nhật tất cả Stale + Orphan:
/fetch-us --sync --keys PRJ-53,PRJ-54,PRJ-45

# Kéo các Missing:
/fetch-us --keys PRJ-60,PRJ-61,PRJ-62 --version v1.3.5
```

## Edge cases

| Tình huống | Xử lý |
|---|---|
| Không có US local | In "0 US local" + chạy tiếp Jira để liệt kê Missing |
| JQL trả 0 | In "0 từ Jira" + mọi local đều Orphan |
| Issue có nhiều fixVersions | Map vào version đầu tiên (path); báo nếu local nằm ở version khác |
| `--all` (tất cả version) | Lặp version trong `00_input/` + version từ JQL chung; in tách block per-version |
| Local md hỏng front-matter | Bỏ qua + warning |
| MCP rate limit | Throttle search; gộp `--all` chạy tuần tự per-version |
