# Fetch User Stories — Mode FETCH (default)

> `/fetch-us --version <vX>` · `/fetch-us --keys <KEY1>,<KEY2>` · `/fetch-us --jql "<jql>"`
> Kéo User Story Jira về `00_input/<v>/<KEY>/{<KEY>.md, attachments/}`.

## Step 0 — Load Jira config (BẮT BUỘC trước mọi thao tác)

1. Tìm `Project_rule.md` của project (thường `02_analyze-requirements/Project_rule.md`, hoặc project root).
2. Đọc block `## Jira Integration` (chung với log-bug) + sub-section `userstory:` (riêng cho skill này).
3. Nếu **thiếu block hoặc sub-section** → **DỪNG**. Hướng dẫn user: chạy lại `/init-project` (Q9 tên QC + Q10 link Jira → block tự sinh theo workspace), hoặc paste template:
   `~/.claude/skills/init-project/references/jira-block-template.md` (đã có cả phần `userstory:` + `userstory.link_handling`).
4. Nếu MCP Atlassian chưa auth → hướng dẫn `/mcp` → "claude.ai Atlassian".
5. Đọc env file (nếu khai báo `attachment_download.env_file`) → kiểm `JIRA_URL/JIRA_USERNAME/JIRA_API_TOKEN`. Thiếu → cảnh báo (skill vẫn chạy, bỏ qua tải binary attachment).
6. Nếu config có `link_handling.gdrive.enabled: true` → kiểm Google Drive MCP có tool `mcp__claude_ai_Google_Drive__download_file_content` (đã auth sẵn trong Claude). Thiếu → fallback "link only" cho Google Docs/Sheets.

## Step 1 — Build JQL

Ưu tiên theo args:
1. `--keys K1,K2` → KHÔNG cần search, gọi `getJiraIssue` trực tiếp cho từng key.
2. `--jql "<raw>"` → dùng nguyên văn.
3. `--version vX` → render `jql_template` với `{project_key}`, `{issue_types}` (join `,`), `{version}` (tên thật trên Jira).

In JQL ra để user xác nhận trước khi search (trừ khi `--yes`).

## Step 2 — Search (skip nếu `--keys`)

```
mcp__claude_ai_Atlassian__searchJiraIssuesUsingJql(
  cloudId, jql,
  fields = ["summary","status","priority","issuetype","fixVersions","updated"],
  maxResults = 50, nextPageToken
)
```
Throttle 200ms/req, follow pagination.

## Step 3 — Per-issue processing

### 3a. Get full issue
```
mcp__claude_ai_Atlassian__getJiraIssue(
  cloudId, issueIdOrKey,
  fields = <config.userstory.fields>,
  responseContentFormat = <config.userstory.description_format | "markdown">
)
```

### 3a'. Get remote links (Web Links đính trên issue)
```
mcp__claude_ai_Atlassian__getJiraIssueRemoteIssueLinks(cloudId, issueIdOrKey)
```
Trả về list, mỗi item có `object.url`, `object.title`, `object.icon`, `relationship` (thường "Web Link").
**Đây là cơ chế chính để US gắn link tài liệu/Figma — KHÔNG nên nhét URL vào description.**

### 3b. Xác định version path
- `--version` user truyền → ưu tiên.
- Else `fixVersions[0].name` của issue (slugify: vd "1.0" → `v1.0`). Rỗng → `unversioned`.
- Path target: `00_input/<v>/<KEY>/`.

### 3b'. Classify remote links + dispatch theo `config.userstory.link_handling`

⚠️ **Token-aware:** binary qua MCP `download_file_content` về Claude là **base64 ~1.33× file size + đi qua context 2 lần** → tốn token ~10× file size. Cho mục đích `analyze-requirements` (đọc nội dung), **`read_text` rẻ hơn ~10×** và đầu ra dùng được ngay. Mặc định luôn ưu tiên hành động nhẹ nhất khả thi.

| URL pattern | type | Action default | Lý do |
|---|---|---|---|
| `figma.com/(file\|design\|proto)/...` | `figma` | **`record`** | Figma file thay đổi liên tục — đọc on-demand qua **Figma MCP** (`mcp__claude_ai_Figma__get_metadata` + `get_design_context`). Cache vô nghĩa. |
| `docs.google.com/spreadsheets/d/<ID>/...` | `gsheets` | **`read_text`** | Text representation đủ cho analyze-requirements; token thấp; dùng MCP `claude.ai Google Drive` đã auth (KHÔNG cần OAuth ngoài). |
| `docs.google.com/document/d/<ID>/...` | `gdocs` | **`read_text`** | Như trên. |
| `drive.google.com/file/d/<ID>/...` | `gdrive` | `record` | File lạ (PDF/image/zip…) — user opt-in download khi cần |
| `(?:miro\|lucid\|adobe\.com/xd)...` | `design-other` | `record` | Đọc qua MCP riêng nếu có |
| khác | `other` | `record` | URL không classify được |

> ⚠️ **`defer_to_script` cho Google Drive đã bỏ khỏi default** trên FPT internal (OAuth corporate boundary phức tạp; cá nhân không có quyền cấp qua gcloud ADC). Giữ option cho **Jira binary attachment** (curl + API token, đơn giản) hoặc CI runner riêng có ADC sẵn.

### 3 actions (chung cho mọi type, override trong config)

| Action | Tool / cơ chế | Token cost | Output |
|---|---|---|---|
| **`record`** | Không gọi gì — chỉ ghi URL + metadata Jira | **~0** | Front-matter `links[i]` |
| **`read_text`** | `mcp__claude_ai_Google_Drive__read_file_content(fileId)` → trả text representation | **Thấp** (= text size · ~1 token/4 chars) | `attachments/<KEY>-<slug>.md` |
| **`defer_to_script`** | Emit `_download.sh` (gdown) cho user chạy NGOÀI Claude | **~0** | Script + placeholder note trong md + file binary sau khi user chạy script |

> ⚠️ `download_binary` qua MCP mặc định TẮT (opt-in `--download-binary`) — base64 ~13× file size là anti-pattern khi gdown thay thế zero-token.

### Workflow theo action

**`record`:**
- Chỉ ghi front-matter `links[i] = {type, url, name}`. Bỏ qua mọi MCP call.

**`read_text` (default cho gsheets/gdocs):**
1. Trích `file_id` từ URL (regex `/d/([A-Za-z0-9_-]+)`).
2. `mcp__claude_ai_Google_Drive__get_file_metadata(file_id)` → name + mimeType + modifiedTime + size.
3. Check `size > max_inline_kb` → fallback `defer_to_script`.
4. `mcp__claude_ai_Google_Drive__read_file_content(file_id)` → text.
5. Ghi `attachments/<KEY>-<slug>.md` với front-matter nhỏ (source URL + fetched_at), body = text.
6. Front-matter `links[i].local: attachments/<KEY>-<slug>.md` + `extracted_via: read_text`.

**`defer_to_script` (zero-token cho binary gốc — khuyến nghị khi cần xlsx/docx/pdf):**
- KHÔNG gọi MCP download.
- Sinh/append vào `00_input/<v>/_download.sh` 1 block per file, dùng `gdown`:
  ```bash
  download_gdrive sheets "<FILE_ID>" xlsx \
    "$ROOT/<KEY>/attachments/<KEY>-<slug>.xlsx" \
    "<KEY> — <name>"
  ```
- Helper `download_gdrive` (template cố định trong script header) hỗ trợ 3 kind: `sheets` (export xlsx), `docs` (export docx), `file` (Drive uc?id=).
- Front-matter ghi `extracted_via: pending-script` + `script: _download.sh`.
- Cuối báo cáo: nhắc user chạy `bash 00_input/<v>/_download.sh`.
- Setup gdown 1 lần (do PEP 668, dùng venv):
  ```bash
  python3 -m venv ~/.venvs/gdown
  ~/.venvs/gdown/bin/pip install gdown
  ln -sf ~/.venvs/gdown/bin/gdown /opt/homebrew/bin/gdown
  ```
- gdown 6.0+ syntax: `gdown -O <out> <URL>` (KHÔNG còn cờ `--fuzzy`).
- Anonymous mode đủ cho Sheets/Docs share-link "Anyone with the link" (verified trên FPT workspace). File restrict tuyệt đối → cần cookies hoặc OAuth ngoài (out of scope skill này).

**Fail handling** (mọi action MCP): 403/404/timeout → fallback **xuống 1 cấp** (`read_text` → `record`; `download_binary` chỉ khi `--download-binary`); ghi `links[i].error` + warning cuối.

### CLI flags ghi đè (per-run, không cần sửa config)
- `--read-text-only` → ép mọi link về `read_text` (nếu có thể) / `record` (nếu không).
- `--download-binary` → ép `download_binary` (chấp nhận token cao).
- `--no-download` → ép `record` (nhanh nhất, chỉ index).
- `--defer-script` → ép `defer_to_script`.

### 3c. Ghi nhận Acceptance Criteria (KHÔNG xuất section riêng — option B)

Skill **KHÔNG** sinh section `## Acceptance Criteria` riêng trong md (tránh dư với description). Thay vào đó:
- Ưu tiên: nếu `config.userstory.acceptance_criteria_field` có giá trị → đọc field; ghi trực tiếp giá trị vào front-matter `acceptance_criteria_value` (nếu user muốn lấy độc lập khỏi description).
- Else: tìm trong description heading khớp `acceptance_criteria_heading` (case-insensitive) → KHÔNG copy nội dung; chỉ ghi nhận **vị trí** vào front-matter (`acceptance_criteria_source: description-heading` + `acceptance_criteria_heading: "<heading thật>"`).
- Else: ghi `acceptance_criteria_source: none`.

Consumer (`analyze-requirements`) đọc front-matter để biết AC nằm ở đâu rồi tự parse description.

### 3d. Idempotency check
- Folder đã có + `last_synced` ≥ `jira_updated` → SKIP (in "unchanged"). Trừ khi `--sync`.

### 3e. Tải attachments (file binary đính trực tiếp trên issue qua field `attachment`)
Khác với remote links (3a'+3b'). Field `attachment` chứa file user upload trực tiếp. Tải qua REST có auth:
```bash
curl -sS -u "$JIRA_USERNAME:$JIRA_API_TOKEN" -H "Accept: application/json" \
  -L -o "00_input/<v>/<KEY>/attachments/<safe_filename>" "<content URL>"
```
Slugify filename, suffix `-2`, `-3` khi trùng. Thiếu env / fail → cảnh báo, vẫn xuất md.

### 3f. Sinh `<KEY>.md`

```markdown
---
us_key: <KEY>
jira_url: <site>/browse/<KEY>
version: <v>
doc_id:                              # để trống — analyze-requirements gán
issue_type: <Story|...>
status: <name>
priority: <name>
assignee: <displayName|—>
reporter: <displayName>
fix_versions: ["<name1>", ...]
sprint: <name|—>
epic: <parent key|—>
labels: [...]
acceptance_criteria_source: customfield_<id> | description-heading | none
acceptance_criteria_heading: "<heading thật khi source=description-heading>"
acceptance_criteria_value: |          # chỉ điền khi source=customfield_<id>
  <raw value của AC field>
links:                                # remote links (Web Link) — KHÔNG nằm trong description
  - type: figma | gsheets | gdocs | gdrive | other
    url: <full URL>
    name: <title từ Jira link object>
    read_via: figma-mcp               # với figma; analyze-requirements/vibe-test dùng tool này
    file_id: <Drive id>               # với gsheets/gdocs/gdrive
    local: attachments/<file>.xlsx    # đường dẫn local nếu đã download
    downloaded_via: google-drive-mcp  # ghi rõ cơ chế đã dùng
    error: "<lý do>"                  # nếu download fail
attachments:                          # file binary đính trực tiếp trên Jira (field attachment[])
  - file: attachments/<safe_filename>
    jira_id: <id>
    mime: <mimeType>
    size: <bytes>
last_synced: <ISO date>
jira_updated: <issue.fields.updated>
---

# <KEY> — <Summary>

## Mô tả (Description)
<description verbatim — markdown render từ Jira. Bao gồm heading AC nếu user viết AC vào description.>

## Tài liệu liên quan
<với mỗi remote link trong `links:`, in 1 dòng:>
- 🎨 **Figma**: [<name>](<url>) — đọc nội dung khi cần qua Figma MCP (`get_metadata` + `get_design_context`), KHÔNG cache file.
- 📊 **Google Sheets**: [<name>](<url>) → đã tải về `attachments/<file>.xlsx` (Drive MCP).
- 📄 **Google Docs**: [<name>](<url>) → đã tải về `attachments/<file>.docx`.
- 🔗 **Other**: [<name>](<url>)

## Đính kèm (file binary trên Jira)
<với mime image/* → embed: ![<filename>](attachments/<safe>)>
<khác → link: - [<filename>](attachments/<safe>) (<mime>, <size> bytes)>
<nếu rỗng → "*(Không có file binary đính trực tiếp trên Jira issue.)*">

## Liên kết Jira
- Issue: <jira_url>
- Parent Epic: <site>/browse/<epic> (<epic summary>)
```

> **Nguyên tắc option B:** mọi thông tin AC vẫn nằm trong `## Mô tả (Description)` (verbatim). Front-matter chỉ
> ghi nhận **vị trí + nguồn** AC, KHÔNG nhân bản nội dung. Tránh ra-of-sync khi description đổi.

### 3g. Cập nhật manifest
File `00_input/<v>/_userstories.md`:
- Header + table.
- Cột: US Key · Summary · Status · Priority · Fix versions · Links (số figma/gsheets/...) · Path · last_synced.

## Step 4 — Báo cáo cuối

```
✅ Fetched: <n>   ⏭ Skipped (unchanged): <n>   🔁 Updated: <n>   ❌ Failed: <n>

Remote links classified:
  - figma:    <n> (recorded, read on-demand via Figma MCP)
  - gsheets:  <n> downloaded · <n> link-only (Drive MCP fail/no permission)
  - gdocs:    <n> downloaded · <n> link-only
  - other:    <n>

Attachments (binary): <n> downloaded · <n> fail (token thiếu)

Path: 00_input/<v>/
  ├─ PRJ-XX/  (links: 2 · attachments: 0 · AC: description-heading "Acceptance Criteria")
  └─ _userstories.md
```

## Edge cases bổ sung
| Tình huống | Xử lý |
|---|---|
| Issue có Web Link nhưng URL pattern không match → `other` | Vẫn record + warning "consider mapping pattern" |
| Google Drive file đã bị restrict / 404 | `download_file_content` lỗi → giữ link, ghi `links[i].error` |
| Drive MCP chưa auth (nếu sau này tách) | Fallback REST export endpoint nếu file public; else link-only |
| User vừa thêm Web Link mới sau lần fetch trước | `--sync` so sánh: link mới → fetch; link mất → đánh dấu `removed_at` trong front-matter |
| Issue đổi version | Move folder + cập nhật manifest cũ + mới |
| Filename trùng / ký tự đặc biệt | Slugify ASCII-safe; trùng → suffix `-2`, `-3`; tên gốc giữ trong `links[i].name` |
| Description rỗng + AC = `customfield` | Vẫn xuất md với section Mô tả "(rỗng)"; AC value lấy từ field theo front-matter |
| Description rỗng + AC = `description-heading` | `acceptance_criteria_source: none` + warning |
| Rate limit | Throttle 200ms; backoff exponential khi 429 |
