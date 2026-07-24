# AI QA Framework — Skill Toolkit Onboarding

> Hướng dẫn nhanh để hiểu và sử dụng bộ skill toolkit `~/.claude/skills/` (qc-claude-v1). Đọc < 1h là grasp được full picture; sau đó dùng làm reference daily.
>
> **Framework-level doc — KHÔNG chứa thông tin project cụ thể.** Mỗi project sử dụng toolkit có docs riêng (`CLAUDE.md`, `PIPELINE.md`, `COMMANDS.md`, `Project_rule.md`) cho project-specific context, conventions, version state.
>
> **Audience tags trong toàn bộ doc:**
> - 🔵 **Both** — áp dụng cho mọi member
> - 👤 **Non-tech** — manual tester, BA, QA lead
> - 🛠 **Tech** — automation engineer, dev-in-test

**Toolkit version:** qc-claude-v1 · v1.0 (released 2026-06-05) · **Skills:** 14 core + 1 utility · **Doc maintained by:** Toolkit owner

---

## Table of Contents

1. [Đọc gì trước — TL;DR + Audience Map](#1-đọc-gì-trước--tldr--audience-map)
2. [Mental Model — Pipeline + MEMORY system](#2-mental-model)
3. [Setup từ máy zero (~30 min)](#3-setup-từ-máy-zero-30-min)
4. [Skill Catalog (14 + 1 utility)](#4-skill-catalog-14--1-utility)
5. [8 Common Workflows (playbooks)](#5-8-common-workflows-playbooks)
6. [Naming Conventions](#6-naming-conventions-framework-defaults)
7. [NEW Features 2026-05-29](#7-new-features-2026-05-29)
8. [Folder Layout (per-project structure)](#8-folder-layout-per-project-structure)
9. [Quality Gates G1-G6 (framework baseline)](#9-quality-gates-g1-g6-framework-baseline)
10. [Golden Rules & Pitfalls](#10-golden-rules--pitfalls)
11. [FAQ / Troubleshooting](#11-faq--troubleshooting)
12. [Glossary + Reference Links](#12-glossary--reference-links)

---

## 1. Đọc gì trước — TL;DR + Audience Map

### 🔵 Toolkit là gì? (3 câu)

Bộ **14 core skills + 1 utility** chạy trong Claude Code, hỗ trợ QA pipeline end-to-end: phân tích requirement → viết test case → review → automate → execute → log bug → report. Skills tự update lẫn nhau qua **MEMORY system** (MASTER + Version + Source); mỗi skill có pipeline position rõ ràng, không chồng chéo. Goal: tester tập trung vào **chất lượng**, AI lo phần **boilerplate + traceability + consistency check**.

### 🔵 Quick Start trong project bất kỳ

Sau khi cd vào project directory (đã setup theo framework structure):

```bash
# 1. Xem pipeline status hiện tại (skill nào đã chạy, đang ở đâu)
cat 02_analyze-requirements/MASTER-MEMORY.md | grep -A 20 "## 8\. Pipeline Status"

# 2. Health check toàn project (catches data drift, orphan refs)
# Trong Claude Code:
/health-check --full

# 3. Xem command cheat sheet của project
cat COMMANDS.md
```

### Audience Map — đọc section nào?

| Role | Sections must-read | Sections skip |
|---|---|---|
| 👤 **Manual tester / BA** | 1, 2 (overview), 3a + 3d-3e, 4 (filter 👤+🔵), 5 (workflows 1-3, 6-8), 6, 7, 9, 10, 11 (filter 🔵), 12 | 3b-3c (tech setup), 4 (🛠 skills detail), 5 (workflows 4-5), 11 (🛠 items) |
| 👤 **QA lead** | All sections (skim 3b-3c) | — |
| 🛠 **Automation engineer** | All 12 sections | — |
| 🔵 **Daily reference** | Section 4 (catalog), 5 (workflows), 6 (naming), 11 (FAQ) | — |

---

## 2. Mental Model

### 🔵 Pipeline 12 bước (DAG)

```
                   init-project (00_) ─── create-test-plan (01_)
                          │                       │
                          └─────────┬─────────────┘
                                    ↓
                          analyze-requirements (02_)
                                    ↓
                            generate-tc (03_)
                                    ↓
                              review-tc (11_)
                                    ↓
                              vibe-test (08_)   ◄── AI thay manual tester
                          (validate TC + capture locators)
                                    ↓
              scan-source-code (10_) → implement-automation (10_) → review-src-tc (11_)
                                              ↓
                                    execute-maintain (10_§15)
                                              ↓
                                       log-bug (05_)
                                              ↓
                                      test-report (08_ + 09_)

Cross-cutting:  ★ health-check ★   (chạy bất kỳ lúc nào — validate consistency)
                ★ fetch-us ★       (utility — kéo Jira US về 00_input/)
```

**Đặc điểm:**
- Mỗi mũi tên = dependency. Skill downstream cần status `≥ PARTIAL` từ skill upstream.
- `vibe-test` chen giữa review-tc và implement-automation: AI test thật trước khi auto-code → giảm rework do TC sai.
- `health-check` không nằm trong main chain — chạy independent để verify state.

### 🔵 3-tier traceability chain

Mọi artifact link ngược về DOC gốc qua chain:

```
DOC (tài liệu spec gốc)
  └── REQ (requirement extracted)
       └── SC (scenario Given/When/Then)
            └── TC (test case Excel)
                 └── Test Method (code)
                      └── Test Result (Pass/Fail/Skip)
                           └── Bug Report (nếu Fail = real bug)
                                └── Final Report (stakeholder GO/NO-GO)
```

Mỗi tier có ID convention rõ ràng (xem §6). Mỗi skill phải maintain link này — health-check kiểm tra orphan/broken links.

### 🔵 MEMORY system — 3 lớp

| MEMORY | Path | Owner | Scope |
|---|---|---|---|
| **MASTER-MEMORY** | `02_analyze-requirements/MASTER-MEMORY.md` | analyze-requirements | **Cross-version registry** — version timeline, DOC ID global, scenario lifecycle, regression scope, §8 Pipeline Status (live) |
| **Version MEMORY** | `02_analyze-requirements/v[X]/MEMORY.md` | analyze-requirements | **Per-version** — scenarios, requirements, clarifications, test data refs, TC Gen Log §9 |
| **Source MEMORY** | `10_source-code/MEMORY.md` | scan-source-code | **Code-side** — Page Object classes, locators, test classes, §15 Execution Log, §16 Fail Registry |

**Quan trọng:** Skills ĐỌC + GHI vào MEMORY tự động. **KHÔNG manually edit** trừ khi sửa typo nhỏ. Skills sẽ overwrite changes nếu run lại.

### 🔵 §8 Pipeline Status (live state)

MASTER-MEMORY có table §8 tracking real-time skill state:

| Status | Meaning |
|---|---|
| `NOT_STARTED` | Skill chưa chạy lần nào |
| `IN_PROGRESS` | Đang chạy (Last Run < 1 ngày cũ — nếu > 1 ngày có thể đã crash, health-check raise WARNING) |
| `PARTIAL` | Đã chạy một phần (vd 1/3 modules) — downstream có thể start nhưng cần lưu ý scope |
| `COMPLETED` | Hoàn thành toàn bộ scope |
| `FAILED` | Lỗi mid-run — downstream KHÔNG nên chạy cho đến khi resolve |

---

## 3. Setup từ máy zero (~30 min)

> 👤 **Manual tester / BA:** Chỉ cần 3a + 3c (Atlassian MCP nếu push Jira) + 3d + 3e. Skip 3b (Java/Maven) — không cần chạy automation.
>
> 🛠 **Tech:** Cần đủ 3a-3e.

### 3a. Prerequisites 🔵

| Tool | Version | Cách check | Install link |
|---|---|---|---|
| Claude Code | latest | `claude --version` | claude.ai/code |
| Git | 2.30+ | `git --version` | git-scm.com |
| Java 21 🛠 | 21.x | `java -version` | adoptium.net |
| Maven 🛠 | 3.9+ | `mvn -version` | maven.apache.org |
| Node.js 🛠 | 18+ | `node -v` | nodejs.org (cho MCP servers) |
| Python 3 | 3.9+ | `python3 --version` | python.org (cho xlsx utilities) |

### 3b. Install skill toolkit 🔵

Skills nằm ở **user-level** (`~/.claude/skills/`) — share giữa các projects trên cùng máy.

```bash
# Kiểm tra đã có chưa
ls ~/.claude/skills/ | head -5

# Nếu chưa, clone từ team toolkit repo (IT cung cấp URL)
git clone <skill-toolkit-repo-url> ~/.claude/skills/

# Verify (phải thấy >14 thư mục: 14 core skills + utility)
ls ~/.claude/skills/ | wc -l
```

### 3c. MCP setup 🛠 (optional cho 👤)

MCP (Model Context Protocol) = connector cho external tools.

| MCP server | Dùng cho | Setup |
|---|---|---|
| **Playwright MCP** | vibe-test web · implement-automation locator | Add vào `~/.claude/settings.json`: `"playwright": {"command": "npx", "args": ["@modelcontextprotocol/server-playwright"]}` |
| **Appium MCP** | vibe-test mobile · implement-automation mobile locator | Cần Appium server `:4723` chạy local; add `"appium": {...}` trong settings.json |
| **Atlassian MCP** | log-bug push Jira · fetch-us | Auth qua claude.ai (one-time browser flow) |
| **Figma MCP** (optional) | analyze-requirements với UI mockup | Auth qua Figma desktop app |

Sau khi setup, restart Claude Code session và verify:
```bash
# Trong Claude Code
/mcp
# Phải thấy list MCP servers connected
```

### 3d. Credentials env file 🔵 (per-project)

**Nguyên tắc:** KHÔNG inline password vào commands. Mỗi project có 1 env file ngoài project folder.

```bash
# Pattern: ~/.<project-slug>/credentials.env
PROJECT_SLUG="<your-project-slug>"   # vd: my-app, dashboard-app, web-portal

mkdir -p ~/.$PROJECT_SLUG
chmod 700 ~/.$PROJECT_SLUG

cat > ~/.$PROJECT_SLUG/credentials.env <<EOF
# Test credentials — chmod 600, DO NOT commit, DO NOT echo
export TEST_USERNAME="your-test-account@example.com"
export TEST_PASSWORD="<get from team lead>"
# Add more env vars cần thiết per project
EOF
chmod 600 ~/.$PROJECT_SLUG/credentials.env
```

Mỗi shell session, source 1 lần:
```bash
source ~/.$PROJECT_SLUG/credentials.env
```

Trong Claude Code:
```
! source ~/.<project-slug>/credentials.env
```
(prefix `!` → env vars persist cho cả session)

> 📝 **Project-specific note:** Mỗi project có `Project_rule.md` ghi rõ env vars cần thiết. Đọc `Project_rule.md` của project đang làm để biết tên slug + danh sách env vars.

### 3e. First verify 🔵

```bash
cd /path/to/your/project
```

Trong Claude Code, gõ:
```
/health-check
```

Expected output: `🟢 PROJECT HEALTH: GOOD` hoặc `🟢 CLEAN` với ≤3 INFO findings. Nếu thấy CRITICAL → escalate team lead.

---

## 4. Skill Catalog (14 + 1 utility)

> Mỗi skill có file `~/.claude/skills/<name>/SKILL.md` chi tiết. Bảng dưới là 1-line summary.

| # | Skill | Pipeline pos | Role | 1-line purpose | Trigger natural language | External deps |
|---|---|---:|---|---|---|---|
| 1 | `init-project` | 1 | 🔵 | Scaffold folder structure + CLAUDE.md + PIPELINE.md + COMMANDS.md cho project mới | "init project", "QA project scaffold" | — |
| ⭐ 1.5 | `init-source-code` ⭐ NEW 2026-05-31 | 0.5 (standalone) | 🛠 (run lần đầu) / 🔵 (status check) | Scaffold `10_source-code/` với chosen archetype: `playwright-ts` (web) / `selenium-java` (web) / `appium-java` (mobile). Tự động generate build config + Page Object base + MEMORY §2 Tech Stack structured cho downstream stack-aware routing | "init source code", "tạo source code", "scaffold automation", "init playwright" | Python 3 + build tool tương ứng (npm/Maven) |
| 2 | `create-test-plan` | 2 | 👤 | Tạo Test Plan markdown: scope, approach, criteria, resources, schedule, risks | "tạo test plan", "test strategy" | — |
| 3 | `analyze-requirements` | 3 | 👤 | Phân tích URD/SRS/specs → scenario map + traceability + data catalog + risk. **NEW: verbatim quoting (3-field structure)** | "phân tích yêu cầu", "đọc SRS", "verbatim quote" | — |
| 4 | `generate-tc` | 4 | 👤 | Tạo TC Excel từ analyze-requirements. **NEW: 3 modes (standard/comprehensive/selective) với 8 test design techniques** | "viết test case", "tạo TC", "comprehensive mode" | — |
| 5 | `review-tc` | 5 | 👤 | Independent agent review TC quality (4 chiều: structural/coverage/content/consistency). Score 0-100, G1 gate | "review TC", "kiểm tra TC quality" | — |
| 6 | `scan-source-code` | 6 | 🛠 | Scan source code → extract Page Object classes, locators, test classes vào `10_source-code/MEMORY.md` | "scan source", "đọc source code" | Java + Maven (hoặc tương đương) |
| 7 | `vibe-test` | 7 | 🔵 | AI execute TC thật qua Playwright/Appium MCP — thay manual tester. Screenshot evidence + locator capture. Mặc định chạy TC **pending**; `--all` = chạy lại **toàn bộ** kể cả đã PASS | "vibe test", "test TC trên web/mobile" | MCP |
| 8 | `implement-automation` | 8 | 🛠 | Generate automation code (POM pattern) từ TC-MASTER. Uses Playwright/Appium MCP cho locator extraction (đọc vibe-locators nếu có) | "implement automation", "code selenium" | Java + MCP |
| 9 | `review-src-tc` | 9 | 🛠 | Compare TC-MASTER vs source code — phát hiện mismatch steps/expected/data | "review source vs TC", "verify implementation" | Code files |
| 10 | `execute-maintain` | 10 | 🛠 | Chạy test (`mvn test` hoặc tương đương), parse pass/fail, classify failures, recheck locator via Playwright MCP | "chạy test", "run automation" | Build tool + framework |
| 11 | `log-bug` | 11 | 🔵 | Tạo bug report markdown từ ASSERTION_FAIL · push/sync Jira via Atlassian MCP · track lifecycle | "log bug", "báo lỗi", "push jira" | Atlassian MCP (cho push) |
| 12 | `test-report` | 12 | 👤 | Stakeholder report: GO/NO-GO recommendation. 5 modes: SPRINT, RELEASE, ADHOC, CROSS-VERSION, TREND | "test report", "GO NO-GO", "summary report" | — |
| 13 | `health-check` | cross | 🔵 | Validate consistency giữa MEMORY files + TC-MASTER + bug-index + Pipeline Status. **mode-aware + 4 new checks** | "health check", "validate consistency" | — |
| 14 | `review-agent` | helper | 🛠 | Independent reviewer agent helper (dùng nội bộ bởi review-tc + review-src-tc — không gọi trực tiếp) | (called by review-tc/review-src-tc) | — |
| ★ | `fetch-us` | utility | 🔵 | Kéo User Story từ Jira → `00_input/<version>/<KEY>/` (Markdown + AC + attachments). KHÔNG nằm trong pipeline | "fetch user stories", "kéo US từ Jira" | Atlassian MCP |

### Cách gọi skill 🔵

3 cách tương đương:

| Cách | Ví dụ | Khi nào dùng |
|---|---|---|
| **Slash command** | `/generate-tc --module <module>` | Khi biết chính xác skill + flags |
| **Natural language tiếng Việt** | "Tạo TC cho module X, comprehensive mode" | Khi không nhớ syntax — Claude tự route |
| **Natural language English** | "Generate TC for module X with comprehensive mode" | Same — Claude routes by trigger keywords |

---

## 5. 8 Common Workflows (playbooks)

> Examples dưới dùng placeholder `v[X]` cho version, `<MODULE>` cho module name. Adapt theo project context.

### Workflow 1 🔵 — "Tôi mới có spec docs, bắt đầu từ đâu?"

**When:** Project mới, nhận spec docs từ BA.

**Steps:**
1. Đặt docs vào `00_input/v1.0/` (markdown/docx/pdf đều OK)
2. `/init-project` (nếu chưa có folder structure) → tạo CLAUDE.md, PIPELINE.md, COMMANDS.md, 12 folders
3. `/create-test-plan` → draft Test Plan trong `01_test-plans/`
4. `/analyze-requirements --init @00_input/v1.0/` → 5 deliverables vào `02_analyze-requirements/v1.0/` **(verbatim quoting mandatory default)**
5. `/generate-tc` (standard mode) HOẶC `/generate-tc --mode comprehensive` (full techniques) → TC Excel vào `03_test-cases/v1.0/fragments/`
6. `/generate-tc --consolidate` → gộp fragments vào TC-MASTER
7. `/review-tc` → quality score G1 (cần ≥70)

**Verify:** `/health-check --full` → mong CLEAN hoặc ≤3 INFO.

---

### Workflow 2 🔵 — "Version mới của app, phân tích delta"

**When:** App release version mới, có CHANGES vs version parent (NEW features + MODIFIED + có thể DEPRECATED).

**Steps:**
1. Tạo folder `00_input/v[NEW]/` và đặt docs mới
2. `/analyze-requirements --delta --version v[NEW] @00_input/v[NEW]/`
   - Skill compare với parent MEMORY → classify scenarios: NEW · MODIFIED · CARRIED · DEPRECATED
   - **MODIFIED** capture 2 Source Quotes (old + new) + diff trong Analyst Note
   - **CARRIED** chỉ reference parent (không re-quote)
3. `/generate-tc --version v[NEW]` → TC chỉ cho NEW + MODIFIED
4. `/review-tc --version v[NEW]`

**Verify:** `MASTER-MEMORY §3 Lifecycle` table có NEW/MODIFIED/CARRIED/DEPRECATED breakdown; `§4 Regression Scope` xác định CARRIED nào cần re-test.

---

### Workflow 3 👤 — "Review TC của QA member khác"

**When:** Lead muốn check chất lượng TC do junior write.

**Steps:**
1. `/review-tc --version v[X]` (FULL mode) → output `11_tc-review/review-report-functional-v[X].md` + `.xlsx`
2. Skill chạy `review-agent` (independent reviewer) → tránh self-review bias
3. Đọc findings theo severity: 🔴 Critical → 🟠 Major → 🟡 Minor → ⚪ Info
4. Quality Score 0-100. **G1 gate: ≥70 → APPROVED**.

**Verify:** Score column trong report Excel; module score breakdown.

---

### Workflow 4 🛠 — "Implement automation cho 1 module"

**When:** TC-MASTER đã APPROVED, cần code automation (POM pattern).

**Steps:**
1. `/scan-source-code` (FULL mode) → cập nhật `10_source-code/MEMORY.md` §1-§19
2. (Optional but recommended) `/vibe-test --module <MODULE>` → AI test TC thật, capture locators → `08_test-runs/vibe/VR-NNN-*/vibe-locators-latest.md`
3. `/implement-automation --module <MODULE>` → generate Page Object class + Test class, dùng locators từ vibe-test
4. Build verify (vd `mvn test-compile`) → confirm OK
5. `/review-src-tc --module <MODULE>` → verify code match TC

**Verify:** `10_source-code/MEMORY.md §13 Implementation Log` có entry cho mỗi TC; build SUCCESS.

---

### Workflow 5 🛠 — "Chạy regression suite + classify fail"

**When:** Sau khi implement xong, chạy test real run.

**Steps:**
1. `! source ~/.<project>/credentials.env` (1 lần per session)
2. `/execute-maintain --run-all` (HOẶC scope hẹp: `--run <TestClass>`)
3. Skill chạy test framework, parse output, classify failures:
   - `LOCATOR_STALE` → suggest `/implement-automation --update`
   - `ASSERTION_FAIL` → có thể app bug → `/log-bug`
   - `ENV_ERROR` → infra issue, không phải bug
4. Output: `10_source-code/MEMORY.md §15 Execution Log` + `§16 Fail Registry`

**Verify:** `§15` có row mới `RUN-XXX`; `§16` có row per failure với classification.

---

### Workflow 6 🔵 — "Found bug, log + push Jira"

**When:** Test run có `ASSERTION_FAIL`, confirmed là real app bug (không phải test code issue).

**Steps:**
1. `/log-bug` → skill đọc `§16 Fail Registry`, tạo `05_bug-reports/BUG-NNN-short-title.md`
2. Skill update `05_bug-reports/bug-index.md`
3. `/log-bug --push-jira <BUG-ID>` → push lên Jira via Atlassian MCP (config per-project trong `Project_rule.md` block `## Jira Integration`)
4. Khi fix verified: `/log-bug --close <BUG-ID>` → update status + sync Jira

**Verify:** Bug file có đủ fields (REQ ID, SC ID, TC ID, FAIL ID, Repro Steps, Expected vs Actual, Severity, Priority, Status); bug-index updated; Jira ticket có `jira_key` field link back.

---

### Workflow 7 🔵 — "Lead muốn release report GO/NO-GO"

**When:** Sprint kết thúc, lead cần stakeholder report.

**Steps:**
1. (Pre-req) Đảm bảo các skills upstream COMPLETED: review-tc, execute-maintain, log-bug
2. `/test-report --release --version v[X]` → 5-mode skill, RELEASE = GO/NO-GO
3. Skill đọc: MASTER-MEMORY + Version MEMORY + TC-MASTER + review report + execution log + bug-index + Test Plan exit criteria
4. Output: `09_reports/release/REPORT-RELEASE-v[X]-[date].md` + `.xlsx` (multi-sheet)
5. Verdict: 🟢 GO · 🟡 CONDITIONAL · 🔴 NO-GO based on Quality Gates

**Verify:** Report có Executive Summary section + Quality Gates table với pass/fail per gate.

---

### Workflow 8 🔵 — "Pipeline state có lỗi không?"

**When:** Bất kỳ lúc nào nghi ngờ data drift, sau mỗi skill major, trước test-report.

**Steps:**
1. `/health-check` (QUICK — đọc MEMORY only, <30s)
2. HOẶC `/health-check --full` (FULL — parse Excel, ~1-3 min, output file `09_reports/health-check/health-check-[date].md`)
3. Đọc findings:
   - 🔴 CRITICAL → fix trước khi chạy skill tiếp theo
   - 🟡 WARNING → nên fix sớm
   - 🔵 INFO → cosmetic / known issue
4. Fix routing trong report (Group A-F → skill nào fix)

**Verify:** Output có `Summary: N CRITICAL · N WARNING · N INFO`; cross-reference matrix table.

---

### Workflow 9 🛠 — "Scaffold Playwright TypeScript web project" (NEW 2026-05-31)

**When:** Project mới mà team chọn stack Playwright + TypeScript (modern web automation) thay vì legacy Selenium Java.

**Steps:**
1. `/init-project` (như usual — Q7 "Framework" trả lời "Playwright TypeScript")
2. `/init-source-code --archetype playwright-ts` → scaffold 15 files vào `10_source-code/`:
   - `package.json` (Playwright + TypeScript deps)
   - `tsconfig.json` (strict mode, ES2022)
   - `playwright.config.ts` (default workers, retries, reporters)
   - `src/pages/BasePage.ts` (abstract base)
   - `src/tests/fixtures.ts` + `setup.ts`
   - `src/utils/api-helpers.ts` + `data-helpers.ts`
   - `playwright-suites/{smoke,regression}.config.ts`
   - `MEMORY.md` với §2 Tech Stack structured (driver cho downstream routing)
3. Build verify:
   ```bash
   cd 10_source-code
   npm install                      # ~50 MB
   npx playwright install           # ~200 MB cho 3 browsers
   npx tsc --noEmit                 # TypeScript compile check
   ```
4. `/scan-source-code` → populate MEMORY §3-§19 với TS conventions (skill auto-detects Language=TypeScript)
5. Continue pipeline: `/analyze-requirements`, `/generate-tc`, `/review-tc`, etc. — downstream skills auto-route TS variants

**Verify:**
- `10_source-code/MEMORY.md §2` có structured Tech Stack table (Language=TypeScript)
- `/health-check` PASS, no CRITICAL
- `/init-source-code --status` returns `Language: TypeScript, Framework: Playwright`

**Alternative archetypes (cùng skill):**
- `--archetype selenium-java` (Web enterprise — manual scaffold, document existing GitLab clone pattern)
- `--archetype appium-java` (Mobile native — manual scaffold)
- `--list` xem available archetypes

---

## 6. Naming Conventions (framework defaults)

> Defaults dưới là framework baseline. Mỗi project có thể override trong `Project_rule.md §3`.

### 🔵 ID patterns

| Type | Pattern | Example |
|---|---|---|
| Document ID | `DOC-v[VERSION]-[NN]` | `DOC-v1.0-01` |
| Requirement ID | `REQ-[MODULE]-[NNN]` | `REQ-LOGIN-001` |
| Scenario ID | `SC-[MODULE]-[NNN]` | `SC-LOGIN-001` |
| Testcase ID | `TC-[MODULE]-[NNN]-[short-title]` | `TC-LOGIN-001-happy-path` |
| Bug ID | `BUG-[NNN]-[short-title]` | `BUG-001-login-redirect-fail` |
| Test run ID | `TR-[SPRINT]-[YYYY-MM-DD]` / `VTR-[SX]-[NNN]-[YYYY-MM-DD]` | `TR-S1-2026-01-15` |
| TC-MASTER file | `TC-MASTER-v[VERSION].xlsx` | `TC-MASTER-v1.0.xlsx` |
| Report file | `REPORT-[MODE]-[CTX]-[YYYY-MM-DD].{md,xlsx}` | `REPORT-RELEASE-Sprint1-2026-01-20.md` |

### 🔵 Status / Priority / Severity values (fixed enum)

| Field | Allowed values |
|---|---|
| **TC Status** | `Pass` · `Fail` · `Blocked` · `Skipped` · `Not Run` |
| **Bug Status** | `Open` · `In Progress` · `Fixed` · `Verified Fixed` · `Closed` · `Closed (False Positive)` · `Won't Fix` |
| **Priority** | `P1` (critical) · `P2` (important) · `P3` (nice-to-have) |
| **Severity** | `Critical` · `High` · `Medium` · `Low` |
| **Lifecycle** (scenarios) | `NEW` · `MODIFIED` · `CARRIED` · `DEPRECATED` |
| **Pipeline Status (§8)** | `NOT_STARTED` · `IN_PROGRESS` · `PARTIAL` · `COMPLETED` · `FAILED` |

### 🔵 Language rules (framework default)

- **Nội dung narrative:** Configurable per project. Project_rule.md §3 ghi rõ ngôn ngữ default (vd tiếng Việt, English, hoặc bilingual).
- **Tech terms:** Luôn giữ English (REST, JSON, OAuth, SSO, Page Object, accessibility id, MCP, DataProvider, etc.)
- **Code blocks:** English (any language)
- **Status/Priority/Severity enums:** English (fixed values như bảng trên)

---

## 7. NEW Features 2026-05-29

### 7a. 🔵 Verbatim Quoting trong `analyze-requirements`

**Vấn đề trước đây:** Skill paraphrase câu từ tài liệu → ID mapping đúng nhưng khi reviewer muốn verify, phải đọc lại full doc gốc.

**Giải pháp:** Mỗi REQ + SC + Clarification trong output có 3 fields tách biệt:

```markdown
### REQ-LOGIN-001 — User authentication

**Source Quote:**
> "User must authenticate via corporate SSO with email domain whitelist."

**Source Location:** `DOC-v1.0-01 §6.1.2 "Authentication Flow" · paragraph 2 · page 14`

**Analyst Note (paraphrase):** Login qua SSO với email domain whitelist.
Implicit: callback URL phải được register sẵn ở IAM provider.
```

**Tại sao quan trọng:**
- Reviewer/QA-lead verify analyze result vs doc gốc < 30s, không phải đọc full tài liệu.
- Khi spec update → diff dễ vì biết đoạn nào doc tương ứng REQ nào.
- Skill `generate-tc` rubric scan keywords trên Source Quote (verbatim) → reliable hơn paraphrase.

**Default:** Mandatory ON. **Opt-out:** `--no-quote` flag (legacy migration only).

**Edge cases handled:**
- Multi-language docs → quote nguyên gốc + bản dịch trong Analyst Note (KHÔNG quote bản dịch)
- Implicit requirements → đánh dấu `Source Quote: *(Implicit — no direct quote)*` + giải thích derivation
- Long quotes (>500 chars) → sidecar `quotes/REQ-XXX-NNN.md`
- Multiple sources → number `Source Quote #1`, `#2`

**Full reference:** `~/.claude/skills/analyze-requirements/references/quoting-guide.md`

---

### 7b. 🔵 Test Design Techniques (`generate-tc` comprehensive mode)

**Vấn đề trước đây:** `/generate-tc` map 1-1 SC→TC. Output chỉ có Functional/UI/Integration categories — 0 negative + 0 boundary + 0 systematic edge cases. Negative-test-class bugs lọt qua test cycle.

**Giải pháp:** 3 modes (default backward-compat):

| Mode | Command | Behavior |
|---|---|---|
| **Standard (default)** | `/generate-tc` | 1-1 SC→TC. **No regression** — output identical to pre-2026-05-29. |
| **Comprehensive** | `/generate-tc --mode comprehensive` | Per SC chạy rubric → apply tất cả 8 techniques applicable. Expand TC count 3-12×. Output thêm sheet `Coverage Matrix`. |
| **Selective** | `/generate-tc --techniques EP,BVA,EG` | Apply chỉ techniques user list. Useful incremental adoption. |

**8 ISTQB-aligned techniques (B1-B8):**

| ID | Name | WHEN apply | Generic example |
|---|---|---|---|
| **B1** | Equivalence Partitioning (EP) | Input có discrete domain (enum/role/category) | "role ∈ {admin/editor/viewer/guest}" → 4 TC |
| **B2** | Boundary Value Analysis (BVA) | Numeric range / date / length | "password 8-32 chars" → 6 TC (min-1/min/min+1/max-1/max/max+1) |
| **B3** | Decision Table (DT) | ≥2 binary conditions → outputs | "logged_in × has_permission × resource_exists" → 4 rules |
| **B4** | State Transition (ST) | Explicit state machine | "Order: draft → submitted → approved → shipped" |
| **B5** | Pairwise (PW) | ≥3 multiplicative parameters | "OS × Browser × Lang × Resolution" → AllPairs ~12 TC |
| **B6** | Error Guessing (EG) | Any user-input field | 10-pattern checklist (null/empty/unicode/SQL/XSS/...) |
| **B7** | CRUD Matrix | Persistent entity ops | Entity × {Create/Read/Update/Delete/List/Search/Bulk} |
| **B8** | Cause-Effect Graph (CEG) | Complex multi-output (DT escalation >16 rules) | Bank loan approval với 4 causes + 2 effects |

**Expected expansion:** 1 baseline TC → 3-12 derived TCs depending on technique mix. Mock login form (2 input fields, no state) typically expand 1 → ~25-30 TCs với EP + BVA + EG.

**Output enrichment khi mode active:**
- Excel sheet `Coverage Matrix` thêm vào TC-MASTER (rows=SC, cols=B1-B8, cell=✅/❌/N/A + count)
- TC Notes column ghi `Technique: <tag>` per derived TC (vd `Technique: BVA-min-1`)
- Baseline TC giữ Notes `Baseline (standard mapping)`

**Full references:**
- `~/.claude/skills/generate-tc/references/techniques.md` — 8 technique definitions + procedures + anti-patterns
- `~/.claude/skills/generate-tc/references/technique-rubric.md` — auto-detection per scenario

---

## 8. Folder Layout (per-project structure)

Mỗi project follow standard structure (set up bởi `/init-project`):

```
<project-root>/
├── CLAUDE.md                                   👤 Project context, version info, conventions
├── PIPELINE.md                                 🔵 Skill manifest + §8 Pipeline Status (live)
├── COMMANDS.md                                 🔵 Command cheat sheet (copy-paste friendly)
├── README.md                                   🔵 Basic project overview
│
├── 00_input/v[X]/                              👤 Tài liệu spec gốc per version
│   └── shared/                                  (shared across versions)
│
├── 01_test-plans/                              👤 TP-[type]-v[X].md
│
├── 02_analyze-requirements/                    👤 OWNED BY: analyze-requirements skill
│   ├── MASTER-MEMORY.md                         🔵 Cross-version registry + §8 Pipeline Status
│   ├── Project_rule.md                          🔵 Naming + workflow + custom rules (per-project)
│   └── v[X]/
│       ├── MEMORY.md                            (per-version: §0-§9, including §4.1 Source Detail)
│       ├── requirement_traceability.md
│       ├── test_scenario_map.md                 (with Source Detail blocks per scenario)
│       ├── test_data_catalog.md
│       ├── risk_assessment.md
│       └── quotes/                              (sidecar cho long verbatim quotes)
│
├── 03_test-cases/                              👤 OWNED BY: generate-tc skill
│   ├── TC-MASTER-LATEST.xlsx                    (copy of active version)
│   └── v[X]/
│       ├── TC-MASTER-v[X].xlsx                  (Overview + ALL + module sheets + Coverage Matrix*)
│       ├── CHANGELOG.md
│       └── fragments/                           (per-module Excel files)
│
├── 04_test-data/                               🔵 Test data resources (formulas, fixtures, etc.)
│
├── 05_bug-reports/                             🔵 OWNED BY: log-bug skill
│   ├── bug-index.md                             (master index)
│   └── BUG-[NNN]-*.md                           (1 file per bug)
│
├── 06_checklists/                              🔵 Smoke + release checklists
│
├── 07_environments/                            🛠 Env config (DEV/STG/PROD URLs, etc.)
│
├── 08_test-runs/                               🔵 OWNED BY: execute-maintain (TR), vibe-test (VR/VTR)
│   ├── v[X]/                                    (per-version run logs)
│   ├── vibe/VR-NNN-*/                           (vibe-test runs + screenshots + locators)
│   └── README.md                                (inventory + naming)
│
├── 09_reports/                                 👤 OWNED BY: test-report, health-check
│   ├── release/REPORT-RELEASE-*.{md,xlsx}
│   ├── adhoc/REPORT-ADHOC-*.{md,xlsx}
│   ├── executive/REPORT-EXECUTIVE-*.{md,html,xlsx}
│   ├── health-check/health-check-[date].md
│   └── README.md
│
├── 10_source-code/                             🛠 OWNED BY: scan-source-code, implement-automation
│   ├── MEMORY.md                                (§1-§19, §15 Execution Log, §16 Fail Registry, §17 SRC-TC Review)
│   ├── pom.xml (Maven) hoặc tương đương         (build config)
│   ├── src/main/                                (Page Object classes / production code)
│   ├── src/test/                                (Test classes)
│   └── testSuites/ (TestNG) hoặc tương đương    (test suite definitions)
│
└── 11_tc-review/                               👤 OWNED BY: review-tc, review-src-tc
    ├── review-report-functional-v[X].{md,xlsx}
    └── src-tc-review-v[X].md
```

`*` Coverage Matrix sheet chỉ tồn tại khi generate-tc comprehensive/selective mode active.

---

## 9. Quality Gates G1-G6 (framework baseline)

> Framework có **6 baseline gates** (G1-G6). Mỗi project có thể extend thêm gates (G7+) trong Test Plan tùy domain (API cross-validation, infrastructure smoke, security scan, etc.).

| Gate | Criteria | Threshold | Skill responsible |
|---|---|---|---|
| **G1** | TC Review score | ≥ 70 | review-tc |
| **G2** | P1 TC coverage executed | 100% | execute-maintain → test-report |
| **G3** | Overall pass rate (effective) | ≥ 90% | test-report |
| **G4** | P1 bugs open | = 0 | log-bug → test-report |
| **G5** | Bug fix rate (when fixes exist) | ≥ 80% | test-report |
| **G6** | Summary report created và reviewed | Yes | test-report |

**Decision logic (test-report):**
- Tất cả gates PASS → 🟢 **GO**
- 1+ gate FAIL (but non-critical) → 🟡 **CONDITIONAL GO**
- Multiple gates FAIL hoặc P1 bugs blocker → 🔴 **NO-GO**

**Project extensions:** Project_rule.md có thể thêm custom rules (vd mandatory UI ↔ API cross-validation cho data-heavy apps) và bonus gates G7+ (vd API schema validation, infrastructure smoke tests, security scan, accessibility audit). Xem Test Plan §4 Exit Criteria của project.

---

## 10. Golden Rules & Pitfalls

> Framework-level rules. Project-specific rules ghi trong `Project_rule.md §9 Active Memory Rules` (vd platform-specific UI quirks, build environment constraints, custom field conventions, domain-specific data formats, etc.).

### 🔵 Top 10 framework rules

1. **KHÔNG manually edit MEMORY files.** MASTER-MEMORY, Version MEMORY, Source MEMORY — skills tự update. Nếu edit tay, lần run kế sẽ overwrite.

2. **KHÔNG inline password vào Bash command.** Pattern cấm: `PASSWORD="actual" mvn test`. Pattern OK: `source ~/.<project>/credentials.env && mvn test`. Báo cáo tracking sẽ flag password literal là sensitive info leak.

3. **KHÔNG skip Source Quote verification trên new analyses.** Mọi REQ/SC mới (post-2026-05-29) phải có Source Quote hoặc đánh dấu `*(Implicit — no direct quote)*` + giải thích derivation.

4. **TC interactive flow phải cover OPEN + PICK + STATE-CHANGE + CONSISTENCY.** Với picker/dropdown/modal: luôn add 2 layers — (1) tap mở dialog · (2) chọn option + verify state change + cross-surface label match. Thiếu layer 2 → cross-surface inconsistency bugs lọt qua.

5. **KHÔNG re-quote CARRIED scenarios trong delta analyze.** CARRIED reference parent version: `Source Quote: see v[parent] REQ-XXX-NNN`. Re-quote = duplicate maintenance.

6. **Push Jira → `bug.md` là source of truth.** Bug lifecycle (Open → Fixed → Closed) maintain trong `.md` file; `--push-jira` sync lên Jira. KHÔNG sửa Jira manual rồi sync ngược về `.md`.

7. **Mỗi REQ MUST có Source Quote hoặc Implicit marker.** No silent assumptions about spec text.

8. **KHÔNG skip review-tc khi G1 chưa pass.** Quality Gate G1 (score ≥70) là prerequisite cho downstream (implement-automation, execute-maintain). Skip = downstream may produce broken artifacts.

9. **KHÔNG break pipeline order.** Skill downstream cần upstream `≥ PARTIAL`. health-check raise CRITICAL A-03 nếu detect. Exception: documented carry-over (vd scan-source-code baseline từ version trước).

10. **Mode flags là opt-in default.** No-flag invocation = standard behavior (backward-compat). Comprehensive/selective mode KHÔNG auto-trigger — user phải explicit choose. Existing projects KHÔNG bị disrupted khi toolkit upgrade.

---

## 11. FAQ / Troubleshooting

### 🔵 Skill báo lỗi `[MISSING]` file

Skill check prerequisites trong PIPELINE.md §3. Nếu thấy `[MISSING]`, chạy skill upstream trước:
- "MEMORY.md missing" → `/analyze-requirements --init` trước
- "TC-MASTER missing" → `/generate-tc --consolidate` trước
- "Source MEMORY missing" → `/scan-source-code` trước

### 🛠 Build/test fail với env var không set

```bash
source ~/.<project>/credentials.env
# Verify (KHÔNG echo password!)
test -n "$TEST_PASSWORD" && echo "ENV_OK" || echo "ENV_MISSING"
# Then run build/test
```

### 🛠 Playwright/Appium MCP disconnected

```bash
# Trong Claude Code
/mcp
# Nếu thấy disconnected:
# 1. Restart Claude Code session
# 2. Re-auth: gõ "authenticate Atlassian" hoặc tương tự
# 3. Check ~/.claude/settings.json có config MCP đúng
```

### 🔵 Health-check báo WARNING `[A-05] version drift`

Project doc (vd CLAUDE.md) `Current version` field stale so với MASTER-MEMORY active version. Fix:
1. Đọc `MASTER-MEMORY.md §1 Version Registry` lấy version đúng
2. Sửa project doc `Current version` field

### 🔵 Comprehensive mode generate quá nhiều TC

`/generate-tc --mode comprehensive` có thể tạo 3-12× baseline. Nếu quá nhiều:
- Dùng selective mode: `/generate-tc --techniques BVA,EG` (chỉ 2 techniques)
- Hoặc filter scope: `--module <MODULE> --priority P1`

### 🛠 Locator stale > 30 ngày

Health-check raise `D-04 WARNING`. Re-capture:
```bash
/vibe-test --module <MODULE>      # chỉ TC pending của module
/vibe-test --all                  # chạy lại TOÀN BỘ TC (kể cả đã PASS) — refresh hết locator
# Output: 08_test-runs/vibe/VR-NNN-*/vibe-locators-latest.md
# implement-automation tự đọc file này
```

### 🛠 review-src-tc báo "orphan method"

Khi comprehensive mode active + parameterized via `@DataProvider`, 1 method covers N derived TCs. KHÔNG phải orphan. Update Source MEMORY §13:
```
| Date | SC | TC range | Test method | Pattern |
| ... | SC-XXX-001 | TC-XXX-014..020 | testFooBoundary | DataProvider BVA |
```

### 🔵 Bug đã fix nhưng status vẫn `Open`

```bash
/log-bug --close BUG-NNN
# Skill update bug.md + bug-index.md + push Jira (nếu config)
```

### 🔵 "Tôi không biết active version đang là gì?"

```bash
grep -A2 "Active version" 02_analyze-requirements/MASTER-MEMORY.md
# HOẶC
/health-check  # output có "Active version: vX.Y.Z"
```

### 🛠 Test method count < TC count (comprehensive mode)

Expected nếu DataProvider parameterized — 1 method với N data rows cover N derived TCs. Document trong Source MEMORY §13 với TC ID range. Health-check D-01 mode-aware sẽ tolerate.

### 🔵 Skill prompt hỏi "có muốn apply verbatim-quoting"

Say **YES** (default ON). NO chỉ dùng legacy migration cho project cũ — sẽ mất text-level traceability.

### 🔵 Bug-index không sync với Jira

Check:
1. Atlassian MCP có authenticated chưa (`/mcp` xem status)
2. `Project_rule.md` có block `## Jira Integration` với `site:` + `project:` + custom fields config

### 🔵 Không hiểu Source Location format

Format chuẩn: `<DOC-ID> §<section> · "<heading>" · <element-ref> · page <N>`. Nếu doc không có heading rõ, dùng fallback hierarchy:
1. `§heading` (nếu có)
2. `page N · paragraph M`
3. `line N`
4. `text-anchor "<first-5-words>..."` (last resort)

Full rules: `~/.claude/skills/analyze-requirements/references/quoting-guide.md` §"Field 2: Source Location".

### 🔵 Skill chạy quá lâu / treo

Typical execution times:
- Health-check QUICK < 30s · FULL 1-3 min
- generate-tc 1 module ~30-60s · all modules ~3-5 min
- execute-maintain Smoke ~5-10 min · Full ~30-60 min
- vibe-test 10-20 TCs ~5-10 min

Nếu treo > 2x expected: check Appium/Playwright server running, MCP connected, network ok.

---

## 12. Glossary + Reference Links

### Glossary 🔵

| Term | Meaning |
|---|---|
| **SC** | Scenario — Given/When/Then test logic unit |
| **TC** | Test Case — concrete test với Steps + Expected Result |
| **REQ** | Requirement — functional/non-functional spec rule |
| **DOC** | Source document (URD/SRS/spec/user story) |
| **MASTER-MEMORY** | Cross-version registry trong `02_analyze-requirements/MASTER-MEMORY.md` |
| **Version MEMORY** | Per-version analyze output trong `02_analyze-requirements/v[X]/MEMORY.md` |
| **Source MEMORY** | Code-side tracking trong `10_source-code/MEMORY.md` |
| **Pipeline §8** | Live skill status table trong MASTER-MEMORY (IN_PROGRESS/COMPLETED/FAILED) |
| **MCP** | Model Context Protocol — connector cho external tools (Playwright/Appium/Atlassian/Figma) |
| **POM** | Page Object Model — Selenium pattern, 1 class per UI page |
| **DataProvider** | TestNG annotation cho parameterized test (1:N TC→method mapping) |
| **Verbatim Quote** | Câu trích nguyên gốc từ doc, blockquote markdown (NEW 2026-05-29) |
| **Coverage Matrix** | Excel sheet trong TC-MASTER hiển thị technique × scenario heatmap (NEW 2026-05-29) |
| **Lifecycle** | Scenario state: NEW · MODIFIED · CARRIED · DEPRECATED |
| **G1-G6** | Framework Quality Gates — pass criteria cho release decision |
| **VR** | Vibe Run (AI manual test session) — `08_test-runs/vibe/VR-NNN-*/` |
| **TR** | Test Run (automation execution) — `08_test-runs/v[X]/TR-*.md` |
| **VTR** | Vibe Test Run (older naming, equivalent VR) |

### Reference Links 🔵

**Framework-level docs (`~/.claude/skills/`):**
- `~/.claude/skills/ONBOARDING.md` (this file)
- Per skill: `~/.claude/skills/<name>/SKILL.md` — full mode/edge case detail
- New features 2026-05-29:
  - `~/.claude/skills/analyze-requirements/references/quoting-guide.md` — Full verbatim quoting rules
  - `~/.claude/skills/generate-tc/references/techniques.md` — 8 ISTQB test design techniques
  - `~/.claude/skills/generate-tc/references/technique-rubric.md` — Auto-detection per scenario
  - `~/.claude/skills/generate-tc/assets/coverage-matrix-template.md` — Excel sheet schema

**Project-level docs (per project, generated bởi `/init-project`):**
- `<project>/CLAUDE.md` — Project context + version history + project-specific customizations
- `<project>/PIPELINE.md` — Skill registry + §6 Mode Quick-Reference + §6.1 NEW features
- `<project>/COMMANDS.md` — Command cheat sheet với syntax examples
- `<project>/README.md` — Basic project overview
- `<project>/02_analyze-requirements/MASTER-MEMORY.md` — Cross-version registry + §8 Pipeline Status (live)
- `<project>/02_analyze-requirements/Project_rule.md` — Naming conventions overrides + Quality Gates extensions + Active Memory Rules
- `<project>/08_test-runs/README.md` — Test run inventory + naming
- `<project>/09_reports/README.md` — Reports grouped by type

---

## Maintenance

**Toolkit version:** qc-claude-v1 · v1.0 (released 2026-06-05)
**Doc scope:** Framework-level only — KHÔNG chứa project specifics. Mỗi project có docs riêng.
**Update triggers:**
- New skill added vào toolkit → update Section 4
- Major skill mode change → update Section 7 + workflow examples
- Framework convention thay đổi → update Section 6
- Pipeline structure thay đổi → update Section 2

**Backward compatibility:** Skills evolve qua versions; default behavior luôn backward-compat — existing projects KHÔNG bị disrupted khi toolkit upgrade. Opt-in flags (`--mode comprehensive`, `--techniques`, `--no-quote`) cho new features.

---

> 🎯 **Đọc xong ONBOARDING.md → bạn đã grasp full picture framework.** Đi vào project cụ thể, đọc thêm `CLAUDE.md` + `Project_rule.md` của project đó để biết customizations.
>
> Daily reference: Section 4 (catalog) + Section 5 (workflows) + Section 11 (FAQ). Khi blocked → ask team lead hoặc chạy `/health-check` trước.
