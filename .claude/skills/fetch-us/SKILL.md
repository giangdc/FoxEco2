---
name: fetch-us
description: Kéo User Story từ Jira về `00_input/<version>/<KEY>/` (per-US folder, Markdown + Acceptance Criteria + attachments). Config per-project đọc từ `Project_rule.md` block `## Jira Integration` — KHÔNG hardcode site/project/field trong skill. Đây là skill TIỆN ÍCH ĐỘC LẬP — KHÔNG nằm trong pipeline 12 bước, KHÔNG ghi MASTER-MEMORY §8. Use when user mentions 'fetch user stories', 'kéo user story', 'lấy US từ Jira', 'import jira us', 'pull stories', 'sync stories from jira', 'tải requirement từ jira', 'kéo requirement', 'lấy yêu cầu từ jira', 'fetch us', or runs /fetch-us command.
license: Proprietary — FPT QA Toolkit v1.0 (qc-claude-v1)
compatibility: Cần Claude Code + Atlassian MCP (claude.ai Atlassian connector) đã auth + block `## Jira Integration` trong project's `Project_rule.md`. Standalone — không phụ thuộc skill nào khác.
metadata:
  toolkit: qc-claude-v1
  version: "1.0"
  released: "2026-06-05"
  category: utility
  source: jira
  output: 00_input/<version>/<KEY>/
  pipeline: standalone
  owner: QC Team
---

# Fetch User Stories (from Jira)

Kéo User Story (description + Acceptance Criteria + attachments) từ Jira → `00_input/<version>/<KEY>/` của project, giảm việc download + xếp tay.

> ⚠️ **STANDALONE — skill tiện ích**, KHÔNG nằm trong pipeline 12 bước (init→test-report).
> Không ghi `MASTER-MEMORY §8`. Không có upstream/downstream guard. Có thể bỏ qua hoàn toàn nếu user đã có docs manual.
> ⚠️ **Skill này là TEMPLATE — KHÔNG hardcode site/project/field.** Mọi thông tin Jira đọc từ `Project_rule.md`.

## Command

| Command | Mode | Mô tả |
|---|---|---|
| `/fetch-us --version v1.3.5` | FETCH | Derive JQL từ config (`fixVersion=v1.3.5`), kéo về `00_input/v1.3.5/` |
| `/fetch-us --keys PRJ-123,PRJ-124` | FETCH | Kéo issue cụ thể (chỉ định version qua `--version` hoặc đọc fixVersions của chính issue) |
| `/fetch-us --jql "project=PRJ AND ..."` | FETCH | Custom JQL toàn phần |
| `/fetch-us --sync [--version vX\|--all]` | SYNC | Re-fetch US đã có, cập nhật description/AC/attachments khi Jira đổi |
| `/fetch-us --status [--version vX]` | STATUS | Gap report: US Jira (theo JQL) vs US đã ở `00_input/v[X]/` |
| `/fetch-us … --dry-run` | (modifier) | Preview payload sẽ tạo, **không ghi file** |
| `--no-download` | (modifier) | Override tất cả link → `record` (chỉ index, ~0 token) |
| `--read-text-only` | (modifier) | Override gsheets/gdocs → `read_text` (default, token thấp ~text size) |
| `--defer-script` | (modifier) | Emit `_download.sh` (gdown) cho user chạy ngoài Claude → **zero token, binary gốc** |
| `--download-binary` | (modifier) | **Opt-in** (off by default): ép `download_binary` qua MCP — base64 ~13× file size, chỉ khi thật cần binary qua context |

## Prerequisites

| Cần có | Check |
|---|---|
| Atlassian MCP đã auth | `/mcp` → Atlassian (claude.ai Atlassian connector) |
| Block `## Jira Integration` trong `Project_rule.md` (có sub-section `userstory:`) | Tự sinh bởi `/init-project` (Q9 tên QC + Q10 link Jira). Template: `~/.claude/skills/init-project/references/jira-block-template.md` |
| (chỉ khi cần tải file binary) `~/.config/jira/.env` có `JIRA_URL/JIRA_USERNAME/JIRA_API_TOKEN` | Tạo API token: `id.atlassian.com/manage-profile/security/api-tokens` |

## Mode Routing

| Condition | → Load |
|---|---|
| `--sync` | `references/sync.md` |
| `--status` | `references/status.md` |
| Default (FETCH) | `references/fetch.md` |

## Nguyên tắc

- **Config per-project** từ `Project_rule.md` block `## Jira Integration` — KHÔNG hardcode trong skill. Thiếu block → DỪNG, gợi ý paste mẫu.
- **1 chiều Jira → md**, idempotent: dùng `last_synced` trong YAML front-matter để skip nếu Jira không mới hơn.
- **Per-US folder**: `00_input/<v>/<KEY>/{<KEY>.md, attachments/...}` — gom mọi thứ của 1 US về 1 chỗ.
- **Acceptance Criteria (option B):** KHÔNG xuất section AC riêng trong md (tránh dư với description). Skill chỉ ghi **vị trí** AC vào front-matter (`acceptance_criteria_source` + `acceptance_criteria_heading` hoặc `acceptance_criteria_field`); nội dung AC vẫn nằm verbatim trong `## Mô tả (Description)` để 1 nguồn duy nhất. Consumer (analyze-requirements) đọc front-matter biết AC ở đâu rồi tự parse.
- **Remote Links — token-aware:** kéo bằng `getJiraIssueRemoteIssueLinks`, classify theo URL pattern, xử lý theo `link_handling` config. Default trên môi trường FPT internal:
  - 🎨 **Figma** → `record` (đọc on-demand qua Figma MCP `get_metadata`/`get_design_context` khi analyze-requirements/vibe-test cần — KHÔNG cache).
  - 📊 **Google Sheets / Docs** → `read_text` (MCP `read_file_content` → text representation `.md`). **Token rẻ ~10×** so với `download_binary`, và text dùng được trực tiếp cho analyze-requirements. **Tận dụng MCP `claude.ai Google Drive` đã auth sẵn — không cần setup OAuth ngoài.**
  - 📁 **Google Drive file lạ (PDF/image/zip)** → `record` (mở browser khi cần).
  - 🔗 **Khác** → `record`.
- **`defer_to_script` (`--defer-script`)** — emit `_download.sh` dùng **gdown** (pip venv install ~1 phút) → tải binary trong shell, **zero token Claude**. Đây là path khuyến nghị khi cần xlsx/docx gốc (vd để analyze-requirements verify formula, hoặc giao file cho team khác). gdown anonymous mode tải được Sheets export endpoint mà không cần OAuth setup phức tạp.
- **⚠️ `download_binary` (MCP `download_file_content`) mặc định TẮT (opt-in `--download-binary`)**: base64 qua context tốn ~10–13× file size. gdown thay thế tốt hơn (zero token) cho mọi nhu cầu binary.
- **Attachment binary trên issue (field `attachment`)** — khác remote links — tải qua REST có token (`~/.config/jira/.env`); fail/không có token → vẫn ghi md, bỏ qua file + cảnh báo.
- **Manifest** `_userstories.md` ở cấp version để các skill khác (analyze-requirements, health-check) tham chiếu nhanh.
- **KHÔNG ghi `MASTER-MEMORY`** (đó là việc của `analyze-requirements` khi nó scan các file này).

## Examples

### Example 1: Kéo tất cả US của 1 version
**Input:** `/fetch-us --version v1.3.5`
**Behavior:** Build JQL `project=PRJ AND issuetype in (Story) AND fixVersion="1.0"` (theo `jql_template` trong config) → search → cho mỗi issue: getJiraIssue, parse AC, tải attachments, ghi `00_input/v1.3.5/<KEY>/<KEY>.md` + `attachments/*`. Cập nhật `_userstories.md`.

### Example 2: Kéo issue cụ thể
**Input:** `/fetch-us --keys PRJ-50,PRJ-51 --version v1.3.5`
**Behavior:** Bỏ qua bước search; getJiraIssue mỗi key trực tiếp; ghi vào `00_input/v1.3.5/PRJ-50/` và `PRJ-51/`.

### Example 3: Đồng bộ lại
**Input:** `/fetch-us --sync --all`
**Behavior:** Đọc mọi `00_input/*/*/<KEY>.md` có `us_key` → so sánh Jira `updated` vs `last_synced` → re-fetch các US cũ hơn.

### Example 4: Gap report
**Input:** `/fetch-us --status --version v1.3.5`
**Behavior:** Liệt kê **In sync / Stale / Missing / Orphan** giữa JQL và folder `00_input/v1.3.5/`.

### Example 5: Dry-run
**Input:** `/fetch-us --keys PRJ-50 --dry-run`
**Behavior:** In ra md content + attachment list sẽ tạo, **không ghi đĩa**.

## Common Edge Cases

| Tình huống | Xử lý |
|---|---|
| MCP Atlassian chưa auth | DỪNG, hướng dẫn `/mcp` → Atlassian |
| `Project_rule.md` thiếu block hoặc thiếu sub-section `userstory:` | DỪNG, gợi ý paste mẫu `Project_rule.jira-block.md` |
| Không có `~/.config/jira/.env` / API token | Ghi md nhưng cảnh báo: attachment không tải; md có link Jira để user mở thủ công |
| US có ảnh **inline trong description** (Jira attachment refs) | Giữ Markdown image refs nguyên bản; cũng tải file về `attachments/` nếu trong list |
| Filename trùng / ký tự đặc biệt | Slugify, giữ extension; trùng → suffix `-2`, `-3` |
| `description_format=markdown` mất bảng/nested | Cho user đổi sang `adf` trong config → skill render ADF→md nhẹ |
| Issue đổi `fixVersion` giữa các lần sync | `--sync` di chuyển folder sang `00_input/<v_new>/`, cập nhật manifest cũ + mới |
| Attachment đã bị xoá trên Jira | `--sync` xoá file local tương ứng + cập nhật front-matter |
| Rate limit Jira (429) | Throttle 200ms/req; nếu vẫn 429 → backoff exponential, báo cuối |
| Field AC không tồn tại + heading không match | `acceptance_criteria_source: none` trong front-matter; consumer biết để xử lý — KHÔNG bịa AC |
| Issue có Web Link nhưng URL pattern không match cấu hình | type `other`, record link + warning để user mở rộng `link_handling` rules |
| Google Drive download fail (permission/404/MCP error) | Giữ link URL, ghi `links[i].error`, vẫn xuất md (link-only) |
| Figma URL — chưa auth Figma MCP | Vẫn record link OK. Khi analyze-requirements/vibe-test chạy → user `/mcp` auth Figma rồi mới đọc được |
| Web Link tăng/giảm giữa các lần sync | `--sync` diff: link mới → fetch; link bị xoá → ghi `removed_at` (không tự xoá file local đã tải) |
| JQL trả về 0 issues | In thông báo + JQL đã dùng để user kiểm tra |
| US ngoài `fixVersion` chính (mixed) | Ưu tiên fixVersion đầu tiên cho path; ghi rõ trong front-matter `fix_versions: [...]` |
