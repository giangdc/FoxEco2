# Test Report — Mode RELEASE (GO/NO-GO)

> `/test-report --release --version v2.0`

## Sources (đọc tất cả, filter version)

| Source | Path | Data |
|--------|------|------|
| Project info | CLAUDE.md | Tên, env, team |
| Project rules | Project_rule.md §8 | Report rules, quality gates |
| Version registry | MASTER-MEMORY | Versions, regression scope |
| Scenario index | Version MEMORY §3-§4 | Scenarios, lifecycle |
| TC-MASTER | `03_test-cases/v[X]/TC-MASTER-v[X].xlsx` (alias file ISC — 42 cột, 1 sheet/module + workbook-level sheets) | Nguồn gốc dữ liệu — nhưng **ưu tiên đọc qua 3 sheet pre-computed bên dưới thay vì tự parse lại từng row Test Cases** |
| **Dashboard** ★ | TC-MASTER sheet `Dashboard` | **(2026-07-21)** Per-module: Tổng TC/Pass/Fail/Block/N/A/Coverage%/Pass%, Priority breakdown (High/Medium/Low), Group breakdown, Auto/Vibe/Reviewed counts, per-round (R1-R5) breakdown — TẤT CẢ đã có sẵn công thức, không tự đếm lại row Excel. |
| **RTM** ★ | TC-MASTER sheet `RTM` | **(2026-07-21)** Requirement coverage: Req ID · Số TC · Đã chạy · Pass · Fail · % phủ · Trạng thái (kể cả "Chưa có TC (gap)") — dùng cho §3 Test Coverage + gap analysis, thay vì tự tính từ Version MEMORY §4. |
| **Report Test** ★ | TC-MASTER sheet `Report Test` | **(2026-07-21)** KPI đã tính sẵn: Tổng số Bug, Critical+Major, %Bug đã Fixed, %Coverage, %Automation, %Bug do AI phát hiện, %TC Pass, Critical/Major còn Open + breakdown Bug Status theo Platform/Function. Đọc trực tiếp thay vì tự tổng hợp từ bug-index.md. |
| **Bug Data** | TC-MASTER sheet `Bug Data` | Khối QC phân tích (Severity mã hoá 20/10/5/2=Critical/Major/Medium/Low, Defect, Effect, Round found/closed) — dùng cho §5 Defect Summary breakdown. Nguồn qua `log-bug/references/sync-excel.md`. |
| **Coverage Matrix** | TC-MASTER `.xlsx` sheet `Coverage Matrix` | Technique × scenario heatmap — chỉ tồn tại khi MEMORY §9 Mode = `comprehensive`/`selective`. Schema: 13 cols (SC ID · Title · Source Hint · B1-B8 · Total · Coverage %). Skip nếu sheet không tồn tại. |
| **MEMORY §9 TC Gen Log** | `02_analyze-requirements/v[X]/MEMORY.md` §9 | Mode + Techniques cols — driver cho §8 Test Design Technique Coverage. |
| TC review | `11_tc-review/review-report-v[X].md` | Review score (G1) |
| SRC-TC review | `11_tc-review/src-tc-review-v[X].md` | Match score (G7) |
| Vibe-test | `08_test-runs/vibe/VR-*/vibe-report.md` | Vibe results (bổ sung — nguồn chính giờ là cột Vibe-test/Kết quả trong TC-MASTER, xem `vibe-test/references/execute.md` Step 7) |
| Execution log | Source MEMORY §15 | Runs (filter version) |
| Fail registry | Source MEMORY §16 | Failures (filter version) |
| Bug reports | `05_bug-reports/bug-index.md` | Bugs (filter version) — cross-check với sheet `Bug Data`, nếu lệch thì Bug Data (mirror mới nhất từ log-bug) thắng cho số liệu report, bug-index vẫn là nguồn lifecycle |
| Risk assessment | `02_.../v[X]/risk_assessment.md` | Risk scores |
| Test plan | `01_test-plans/TP-*-v[X].md` | Exit criteria = Quality Gates |

## Workflow

### Step 1: Read all sources (version-filtered)

### Step 2: Calculate metrics

| Metric | Formula / Nguồn |
|--------|---------|
| Test coverage | **Đọc `Dashboard` cột "Coverage %"** (per module, đã có formula) — KHÔNG tự đếm row. Tổng hợp toàn version = tổng `Executed` / tổng `Tổng TC` trên mọi row Dashboard. |
| Automation coverage | **Đọc `Dashboard` cột "Auto"** / cột "Tổng TC" (Auto đã COUNTIF cột Automated=Yes theo formula). |
| Pass rate | **Đọc `Dashboard` cột "Pass %"** (per module) hoặc tổng `Pass` / (`Pass`+`Fail`) cộng dồn mọi row Dashboard. |
| Defect density | **Đọc `Report Test` KPI "Tổng số Bug"** / tổng `Executed` (Dashboard) — thay vì tự đếm bug-index.md. |
| Bug fix rate | **Đọc `Report Test` KPI "% Bug đã Fixed"** trực tiếp. |
| Blocked rate | Cộng dồn cột "Block" trên mọi row `Dashboard` / tổng `Tổng TC`. |
| NEW scenario coverage | TCs cho NEW / total NEW — vẫn cần Version MEMORY §4 (lifecycle NEW/CARRIED/MODIFIED không có trong Excel), map NEW scenario → Req ID → tra `RTM` cột "Số TC"/"Đã chạy". |
| MODIFIED scenario coverage | Tương tự NEW, filter MODIFIED trong Version MEMORY §4. |
| Regression coverage | CARRIED TCs executed / regression scope — CARRIED TC nhận diện qua Remark chứa `Carried từ v[X]` (không còn cột Lifecycle riêng), đối chiếu MASTER-MEMORY §4 Regression Scope. |
| Requirement coverage gap | **Đọc thẳng `RTM` cột "Trạng thái" = "Chưa có TC (gap)"** — liệt kê Req ID chưa có TC nào, không cần tự suy luận. |
| **TC generation mode** | Read MEMORY §9 Mode col: `standard` / `comprehensive` / `selective`. Display trong Executive Summary. |
| **TC expansion factor** | Total TCs (từ `Dashboard` tổng cột "Tổng TC") / baseline scenario count. = 1.0 cho standard mode, 3-12 cho comprehensive. Indicates test intensity. |
| **Technique coverage** | Read Coverage Matrix sheet (nếu tồn tại): per-technique TC count + % scenarios applied. Format: "B1 EP: 8 TCs across 2 scenarios" etc. |
| **% Bug do AI phát hiện** | **Đọc `Report Test` KPI trực tiếp** — không tự suy luận từ Origin cột J của TC (AI/QC), vì bug do AI "phát hiện" ≠ TC do AI "sinh". |

### Step 3: Evaluate Quality Gates

| # | Gate | Criteria | Actual | Status |
|---|------|----------|--------|--------|
| G1 | TC Review | Score ≥ 70 | [score] | ✅/❌ |
| G2 | High (P1) Priority Pass | 100% | [%] | ✅/❌ — filter TC Priority (Dashboard cột "High") = `High` |
| G3 | Overall Pass | ≥ 90% | [%] | ✅/❌ — `Report Test` KPI "% TC Pass" |
| G4 | P1 Bugs | 0 open | [count] | ✅/❌ — bug `priority` field (P1-3, không đổi), không nhầm với Severity |
| G5 | Bug Fix Rate | ≥ 80% | [%] | ✅/❌ — `Report Test` KPI "% Bug đã Fixed" |
| G6 | Blocked | ≤ 0 | [count] | ✅/❌ |
| G7 | SRC-TC Match | Score ≥ 70 | [score] | ✅/❌ |

### Step 4: GO/NO-GO recommendation
All gates ✅ → **GO.** Any gate ❌ → **NO-GO** + list blockers.

### Step 5: Generate report

**Files:**
- `09_reports/REPORT-RELEASE-v[X]-[date].md`
- `09_reports/REPORT-RELEASE-v[X]-[date].xlsx` (optional)

```markdown
# Release Report — v[X] — [date]

## 1. Executive Summary
[2-3 câu cho non-technical reader]
**Recommendation: [GO / CONDITIONAL GO / NO-GO]**

## 2. Quality Gates
(table từ Step 3)

## 3. Test Coverage
### Scenario Lifecycle
| Lifecycle | Count | With TC | Executed | Pass |
|-----------|-------|---------|----------|------|
| NEW | | | | |
| MODIFIED | | | | |
| CARRIED | | | | |

### By Module
(module × TC × pass/fail matrix)

## 4. Execution Results
(latest run stats, failure breakdown)

## 5. Defect Summary
(by severity [Critical/Major/Medium/Low — theo Bug Data sheet, KHÔNG còn nhãn "High"], by module/Function, by Platform [Web/Mobile], by status, open bugs list — nguồn: `Report Test` §1a/1b + `Bug Data` sheet)

## 6. Code Implementation Quality
| Metric | Value |
|--------|-------|
| SRC-TC score | [N]/100 |
| Step coverage | [%] |
| Assert coverage | [%] |

## 7. Vibe Test Results
(summary từ vibe-report: passed/blocked/failed TCs)

## 8. Test Design Technique Coverage (chỉ khi comprehensive/selective mode)

**TC generation mode:** [standard / comprehensive / selective]
**TC expansion factor:** [N]× (baseline N TCs → expanded M TCs)

| Technique | TCs generated | Scenarios applied | % scenarios |
|---|---:|---:|---:|
| B1 EP (Equivalence Partitioning) | [N] | [n] | [%] |
| B2 BVA (Boundary Value Analysis) | [N] | [n] | [%] |
| B3 DT (Decision Table) | [N] | [n] | [%] |
| B4 ST (State Transition) | [N] | [n] | [%] |
| B5 PW (Pairwise) | [N] | [n] | [%] |
| B6 EG (Error Guessing) | [N] | [n] | [%] |
| B7 CRUD Matrix | [N] | [n] | [%] |
| B8 CEG (Cause-Effect Graph) | [N] | [n] | [%] |

**Implication:** [comprehensive mode catches edge cases that standard mode misses. E.g., BUG-XXX class issues prevented bằng B1 EP partition negatives.]

Source: TC-MASTER sheet `Coverage Matrix`. Skip nếu mode = standard (sheet không tồn tại).

## 9. Risk Assessment
(from risk_assessment.md)

## 10. Recommendations
- [ ] Release / Release with known issues / Block release
```

### Step 6: Update
- `08_test-runs/TR-v[X]-[date].md` (test run log)
- CLAUDE.md append
- §8 = COMPLETED
