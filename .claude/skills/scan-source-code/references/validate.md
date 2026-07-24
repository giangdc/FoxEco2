# Scan Source Code — Mode VALIDATE

> `/scan-source-code --validate`
> So sánh MEMORY với code thực tế, báo cáo inconsistencies.

## Workflow

### Step 1: Đọc MEMORY + scan actual files

### Step 2: Validate từng section

| Check | Compare | Finding |
|-------|---------|---------|
| §1 tree vs disk | MEMORY file list vs actual files | Missing in MEMORY / Missing on disk |
| §2 tech stack | pom.xml vs MEMORY §2 | Version mismatch |
| §5 conventions | Scan actual naming patterns vs MEMORY §5 | New patterns not recorded |
| §6 page classes | MEMORY entries vs actual files | Class exists but not in MEMORY, or vice versa |
| §6 elements | @FindBy count in code vs MEMORY §6 | Element count mismatch |
| §7 test classes | MEMORY entries vs actual files | Method count mismatch |
| §7 coverage | §7 SC mappings vs Version MEMORY §4 | Scenarios without test methods |

### Step 3: Present findings

```
🔍 Validate results:

✅ Consistent: §1, §2, §3
⚠️ Inconsistent:
  - §6: LoginPage has 6 elements on disk, MEMORY says 4 (2 new since last scan)
  - §7: DashboardTest has 8 methods, MEMORY says 6 (2 new)
  - §5: Found pattern "lbl[Name]" (3 occurrences) not in conventions

Recommend: /scan-source-code --delta (update MEMORY)
```

KHÔNG sửa MEMORY — chỉ report.
