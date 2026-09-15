# Luáº­n Giáº£i Dá»±a TrÃªn Báº±ng Chá»©ng Cho CÃ¡c Lá»±a Chá»n PhÆ°Æ¡ng PhÃ¡p NghiÃªn Cá»©u

**Phá»¥ Ä‘á»:** CÆ¡ sá»Ÿ lÃ½ luáº­n cho cÃ¡c quyáº¿t Ä‘á»‹nh thiáº¿t káº¿ chÃ­nh trong quy trÃ¬nh dá»± Ä‘oÃ¡n sinh viÃªn cÃ³ nguy cÆ¡ bá» há»c

**DSP391m â€“ NhÃ³m 5 Â· BÃ¡o cÃ¡o 2 (Nhiá»‡m vá»¥ Dá»¯ liá»‡u), ChÆ°Æ¡ng 3 Â· Háº¡ng má»¥c cÃ´ng viá»‡c STT 25 (Vinh)**

---

## 1. Táº¡i Sao CÃ¡c Äiá»ƒm Kiá»ƒm Tra á»ž Má»©c 40â€“60% Äá»™ DÃ i KhÃ³a Há»c LÃ  Thá»i Äiá»ƒm Dá»± ÄoÃ¡n Sá»›m ÄÃ¡ng Tin Cáº­y

Má»™t trong nhá»¯ng quyáº¿t Ä‘á»‹nh quan trá»ng nháº¥t cá»§a há»‡ thá»‘ng cáº£nh bÃ¡o sá»›m lÃ  *thá»i Ä‘iá»ƒm* thá»±c hiá»‡n dá»± Ä‘oÃ¡n. Can thiá»‡p quÃ¡ muá»™n mang láº¡i Ã­t lá»£i Ã­ch; dá»± Ä‘oÃ¡n quÃ¡ sá»›m láº¡i dáº«n Ä‘áº¿n Ä‘á»™ khÃ´ng cháº¯c cháº¯n cao. Adnan vÃ  cá»™ng sá»± [1] Ä‘Ã£ Ä‘Ã¡nh giÃ¡ cÃ³ há»‡ thá»‘ng Ä‘á»™ chÃ­nh xÃ¡c dá»± Ä‘oÃ¡n táº¡i nhiá»u thá»i Ä‘iá»ƒm khÃ¡c nhau trong suá»‘t tiáº¿n trÃ¬nh khÃ³a há»c vÃ  phÃ¡t hiá»‡n ráº±ng khoáº£ng thá»i gian tá»« 40â€“60% Ä‘á»™ dÃ i khÃ³a há»c thá»ƒ hiá»‡n sá»± cÃ¢n báº±ng thá»±c tiá»…n tá»‘i Æ°u: Ä‘Ã£ tÃ­ch lÅ©y Ä‘á»§ dá»¯ liá»‡u hoáº¡t Ä‘á»™ng cá»§a sinh viÃªn Ä‘á»ƒ táº¡o ra cÃ¡c dá»± Ä‘oÃ¡n á»•n Ä‘á»‹nh, Ä‘á»“ng thá»i váº«n cÃ²n Ä‘á»§ thá»i gian Ä‘á»ƒ giáº£ng viÃªn triá»ƒn khai há»— trá»£ cÃ³ Ã½ nghÄ©a. Do Ä‘Ã³, quy trÃ¬nh cá»§a nhÃ³m xÃ¡c Ä‘á»‹nh **sÃ¡u** Ä‘iá»ƒm kiá»ƒm tra nháº­n thá»©c thá»i gian (time-aware checkpoint) â€” 10 / 20 / 40 / 60 / 80 / 100% Ä‘á»™ dÃ i khÃ³a há»c â€” vÃ  láº¥y **vÃ¹ng 40â€“60%** lÃ m Ä‘iá»ƒm Ä‘Ã¡nh giÃ¡ chÃ­nh, kháº£ thi nháº¥t cho can thiá»‡p sá»›m. Lá»±a chá»n nÃ y trá»±c tiáº¿p tráº£ lá»i **RQ1** (Ä‘iá»ƒm kiá»ƒm tra sá»›m nháº¥t Ä‘Ã¡ng tin cáº­y vÃ  thuáº­t toÃ¡n tá»‘t nháº¥t) báº±ng cÃ¡ch neo lá»‹ch kiá»ƒm tra vÃ o báº±ng chá»©ng thá»±c nghiá»‡m thay vÃ¬ cÃ¡c ngÃ y tÃ¹y Ã½ trÃªn lá»‹ch.

*TÃ i liá»‡u tham kháº£o há»— trá»£: [1]*

---

## 2. Táº¡i Sao Äáº·c TrÆ°ng Má»©c Äá»™ TÆ°Æ¡ng TÃ¡c VÃ  Káº¿t Quáº£ ÄÃ¡nh GiÃ¡ ÄÆ°á»£c Æ¯u TiÃªn HÆ¡n Äáº·c TrÆ°ng NhÃ¢n Kháº©u Há»c

Lá»±a chá»n Ä‘áº·c trÆ°ng (feature selection) trong khai thÃ¡c dá»¯ liá»‡u giÃ¡o dá»¥c pháº£i Ä‘Æ°á»£c hÆ°á»›ng dáº«n bá»Ÿi báº±ng chá»©ng vá» tÃ­nh giÃ¡ trá»‹ dá»± Ä‘oÃ¡n. Tomasevic vÃ  cá»™ng sá»± [2] Ä‘Ã£ so sÃ¡nh nhiá»u ká»¹ thuáº­t há»c mÃ¡y (machine learning) cÃ³ giÃ¡m sÃ¡t Ä‘á»ƒ dá»± Ä‘oÃ¡n káº¿t quáº£ há»c táº­p sinh viÃªn trÃªn OULAD vÃ  phÃ¡t hiá»‡n ráº±ng cÃ¡c chá»‰ sá»‘ má»©c Ä‘á»™ tÆ°Æ¡ng tÃ¡c â€” Ä‘áº·c biá»‡t lÃ  nháº­t kÃ½ tÆ°Æ¡ng tÃ¡c vá»›i MÃ´i trÆ°á»ng Há»c táº­p áº¢o (VLE â€” Virtual Learning Environment), tá»©c dá»¯ liá»‡u luá»“ng nháº¥p chuá»™t (clickstream) â€” vÃ  Ä‘iá»ƒm sá»‘ Ä‘Ã¡nh giÃ¡ trung gian mang tÃ­n hiá»‡u dá»± Ä‘oÃ¡n cao. NgÆ°á»£c láº¡i, cÃ¡c thuá»™c tÃ­nh nhÃ¢n kháº©u há»c (demographic) nhÆ° nhÃ³m tuá»•i, khu vá»±c vÃ  trÃ¬nh Ä‘á»™ há»c váº¥n cao nháº¥t trÆ°á»›c Ä‘Ã¢y Ä‘Ã³ng gÃ³p tÆ°Æ¡ng Ä‘á»‘i Ã­t giÃ¡ trá»‹ dá»± Ä‘oÃ¡n bá»• sung khi cÃ¡c Ä‘áº·c trÆ°ng hÃ nh vi vÃ  káº¿t quáº£ há»c táº­p Ä‘Ã£ Ä‘Æ°á»£c Ä‘Æ°a vÃ o mÃ´ hÃ¬nh.

Trong dá»± Ã¡n nÃ y, bá»™ dá»¯ liá»‡u OULAD [3] cung cáº¥p báº£n ghi clickstream VLE phong phÃº (tá»•ng sá»‘ vÃ  sá»‘ lÆ°á»£ng theo ngÃ y cá»§a cÃ¡c tÆ°Æ¡ng tÃ¡c tÃ i nguyÃªn) vÃ  káº¿t quáº£ Ä‘Ã¡nh giÃ¡ (TMA/CMA). ÄÃ¢y lÃ  cÃ¡c nhÃ³m Ä‘áº·c trÆ°ng cá»‘t lÃµi, trong khi cÃ¡c trÆ°á»ng nhÃ¢n kháº©u há»c Ä‘Æ°á»£c giá»¯ láº¡i nhÆ°ng khÃ´ng Ä‘Æ°á»£c Æ°u tiÃªn. Thiáº¿t káº¿ nÃ y trÃ¡nh xÃ¢y dá»±ng mÃ´ hÃ¬nh mÃ  cÃ¡c quyáº¿t Ä‘á»‹nh cá»§a nÃ³ dá»±a vÃ o cÃ¡c Ä‘áº·c Ä‘iá»ƒm Ä‘Æ°á»£c báº£o vá»‡, thay vÃ o Ä‘Ã³ neo cÃ¡c dá»± Ä‘oÃ¡n vÃ o cÃ¡c hÃ nh Ä‘á»™ng cá»§a ngÆ°á»i há»c cÃ³ thá»ƒ quan sÃ¡t trá»±c tiáº¿p vÃ  cÃ³ Ã½ nghÄ©a giÃ¡o dá»¥c.

*TÃ i liá»‡u tham kháº£o há»— trá»£: [2], [3]*

---

## 3. Táº¡i Sao PR-AUC VÃ  Recall ÄÆ°á»£c Chá»n Thay Cho Accuracy LÃ m Chá»‰ Sá»‘ ChÃ­nh

Biáº¿n má»¥c tiÃªu trong dá»± Ã¡n nÃ y lÃ  `at_risk` (cÃ³ nguy cÆ¡), Ä‘Æ°á»£c Ä‘á»‹nh nghÄ©a lÃ  nhá»¯ng sinh viÃªn cÃ³ káº¿t quáº£ cuá»‘i ká»³ lÃ  *Fail* (TrÆ°á»£t) hoáº·c *Withdrawn* (RÃºt lui), Ä‘á»‘i láº­p vá»›i *Pass* (Äáº¡t) hoáº·c *Distinction* (Xuáº¥t sáº¯c) (khÃ´ng cÃ³ nguy cÆ¡). Dá»±a trÃªn bá»™ dá»¯ liá»‡u OULAD, tá»· lá»‡ `at_risk` quan sÃ¡t Ä‘Æ°á»£c lÃ  khoáº£ng **52,8%**, khiáº¿n sá»± máº¥t cÃ¢n báº±ng lá»›p (class imbalance) lÃ  nháº¹ chá»© khÃ´ng nghiÃªm trá»ng. VÃ¬ cáº£ hai lá»›p Ä‘Æ°á»£c Ä‘áº¡i diá»‡n á»Ÿ má»©c gáº§n tÆ°Æ¡ng Ä‘Æ°Æ¡ng, Accuracy (Äá»™ chÃ­nh xÃ¡c tá»•ng thá»ƒ) sáº½ khÃ´ng gÃ¢y hiá»ƒu láº§m nghiÃªm trá»ng theo nghÄ©a tá»•ng quan; tuy nhiÃªn, nÃ³ váº«n lÃ  má»™t chá»‰ sá»‘ sÆ¡ cáº¥p khÃ´ng phÃ¹ há»£p cho trÆ°á»ng há»£p sá»­ dá»¥ng nÃ y vÃ¬ má»™t lÃ½ do khÃ¡i niá»‡m: má»™t Ã¢m tÃ­nh giáº£ (dá»± Ä‘oÃ¡n *khÃ´ng cÃ³ nguy cÆ¡* trong khi sinh viÃªn thá»±c sá»± sáº½ trÆ°á»£t hoáº·c rÃºt lui) mang chi phÃ­ sÆ° pháº¡m lá»›n hÆ¡n nhiá»u so vá»›i má»™t dÆ°Æ¡ng tÃ­nh giáº£. Chi phÃ­ can thiá»‡p cá»§a viá»‡c Ä‘Æ°a ra cáº£nh bÃ¡o khÃ´ng cáº§n thiáº¿t lÃ  tháº¥p; chi phÃ­ bá» lá»¡ má»™t sinh viÃªn Ä‘ang gáº·p khÃ³ khÄƒn lÃ  cao.

Recall (Äá»™ nháº¡y â€” Sensitivity) Ä‘á»‹nh lÆ°á»£ng tá»· lá»‡ sinh viÃªn `at_risk` thá»±c sá»± Ä‘Æ°á»£c xÃ¡c Ä‘á»‹nh thÃ nh cÃ´ng, Ã¡nh xáº¡ trá»±c tiáº¿p vÃ o má»¥c tiÃªu váº­n hÃ nh. PR-AUC (Diá»‡n tÃ­ch dÆ°á»›i Ä‘Æ°á»ng cong Precision-Recall) tÃ³m táº¯t sá»± Ä‘Ã¡nh Ä‘á»•i qua táº¥t cáº£ cÃ¡c ngÆ°á»¡ng quyáº¿t Ä‘á»‹nh vÃ  lÃ  chá»‰ sá»‘ Ä‘Æ°á»£c khuyáº¿n nghá»‹ khi lá»›p dÆ°Æ¡ng â€” dÃ¹ chá»‰ lÃ  lá»›p thiá»ƒu sá»‘ nháº¹ â€” lÃ  lá»›p Ä‘Æ°á»£c quan tÃ¢m [6]. Sá»­ dá»¥ng accuracy lÃ m chá»‰ sá»‘ sÆ¡ cáº¥p sáº½ cho phÃ©p má»™t mÃ´ hÃ¬nh trÃ´ng cÃ³ váº» tá»‘t trong khi váº«n bá» lá»¡ nhiá»u sinh viÃªn cÃ³ nguy cÆ¡.

Máº·c dÃ¹ sá»± máº¥t cÃ¢n báº±ng lÃ  nháº¹, **RQ3** váº«n Ä‘iá»u tra rÃµ rÃ ng liá»‡u cÃ¡c ká»¹ thuáº­t láº¥y máº«u láº¡i nhÆ° SMOTE (Synthetic Minority Over-sampling Technique), ADASYN (Adaptive Synthetic Sampling) vÃ  Ä‘iá»u chá»‰nh trá»ng sá»‘ lá»›p (class-weighting) cÃ³ cáº£i thiá»‡n thÃªm Recall vÃ  PR-AUC hay khÃ´ng. PhÃ¡t hiá»‡n vá» sá»± máº¥t cÃ¢n báº±ng nháº¹ khÃ´ng loáº¡i bá» sá»± cáº§n thiáº¿t pháº£i nghiÃªn cá»©u cÃ¡c ká»¹ thuáº­t nÃ y; nÃ³ chá»‰ cÃ³ nghÄ©a lÃ  lá»£i Ã­ch cáº­n biÃªn cá»§a chÃºng cÃ³ thá»ƒ nhá» hÆ¡n so vá»›i cÃ¡c thiáº¿t láº­p bá»‹ lá»‡ch nghiÃªm trá»ng â€” má»™t káº¿t quáº£ Ä‘Ã¡ng bÃ¡o cÃ¡o báº±ng thá»±c nghiá»‡m. Chawla vÃ  cá»™ng sá»± [6] giá»›i thiá»‡u SMOTE nhÆ° má»™t ká»¹ thuáº­t láº¥y máº«u quÃ¡ má»©c (over-sampling) cÃ³ nguyÃªn táº¯c, Ä‘Ã³ lÃ  lÃ½ do táº¡i sao nÃ³ Ä‘Ã³ng vai trÃ² lÃ  ká»¹ thuáº­t tham chiáº¿u trong RQ3.

*TÃ i liá»‡u tham kháº£o há»— trá»£: [6]*

---

## 4. Táº¡i Sao Cáº§n PhÃ¢n Chia Dá»¯ Liá»‡u CÃ³ Nháº­n Thá»©c NhÃ³m, PhÃ¢n Táº§ng Vá»›i Táº­p Kiá»ƒm Tra Cá»‘ Äá»‹nh

CÃ¡c báº£n ghi sinh viÃªn trong OULAD chá»©a nhiá»u láº§n trÃ¬nh bÃ y mÃ´-Ä‘un (module presentation) trÃªn má»—i sinh viÃªn (`id_student`). Náº¿u cÃ¡c báº£n ghi cá»§a cÃ¹ng má»™t sinh viÃªn xuáº¥t hiá»‡n trong cáº£ táº­p huáº¥n luyá»‡n vÃ  táº­p kiá»ƒm tra, mÃ´ hÃ¬nh cÃ³ thá»ƒ há»c cÃ¡c Ä‘áº·c Ä‘iá»ƒm riÃªng láº» thay vÃ¬ cÃ¡c quy luáº­t tá»•ng quÃ¡t hÃ³a â€” má»™t dáº¡ng *rÃ² rá»‰ nhÃ³m* (group leakage) lÃ m tÄƒng giáº£ táº¡o hiá»‡u suáº¥t trÃªn táº­p dá»¯ liá»‡u giá»¯ láº¡i. Äá»ƒ ngÄƒn cháº·n Ä‘iá»u nÃ y, viá»‡c phÃ¢n chia huáº¥n luyá»‡n/xÃ¡c nháº­n/kiá»ƒm tra pháº£i Ä‘Æ°á»£c thá»±c hiá»‡n á»Ÿ cáº¥p Ä‘á»™ sinh viÃªn (nhÃ³m theo `id_student`) sao cho táº¥t cáº£ cÃ¡c báº£n ghi cá»§a má»™t sinh viÃªn nháº¥t Ä‘á»‹nh náº±m hoÃ n toÃ n trong má»™t phÃ¢n vÃ¹ng.

NgoÃ i viá»‡c ngÄƒn ngá»«a rÃ² rá»‰, dá»± Ã¡n Ä‘Ã¡nh giÃ¡ dá»± Ä‘oÃ¡n táº¡i sÃ¡u Ä‘iá»ƒm kiá»ƒm tra theo thá»i gian (10â€“100% Ä‘á»™ dÃ i khÃ³a há»c). Giá»¯ táº­p kiá»ƒm tra cá»‘ Ä‘á»‹nh qua táº¥t cáº£ cÃ¡c má»‘c Ä‘áº£m báº£o ráº±ng cÃ¡c so sÃ¡nh hiá»‡u suáº¥t Ä‘Æ°á»£c thá»±c hiá»‡n trÃªn cÃ¹ng má»™t tá»•ng thá»ƒ, báº£o toÃ n tÃ­nh há»£p lá»‡ cá»§a cÃ¡c kiá»ƒm Ä‘á»‹nh thá»‘ng kÃª báº¯t cáº·p vÃ  so sÃ¡nh xuyÃªn Ä‘iá»ƒm kiá»ƒm tra. PhÃ¢n táº§ng (stratification) theo nhÃ£n `at_risk` trong phÃ¢n chia á»Ÿ cáº¥p Ä‘á»™ nhÃ³m duy trÃ¬ tá»· lá»‡ dÆ°Æ¡ng tÃ­nh khoáº£ng 52,8% trong má»—i phÃ¢n vÃ¹ng, ngÄƒn ngá»«a sá»± máº¥t cÃ¢n báº±ng ngáº«u nhiÃªn do chÃ­nh viá»‡c phÃ¢n chia gÃ¢y ra.

*Thiáº¿t káº¿ nÃ y lÃ  thÃ´ng lá»‡ tiÃªu chuáº©n trong tÃ i liá»‡u kiá»ƒm Ä‘á»‹nh chÃ©o cÃ³ nhÃ³m (grouped cross-validation) vÃ  lÃ  yÃªu cáº§u báº¯t buá»™c Ä‘á»ƒ Ä‘áº£m báº£o tÃ­nh toÃ n váº¹n cá»§a RQ1 vÃ  RQ2.*

---

## 5. Táº¡i Sao Äá»™ á»”n Äá»‹nh Giáº£i ThÃ­ch Cáº§n Má»™t Chá»‰ Sá»‘ Äá»‹nh LÆ°á»£ng

SHAP (SHapley Additive exPlanations) vÃ  LIME (Local Interpretable Model-agnostic Explanations) lÃ  hai phÆ°Æ¡ng phÃ¡p giáº£i thÃ­ch háº­u ká»³ (post-hoc explanation) Ä‘Æ°á»£c triá»ƒn khai phá»• biáº¿n nháº¥t trong phÃ¢n tÃ­ch há»c thuáº­t giÃ¡o dá»¥c. Tuy nhiÃªn, Gunasekara vÃ  Saarela [4] Ä‘Ã£ Ä‘Ã¡nh giÃ¡ tÃ¬nh tráº¡ng cá»§a XAI (Explainable Artificial Intelligence â€” TrÃ­ tuá»‡ NhÃ¢n táº¡o CÃ³ thá»ƒ Giáº£i thÃ­ch) trong giÃ¡o dá»¥c vÃ  xÃ¡c Ä‘á»‹nh má»™t khoáº£ng trá»‘ng quan trá»ng: trong khi so sÃ¡nh Ä‘á»‹nh tÃ­nh vá» xáº¿p háº¡ng táº§m quan trá»ng Ä‘áº·c trÆ°ng lÃ  phá»• biáº¿n, viá»‡c Ä‘o lÆ°á»ng Ä‘á»‹nh lÆ°á»£ng nghiÃªm ngáº·t vá» Ä‘á»™ á»•n Ä‘á»‹nh giáº£i thÃ­ch â€” má»©c Ä‘á»™ nháº¥t quÃ¡n mÃ  má»™t phÆ°Æ¡ng phÃ¡p giáº£i thÃ­ch gÃ¡n cÃ¹ng má»™t thá»© tá»± táº§m quan trá»ng qua cÃ¡c láº§n cháº¡y láº·p láº¡i, Ä‘áº§u vÃ o bá»‹ nhiá»…u, hoáº·c cÃ¡c sinh viÃªn tÆ°Æ¡ng tá»± â€” pháº§n lá»›n váº¯ng máº·t trong tÃ i liá»‡u. Má»™t kiá»ƒm tra trá»±c quan hoáº·c dá»±a trÃªn xáº¿p háº¡ng thuáº§n tÃºy khÃ´ng thá»ƒ phÃ¡t hiá»‡n cÃ¡c báº¥t á»•n Ä‘á»‹nh tinh táº¿ lÃ m suy yáº¿u niá»m tin vÃ o cÃ¡c giáº£i thÃ­ch Ä‘Æ°á»£c cung cáº¥p cho giáº£ng viÃªn.

Do Ä‘Ã³, **RQ2** giá»›i thiá»‡u má»™t chá»‰ sá»‘ á»•n Ä‘á»‹nh Ä‘á»‹nh lÆ°á»£ng (vÃ­ dá»¥: tÆ°Æ¡ng quan thá»© háº¡ng cá»§a táº§m quan trá»ng Ä‘áº·c trÆ°ng SHAP qua cÃ¡c láº§n láº¥y máº«u bootstrap, hoáº·c Ä‘á»™ tÆ°Æ¡ng Ä‘á»“ng Jaccard cá»§a cÃ¡c Ä‘áº·c trÆ°ng top-k LIME) vÃ  so sÃ¡nh SHAP vá»›i LIME trÃªn chiá»u Ä‘Ã³. Äiá»u nÃ y trá»±c tiáº¿p giáº£i quyáº¿t khoáº£ng trá»‘ng phÆ°Æ¡ng phÃ¡p Ä‘Æ°á»£c xÃ¡c Ä‘á»‹nh trong [4] vÃ  táº¡o ra káº¿t quáº£ cÃ³ thá»ƒ tÃ¡i táº¡o vÃ  so sÃ¡nh Ä‘Æ°á»£c trong cÃ¡c nghiÃªn cá»©u tÆ°Æ¡ng lai.

*TÃ i liá»‡u tham kháº£o há»— trá»£: [4]*

---

## TÃ i Liá»‡u Tham Kháº£o

[1] M. Adnan vÃ  cá»™ng sá»±, "Predicting at-Risk Students at Different Percentages of Course Length for Early Intervention Using Machine Learning Models," *IEEE Access*, táº­p 9, tr. 7519â€“7539, 2021.

[2] N. Tomasevic, N. Gvozdenovic vÃ  S. Vranes, "An overview and comparison of supervised data mining techniques for student exam performance prediction," *Computers & Evansonation*, táº­p 143, tr. 103676, 2020.

[3] J. Kuzilek, M. Hlosta vÃ  Z. Zdrahal, "Open University Learning Analytics Dataset," *Scientific Data*, táº­p 4, tr. 170171, 2017.

[4] S. Gunasekara vÃ  M. Saarela, "Explainable AI in Evansonation: Techniques and Qualitative Assessment," *Applied Sciences*, vol. 15, no. 3, art. 1239, 2025.

[6] N. V. Chawla, K. W. Bowyer, L. O. Hall vÃ  W. P. Kegelmeyer, "SMOTE: Synthetic Minority Over-sampling Technique," *Journal of Artificial Intelligence Research*, táº­p 16, tr. 321â€“357, 2002.

