# Template block `## Jira Integration` (per-workspace)

> Block này do **`/init-project` tự sinh** vào `02_analyze-requirements/Project_rule.md` của workspace
> mỗi người, dựa trên 2 câu hỏi lúc init: **Tên QC phụ trách (Q9)** + **Link Jira dự án (Q10)**.
> Skill `log-bug` (push/pull) và `fetch-us` đọc config từ block này — KHÔNG hardcode trong skill.

## Cách map từ câu trả lời init

| Câu hỏi init | Điền vào field |
|---|---|
| Q9 — Tên QC phụ trách | `qc_name` (+ ghi vào CLAUDE.md mục Project info) |
| Q10 — Link Jira dự án, vd `https://<site>.atlassian.net/browse/PRJ-123` hoặc `.../projects/PRJ` | `site` = phần `https://<site>.atlassian.net` · `project_key` = mã trước dấu gạch (vd `PRJ`) |

Các field còn lại để mặc định/TBD — skill `log-bug` sẽ tự khám phá khi chạy lần đầu
(`getVisibleJiraProjects` → `getJiraProjectIssueTypesMetadata` → `getJiraIssueTypeMetaWithFields`)
rồi GHI ngược vào block.

## Template (copy nguyên khối vào Project_rule.md, thay giá trị `<...>`)

```
## Jira Integration
qc_name:         <Tên QC phụ trách workspace — từ Q9>
site:            https://<your>.atlassian.net
cloud_id:        <uuid | để trống → dùng hostname, fail thì getAccessibleAtlassianResources>
project_key:     <KEY — từ Q10>
issue_type:      Bug
reporter:        <accountId | để trống = tài khoản auth>
parent_epic:     <KEY-n | để trống nếu screen không bắt parent>
fix_version:     <id ưu tiên, hoặc name | để trống>
priority_map:    P1=Highest, P2=High, P3=Medium, P4=Low
required_fields:                 # field BẮT BUỘC khi create — log-bug tự khám phá rồi điền
  - <fieldKey>: <value>
recommended_fields:
  - <fieldKey>: <value>
status_map:      New=To Do, InProgress=In Progress, Fixed=<TBD>, Verified=<TBD>, Closed=<TBD>
description_extra: [Environment, Version, Module, Traceability]
match_jql:       project = {project_key} AND summary ~ "{bug_id}"
userstory:                       # sub-section riêng cho fetch-us
  issue_types:   [Story]
  jql_template:  project = {project_key} AND issuetype in ({issue_types}) AND fixVersion = "{version}" ORDER BY key ASC
  link_handling:                 # token-aware (xem fetch-us/SKILL.md)
    figma:   record
    gsheets: read_text
    gdocs:   read_text
    gdrive:
      enabled: true
    other:   record
  attachment_download:
    env_file: ~/.config/jira/.env   # chỉ cần khi tải binary attachment
```

## Ghi chú
- Mỗi member init workspace riêng → block riêng → **skill tự map theo workspace từng người**, không ai đụng config của ai.
- Schema chi tiết field & quy trình khám phá: `~/.claude/skills/log-bug/references/push-jira.md` (mục "Schema block").
- Workspace không dùng Jira (Q10 = "Không dùng") → KHÔNG sinh block; `fetch-us`/`log-bug --push-jira` sẽ dừng và chỉ dẫn bổ sung sau.
