# EduGuard: Hệ thống Cảnh báo Sớm và Tư vấn Học tập Tự động dựa trên AI

**AI1909 - ADS | Nhóm 2**  
**Báo cáo 1: Kế hoạch nghiên cứu và triển khai Tuần 1-2**

> **Trạng thái báo cáo:** Đây là kế hoạch nghiên cứu và triển khai. Các nội dung dưới đây mô tả những phân tích dự kiến, trừ khi được ghi rõ là phát hiện của dự án.

## Tóm tắt

Môi trường học tập trực tuyến (Virtual Learning Environment - VLE) ghi nhận các hoạt động như mở tài liệu, truy cập diễn đàn, nộp bài đánh giá và tham gia các hoạt động của học phần. Những dữ liệu này được sử dụng trong Khai phá Dữ liệu Giáo dục và Phân tích Học tập để nghiên cứu kết quả học tập và tình trạng rút lui. Vì mức độ tham gia của sinh viên có thể giảm dần theo thời gian, thông tin sớm có thể giúp giảng viên hỗ trợ khi vẫn còn khả năng can thiệp.

Bộ dữ liệu Open University Learning Analytics Dataset (OULAD) phù hợp với dự án vì chứa thông tin sinh viên đã ẩn danh, thông tin đăng ký, hoạt động VLE, kết quả đánh giá và thông tin học phần. EduGuard sẽ nghiên cứu khả năng nhận diện sinh viên có nguy cơ tại các thời điểm khác nhau trong khóa học. Dự án phân biệt giữa việc dự đoán kết quả cuối khóa và việc nhận diện những sinh viên vẫn còn có thể nhận hỗ trợ tại thời điểm dự đoán.

## 1. Động lực và Phát biểu Bài toán

Giảng viên cần thông tin kịp thời về những sinh viên có thể cần hỗ trợ. Thông tin này chỉ hữu ích nếu có được khi vẫn còn thời gian phản hồi. Vì vậy, mô hình cần được đánh giá cẩn thận. Một mô hình được đánh giá trên những sinh viên đã rút lui có thể hữu ích cho việc dự đoán kết quả cuối khóa, nhưng cách đánh giá đó không trả lời câu hỏi vận hành về việc nhận diện những sinh viên vẫn đang theo học và có thể nhận hỗ trợ.

Chỉ số accuracy cũng chưa đủ. Điểm rủi ro không giải thích sinh viên bị gắn cờ vì không hoạt động, chưa hoàn thành bài, điểm đánh giá thấp hay yếu tố khác. Nếu thiếu thông tin này, giảng viên có thể không biết nên áp dụng loại hỗ trợ nào. Do đó, EduGuard sẽ đánh giá độ ổn định của giải thích, vì các giải thích thay đổi đáng kể giữa các lần huấn luyện hoặc lựa chọn mô hình có thể khó được tin cậy.

Dự án sẽ xây dựng một hệ thống cảnh báo sớm nhị phân, có xét thời gian, chỉ sử dụng thông tin có sẵn đến từng checkpoint. Pipeline sẽ xử lý rò rỉ theo thời gian và rò rỉ theo sinh viên. Kết quả sẽ được báo cáo cho cả nhóm đánh giá đầy đủ và nhóm còn đang hoạt động tại checkpoint. Dự án cũng nghiên cứu liệu giải thích của mô hình có thể liên kết với các khuyến nghị hỗ trợ khả thi hay không.

## 2. Công trình Liên quan và Khoảng trống Nghiên cứu

### 2.1 Dự đoán Rủi ro và Mô hình hóa theo Thời gian

Kuzilek, Hlosta và Zdrahal giới thiệu OULAD, gồm bảy bảng liên quan và 32.593 bản ghi đăng ký sinh viên-học phần-lần mở học phần trên 22 module presentations [1]. Dữ liệu bao gồm thông tin nhân khẩu học, hoạt động VLE, kết quả đánh giá và thông tin học phần. Dữ liệu phát hành đã được ẩn danh.

Tomasevic và cộng sự so sánh các phương pháp học có giám sát để dự đoán kết quả thi trên một tập con của OULAD. Nghiên cứu sử dụng hai lần mở học phần DDD và 3.166 sinh viên sau khi loại các sinh viên không có kết quả thi [3]. Kết quả cho thấy việc kết hợp hoạt động VLE với điểm đánh giá có thể hữu ích. So sánh đó chưa bao gồm đầy đủ nhóm mô hình gradient boosting dự kiến sử dụng trong dự án này.

Adnan và cộng sự nghiên cứu dự đoán tại nhiều tỷ lệ độ dài khóa học, sử dụng đặc trưng tích lũy tại các mốc 0%, 20%, 40%, 60%, 80% và 100% [2]. Đánh giá sử dụng accuracy, precision, recall, F-score và AUC. Kết quả này là cơ sở cho việc sử dụng các checkpoint theo thời gian trong dự án, trong đó bổ sung checkpoint 10%. Nghiên cứu gộp Pass với Distinction và Fail với Withdrawn thay vì xử lý bốn kết quả cuối khóa như bốn lớp riêng biệt.

Một yêu cầu phương pháp quan trọng của EduGuard là chia dữ liệu theo mã định danh sinh viên. Một lần đăng ký có thể chứa các quan sát lặp lại hoặc nhiều lần mở học phần, vì vậy chia ngẫu nhiên theo dòng có thể khiến thông tin của cùng một sinh viên xuất hiện ở cả tập huấn luyện và kiểm tra. Dự án sẽ sử dụng một phép chia theo sinh viên được cố định và ghi lại rõ quy trình chia.

### 2.2 AI Có thể Giải thích trong Dự đoán Giáo dục

SHAP và LIME thường được sử dụng để giải thích các dự đoán của mô hình học máy [4], [5]. SHAP có thể mô tả đóng góp của đặc trưng trên toàn bộ dữ liệu và ở từng dự đoán. LIME giải thích một dự đoán bằng cách xây dựng một mô hình cục bộ đơn giản quanh trường hợp đó. Kết quả của hai phương pháp có thể phụ thuộc vào việc lấy mẫu, quá trình huấn luyện mô hình và lát dữ liệu được chọn.

Các nghiên cứu giáo dục trước đây thường đánh giá giải thích thông qua biểu đồ tầm quan trọng của đặc trưng hoặc thảo luận định tính [4], [5]. EduGuard sẽ bổ sung việc quan sát trực quan bằng các thước đo ổn định định lượng. Phân tích sẽ kiểm tra liệu các đặc trưng quan trọng có giữ được mức tương đồng khi huấn luyện lại mô hình, thay đổi checkpoint hoặc thay đổi phương pháp xử lý mất cân bằng hay không.

### 2.3 Xử lý Mất Cân bằng Lớp

SMOTE tạo các quan sát tổng hợp cho lớp thiểu số từ các quan sát hiện có. ADASYN tạo nhiều quan sát hơn tại những vùng khó phân loại. Class weighting thay đổi mức phạt tương đối của các lỗi mà không thêm dòng tổng hợp.

Theo cách ánh xạ nhãn của dự án, `at_risk = 1` đại diện cho Fail hoặc Withdrawn, còn `at_risk = 0` đại diện cho Pass hoặc Distinction. Trong dữ liệu OULAD hiện tại, các lượt đăng ký at-risk chiếm 17.208 trên tổng số 32.593 lượt, tương đương khoảng 52,8%. Vì vậy, at-risk là lớp đa số nhẹ chứ không phải lớp thiểu số hiếm. So sánh SMOTE, ADASYN và class weighting do đó là thí nghiệm về độ bền, không phải tuyên bố rằng cần khôi phục một lớp at-risk bị thiếu nghiêm trọng.

Vì bỏ sót một sinh viên at-risk có ý nghĩa quan trọng về vận hành, recall của lớp at-risk và PR-AUC sẽ được báo cáo cùng precision, F1, ROC-AUC, độ hiệu chuẩn và ma trận nhầm lẫn. Mọi phương pháp resampling chỉ được áp dụng bên trong các fold huấn luyện, không áp dụng cho dữ liệu validation hoặc test.

### 2.4 Khoảng trống Nghiên cứu

Nhóm đã sàng lọc 30 tài liệu và giữ lại 27 bài độc lập sau khi loại trùng lặp. Bảng dưới đây tóm tắt các bằng chứng liên quan nhất. Danh sách sàng lọc đầy đủ, tiêu chí đưa vào và bảng liên kết giữa từng bài với các nhận định cần được đưa vào phụ lục literature review của báo cáo cuối.

| Lĩnh vực nghiên cứu | Bằng chứng được xem xét | Hạn chế được nhận diện | Phản hồi của EduGuard |
|---|---|---|---|
| Dự đoán kết quả trên OULAD | Kuzilek et al. [1]; Tomasevic et al. [3] | Khác biệt về tập đặc trưng và so sánh mô hình làm cho việc đối chiếu trực tiếp khó khăn | Sử dụng pipeline đặc trưng có thể tái lập và một quy trình đánh giá thống nhất |
| Dự đoán theo thời gian | Adnan et al. [2] | Chất lượng dự đoán thay đổi theo tiến độ khóa học; kết quả trên sinh viên còn hoạt động có thể khác nhóm đầy đủ | Đánh giá checkpoint từ 10% đến 100% và báo cáo hai nhóm đối tượng |
| AI có thể giải thích trong giáo dục | Gunasekara và Saarela [4]; Alamri và Alharbi [5] | Độ tốt của giải thích thường chủ yếu được đánh giá bằng biểu đồ hoặc thảo luận định tính | Đo mức đồng thuận thứ hạng và độ biến thiên qua seed, checkpoint và phương pháp mất cân bằng |
| Xử lý mất cân bằng lớp | Các nghiên cứu về SMOTE, ADASYN và class weighting | Tác động đến độ ổn định của giải thích chưa được đo nhất quán | So sánh không resampling, class weighting, SMOTE và ADASYN |
| Giải thích phản thực tế | Wachter et al. [6]; Mothilal et al. [7] và các công trình giáo dục được xác định trong quá trình tổng quan | Một phản thực tế hợp lệ về mặt toán học có thể không khả thi về mặt sư phạm | Ràng buộc recourse theo tính có thể tác động, tính bất biến, tính khả thi và chi phí |

Dự án sẽ kết hợp dự đoán theo thời gian với XAI trên OULAD, so sánh mô hình mạng nơ-ron và mô hình ensemble, đồng thời đo độ ổn định của giải thích. Dự án cũng nghiên cứu liệu lựa chọn phương pháp xử lý mất cân bằng có ảnh hưởng đến cả chỉ số dự đoán và giải thích hay không. Counterfactual recourse là phần mở rộng dự kiến và sẽ không được trình bày như một đóng góp đã hoàn thành cho đến khi các ràng buộc và đánh giá được triển khai.

## 3. Mục tiêu của Dự án

### 3.1 Mục tiêu Tổng quát

Mục tiêu tổng quát là thiết kế và đánh giá một framework cảnh báo sớm theo thời gian để nhận diện sinh viên có thể trượt hoặc rút lui khỏi một khóa học trực tuyến. Ở giai đoạn Tuần 1-2, mục tiêu này được trình bày dưới dạng kế hoạch nghiên cứu và triển khai; kết quả sẽ được bổ sung sau khi hoàn thành thí nghiệm.

### 3.2 Mục tiêu Cụ thể

1. Xác định yêu cầu dữ liệu và đơn vị phân tích cho nghiên cứu OULAD.
2. Kết hợp bảy bảng OULAD trong một pipeline dữ liệu có thể tái lập.
3. Tạo đặc trưng nhân khẩu học, tham gia học tập, đăng ký và đánh giá tại nhiều checkpoint theo tiến độ khóa học.
4. So sánh năm nhóm mô hình học có giám sát trong cùng quy trình đánh giá theo sinh viên: Logistic Regression, Random Forest, XGBoost, LightGBM và mạng nơ-ron nhân tạo được triển khai bằng bộ phân loại MLP.
5. Xác định checkpoint sớm nhất đạt tiêu chí độ tin cậy được định trước.
6. Thử nghiệm SHAP và LIME, đồng thời định nghĩa các thước đo định lượng cho độ ổn định của giải thích.
7. So sánh không resampling, class weighting, SMOTE và ADASYN, trong đó resampling chỉ được thực hiện trên các fold huấn luyện.
8. Báo cáo riêng kết quả cho tất cả lượt đăng ký đủ điều kiện và cho sinh viên còn hoạt động tại checkpoint.
9. Thiết kế và đánh giá về sau cơ chế counterfactual recourse cho các hình thức hỗ trợ giáo dục khả thi.

### 3.3 Câu hỏi Nghiên cứu

**RQ1.** Tại các checkpoint 10%, 20%, 40%, 60%, 80% và 100% của tiến độ khóa học, thuật toán nào cho kết quả dự đoán at-risk tốt nhất trên OULAD, và checkpoint nào là checkpoint đầu tiên đạt tiêu chí độ tin cậy đã định trước?

**RQ2.** Các giải thích SHAP và LIME cho cùng một mô hình nhất quán đến mức nào, và độ ổn định của giải thích thay đổi ra sao theo checkpoint và phương pháp xử lý mất cân bằng?

**RQ3.** Việc xử lý mất cân bằng, bao gồm SMOTE, ADASYN và class weighting, ảnh hưởng như thế nào đến hiệu năng dự đoán và độ ổn định của giải thích?

**RQ4.** Các giải thích phản thực tế có ràng buộc có thể tạo ra kế hoạch hỗ trợ tối thiểu và khả thi cho sinh viên at-risk hay không, và mức effort cần thiết cho recourse thay đổi thế nào theo các checkpoint?

RQ4 là hướng nghiên cứu dự kiến ở giai đoạn hiện tại. Không được trình bày RQ4 như một kết quả đã hoàn thành cho đến khi module recourse, các ràng buộc về khả năng tác động, kiểm thử tính hợp lệ và đánh giá đã được thực hiện.

### 3.4 Định nghĩa Vận hành

- **Lượt đăng ký:** một bản ghi sinh viên-module presentation, là đơn vị phân tích chính.
- **Checkpoint:** một tỷ lệ phần trăm của độ dài khóa học tương ứng. Chỉ các đặc trưng có sẵn tại hoặc trước thời điểm đó mới được sử dụng.
- **Nhóm đầy đủ:** tất cả lượt đăng ký đủ điều kiện đánh giá tại checkpoint tương ứng, bao gồm cả những lượt đăng ký có kết quả cuối khóa được quan sát về sau.
- **Nhóm còn hoạt động tại checkpoint:** các lượt đăng ký của sinh viên chưa rút lui trước checkpoint, theo quy tắc hoạt động và kết quả được dự án công bố. Phần triển khai cuối cùng phải nêu chính xác quy tắc này và bảo đảm không sử dụng thông tin sau checkpoint.
- **Checkpoint đáng tin cậy:** checkpoint sớm nhất thỏa mãn tiêu chí được cố định trước khi đánh giá test cuối cùng. Tiêu chí cần nêu metric mục tiêu, ngưỡng tối thiểu và quy tắc bất định; ví dụ recall đạt ít nhất ngưỡng do dự án quy định với khoảng tin cậy bootstrap không thấp hơn ngưỡng đó.
- **Đặc trưng có thể tác động:** đặc trưng mà giảng viên hoặc sinh viên có thể tác động một cách hợp lý trong thời gian can thiệp. Các thuộc tính bất biến như tuổi và giới tính sẽ không bị thay đổi khi tạo recourse.

## 4. Cấu trúc Luận văn

Báo cáo cuối sẽ được tổ chức thành sáu phần chính:

1. **Giới thiệu và tổng quan tài liệu:** động lực giáo dục, câu hỏi nghiên cứu và đóng góp dự kiến.
2. **Công trình liên quan:** dự đoán trên OULAD, phân tích học tập theo thời gian, XAI, mất cân bằng lớp và actionable recourse.
3. **Dữ liệu và phương pháp:** OULAD, định nghĩa nhãn mục tiêu, tạo đặc trưng, checkpoint, phòng chống leakage, chia theo sinh viên, cross-validation và tiền xử lý.
4. **So sánh mô hình và dự đoán theo thời gian:** kết quả RQ1, phân tích độ tin cậy và so sánh hai nhóm đánh giá.
5. **Mất cân bằng và độ ổn định của giải thích:** ảnh hưởng của các chiến lược mất cân bằng và độ ổn định SHAP/LIME cho RQ2 và RQ3.
6. **Thảo luận và kết luận:** hạn chế, phát hiện, cân nhắc triển khai, khuyến nghị giám sát và hướng phát triển, bao gồm đánh giá trên các cơ sở khác và counterfactual recourse có ràng buộc.

## Tài liệu tham khảo

[1] J. Kuzilek, M. Hlosta, and Z. Zdrahal, “Open University Learning Analytics Dataset,” *Scientific Data*, 2017.

[2] M. Adnan et al., “Predicting at-Risk Students at Different Percentages of Course Length for Early Intervention Using Machine Learning Models,” *IEEE Access*, vol. 9, pp. 7519-7539, 2021.

[3] N. Tomasevic, N. Gvozdenovic, and S. Vranes, “An Overview and Comparison of Supervised Data Mining Techniques for Student Exam Performance Prediction,” *Computers & Education*, vol. 143, art. 103676, 2020.

[4] S. Gunasekara and M. Saarela, “Explainable AI in Education: Techniques and Qualitative Assessment,” *Applied Sciences*, vol. 15, no. 3, art. 1239, 2025.

[5] A. Alamri and A. Alharbi, “Explainable Student Performance Prediction: A Systematic Review,” *IEEE Access*, 2021.

[6] S. Wachter, B. Mittelstadt, and C. Russell, “Counterfactual Explanations without Opening the Black Box: Automated Decisions and the GDPR,” *Harvard Journal of Law & Technology*, vol. 31, no. 2, pp. 841-887, 2018.

[7] R. K. Mothilal, A. Sharma, and C. Tan, “Explaining Machine Learning Classifiers through Diverse Counterfactual Explanations,” in *Proceedings of the ACM Conference on Fairness, Accountability, and Transparency*, 2020, pp. 607-617.

> **Lưu ý về việc hoàn thiện tài liệu tham khảo:** Bản nộp cuối phải bổ sung đầy đủ các mục thư mục cho các nghiên cứu về counterfactual trong giáo dục, dropout/survival analysis và clickstream theo thời gian được sử dụng trong tổng quan 27 bài. Mô tả một chủ đề không phải là một tài liệu tham khảo hợp lệ. Mỗi mục cần có tác giả, tên bài, nơi xuất bản, năm, volume/trang hoặc article number, và DOI hoặc URL ổn định nếu có.

## Đánh giá Bản sửa

### Các thay đổi đã thực hiện

- Chuyển báo cáo thành bản Markdown có thể tái lập, đồng thời giữ nguyên DOCX gốc.
- Thêm trạng thái báo cáo rõ ràng để không nhầm lẫn giữa kế hoạch và kết quả đã hoàn thành.
- Thay hình ảnh Research Gap bằng bảng Markdown có thể tìm kiếm và sao chép.
- Định nghĩa đơn vị đăng ký, checkpoint, nhóm đầy đủ, nhóm còn hoạt động tại checkpoint, tiêu chí độ tin cậy và đặc trưng có thể tác động.
- Liệt kê rõ năm nhóm mô hình dự kiến.
- Làm rõ at-risk là lớp đa số nhẹ theo cách ánh xạ nhãn hiện tại và resampling là thí nghiệm về độ bền.
- Bổ sung yêu cầu chỉ resampling bên trong các fold huấn luyện.
- Thay các cách diễn đạt tuyệt đối như “chưa từng được nghiên cứu” bằng cách diễn đạt có giới hạn theo bằng chứng.
- Loại các tài liệu tham khảo dạng placeholder khỏi danh mục đánh số và ghi rõ phần thư mục còn phải hoàn thiện.
- Thêm một hạn chế trung thực: tuyên bố đã rà 30 tài liệu và 27 bài độc lập vẫn cần bảng sàng lọc hoặc phụ lục để kiểm chứng.

### Đánh giá sau khi sửa

**Đã cải thiện:** Báo cáo hiện rõ ràng, dễ kiểm tra và ít overclaim hơn. Các câu hỏi nghiên cứu đã gắn với quy trình đo lường cụ thể, đồng thời phân biệt rõ dự đoán kết quả cuối khóa với can thiệp cho sinh viên còn hoạt động.

**Cần hoàn thiện trước khi nộp:**

1. Hoàn thiện thư mục đầy đủ của 27 bài và cung cấp phụ lục sàng lọc/map bằng chứng.
2. Kiểm tra mọi thông tin thư mục, đặc biệt là tác giả, năm xuất bản, tên bài, DOI và số trang hoặc article number.
3. Chốt quy tắc xác định nhóm còn hoạt động tại checkpoint trong phần phương pháp và bảo đảm quy tắc này không sử dụng thông tin sau checkpoint.
4. Xác định trước ngưỡng độ tin cậy, metric mục tiêu, phương pháp tính khoảng tin cậy và quy tắc chọn mô hình.
5. Bổ sung citation cuối cùng cho các nghiên cứu counterfactual và dự đoán theo thời gian trong giáo dục thay vì để dưới dạng mô tả chủ đề.

**Đánh giá tổng thể:** Phù hợp để sử dụng như bản dự thảo kế hoạch nghiên cứu Tuần 1-2 đã chỉnh sửa. Chưa nên xem là bản tổng quan tài liệu cuối cùng cho đến khi hoàn thành các yêu cầu về tài liệu tham khảo và khả năng truy nguyên bằng chứng nêu trên.
