# Log Bug — Mode CLOSE

> `/log-bug --close BUG-001`

Check: status PHẢI = Verified trước khi close. Nếu chưa → block + suggest retest.

Khi close thành công: cập nhật `status: Closed` trong bug md + bug-index.md, đồng thời đồng bộ Bug
Data sheet — cột D (Status Jira → Done/Cancel tuỳ resolution), cột I (Resolved = ngày close), cột V
(Round closed bug = round hiện tại). Xem `references/sync-excel.md`.
