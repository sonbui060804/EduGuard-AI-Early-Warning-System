# CÃ¡c nghiÃªn cá»©u ná»n: Äá»‘i chiáº¿u quy trÃ¬nh tiá»n xá»­ lÃ½ OULAD

**Phá»¥ Ä‘á»:** So sÃ¡nh thu tháº­p, lÃ m sáº¡ch, táº¡o Ä‘áº·c trÆ°ng vÃ  phÃ¢n chia dá»¯ liá»‡u giá»¯a bá»‘n nghiÃªn cá»©u ná»n Ä‘á»ƒ láº­p luáº­n cho cÃ¡c lá»±a chá»n cá»§a nhÃ³m.

**DSP391m â€“ NhÃ³m 5 Â· BÃ¡o cÃ¡o 2 (TÃ¡c vá»¥ dá»¯ liá»‡u), ChÆ°Æ¡ng 3 Â· Háº¡ng má»¥c STT 24 (Vinh)**

---

> **Ghi chÃº kiá»ƒm chá»©ng.** CÃ¡c Ã´ dÆ°á»›i Ä‘Ã¢y Ä‘Ã£ Ä‘Æ°á»£c Ä‘á»‘i chiáº¿u vá»›i báº£n gá»‘c: toÃ n vÄƒn cho [1], [2] vÃ  [4]; pháº§n tÃ³m táº¯t cÃ¹ng cÃ¡c bÃ i trÃ­ch dáº«n Ä‘á»™c láº­p cho [5] (toÃ n vÄƒn nhÃ  xuáº¥t báº£n bá»‹ giá»›i háº¡n). Nhá»¯ng Ã´ nguá»“n khÃ´ng nÃªu rÃµ Ä‘Æ°á»£c Ä‘Ã¡nh dáº¥u *"khÃ´ng nÃªu rÃµ"* thay vÃ¬ suy Ä‘oÃ¡n.

---

## 1. Giá»›i thiá»‡u

Bá»™ dá»¯ liá»‡u Open University Learning Analytics Dataset (OULAD) â€” mÃ´ táº£ bá»Ÿi Kuzilek vÃ  cá»™ng sá»± [3] â€” gá»“m báº£y báº£ng quan há»‡ bao phá»§ 32.593 lÆ°á»£t Ä‘Äƒng kÃ½ sinh viÃªn, gá»“m há»“ sÆ¡ nhÃ¢n kháº©u há»c, tÆ°Æ¡ng tÃ¡c clickstream trÃªn mÃ´i trÆ°á»ng há»c áº£o (VLE) vÃ  káº¿t quáº£ Ä‘Ã¡nh giÃ¡. VÃ¬ nhiá»u nhÃ³m nghiÃªn cá»©u Ä‘Ã£ dÃ¹ng bá»™ dá»¯ liá»‡u nÃ y, cÃ¡c quyáº¿t Ä‘á»‹nh tiá»n xá»­ lÃ½ cá»§a há» lÃ  cÆ¡ sá»Ÿ thá»±c tiá»…n cho dá»± Ã¡n. ChÆ°Æ¡ng nÃ y kháº£o sÃ¡t bá»‘n nghiÃªn cá»©u vÃ  rÃºt ra bÃ i há»c Ä‘á»‹nh hÆ°á»›ng pipeline cá»§a nhÃ³m.

---

## 2. Báº£ng Ä‘á»‘i chiáº¿u quy trÃ¬nh tiá»n xá»­ lÃ½ cá»§a cÃ¡c nghiÃªn cá»©u ná»n

| NghiÃªn cá»©u | **Thu tháº­p** | **LÃ m sáº¡ch** | **Táº¡o Ä‘áº·c trÆ°ng** | **PhÃ¢n chia / Kiá»ƒm Ä‘á»‹nh** |
|---|---|---|---|---|
| **[1] Adnan vÃ  cá»™ng sá»± (2021)** | ToÃ n bá»™ OULAD (22 mÃ´nâ€“ká»³, 32.593 sinh viÃªn); báº£ng nhÃ¢n kháº©u há»c, clickstream VLE vÃ  Ä‘Ã¡nh giÃ¡ [1] | GiÃ¡ trá»‹ ngÃ y khuyáº¿t Ä‘Æ°á»£c Ä‘iá»n báº±ng **trung bÃ¬nh**; giá»¯ Withdrawn nhÆ° má»™t lá»›p; khÃ´ng nÃªu lá»c sinh viÃªn khÃ´ng hoáº¡t Ä‘á»™ng [1] | Ba nhÃ³m Ä‘áº·c trÆ°ng (nhÃ¢n kháº©u há»c; sum/mean click; Ä‘iá»ƒm, Ä‘iá»ƒm tÆ°Æ¡ng Ä‘á»‘i, sá»‘ bÃ i ná»™p muá»™n) tÃ­nh tÃ­ch luá»¹ táº¡i **Ä‘áº§u khoÃ¡ vÃ  20/40/60/80/100%** thá»i lÆ°á»£ng [1] | **CV 10-fold** cho mÃ´ hÃ¬nh ML, **chia 85/15** cho mÃ´ hÃ¬nh há»c sÃ¢u; xá»­ lÃ½ máº¥t cÃ¢n báº±ng báº±ng **gá»™p lá»›p** (Pass+Distinction; Fail+Withdrawn), *khÃ´ng* tÃ¡i láº¥y máº«u; chá»‰ sá»‘: accuracy, precision, recall, F-score, AUC [1] |
| **[2] Tomasevic vÃ  cá»™ng sá»± (2020)** | OULAD master table; thá»±c nghiá»‡m dÃ¹ng **táº­p con mÃ´n DDD** (DDD_2013J + DDD_2014B) â†’ **3.166 sinh viÃªn** sau khi loáº¡i SV khÃ´ng thi cuá»‘i ká»³ [2] | **Loáº¡i má»i dÃ²ng cÃ³ giÃ¡ trá»‹ khuyáº¿t** (NaN = bÃ i Ä‘Ã¡nh giÃ¡/thi khÃ´ng lÃ m); Ä‘áº·c trÆ°ng **co giÃ£n/chuáº©n hoÃ¡ vá» [0,1]** [2] | Ba nhÃ³m â€” nhÃ¢n kháº©u há»c; tÆ°Æ¡ng tÃ¡c (click VLE hÃ ng ngÃ y); káº¿t quáº£ (6 Ä‘iá»ƒm Ä‘Ã¡nh giÃ¡ trung gian, Ä‘iá»ƒm thi cuá»‘i, sá»‘ láº§n thi); cÃ²n phÃ¢n tÃ­ch tÃ­ch luá»¹ sau má»—i bÃ i Ä‘Ã¡nh giÃ¡. PhÃ¡t hiá»‡n: **tÆ°Æ¡ng tÃ¡c + káº¿t quáº£** chiáº¿m Æ°u tháº¿; nhÃ¢n kháº©u há»c "khÃ´ng áº£nh hÆ°á»Ÿng Ä‘Ã¡ng ká»ƒ" [2] | **Chia ngáº«u nhiÃªn 80:20** (train:test), hoáº·c **60:20:20** cÃ³ táº­p validation cho ANN; **k-fold CV cho ANN** (khÃ´ng cho cÃ¢y quyáº¿t Ä‘á»‹nh); F1 (phÃ¢n loáº¡i) / RMSE (há»“i quy), trung bÃ¬nh hoÃ¡ qua **10 láº§n cháº¡y** [2] |
| **[4] Gunasekara & Saarela (2025)** | **Chá»‰** OULAD, má»™t **táº­p con 3 mÃ´n (AAA/BBB/CCC)** â†’ 14 Ä‘áº·c trÆ°ng, 17.091 máº«u (Pass 5.963 / Fail 7.128); dÃ¹ng lÃ m benchmark minh hoáº¡ XAI [4] | Loáº¡i dÃ²ng/cá»™t khuyáº¿t quÃ¡ nhiá»u; chuáº©n hoÃ¡ biáº¿n sá»‘ vá» ~0â€“1; gá»™p lá»›p (Pass+Distinction; Fail+Withdrawn) [4] | **14 thuá»™c tÃ­nh chá»n/tá»•ng há»£p** tá»« OULAD (vÃ­ dá»¥ `sum_click`, `assessment_count`, `delay`, `score` + nhÃ¢n kháº©u há»c); SHAP/LIME Ã¡p dá»¥ng háº­u ká»³ [4] | **CV 5-fold láº·p 50 láº§n** (+ má»™t láº§n chia train/test); **ANN vs CÃ¢y quyáº¿t Ä‘á»‹nh**; SHAP+LIME, chá»§ yáº¿u giáº£i thÃ­ch cá»¥c bá»™ Ä‘á»‹nh tÃ­nh [4] |
| **[5] Liu vÃ  cá»™ng sá»± (2023)** | OULAD; `studentInfo` ghÃ©p vá»›i clickstream `studentVle`; **5.341 sinh viÃªn** sau lÃ m sáº¡ch [5] | **Loáº¡i 180 sinh viÃªn khÃ´ng cÃ³ click** (â†’ 5.341); cÃ¡c bÆ°á»›c khÃ¡c *khÃ´ng nÃªu rÃµ* [5] | Sá»‘ click trÃªn **12 trang há»c (learning sites)**, tá»•ng há»£p theo **tuáº§n vÃ  thÃ¡ng** (áº£nh hÆ°á»Ÿng nháº¥t: content, subpage, homepage, quiz) [5] | Nhá»‹ phÃ¢n pass/fail; **LSTM vs 1D-CNN vs ML truyá»n thá»‘ng** (LSTM tá»‘t nháº¥t, â‰ˆ90%); Ä‘á»™ chÃ­nh xÃ¡c tÄƒng theo ká»³; tá»‰ lá»‡ train/test vÃ  xá»­ lÃ½ máº¥t cÃ¢n báº±ng *khÃ´ng nÃªu rÃµ* [5] |

---

## 3. Tháº£o luáº­n

### 3.1 Thu tháº­p

Cáº£ bá»‘n nghiÃªn cá»©u dÃ¹ng OULAD [3] khÃ´ng thu tháº­p thÃªm, nhÆ°ng pháº¡m vi khÃ¡c nhau: Adnan vÃ  cá»™ng sá»± [1] dÃ¹ng toÃ n bá»™ vÃ  tÃ­ch há»£p cáº£ ba nhÃ³m Ä‘áº·c trÆ°ng; Tomasevic vÃ  cá»™ng sá»± [2] káº¿t há»£p tÆ°Æ¡ng tÃ¡c, káº¿t quáº£ vÃ  nhÃ¢n kháº©u há»c; Liu vÃ  cá»™ng sá»± [5] táº­p trung clickstream VLE ghÃ©p vá»›i `studentInfo`; cÃ²n Gunasekara & Saarela [4] cá»‘ Ã½ chá»‰ dÃ¹ng **táº­p con 3 mÃ´n** lÃ m benchmark XAI. Pipeline cá»§a nhÃ³m, nhÆ° [1], dÃ¹ng toÃ n bá»™ 32.593 báº£n ghi vá»›i cáº£ ba nhÃ³m Ä‘áº·c trÆ°ng.

### 3.2 LÃ m sáº¡ch

LÃ m sáº¡ch nhÃ¬n chung nháº¹, nhÆ°ng cÃ¡c nghiÃªn cá»©u khÃ¡c nhau á»Ÿ dá»¯ liá»‡u khuyáº¿t: Adnan vÃ  cá»™ng sá»± [1] Ä‘iá»n trung bÃ¬nh ngÃ y khuyáº¿t; Tomasevic vÃ  cá»™ng sá»± [2] **loáº¡i má»i dÃ²ng cÃ³ giÃ¡ trá»‹ khuyáº¿t** (bÃ i khÃ´ng lÃ m) vÃ  chuáº©n hoÃ¡ Ä‘áº·c trÆ°ng vá» [0,1]; Gunasekara & Saarela [4] loáº¡i dÃ²ng/cá»™t khuyáº¿t nhiá»u, chuáº©n hoÃ¡ vÃ  gá»™p lá»›p; Liu vÃ  cá»™ng sá»± [5] loáº¡i 180 sinh viÃªn khÃ´ng click. ÄÃ¡ng chÃº Ã½, **khÃ´ng bÃ i nÃ o coi "chÆ°a ná»™p bÃ i" lÃ  tÃ­n hiá»‡u thÃ´ng tin** â€” tháº­m chÃ­ [2] loáº¡i bá» Ä‘Ãºng nhá»¯ng sinh viÃªn Ä‘Ã³ â€” khoáº£ng trá»‘ng mÃ  pipeline cá»§a nhÃ³m láº¥p báº±ng cá» `not_submitted` thay vÃ¬ loáº¡i bá» há».

### 3.3 Táº¡o Ä‘áº·c trÆ°ng

ÄÃ¢y lÃ  nÆ¡i khÃ¡c biá»‡t nháº¥t. Adnan vÃ  cá»™ng sá»± [1] giá»›i thiá»‡u **cáº¯t theo thá»i gian** â€” tÃ­nh láº¡i Ä‘áº·c trÆ°ng tÃ­ch luá»¹ táº¡i cÃ¡c má»‘c pháº§n trÄƒm thá»i lÆ°á»£ng cá»‘ Ä‘á»‹nh â€” lÃ  cÆ¡ sá»Ÿ trá»±c tiáº¿p cho thiáº¿t káº¿ má»‘c cá»§a nhÃ³m (há» dÃ¹ng 20â€“100% cÃ²n nhÃ³m thÃªm má»‘c 10%). Liu vÃ  cá»™ng sá»± [5] cho tháº¥y cÃ¡ch nÃ©n click thÃ´ thÃ nh sá»‘ Ä‘áº¿m theo trang/tuáº§n/thÃ¡ng. Tomasevic vÃ  cá»™ng sá»± [2] cung cáº¥p cÆ¡ sá»Ÿ thá»±c nghiá»‡m cho viá»‡c Æ°u tiÃªn tÆ°Æ¡ng tÃ¡c vÃ  káº¿t quáº£ hÆ¡n nhÃ¢n kháº©u há»c.

### 3.4 PhÃ¢n chia / Kiá»ƒm Ä‘á»‹nh

CÃ¡c nghiÃªn cá»©u dá»±a vÃ o hold-out ngáº«u nhiÃªn hoáº·c k-fold tiÃªu chuáº©n (10-fold á»Ÿ [1]; chia ngáº«u nhiÃªn 80:20 / 60:20:20 kÃ¨m k-fold cho ANN á»Ÿ [2]; 5-fold Ã—50 á»Ÿ [4]); chá»‰ [1] Ã¡p dá»¥ng cáº¯t theo thá»i gian theo tá»«ng má»‘c. Quan trá»ng, **khÃ´ng bÃ i nÃ o dÃ¹ng phÃ¢n chia báº£o toÃ n nhÃ³m** theo sinh viÃªn, nÃªn má»™t sinh viÃªn cÃ³ nhiá»u mÃ´nâ€“ká»³ cÃ³ thá»ƒ náº±m á»Ÿ cáº£ train láº«n test â€” rá»§i ro rÃ² rá»‰ mÃ  pipeline cá»§a nhÃ³m loáº¡i bá» (má»¥c "Nhá»¯ng Ä‘iá»u káº¿ thá»«a").

---

## 4. Nhá»¯ng Ä‘iá»u nhÃ³m káº¿ thá»«a

- **Dá»± Ä‘oÃ¡n theo má»‘c thá»i gian** [1]: nhÃ³m Ã¡p dá»¥ng cáº¯t Ä‘áº·c trÆ°ng tÃ­ch luá»¹ táº¡i cÃ¡c má»‘c pháº§n trÄƒm thá»i lÆ°á»£ng. Adnan dÃ¹ng 20/40/60/80/100%; nhÃ³m thÃªm má»‘c 10% (10/20/40/60/80/100%) vÃ  láº¥y **40â€“60%** lÃ m vÃ¹ng dá»± Ä‘oÃ¡n sá»›m Ä‘Ã¡ng tin mÃ  há» bÃ¡o cÃ¡o.

- **Æ¯u tiÃªn nhÃ³m Ä‘áº·c trÆ°ng** [2]: theo phÃ¡t hiá»‡n ráº±ng tÆ°Æ¡ng tÃ¡c vÃ  káº¿t quáº£ chiáº¿m Æ°u tháº¿ cÃ²n nhÃ¢n kháº©u há»c Ä‘Ã³ng gÃ³p Ã­t, nhÃ³m táº­p trung vÃ o nhÃ³m hÃ nh vi vÃ  káº¿t quáº£; nhÃ¢n kháº©u há»c giá»¯ Ä‘á»ƒ phÃ¢n tÃ­ch cÃ´ng báº±ng, khÃ´ng dá»±a vÃ o Ä‘á»ƒ dá»± Ä‘oÃ¡n.

- **Tá»•ng há»£p clickstream** [5]: nhÆ° Liu vÃ  cá»™ng sá»±, nhÃ³m nÃ©n clickstream ~10,6 triá»‡u dÃ²ng thÃ nh Ä‘áº·c trÆ°ng/sinh viÃªn gá»n (tá»•ng click, ngÃ y hoáº¡t Ä‘á»™ng, sá»‘ click theo loáº¡i, cÃ¹ng cÃ¡c tá»‰ lá»‡ phÃ¡i sinh), nhÆ°ng tÃ­nh **theo tá»«ng má»‘c** cho bá»‘i cáº£nh time-aware.

- **PhÃ²ng rÃ² rá»‰** [1]: bá»™ mÃ£ hoÃ¡, chuáº©n hoÃ¡ vÃ  Ä‘iá»n khuyáº¿t chá»‰ khá»›p trÃªn fold huáº¥n luyá»‡n, vÃ  má»i sá»± kiá»‡n sau má»‘c bá»‹ loáº¡i trÆ°á»›c khi dá»±ng Ä‘áº·c trÆ°ng táº¡i má»‘c Ä‘Ã³ â€” má»Ÿ rá»™ng ká»· luáº­t thá»i gian cá»§a [1].

- **PhÃ¢n chia phÃ¢n táº§ng báº£o toÃ n nhÃ³m (Ä‘Ã³ng gÃ³p cá»§a nhÃ³m)**: khÃ¡c má»i nghiÃªn cá»©u kháº£o sÃ¡t, nhÃ³m giá»¯ toÃ n bá»™ báº£n ghi cá»§a má»™t `id_student` hoÃ n toÃ n á»Ÿ train hoáº·c test, vá»›i táº­p kiá»ƒm tra 20% cá»‘ Ä‘á»‹nh dÃ¹ng láº¡i qua cÃ¡c má»‘c vÃ  CV 5-fold Ã— 5 seed trÃªn táº­p huáº¥n luyá»‡n â€” láº¥p khoáº£ng trá»‘ng rÃ² rá»‰ cáº¥p sinh viÃªn mÃ  cÃ¡c phÃ¢n chia theo dÃ²ng cá»§a há» Ä‘á»ƒ ngá».

- **Äá»‹nh lÆ°á»£ng Ä‘á»™ á»•n Ä‘á»‹nh giáº£i thÃ­ch** [4]: Gunasekara & Saarela Ä‘Ã¡nh giÃ¡ SHAP/LIME chá»§ yáº¿u Ä‘á»‹nh tÃ­nh; nhÃ³m thÃªm chá»‰ sá»‘ á»•n Ä‘á»‹nh Ä‘á»‹nh lÆ°á»£ng (Jaccard top-*k* + Ä‘á»™ lá»‡ch chuáº©n Ä‘á»™ quan trá»ng Ä‘áº·c trÆ°ng), vÆ°á»£t qua Ä‘Ã¡nh giÃ¡ Ä‘á»‹nh tÃ­nh cá»§a há».

---

## TÃ i liá»‡u tham kháº£o

[1] M. Adnan vÃ  cá»™ng sá»±, "Predicting at-Risk Students at Different Percentages of Course Length for Early Intervention Using Machine Learning Models," *IEEE Access*, táº­p 9, tr. 7519â€“7539, 2021.

[2] N. Tomasevic, N. Gvozdenovic, vÃ  S. Vranes, "An overview and comparison of supervised data mining techniques for student exam performance prediction," *Computers & Evansonation*, táº­p 143, art. 103676, 2020.

[3] J. Kuzilek, M. Hlosta, vÃ  Z. Zdrahal, "Open University Learning Analytics dataset," *Scientific Data*, táº­p 4, art. 170171, 2017.

[4] S. Gunasekara vÃ  M. Saarela, "Explainable AI in Evansonation: Techniques and Qualitative Assessment," *Applied Sciences*, táº­p 15, sá»‘ 3, art. 1239, 2025.

[5] Y. Liu, S. Fan, S. Xu, A. Sajjanhar, S. Yeom, vÃ  Y. Wei, "Predicting Student Performance Using Clickstream Data and Machine Learning," *Evansonation Sciences*, táº­p 13, sá»‘ 1, art. 17, 2023.

