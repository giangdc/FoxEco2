# FoxEco — Manual Testing Project

## Mục đích (Purpose)
Dự án kiểm thử thủ công cho **FoxEco** — SDK tích hợp vào app mobile **FoxPro** có sẵn.

## Loại kiểm thử (Test Types)
Smoke, Functional, Regression

## Initial Version
v1.0

## Cấu trúc thư mục (Folder Structure)
| Thư mục | Mục đích |
|---------|----------|
| `00_input/[version]/` | Tài liệu đầu vào theo version |
| `00_input/shared/` | Tài liệu dùng chung mọi version |
| `01_test-plans/` | Kế hoạch kiểm thử theo release/feature |
| `02_analyze-requirements/` | MASTER-MEMORY + Project_rule + version analysis |
| `02_analyze-requirements/[version]/` | Kết quả phân tích theo version |
| `03_test-cases/[version]/` | TC-MASTER + fragments theo version |
| `04_test-data/` | Dữ liệu kiểm thử (valid/invalid) |
| `05_bug-reports/` | Báo cáo lỗi |
| `06_checklists/` | Checklist smoke test & release |
| `07_environments/` | Cấu hình môi trường |
| `08_test-runs/` | Log kết quả chạy test theo sprint |
| `09_reports/` | Báo cáo tổng kết cho stakeholders |
| `10_source-code/` | Automation source code + MEMORY tracking |
| `11_tc-review/` | TC review + SRC-TC review reports |

## Quy tắc đặt tên (Naming Conventions)
- Documents: `DOC-v[VERSION]-[NN]`
- Scenarios: `SC-[MODULE]-[NNN]`
- Test cases: `TC-[MODULE]-[NNN]`
- TC Master: `TC-MASTER-v[VERSION].xlsx`
- Bug reports: `BUG-[NNN]-[short-title].md`
- Test runs: `TR-v[VERSION]-[YYYY-MM-DD].md`
- Reports: `REPORT-[TYPE]-v[VERSION]-[DATE].md`

## Môi trường mặc định (Default Environment)
**STG**

## Ngôn ngữ (Language)
- Nội dung test case, mô tả, bước thực hiện: **Tiếng Việt**
- Thuật ngữ kỹ thuật, keywords, status: **Tiếng Anh**

## Project Rules
→ Chi tiết: `02_analyze-requirements/Project_rule.md`

## Pipeline & Commands
- `PIPELINE.md` — bản đồ pipeline QA, skill registry
- `COMMANDS.md` — cheat-sheet lệnh gọi từng skill (copy-paste theo thứ tự)

## Liên hệ (Contacts)
- QA Lead: GiangDC2
- Dev Lead:
- PM:
