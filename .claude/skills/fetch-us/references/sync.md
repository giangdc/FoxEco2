# Fetch User Stories — Mode SYNC

> `/fetch-us --sync [--version vX | --all]` · `--keys K1,K2 --sync`
> Re-fetch các US đã có trong `00_input/`, cập nhật khi Jira mới hơn. Idempotent.

## Workflow

### Step 0 — Load config (như `fetch.md` Step 0)
- MCP auth + block `## Jira Integration` + env (cho attachment).

### Step 1 — Liệt kê US đã có
- `--all`: glob `00_input/*/*/*.md`, lọc file có YAML front-matter chứa `us_key`.
- `--version vX`: chỉ trong `00_input/vX/`.
- `--keys K1,K2`: lọc theo key.

In bảng preview (số US sẽ check + thời điểm `last_synced` cũ nhất/mới nhất).

### Step 2 — Per-US compare & refresh
Cho mỗi US:
1. Đọc front-matter để lấy `us_key`, `last_synced`, `jira_updated`, `version`, `fix_versions`, `attachments`.
2. `getJiraIssue(us_key, fields=...)` → `issue.fields.updated` (Jira).
3. **So sánh**:
   - Jira `updated` ≤ md `jira_updated` → SKIP (no change). Log "in sync".
   - Jira `updated` > md `jira_updated` → **re-fetch** (làm lại Step 3a–3g của `fetch.md`).
4. **Diff attachments**:
   - Attachment ID có trong front-matter nhưng KHÔNG còn trên Jira → **xoá file local** + cập nhật front-matter (bỏ entry).
   - Attachment ID mới trên Jira (chưa có local) → tải mới.
   - Attachment ID + jira_id giống mà filename đổi → đổi tên file local.
5. **Diff fix_versions**:
   - Nếu `issue.fixVersions[0].name` đổi → US đã chuyển version. Hành xử:
     a. Tạo folder mới `00_input/<v_new>/<KEY>/` với nội dung mới (move file).
     b. Cập nhật manifest cũ (`00_input/<v_old>/_userstories.md`): đánh dấu **"moved → <v_new>"** + giữ dòng để traceability.
     c. Cập nhật manifest mới: thêm dòng.
     d. Xoá folder cũ `00_input/<v_old>/<KEY>/`? → MẶC ĐỊNH **giữ + đánh dấu moved**. Cờ `--prune-moved` để thực xoá.
6. Cập nhật front-matter `last_synced` + `jira_updated`.

### Step 3 — Manifest cập nhật
- Mỗi version folder bị ảnh hưởng → re-render dòng tương ứng.
- Sort + dedupe.

### Step 4 — Báo cáo

```
🔁 Synced: <n>   ⏭ In sync: <n>   📦 Moved (version change): <n>   ❌ Failed: <n>

Updated US (Jira mới hơn):
  - PRJ-50  (updated 2026-05-29 vs synced 2026-05-25; +1 attachment, +2 line AC)
  - PRJ-53  (status: To Do → In Progress)

Moved version (giữ folder cũ kèm marker):
  - PRJ-60  v1.3.5 → v1.4.0   (xoá folder cũ bằng --prune-moved nếu muốn)

Attachment changes:
  + 3 new files (PRJ-50, PRJ-55)
  - 1 deleted (PRJ-53/attachments/old-mockup.png — không còn trên Jira)
```

## Edge cases

| Tình huống | Xử lý |
|---|---|
| Md thiếu `jira_updated` (file cũ trước khi skill thêm field) | Fallback so sánh `last_synced` < Jira `updated` |
| Md có `us_key` không match key thật (filename rename) | Tin `us_key` trong front-matter (canonical); báo warning nếu lệch tên file |
| Issue không còn (xoá/move project) | Đánh dấu folder `_deleted/` trong cùng version + log; KHÔNG xoá file (user quyết) |
| Conflict: user sửa tay md sau khi push | Phát hiện qua mismatch description vs Jira; **ưu tiên Jira**, lưu bản local cũ thành `<KEY>.local.md.bak` trước khi ghi đè |
| Nhiều fixVersions thay đổi thứ tự | Path lấy theo `[0]`; nếu thứ tự đổi nhưng `[0]` không đổi → chỉ update `fix_versions` field, không move folder |
| Rate limit | Throttle, retry với jitter |
