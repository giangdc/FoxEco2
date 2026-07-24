# Review TC — Mode MODULE

> `/review-tc --module Login`

Giống Mode FULL nhưng:
- Parse chỉ 1 sheet TC thuộc module chỉ định — match theo `C3` (Tên chức năng) của sheet, hoặc theo cột D (tên tab) tương ứng ở sheet `Dashboard` nếu tên module không khớp trực tiếp tên tab
- R2 coverage: chỉ check scenarios của module đó
- R2-16/R2-17 (RTM/Dashboard cross-check): vẫn chạy nhưng chỉ báo finding liên quan đến sheet đang review
- Output: inline summary (không tạo file riêng)
- Score: module-level score (không phải overall)
