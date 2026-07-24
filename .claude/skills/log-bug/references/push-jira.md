# Log Bug — PUSH-JIRA / PULL-JIRA (đồng bộ 2 chiều · config per-project)

> `/log-bug --push-jira [BUG-NNN|--all]`  → md → Jira (tạo/cập nhật issue + attach + ghi key về)
> `/log-bug --pull-jira [BUG-NNN|--all]`  → Jira → md (kéo status về md + bug-index)

⚠️ **Skill này là TEMPLATE — KHÔNG hardcode site/project/field.** Mọi thông tin Jira đọc từ
**`Project_rule.md`** của dự án hiện tại (tạm thời; có thể đổi nguồn sau).

## Step 0 — Load Jira config (BẮT BUỘC trước mọi thao tác)
1. Tìm `Project_rule.md` của dự án (thường `02_analyze-requirements/Project_rule.md`, hoặc project root).
2. Đọc block `## Jira Integration` trong đó.
3. Nếu **không có block** → DỪNG, yêu cầu user thêm theo schema dưới (có mẫu đã điền để tham khảo).
4. Nếu MCP Atlassian chưa auth → hướng dẫn `/mcp` → Atlassian.

### Schema block `## Jira Integration` (đặt trong Project_rule.md)
```
## Jira Integration
site:            https://<your>.atlassian.net
cloud_id:        <uuid | để trống → dùng hostname, fail thì getAccessibleAtlassianResources>
project_key:     <KEY>
issue_type:      Bug
reporter:        <accountId | để trống = tài khoản auth>
parent_epic:     <KEY-n | để trống nếu screen không bắt parent>   # nếu workflow ép: phải đang In Progress/QA Accept
fix_version:     <id ưu tiên, hoặc name | để trống>
priority_map:    P1=Highest, P2=High, P3=Medium, P4=Low
required_fields:                 # field BẮT BUỘC khi create (tùy field-config từng dự án)
  - <fieldKey>: <value>          # vd customfield_10678: "5"   (cascade → {"value": ...})
recommended_fields:              # nên set nếu có
  - <fieldKey>: <value>
status_map:      New=To Do, InProgress=In Progress, Fixed=<...>, Verified=<...>, Closed=<...>
description_extra: [Environment, Version, Module, Traceability]   # field Jira screen KHÔNG có → nhét vào Description
match_jql:       project = {project_key} AND summary ~ "{bug_id}"
```
> Nếu là dự án Jira **mới/chưa biết schema** → tự khám phá rồi GHI vào block trên:
> `getVisibleJiraProjects` → `getJiraProjectIssueTypesMetadata` → `getJiraIssueTypeMetaWithFields`
> (lấy required + custom field ids + version) → `getTransitionsForJiraIssue` (status/transition ids).
> Lưu ý: create-meta có thể báo `required:false` nhưng create THẬT vẫn enforce → cứ thử tạo để lộ field bắt buộc.

## Field mapping (md → Jira, theo config)
| md (front-matter / nội dung) | Jira | Lấy từ |
|---|---|---|
| H1 title (bỏ `BUG-NNN:`) | Summary = `[BUG-NNN] <title>` | (prefix để pull match) |
| Summary+Steps+Expected+Actual+Impact + `description_extra` | Description (markdown) | body md |
| issue_type | issuetype | config |
| project_key | project | config |
| priority | Priority | config.priority_map[priority] |
| parent_epic | parent `{key}` | config (nếu có) |
| fix_version | fixVersions `[{id}]` (ưu tiên id) | config |
| required_fields / recommended_fields | additional_fields | config (cascade → `{"value":...}`) |
| reporter | reporter | config | default auth |
| status | workflow status (transition) | config.status_map |
| attachments[] | Attachments | xem PUSH bước 5 |

## PUSH workflow (`--push-jira`)
1. Đọc bug md + front-matter; load config (Step 0).
2. **Idempotent:** `jira_key` đã có → `editJiraIssue` đồng bộ field + transition theo status; KHÔNG tạo mới.
3. Build `additional_fields` từ config (priority, parent, fixVersions, required/recommended fields).
4. `createJiraIssue` (cloudId, projectKey, issueTypeName, summary, description markdown, additional_fields) → key.
5. Attachments: nếu MCP có tool upload → dùng; nếu không → REST fallback (API token trong `~/.config/jira/.env`):
   ```bash
   curl -s -u "$JIRA_USERNAME:$JIRA_API_TOKEN" -X POST -H "X-Atlassian-Token: no-check" \
     -F "file=@<path>" "$JIRA_URL/rest/api/3/issue/<KEY>/attachments"
   ```
6. Transition issue về status khớp `status` md (`getTransitionsForJiraIssue` → `transitionJiraIssue`).
7. Ghi `jira_key`/`jira_url`/`last_synced` vào front-matter bug md + cột Jira Key trong `bug-index.md`.
   ⚠️ Nếu bug nguồn nằm trong dự án LIVE → ghi vào **bản copy ở sandbox**, KHÔNG sửa file dự án live.
7b. **Đồng bộ Bug Data sheet** (TC-MASTER Excel) — xem `references/sync-excel.md`. Giờ đã có
   `jira_key`, update đầy đủ khối A (cột A-K) cho row đã append lúc `log.md` Step 3b.
7c. **Ghi ngược `jira_key` vào cột "ID Bugs" của sheet Test Cases** (khác Bug Data — xem
   `references/sync-excel.md` §"Bước bổ sung"). TC row liên quan xác định qua label `tc-[xxx]` trong
   front-matter. Đây là bước BẮT BUỘC, không phải optional — vibe-test/execute-maintain chỉ ghi tạm
   `BUG-NNN` lúc TC fail vì chưa có jira_key, log-bug là nơi duy nhất hoàn tất liên kết này.
8. Báo cáo: key + url + field đã set + attachment.

`--all`: lặp các `BUG-*.md` chưa có `jira_key`; in dry-run trước khi tạo hàng loạt.

## PULL workflow (`--pull-jira`)
1. Lấy issue theo `jira_key`, hoặc `searchJiraIssuesUsingJql` dùng `config.match_jql`.
2. Đọc status Jira → map ngược qua `config.status_map`.
3. Khác `status` hiện tại → cập nhật `status` + Status History trong md + `bug-index.md`, set `last_synced`.
3b. Đồng bộ lại Bug Data sheet (cột D Status + cột O tự tính theo formula + cột I Resolved nếu chuyển
   Done) — xem `references/sync-excel.md`.
4. `--all`: đồng bộ mọi bug có `jira_key`.

## Workflow gating (nếu dự án bật)
- Nếu Bug screen ép **parent** + workflow yêu cầu **parent Epic đang active** (vd In Progress/QA Accept):
  parent Epic thường phải tạo/đưa-active **thủ công trên UI** (Epic hay có nhiều field bắt buộc + Attachment).
  Tạo 1 Epic parent dùng chung, ghi `parent_epic` vào config, tái dùng cho mọi bug.

## Edge cases
| Tình huống | Xử lý |
|---|---|
| Thiếu block `## Jira Integration` | Dừng, yêu cầu user thêm (theo schema) |
| Chưa auth MCP | Dừng, `/mcp` → Atlassian |
| `jira_key` đã có | Update (idempotent), không tạo trùng |
| Required field thiếu khi create | Đọc lỗi → bổ sung từ config; KHÔNG đoán bừa giá trị nghiệp vụ |
| Priority/field không map | Fallback + cảnh báo |
| Attachment lỗi/không hỗ trợ | Tạo issue trước, attach sau (REST) hoặc báo file fail |
| Reporter accountId sai | Bỏ → default theo token |
| Bug nguồn ở dự án live | Ghi-ngược vào sandbox copy, không đụng file live |

> 📎 Block `## Jira Integration` được `/init-project` **tự sinh theo workspace mỗi người** (Q9 tên QC + Q10 link Jira).
> Template chuẩn: `~/.claude/skills/init-project/references/jira-block-template.md` — các field TBD do skill này tự khám phá (quy trình ở trên) rồi ghi ngược vào block.
