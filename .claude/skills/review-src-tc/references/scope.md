# Review SRC-TC — Mode SCOPE

> `/review-src-tc --module Login` | `/review-src-tc --member member_A`

Giống FULL nhưng filter:
- `--module Login` → chỉ TCs + code thuộc module Login (match theo `C3` Tên chức năng của sheet, hoặc tên tab)
- `--member member_A` → **(thay đổi so với schema cũ)** Template ISC KHÔNG còn cột "Assigned To" — mỗi TC không có assignee riêng trong Excel nữa. Filter theo member dùng 1 trong 2 nguồn thay thế, ưu tiên theo thứ tự:
  1. `git log --format='%an' -1 -- [test file]` — tác giả commit gần nhất của file test → match theo tên/username.
  2. Source MEMORY §13 Implementation Log nếu project tự thêm cột "Implemented by" khi ghi log (không bắt buộc theo template chuẩn).
  - Nếu cả 2 đều không có → báo user: `"Không tìm được thông tin assignee cho member_A — cần dùng git author hoặc bổ sung cột tùy biến trong Source MEMORY §13."`, KHÔNG tự bịa mapping.

Output inline summary (không tạo file riêng trừ khi >20 findings).
