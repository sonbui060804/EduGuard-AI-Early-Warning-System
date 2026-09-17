# EduGuard: Hệ thống Cảnh báo Sớm và Tư vấn Học tập dựa trên AI cho Sinh viên

## Bản dự thảo Báo cáo 1 đã chỉnh sửa - Tuần 1-2

> **Trạng thái tài liệu.** Đây là bản dự thảo ở tuần 1-2. Tài liệu ghi nhận định nghĩa bài toán, tổng quan tài liệu, khoảng trống nghiên cứu, mục tiêu, phạm vi, yêu cầu dữ liệu và phương pháp dự kiến. Các chỉ số mô hình, độ ổn định giải thích, kết quả công bằng, hiệu quả triển khai và kết quả actionable recourse chỉ được khẳng định sau khi đã thực nghiệm và kiểm chứng.

## Tóm tắt

Các nền tảng học trực tuyến tạo ra nhiều dấu vết về mức độ tương tác, hoạt động đánh giá và quá trình tham gia khóa học của sinh viên. Những dữ liệu này mở ra khả năng phát hiện sớm sinh viên có nguy cơ trượt hoặc bỏ học. Tuy nhiên, một hệ thống cảnh báo sớm hữu ích không chỉ cần điểm dự báo cao. Hệ thống phải sử dụng đúng thông tin có sẵn tại thời điểm dự báo, phân biệt sinh viên còn có thể tiếp cận với sinh viên đã rút khỏi khóa học, cung cấp giải thích mà giảng viên có thể hiểu và hướng tới các hành động hỗ trợ khả thi.

Dự án đề xuất EduGuard, một khung cảnh báo sớm theo thời gian và có khả năng giải thích trên bộ dữ liệu Open University Learning Analytics Dataset (OULAD). Nghiên cứu dự kiến sử dụng dữ liệu nhân khẩu học, hành vi VLE, đăng ký và đánh giá tại sáu mốc tiến độ khóa học: 10%, 20%, 40%, 60%, 80% và 100%. Logistic Regression, Random Forest, XGBoost, LightGBM và mạng nơ-ron nhân tạo sẽ được so sánh bằng thiết kế đánh giá theo cấp sinh viên và chống rò rỉ. SHAP và LIME sẽ được nghiên cứu như các phương pháp giải thích hậu nghiệm; độ ổn định giải thích và các chiến lược xử lý mất cân bằng sẽ được kiểm tra thực nghiệm. Counterfactual actionable recourse hiện là hướng mở rộng dự kiến, chỉ được coi là đóng góp sau khi module được triển khai và kiểm chứng.

## 1. Giới thiệu và Bối cảnh

Môi trường học tập ảo ghi nhận các hoạt động như truy cập tài liệu, xem diễn đàn, nộp bài và tham gia các hoạt động học tập. Educational Data Mining và Learning Analytics sử dụng những dấu vết này để nghiên cứu kết quả học tập, trượt và rút khóa học. Tuy nhiên, sinh viên có thể giảm tương tác dần dần mà không được hỗ trợ cho đến khi kết quả gần như không thể thay đổi.

OULAD là bối cảnh phù hợp vì chứa thông tin sinh viên đã ẩn danh, đăng ký khóa học, clickstream VLE, kết quả đánh giá và siêu dữ liệu khóa học. Dự án sử dụng bộ dữ liệu này để nghiên cứu liệu một mô hình cảnh báo sớm có thể xác định nguy cơ tại nhiều thời điểm trong khóa học hay không, đồng thời phân biệt trung thực giữa dự báo kết quả cuối khóa và dự báo phục vụ can thiệp.

## 2. Động lực và Phát biểu Bài toán

Động lực của EduGuard có cả khía cạnh giáo dục và phương pháp luận. Về giáo dục, giảng viên cần biết sớm sinh viên nào cần chú ý khi vẫn còn thời gian hỗ trợ. Về phương pháp, bằng chứng cho một cảnh báo phải được đánh giá cẩn thận. Một mô hình đánh giá trên toàn bộ lượt ghi danh lịch sử có thể gặp bài toán dễ hơn khi một số sinh viên đã rút trước thời điểm dự báo. Kết quả đó có thể hữu ích cho phân loại kết quả cuối khóa, nhưng không nên tự động được hiểu là dự báo thành công đối với những sinh viên vẫn đang theo học.

Chỉ tối ưu độ chính xác cũng chưa đủ. Một điểm rủi ro dạng hộp đen không cho biết sinh viên bị gắn cờ vì không hoạt động, chưa nộp bài, kết quả đánh giá thấp hay nguyên nhân nào khác. Không có giải thích, giảng viên khó chọn biện pháp hỗ trợ phù hợp. Giải thích cũng cần được kiểm tra độ ổn định, vì thứ hạng đặc trưng thay đổi mạnh giữa các lần chạy sẽ làm giảm độ tin cậy.

Vì vậy, dự án xác định bài toán như sau: xây dựng hệ thống cảnh báo sớm nhị phân theo thời gian, chỉ sử dụng thông tin có sẵn trước hoặc tại mỗi mốc tiến độ khóa học. Hệ thống cần ngăn rò rỉ theo thời gian và theo sinh viên, so sánh cả quần thể đầy đủ và quần thể còn theo học, tạo giải thích dễ hiểu, đồng thời nghiên cứu khả năng chuyển giải thích thành khuyến nghị hỗ trợ khả thi.

## 3. Mục tiêu và Phạm vi Dự án

### 3.1 Mục tiêu Tổng quát

Mục tiêu tổng quát là thiết kế và đánh giá một khung cảnh báo sớm theo thời gian, có khả năng giải thích, nhằm phát hiện sinh viên có nguy cơ trượt hoặc rút khỏi khóa học trực tuyến. Ở tuần 1-2, mục tiêu này được thể hiện dưới dạng kế hoạch nghiên cứu và triển khai; các kết luận thực nghiệm sẽ được bổ sung sau khi hoàn thành các thí nghiệm tương ứng.

### 3.2 Mục tiêu Cụ thể

1. Đặc tả yêu cầu dữ liệu và cấp phân tích cho nghiên cứu trên OULAD.
2. Tích hợp bảy bảng quan hệ OULAD thành pipeline phân tích có thể tái lập.
3. Xây dựng đặc trưng nhân khẩu học, tương tác VLE, đăng ký và đánh giá tại nhiều mốc tiến độ.
4. So sánh năm nhóm mô hình học có giám sát bằng một quy trình đánh giá chung theo cấp sinh viên.
5. Xác định mốc sớm nhất mà dự báo đạt tiêu chí tin cậy đã định trước.
6. Đánh giá giải thích SHAP và LIME, đồng thời định nghĩa các chỉ số ổn định định lượng.
7. So sánh không tái lấy mẫu, class weighting, SMOTE và ADASYN như các điều kiện kiểm tra độ bền.
8. Tách đánh giá phân loại kết quả trên toàn bộ quần thể khỏi đánh giá can thiệp trên nhóm còn theo học.
9. Thiết kế và sau đó kiểm chứng counterfactual recourse có ràng buộc cho hỗ trợ giáo dục khả thi.

### 3.3 Câu hỏi Nghiên cứu

- **RQ1:** Ở mốc tiến độ nào dự báo nguy cơ đủ tin cậy và thuật toán nào tốt nhất trong quy trình đánh giá chung?
- **RQ2:** Giải thích SHAP và LIME nhất quán đến đâu giữa các seed, các mốc thời gian và các điều kiện huấn luyện?
- **RQ3:** Class weighting, SMOTE và ADASYN ảnh hưởng thế nào đến chỉ số dự báo và độ ổn định giải thích khi lớp at-risk chỉ mất cân bằng nhẹ?
- **RQ4:** Là hướng mở rộng dự kiến, counterfactual explanation có thể tạo ra gợi ý can thiệp khả thi cho sinh viên còn theo học hay không?

Ở giai đoạn hiện tại, RQ4 là hướng nghiên cứu dự kiến. Không nên trình bày RQ4 như một kết quả đã hoàn thành khi module, ràng buộc, kiểm thử và đánh giá chưa được thực hiện.

### 3.4 Đóng góp Dự kiến

Đóng góp dự kiến là một khung nghiên cứu tích hợp dự báo theo thời gian, giải thích, đánh giá theo quần thể và hỗ trợ can thiệp tiềm năng. Dự án hướng tới một so sánh có thể tái lập về mô hình và quyết định xử lý dữ liệu, thay vì khẳng định hiệu năng phổ quát.

### 3.5 Đóng góp Phương pháp

Đóng góp phương pháp dự kiến là thiết kế thực nghiệm chống rò rỉ. Thiết kế sẽ sử dụng tạo đặc trưng theo cutoff, chia dữ liệu cố định theo sinh viên, tiền xử lý chỉ trên dữ liệu huấn luyện, giữ cùng sinh viên test qua các mốc và báo cáo rõ quần thể đánh giá. Nghiên cứu cũng định nghĩa quy trình định lượng để so sánh độ ổn định giải thích và chiến lược xử lý mất cân bằng.

### 3.6 Đóng góp Theo Bối cảnh Thị trường

Bối cảnh ứng dụng là giáo dục đại học trực tuyến và kết hợp, nơi các cơ sở đào tạo đã thu thập dấu vết từ hệ thống quản lý học tập nhưng có thể thiếu một quy trình cảnh báo sớm dễ giải thích. EduGuard được thiết kế như một mô hình nghiên cứu có thể tham khảo trong bối cảnh này. Khả năng chuyển sang cơ sở, nền tảng hoặc quốc gia khác vẫn là giả thuyết cần kiểm chứng bên ngoài.

### 3.7 Đóng góp Thực tiễn

Sản phẩm thực tiễn dự kiến là một quy trình nguyên mẫu dựa trên bằng chứng cho giảng viên và bộ phận hỗ trợ học tập. Sau này quy trình có thể bao gồm điểm rủi ro theo checkpoint, giải thích và gợi ý hỗ trợ có ràng buộc. Ở giai đoạn hiện tại, dự án chưa khẳng định hệ thống có thể tự động quyết định thay sinh viên hoặc đã cải thiện kết quả đào tạo.

### 3.8 Phạm vi

**Bao gồm:**

- bảy bảng quan hệ OULAD và mối quan hệ đã đặc tả;
- một lượt ghi danh student-module-presentation là đơn vị phân tích;
- nhãn nhị phân `at_risk`, trong đó Fail và Withdrawn được gộp vào nhóm nguy cơ;
- sáu checkpoint dự kiến: 10%, 20%, 40%, 60%, 80% và 100%;
- đặc trưng nhân khẩu học, tương tác VLE, đăng ký và đánh giá;
- năm thuật toán học có giám sát;
- chia nhóm, tiền xử lý chỉ trên train, SHAP/LIME và so sánh mất cân bằng;
- hướng mở rộng counterfactual recourse.

**Loại trừ hoặc để sau:**

- tự động ra quyết định về sinh viên;
- can thiệp hoàn toàn tự động;
- khẳng định quan hệ nhân quả của can thiệp;
- dự báo điểm chi tiết;
- chứng nhận công bằng;
- khẳng định hiệu quả triển khai ngoài OULAD;
- chỉ số mô hình và chất lượng recourse trước khi hoàn thành thực nghiệm.

## 4. Tổng quan Nghiên cứu và Khoảng trống

### 4.1 Dự báo At-Risk trên OULAD

Adnan et al. [1] là tiền lệ quan trọng cho dự báo theo thời gian trên OULAD. Họ sử dụng đặc trưng tích lũy tại các mốc từ 20% đến 100% khóa học. EduGuard tiếp thu nguyên tắc checkpoint và đề xuất thêm mốc 10%. Khác biệt chính cần kiểm chứng là chia dữ liệu cố định theo sinh viên và báo cáo riêng toàn bộ quần thể với nhóm còn theo học.

Tomasevic et al. [2] so sánh các phương pháp học có giám sát trên tập con module DDD và cho thấy đặc trưng tương tác cùng kết quả đánh giá có giá trị hơn biến nhân khẩu học. Cách xử lý missing và chia ngẫu nhiên của họ là cơ sở để EduGuard coi việc chưa nộp bài là tín hiệu tiềm năng và kiểm soát trùng sinh viên giữa train và test.

Liu et al. [3] cho thấy giá trị của việc tổng hợp clickstream theo các khoảng thời gian. EduGuard kế thừa nguyên tắc nén đặc trưng nhưng đề xuất tính lại đặc trưng tại các checkpoint tương đối và không tự động loại bỏ sinh viên không có click.

### 4.2 XAI và Recourse

Gunasekara và Saarela [4] minh họa việc dùng SHAP và LIME cho dự báo giáo dục trên một tập con OULAD. Phần giải thích của họ chủ yếu mang tính định tính, tạo động lực cho việc đánh giá định lượng độ ổn định giữa các seed và checkpoint. Các nghiên cứu về counterfactual, gồm Wachter et al. [5], Mothilal et al. [6] và nghiên cứu liên quan OULAD của Tsiakmaki et al. [7], cho thấy actionable explanation là một hướng nghiên cứu phù hợp. Vì vậy, EduGuard không nên tuyên bố rằng counterfactual hoàn toàn chưa tồn tại; khoảng trống được đề xuất là tích hợp recourse với dự báo theo checkpoint, đánh giá kép theo quần thể, chia chống rò rỉ và đánh giá độ ổn định giải thích.

### 4.3 Research Gap Graph

Khoảng trống của dự án là khoảng trống tích hợp, không phải tuyên bố mọi thành phần đều mới.

| Nghiên cứu | Phạm vi OULAD | Theo thời gian | XAI | Ổn định định lượng | So sánh mất cân bằng | Recourse |
|---|---|---|---|---|---|---|
| Adnan et al. [1] | Toàn bộ OULAD | Có | Không | Chưa báo cáo | Gộp lớp | Không |
| Tomasevic et al. [2] | Tập con DDD | Một phần | Không | Chưa báo cáo | Chưa nêu | Không |
| Liu et al. [3] | Tập con clickstream | Tổng hợp theo thời gian | Không | Chưa báo cáo | Chưa nêu | Không |
| Gunasekara & Saarela [4] | Tập con ba module | Không trọng tâm | SHAP + LIME | Chủ yếu định tính | Không trọng tâm | Không |
| Tsiakmaki et al. [7] | Liên quan OULAD | Không trọng tâm | Counterfactual | Chưa báo cáo | Không trọng tâm | Có |
| **Đề xuất EduGuard** | **Toàn bộ OULAD** | **Sáu checkpoint** | **SHAP + LIME** | **Đánh giá định lượng dự kiến** | **So sánh có kiểm soát** | **Recourse có ràng buộc dự kiến** |

Khoảng trống được đề xuất là thiếu một quy trình nhất quán kết hợp dự báo theo thời gian, kiểm soát rò rỉ theo sinh viên, báo cáo kép theo quần thể, độ ổn định giải thích định lượng, phân tích mất cân bằng và recourse có ràng buộc giáo dục trên bối cảnh OULAD đầy đủ.

## 5. Yêu cầu Dữ liệu và Phương pháp Dự kiến

OULAD gồm bảy bảng quan hệ về thông tin sinh viên, đăng ký, hoạt động VLE, siêu dữ liệu VLE, bài nộp, siêu dữ liệu đánh giá và thông tin khóa học. Đơn vị phân tích dự kiến là một lượt ghi danh `(id_student, code_module, code_presentation)`.

Nhãn sẽ được tạo từ `final_result`: Fail và Withdrawn là at-risk, Pass và Distinction là not-at-risk. Định nghĩa này và tỷ lệ mất cân bằng nhẹ cần được kiểm tra từ dữ liệu thô trước khi mô hình hóa.

Đặc trưng sẽ gồm ba nhóm chính: nhân khẩu học và bối cảnh, tương tác VLE và kết quả đánh giá. Dữ liệu phụ thuộc thời gian sẽ được cắt tại checkpoint tương ứng để không đưa sự kiện sau thời điểm dự báo vào vector đặc trưng sớm hơn.

Đánh giá dự kiến dùng split cố định theo sinh viên. Tất cả bản ghi của cùng `id_student` sẽ nằm trong một partition. Xử lý missing, scale, encode, ngưỡng outlier và resampling chỉ được học hoặc áp dụng trong dữ liệu train. Các chỉ số chính dự kiến là recall và PR-AUC; F1, ROC-AUC, calibration và phân tích nhóm sẽ là chỉ số hỗ trợ.

## 6. Kế hoạch 10 Tuần

| Thời gian | Công việc dự kiến | Bằng chứng cần có |
|---|---|---|
| Tuần 1-2 | Xác định bài toán, tổng quan tài liệu, research graph, đặc tả dữ liệu, ethics và scope | Proposal, tài liệu tham khảo đã rà soát, yêu cầu dữ liệu |
| Tuần 3-4 | Kiểm tra dữ liệu thô, dựng master table, làm sạch, thiết kế checkpoint | Data dictionary, cleaning log, leakage tests |
| Tuần 5-6 | Pipeline đặc trưng baseline, split cố định, huấn luyện ban đầu | Chỉ số baseline và artifact tái lập |
| Tuần 7-8 | Cross-validation, threshold, SHAP/LIME, so sánh mất cân bằng | Bảng kết quả và phân tích giải thích |
| Tuần 9 | Prototype counterfactual recourse và tích hợp dashboard nếu khả thi | Ràng buộc recourse, test và output prototype |
| Tuần 10 | Chạy tái lập, chốt báo cáo, hình, tài liệu tham khảo và thuyết trình | Báo cáo cuối và gói nộp |

## Tài liệu tham khảo

[1] M. Adnan et al., “Predicting at-Risk Students at Different Percentages of Course Length for Early Intervention Using Machine Learning Models,” *IEEE Access*, vol. 9, pp. 7519-7539, 2021.

[2] N. Tomasevic, N. Gvozdenovic, and S. Vranes, “An Overview and Comparison of Supervised Data Mining Techniques for Student Exam Performance Prediction,” *Computers & Education*, vol. 143, art. 103676, 2020.

[3] Y. Liu et al., “Predicting Student Performance Using Clickstream Data and Machine Learning,” *Education Sciences*, vol. 13, no. 1, art. 17, 2023.

[4] S. Gunasekara and M. Saarela, “Explainable AI in Education: Techniques and Qualitative Assessment,” *Applied Sciences*, vol. 15, no. 3, art. 1239, 2025.

[5] S. Wachter, B. Mittelstadt, and C. Russell, “Counterfactual Explanations Without Opening the Black Box,” *Harvard Journal of Law & Technology*, vol. 31, no. 2, pp. 841-887, 2018.

[6] R. K. Mothilal, A. Sharma, and C. Tan, “Explaining Machine Learning Classifiers through Diverse Counterfactual Explanations,” in *Proceedings of the ACM Conference on Fairness, Accountability, and Transparency*, 2020, pp. 607-617.

[7] M. Tsiakmaki et al., “Counterfactual Explanations for Student Success Prediction: A Comparative Study on OULAD,” in *Proceedings of the Workshop on Explainability and Transparency in Educational AI*, CEUR-WS, 2023.
