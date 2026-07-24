# Generate TC — Mode CONSOLIDATE

> `/generate-tc --consolidate` | `/generate-tc --consolidate --version v2.0`
> Gộp tất cả fragments → TC-MASTER (workbook đầy đủ theo template ISC)

## Bối cảnh — thay đổi so với schema cũ

TC-MASTER giờ là bản build từ **template ISC gốc** (`03_test-cases/_template/ISC_Template_SDLC_TestCase_Report_Version.xlsx` — xem `generate.md` Step 0), không còn tự dựng sheet `Overview`/`ALL`/per-module. Mỗi module/function = **1 sheet riêng** (`Test Cases`, `Test Case 2`, `Test Case 3`...) trong CÙNG 1 workbook, cộng với các sheet workbook-level cố định: `Cover`, `Guideline`, `Revision History`, `Summary`, `Dashboard`, `Report Test`, `Bug Data`, `RTM`.

**File naming (quy định QA, Guideline sheet mục 1):**
```
ISC_[Tên dự án]_[Version]_TC_[Version TC]_R[Số round test].xlsx
```
Output chính: `03_test-cases/v[X]/ISC_[Project]_[X]_TC_[TCVersion]_R[Round].xlsx`

**Cầu nối tương thích pipeline (tạm thời):** review-tc, implement-automation, review-src-tc, health-check, test-report, log-bug, vibe-test hiện vẫn tham chiếu path cứng `TC-MASTER-v[X].xlsx` / `TC-MASTER-LATEST.xlsx` (chưa được cập nhật theo template mới). generate-tc **PHẢI** tiếp tục xuất 2 file này như bản copy/alias của file ISC chính thức, cho đến khi các skill downstream được cập nhật (xem gap analysis — out of scope của lần sửa này). Không được bỏ bước này, nếu không toàn bộ downstream sẽ gãy.

## Workflow

### Step 1: Xác định version + scan fragments

```bash
ls 03_test-cases/v[X]/fragments/TC-*.xlsx
```

Liệt kê fragments → confirm với user:
```
📂 Fragments found cho v2.0:
  - TC-LOGIN-v2.0.xlsx (8 TCs)
  - TC-DASHBOARD-v2.0.xlsx (12 TCs)
  - TC-PROFILE-v2.0.xlsx (5 TCs)

Include CARRIED TCs từ v1.0 (regression)? (Y/N)
```

### Step 2: Đọc CARRIED TCs (nếu regression)

Template ISC **không có cột Version Origin/Lifecycle riêng** (khác schema cũ) — lifecycle NEW/CARRIED/MODIFIED chỉ sống trong Version MEMORY §4, không phải trong Excel.

```
1. MASTER-MEMORY §4 → Regression Scope
2. TC-MASTER-v[PARENT] (file ISC của version cha) → đọc sheet function tương ứng, copy cột B–M của
   các TC CARRIED
3. Khi ghi sang sheet function của version mới:
   - Cột B–M: copy nguyên giá trị (Req ID, DOC Source, Group, Priority, Title, Steps, Expected,
     Origin, Review, Automated, Script)
   - Cột N–AL (round data): để TRỐNG — bắt buộc retest ở version mới, KHÔNG copy kết quả round cũ
   - Cột AP (Remark): ghi `Carried từ v[PARENT]` — nếu ô đã có nội dung khác (vd Technique tag),
     nối thêm bằng ` | Carried từ v[PARENT]`
   - Cột A (Testcase ID) và AM/AN/AO: copy formula (không copy giá trị), dịch theo row mới — ID sẽ
     tự sinh lại theo STT của sheet version mới, KHÔNG giữ ID cũ (ID cũ chỉ còn ý nghĩa lịch sử trong
     MEMORY §9/CHANGELOG)
   - Vị trí chèn row: theo đúng Screen/Block của scenario CARRIED đó (cột Screen/Block ở bảng
     "Scenarios — CARRIED" trong `test_scenario_map.md` version mới) — chèn vào ĐÚNG nhóm label row
     tương ứng (xem `generate.md` Step 6.4), không append rời ở cuối sheet phá vỡ thứ tự group.
```

### Step 3: Merge vào TC-MASTER

Đọc skill xlsx: `view /mnt/skills/public/xlsx/SKILL.md`

**Cách build TC-MASTER (bám sát template ISC):**

```
1. Nếu TC-MASTER-v[X] (ISC) CHƯA tồn tại cho version này:
   - Copy nguyên 03_test-cases/_template/ISC_Template_SDLC_TestCase_Report_Version.xlsx →
     03_test-cases/v[X]/ISC_[Project]_[X]_TC_v1_R1.xlsx (giữ nguyên toàn bộ sheet: Cover, Guideline,
     Revision History, Summary, Dashboard, Report Test, Bug Data, RTM, + 1 sheet "Test Cases" mẫu)
   - Ghi Summary!C6 (Tên dự án), C8 (Version), C9 (Sprint), C10/C11 (ngày test) — các sheet
     Test Cases/RTM/Dashboard tham chiếu ngược lại các cell này qua formula, tự cập nhật.
   - Ghi Revision History row đầu: version=1.0, ngày=hôm nay, change="Tạo mới".
2. Với MỖI module trong fragments (theo thứ tự generate):
   a. Nếu module đã có sheet trong TC-MASTER (do SYNC lần trước) → xem sync.md Step 3 REPLACE.
   b. Nếu module MỚI:
      - Nếu đây là module đầu tiên → dùng thẳng sheet "Test Cases" có sẵn trong template.
      - Nếu không → duplicate sheet template "Test Cases" (giữ nguyên format/formula/data
        validation), đặt tên tab = tên module (Excel giới hạn tối đa 31 ký tự — sanitize/rút gọn
        nếu cần, tránh ký tự `: \ / ? * [ ]`).
      - Gán Mã chức năng (C2): quét cột C sheet Dashboard (row 4–33) lấy số `TC_NN` lớn nhất hiện
        có, +1. Ghi C3 = tên module.
      - Copy toàn bộ vùng row 7→cuối của fragment vào sheet mới — **bao gồm cả row label Screen/Block**
        (`generate.md` Step 6.4: merge A:I hoặc B:I, fill màu, text) chứ không chỉ riêng cột B–M của
        row TC. Copy nguyên giá trị + merge cells + fill của mọi row (label lẫn TC); copy-down formula
        cột A/AM/AN/AO riêng cho row TC theo đúng số row (row label không có formula cột A).
      - Nếu module có Coverage Matrix sheet trong fragment (comprehensive mode) → copy nguyên
        sheet đó vào TC-MASTER (giữ tên `Coverage Matrix`; nếu đã tồn tại từ module khác, đổi tên
        `Coverage Matrix - [Module]` để tránh trùng — sheet này KHÔNG thuộc bộ 9 sheet chuẩn ISC).
   c. **Thêm 1 row mới vào sheet Dashboard** (row tiếp theo trong khoảng 4–33, đã có sẵn formula
      cho mọi cột F trở đi — xem `generate.md`): điền tay 4 cột B (STT)/C (Mã CN)/D (Tên tab sheet
      — PHẢI khớp 100% tên sheet thật)/E (Function/Màn hình). KHÔNG động vào cột F trở đi (formula
      tự tính khi mở Excel).
   d. **Cập nhật RTM cho mọi Req ID xuất hiện trong module này:**
      - Formula RTM (cột E/F/G/H) hard-code TÊN SHEET trực tiếp (không dùng INDIRECT), dạng:
        `=COUNTIF('Test Cases'!$B$7:$B$500,"*"&$B6&"*")+COUNTIF('Test Case 2'!$B$7:$B$500,"*"&$B6&"*")+...`
      - Với Req ID ĐÃ có row trong RTM: nối thêm 1 term `+COUNTIF('[TênSheetMới]'!$B$7:$B$500,"*"&$B[row]&"*")`
        vào CUỐI mỗi formula E/F/G/H hiện tại của row đó (áp dụng tương tự cho F/G/H, khác điều
        kiện đếm theo formula gốc đã có ở `generate.md`).
      - Với Req ID CHƯA có trong RTM: thêm row mới (B=Req ID, C=mô tả lấy từ MEMORY §2/§4, D=DOC
        Source, rồi 4 formula E/F/G/H chỉ chứa 1 term ứng với sheet mới, I=`=IFERROR(F[row]/E[row],0)`,
        J=`=IF(E[row]=0,"Chưa có TC (gap)",IF(H[row]>0,"Có lỗi (Fail)",IF(F[row]>=E[row],"Đã test xong","Đang test")))`).
      - **Không bỏ qua bước này** — bỏ qua sẽ khiến RTM báo sai coverage (thiếu đếm sheet mới) dù
        Dashboard/Test Cases đúng.
      - ⚠️ **Row "Tổng" cuối RTM** (template mẫu: row 11, ngay dưới 5 Req ID mẫu) có formula
        `=SUM(E6:E10)` (tương tự F/G/H) — **range CỐ ĐỊNH, không tự mở rộng** khi thêm row mới (khác
        Dashboard vốn đã pre-provision sẵn 30 row formula 4–33). Khi thêm Req ID row mới bên trên
        row Tổng: PHẢI `ws.insert_rows()` thật (không ghi đè xuống row trống phía dưới) để Excel tự
        dịch row Tổng xuống VÀ tự mở rộng range SUM theo cơ chế insert-row chuẩn của Excel; nếu công
        cụ ghi không hỗ trợ insert-row có dịch formula, phải tự tay sửa lại range SUM (`E6:E[dòng data
        cuối]`, tương tự F/G/H) sau khi thêm row — nếu quên, row Tổng sẽ tính thiếu các Req ID mới.
3. Summary!C12 (Số sheet chức năng) tự cập nhật qua formula `=COUNTIF(Dashboard!$D$4:$D$33,"?*")` —
   không cần ghi tay.
```

### Step 4: Validate

- Mã chức năng (C2 mỗi sheet) không trùng, tăng dần
- Tên tab sheet ≤ 31 ký tự, khớp 100% với cột D Dashboard tương ứng, không trùng tên
- Mọi Req ID trong các sheet TC đều có row tương ứng trong RTM (không orphan)
- RTM formula của MỌI row đã có đủ term cho MỌI sheet TC hiện có trong workbook (không sheet nào bị thiếu trong chuỗi `+COUNTIF(...)`)
- RTM row "Tổng": range 4 formula `SUM(E...:E...)`/F/G/H đã bao trọn từ row data đầu tới row data cuối (không sót Req ID mới thêm ở cuối)
- Sort thứ tự sheet tab: theo thứ tự tạo module (không bắt buộc alphabet)

### Step 5: Xuất file + tạo alias tương thích pipeline

```bash
# File chính thức theo quy định QA
03_test-cases/v[X]/ISC_[Project]_[X]_TC_[TCVersion]_R[Round].xlsx

# Alias bắt buộc cho downstream skill chưa migrate (xem "Bối cảnh" ở trên)
cp ISC_..._R[Round].xlsx 03_test-cases/v[X]/TC-MASTER-v[X].xlsx
cp ISC_..._R[Round].xlsx 03_test-cases/TC-MASTER-LATEST.xlsx
```

### Step 6: Cập nhật MASTER-MEMORY §6

```
| v2.0 | ISC_[Project]_v2.0_TC_v1_R1.xlsx (alias: TC-MASTER-v2.0.xlsx) | 45 | 2026-04-15 | ✅ Consolidated |
```

Ghi CHANGELOG: `action = CONSOLIDATE, scope = all fragments + [N] CARRIED`
Ghi §8 = COMPLETED. Append CLAUDE.md.

## Checklist
- [ ] Tất cả fragments merged, mỗi module = 1 sheet riêng dựa trên template "Test Cases"
- [ ] Row label Screen/Block (merge cell + fill màu) được copy nguyên từ fragment, không chỉ copy cột B–M; CARRIED TC chèn đúng nhóm Screen/Block, không append rời cuối sheet
- [ ] CARRIED TCs included (nếu regression) — cột B–M copy, round data (N–AL) để trống, Remark ghi `Carried từ v[X]`
- [ ] Mã chức năng không trùng, tăng dần; tên tab sheet khớp 100% với Dashboard cột D
- [ ] Dashboard có đủ 1 row / module, cột B–E điền tay đúng, cột F+ để formula tự tính
- [ ] RTM: mọi Req ID có row, formula mỗi row đã cộng đủ term cho MỌI sheet TC hiện có
- [ ] RTM row "Tổng": range SUM đã mở rộng bao hết Req ID row mới (không bị bỏ sót do range cố định)
- [ ] TC-MASTER ISC file tạo thành công (Cover/Guideline/Revision History/Summary/Dashboard/Report Test/Bug Data/RTM + N sheet TC)
- [ ] Alias TC-MASTER-v[X].xlsx + TC-MASTER-LATEST.xlsx đã copy (tương thích downstream skill chưa migrate)
- [ ] MASTER-MEMORY §6 cập nhật
- [ ] §8 = COMPLETED
