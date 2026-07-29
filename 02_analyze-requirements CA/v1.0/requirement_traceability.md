# Requirement Traceability — v1.0

> Tạo bởi: analyze-requirements. Ma trận truy vết REQ ↔ DOC ↔ Scenario ↔ Clarification.
> Text-level traceability: Source Quote per REQ ở `MEMORY.md §4.1`, per SC ở `test_scenario_map.md`.
>
> **Structure-lock:** giữ nguyên header cột + section dưới đây. KHÔNG tự thêm/bớt/đổi tên cột.

## 1. Traceability Matrix (REQ → DOC → SC)

> 1 bảng con per module. 1 dòng / REQ (KHÔNG gộp nhiều REQ vào 1 dòng).

### Module SENDER — DOC-v1.0-01, DOC-v1.0-02
| REQ ID | Maps (Ref DOC) | DOC §section | Scenarios | Clarification |
|--------|----------------|--------------|-----------|---------------|
| REQ-SENDER-001 | — | §1.1 | SC-SENDER-001, SC-SENDER-002 | C-SENDER-1 (resolved) |
| REQ-SENDER-002 | — | §1.2 | SC-SENDER-003 | C-SENDER-2 |
| REQ-SENDER-003 | — | §1.3 | SC-SENDER-004 | — |
| REQ-SENDER-004 | — | §1.4 | SC-SENDER-005, SC-SENDER-006, SC-SENDER-007 | — |
| REQ-SENDER-005 | — | §1.5 | SC-SENDER-008 | C-SENDER-2 |
| REQ-SENDER-006 | — | §D1b US-D18 | SC-SENDER-009, SC-SENDER-010 | — (🚫 Blocked, xem §2) |

### Module CARRIER — DOC-v1.0-01, DOC-v1.0-03
| REQ ID | Maps (Ref DOC) | DOC §section | Scenarios | Clarification |
|--------|----------------|--------------|-----------|---------------|
| REQ-CARRIER-001 | — | §2.1 | SC-CARRIER-001 | — |
| REQ-CARRIER-002 | — | §2.2 | SC-CARRIER-002, SC-CARRIER-003 | — |
| REQ-CARRIER-003 | — | §2.3 | SC-CARRIER-004 | — |
| REQ-CARRIER-004 | — | §2.4 | SC-CARRIER-005, SC-CARRIER-006 | C-CARRIER-1 (resolved) |
| REQ-CARRIER-005 | — | §2.5 | SC-CARRIER-007 | C-CARRIER-2 (resolved) |
| REQ-CARRIER-006 | — | UI DOC-v1.0-03 (Bảng tin/Chi tiết tin field-level, không có §section BRD) | SC-CARRIER-008, SC-CARRIER-009 | — |

### Module RECEIVER — DOC-v1.0-01
| REQ ID | Maps (Ref DOC) | DOC §section | Scenarios | Clarification |
|--------|----------------|--------------|-----------|---------------|
| REQ-RECEIVER-001 | — | §3.1 | SC-RECEIVER-001, SC-RECEIVER-002 | — |
| REQ-RECEIVER-002 | — | §3.2 | SC-RECEIVER-003, SC-RECEIVER-004 | C-GENERAL-2 (bước ngay sau — xem §2) |

### Module OFFER — DOC-v1.0-02, DOC-v1.0-03 (🔓 Unblocked 2026-07-27 — UI xác nhận qua Chrome MCP)
| REQ ID | Maps (Ref DOC) | DOC §section | Scenarios | Clarification |
|--------|----------------|--------------|-----------|---------------|
| REQ-OFFER-001 | — | §D1b US-D10; UI DOC-v1.0-03 | SC-OFFER-001 | C-SENDER-1 (unblocked) |
| REQ-OFFER-002 | — | §D1b US-D11 | SC-OFFER-002 | — |
| REQ-OFFER-003 | — | §D1b US-D12, §D6 NTF-03; UI DOC-v1.0-03 | SC-OFFER-003 | — |
| REQ-OFFER-004 | — | §D1b US-D13 | SC-OFFER-004 | — |

### Module CANCEL — DOC-v1.0-02, DOC-v1.0-03 (🔓 Unblocked 2026-07-27 — UI xác nhận qua Chrome MCP)
| REQ ID | Maps (Ref DOC) | DOC §section | Scenarios | Clarification |
|--------|----------------|--------------|-----------|---------------|
| REQ-CANCEL-001 | — | §D1b US-D16, §D3 CNL-01, §D4 BR-CNL-01; UI DOC-v1.0-03 | SC-CANCEL-001, SC-CANCEL-002 | C-CARRIER-1 (unblocked) |
| REQ-CANCEL-002 | — | §D7 OPR-11, §D4 BR-ASN-03 | SC-CANCEL-003 | — |
| REQ-CANCEL-003 | — | §D7 OPR-09 | SC-CANCEL-004 | — |
| REQ-CANCEL-004 | — | §D1b US-D16 | SC-CANCEL-002 | — |

### Module GIFT — DOC-v1.0-02, DOC-v1.0-03 (🔓 Unblocked 2026-07-27 — UI xác nhận qua Chrome MCP)
| REQ ID | Maps (Ref DOC) | DOC §section | Scenarios | Clarification |
|--------|----------------|--------------|-----------|---------------|
| REQ-GIFT-001 | — | §A7; UI DOC-v1.0-03 | SC-GIFT-001 | — |
| REQ-GIFT-002 | — | §D1b US-D15; UI DOC-v1.0-03 (⚠️ có nút xác nhận, khác BRD) | SC-GIFT-002 | C-GENERAL-2 |
| REQ-GIFT-003 | — | §D1b US-D20; UI DOC-v1.0-03 | SC-GIFT-003 | C-GIFT-2 (resolved qua Figma) |
| REQ-GIFT-004 | — | UI DOC-v1.0-03 (không có §section BRD tương ứng) | SC-GIFT-004 | C-GIFT-2 (resolved qua Figma) |

### Module NOTIFICATION — DOC-v1.0-02, DOC-v1.0-03 (🔓 Unblocked 2026-07-27 — UI xác nhận qua Chrome MCP)
| REQ ID | Maps (Ref DOC) | DOC §section | Scenarios | Clarification |
|--------|----------------|--------------|-----------|---------------|
| REQ-NOTIFICATION-001 | — | §D6; UI DOC-v1.0-03 | SC-NOTIFICATION-001 | — |
| REQ-NOTIFICATION-002 | — | UI DOC-v1.0-03 (không có §section BRD tương ứng) | SC-NOTIFICATION-002 | — |

### Module ORDER — DOC-v1.0-01, DOC-v1.0-02
| REQ ID | Maps (Ref DOC) | DOC §section | Scenarios | Clarification |
|--------|----------------|--------------|-----------|---------------|
| REQ-ORDER-001 | — | §4 | SC-ORDER-001 | — |
| REQ-ORDER-002 | — | §4 | SC-ORDER-002, SC-ORDER-003, SC-ORDER-004 | C-ORDER-1 |
| REQ-ORDER-003 | — | §D1b US-D19, §D4 BR-EDIT-01 | SC-ORDER-005, SC-ORDER-006 | — (🚫 Blocked, xem §2) |
| REQ-ORDER-004 | — | §D1b US-D04 | SC-ORDER-007 | C-ORDER-2 (🚫 Blocked, xem §2) |

### Module ADMIN — DOC-v1.0-02 (🚫 Blocked — không có Admin Portal, xem §2)
| REQ ID | Maps (Ref DOC) | DOC §section | Scenarios | Clarification |
|--------|----------------|--------------|-----------|---------------|
| REQ-ADMIN-001 | — | §D4 Permission Matrix | SC-ADMIN-001 | — |

### Module MEDIA — DOC-v1.0-02 (🚫 Blocked — chưa có UI, xem §2)
| REQ ID | Maps (Ref DOC) | DOC §section | Scenarios | Clarification |
|--------|----------------|--------------|-----------|---------------|
| REQ-MEDIA-001 | — | §D3 PUP-03 | SC-MEDIA-001 | — |
| REQ-MEDIA-002 | — | §D3 GPS-01 | SC-MEDIA-002 | — |

### Module GENERAL — DOC-v1.0-01, DOC-v1.0-02, DOC-v1.0-03
| REQ ID | Maps (Ref DOC) | DOC §section | Scenarios | Clarification |
|--------|----------------|--------------|-----------|---------------|
| REQ-GENERAL-001 | — | §0 | SC-GENERAL-001 | — |
| REQ-GENERAL-002 | — | UI DOC-v1.0-03 (không có §section, không có mô tả tương ứng trong DOC-v1.0-01/02) | SC-GENERAL-002 | — |
| REQ-GENERAL-003 | — | UI DOC-v1.0-03 (Trang chủ dashboard, không có §section BRD) | SC-GENERAL-003, SC-GENERAL-004 | — |

> **Cột Maps (Ref DOC):** `req_notation: none` trong `Project_rule.md` — cả DOC-v1.0-01 và DOC-v1.0-02 đều không dùng ký hiệu FR/VR/AC/UC nhất quán đủ để trích trực tiếp (BRD có mã ID riêng theo module như ORD-01/CNL-01/GIFT-01/US-D16 nhưng không phải hệ thống numbering thống nhất kiểu FR/VR) — toàn bộ cột này để `—`, traceability dựa vào cột `DOC §section` (đã bao gồm mã ID gốc của BRD trong section ref, vd "§D1b US-D16", "§D7 OPR-11" để dễ tra ngược).

## 2. Coverage Summary
- **Scenario có REQ + DOC source:** 51/51 (100%).
- **REQ có ≥1 scenario:** 38/38 (100%) — mọi REQ đều có ít nhất 1 scenario.
- **REQ chưa có scenario (gap có chủ đích):** Không có.
- **🔓 UNBLOCK (2026-07-27, sau khi tích hợp DOC-v1.0-03):** 4/6 module trước đó Blocked nay đã có UI thật xác nhận qua Chrome MCP — **OFFER, CANCEL, GIFT, NOTIFICATION** chuyển ⏳ Ready (sẵn sàng generate-tc). Chỉ còn **ADMIN** (không có Admin Portal) và **MEDIA** (camera/GPS chưa có UI) thật sự 🚫 Blocked. SC-ORDER-007 (EXPIRED) Blocked 1 phần (badge có ở lịch sử Sender, feed công khai chưa verify).
- **🚫 REQ/SC còn Blocked thật:** REQ-ADMIN-001/SC-ADMIN-001, REQ-MEDIA-001..002/SC-MEDIA-001..002, REQ-SENDER-006/SC-SENDER-009..010 (email tự điền — chưa có field trong prototype), REQ-ORDER-003/SC-ORDER-005..006 (chỉnh sửa đơn), REQ-ORDER-004/SC-ORDER-007 (EXPIRED, 1 phần) — tổng 6 REQ / 9 SC còn thật sự Blocked.
- **REQ resolved từ Clarification cũ:** REQ-SENDER-001 (C-SENDER-1), REQ-CARRIER-004/005 (C-CARRIER-1/2) — nay đã có REQ/SC con cháu tương ứng (OFFER/CANCEL/GIFT), VÀ đã unblock UI (2026-07-27).
- **(Mốc cập nhật 2026-07-24):** tích hợp BRD v3.1 (DOC-v1.0-02): +18 REQ, +20 SC; resolve 3 clarification cũ; +2 clarification mới (C-ORDER-2, C-GENERAL-2 BLOCKER).
- **(Mốc cập nhật 2026-07-27):** tích hợp DOC-v1.0-03 (prototype cập nhật, verify Chrome MCP + đối chiếu Figma gốc): +3 REQ/SC mới (GENERAL bottom nav, GIFT xem lịch sử quà, NOTIFICATION đánh dấu đã đọc); unblock OFFER/CANCEL/GIFT/NOTIFICATION; resolve C-GIFT-2 (Figma xác nhận màn "Quà đã nhận" thuộc Carrier); tái khẳng định C-GENERAL-2; +1 clarification mới C-GENERAL-3 (Open — tier/điểm uy tín/điểm ECO mâu thuẫn BRD).
- **(Mốc cập nhật 2026-07-27, lần 2):** bổ sung field-level detail cho Trang chủ (REQ-GENERAL-003) + Bảng tin/Chi tiết tin (REQ-CARRIER-006) theo yêu cầu user, chuẩn bị generate-tc theo sheet-by-tab. +2 REQ, +4 SC (SC-GENERAL-003/004, SC-CARRIER-008/009) — 2 trong số đó (SC-GENERAL-004 empty state, SC-CARRIER-009 ảnh vắng mặt) có Expected Result "chưa xác định" vì chưa quan sát được trong demo (dữ liệu mẫu luôn có sẵn) — không đoán, cần vibe-test xác nhận.

## 3. Clarifications — Source Quote (ambiguous text)

> Trích nguyên văn đoạn mơ hồ per clarification (quoting-guide EC6). Tóm tắt + status: xem `MEMORY.md §6`.

#### C-SENDER-1 — Nhánh "Tôi nhận giao hàng" chưa implement (RESOLVED scope / 🔓 Unblocked test 2026-07-27)
**Source Quote (ambiguous, gốc):**
> "Nhánh "Tôi nhận giao hàng" (Carrier tự đăng tin rảnh rỗi, hiển thị "Chỉ hiển thị cho người đăng tin xem", hệ thống match rồi noti — Figma connector 89:117, 89:132, 90:149, 90:157) **chưa được implement** trong bản HTML prototype này"

**Source Location:** `DOC-v1.0-01 §1.1 "Chọn vai trò" · paragraph "Known gap vs Figma"`
**Analyst Note:** Cần BA/PO xác nhận nhánh này có trong scope v1.0 (chờ dev) hay defer version sau. Không chặn test các nhánh đã có UI.

**Resolution Quote (2026-07-24, DOC-v1.0-02):**
> "Là Carrier đang có nhu cầu di chuyển, tôi muốn đăng tin "Tôi nhận giao hàng" với điểm xuất phát, điểm đến, khung giờ và tên/SĐT..." (US-D10, `DOC-v1.0-02 §D1b`)

**Resolution Note:** CÓ trong scope chính thức — đã tạo module OFFER (REQ-OFFER-001..004/SC-OFFER-001..004). **Unblocked 2026-07-27:** verify qua Chrome MCP trên DOC-v1.0-03 — form đăng OFFER 1 màn đầy đủ field (điểm xuất phát/đến, khoảng ngày, khung giờ di chuyển, tên/SĐT, checkbox điều khoản) khớp đúng US-D10. Sẵn sàng generate-tc.

#### C-CARRIER-1 — Nhánh "Huỷ đơn" chưa implement (RESOLVED scope / 🔓 Unblocked test 2026-07-27)
**Source Quote (ambiguous, gốc):**
> "Nhánh "Huỷ đơn" (mô tả trong Figma tại nhiều điểm: sau khi xem tin, sau khi đã ghép, sau khi đã lấy hàng...) **chưa có UI** trong bản HTML prototype."

**Source Location:** `DOC-v1.0-01 §2.5 "Hoàn thành" · paragraph "Known gap vs Figma" #1`
**Analyst Note:** Nghiệp vụ Huỷ đơn thường quan trọng trong app thực tế — cần xác nhận scope trước khi generate-tc phân bổ effort cho nhánh này ở version sau.

**Resolution Quote (2026-07-24, DOC-v1.0-02):**
> "popup huỷ bắt buộc nhập lý do (nút Xác nhận khoá tới khi có lý do); đơn huỷ ghi rõ ai huỷ... đồng bộ realtime cho cả 3 bên" (US-D16, `DOC-v1.0-02 §D1b`)

**Resolution Note:** CÓ trong scope, đặc tả rất chi tiết (CNL-01, BR-CNL-01, OPR-09/11). Đã tạo module CANCEL (REQ-CANCEL-001..004/SC-CANCEL-001..004). **Unblocked 2026-07-27:** verify qua Chrome MCP trên DOC-v1.0-03 — nút "Huỷ đơn" ở màn Theo dõi đơn (trạng thái Chờ ghép) mở popup "Huỷ đơn hàng" với textarea lý do bắt buộc, nút Xác nhận khoá tới khi có lý do — khớp đúng US-D16. Sẵn sàng generate-tc (SC-CANCEL-002/003/004 vẫn cần verify thêm khi thực thi TC thật — chưa bấm Xác nhận để giữ nguyên state demo).

#### C-CARRIER-2 — Nhánh "Tặng quà cảm ơn" chưa implement (RESOLVED scope / 🔓 Unblocked test 2026-07-27)
**Source Quote (ambiguous, gốc):**
> "Nhánh "Tặng quà cảm ơn cho người vận chuyển" sau khi hoàn thành (...) **chưa có UI** trong bản HTML prototype."

**Source Location:** `DOC-v1.0-01 §2.5 "Hoàn thành" · paragraph "Known gap vs Figma" #2`
**Analyst Note:** Tính năng retention/post-completion, không chặn happy-path chính. Out-of-scope v1.0 trừ khi BA xác nhận ngược lại.

**Resolution Quote (2026-07-24, DOC-v1.0-02):**
> "4 loại quà: bông hoa, ly cà phê, gấu bông, vương miện — biểu tượng phi vật chất" (`DOC-v1.0-02 §A7`)

**Resolution Note:** CÓ trong scope. Đã tạo module GIFT (REQ-GIFT-001..004/SC-GIFT-001..004). **Unblocked 2026-07-27:** verify qua Chrome MCP trên DOC-v1.0-03 — flow tặng quà chạy được đầy đủ (Hoạt động → Đơn của tôi → Đã hoàn thành → tap đơn → màn Tặng quà → chọn 1/4 quà → Xác nhận tặng quà). Lưu ý C-GENERAL-2 (mâu thuẫn rating, đã tái khẳng định KHÔNG rating) và C-GIFT-2 mới (màn "Quà đã nhận" — Figma xác nhận thuộc Carrier, DOC-v1.0-03 đang hiện nhầm ở Receiver).

#### C-SENDER-2 — Wizard không tạo listing độc lập (non-blocking, vẫn Open)
**Source Quote (ambiguous):**
> "Đơn đăng qua wizard **không** xuất hiện như tin mới độc lập trong feed "Tin mới" của Carrier/Receiver — ghi đè vào 1 order slot có sẵn trong store demo."

**Source Location:** `DOC-v1.0-01 §1.5 "Theo dõi đơn (Sender)" · paragraph "Known gap"`
**Analyst Note:** Đánh giá "không phải bug" là suy luận của analyst khi vibe-test, chưa xác nhận từ BA/dev — giữ Open để tránh giả định sai khi có backend multi-order thật.

#### C-ORDER-1 — Hành vi reset chưa rõ ràng với wizard form state (non-blocking, vẫn Open)
**Source Quote (ambiguous):**
> "nút toàn cục "↺ Chạy lại từ đầu" reset về `posted` ban đầu, KHÔNG xoá đơn vừa đăng qua wizard — cần verify lại kỹ hơn vì đã quan sát wizard giữ nguyên form data sau reset"

**Source Location:** `DOC-v1.0-01 §4 "ORDER STATUS MACHINE" · "Ràng buộc quan trọng" bullet 1`
**Analyst Note:** SC-ORDER-002 chỉ assert phần chắc chắn (status reset) — không assert wizard form state cho tới khi resolve.

#### C-ORDER-2 — Ngưỡng thời gian hết hạn tin (EXPIRED) chưa xác định (Resolved 2026-07-27)
**Source Quote (ambiguous):**
> "Quá hạn cấu hình mà chưa MATCHED → tự chuyển EXPIRED... [...] CÂU HỎI MỞ CHO BA: [...] **Hạn tin mặc định?**"

**Source Location:** `DOC-v1.0-02 §D1b US-D04` + `§D5 "Câu hỏi mở cho BA"`
**Analyst Note:** Chính BRD liệt kê đây là câu hỏi mở — không tự chọn con số ngưỡng để viết TC boundary.

**Resolution (user, 2026-07-27):** "sau khi qua hạn ngày Từ ngày khi tạo sẽ hết hạn tin" — ngưỡng KHÔNG phải duration cố định (không phải "24h kể từ tạo"), mà là mốc tuyệt đối = giá trị field "Từ ngày" (chọn ở wizard bước 2). Qua mốc này mà chưa MATCHED → EXPIRED. Vẫn 🚫 Blocked cho TC thật (chờ UI/worker), nhưng business rule đã rõ để viết TC boundary khi implement.

#### C-GENERAL-2 — Mâu thuẫn nội bộ: có rating sao hay không? (Resolved 2026-07-27)
**Source Quote (ambiguous, mâu thuẫn nhau trong cùng tài liệu):**
> Đoạn 1 (§A7): "Không tính điểm, không tier/xếp hạng, không CO₂, không quy đổi tiền / thanh toán in-app"
> Đoạn 2 (§A5 BR-INT-06): "Không đánh giá sao; ghi nhận thiện chí bằng quà ảo..."
> Đoạn 3 (§D2): "[HOÀN TẤT] Đánh giá 2 chiều → ... → CO₂ + điểm → COMPLETED"
> Đoạn 4 (§D3): "RAT-01/02 Đánh giá 2 chiều — 1–5 sao + nhận xét"

**Source Location:** `DOC-v1.0-02 §A5 BR-INT-06`, `§A7`, `§D2 "Workflow & Status Flow"`, `§D3 RAT-01/02`
**Analyst Note:** Mâu thuẫn nội bộ THẬT trong chính BRD (§A vs §D2/D3), không phải hiểu nhầm của analyst. **BLOCKER** cho TC ở bước ngay sau "Hoàn thành" (SC-RECEIVER-003 mở rộng, SC-GIFT-002) — không viết TC cho bước rating cho tới khi BA xác nhận model đúng.

**Resolution (user, 2026-07-27, LẦN 1):** "không rating sao" — model chính thức = §A7/§A5 BR-INT-06, quà ảo (GIFT) thay thế hoàn toàn rating. §D2/§D3 (Đánh giá 2 chiều 1-5 sao) là spec cũ, KHÔNG implement/test. TC ngay sau "Hoàn thành" chỉ theo luồng GIFT.

**Addendum + Tái xác nhận (2026-07-27, LẦN 2):** DOC-v1.0-03 (prototype cập nhật) lại hiện UI rating thật — order card "Đã hoàn thành" có 5 sao cam + nhãn "Đã đánh giá", notification "Bạn nhận được đánh giá 5 sao". User xem bằng chứng này và tái xác nhận: "rating k ton tai, chi co gift thoi, trong figma cung k co rating dau" (rating không tồn tại, chỉ có gift; Figma gốc cũng không có rating). → UI 5-sao trong DOC-v1.0-03 là **known prototype inconsistency**, KHÔNG phải căn cứ đảo ngược quyết định. generate-tc giữ nguyên: không viết TC cho rating.

#### C-GENERAL-3 — Tier/điểm uy tín/điểm ECO trong UI mâu thuẫn BRD §A7 (Open, mới 2026-07-27)
**Source Quote (mâu thuẫn):**
> BRD: "Không tính điểm, không tier/xếp hạng, không CO₂, không quy đổi tiền / thanh toán in-app" (`DOC-v1.0-02 §A7`)
> UI quan sát (DOC-v1.0-03): màn "Cá nhân" (Carrier) hiển thị badge "Hạng Đồng hành", chỉ số "điểm uy tín" (vd 4.8), "điểm ECO" (vd 540)

**Source Location:** `DOC-v1.0-02 §A7` vs `DOC-v1.0-03` (quan sát UI trực tiếp, không có §section)
**Analyst Note:** Cùng loại mâu thuẫn UI-vs-BRD như C-GENERAL-2 (rating), nhưng KHÁC ở chỗ: chưa được user re-confirm trực tiếp — không tự suy ra là "prototype inconsistency" giống rating.

**Status:** Open — cần user/BA xác nhận: (a) cũng là UI lỗi thời cần bỏ (giống rating), hay (b) đây là phần thật sự có trong scope và BRD §A7 mới là phần chưa cập nhật. KHÔNG viết TC cho các field này cho tới khi có câu trả lời.

#### C-GIFT-2 — Vai trò hiển thị màn "Quà đã nhận" (Resolved qua Figma, 2026-07-27)
**Source Quote (mâu thuẫn quan sát):**
> DOC-v1.0-03: màn "Quà đã nhận" (lịch sử quà) xuất hiện ở phone gắn nhãn "NGƯỜI NHẬN" (Receiver, Phan Văn Hưng)
> Figma board gốc (`SEu9ekmu2wh1XxZCJkqAbP`, node 23:153, connector 94:255): "Note: màng hình này nằm ở menu Cá nhân \\ Quà đã nhận" — note này nằm trên hàng "NGƯỜI GIAO" (Carrier), ngay sau bước "mở thông báo nhận được quà"

**Source Location:** `DOC-v1.0-03` (quan sát UI) vs Figma board gốc node 23:153 (connector 94:255, section "NGƯỜI GIAO")
**Analyst Note:** Figma là nguồn thiết kế gốc, ghi rõ ràng màn này thuộc Carrier — bằng chứng đáng tin hơn cách DOC-v1.0-03 đang wiring.

**Resolution:** Màn "Quà đã nhận" thuộc về **Carrier's Cá nhân tab** (theo Figma) — DOC-v1.0-03 hiện màn này ở Receiver nhiều khả năng là lỗi wiring trong bản prototype, không phải chủ đích thiết kế. generate-tc viết TC với Precondition = Carrier's profile. Nếu vibe-test/execute trên UI thật vẫn thấy ở Receiver → log bug tham chiếu C-GIFT-2.
