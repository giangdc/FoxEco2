# Review SRC-TC — Mode FULL

> `/review-src-tc`

## Workflow

### Step 1: Đọc context + guard
Check implement-automation ≥ PARTIAL + generate-tc ≥ PARTIAL.
Đọc Source MEMORY §7 (Test Registry), §13 (Implementation Log).
Ghi §8 = IN_PROGRESS.

### Step 2: Parse TC-MASTER

Template ISC (42 cột A-AP, xem `generate-tc/references/generate.md` §"TC Structure"). Extract per TC:
- TC ID (**cột A**, formula-derived `[Mã CN].[STT]` — vd `TC_01.2`, đọc giá trị đã resolve `data_only=True`)
- Req ID (**cột B** — có thể nhiều giá trị, phân cách dấu phẩy) — thay cho SC ID (template không còn Scenario ID column)
- Steps (**cột H**), Expected (**cột I**) — **test data nằm inline trong text Steps, không có cột Test Data riêng**
- Remark (**cột AP**, cột 42 — technique tag `Technique: <tag>` nếu có, cần cho M4-04; có thể nối nhiều ghi chú bằng ` | `)

### Step 3: Read test classes
Read .java files từ `10_source-code/`. Extract per method:
- Method name, `@Test description` (TC ID + Req ID)
- `// Step N:` comments → paired with action lines below
- `// Expected N:` comments → paired with assertion lines below
- Hardcoded data values (string literals in method body)

### Step 4: Pair TC ↔ method

**Match strategy:**
1. `@Test description` chứa TC ID → direct match
2. Source MEMORY §13 mapping (TC ID → method name)
3. Method name contains scenario hint → fuzzy match

**Results:**
- **MATCHED:** TC có method tương ứng
- **NOT_IMPLEMENTED:** TC không có method → gap
- **ORPHAN_CODE:** Method không link về TC nào → dead code hoặc undocumented

### Step 5: Agent review (hoặc direct)

**Agent mode** (implement-automation ≥ PARTIAL, no `--direct`):

Agent nhận: system prompt từ AGENT.md §3b (persona + format) + **check definitions M1-M4 bên dưới** (qua payload).
**M1-M4 checks ở đây là SINGLE SOURCE OF TRUTH** — cả direct mode và agent mode đều dùng.
    "pairs": [
        {
            "tc_id": "TC_01.1",
            "req_id": "REQ-01",
            "tc_steps": [
                "1. Nhập 'user@test.com' vào field Email",
                "2. Nhập 'Test@123' vào field Password",
                "3. Nhấn button Đăng nhập"
            ],
            "tc_expected": [
                "1. Redirect về trang Dashboard",
                "2. Hiển thị username 'user@test.com' trên header"
            ],
            "tc_data": {"Email": "user@test.com", "Password": "Test@123"},
            "code_method": "testLoginSuccess",
            "code_file": "LoginTest.java",
            "code_steps": [
                "// Step 1: Nhập 'user@test.com' vào field Email\nloginPage().enterEmail(\"user@test.com\");",
                "// Step 2: Nhập 'Test@123' vào field Password\nloginPage().enterPassword(\"Test@123\");",
                "// Step 3: Nhấn button Đăng nhập\nloginPage().clickLogin();"
            ],
            "code_assertions": [
                "// Expected 1: Redirect về trang Dashboard\nassertTrue(dashboardPage().isDisplayed());"
            ],
            "code_data": {"email": "user@test.com", "password": "Test@123"}
        }
    ],
    "not_implemented": ["TC_01.5", "TC_01.6"],
    "orphan_methods": ["testOldFeature"]
}
```

> `tc_data` không đến từ 1 cột riêng — parse literal value trực tiếp từ text `tc_steps`/`tc_expected` (regex/manual extraction giá trị trong dấu nháy hoặc sau từ khóa "nhập/chọn"). Chỉ dùng để đối chiếu M3, không phải trường Excel thật.

Agent applies M1-M4 checks (system prompt trong AGENT.md §3b):

**M1: Step Coverage**
| Check | Severity | Logic |
|-------|----------|-------|
| M1-01 | Critical | TC step thiếu code → `// Step N` comment hoặc action không có |
| M1-02 | Major | Code có step thừa → action không match TC step nào |
| M1-03 | Minor | Step comment text khác TC → `// Step 1: Login` vs TC "Nhấn Đăng nhập" |
| M1-04 | Minor | Step numbering sai → `// Step 3` nhảy qua `// Step 2` |

**M2: Assertion Coverage**
| Check | Severity | Logic |
|-------|----------|-------|
| M2-01 | Critical | TC expected thiếu assertion → `// Expected N` hoặc assert không có |
| M2-02 | Major | Expected không thể automate nhưng thiếu `// MANUAL VERIFY` |
| M2-03 | Minor | Assertion message không chứa "Expected N:" prefix |
| M2-04 | Minor | Assertion type mismatch → `assertTrue` khi cần `assertEquals` |

**M3: Data Accuracy**
| Check | Severity | Logic |
|-------|----------|-------|
| M3-01 | Critical | Hardcoded data ≠ giá trị inline trong TC **Steps (cột H)** → code dùng "admin" nhưng TC nói "user@test.com". Template không có cột Test Data riêng — giá trị chuẩn nằm trong text Steps. |
| M3-02 | Major | Data hardcoded thay vì parameterized (khi cần) |
| M3-03 | Minor | Data format khác → code "user@test.com" vs TC "user@test.com " (trailing space) |

**M4: Traceability**
| Check | Severity | Logic |
|-------|----------|-------|
| M4-01 | Major | `@Test description` thiếu TC ID (cột A) |
| M4-02 | Major | `@Test description` thiếu Req ID (cột B) — template ISC không còn Scenario ID column, Req ID là khóa truy vết bắt buộc thay thế |
| M4-03 | Minor | Method name không reflect scenario |
| M4-04 | Minor | **(cập nhật 2026-07-21, trước đây "Notes column")** Khi Version MEMORY §9 (TC Gen Log) Mode = `comprehensive`/`selective` và TC **Remark (cột AP)** có `Technique: <tag>`: `@Test description` nên include technique tag để truy nguồn (e.g., `@Test(description = "TC_03.14 / REQ-08 / Technique: BVA-min-1")`). Missing tag = Minor info — không break logic. |

**Direct mode:** Main Claude runs M1-M4 + disclaimer + score capped 85.

### 🆕 Comprehensive mode awareness (2026-05-29)

Khi Version MEMORY §9 (TC Gen Log) Mode = `comprehensive` HOẶC `selective`, derived TCs (TC ID > baseline count) có thể được implement bằng 2 cách:

**A. 1:1 mapping** — mỗi derived TC có method riêng:
```java
@Test(description = "TC_03.14 / REQ-08 / Technique: BVA-min-1")
public void testSsoLoginPasswordLength7() { ... }

@Test(description = "TC_03.15 / REQ-08 / Technique: BVA-min")
public void testSsoLoginPasswordLength8() { ... }
```

**B. 1:N parameterized** — 1 method covers N derived TCs via `@DataProvider`:
```java
@DataProvider(name = "passwordBoundary")
public Object[][] data() {
    return new Object[][] {
        {7, false, "TC_03.14", "BVA-min-1"},
        {8, true, "TC_03.15", "BVA-min"},
        {9, true, "TC_03.16", "BVA-min+1"},
        // ...
    };
}

@Test(dataProvider = "passwordBoundary",
      description = "REQ-08 / Technique: BVA suite (TC_03.14..TC_03.20)")
public void testSsoLoginPasswordBoundary(int len, boolean accept, String tcId, String tag) {
    // ...
}
```

**Reviewer xử lý:**

| Pattern | M1 (Step Coverage) behavior | Orphan-method classification |
|---|---|---|
| Pattern A (1:1) | Apply M1 chuẩn — verify mỗi method có TC ID comment | Method không tồn tại trong TC-MASTER = orphan |
| Pattern B (1:N parameterized) | Verify `@DataProvider` data rows = derived TC count; description chứa TC ID range (`TC_03.14..TC_03.20`) hoặc Req ID; M1-01 KHÔNG raise "missing code per derived TC" — single method valid cho cả N TCs | DataProvider rows mapping vào TC IDs trong description → KHÔNG flag orphan |
| Hybrid | Document trong Source MEMORY §13 Implementation Log: cột "Test method" can be single hoặc range (e.g., `testSsoLoginPasswordBoundary` covers TC_03.14..TC_03.20) | Per case |

**Edge cases additions:**

| Scenario | Handling |
|---|---|
| Comprehensive mode + DataProvider parameterized | M1 PASS nếu `@DataProvider` size = derived TC count. Verify description chứa Req ID + TC ID range. |
| Method count < TC count (post-comprehensive) | Acceptable nếu parameterized — log INFO instead of WARNING |
| Description chứa "Technique:" tag | M4-04 PASS — improved traceability |
| Description thiếu "Technique:" tag (Mode=comprehensive) | M4-04 Minor — suggest add for traceback |
| Source MEMORY §13 entry list TC ID range (`TC_03.14..TC_03.20`) | Treat as 1:N parameterized, accept |

### Step 6: Format report

```markdown
# SRC-TC Review Report — v[X]

> Generated: [datetime]
> Mode: Agent / Direct
> TC-MASTER: [file]
> Source: [repo path]

## TC Implementation Coverage
| Status | Count | % |
|--------|-------|---|
| Fully matched | [N] | [%] |
| Partial matched | [N] | [%] |
| Not implemented | [N] | [%] |
| Orphan code | [N] | — |

## Match Rate: [N]%

## Findings

### 🔴 CRITICAL
**[M1-01] TC_01.3 — Missing step 2 in code**
- TC Step 2: "Chọn 'Remember me' checkbox"
- Code: No action for checkbox — only email + password + click login
- Impact: Checkbox step not tested

### 🟠 MAJOR
**[M3-01] TC_01.2 — Wrong test data**
- TC Steps (cột H): Email = "user@"
- Code line 45: loginPage().enterEmail("invalid-email")
- Impact: Testing different invalid format than specified

...

## Not Implemented TCs
| TC ID | Req ID | Module | Priority | Reason |
|-------|-------|--------|----------|--------|
| TC_01.5 | REQ-05 | Login | Medium | No test method |

## Orphan Code
| Class | Method | Notes |
|-------|--------|-------|
| LoginTest | testOldFeature | No TC mapping — possibly dead code |

## Quality Gate G7: [match_rate]% — [PASS ≥70 / FAIL <70]
```

**Output:** `11_tc-review/src-tc-review-v[X].md`

### Step 7: §8 = COMPLETED

## Checklist
- [ ] TC-MASTER parsed (42 cột, template ISC — cột A formula, đọc `data_only=True`)
- [ ] Test classes read (.java files)
- [ ] TC ↔ method paired
- [ ] Agent called (hoặc fallback + disclaimer)
- [ ] M1-M4 checks applied
- [ ] Match rate calculated
- [ ] Not-implemented TCs listed
- [ ] Orphan code listed
- [ ] Report file tạo
- [ ] §8 = COMPLETED
