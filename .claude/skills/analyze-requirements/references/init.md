# Analyze Requirements — Mode INIT

> `/analyze-requirements --init @00_input/v1.0/`
> `/analyze-requirements --init @00_input/v1.0/ --figma "https://figma.com/file/xxx"`
> Khi nào: Chưa có MASTER-MEMORY.md, hoặc user bắt đầu project mới.

## Input → Output

| Input (đọc) | Output (tạo) |
|-------------|-------------|
| CLAUDE.md | `02_.../v[X]/MEMORY.md` |
| PIPELINE.md | `02_.../v[X]/requirement_traceability.md` |
| `00_input/[version]/*` | `02_.../v[X]/test_scenario_map.md` |
| Figma (optional) | `02_.../v[X]/test_data_catalog.md` |
| | `02_.../v[X]/risk_assessment.md` |
| | `02_.../MASTER-MEMORY.md` (tạo mới) |
| | `02_.../Project_rule.md` (nếu chưa có) |

---

## Workflow

### Step 1: Đọc context + guard

```
1. PIPELINE.md → check prerequisites (không có hard prerequisite cho INIT)
2. CLAUDE.md → project info, conventions
3. Project_rule.md → nếu tồn tại, đọc naming rules
4. Ghi MASTER-MEMORY §8 analyze-requirements = IN_PROGRESS (nếu MASTER-MEMORY chưa có → tạo sau)
```

Hỏi version nếu chưa biết: **"Đây là version nào? (mặc định: v1.0)"**

### Step 2: Scan + đọc tài liệu input

```
1. Scan 00_input/[version]/
2. Liệt kê files → hỏi: "Phân tích tất cả hay chọn?"
3. Hỏi: "Có Figma link không?"
4. Tạo folder structure:
   mkdir -p 00_input/v[X]/ 00_input/shared/ 02_analyze-requirements/v[X]/
```

**Nếu có Figma + MCP connected:**
```
get_metadata(figma_link) → node map
get_design_context(node_id) → chi tiết frame
get_screenshot(node_id) → visual reference
```
Ghi vào Document Registry: `DOC-v[VERSION]-FIG-[NN]`

### Step 3: Phân rã requirement

```
Module → Feature → Requirement → Acceptance Criteria → Scenario
```

#### Xác định Screen/Block (trước khi derive Scenario)

Với mỗi Module, trước khi liệt kê Scenario, xác định cấu trúc UI 2 tầng:
- **Screen** = 1 màn hình/trang cụ thể trong Module (vd "Danh sách chính sách giá", "Tạo mới yêu cầu").
- **Block** = 1 khu vực chức năng riêng biệt trong Screen. Gộp field/cột/action vào CÙNG 1 Block theo
  1 trong 3 tiêu chí sau (ưu tiên gộp hơn tách nhỏ — mục tiêu: hạn chế tối đa Block chỉ có 1
  Scenario/TC, loại này gây rối khi generate-tc render Excel và khó review):
  1. **Field/cột liên quan chặt** — ≥2 field/cột nằm gần nhau trên màn hình VÀ test được "đủ/thiếu"
     như 1 đơn vị độc lập (vd 8 cột 1 bảng, 5 field 1 form, bộ lọc tìm kiếm).
  2. **Nút/action gần nhau hoặc cùng nhóm thao tác** — các button/action nằm cạnh nhau hoặc phục vụ
     cùng 1 luồng thao tác, dù mỗi nút riêng lẻ chỉ sinh 1-2 Scenario (vd nút Khóa + Mở khóa + Xóa
     trong 1 dòng bảng → gộp 1 Block "Thao tác trên danh sách" thay vì 3 Block rời).
  3. **Chức năng tương tự cùng chủ đề** — các field/action có cùng bản chất nghiệp vụ dù nằm rải rác
     nhiều chỗ trong CÙNG 1 Screen, không nhất thiết cạnh nhau về vị trí (vd validate email trùng +
     rule mật khẩu mặc định + các rule bảo mật khác trong cùng 1 form → gộp 1 Block "Bảo mật tài
     khoản"; các Scenario về phân quyền/quyền truy cập rải rác trong 1 Screen → gộp 1 Block
     "Phân quyền").
  Khu vực chỉ có 1 field/action đơn lẻ, không khớp tiêu chí nào ở trên → KHÔNG tách Block riêng, gộp
  vào Block cha gần nhất theo tiêu chí phù hợp nhất — chỉ để rời/không gắn Block (Screen-level) khi
  thực sự không có Block nào phù hợp.
  **Giới hạn kiến trúc (BẮT BUỘC):** 1 Block chỉ thuộc về đúng 1 Screen — KHÔNG gộp Block xuyên
  Screen, hệ quả trực tiếp từ cấu trúc render 2 tầng Screen→Block ở Excel (`generate-tc/references/
  generate.md` Step 4: Screen là row cha merge A:I, Block là row con merge B:I lồng trong đúng 1
  Screen). Nếu phát hiện nhiều "Screen" trong cùng Module chỉ có 1 Scenario/TC và cùng chủ đề (vd vài
  màn hình phụ đều thuộc nhóm bảo mật/phân quyền) → đây là dấu hiệu ranh giới Screen đang bị tách quá
  nhỏ, không phải vấn đề Block — cân nhắc sửa lại Screen (vd gộp thành 1 Screen cha "Bảo mật & Truy
  cập" chứa các Block con) TRƯỚC khi định nghĩa Block, không tự động "biến Screen thành Block" ở bước
  sau.
- Không phải Scenario nào cũng thuộc 1 Block cụ thể — nhiều Scenario áp dụng CHUNG cho cả Screen,
  không gắn Block nào. Đây là case bình thường, phổ biến (theo ví dụ thật QA cung cấp trong template
  Excel: TC đứng ngay dưới label Screen, trước label Block đầu tiên) — KHÔNG phải ngoại lệ hiếm.
- **Trước khi chốt Block Definitions:** đếm số Block (và số Screen) chỉ có 1 Scenario/TC trong Module.
  Nếu có → rà lại theo tiêu chí 1-3 ở trên xem có gộp được không, chỉ giữ riêng khi thực sự không liên
  quan gì tới Block/Screen khác.

Điền phần **"Block Definitions"** của `assets/scenario-map-template.md` NGAY tại bước này (Module →
Screen → Block → bảng Field/Cột/Action + Rule ngắn), kèm Source Quote/Location như REQ/SC (xem quoting
rule bên dưới — áp dụng y hệt cho Block). Đây là nguồn sự thật cố định: `generate-tc` dùng lại để
group TC theo Screen/Block khi xuất Excel, KHÔNG tự phát hiện lại ranh giới block lúc generate.

Sau khi có Block Definitions, mỗi Scenario derive ở phần dưới PHẢI gắn đúng cột Screen + Block (khớp
tên đã định nghĩa ở trên, không bịa tên block mới ở bảng Scenarios) — hoặc để trống/`—` nếu Scenario
áp dụng chung cho cả Screen, không thuộc Block cụ thể nào.

Mỗi requirement xác định:
- **Requirement ID:** `REQ-[MODULE]-[NNN]`
- **DOC Source:** `DOC-v[VERSION]-[NN]`
- **Loại:** Functional / Non-functional / UI / Business Rule / Integration
- **Mức rủi ro:** High / Medium / Low
- **Testability:** đủ rõ? Mơ hồ → ghi Clarification, KHÔNG đoán

Mỗi requirement cần ít nhất:
- 1 positive scenario (happy path)
- 1 negative scenario (nếu applicable)
- Boundary scenarios (nếu có input ranges)

**UI scenarios (khi có Figma/wireframe):** `SC-[MODULE]-UI-[NNN]`, DOC Source = `DOC-v[VERSION]-FIG-[NN]`

#### Dropdown/Enum option-list completeness (derive kèm scenario hành vi)

Khi 1 Scenario mô tả hành vi **chọn 1 giá trị trong dropdown/select/filter** (lọc danh sách, cascading,
set default...), kiểm tra: giá trị của dropdown đó có phải 1 **enum cố định, nhiều option đặt tên cụ
thể** (không phải free-text/user-generated) không? Nếu có → PHẢI derive thêm **1 Scenario riêng** verify
bản thân dropdown hiển thị **đủ + đúng danh sách giá trị** (option nào, tên gì, group nào, thứ tự nào,
option mặc định là gì) — KHÔNG được coi scenario hành vi (vd "chọn X → lọc đúng Y") là đã cover phần
này, vì 2 cái pass/fail độc lập nhau (dropdown có thể thiếu/sai 1 option nhưng hành vi lọc của các
option còn lại vẫn đúng bình thường).

**Vì sao có rule này:** case thật (CMS v1.4, module LDP, phát hiện 2026-07-22 trước khi generate-tc
chạy) — REQ-LDP-029 mô tả dropdown "Tất cả template" trên Block "Bộ lọc & Tìm kiếm", nhưng chỉ derive
được 1 SC-LDP-061 "chọn 1 template cụ thể → danh sách lọc đúng" (thuần hành vi). Không SC nào verify
dropdown có đủ + đúng cả 5 loại template (định nghĩa ở REQ-LDP-018..022 — TÁCH RIÊNG khỏi REQ-LDP-029
mô tả dropdown). Đây cùng lớp gap với BUG-004 (thiếu cột "Loại gói" ở bảng danh sách PROMO — xem
Field/Column completeness ở `generate-tc/references/generate.md` Step 3b) nhưng xảy ra sớm hơn, ở cấp
SC/analyze-requirements thay vì TC/generate-tc — và khó phát hiện hơn vì REQ định nghĩa NGUỒN giá trị
và REQ mô tả HÀNH VI dùng dropdown đó thường nằm ở 2 chỗ khác nhau trong tài liệu (generate-tc chỉ grep
văn bản gần Scenario, không tự cross-reference REQ khác).

**Cách áp dụng:**
1. Khi gặp Scenario dạng "chọn [dropdown] → [hành vi]", tra xem giá trị dropdown đó được định nghĩa ở
   đâu (cùng REQ, hoặc REQ/module khác — vd 1 enum Template/Trạng thái/Vai trò được tái sử dụng làm
   option cho nhiều dropdown khác nhau trong cùng Module).
2. Nếu dropdown có ≥2 option cụ thể, đặt tên rõ ràng (không phải free-text) → thêm 1 Scenario "Verify
   dropdown [tên field] hiển thị đủ + đúng danh sách giá trị" (Given: mở màn/dropdown MỚI, chưa chọn
   gì; When: mở dropdown; Then: liệt kê đủ N option đúng tên/đúng group/đúng thứ tự + option mặc định
   nếu có — áp dụng nguyên tắc verify pristine state, xem case study BUG-005 ở `generate-tc/references/
   generate.md`).
3. Gắn Scenario mới vào CÙNG Block với Scenario hành vi filter/cascading (không tạo Block riêng — đây
   là field/cụm liên quan chặt theo tiêu chí 1 ở §Xác định Screen/Block phía trên).

#### 🔖 Verbatim quoting (MANDATORY — đọc `references/quoting-guide.md`)

Mỗi REQ + SC + Clarification trong output PHẢI có 3 phần tách biệt (đặt dưới row bảng tương ứng):

1. **Source Quote** — verbatim text từ tài liệu (markdown blockquote `>`). KHÔNG paraphrase, KHÔNG dịch, KHÔNG sửa typo.
2. **Source Location** — `<DOC-ID> §<section> · "<heading>" · <paragraph/table/figure ref> · page <N>`. Đủ chi tiết user mở doc tới đúng vị trí trong <30s.
3. **Analyst Note** — paraphrase tiếng Việt + implicit assumptions + cross-references (clarifications, related REQs).

Implicit requirements (derived từ scope/convention, không quote trực tiếp): đánh dấu `Source Quote: *(Implicit — no direct quote)*` + Analyst Note giải thích derivation.

Long quote (>500 chars): sidecar `02_analyze-requirements/v[VERSION]/quotes/REQ-XXX-NNN.md`; inline first 80 chars + reference.

Multiple sources: number `Source Quote #1`, `#2`, …

Opt-out: `--no-quote` flag (legacy migration only — default ON).

**Mini-example:**

```markdown
### REQ-LOGIN-001 — User SSO authentication

**Source Quote:**
> "User must authenticate via corporate SSO with @<domain> email whitelist."

**Source Location:** `DOC-v[X]-NN §6.1.2 "Authentication Flow" · paragraph 2 · page 14`

**Analyst Note:** Login qua SSO IAM, whitelist domain. Implicit: callback URL pre-registered. Liên quan C1.
```

Xem `references/quoting-guide.md` cho full rules + edge cases (multi-language docs, table/figure refs, multi-source REQs, anti-patterns).

### Step 4: Tạo deliverables

Tạo 5 files trong `02_analyze-requirements/v[VERSION]/`. **Mỗi file PHẢI theo đúng asset template tương ứng — đọc template trước khi ghi, copy header cột + section verbatim (structure-lock, Nguyên tắc cốt lõi #6):**

| Deliverable | Template BẮT BUỘC |
|-------------|-------------------|
| `MEMORY.md` | `assets/version-memory-template.md` |
| `test_scenario_map.md` | `assets/scenario-map-template.md` |
| `requirement_traceability.md` | `assets/requirement-traceability-template.md` |
| `test_data_catalog.md` | `assets/test-data-catalog-template.md` |
| `risk_assessment.md` | `assets/risk-assessment-template.md` |

(MASTER-MEMORY.md ở Step 5 dùng `assets/master-memory-template.md`.)

**Quy tắc quan trọng:**
- KHÔNG tự thêm/bớt/đổi tên cột hay đổi thứ tự section so với template (đảm bảo output đồng nhất mọi session/máy).
- `risk_assessment.md`: dùng DUY NHẤT 1 dạng bảng chi tiết hợp nhất cho mọi module (Risk ID = `RISK-<MODULE>-NN`).
- `MEMORY.md §3 Module Summary`: giữ đủ 12 cột multi-version (version đầu → MODIFIED/CARRIED/DEPRECATED = 0).
- `MEMORY.md §9 TC Generation Log`: header 8 cột (Priority+Mode+Techniques+Review Status; khớp version-memory-template.md, generate-tc 2026-05-29).
- Given/When/Then rõ ràng, cụ thể; mỗi scenario trace ngược về REQ ID + DOC Source.
- Tên Screen/Block ở bảng Scenarios PHẢI khớp verbatim với tên đã định nghĩa ở "Block Definitions"
  (cùng Module) — không tự đổi tên/viết tắt khác đi giữa 2 chỗ.
- Viết tiếng Việt, giữ tiếng Anh cho technical terms.
- DOC ID BẮT BUỘC prefix version: `DOC-v1.0-01` (không phải `DOC-01`).

### Step 5: Tạo MASTER-MEMORY.md

Tạo mới tại `02_analyze-requirements/MASTER-MEMORY.md`.
Dùng template `assets/master-memory-template.md`.
Bao gồm §8 Pipeline Status table (từ PIPELINE.md §5.2).

### Step 6: Tạo Project_rule.md (nếu chưa có)

Nếu chưa tồn tại → tạo từ template, điền project info từ CLAUDE.md.
Hỏi user review + bổ sung Custom Rules §10.

### Step 7: Review + present kết quả

```
📊 Kết quả phân tích v[VERSION]:

Scenarios:
  - NEW: [N] | P1: [n] | P2: [n] | P3: [n]

Clarifications cần xử lý: [N]
Modules: [list]

Bạn muốn review file nào trước?
```

Nhận feedback → nếu cần sửa → chuyển sang Mode UPDATE (`references/update.md`).

### Step 8: Handoff + cập nhật status

```
📋 Analyze v[VERSION] hoàn tất.

Bước tiếp:
  /generate-tc --version v[VERSION]
  /generate-tc --module [MODULE] --version v[VERSION]
```

- Append kết quả vào CLAUDE.md
- Ghi MASTER-MEMORY §8 = **COMPLETED**

---

## Checklist

- [ ] Version folder tạo: `00_input/v[X]/` + `02_.../v[X]/`
- [ ] DOC IDs prefix version: `DOC-v[X]-[NN]`
- [ ] 5 deliverable files tạo trong `02_.../v[X]/`
- [ ] **Structure-lock verified (BLOCKING):** mỗi deliverable khớp ĐÚNG header cột + thứ tự section của asset template tương ứng (KHÔNG thêm/bớt/đổi tên cột, KHÔNG đổi thứ tự section). Cần cột mới → sửa asset template TRƯỚC, KHÔNG tự ý đổi output. FAIL → sửa rồi mới đánh COMPLETED.
- [ ] MASTER-MEMORY.md tạo (bao gồm §8 Pipeline Status)
- [ ] Project_rule.md tạo (nếu chưa có)
- [ ] Scenario Index đầy đủ, Lifecycle = NEW
- [ ] Block Definitions điền đủ cho mọi Module (Screen → Block → Field/Rule), Screen/Block ở bảng
      Scenarios khớp verbatim với Block Definitions
- [ ] Không còn Block/Screen fragmentation quá mức: mọi Block/Screen chỉ có 1 Scenario đã được rà lại
      theo tiêu chí gộp 1-3 (§Xác định Screen/Block) — chỉ giữ riêng khi có lý do không gộp được
- [ ] **Dropdown/Enum option-list completeness:** mọi Scenario dạng "chọn dropdown/select → hành vi"
      đã được rà theo §Dropdown/Enum option-list completeness — nếu dropdown là enum cố định nhiều
      option, có Scenario riêng verify đủ/đúng danh sách giá trị, không chỉ SC test hành vi
- [ ] §8 Pipeline Status = COMPLETED
- [ ] CLAUDE.md append
- [ ] KHÔNG có Java/Python code trong bất kỳ file nào
