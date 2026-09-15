# Äáº·c táº£ Dá»¯ liá»‡u cho Há»c mÃ¡y CÃ³ Nháº­n thá»©c Thá»i gian vÃ  Kháº£ nÄƒng Giáº£i thÃ­ch trÃªn OULAD

**DSP391m â€“ NhÃ³m 5 Â· BÃ¡o cÃ¡o 2 (Nhiá»‡m vá»¥ Dá»¯ liá»‡u), ChÆ°Æ¡ng 3 Â· Nhiá»‡m vá»¥ 3.1 â€” Äáº·c táº£ Dá»¯ liá»‡u**

---

## TÃ³m táº¯t

TÃ i liá»‡u nÃ y Ä‘áº·c táº£ cÃ¡c yÃªu cáº§u dá»¯ liá»‡u cho Ä‘á» tÃ i "Há»c mÃ¡y CÃ³ Nháº­n thá»©c Thá»i gian vÃ  Kháº£ nÄƒng Giáº£i thÃ­ch (Time-Aware Explainable ML) Ä‘á»ƒ Dá»± Ä‘oÃ¡n Sá»›m Sinh viÃªn CÃ³ Nguy cÆ¡ trÃªn OULAD." Ba cÃ¢u há»i nghiÃªn cá»©u Ä‘iá»u hÆ°á»›ng quÃ¡ trÃ¬nh Ä‘áº·c táº£: (CH1) xÃ¡c Ä‘á»‹nh má»‘c tiáº¿n Ä‘á»™ khÃ³a há»c sá»›m nháº¥t cÃ³ thá»ƒ dá»± Ä‘oÃ¡n tin cáº­y vÃ  thuáº­t toÃ¡n hiá»‡u quáº£ nháº¥t táº¡i má»‘c Ä‘Ã³; (CH2) Ä‘Ã¡nh giÃ¡ Ä‘á»™ á»•n Ä‘á»‹nh cá»§a cÃ¡c giáº£i thÃ­ch háº­u nghiá»‡m SHAP/LIME qua cÃ¡c cá»­a sá»• thá»i gian; vÃ  (CH3) Ä‘Ã¡nh giÃ¡ áº£nh hÆ°á»Ÿng cá»§a cÃ¡c chiáº¿n lÆ°á»£c xá»­ lÃ½ máº¥t cÃ¢n báº±ng lá»›pâ€”SMOTE, ADASYN, vÃ  Ä‘iá»u chá»‰nh trá»ng sá»‘ lá»›p (class-weight)â€”lÃªn Ä‘á»™ chÃ­nh xÃ¡c dá»± Ä‘oÃ¡n vÃ  tÃ­nh nháº¥t quÃ¡n cá»§a giáº£i thÃ­ch. Má»—i yÃªu cáº§u Ä‘Æ°á»£c suy diá»…n trá»±c tiáº¿p tá»« Ã­t nháº¥t má»™t cÃ¢u há»i nghiÃªn cá»©u vÃ  Ä‘Æ°á»£c Ã¡nh xáº¡ tá»›i báº£ng cá»¥ thá»ƒ trong Bá»™ dá»¯ liá»‡u PhÃ¢n tÃ­ch Há»c táº­p TrÆ°á»ng Äáº¡i há»c Má»Ÿ (Open University Learning Analytics Dataset â€” OULAD) [3]. PhÃ¢n tÃ­ch xÃ¡c nháº­n ráº±ng OULAD cung cáº¥p Ä‘áº§y Ä‘á»§ cÃ¡c nhÃ³m dá»¯ liá»‡u cáº§n thiáº¿tâ€”ngá»¯ cáº£nh nhÃ¢n kháº©u há»c, hÃ nh vi tÆ°Æ¡ng tÃ¡c cÃ³ dáº¥u thá»i gian, vÃ  thÃ nh tÃ­ch há»c táº­p theo chiá»u dá»câ€”á»Ÿ quy mÃ´ vÃ  Ä‘á»™ chi tiáº¿t thá»i gian Ä‘á»§ Ä‘á»ƒ há»— trá»£ cáº£ ba cÃ¢u há»i nghiÃªn cá»©u.

---

## 1. Giá»›i thiá»‡u

Nháº­n dáº¡ng sá»›m sinh viÃªn cÃ³ nguy cÆ¡ lÃ  má»™t thÃ¡ch thá»©c trá»ng tÃ¢m trong lÄ©nh vá»±c phÃ¢n tÃ­ch há»c táº­p (learning analytics). Can thiá»‡p trÆ°á»›c khi sinh viÃªn máº¥t káº¿t ná»‘i hoáº·c tháº¥t báº¡i Ä‘Ã²i há»i cÃ¡c mÃ´ hÃ¬nh dá»± Ä‘oÃ¡n vá»«a chÃ­nh xÃ¡c táº¡i cÃ¡c má»‘c tiáº¿n Ä‘á»™ sá»›m vá»«a cÃ³ thá»ƒ giáº£i thÃ­ch Ä‘Æ°á»£c cho cá»‘ váº¥n há»c táº­p. Äá» tÃ i nÃ y hiá»‡n thá»±c hÃ³a bÃ i toÃ¡n trÃªn OULAD [3], bá»™ dá»¯ liá»‡u quan há»‡ cÃ´ng khai do TrÆ°á»ng Äáº¡i há»c Má»Ÿ (The Open University, UK) phÃ¡t hÃ nh. TrÆ°á»›c khi tiáº¿n hÃ nh báº¥t ká»³ cÃ´ng viá»‡c mÃ´ hÃ¬nh hÃ³a nÃ o, dá»¯ liá»‡u cáº§n thiáº¿t pháº£i Ä‘Æ°á»£c xÃ¡c Ä‘á»‹nh cháº·t cháº½ vÃ  biá»‡n há»™ dá»±a trÃªn cÃ¡c cÃ¢u há»i nghiÃªn cá»©u. TÃ i liá»‡u nÃ y thá»±c hiá»‡n nghÄ©a vá»¥ Ä‘Ã³ trong vai trÃ² Nhiá»‡m vá»¥ 3.1 trong chuá»—i bÃ n giao capstone DSP391m.

---

## 2. CÃ¢u há»i NghiÃªn cá»©u vÃ  Nhu cáº§u Dá»¯ liá»‡u

Ba cÃ¢u há»i nghiÃªn cá»©u Ä‘áº·t ra cÃ¡c yÃªu cáº§u dá»¯ liá»‡u riÃªng biá»‡t:

- **CH1** (Má»‘c tin cáº­y sá»›m nháº¥t): Ä‘Ã²i há»i há»“ sÆ¡ cÃ³ chá»‰ sá»‘ thá»i gian vá» hÃ nh vi vÃ  thÃ nh tÃ­ch cá»§a tá»«ng sinh viÃªn Ä‘á»ƒ cÃ¡c Ä‘áº·c trÆ°ng cÃ³ thá»ƒ Ä‘Æ°á»£c tÃ­nh toÃ¡n táº¡i nhiá»u ngÆ°á»¡ng tiáº¿n Ä‘á»™ rá»i ráº¡c (vÃ­ dá»¥: 20%, 40%, 60%, 80% Ä‘á»™ dÃ i khÃ³a há»c). Äiá»u nÃ y Ä‘Ã²i há»i cáº£ sá»± kiá»‡n clickstream (luá»“ng nháº¥p chuá»™t) láº«n bÃ i ná»™p kiá»ƒm tra mang thÃ´ng tin ngÃ y thÃ¡ng, cÃ¹ng vá»›i tá»•ng thá»i lÆ°á»£ng khÃ³a há»c lÃ m cÆ¡ sá»Ÿ tÃ­nh pháº§n trÄƒm tiáº¿n Ä‘á»™.

- **CH2** (Äá»™ á»•n Ä‘á»‹nh giáº£i thÃ­ch): Ä‘Ã²i há»i cÃ¹ng cÃ¡c vectÆ¡ Ä‘áº·c trÆ°ng dÃ¹ng cho dá»± Ä‘oÃ¡n pháº£i cÃ³ máº·t táº¡i má»—i má»‘c kiá»ƒm tra Ä‘á»ƒ giÃ¡ trá»‹ phÃ¢n bá»• SHAP vÃ  LIME cÃ³ thá»ƒ Ä‘Æ°á»£c so sÃ¡nh theo thá»i gian. KhÃ´ng cáº§n thÃªm báº£ng nÃ o ngoÃ i nhá»¯ng báº£ng phá»¥c vá»¥ CH1, nhÆ°ng Ä‘iá»u nÃ y cá»§ng cá»‘ yÃªu cáº§u vá» cÃ¡c cá»™t Ä‘áº·c trÆ°ng nháº¥t quÃ¡n vÃ  Ä‘Æ°á»£c Ä‘á»‹nh nghÄ©a rÃµ rÃ ng.

- **CH3** (Xá»­ lÃ½ máº¥t cÃ¢n báº±ng): Ä‘Ã²i há»i nhÃ£n káº¿t quáº£ nhá»‹ phÃ¢n vÃ  thÃ´ng tin vá» phÃ¢n phá»‘i biÃªn cá»§a nÃ³ trong toÃ n bá»™ táº­p dá»¯ liá»‡u. Cáº£ SMOTE/ADASYN (tá»•ng há»£p máº«u lá»›p thiá»ƒu sá»‘) láº«n Ä‘iá»u chá»‰nh trá»ng sá»‘ lá»›p Ä‘á»u hoáº¡t Ä‘á»™ng trÃªn cá»™t nhÃ£n vÃ  toÃ n bá»™ ma tráº­n Ä‘áº·c trÆ°ng. Äiá»u nÃ y lÃ m cho biáº¿n káº¿t quáº£ vÃ  toÃ n bá»™ táº­p Ä‘áº·c trÆ°ng Ä‘á»u cáº§n thiáº¿t.

---

## 3. YÃªu cáº§u Dá»¯ liá»‡u Ãnh xáº¡ tá»›i CÃ¡c Báº£ng OULAD

Báº£ng 1 trÃ¬nh bÃ y tá»«ng yÃªu cáº§u dá»¯ liá»‡u, cÃ¢u há»i nghiÃªn cá»©u mÃ  nÃ³ phá»¥c vá»¥, vÃ  báº£ng nguá»“n OULAD cung cáº¥p dá»¯ liá»‡u Ä‘Ã³.

**Báº£ng 1. YÃªu cáº§u Dá»¯ liá»‡u vÃ  Nguá»“n OULAD**

| YÃªu cáº§u | Má»¥c Ä‘Ã­ch / LÃ½ do cáº§n thiáº¿t | Báº£ng nguá»“n OULAD | Cá»™t chÃ­nh |
|---|---|---|---|
| NhÃ£n káº¿t quáº£ nhá»‹ phÃ¢n (at-risk) | Äá»‹nh nghÄ©a má»¥c tiÃªu dá»± Ä‘oÃ¡n; cáº§n thiáº¿t cho cáº£ ba CH | `studentInfo` | `final_result` (Pass/Distinction â†’ khÃ´ng nguy cÆ¡; Fail/Withdrawn â†’ cÃ³ nguy cÆ¡) |
| HÃ nh vi tÆ°Æ¡ng tÃ¡c cÃ³ dáº¥u thá»i gian | CH1 cáº§n tÃ­n hiá»‡u cÃ³ nháº­n thá»©c thá»i gian Ä‘á»ƒ xÃ¢y dá»±ng Ä‘áº·c trÆ°ng táº¡i má»‘c kiá»ƒm tra; CH2 cáº§n Ä‘áº·c trÆ°ng tÆ°Æ¡ng tÃ¡c nháº¥t quÃ¡n | `studentVle` (~10,6 triá»‡u hÃ ng), `vle` | `date`, `sum_clicks`, `id_site`, `activity_type` |
| ThÃ nh tÃ­ch há»c táº­p theo chiá»u dá»c | TÃ­n hiá»‡u Ä‘iá»ƒm sá»‘ sá»›m cho Ä‘áº·c trÆ°ng táº¡i má»‘c kiá»ƒm tra (CH1, CH2); Ä‘Ã³ng gÃ³p vÃ o cáº¥u trÃºc lá»›p (CH3) | `studentAssessment`, `assessments` | `date_submitted`, `score`, `is_banked`, `assessment_type`, `weight`, `date` (háº¡n chÃ³t) |
| Ngá»¯ cáº£nh nhÃ¢n kháº©u há»c | Äáº·c trÆ°ng thá»© cáº¥p phá»¥c vá»¥ phÃ¢n tÃ­ch cÃ´ng báº±ng vÃ  Ä‘áº§u vÃ o mÃ´ hÃ¬nh (táº¥t cáº£ CH) | `studentInfo` | `gender`, `region`, `highest_evansonation`, `imd_band`, `age_band`, `num_of_prev_attempts`, `studied_credits`, `disability` |
| Lá»‹ch Ä‘Äƒng kÃ½ cá»§a sinh viÃªn | Ghi nháº­n Ä‘Äƒng kÃ½ muá»™n vÃ  há»§y Ä‘Äƒng kÃ½ sá»›m nhÆ° tÃ­n hiá»‡u hÃ nh vi (CH1) | `studentRegistration` | `date_registration`, `date_unregistration` |
| Lá»‹ch trÃ¬nh / thá»i lÆ°á»£ng khÃ³a há»c | Chuyá»ƒn Ä‘á»•i ngÃ y sá»± kiá»‡n thÃ´ thÃ nh pháº§n trÄƒm tiáº¿n Ä‘á»™ khÃ³a há»c (CH1) | `courses` | `module_presentation_length` |

---

## 4. NhÃ³m Äáº·c trÆ°ng vÃ  Biáº¿n Má»¥c tiÃªu

Ba nhÃ³m Ä‘áº·c trÆ°ng Ä‘Æ°á»£c xÃ¢y dá»±ng tá»« cÃ¡c báº£ng Ä‘Ã£ xÃ¡c Ä‘á»‹nh, cÃ¹ng vá»›i biáº¿n má»¥c tiÃªu:

**4.1 Äáº·c trÆ°ng NhÃ¢n kháº©u há»c (Demographic Features)**
Láº¥y tá»« `studentInfo` vÃ  `studentRegistration`. Bao gá»“m giá»›i tÃ­nh, khu vá»±c, trÃ¬nh Ä‘á»™ há»c váº¥n cao nháº¥t trÆ°á»›c Ä‘Ã³, chá»‰ sá»‘ thiá»‡t thÃ²i IMD (IMD deprivation band), nhÃ³m tuá»•i, sá»‘ láº§n thá»­ trÆ°á»›c Ä‘Ã³, sá»‘ tÃ­n chá»‰ Ä‘Äƒng kÃ½, tÃ¬nh tráº¡ng khuyáº¿t táº­t, ngÃ y Ä‘Äƒng kÃ½, vÃ  (náº¿u cÃ³) ngÃ y há»§y Ä‘Äƒng kÃ½. Äáº·c trÆ°ng nhÃ¢n kháº©u há»c lÃ  tÄ©nh theo tá»«ng báº£n ghi sinh viÃªn-há»c pháº§n-Ä‘á»£t trÃ¬nh bÃ y vÃ  Ä‘Ã³ng vai trÃ² lÃ  biáº¿n hiá»‡p biáº¿n ná»n.

**4.2 Äáº·c trÆ°ng TÆ°Æ¡ng tÃ¡c (VLE â€” Virtual Learning Environment)**
Láº¥y tá»« `studentVle` (sá»± kiá»‡n tÆ°Æ¡ng tÃ¡c) káº¿t ná»‘i vá»›i `vle` (siÃªu dá»¯ liá»‡u loáº¡i hoáº¡t Ä‘á»™ng). Dá»¯ liá»‡u clickstream thÃ´ (~10.655.280 tÆ°Æ¡ng tÃ¡c) Ä‘Æ°á»£c tá»•ng há»£p theo sinh viÃªn, há»c pháº§n-Ä‘á»£t trÃ¬nh bÃ y, vÃ  má»‘c tiáº¿n Ä‘á»™ khÃ³a há»c Ä‘á»ƒ táº¡o ra sá»‘ lÆ°á»£ng vÃ  tá»‘c Ä‘á»™ hoáº¡t Ä‘á»™ng theo tá»«ng loáº¡i (vÃ­ dá»¥: `oucontent`, `quiz`, `resource`, `forumng`). Cá»™t `date` trong `studentVle` lÃ  thiáº¿t yáº¿u: Ä‘Ã¢y lÃ  neo thá»i gian cho phÃ©p Ä‘áº·c trÆ°ng Ä‘Æ°á»£c cáº¯t ngáº¯n táº¡i má»—i ngÆ°á»¡ng má»‘c kiá»ƒm tra.

**4.3 Äáº·c trÆ°ng ThÃ nh tÃ­ch (Assessment â€” Kiá»ƒm tra)**
Láº¥y tá»« `studentAssessment` (há»“ sÆ¡ ná»™p bÃ i) káº¿t ná»‘i vá»›i `assessments` (siÃªu dá»¯ liá»‡u kiá»ƒm tra). Äáº·c trÆ°ng bao gá»“m Ä‘iá»ƒm trung bÃ¬nh cÃ³ trá»ng sá»‘ lÅ©y tÃ­ch, tá»· lá»‡ bÃ i kiá»ƒm tra ná»™p Ä‘Ãºng háº¡n, vÃ  viá»‡c cÃ³ bÃ i kiá»ƒm tra nÃ o Ä‘Æ°á»£c lÆ°u ngÃ¢n hÃ ng (banked) hay khÃ´ng. Cá»™t `date_submitted` trong `studentAssessment` cho phÃ©p cáº¯t ngáº¯n theo thá»i gian tÆ°Æ¡ng tá»± nhÆ° cÃ¡ch tiáº¿p cáº­n Ä‘á»‘i vá»›i Ä‘áº·c trÆ°ng tÆ°Æ¡ng tÃ¡c VLE.

**4.4 Biáº¿n Má»¥c tiÃªu**
NhÃ£n nhá»‹ phÃ¢n Ä‘Æ°á»£c suy diá»…n tá»« `final_result` trong `studentInfo`. CÃ¡c báº£n ghi vá»›i `final_result` âˆˆ {Fail, Withdrawn} Ä‘Æ°á»£c gÃ¡n nhÃ£n cÃ³ nguy cÆ¡ (lá»›p dÆ°Æ¡ng = 1); cÃ¡c báº£n ghi {Pass, Distinction} Ä‘Æ°á»£c gÃ¡n nhÃ£n khÃ´ng nguy cÆ¡ (0). Tá»· lá»‡ cÃ³ nguy cÆ¡ quan sÃ¡t Ä‘Æ°á»£c trong toÃ n bá»™ táº­p dá»¯ liá»‡u xáº¥p xá»‰ 52,8%, cho tháº¥y máº¥t cÃ¢n báº±ng lá»›p nháº¹, lÃ  Ä‘á»™ng lá»±c cho CH3.

---

## 5. Háº¡t nhÃ¢n Dá»¯ liá»‡u vÃ  KhÃ³a Tá»•ng há»£p

ÄÆ¡n vá»‹ phÃ¢n tÃ­ch lÃ  má»™t báº£n ghi trÃªn má»—i bá»™ ba **(id\_student, code\_module, code\_presentation)**. VÃ¬ má»™t sinh viÃªn cÃ³ thá»ƒ Ä‘Äƒng kÃ½ nhiá»u há»c pháº§n-Ä‘á»£t trÃ¬nh bÃ y, khÃ³a tá»•ng há»£p (composite key) gá»“m ba cá»™t nÃ y lÃ  báº¯t buá»™c Ä‘á»ƒ xÃ¡c Ä‘á»‹nh duy nháº¥t má»—i quan sÃ¡t. Táº¥t cáº£ cÃ¡c báº£ng Ä‘áº·c trÆ°ng Ä‘Æ°á»£c káº¿t ná»‘i theo khÃ³a tá»•ng há»£p nÃ y trÆ°á»›c khi tiáº¿n hÃ nh mÃ´ hÃ¬nh hÃ³a. Táº­p dá»¯ liá»‡u phÃ¢n tÃ­ch cuá»‘i cÃ¹ng chá»©a **32.593** báº£n ghi nhÆ° váº­y, láº¥y tá»« **28.785** sinh viÃªn duy nháº¥t trÃªn **22** Ä‘á»£t trÃ¬nh bÃ y há»c pháº§n.

---

## 6. Vai trÃ² cá»§a Tá»«ng Báº£ng OULAD

Báº£ng 2 tÃ³m táº¯t lÃ½ do táº¥t cáº£ báº£y báº£ng OULAD Ä‘á»u cáº§n thiáº¿t vÃ  chá»‰ ra báº£ng nÃ o cÃ³ chá»‰ sá»‘ thá»i gian.

**Báº£ng 2. Vai trÃ² CÃ¡c Báº£ng OULAD**

| Báº£ng | Vai trÃ² trong NghiÃªn cá»©u nÃ y | CÃ³ chá»‰ sá»‘ thá»i gian? |
|---|---|---|
| `studentInfo` | Cung cáº¥p nhÃ£n káº¿t quáº£ vÃ  táº¥t cáº£ Ä‘áº·c trÆ°ng nhÃ¢n kháº©u há»c | KhÃ´ng |
| `studentRegistration` | Cung cáº¥p ngÃ y Ä‘Äƒng kÃ½ vÃ  ngÃ y há»§y Ä‘Äƒng kÃ½ theo tá»«ng láº§n ghi danh | Má»™t pháº§n (`date_registration`, `date_unregistration`) |
| `studentVle` | Nguá»“n chÃ­nh cá»§a hÃ nh vi tÆ°Æ¡ng tÃ¡c; ~10,6 triá»‡u sá»± kiá»‡n clickstream | CÃ³ (`date`) |
| `vle` | Ãnh xáº¡ `id_site` tá»›i `activity_type`; cáº§n Ä‘á»ƒ táº¡o Ä‘áº·c trÆ°ng tÆ°Æ¡ng tÃ¡c theo loáº¡i | KhÃ´ng |
| `studentAssessment` | Há»“ sÆ¡ ná»™p bÃ i kiá»ƒm tra vá»›i ngÃ y ná»™p vÃ  Ä‘iá»ƒm sá»‘ | CÃ³ (`date_submitted`) |
| `assessments` | Cung cáº¥p loáº¡i kiá»ƒm tra, trá»ng sá»‘, vÃ  ngÃ y háº¡n chÃ³t; cáº§n Ä‘á»ƒ tÃ­nh Ä‘áº·c trÆ°ng thÃ nh tÃ­ch cÃ³ trá»ng sá»‘ | Má»™t pháº§n (`date` lÃ  háº¡n chÃ³t) |
| `courses` | Cung cáº¥p `module_presentation_length` Ä‘á»ƒ chuyá»ƒn Ä‘á»•i ngÃ y sá»± kiá»‡n thÃ nh pháº§n trÄƒm tiáº¿n Ä‘á»™ | KhÃ´ng |

CÃ¡c cá»™t cÃ³ chá»‰ sá»‘ thá»i gianâ€”`studentVle.date` vÃ  `studentAssessment.date_submitted`â€”lÃ  ná»n táº£ng kiáº¿n trÃºc cá»§a yÃªu cáº§u cÃ³ nháº­n thá»©c thá»i gian. Náº¿u thiáº¿u chÃºng, viá»‡c cáº¯t ngáº¯n theo má»‘c kiá»ƒm tra (thiáº¿t yáº¿u cho CH1 vÃ  CH2) khÃ´ng thá»ƒ thá»±c hiá»‡n Ä‘Æ°á»£c.

---

## 7. Quy mÃ´ Dá»¯ liá»‡u vÃ  TÃ­nh Äáº§y Ä‘á»§

CÃ¡c thá»‘ng kÃª quy mÃ´ sau Ä‘Ã¢y xÃ¡c nháº­n OULAD Ä‘á»§ Ä‘iá»u kiá»‡n cho nghiÃªn cá»©u dá»± kiáº¿n:

- **32.593** báº£n ghi sinh viÃªn-há»c pháº§n-Ä‘á»£t trÃ¬nh bÃ y (háº¡t nhÃ¢n phÃ¢n tÃ­ch)
- **28.785** sinh viÃªn duy nháº¥t
- **22** Ä‘á»£t trÃ¬nh bÃ y há»c pháº§n (7 khÃ³a há»c Ã— nhiá»u nÄƒm trÃ¬nh bÃ y)
- **7** báº£ng quan há»‡
- **10.655.280** hÃ ng tÆ°Æ¡ng tÃ¡c VLE
- **173.912** hÃ ng ná»™p bÃ i kiá»ƒm tra
- **~52,8%** tá»· lá»‡ cÃ³ nguy cÆ¡ (máº¥t cÃ¢n báº±ng nháº¹; biá»‡n há»™ cho CH3 nhÆ°ng khÃ´ng háº¡n cháº¿ nghiÃªm trá»ng viá»‡c mÃ´ hÃ¬nh hÃ³a)

Quy mÃ´ táº­p dá»¯ liá»‡u Ä‘á»§ Ä‘á»ƒ huáº¥n luyá»‡n vÃ  Ä‘Ã¡nh giÃ¡ nhiá»u bá»™ phÃ¢n loáº¡i táº¡i má»—i ngÆ°á»¡ng má»‘c kiá»ƒm tra, táº¡o ra cÃ¡c phÃ¢n bá»• SHAP/LIME á»•n Ä‘á»‹nh, vÃ  so sÃ¡nh ba chiáº¿n lÆ°á»£c xá»­ lÃ½ máº¥t cÃ¢n báº±ng. Äá»™ chi tiáº¿t thá»i gian (Ä‘á»™ phÃ¢n giáº£i hÃ ng ngÃ y trong cáº£ `studentVle` vÃ  `studentAssessment`) Ä‘á»§ Ä‘á»ƒ hiá»‡n thá»±c hÃ³a cÃ¡c ngÆ°á»¡ng má»‘c kiá»ƒm tra táº¡i cÃ¡c khoáº£ng cÃ¡ch tinh táº¿.

---

## 8. Káº¿t luáº­n vá» TÃ­nh Äáº§y Ä‘á»§ cá»§a Dá»¯ liá»‡u

OULAD cung cáº¥p táº¥t cáº£ cÃ¡c nhÃ³m dá»¯ liá»‡u yÃªu cáº§u bá»Ÿi CH1â€“CH3: nhÃ£n káº¿t quáº£ nhá»‹ phÃ¢n, hÃ nh vi tÆ°Æ¡ng tÃ¡c cÃ³ dáº¥u thá»i gian, thÃ nh tÃ­ch kiá»ƒm tra theo chiá»u dá»c, vÃ  ngá»¯ cáº£nh nhÃ¢n kháº©u há»c. KhÃ³a tá»•ng há»£p `(id_student, code_module, code_presentation)` Ä‘áº£m báº£o liÃªn káº¿t khÃ´ng mÆ¡ há»“ qua táº¥t cáº£ báº£y báº£ng. Vá»›i hÆ¡n 32.000 báº£n ghi phÃ¢n tÃ­ch, hÆ¡n 10,6 triá»‡u sá»± kiá»‡n tÆ°Æ¡ng tÃ¡c cÃ³ dáº¥u thá»i gian, vÃ  Ä‘á»™ phÃ¢n giáº£i thá»i gian má»™t ngÃ y, táº­p dá»¯ liá»‡u cung cáº¥p quy mÃ´ vÃ  Ä‘á»™ chi tiáº¿t Ä‘á»§ Ä‘á»ƒ há»— trá»£ mÃ´ hÃ¬nh hÃ³a má»‘c kiá»ƒm tra cÃ³ nháº­n thá»©c thá»i gian, phÃ¢n tÃ­ch Ä‘á»™ á»•n Ä‘á»‹nh giáº£i thÃ­ch, vÃ  thá»­ nghiá»‡m xá»­ lÃ½ máº¥t cÃ¢n báº±ng. KhÃ´ng cáº§n nguá»“n dá»¯ liá»‡u bÃªn ngoÃ i nÃ o Ä‘á»ƒ giáº£i quyáº¿t ba cÃ¢u há»i nghiÃªn cá»©u.

---

## TÃ i liá»‡u Tham kháº£o

[3] J. Kuzilek, M. Hlosta, Z. Zdrahal, "Open University Learning Analytics dataset," *Scientific Data*, vol. 4, art. 170171, 2017.

