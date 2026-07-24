# Requirement Traceability — v[VERSION]

> Tạo bởi: analyze-requirements. Ma trận truy vết REQ ↔ DOC ↔ Scenario ↔ Clarification.
> Text-level traceability: Source Quote per REQ ở `MEMORY.md §4.1`, per SC ở `test_scenario_map.md`.
>
> **Structure-lock:** giữ nguyên header cột + section dưới đây. KHÔNG tự thêm/bớt/đổi tên cột.

## 1. Traceability Matrix (REQ → DOC → SC)

> 1 bảng con per module. 1 dòng / REQ (KHÔNG gộp nhiều REQ vào 1 dòng).

### Module [MODULE] — DOC-v[VERSION]-[NN]
| REQ ID | Maps (Ref DOC) | DOC §section | Scenarios | Clarification |
|--------|----------------|--------------|-----------|---------------|
| REQ-[MODULE]-[NNN] | <ref theo ký hiệu DOC: vd FR-[NNN]/VR-[NNN], AC-[NNN], UC-[NNN], US key> | §[N] | SC-[MODULE]-[NNN] | C-[MODULE]-[N] hoặc — |

(lặp bảng cho mỗi module)

> **Cột Maps (Ref DOC):** dùng ký hiệu theo `req_notation` trong block `## DOC Notation` của `Project_rule.md` (sinh bởi `/init-project` Q11; vd FCP dùng FR/VR; dự án khác có thể là AC, UC, US key Jira...). `req_notation: none` hoặc DOC **không đánh số** → để `—` và dựa vào cột `DOC §section`. **KHÔNG tự bịa số FR/VR** khi doc không có.

## 2. Coverage Summary
- **Scenario có REQ + DOC source:** [n]/[N] (100%).
- **REQ có ≥1 scenario:** ~[%] (các REQ core functional/validation/permission).
- **REQ chưa có scenario (gap có chủ đích):** [list REQ-ID] — Phase-2/NFR/display-rule/duplicate-multi-select; ghi rõ để generate-tc xem xét.
- **(Mốc cập nhật):** ghi delta khi bổ sung REQ/SC/TC (vd sau sweep/UPDATE).

## 3. Clarifications — Source Quote (ambiguous text)

> Trích nguyên văn đoạn mơ hồ per clarification (quoting-guide EC6). Tóm tắt + status: xem `MEMORY.md §6`.

#### C-[MODULE]-[N] — <topic> (BLOCKER nếu chặn downstream)
**Source Quote (ambiguous):**
> "<verbatim ambiguous text từ doc>"

**Source Location:** `DOC-v[VERSION]-[NN] §[section] · paragraph [N]`
**Analyst Note:** <giải thích ambiguity + proposed resolution + tác động (BLOCKER/non-blocking)>

(lặp cho mỗi clarification cần trích; các clarification còn lại tóm tắt + status trong MEMORY §6)
