# Verbatim Quoting Guide — analyze-requirements

> Mandatory cho INIT + DELTA mode. Mỗi requirement/scenario/clarification trong output cần 3 phần tách biệt: **Source Quote** (verbatim) + **Source Location** (precise ref) + **Analyst Note** (paraphrase). Mục đích: user verify analyze result vs tài liệu gốc mà không phải đọc lại toàn bộ doc.

## Tại sao cần verbatim quoting?

Skill paraphrase câu từ → ID mapping (`REQ ↔ DOC`) đúng nhưng text-level traceability mất. Hậu quả:
- Reviewer/QA-lead audit không verify được analyst hiểu đúng spec.
- Spec update → khó diff vì không biết requirement nào tương ứng đoạn nào doc.
- User mất confidence, phải tự đọc lại doc → tốn thời gian, dễ miss.

Verbatim quote + location + note tách biệt giải quyết cả 3.

## 3-Field Structure (mandatory format)

Mỗi REQ + SC + Clarification item output theo template sau, đặt trực tiếp dưới row table tương ứng:

```markdown
### REQ-LOGIN-001 — User SSO authentication

**Source Quote:**
> "User must be able to authenticate using corporate SSO via the IAM gateway with workspace@<domain> email whitelist."

**Source Location:** `DOC-v1.2.1-10 §6.1.2 "Authentication Flow" · paragraph 2 · page 14`

**Analyst Note (paraphrase):** Yêu cầu login qua SSO IAM gateway với email domain whitelist. Implicit: callback URL phải được register sẵn ở IAM provider. (Liên quan Clarification C1 — scope whitelist.)
```

## Rules per field

### Field 1: Source Quote

| Quy tắc | Chi tiết |
|---|---|
| **Verbatim** | Giữ nguyên ngôn ngữ + formatting + typo của tài liệu gốc. KHÔNG paraphrase, KHÔNG sửa typo, KHÔNG dịch. |
| **Format** | Markdown blockquote `>`. Mỗi đoạn trên 1 hoặc nhiều dòng blockquote. |
| **Multi-paragraph** | Cho phép ellipsis `(...)` khi cắt giữa đoạn. Đánh dấu rõ vị trí cắt bằng dòng `> (...)`. |
| **Long quote (>500 chars)** | Sidecar file: `02_analyze-requirements/v[X]/quotes/REQ-XXX-NNN.md` chứa full quote; main MEMORY chỉ inline first 80 chars + `(full quote: quotes/REQ-XXX-NNN.md)`. |
| **Different language** | Quote nguyên gốc (Anh/Trung/Nhật/…). Bản dịch tiếng Việt CHỈ trong Analyst Note, KHÔNG trong Source Quote. |
| **Inline formatting** | Giữ nguyên: `code`, **bold**, *italic*, lists, dấu câu. |
| **Special chars** | Escape markdown khi cần (`\\|` cho pipe trong cell, `\\*` cho asterisk literal). |

### Field 2: Source Location

Format chuẩn:

```
<DOC-ID> §<section> · "<heading>" · <element-ref> · page <N>
```

| Element | Mô tả | Ví dụ |
|---|---|---|
| `DOC-ID` | Đã đánh số registry §2 | `DOC-v1.2.1-10` |
| `§<section>` | Số mục theo doc | `§6.1.2`, `§7.3` |
| `"<heading>"` | Tên mục (quoted) | `"Authentication Flow"` |
| `<element-ref>` | Cụ thể vị trí trong section | `paragraph 2`, `line 14`, `bullet 3`, `Table 7.3.1`, `Figure 4.2` |
| `page <N>` | Số trang | `page 14` (omit nếu doc không có pagination, vd HTML) |

**Fallback hierarchy** khi doc không có heading rõ:

1. `§heading` (nếu có)
2. `page N · paragraph M` (nếu có pagination)
3. `line N` (nếu plain text)
4. `text-anchor "<first-5-words>..."` (last resort — search anchor)

**Special doc types:**

| Doc type | Location format example |
|---|---|
| Word/PDF | `DOC-v1-01 §6.1.2 "Login Flow" · paragraph 2 · page 14` |
| HTML | `DOC-v1-02 §Tab "Authentication" · element #login-form · DOM path body>main>section[2]` |
| Excel | `DOC-v1-03 sheet "API Spec" · cell B5:F12 · range "Auth endpoints"` |
| Markdown | `DOC-v1-04 §"Login Flow" · line 42-50` |
| Figma | `DOC-v1-FIG-01 frame "Login screen" · node id 5:1234 · annotation "SSO button"` |
| Jira ticket | `DOC-v1-JIRA-01 ticket DASH-123 · field "Acceptance Criteria" · bullet 3` |

### Field 3: Analyst Note

| Quy tắc | Chi tiết |
|---|---|
| **Paraphrase rõ** | Bằng ngôn ngữ chính của project (tiếng Việt default). Diễn giải spec, KHÔNG copy verbatim. |
| **Implicit assumption** | Đánh dấu rõ với prefix `Implicit:` để reader biết đây là derivation, không nằm direct trong doc. |
| **Cross-reference** | Liên kết tới clarifications (`C<N>`), related REQs (`REQ-<X>-<NNN>`), bug history (`BUG-<NNN>`). |
| **KHÔNG thay thế Source Quote** | Analyst Note bổ sung context — Source Quote vẫn là canonical reference. |
| **Length** | 1-5 câu thường đủ. Quá dài → split thành multiple notes hoặc move vào risk_assessment. |

---

## Edge cases

### EC1: Implicit requirement (không có direct quote)

Khi requirement derived từ scope statement, convention, hoặc absence trong doc:

```markdown
### REQ-AUTH-007 — Session timeout default 30 phút

**Source Quote:** *(Implicit — no direct quote)*

**Source Location:** `DOC-v1.2.1-10 §6.1 "Authentication" · scope statement` (derived from omission — doc không specify session lifetime, IAM gateway default applies)

**Analyst Note:** Doc không nêu cụ thể session lifetime; theo convention IAM corporate gateway = 30 phút idle. Cần Clarification C4 confirm với IAM team. Test coverage: phải verify session expire chính xác sau 30 phút.
```

### EC2: Multiple sources per REQ

Khi 1 requirement được spec từ ≥2 docs:

```markdown
### REQ-PERIOD-001 — Period switcher 4 tabs

**Source Quote #1** (functional spec):
> "User can switch period among Day / Week / Month / Year tabs at top of dashboard."

**Source Location #1:** `DOC-v1.3-08 §4.2 "Period UI" · paragraph 1 · page 9`

**Source Quote #2** (data contract):
> "API parameter `period_type` accepts: D | W | M | Y."

**Source Location #2:** `DOC-v1.3-09 §3.1 "API Contract" · Table 3.1 row 4 · page 5`

**Analyst Note:** Yêu cầu hợp nhất từ 2 docs: UI có 4 tab, mapping với API `period_type` enum. Cross-validate: UI selection → API call value phải match 1-1.
```

### EC3: Table/figure reference

Khi requirement đến từ table cell hoặc figure:

```markdown
### REQ-HR-003 — HR unit hierarchy 4 cấp

**Source Quote:**
> Table 7.3.1 "HR Unit Mapping":
> | Cấp | Tên | Code |
> |---|---|---|
> | 1 | Khối | KHOI |
> | 2 | Bộ phận | BP |
> | 3 | Nhóm | NHOM |
> | 4 | Nhân viên | NV |

**Source Location:** `DOC-v1.2.1-10 §7.3 "HR Module" · Table 7.3.1 "HR Unit Mapping" · page 28`

**Analyst Note:** HR có 4 cấp drill-down rõ. Implicit: leaf level (cấp 4 NV) là cá nhân — không phải subgroup. Drill chain test cần cover từ Khối → Bộ phận → Nhóm → leaf NV.
```

### EC4: Cross-language document

Khi tài liệu tiếng Anh nhưng project tiếng Việt:

```markdown
### REQ-SALES-005 — Camera service excluded from RM

**Source Quote:**
> "The cust_lost metric is not applicable to Camera service line — backend stored procedure rejects this combination with ORA-20102."

**Source Location:** `DOC-v1.3-09 §5.2 "RM Metric Scope" · paragraph 4 · page 18`

**Analyst Note:** Endpoint `cust_lost` KHÔNG hỗ trợ service=Camera (backend reject với mã lỗi ORA-20102). Mobile app phải filter Camera khỏi RM call. Test coverage: negative TC verify error response + graceful UI handling.
```

### EC5: Scenario quote (justify Given/When/Then)

Source Quote trong scenario_map.md justify scenario design:

```markdown
### SC-LOGIN-001 — Happy path SSO success

**Given/When/Then row:** (see main table above)

**Source Quote:**
> "On successful SSO callback, app receives JWT token, persists to secure storage, and navigates to default landing (Sales tab)."

**Source Location:** `DOC-v1.2.1-10 §6.1.5 "Post-login flow" · paragraph 1 · page 16`

**Analyst Note:** Happy path: callback success → token persist → land Sales. Test verify: token visible in storage; landing screen = Sales tab default; no flash screen between callback và Sales.
```

### EC6: Clarification quote (ambiguous text)

Clarification item track exactly đoạn nào ambiguous:

```markdown
### C3 — Report table column field mapping

**Source Quote (ambiguous):**
> "Bảng báo cáo hiển thị 6 cột: kỳ trước, kỳ hiện tại, lũy kế, kỳ cùng năm trước, kế hoạch, chênh lệch."

**Source Location:** `DOC-v[X]-NN §8.2.1 "Report table layout" · paragraph 3 · page 31`

**Analyst Note:** Doc không specify backend field name mapping cho 6 cột (tên tiếng Việt label ↔ schema field name). Cần BA + Backend confirm mapping document. Risk: Test cases sẽ Blocked nếu không resolve trước generate-tc. (Khi resolved, link sang field-mapping reference file trong test_data_catalog.)
```

---

## Workflow integration

### INIT mode (new analysis)

1. Đọc tài liệu input → đánh DOC ID.
2. **Cho mỗi requirement identify được** trong doc:
   - Copy verbatim text → Source Quote field.
   - Note location → Source Location field.
   - Write Vietnamese paraphrase + implicit notes → Analyst Note field.
3. **Cho mỗi scenario** derived từ requirement:
   - Source Quote = đoạn doc justify scenario shape (có thể quote khác requirement quote).
   - Analyst Note: explain Given/When/Then derivation.
4. **Cho mỗi clarification:**
   - Source Quote = exact ambiguous text.
   - Analyst Note: explain ambiguity + proposed resolution.

### DELTA mode (version update)

| Lifecycle | Quote handling |
|---|---|
| **NEW** | Capture new Source Quote từ new doc (mandatory). |
| **MODIFIED** | Capture **2** Source Quotes: parent version + new version. Show diff trong Analyst Note. Reference: `Source Quote (old) — DOC-v1.2-07 §X` + `Source Quote (new) — DOC-v1.3-08 §Y`. |
| **CARRIED** | KHÔNG cần re-quote. Reference parent version: `Source Quote: see v1.2 REQ-XXX-NNN`. Location field link parent doc. |
| **DEPRECATED** | Keep parent quote + add `Deprecated reason` trong Analyst Note. |

### Backward-compat

- Existing v1.0/v1.2/v1.3/v1.2.1 analyses **KHÔNG cần retroactive backfill.** Plan chỉ áp dụng version mới sau merge.
- Skill prompt mặc định ON. Opt-out qua `--no-quote` flag (legacy quick migration).
- Templates updated render OK với legacy data (rows không có Source Detail block chỉ hiển thị bảng — không break).

---

## Anti-patterns (KHÔNG được làm)

| Anti-pattern | Tại sao sai | Fix |
|---|---|---|
| Quote bản dịch tiếng Việt khi doc gốc tiếng Anh | Lose verbatim guarantee | Quote nguyên Anh + dịch trong Analyst Note |
| Source Location chỉ ghi `DOC-v1-01` không có section | Không navigable | Phải có ≥ section/page/line ref |
| Analyst Note copy paste y hệt Source Quote | Redundant + giả vờ paraphrase | Analyst Note phải thêm context, không lặp |
| Skip Source Quote vì "quá hiển nhiên" | Mất traceability | Mọi REQ MUST có quote (hoặc đánh dấu Implicit) |
| Quote >2 paragraphs inline trong MEMORY | File phình to | Dùng sidecar `quotes/REQ-XXX-NNN.md` |
| Paraphrase code/identifier (vd đổi `cust_lost` thành "metric mất khách") | Lose technical precision | Giữ nguyên technical terms — kể cả trong Analyst Note |
| Source Quote chèn analyst comment giữa (vd `> "User must... [analyst: và cũng ngụ ý] ... authenticate"`) | Pollutes verbatim | Analyst comments CHỈ trong Analyst Note field |

---

## Out-of-scope (chưa cover, sẽ mở rộng theo nhu cầu)

- CJK vertical text orientation
- RTL embedded trong LTR doc
- Mathematical notation rendering (LaTeX trong PDF)
- Hand-drawn diagrams (cần OCR/manual transcription)
- Encrypted/password-protected docs (user phải decrypt trước)
- Live-update docs (Confluence/Notion realtime — snapshot at analyze time, note `accessed YYYY-MM-DD`)

User có thể request mở rộng quoting-guide với edge case mới.

---

## Generic examples (project-agnostic)

### Example 1: Web e-commerce — checkout flow

```markdown
### REQ-CHECKOUT-001 — Cart total includes tax + shipping

**Source Quote:**
> "The displayed cart total must include applicable sales tax (computed via TaxCalc API) and shipping cost (per shipping zone)."

**Source Location:** `DOC-v2.0-03 §4.3 "Pricing Display" · paragraph 1 · page 12`

**Analyst Note:** Cart total = subtotal + tax + shipping. Tax từ TaxCalc API external service. Shipping varies by zone (catalog ở §4.4). Cần test: tax calculation accuracy + zero-tax states (vd export sale) + free-shipping threshold edge cases.
```

### Example 2: REST API — auth endpoint

```markdown
### REQ-API-AUTH-001 — POST /auth/login rate limit

**Source Quote:**
> "POST /auth/login is rate-limited to 5 attempts per IP per 15 minutes. Subsequent attempts return HTTP 429 with Retry-After header."

**Source Location:** `DOC-v3.0-API §2.1 "Auth endpoints" · Table 2.1.2 row 1 · page 7`

**Analyst Note:** Rate limit 5/15min per IP. HTTP 429 + Retry-After. Test coverage: BVA (attempt 5 OK, attempt 6 fail), error handling (Retry-After respected), state reset after window.
```

### Example 3: Mobile app — settings persistence

```markdown
### REQ-SETTINGS-002 — Theme preference persists across reinstalls

**Source Quote:** *(Implicit — no direct quote)*

**Source Location:** `DOC-v1.0-spec §5.1 "Settings" · scope statement` (derived from "user preferences" generic claim)

**Analyst Note:** Doc nêu "user preferences persist" general, không specify scope. Implicit: phải survive app reinstall (qua cloud sync hoặc OS-backed keystore). Cần Clarification — backend cloud sync chưa có ở v1.0, có thể fallback OS keychain. Test coverage cần defer pending clarification.
```
