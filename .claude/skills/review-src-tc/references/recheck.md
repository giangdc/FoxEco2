# Review SRC-TC — Mode RECHECK

> `/review-src-tc --recheck`

## Workflow
1. Đọc src-tc-review-v[X].md cũ → danh sách findings
2. Re-read affected .java files + TC-MASTER
3. Re-check từng finding:
   - Fixed (code updated match TC) → ✅ Fixed
   - Still open → 🔴 Still Open
4. Re-calculate match rate
5. Cập nhật report:

```markdown
## Recheck — [date]
Previous match rate: 75% → New: 88% (+13%)
Findings: 5 fixed, 2 still open, 0 new
G7: FAIL → PASS ✅
```
