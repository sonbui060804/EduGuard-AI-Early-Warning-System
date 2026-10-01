## Thay đổi phase 3:

Đã có một số thay đổi trong hệ thống (sửa lại để có thể chạy được DiCE), ae đọc qua nhé:

1. Sửa đường dẫn nạp dữ liệu bị sai (`dataset_t...`) để thiết lập kết nối logic xuyên suốt từ mốc 0% -> 100%.
2. DiCE trả về kết quả mảng `object` thay vì số thực, làm hỏng quá trình xử lý `np.log1p` kế tiếp (các số liệu trả về số thập phân, kiểu em phải đi học thêm 3.04 buổi nữa). Đã thiết kế một `EduGuardModelWrapper` để ép kiểu về số nguyên
3. Xử lý trường hợp "Không thể sinh phương án an toàn" khi sinh viên không thể cứu được nữa, in thông báo ra màn hình để giúp giảng viên trực tiếp xử lý.

---

## Giải thích ngắn gọn về Thuật toán DiCE

**DiCE** (Diverse Counterfactual Explanations) là một thuật toán thuộc nhóm XAI (Trí tuệ nhân tạo Xúc tích/ Giải thích được). Trái với nền tảng SHAP (chỉ ra nguyên nhân tại sao sinh viên có rủi ro), DiCE cung cấp hành động cụ thể bằng cách trả lời câu hỏi "What-If" (Nếu... thì).

**Cơ chế hoạt động:**
* **Tìm kiếm Phương án (Counterfactuals):** Nếu sinh viên A đang bị dự đoán Rớt (p > 50%), DiCE sẽ xáo trộn (perturb) các tham số hành vi của sinh viên (như tăng số lượt click, tăng điểm bài nộp...) để mô phỏng một "bản sao" của học sinh A. Nó liên tục thử và học cho đến khi cái bản sao đó được mô hình phân loại là **Qua môn (p < 50%)**.
* **Khoảng cách tối thiểu:** Nó ưu tiên những phương án thay đổi ít nhất (Khoảng cách ngắn nhất) so với thực tế, đảm bảo công sức sinh viên bỏ ra để lật ngược tình thế là thấp nhất có thể.
* **Đảm bảo tính đa dạng (Diversity):** DiCE cung cấp đồng thời nhiều phương án giải quyết bài toán cùng 1 lúc (ví dụ: cách 1 là nỗ lực bấm bài giảng, cách 2 là nỗ lực làm bù bài kiểm tra) để giảng viên có nhiều sự lựa chọn khi tư vấn.

---

## Cần làm tiếp theo

1. **Kiểm thử trên Toàn hệ thống (Automated Verification):**
   * Viết thêm Unit Test (kiểm thử đơn vị) để chạy thử nghiệm kịch bản DiCE ở tất cả các mốc `t={10, 20, 40, ...}` để đảm bảo không bị crash khi có dữ liệu format lạ.
2. **Triển khai phương pháp tối ưu hơn cho DiCE:** 
   * Tùy chọn `method="random"` hiện tại hoạt động khá nhanh trên Streamlit nhưng tối ưu chưa tốt, ngoài ra phương án DiCE có sự thay đổi với mỗi lần chạy mô hình (kết quả không cố định). Có thể thử cài đặt `method="genetic"` hoặc `kdtree`

---

## Cập nhật phân hệ Kế hoạch Sư phạm (1/10):

Hệ thống đã triển khai logic sư phạm thay vì các con số máy móc thuần túy từ thuật toán DiCE:
1. **Lọc sinh viên Ghost (t >= 40%):** Tự động phát hiện sinh viên đã bỏ học (truy cập = 0, hoặc Điểm = 0 + không nộp bài + không hoạt động > 30 ngày) để phát **Báo động đỏ**, yêu cầu giảng viên gọi điện thay vì đưa ra kịch bản DiCE vô nghĩa.
2. **Loại bỏ 3 kịch bản trùng lặp:** Hợp nhất kết quả từ DiCE thành một bộ **Khuyến nghị Hành động** duy nhất, gán theo mức Ưu tiên (Ưu tiên 1, 2) một cách tường minh, rất dễ sử dụng cho giảng viên.
3. **Tracking 3 "Core Goals" tĩnh:** Phân tách rõ Lần cuối hoạt động, Điểm tích lũy, và Số lần bỏ nộp bài thành 3 ô Metrics dễ quan sát, kèm theo hiệu ứng định hướng (màu Xanh khi âm số bài chưa nộp/ ngày ko hoạt động).
