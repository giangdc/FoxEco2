# Project Rules — FoxEco

> Quy tắc dự án dùng chung cho toàn pipeline QA. Các skill đọc file này để áp đúng convention.

## 1. Thông tin dự án (Project Info)
- **Tên dự án:** FoxEco
- **Loại sản phẩm:** SDK tích hợp vào app mobile **FoxPro** có sẵn (không phải web app độc lập)
- **QC phụ trách:** GiangDC2
- **Mode:** Solo
- **Version đầu tiên:** v1.0

## 2. Môi trường (Environments)
| Env | Host app | Default |
|-----|----------|---------|
| STG | FoxPro (mobile) | ✅ |

> Không có URL riêng vì FoxEco là SDK, không phải web app. Chi tiết host app/platform/build cập nhật vào `07_environments/environments.md`.

## 3. Loại kiểm thử (Test Types)
- Smoke
- Functional
- Regression

## 4. Ngôn ngữ (Language)
- Nội dung test case, mô tả, bước thực hiện, các thông báo trả ra trên terminal khi làm việc: **Tiếng Việt**
- Thuật ngữ kỹ thuật, keywords, status: **Tiếng Anh**

## 5. Automation
- **Có automation:** Không (hiện tại)
- (Khi cần thêm: chạy `/init-source-code --archetype appium-java` vì FoxEco là SDK tích hợp app mobile — Appium Java phù hợp nhất để scaffold `10_source-code/`.)

## 6. Quy tắc đặt tên (Naming Conventions)
- Documents: `DOC-v[VERSION]-[NN]`
- Scenarios: `SC-[MODULE]-[NNN]`
- Test cases: `TC-[MODULE]-[NNN]`
- TC Master: `TC-MASTER-v[VERSION].xlsx`
- Bug reports: `BUG-[NNN]-[short-title].md`
- Test runs: `TR-v[VERSION]-[YYYY-MM-DD].md`
- Reports: `REPORT-[TYPE]-v[VERSION]-[DATE].md`

## 7. Priority & Severity
- Priority: P1 (Highest) · P2 (High) · P3 (Medium) · P4 (Low)
- Severity: Critical · High · Medium · Low

## 8. Quality Gates (mặc định)
- G1: TC Review score ≥ 70
- G2: P1 pass rate = 100%
- G3: Overall pass rate ≥ 90%
- G4: No P1 bugs open
- G5: Bug fix rate ≥ 80%
- G6: Blocked ≤ 0
- G7: SRC-TC match score ≥ 70 (nếu có automation)

## 9. DOC Notation
req_notation: FR/VR (doc-native, module-prefixed)
# FR/VR: doc đánh số Functional/Validation Rule (vd kiểu FCP)
# none:  doc không đánh số → traceability dùng DOC-ID §section
# auto:  chưa rõ → analyze-requirements tự phát hiện từ doc ở lần chạy đầu rồi GHI NGƯỢC giá trị thật vào đây
#
# [auto-detected 2026-07-24 by analyze-requirements --init v1.0]
# DOC-v1.0-01 (FoxEco BRD v3.1) CÓ đánh số requirement, nhưng theo ID riêng từng domain thay vì
# 1 cặp FR/VR thống nhất: ORD-NN, ASN-NN, DLV-NN (viết tắt PUP/GPS/DLV/COST theo bước flow), GIFT-NN,
# CNL-NN, MTCH-NN, LOC-NN, RAT-NN (chức năng Gửi Hàng — bảng §D3); BR-<MODULE>-NN (Business Rules —
# §D4/§A5); NTF-NN (Notifications — §D6); OPR-NN (Operating Rules — §D7); NT-NN/USR-NN/TS-NN
# (Nền tảng chung — §A2/§A6/§A8); US-D<NN> (User Story kèm cột Acceptance Criteria riêng — §D1b).
# → Traceability cột "Maps (Ref DOC)" dùng TRỰC TIẾP ID gốc này (vd `ORD-01`, `BR-CNL-01`, `US-D16`),
#   không quy đổi sang ký hiệu FR/VR chuẩn hoá. DOC-v1.0-02 (PRD tái dựng từ demo, .docx) KHÔNG có ID
#   riêng cho từng field — định vị bằng `§section · Table N` (heading + số bảng).
# req_notation ghi "FR/VR (doc-native, module-prefixed)" để phản ánh: có đánh số thật (không phải
# "none"), nhưng không phải 1 ký hiệu FR/VR đơn nhất — mọi lần chạy sau dùng nguyên ID gốc theo domain.

## 10. Custom Rules

### 10.1 UI Figma phải khớp Tài liệu mới được viết TC (added 2026-07-24, QA GiangDC2)
- Chỉ viết test case khẳng định 1 field/nút/màn hình/hành vi UI cụ thể khi **cả 2 nguồn khớp nhau**:
  (a) tài liệu yêu cầu (BRD/PRD/US) và
  (b) bằng chứng UI thực tế (ảnh Figma DOC-v1.0-04 hoặc quan sát app STG thật).
- Nếu 2 nguồn **KHÔNG khớp** (field có trong tài liệu nhưng không thấy trên UI/Figma, hoặc ngược lại) → **KHÔNG tự suy đoán/bịa vị trí hay hành vi UI**. Bắt buộc:
  1. Ghi nhận thành clarification mới (`C-[MODULE]-NN`) trong `test_scenario_map.md`/`MEMORY.md`, đánh dấu rõ "chưa xác nhận UI".
  2. Không viết TC khẳng định field/hành vi đó tồn tại ở 1 màn hình cụ thể cho tới khi có xác nhận (BA/PO hoặc vibe-test trên app thật).
  3. Nếu cần, viết 1 TC dạng "GAP finding" ghi nhận sự thiếu vắng, thay vì TC test hành vi giả định.
- Áp dụng cho mọi skill sinh/viết TC: `generate-tc`, `vibe-test`, trả lời liệt kê case trực tiếp trong chat.
- Case gốc (ví dụ minh hoạ khi 2 nguồn không khớp): `USR-07` "Cấu hình kênh liên hệ sẽ lộ" (SĐT/Workplace-email) — có trong BRD (`DOC-v1.0-01`) nhưng KHÔNG xuất hiện ở bất kỳ ảnh Figma nào (`DOC-v1.0-04`) của màn Cá nhân, và QA xác nhận không thấy trên app STG thật. **Cập nhật 2026-07-27:** `C-USR-02` nay đã **Resolved — Deferred** (BA/PO xác nhận tính năng này là phase sau, không thuộc scope UI v1.0) — không còn là GAP đang chờ xác nhận nữa, nhưng vẫn giữ làm case tham khảo cho rule này khi gặp mâu thuẫn tương tự ở clarification khác.

### 10.2 Màn hình có tab/segmented-control → mỗi tab 1 TC riêng verify data (added 2026-07-27, QA GiangDC2)
- Khi 1 màn hình có tab switcher/segmented-control lọc dữ liệu theo trạng thái (vd "Đang diễn ra"/"Đã hoàn thành"), **KHÔNG gộp việc verify data của cả 2 (hoặc nhiều) tab vào chung 1 TC "chuyển tab qua lại"**.
- Bắt buộc: mỗi tab có **≥1 TC riêng biệt** verify đúng data hiển thị khi tab đó active (danh sách chỉ chứa đúng nhóm trạng thái thuộc tab đó, không lẫn dữ liệu của tab khác).
- Lý do: khi 1 TC gộp gồm nhiều bước kiểm tra data ở nhiều tab, nếu FAIL sẽ không rõ ngay tab nào sai (phải đọc lại từng step) — tách riêng giúp trace lỗi tức thì + khớp nguyên tắc atomic test case (1 TC verify 1 điều kiện rõ ràng).
- Việc UI tab switcher tồn tại/switch được (cơ chế bấm đổi tab) vẫn có thể giữ là 1 TC riêng, độc lập với các TC verify-data-theo-tab.
- Áp dụng cho mọi skill sinh TC: `generate-tc`, `vibe-test`, trả lời liệt kê case trực tiếp trong chat.
- Case gốc: màn "Hoạt động" (Đơn của tôi) — SC-ORD-017 (data tab "Đang diễn ra") và SC-ORD-026 (data tab "Đã hoàn thành"), tách ra từ 1 TC gộp ban đầu.

### Phase 1 Scope (PM confirm 2026-07-24)
PM chốt phạm vi kiểm thử v1.0 (Phase 1) chỉ gồm 5 luồng chính:
1. Đăng tin (NEED/OFFER) — module ORD
2. Bảng tin — module ORD (screen Bảng tin)
3. Ghép nối — module ASN (⚠ chưa rõ có gồm auto-match OFFER↔NEED hay chỉ luồng thủ công — câu hỏi RIÊNG về scope Phase 1 test, khác clarification C-xxx, PM chưa trả lời)
4. Xác nhận nhận hàng / hoàn thành — module DLV (⚠ chưa rõ có gồm ảnh bằng chứng/GPS/chi phí/báo sự cố hay chỉ core confirm — câu hỏi RIÊNG về scope Phase 1 test, khác clarification C-xxx, PM chưa trả lời)
5. Đánh giá — module GIFT (✅ Resolved 2026-07-27: "Đánh giá" trong Phase 1 chỉ có nghĩa **Quà ảo (GIFT-01)** — Chấm sao/RAT-01/02 là phase sau, out of scope v1.0, xem C-GIFT-01)

**Ngoài phạm vi Phase 1 (đã xác nhận Out of scope v1.0, 2026-07-27):** CNL (Huỷ đơn), NTF (Thông báo), TS (Trust & Safety/Admin), USR chỉ số cá nhân nâng cao (tier/điểm ECO/CO2), chỉnh sửa tin (ORD-10), ảnh bằng chứng/GPS/chi phí/báo sự cố (nhánh phụ của DLV), auto-match tuyến OFFER↔NEED (nhánh phụ của ASN).

**Câu hỏi ưu tiên cần PM/BA trả lời trong scope Phase 1 — Đã resolved (2026-07-27, BA/PO trả lời qua chat, chi tiết đầy đủ xem `02_analyze-requirements/v1.0/MEMORY.md §6`):**
- "Đánh giá" = Quà ảo hay Chấm sao? → **Quà ảo (GIFT-01)**; Chấm sao là phase sau (C-GIFT-01, C-USR-01: Resolved — Deferred).
- Ai được xác nhận "Đã nhận hàng"? → **Chỉ Receiver** (C-DLV-01: Resolved).
- Ngưỡng giá trị hàng cảnh báo bảo hiểm? → **Chưa làm ở v1.0** (C-ORD-02: Resolved — Deferred).
- Wizard đăng tin có field nào bắt buộc không? → **Có** — Loại hàng/Giá trị (B1) + Người nhận (B2) bắt buộc, maxlength TBD (C-ORD-01: Resolved).
- Hạn tin mặc định bao lâu? → **Theo giá trị "Đến ngày" user tự chọn** lúc đăng tin, không phải hằng số (C-ORD-03: Resolved).
- SĐT có nên hiện sớm ở Chi tiết tin trước khi ghép không? → **Không** — chỉ lộ sau khi ghép, theo BRD (C-ASN-01: Resolved).
- Chủ tin/Người nhận có được tự "nhận mang giúp" tin của mình không? → **Không**, khớp OPR-05 (C-ASN-02: Resolved).
- Dùng UI nào cho màn xác nhận nhận hàng? → **Modal đơn giản** (theo Figma); form đầy đủ out of scope v1.0 (C-DLV-03: Resolved).

**Còn Open thực sự (chưa có câu trả lời):** `C-ORD-05` (biến thể "Mã tin"), `C-NTF-01` (danh sách thông báo chính thức — đã có bảng unified 3 nguồn ở `MEMORY.md §6.1` chờ BA chọn), `C-DLV-02` (default bật/tắt chia sẻ vị trí), maxlength cụ thể của `C-ORD-01`.

## Jira Integration
> Khám phá + xác nhận 2026-08-04 qua Atlassian MCP (`getVisibleJiraProjects` → `getJiraProjectIssueTypesMetadata`
> → `getJiraIssueTypeMetaWithFields` → `getTransitionsForJiraIssue` trên issue thật FE-146/FE-131) +
> đối chiếu 49 bug Bug-type đã có sẵn trong project (dự án LIVE, team đã dùng thật — KHÔNG phải sandbox).
qc_name:         GiangDC2
site:            https://foxproject.atlassian.net
cloud_id:        f192baca-4acd-46c2-8d8d-ce0d4e636d4e
project_key:     FE
issue_type:      Bug          # id 10293
reporter:                     # để trống = tài khoản auth (giangdc2@fpt.com)
parent_epic:     FE-1         # "[FoxEco] Triển khai Phase 1 - Nền tảng chung & Gửi hàng (MVP)" — user xác nhận 2026-08-04: LUÔN gắn, khớp 100% 49 bug hiện có
fix_version:     10518        # tên "V1.0", khớp affects_versions: [v1.0]
priority_map:    P1=Highest, P2=High, P3=Medium, P4=Low   # khớp đúng tên trong Jira (không cần đổi), §7 file này
required_fields:               # KHÔNG có custom field nào bắt buộc thật — create-meta chỉ ép issuetype/project/reporter/summary (system field, skill tự set)
recommended_fields:            # cascading select — value dạng {"value": "..."} khi build additional_fields
  - customfield_10678: "{severity_code}"   # Severity — value = SỐ dạng string, allowedValues: 0/2/5/10/20 (khớp map Critical=20·Major=10·Medium=5·Low=2 sẵn có trong log.md; "0" chưa rõ nhãn tương ứng, không dùng)
  - customfield_10679: "{round_found}"     # Test Round — value = SỐ dạng string "1".."7", lấy trực tiếp round_found
  - customfield_10681: "Android, iOS"      # Platform — user xác nhận 2026-08-04: LUÔN dùng giá trị gộp này (khớp convention team, dù QA hiện chỉ test Android qua Appium MCP) — field KHÔNG có option "Mobile" riêng
  - customfield_10682: "{effect}"          # Effect — value trùng tên trực tiếp với effect front-matter (Functionality/Performance/Security/Serviceability/Usability)
  - customfield_10685: "{defect}"          # Defect Type — value trùng tên trực tiếp với defect front-matter (Data/Interface/Logic/Server/Other); Jira có thêm option "Requirement" chưa dùng trong md enum
  # customfield_10683 (Test method) để mặc định "Manual" (defaultValue có sẵn) — vibe-test là AI-assisted exploratory, gần Manual hơn Auto
  # customfield_11055 (Duplicate) để mặc định "No"
status_map:      New=To Do, InProgress=In Progress, Fixed=In review, Verified=Done, Closed=Done
                 # workflow thật (xác nhận qua getTransitionsForJiraIssue trên FE-131, status "In review"):
                 # To Do → In Progress → In review → (QC Accept) → Done  |  (QC Reject) → về In Progress
                 # Any status → "To cancel" → Cancel (Done-category, dùng cho Won't Fix) | → "Pending" → Pending (Done-category, dùng khi blocked)
description_extra: [Environment, Version, Module, Traceability]
match_jql:       project = {project_key} AND labels = "{bug_id_lower}"
                 # ⚠ KHÔNG dùng summary ~ "{bug_id}" (default schema) — team KHÔNG đặt "BUG-NNN" trong Summary,
                 # convention thật của team: Summary = "[TC_XX - Tên module]: <mô tả ngắn>" (vd
                 # "[TC_03 - Thông báo ]: Gởi cùng lúc 2 thông báo cảm ơn..."), Description dạng
                 # "Điều kiện test:/Step:/Actual:/=> Bug:/KQMM:". Khi push-jira thật chạy: (1) build Summary
                 # theo đúng format trên (lấy TC ID đầu tiên trong labels + Module từ components[0]), KHÔNG
                 # dùng format "[BUG-NNN] title" mặc định của push-jira.md, để khớp UI Jira team đang nhìn;
                 # (2) vẫn thêm 1 label riêng `bug-nnn` (lowercase, vd "bug-003") — KHÔNG hiện trên UI chính,
                 # chỉ dùng để match_jql pull ngược đúng issue.
notes:
  - "49 bug Bug-type hiện có trong FE, status thật: To Do=27 · In Progress=9 · In review=13, chưa có Done nào."
  - "Assignee mặc định do Jira/automation project tự set (quan sát: hầu hết về Tuanvm37) — log-bug KHÔNG tự set assignee, để trống khi create."
  - "Có vài custom field khác (customfield_10825='ISC', customfield_10787/10972='Normal') xuất hiện trên issue thật nhưng KHÔNG có trong create-meta (getJiraIssueTypeMetaWithFields) — nhiều khả năng do Jira Automation rule tự điền SAU khi tạo, KHÔNG cần set thủ công lúc create."
userstory:                       # sub-section riêng cho fetch-us — CHƯA xác nhận, để nguyên default
  issue_types:   [Story]
  jql_template:  project = {project_key} AND issuetype in ({issue_types}) AND fixVersion = "{version}" ORDER BY key ASC
  link_handling:
    figma:   record
    gsheets: read_text
    gdocs:   read_text
    gdrive:
      enabled: true
    other:   record
  attachment_download:
    env_file: ~/.config/jira/.env
