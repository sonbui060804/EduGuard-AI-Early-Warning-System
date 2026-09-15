# Chuáº©n HÃ³a vÃ  Biáº¿n Äá»•i Dá»¯ Liá»‡u: PhÃ¢n Loáº¡i Biáº¿n, MÃ£ HÃ³a vÃ  Chiáº¿n LÆ°á»£c Thang Äo

**DSP391m â€“ NhÃ³m 5 Â· BÃ¡o cÃ¡o 2 (Nhiá»‡m vá»¥ Dá»¯ liá»‡u), ChÆ°Æ¡ng 3 Â· Nhiá»‡m vá»¥ 3.4 â€” Chuáº©n hÃ³a & Biáº¿n Ä‘á»•i**

---

## TÃ³m táº¯t (Abstract)

BÃ¡o cÃ¡o nÃ y ghi láº¡i danh má»¥c phÃ¢n loáº¡i biáº¿n, cÃ¡c quyáº¿t Ä‘á»‹nh mÃ£ hÃ³a (encoding) vÃ  chiáº¿n lÆ°á»£c chuáº©n hÃ³a thang Ä‘o (standardisation) Ä‘Æ°á»£c triá»ƒn khai trong `src/features/preprocessing.py` thuá»™c dá»± Ã¡n há»c pháº§n DSP391m (NhÃ³m 5). Táº­p dá»¯ liá»‡u, Ä‘Æ°á»£c trÃ­ch xuáº¥t tá»« bá»™ dá»¯ liá»‡u phÃ¢n tÃ­ch há»c táº­p cá»§a Äáº¡i há»c Má»Ÿ Anh (OULAD), chá»©a 28 Ä‘áº·c trÆ°ng thÃ´ vÃ  phÃ¡i sinh bao gá»“m tÆ°Æ¡ng tÃ¡c nháº¥p chuá»™t (clickstream), thuá»™c tÃ­nh nhÃ¢n kháº©u há»c vÃ  chá»‰ sá»‘ káº¿t quáº£ há»c táº­p. Má»—i Ä‘áº·c trÆ°ng Ä‘Æ°á»£c gÃ¡n vÃ o má»™t trong nÄƒm danh má»¥c kiá»ƒu â€” Ä‘á»‹nh lÆ°á»£ng (numeric), thá»© báº­c (ordinal), danh Ä‘á»‹nh (nominal), nhá»‹ phÃ¢n (binary) hoáº·c chá»‰ bÃ¡o (indicator) â€” vÃ  Ä‘Æ°á»£c xá»­ lÃ½ bá»Ÿi transformer tÆ°Æ¡ng á»©ng tÆ°Æ¡ng thÃ­ch vá»›i sklearn trong má»™t `ColumnTransformer` duy nháº¥t. Má»™t quy trÃ¬nh phÃ²ng trÃ¡nh rÃ² rá»‰ thÃ´ng tin (anti-leakage) nghiÃªm ngáº·t quy Ä‘á»‹nh trÃ¬nh tá»± cÃ¡c bÆ°á»›c: toÃ n bá»™ bá»™ mÃ£ hÃ³a vÃ  `StandardScaler` chá»‰ Ä‘Æ°á»£c khá»›p (fit) trÃªn táº­p huáº¥n luyá»‡n vÃ  sau Ä‘Ã³ Ã¡p dá»¥ng cho cáº£ táº­p huáº¥n luyá»‡n láº«n táº­p kiá»ƒm tra. Giai Ä‘oáº¡n biáº¿n Ä‘á»•i táº¡o ra ma tráº­n Ä‘áº·c trÆ°ng dÃ y Ä‘áº·c (dense) 49 cá»™t, Ä‘Æ°á»£c xÃ¡c minh khÃ´ng cÃ³ giÃ¡ trá»‹ khuyáº¿t (NaN), vá»›i tÃªn Ä‘áº·c trÆ°ng Ä‘Æ°á»£c giá»¯ nguyÃªn theo chuáº©n `snake_case` phá»¥c vá»¥ phÃ¢n tÃ­ch diá»…n giáº£i mÃ´ hÃ¬nh (explainability) báº±ng SHAP vÃ  LIME á»Ÿ cÃ¡c bÆ°á»›c tiáº¿p theo.

---

## 1. Giá»›i thiá»‡u

Má»™t pipeline há»c mÃ¡y (machine learning) hiá»‡u quáº£ Ä‘Ã²i há»i cÃ¡c giÃ¡ trá»‹ Ä‘áº·c trÆ°ng thÃ´ pháº£i Ä‘Æ°á»£c chuyá»ƒn Ä‘á»•i thÃ nh biá»ƒu diá»…n sá»‘ vá»«a phÃ¹ há»£p vá» máº·t toÃ¡n há»c vá»›i tá»«ng lá»›p mÃ´ hÃ¬nh, vá»«a khÃ´ng bá»‹ nhiá»…m thÃ´ng tin rÃ² rá»‰ tá»« dá»¯ liá»‡u kiá»ƒm tra chÆ°a tháº¥y. Trong bÃ i toÃ¡n dá»± Ä‘oÃ¡n sinh viÃªn cÃ³ nguy cÆ¡ (at-risk) cá»§a DSP391m, cÃ¡c Ä‘áº·c trÆ°ng báº¯t nguá»“n tá»« ba thang Ä‘o khÃ¡c nhau: sá»‘ Ä‘áº¿m liÃªn tá»¥c vÃ  rá»i ráº¡c tá»« nháº­t kÃ½ nháº¥p chuá»™t VLE, thuá»™c tÃ­nh phÃ¢n loáº¡i cÃ³ thá»© tá»± thu tháº­p khi Ä‘Äƒng kÃ½ há»c, vÃ  Ä‘á»‹nh danh phÃ¢n loáº¡i khÃ´ng cÃ³ thá»© tá»±. Ãp dá»¥ng má»™t chiáº¿n lÆ°á»£c mÃ£ hÃ³a duy nháº¥t cho táº¥t cáº£ cÃ¡c Ä‘áº·c trÆ°ng â€” vÃ­ dá»¥ nhÆ° dÃ¹ng `OneHotEncoder` cho biáº¿n thá»© báº­c â€” sáº½ loáº¡i bá» thÃ´ng tin thá»© háº¡ng ná»™i táº¡i cá»§a cÃ¡c danh má»¥c nhÆ° trÃ¬nh Ä‘á»™ há»c váº¥n hay dáº£i tÆ°á»›c Ä‘oáº¡t, lÃ m phÃ¬nh to sá»‘ chiá»u khÃ´ng gian Ä‘áº·c trÆ°ng mÃ  khÃ´ng tÄƒng thÃªm giÃ¡ trá»‹ thÃ´ng tin. NgÆ°á»£c láº¡i, Ã¡p dá»¥ng mÃ£ sá»‘ nguyÃªn cho biáº¿n danh Ä‘á»‹nh nhÆ° `region` sáº½ Ã¡p Ä‘áº·t má»™t quan há»‡ thá»© tá»± sai lá»‡ch. Má»¥c 2 liá»‡t kÃª danh má»¥c phÃ¢n loáº¡i biáº¿n giáº£i quyáº¿t cÃ¡c phÃ¢n biá»‡t nÃ y. Má»¥c 3 trÃ¬nh bÃ y chi tiáº¿t tá»«ng phÆ°Æ¡ng phÃ¡p mÃ£ hÃ³a vÃ  cÄƒn cá»© ká»¹ thuáº­t. Má»¥c 4 mÃ´ táº£ bÆ°á»›c chuáº©n hÃ³a vÃ  cÃ¡ch triá»ƒn khai phÃ²ng trÃ¡nh rÃ² rá»‰. Má»¥c 5 trÃ¬nh bÃ y trÃ¬nh tá»± pipeline biáº¿n Ä‘á»•i. Má»¥c 6 bÃ¡o cÃ¡o cÃ¡c thuá»™c tÃ­nh Ä‘áº§u ra Ä‘Ã£ Ä‘Æ°á»£c xÃ¡c minh.

---

## 2. Danh má»¥c PhÃ¢n loáº¡i Biáº¿n

28 Ä‘áº·c trÆ°ng Ä‘áº§u vÃ o (loáº¡i trá»« biáº¿n má»¥c tiÃªu `at_risk` vÃ  cÃ¡c cá»™t Ä‘á»‹nh danh `id_student`, `code_module`, `code_presentation`) Ä‘Æ°á»£c chia thÃ nh nÄƒm kiá»ƒu. Viá»‡c phÃ¢n loáº¡i kiá»ƒu biáº¿n quyáº¿t Ä‘á»‹nh lá»±a chá»n transformer trong `ColumnTransformer` tiáº¿p theo.

**Báº£ng 1. PhÃ¢n loáº¡i biáº¿n vÃ  gÃ¡n bá»™ mÃ£ hÃ³a / chuáº©n hÃ³a**

| Kiá»ƒu | Sá»‘ lÆ°á»£ng | Biáº¿n | Bá»™ mÃ£ hÃ³a / Chuáº©n hÃ³a |
|------|---------|------|------------------------|
| Äá»‹nh lÆ°á»£ng (Numeric) | 19 | `num_of_prev_attempts`, `studied_credits`, `date_registration`, `total_clicks`, `n_days_active`, `clicks_forumng`, `clicks_oucontent`, `clicks_resource`, `clicks_homepage`, `clicks_oucollaborate`, `clicks_quiz`, `clicks_subpage`, `clicks_url`, `max_clicks_single_day`, `mean_clicks_per_active_day`, `days_since_last_activity`, `mean_score_to_date`, `n_assessments_submitted`, `weighted_score_to_date` | `StandardScaler` (má»™t sá»‘ Ä‘áº·c trÆ°ng Ä‘Æ°á»£c log1p / winsorize trÆ°á»›c á»Ÿ giai Ä‘oáº¡n xá»­ lÃ½ ngoáº¡i lai) |
| Thá»© báº­c (Ordinal) | 3 | `highest_evansonation`, `imd_band`, `age_band` | `OrdinalEncoder` vá»›i thá»© tá»± danh má»¥c cá»‘ Ä‘á»‹nh, tÆ°á»ng minh |
| Danh Ä‘á»‹nh (Nominal) | 3 | `region`, `code_module`, `code_presentation` | `OneHotEncoder` |
| Nhá»‹ phÃ¢n (Binary) | 2 | `gender`, `disability` | Ãnh xáº¡ 0/1 trá»±c tiáº¿p qua `BinaryEncoder` tÃ¹y chá»‰nh |
| Chá»‰ bÃ¡o (Indicator) | 1 | `not_submitted` | Passthrough (Ä‘Ã£ lÃ  0/1 tá»« bÆ°á»›c feature engineering) |

**Ghi chÃº vá» phÃ¢n nhÃ³m con trong biáº¿n Ä‘á»‹nh lÆ°á»£ng.** Trong 19 biáº¿n Ä‘á»‹nh lÆ°á»£ng, cÃ¡c sá»‘ Ä‘áº¿m nháº¥p chuá»™t VLE (`total_clicks`, `n_days_active`, vÃ  toÃ n bá»™ tÃ¡m cá»™t `clicks_<type>`, cÃ¹ng vá»›i `max_clicks_single_day` vÃ  `mean_clicks_per_active_day`) cÃ³ phÃ¢n phá»‘i lá»‡ch pháº£i máº¡nh vÃ  Ä‘Æ°á»£c biáº¿n Ä‘á»•i trÆ°á»›c báº±ng `log1p` trÆ°á»›c khi Ã¡p dá»¥ng `StandardScaler`. CÃ¡c biáº¿n `studied_credits`, `num_of_prev_attempts`, `weighted_score_to_date` vÃ  `days_since_last_activity` Ä‘Æ°á»£c winsorize á»Ÿ phÃ¢n vá»‹ thá»© 1 vÃ  thá»© 99. Ba biáº¿n â€” `mean_score_to_date`, `n_assessments_submitted` vÃ  `date_registration` â€” khÃ´ng nháº­n báº¥t ká»³ biáº¿n Ä‘á»•i ngoáº¡i lai nÃ o.

---

## 3. CÃ¡c PhÆ°Æ¡ng phÃ¡p MÃ£ hÃ³a vÃ  CÄƒn cá»© Ká»¹ thuáº­t

### 3.1 OrdinalEncoder (biáº¿n thá»© báº­c)

Biáº¿n thá»© báº­c (ordinal) cÃ³ thá»© tá»± xáº¿p háº¡ng ná»™i táº¡i mang thÃ´ng tin dá»± Ä‘oÃ¡n. MÃ£ hÃ³a chÃºng thÃ nh cÃ¡c sá»‘ nguyÃªn 0, 1, 2, â€¦ kâˆ’1 báº£o toÃ n thá»© tá»± nÃ y mÃ  khÃ´ng lÃ m tÄƒng sá»‘ chiá»u. `OneHotEncoder` sáº½ phÃ¡ há»§y quan há»‡ thá»© háº¡ng; do Ä‘Ã³ nÃ³ Ä‘Æ°á»£c loáº¡i trá»« tÆ°á»ng minh cho cÃ¡c biáº¿n nÃ y.

Thá»© tá»± danh má»¥c chÃ­nh xÃ¡c Ä‘Æ°á»£c cá»‘ Ä‘á»‹nh trong `ORDINAL_ORDERS` lÃ :

- `highest_evansonation`: `No Formal quals` < `Lower Than A Level` < `A Level or Equivalent` < `HE Qualification` < `Post Graduate Qualification`
- `imd_band`: `Unknown` < `0-10%` < `10-20` < `20-30%` < `30-40%` < `40-50%` < `50-60%` < `60-70%` < `70-80%` < `80-90%` < `90-100%`
- `age_band`: `0-35` < `35-55` < `55<=`

Cáº¥u hÃ¬nh `handle_unknown='use_encoded_value'` káº¿t há»£p `unknown_value=-1` Ä‘áº£m báº£o ráº±ng má»i danh má»¥c xuáº¥t hiá»‡n trong táº­p kiá»ƒm tra nhÆ°ng váº¯ng máº·t trong táº­p huáº¥n luyá»‡n sáº½ Ä‘Æ°á»£c gÃ¡n mÃ£ âˆ’1 thay vÃ¬ gÃ¢y lá»—i ngoáº¡i lá»‡ (exception). CÃ¡c mÃ´ hÃ¬nh dá»±a trÃªn cÃ¢y (Random Forest, XGBoost, LightGBM) xá»­ lÃ½ giÃ¡ trá»‹ sentinel nÃ y mÃ  khÃ´ng gáº·p váº¥n Ä‘á».

### 3.2 OneHotEncoder (biáº¿n danh Ä‘á»‹nh)

Biáº¿n danh Ä‘á»‹nh (nominal) â€” `region`, `code_module`, `code_presentation` â€” khÃ´ng cÃ³ thá»© tá»± ná»™i táº¡i. Viá»‡c gÃ¡n mÃ£ sá»‘ nguyÃªn sáº½ Ã¡p Ä‘áº·t má»™t thá»© háº¡ng sai lá»‡ch, vÃ­ dá»¥ ngá»¥ Ã½ má»™t vÃ¹ng Ä‘á»‹a lÃ½ "lá»›n hÆ¡n" vÃ¹ng khÃ¡c. `OneHotEncoder` táº¡o ra má»™t cá»™t nhá»‹ phÃ¢n cho má»—i giÃ¡ trá»‹ danh má»¥c, lÃ m cho phÃ©p mÃ£ hÃ³a báº¥t biáº¿n vá»›i hoÃ¡n vá»‹.

Cáº¥u hÃ¬nh: `handle_unknown='ignore'` (danh má»¥c láº¡ trong táº­p kiá»ƒm tra táº¡o ra hÃ ng toÃ n sá»‘ khÃ´ng, trÃ¡nh lá»—i runtime); `sparse_output=False` (máº£ng dÃ y Ä‘áº·c Ä‘á»ƒ tÆ°Æ¡ng thÃ­ch pipeline); `drop=None` (giá»¯ láº¡i táº¥t cáº£ cÃ¡c cá»™t). Lá»±a chá»n `drop=None` lÃ  chá»§ Ã½: viá»‡c loáº¡i bá» má»™t cá»™t tham chiáº¿u sáº½ ngÄƒn SHAP waterfall plot vÃ  LIME gÃ¡n táº§m quan trá»ng (importance) cho danh má»¥c bá»‹ loáº¡i bá» Ä‘Ã³, lÃ m giáº£m kháº£ nÄƒng diá»…n giáº£i sau thá»±c nghiá»‡m (post-hoc interpretability).

### 3.3 BinaryEncoder (biáº¿n nhá»‹ phÃ¢n)

Hai Ä‘áº·c trÆ°ng chá»‰ nháº­n Ä‘Ãºng hai giÃ¡ trá»‹:

- `gender`: M â†’ 1, F â†’ 0
- `disability`: Y â†’ 1, N â†’ 0

Má»™t lá»›p `BinaryEncoder` tÃ¹y chá»‰nh (káº¿ thá»«a `BaseEstimator` / `TransformerMixin` cá»§a sklearn) triá»ƒn khai báº£ng tra cá»©u cá»‘ Ä‘á»‹nh nÃ y. KhÃ´ng cáº§n bÆ°á»›c fit thá»±c sá»± vÃ¬ Ã¡nh xáº¡ lÃ  háº±ng sá»‘ Ä‘Æ°á»£c Ä‘á»‹nh nghÄ©a trong dá»± Ã¡n; phÆ°Æ¡ng thá»©c `fit` lÃ  no-op Ä‘Æ°á»£c giá»¯ láº¡i Ä‘á»ƒ tÆ°Æ¡ng thÃ­ch vá»›i `ColumnTransformer`.

### 3.4 Passthrough (Ä‘áº·c trÆ°ng chá»‰ bÃ¡o)

Cá» `not_submitted` Ä‘Æ°á»£c táº¡o ra bá»Ÿi bÆ°á»›c feature engineering dÆ°á»›i dáº¡ng sá»‘ nguyÃªn 0/1 vÃ  khÃ´ng cáº§n biáº¿n Ä‘á»•i thÃªm. NÃ³ Ä‘Æ°á»£c chuyá»ƒn qua `ColumnTransformer` thÃ´ng qua transformer `'passthrough'` Ä‘á»ƒ báº£o toÃ n sá»± hiá»‡n diá»‡n trong ma tráº­n Ä‘áº·c trÆ°ng Ä‘áº§u ra.

---

## 4. Chuáº©n hÃ³a Thang Ä‘o (Standardisation / Scaling)

### 4.1 StandardScaler

ToÃ n bá»™ 19 biáº¿n Ä‘á»‹nh lÆ°á»£ng Ä‘Æ°á»£c chuáº©n hÃ³a vá» trung bÃ¬nh báº±ng khÃ´ng vÃ  phÆ°Æ¡ng sai Ä‘Æ¡n vá»‹ sá»­ dá»¥ng `StandardScaler` cá»§a sklearn (chuáº©n hÃ³a z-score: xâ€² = (x âˆ’ Î¼) / Ïƒ). Sau cÃ¡c biáº¿n Ä‘á»•i log1p hoáº·c winsorize Ä‘Ã£ Ã¡p dá»¥ng trong giai Ä‘oáº¡n xá»­ lÃ½ ngoáº¡i lai, má»—i cá»™t Ä‘á»‹nh lÆ°á»£ng Ä‘Æ°á»£c dá»‹ch chuyá»ƒn vÃ  thu phÃ³ng Ä‘á»™c láº­p sao cho phÃ¢n phá»‘i trÃªn táº­p huáº¥n luyá»‡n cÃ³ trung bÃ¬nh 0 vÃ  Ä‘á»™ lá»‡ch chuáº©n 1.

### 4.2 CÄƒn cá»©

Sá»‘ Ä‘áº¿m nháº¥p chuá»™t VLE dao Ä‘á»™ng tá»« khÃ´ng Ä‘áº¿n vÃ i nghÃ¬n; biáº¿n Ä‘iá»ƒm sá»‘ tráº£i dÃ i tá»« 0 Ä‘áº¿n 100. KhÃ´ng cÃ³ chuáº©n hÃ³a, cÃ¡c mÃ´ hÃ¬nh tÃ­nh khoáº£ng cÃ¡ch hoáº·c Ä‘á»™ lá»›n gradient (Logistic Regression, Máº¡ng nÆ¡-ron nhÃ¢n táº¡o / Artificial Neural Network) sáº½ bá»‹ thá»‘ng trá»‹ bá»Ÿi cÃ¡c biáº¿n clickstream cÃ³ biÃªn Ä‘á»™ cao. Máº·c dÃ¹ cÃ¡c mÃ´ hÃ¬nh dá»±a trÃªn cÃ¢y (Random Forest, XGBoost, LightGBM) phÃ¢n chia trÃªn ngÆ°á»¡ng Ä‘áº·c trÆ°ng vÃ  vá» lÃ½ thuyáº¿t khÃ´ng nháº¡y cáº£m vá»›i thang Ä‘o, `StandardScaler` Ä‘Æ°á»£c Ã¡p dá»¥ng Ä‘á»“ng nháº¥t trÃªn toÃ n bá»™ Ä‘áº·c trÆ°ng Ä‘á»‹nh lÆ°á»£ng Ä‘á»ƒ Ä‘áº£m báº£o tÃ­nh nháº¥t quÃ¡n cá»§a pipeline: má»™t láº§n gá»i `preprocess()` táº¡o ra ma tráº­n Ä‘áº·c trÆ°ng há»£p lá»‡ cho má»i lá»›p mÃ´ hÃ¬nh mÃ  khÃ´ng cáº§n can thiá»‡p thÃªm.

### 4.3 Triá»ƒn khai PhÃ²ng trÃ¡nh RÃ² rá»‰ (Anti-Leakage)

Bá»™ chuáº©n hÃ³a (scaler) chá»‰ Ä‘Æ°á»£c khá»›p (fit) trÃªn táº­p huáº¥n luyá»‡n. CÃ¡c tham sá»‘ Ä‘Ã£ khá»›p (`scaler.mean_` vÃ  `scaler.var_`) Ä‘Æ°á»£c tÃ­nh toÃ¡n hoÃ n toÃ n tá»« cÃ¡c quan sÃ¡t huáº¥n luyá»‡n. PhÆ°Æ¡ng thá»©c `.transform()` â€” Ã¡p dá»¥ng trung bÃ¬nh vÃ  phÆ°Æ¡ng sai Ä‘Ã£ lÆ°u â€” sau Ä‘Ã³ Ä‘Æ°á»£c gá»i trÃªn cáº£ máº£ng huáº¥n luyá»‡n vÃ  kiá»ƒm tra. HÃ m táº¯t `.fit_transform()` khÃ´ng bao giá» Ä‘Æ°á»£c gá»i trÃªn toÃ n bá»™ táº­p dá»¯ liá»‡u. Äiá»u nÃ y ngÄƒn cháº·n báº¥t ká»³ thÃ´ng tin thá»‘ng kÃª nÃ o tá»« táº­p kiá»ƒm tra áº£nh hÆ°á»Ÿng Ä‘áº¿n phÃ©p biáº¿n Ä‘á»•i Ã¡p dá»¥ng lÃªn dá»¯ liá»‡u huáº¥n luyá»‡n, vá»‘n sáº½ cáº¥u thÃ nh rÃ² rá»‰ dá»¯ liá»‡u (data leakage) vÃ  táº¡o ra Æ°á»›c lÆ°á»£ng kháº£ nÄƒng tá»•ng quÃ¡t hÃ³a quÃ¡ láº¡c quan.

**Báº£ng 2. TÃ³m táº¯t mÃ£ hÃ³a vÃ  chuáº©n hÃ³a**

| Transformer | Äáº·c trÆ°ng | Cáº¥u hÃ¬nh chÃ­nh |
|-------------|-----------|----------------|
| `StandardScaler` | 19 biáº¿n Ä‘á»‹nh lÆ°á»£ng | Fit trÃªn train only; `scaler.mean_` tÃ­nh tá»« train |
| `OrdinalEncoder` | 3 biáº¿n thá»© báº­c | Danh sÃ¡ch danh má»¥c tÆ°á»ng minh; `handle_unknown='use_encoded_value'`, `unknown_value=-1` |
| `OneHotEncoder` | 3 biáº¿n danh Ä‘á»‹nh | `handle_unknown='ignore'`, `sparse_output=False`, `drop=None` |
| `BinaryEncoder` (tÃ¹y chá»‰nh) | 2 biáº¿n nhá»‹ phÃ¢n | Báº£ng tra cá»©u cá»‘ Ä‘á»‹nh: M/Yâ†’1, F/Nâ†’0 |
| `passthrough` | 1 biáº¿n chá»‰ bÃ¡o | KhÃ´ng biáº¿n Ä‘á»•i |

---

## 5. TrÃ¬nh tá»± Pipeline Biáº¿n Ä‘á»•i

TrÃ¬nh tá»± pipeline phÃ²ng trÃ¡nh rÃ² rá»‰ Ä‘áº§y Ä‘á»§, Ä‘Æ°á»£c triá»ƒn khai trong `preprocess()`, lÃ :

1. **PhÃ¢n chia train/test** â€” thá»±c hiá»‡n bÃªn ngoÃ i module nÃ y, trÆ°á»›c má»i bÆ°á»›c fit.
2. **`handle_missing(X_train)`** â€” logic Ä‘iá»n khuyáº¿t Ä‘Æ°á»£c rÃºt ra tá»« dá»¯ liá»‡u huáº¥n luyá»‡n; cÃ¹ng quy táº¯c Ä‘Ã³ Ä‘Æ°á»£c Ã¡p dá»¥ng cho táº­p kiá»ƒm tra mÃ  khÃ´ng fit láº¡i.
3. **`handle_outliers(X_train)`** â€” cÃ¡c biáº¿n Ä‘á»•i log1p vÃ  winsorize Ä‘Æ°á»£c Ã¡p dá»¥ng; táº­p kiá»ƒm tra Ä‘Æ°á»£c biáº¿n Ä‘á»•i theo cÃ¹ng quy táº¯c xÃ¡c Ä‘á»‹nh (deterministic).
4. **`ColumnTransformer.fit(X_train)`** â€” táº¥t cáº£ cÃ¡c transformer (StandardScaler, OrdinalEncoder, OneHotEncoder, BinaryEncoder) chá»‰ Ä‘Æ°á»£c khá»›p trÃªn táº­p huáº¥n luyá»‡n.
5. **`ColumnTransformer.transform(X_train)` vÃ  `.transform(X_test)`** â€” transformer Ä‘Ã£ khá»›p Ä‘Æ°á»£c Ã¡p dá»¥ng cho cáº£ hai táº­p.
6. **TÃ¡i láº¥y máº«u (SMOTE/ADASYN)** â€” chá»‰ Ã¡p dá»¥ng trÃªn máº£ng huáº¥n luyá»‡n Ä‘Ã£ biáº¿n Ä‘á»•i; táº­p kiá»ƒm tra khÃ´ng bao giá» Ä‘Æ°á»£c tÃ¡i láº¥y máº«u.

TrÃ¬nh tá»± nÃ y Ä‘Æ°á»£c tham chiáº¿u chÃ©o trong tÃ i liá»‡u Preprocessing Sequence (TÃ i liá»‡u 07).

---

## 6. Thuá»™c tÃ­nh Äáº§u ra

`ColumnTransformer` Ä‘Ã£ khá»›p Ä‘Æ°á»£c tuáº§n tá»± hÃ³a vÃ o `scaler.pkl` thÃ´ng qua `joblib.dump()` Ä‘á»ƒ Ä‘áº£m báº£o kháº£ nÄƒng tÃ¡i táº¡o (reprovansonibility) vÃ  triá»ƒn khai. HÃ m `preprocess()` tráº£ vá» bá»‘n Ä‘á»‘i tÆ°á»£ng: máº£ng huáº¥n luyá»‡n Ä‘Ã£ biáº¿n Ä‘á»•i, máº£ng kiá»ƒm tra Ä‘Ã£ biáº¿n Ä‘á»•i, transformer Ä‘Ã£ khá»›p, vÃ  danh sÃ¡ch tÃªn Ä‘áº·c trÆ°ng thu Ä‘Æ°á»£c tá»« `ct.get_feature_names_out()`.

CÃ¡c thuá»™c tÃ­nh Ä‘áº§u ra Ä‘Ã£ Ä‘Æ°á»£c xÃ¡c minh:

- **Sá»‘ cá»™t**: 49 cá»™t sau khi mÃ£ hÃ³a (19 Ä‘á»‹nh lÆ°á»£ng + 3 thá»© báº­c + káº¿t quáº£ má»Ÿ rá»™ng one-hot cá»§a region/code_module/code_presentation + 2 nhá»‹ phÃ¢n + 1 chá»‰ bÃ¡o).
- **GiÃ¡ trá»‹ khuyáº¿t**: khÃ´ng cÃ³ giÃ¡ trá»‹ NaN trong báº¥t ká»³ máº£ng Ä‘áº§u ra nÃ o sau khi biáº¿n Ä‘á»•i.
- **TÃªn Ä‘áº·c trÆ°ng**: Ä‘Æ°á»£c giá»¯ Ä‘áº§y Ä‘á»§ theo chuáº©n `snake_case` vá»›i tiá»n tá»‘ tÃªn transformer (vÃ­ dá»¥: `num__total_clicks`, `nominal__region_East Anglian Region`) Ä‘á»ƒ gÃ¡n nhÃ£n tÆ°á»ng minh trong SHAP waterfall plot vÃ  hiá»ƒn thá»‹ táº§m quan trá»ng Ä‘áº·c trÆ°ng cá»§a LIME.

---

## 7. Quy táº¯c Äáº·t tÃªn Äáº·c trÆ°ng vÃ  Kháº£ nÄƒng Diá»…n giáº£i Sau thá»±c nghiá»‡m

Viá»‡c sá»­ dá»¥ng nháº¥t quÃ¡n tÃªn cá»™t mÃ´ táº£ theo chuáº©n `snake_case` xuyÃªn suá»‘t `preprocessing.py` (vÃ­ dá»¥: `mean_clicks_per_active_day`, `weighted_score_to_date`, `days_since_last_activity`) Ä‘áº£m báº£o ráº±ng káº¿t quáº£ Ä‘áº§u ra cá»§a SHAP vÃ  LIME tá»± giáº£i thÃ­ch. Khi `ColumnTransformer` Ä‘Æ°á»£c cáº¥u hÃ¬nh vá»›i `verbose_feature_names_out=True`, má»—i cá»™t Ä‘áº§u ra mang tiá»n tá»‘ transformer giÃºp xÃ¡c Ä‘á»‹nh nguá»“n gá»‘c, cho phÃ©p nhÃ  phÃ¢n tÃ­ch truy ngÆ°á»£c báº¥t ká»³ giÃ¡ trá»‹ táº§m quan trá»ng Ä‘áº·c trÆ°ng nÃ o vá» biáº¿n nguá»“n thÃ´ tÆ°Æ¡ng á»©ng mÃ  khÃ´ng cáº§n tra cá»©u tá»« Ä‘iá»ƒn dá»¯ liá»‡u riÃªng biá»‡t. Lá»±a chá»n thiáº¿t káº¿ nÃ y trá»±c tiáº¿p há»— trá»£ yÃªu cáº§u kháº£ nÄƒng diá»…n giáº£i cá»§a bÃ i toÃ¡n dá»± Ä‘oÃ¡n nguy cÆ¡ sinh viÃªn, trong Ä‘Ã³ giÃ¡o viÃªn vÃ  cá»‘ váº¥n há»c táº­p pháº£i hiá»ƒu Ä‘Æ°á»£c hÃ nh vi sinh viÃªn hoáº·c thuá»™c tÃ­nh nhÃ¢n kháº©u há»c nÃ o thÃºc Ä‘áº©y tá»«ng cáº£nh bÃ¡o nguy cÆ¡ cÃ¡ nhÃ¢n.

---

*BiÃªn soáº¡n bá»Ÿi NhÃ³m 5 DSP391m. ToÃ n bá»™ logic biáº¿n Ä‘á»•i tham chiáº¿u `src/features/preprocessing.py`, Ä‘Ã£ commit vÃ o kho mÃ£ nguá»“n dá»± Ã¡n (nhÃ¡nh: main).*

