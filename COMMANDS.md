# COMMANDS — FoxEco

> Cheat-sheet lệnh gọi skill cho dự án **FoxEco** (SDK tích hợp vào app mobile **FoxPro** có sẵn — Solo, **chưa có automation**).
> Copy-paste lệnh theo thứ tự pipeline. Version dùng trong ví dụ dưới là `v1.0` — đổi thành version thật khi chạy.

## Pipeline flow

```
1. /create-test-plan --create
2. /analyze-requirements --init @00_input/v1.0/
3. /generate-tc @02_analyze-requirements/v1.0/
4. /review-tc @03_test-cases/v1.0/
5. /generate-tc --consolidate                → TC-MASTER-v1.0.xlsx
6. /vibe-mobile @03_test-cases/v1.0/         → 08_test-runs/vibe/ (chạy TC qua Appium MCP trên app FoxPro)
7. /log-bug                                  → 05_bug-reports/
8. /test-report                              → 09_reports/

/health-check                                → chạy bất kỳ lúc nào, đối chiếu consistency toàn bộ file trên
```

## 1. Test Plan
| Lệnh | Mô tả |
|------|-------|
| `/create-test-plan --create` (alias `/test-plan`) | Tạo test plan mới từ template |

## 2. Analyze Requirements
| Lệnh | Mô tả |
|------|-------|
| `/analyze-requirements --init @00_input/v1.0/` (alias `/analyze`) | Phân tích tài liệu version đầu |
| `/analyze-requirements --delta --version vX.Y @00_input/vX.Y/` | Phân tích version mới, so sánh parent |
| `/analyze-requirements --update "feedback BA/dev"` | Cập nhật theo feedback, không tạo lại từ đầu |
| `/analyze-requirements --review` | Xem tổng quan, không sửa file |
| `/analyze-requirements --sweep` | Completeness sweep — rà tìm requirement bỏ sót |
| `/analyze-requirements --migrate` | Migrate folder cũ (flat) về convention multi-version |

> Đặt tài liệu requirement (SDK spec, integration guide...) vào `00_input/[version]/` trước khi chạy.

## 3. Generate & Review Test Cases
| Lệnh | Mô tả |
|------|-------|
| `/generate-tc @02_analyze-requirements/v1.0/` | Sinh test case từ analysis (standard mode, 1-1 mapping) |
| `/generate-tc --module NAME` | Sinh TC cho 1 module |
| `/generate-tc --mode comprehensive` | Áp dụng đủ 8 test design technique (B1-B8), mở rộng TC + Coverage Matrix |
| `/generate-tc --direct --name "X" --id N --spec "..."` | Viết TC nhanh không qua analyze |
| `/generate-tc --consolidate` | Gộp fragments → `TC-MASTER-v[X].xlsx` |
| `/generate-tc --sync` | Đồng bộ fragment mới vào TC-MASTER đã có |
| `/review-tc @03_test-cases/v1.0/` | Review chất lượng TC (gate G1 ≥ 70) |
| `/review-tc --module NAME` | Review 1 module |
| `/review-tc --recheck` | Review lại sau khi sửa TC |

## 4. Vibe-test (chạy TC qua Appium MCP — không cần code automation)
| Lệnh | Mô tả |
|------|-------|
| `/vibe-test @03_test-cases/v1.0/` | Chạy TC qua MCP (tự phát hiện web/mobile), AI đóng vai manual tester |
| `/vibe-mobile` | Ép chạy nhánh mobile (Appium MCP) — dùng cho FoxEco SDK trên app FoxPro |

> Automation code (Appium Java) chưa được khởi tạo. Khi cần bật automation: `/init-source-code --archetype appium-java` → sau đó dùng thêm `/scan-source-code`, `/implement-automation`, `/review-src-tc`, `/execute-maintain` (hiện N/A).

## 5. Report & Bug
| Lệnh | Mô tả |
|------|-------|
| `/log-bug` | Ghi nhận bug vào `05_bug-reports/` + `bug-index.md` |
| `/test-report` (alias `/report`) | Báo cáo tổng kết vào `09_reports/` |

## 6. Health Check (cross-cutting, chạy bất kỳ lúc nào)
| Lệnh | Mô tả |
|------|-------|
| `/health-check` | Quick check — đối chiếu MEMORY files, phát hiện inconsistency (< 30s) |
| `/health-check --full` | Full check — thêm parse TC-MASTER Excel, ghi report vào `09_reports/` |
| `/health-check --version vX.Y` | Check riêng 1 version |

> **Jira:** dự án chưa cấu hình Jira (chưa start, sẽ bổ sung link sau) → `fetch-us` và `/log-bug --push-jira` chưa dùng được.
> Bổ sung block `## Jira Integration` vào `Project_rule.md` để bật (xem `fetch-us` skill để biết cấu hình cần thiết).
