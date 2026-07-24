# Review TC — Mode RECHECK

> `/review-tc --recheck`
> Khi nào: Đã sửa TC theo findings trước, muốn verify.

## Workflow
1. Đọc review-report cũ → danh sách findings
2. Parse TC-MASTER mới (có thể đã update)
3. Re-check từng finding:
   - Finding resolved → status = **Fixed**
   - Finding vẫn còn → status = **Still Open**
   - New issue phát hiện → status = **New**
4. Re-calculate score
5. Cập nhật review-report:

```markdown
## Recheck — [date]

| Finding | Previous | Now | Status |
|---------|----------|-----|--------|
| R3-01 TC_02.3 (Login) | Step vague | Step updated | ✅ Fixed |
| R2-03 Login sheet | No negative TC | 2 negative TCs added | ✅ Fixed |
| R4-02 TC_05.5 (Dashboard) | High for edge case | Still High | 🔴 Still Open |

Previous score: 65 → New score: 78 (+13)
G1: FAIL → PASS ✅
```

Lưu ý: Testcase ID (`TC_[MãCN].[STT]`) tự sinh lại theo formula mỗi khi thứ tự row thay đổi — khi re-parse để recheck, match finding cũ với TC hiện tại theo **Req ID + DOC Source + Test Title** (ổn định hơn ID nếu row bị thêm/xoá), không chỉ theo ID.
