# PhÆ°Æ¡ng PhÃ¡p LÃ m Sáº¡ch Dá»¯ Liá»‡u: PhÃ¢n TÃ­ch vÃ  Luáº­n Giáº£i

**DSP391m â€“ NhÃ³m 5 Â· BÃ¡o cÃ¡o 2 (Nhiá»‡m vá»¥ Dá»¯ liá»‡u), ChÆ°Æ¡ng 3 Â· Task 3.3 â€” PhÆ°Æ¡ng PhÃ¡p LÃ m Sáº¡ch Dá»¯ Liá»‡u**

---

## TÃ³m Táº¯t

ChÆ°Æ¡ng nÃ y trÃ¬nh bÃ y phÃ¢n tÃ­ch bá»‘n váº¥n Ä‘á» lÃ m sáº¡ch dá»¯ liá»‡u Ä‘Æ°á»£c xá»­ lÃ½ trong pipeline cá»§a NhÃ³m 5 DSP391m: báº£n ghi trÃ¹ng láº·p (duplicate records), khÃ´ng nháº¥t quÃ¡n danh má»¥c (categorical inconsistency), giÃ¡ trá»‹ khuyáº¿t (missing values) vÃ  ngoáº¡i lai (outliers). Má»™t váº¥n Ä‘á» thá»© nÄƒm â€” rÃ² rá»‰ thÃ´ng tin thá»i gian (temporal leakage) do báº£n ghi cÃ³ ngÃ y trong tÆ°Æ¡ng lai â€” Ä‘Æ°á»£c coi lÃ  bÆ°á»›c lÃ m sáº¡ch Ä‘á»“ng thá»i lÃ  bÆ°á»›c ngÄƒn rÃ² rá»‰ (leakage-prevention). Vá»›i má»—i váº¥n Ä‘á», bÃ i viáº¿t trÃ¬nh bÃ y má»¥c Ä‘Ã­ch, cÆ¡ cháº¿ phÃ¡t hiá»‡n, quyáº¿t Ä‘á»‹nh cho tá»«ng biáº¿n vÃ  káº¿t quáº£ sau lÃ m sáº¡ch Ä‘Æ°á»£c kiá»ƒm chá»©ng. ToÃ n bá»™ logic lÃ m sáº¡ch náº±m trong hai module: `src/data/build_master_table.py` (tÃ­nh toÃ n váº¹n cáº¥u trÃºc, trÃ¹ng láº·p, nháº¥t quÃ¡n) vÃ  `src/features/preprocessing.py` (giÃ¡ trá»‹ khuyáº¿t, ngoáº¡i lai). Má»i quyáº¿t Ä‘á»‹nh Ä‘á»u cÃ³ kháº£ nÄƒng tÃ¡i táº¡o: tham sá»‘ Ä‘Æ°á»£c há»c tá»« táº­p huáº¥n luyá»‡n (training split) duy nháº¥t, vÃ  má»i hÃ ng Ä‘Æ°á»£c biáº¿n Ä‘á»•i Ä‘á»u Ä‘Æ°á»£c giá»¯ láº¡i trong bá»™ dá»¯ liá»‡u.

---

## 1. Giá»›i Thiá»‡u

Dá»¯ liá»‡u thÃ´ Ä‘Æ°á»£c tá»•ng há»£p tá»« viá»‡c ná»‘i báº£y báº£ng OULAD chá»©a cÃ¡c lá»—i, náº¿u khÃ´ng Ä‘Æ°á»£c sá»­a, sáº½ lÃ m lá»‡ch quÃ¡ trÃ¬nh huáº¥n luyá»‡n mÃ´ hÃ¬nh hoáº·c vÃ´ hiá»‡u hÃ³a cÃ¡c chá»‰ sá»‘ Ä‘Ã¡nh giÃ¡. Bá»‘n loáº¡i lá»—i Ä‘Æ°á»£c xá»­ lÃ½ cÃ³ há»‡ thá»‘ng trÆ°á»›c khi phÃ¢n chia train/test vÃ  láº¡i trong trÃ¬nh tá»± tiá»n xá»­ lÃ½ (preprocessing) chá»‘ng rÃ² rá»‰. Thá»© tá»± thá»±c hiá»‡n lÃ : (1) lÃ m sáº¡ch cáº¥u trÃºc lÃºc xÃ¢y dá»±ng báº£ng, (2) Ä‘iá»n giÃ¡ trá»‹ khuyáº¿t Ä‘Æ°á»£c há»c tá»« táº­p train, (3) biáº¿n Ä‘á»•i ngoáº¡i lai Ä‘Æ°á»£c há»c tá»« táº­p train, (4) mÃ£ hÃ³a vÃ  chuáº©n hÃ³a Ä‘Æ°á»£c há»c tá»« táº­p train.

---

## 2. Báº£n Ghi TrÃ¹ng Láº·p

**Má»¥c Ä‘Ã­ch.** Má»—i hÃ ng trong báº£ng master Ä‘Æ°á»£c thiáº¿t káº¿ Ä‘á»ƒ biá»ƒu diá»…n má»™t bá»™ ba duy nháº¥t (sinh viÃªn, module, há»c ká»³). CÃ¡c khÃ³a tá»•ng há»£p bá»‹ trÃ¹ng láº·p sáº½ lÃ m tÄƒng sá»‘ lÆ°á»£ng báº£n ghi cá»§a má»™t sá»‘ sinh viÃªn vÃ  lÃ m sai lá»‡ch cÃ¡c thá»‘ng kÃª tá»•ng há»£p.

**PhÆ°Æ¡ng phÃ¡p.** HÃ m `_clean` trong `build_master_table.py` gá»i `pandas.DataFrame.drop_duplicates` trÃªn khÃ³a tá»•ng há»£p `(code_module, code_presentation, id_student)`, tÆ°Æ¡ng á»©ng vá»›i háº±ng sá»‘ `GROUP_COLS`. Báº£ng sau khi khá»­ trÃ¹ng láº·p Ä‘Æ°á»£c Ä‘Ã¡nh chá»‰ sá»‘ láº¡i tá»« Ä‘áº§u.

**Káº¿t quáº£.** Kiá»ƒm tra sau lÃ m sáº¡ch xÃ¡c nháº­n khÃ´ng cÃ²n khÃ³a trÃ¹ng láº·p. Sá»‘ lÆ°á»£ng Ä‘Æ°á»£c ghi vÃ o `data/interim/master_cleaning_log.csv` dÆ°á»›i má»¥c `duplicate_keys_removed`. Nháº­t kÃ½ ná»‘i báº£ng (join log) ghi riÃªng sá»‘ lÆ°á»£ng hÃ ng á»Ÿ má»—i bÆ°á»›c merge Ä‘á»ƒ phÃ¡t hiá»‡n ngay láº­p tá»©c khi sá»‘ hÃ ng tÄƒng báº¥t thÆ°á»ng.

### 2.1 DÃ²ng clickstream trÃ¹ng láº·p toÃ n pháº§n â€” quyáº¿t Ä‘á»‹nh Ä‘Æ°á»£c vÄƒn báº£n hoÃ¡

**Quan sÃ¡t.** File thÃ´ `studentVle.csv` cÃ³ 10.655.280 dÃ²ng, trong Ä‘Ã³ 787.170 dÃ²ng (7,4%) trÃ¹ng láº·p toÃ n pháº§n (giá»‘ng há»‡t trÃªn má»i cá»™t) vá»›i má»™t dÃ²ng khÃ¡c. ÄÃ¢y lÃ  Ä‘áº·c Ä‘iá»ƒm cÃ³ sáºµn cá»§a chÃ­nh báº£n phÃ¢n phá»‘i OULAD: báº£ng nÃ y khÃ´ng cÃ³ khÃ³a duy nháº¥t, vÃ  má»™t dÃ²ng biá»ƒu diá»…n tÆ°Æ¡ng tÃ¡c cá»§a má»™t sinh viÃªn vá»›i má»™t tÃ i nguyÃªn VLE trong má»™t ngÃ y, vá»›i `sum_click` Ä‘Ã£ Ä‘Æ°á»£c cá»™ng gá»™p tá»« nguá»“n. VÃ¬ váº­y, chá»‰ dá»±a vÃ o lÆ°á»£c Ä‘á»“, hai dÃ²ng giá»‘ng há»‡t nhau khÃ´ng thá»ƒ phÃ¢n biá»‡t vá»›i má»™t báº£n ghi tá»•ng há»£p láº·p láº¡i há»£p lá»‡.

**Quyáº¿t Ä‘á»‹nh â€” giá»¯ vÃ  cá»™ng dá»“n.** Pipeline giá»¯ nguyÃªn cÃ¡c dÃ²ng nÃ y; bÆ°á»›c tá»•ng há»£p theo má»‘c (`groupby` + `sum` trÃªn `sum_click`) cá»™ng dá»“n chÃºng vÃ o cÃ¡c Ä‘áº·c trÆ°ng tÆ°Æ¡ng tÃ¡c. CÄƒn cá»©: (i) trung thÃ nh vá»›i bá»™ dá»¯ liá»‡u nhÆ° Ä‘Æ°á»£c cÃ´ng bá»‘ â€” khi khÃ´ng cÃ³ khÃ³a duy nháº¥t, viá»‡c xÃ³a má»™t báº£n sao sáº½ lÃ  phá»ng Ä‘oÃ¡n khÃ´ng kiá»ƒm chá»©ng Ä‘Æ°á»£c vá» viá»‡c báº£n ghi nÃ o lÃ  "tháº­t"; (ii) nháº¥t quÃ¡n vá»›i cÃ¡c nghiÃªn cá»©u ná»n (Adnan vÃ  cá»™ng sá»± 2021; Tomasevic vÃ  cá»™ng sá»± 2020), vá»‘n lÃ m viá»‡c trÃªn cÃ¡c báº£ng OULAD gá»‘c mÃ  khÃ´ng khá»­ trÃ¹ng láº·p clickstream, nhá» Ä‘Ã³ cÃ¡c Ä‘áº·c trÆ°ng tá»« click cá»§a chÃºng tÃ´i váº«n so sÃ¡nh Ä‘Æ°á»£c.

**Giá»›i háº¡n Ä‘Æ°á»£c ghi nháº­n.** Náº¿u má»™t pháº§n cÃ¡c dÃ²ng trÃ¹ng nÃ y lÃ  lá»—i ghi kÃ©p tá»« nguá»“n, cÃ¡c tá»•ng click (`total_clicks`, `clicks_*`) sáº½ bá»‹ Ä‘áº¿m trá»™i cho nhá»¯ng ngÃ y-sinh viÃªn bá»‹ áº£nh hÆ°á»Ÿng. Äiá»u nÃ y Ä‘Æ°á»£c cháº¥p nháº­n vÃ  vÄƒn báº£n hoÃ¡ nhÆ° má»™t giá»›i háº¡n cá»§a dá»¯ liá»‡u nguá»“n thay vÃ¬ "sá»­a" báº±ng cÃ¡ch xÃ³a. LÆ°u Ã½ sá»± tÆ°Æ¡ng pháº£n vá»›i bÆ°á»›c khá»­ trÃ¹ng láº·p báº£ng master á»Ÿ trÃªn, nÆ¡i khÃ³a tá»•ng há»£p cho phÃ©p nháº­n diá»‡n cháº¯c cháº¯n báº£n ghi trÃ¹ng thá»±c sá»±.

---

## 3. Nháº¥t QuÃ¡n vÃ  Chuáº©n HÃ³a

**Má»¥c Ä‘Ã­ch.** CÃ¡c cá»™t chuá»—i phÃ¢n loáº¡i (categorical string) Ä‘Æ°á»£c láº¥y tá»« CSV cÃ³ thá»ƒ chá»©a khoáº£ng tráº¯ng Ä‘áº§u hoáº·c cuá»‘i, khiáº¿n cÃ¡c danh má»¥c giá»‘ng nhau vá» ngá»¯ nghÄ©a xuáº¥t hiá»‡n nhÆ° cÃ¡c giÃ¡ trá»‹ riÃªng biá»‡t trong thao tÃ¡c groupby hay encoder.

**PhÆ°Æ¡ng phÃ¡p.** Äá»‘i vá»›i má»—i cá»™t trong `CATEGORICAL_COLS` â€” `gender`, `region`, `highest_evansonation`, `imd_band`, `age_band`, `disability` â€” pipeline Ã¡p dá»¥ng `str.strip()` sau khi ná»‘i báº£ng. KhÃ´ng thá»±c hiá»‡n chuáº©n hÃ³a chá»¯ hoa/thÆ°á»ng hay há»£p nháº¥t tá»« Ä‘á»“ng nghÄ©a; má»¥c Ä‘Ã­ch lÃ  chuáº©n hÃ³a tá»‘i thiá»ƒu, cÃ³ thá»ƒ Ä‘áº£o ngÆ°á»£c.

**Lá»±c lÆ°á»£ng sá»‘ (cardinality) Ä‘Ã£ kiá»ƒm chá»©ng sau lÃ m sáº¡ch.**

| Biáº¿n | Sá»‘ giÃ¡ trá»‹ phÃ¢n biá»‡t |
|---|---|
| `region` | 13 |
| `highest_evansonation` | 5 |
| `imd_band` | 10 |
| `age_band` | 3 |
| `gender` | 2 |
| `disability` | 2 |

**Äáº·c Ä‘iá»ƒm OULAD: giÃ¡ trá»‹ `"10-20"` trong `imd_band`.** Dá»¯ liá»‡u gá»‘c OULAD bá» sÃ³t kÃ½ hiá»‡u `%` á»Ÿ dáº£i thá»© hai, ghi lÃ  `"10-20"` thay vÃ¬ `"10-20%"`. Pipeline giá»¯ nguyÃªn giÃ¡ trá»‹ nÃ y. Bá»™ mÃ£ hÃ³a thá»© báº­c (ordinal encoder) Ä‘á»‹nh nghÄ©a trong `preprocessing.py` liá»‡t kÃª rÃµ rÃ ng `"10-20"` á»Ÿ thá»© háº¡ng 2 trong chuá»—i `ORDINAL_ORDERS["imd_band"]`. Viá»‡c tá»± Ä‘á»™ng ghi Ä‘Ã¨ danh má»¥c thÃ´ sáº½ táº¡o ra sá»± khÃ´ng khá»›p giá»¯a dá»¯ liá»‡u nguá»“n vÃ  cáº¥u hÃ¬nh encoder, Ä‘á»“ng thá»i lÃ m phá»©c táº¡p viá»‡c kiá»ƒm tra kháº£ nÄƒng tÃ¡i táº¡o.

---

## 4. GiÃ¡ Trá»‹ Khuyáº¿t

**Má»¥c Ä‘Ã­ch.** GiÃ¡ trá»‹ khuyáº¿t khÃ´ng Ä‘Æ°á»£c xá»­ lÃ½ sáº½ ngÄƒn cÃ¡c estimator cá»§a sklearn huáº¥n luyá»‡n vÃ , náº¿u Ä‘Æ°á»£c Ä‘iá»n má»™t cÃ¡ch thÃ´ sÆ¡, cÃ³ thá»ƒ gÃ¢y rÃ² rá»‰ thÃ´ng tin (leakage) hoáº·c lÃ m mÃ©o tÃ­n hiá»‡u suy diá»…n.

**PhÆ°Æ¡ng phÃ¡p.** HÃ m `handle_missing` trong `preprocessing.py` Ã¡p dá»¥ng cÃ¡c chiáº¿n lÆ°á»£c theo tá»«ng biáº¿n. CÃ¡c thá»‘ng kÃª Ä‘iá»n giÃ¡ trá»‹ (median cá»§a `date_registration` trÃªn táº­p huáº¥n luyá»‡n) Ä‘Æ°á»£c tÃ­nh chá»‰ tá»« táº­p train vÃ  sau Ä‘Ã³ Ã¡p dá»¥ng Ä‘á»“ng nháº¥t cho táº­p test, Ä‘Ã¡p á»©ng yÃªu cáº§u chá»‘ng rÃ² rá»‰.

**Báº£ng 1: PhÃ¢n tÃ­ch giÃ¡ trá»‹ khuyáº¿t.**

| Biáº¿n | # Khuyáº¿t | CÆ¡ cháº¿ giáº£ Ä‘á»‹nh | Chiáº¿n lÆ°á»£c |
|---|---|---|---|
| `imd_band` | 1.111 | MAR / MCAR | Äiá»n `'Unknown'`; chÃ¨n lÃ m danh má»¥c thá»© háº¡ng 0 trong `ORDINAL_ORDERS["imd_band"]` |
| `mean_score_to_date` | thiáº¿u khi chÆ°a ná»™p bÃ i | MNAR | Äiá»n `0`; chá»‰ bÃ¡o nhá»‹ phÃ¢n (binary indicator) `not_submitted` Ä‘Ã£ Ä‘Æ°á»£c táº¡o trong bÆ°á»›c feature engineering |
| `weighted_score_to_date` | thiáº¿u khi chÆ°a ná»™p bÃ i | MNAR | Äiá»n `0`; cÃ¹ng chá»‰ bÃ¡o `not_submitted` |
| `n_assessments_submitted` | thiáº¿u khi chÆ°a ná»™p bÃ i | MNAR | Äiá»n `0`; cÃ¹ng chá»‰ bÃ¡o `not_submitted` |
| `date_registration` | 45 | MCAR | Äiá»n median cá»§a táº­p huáº¥n luyá»‡n (há»c tá»« train) |
| `date_unregistration` | 22.521 | Váº¯ng máº·t theo cáº¥u trÃºc | KhÃ´ng Ä‘iá»n; khÃ´ng dÃ¹ng lÃ m Ä‘áº·c trÆ°ng |

**CÄƒn cá»© quyáº¿t Ä‘á»‹nh.**

- `imd_band`: Sá»± váº¯ng máº·t cÃ³ thá»ƒ cÃ³ tÃ­nh cháº¥t hÃ nh chÃ­nh hÆ¡n lÃ  liÃªn quan Ä‘áº¿n káº¿t quáº£ há»c táº­p (MAR hoáº·c MCAR). Táº¡o danh má»¥c `"Unknown"` riÃªng báº£o toÃ n thang Ä‘o thá»© báº­c cá»§a 10 giÃ¡ trá»‹ cÃ²n láº¡i mÃ  khÃ´ng pháº£i Æ°á»›c tÃ­nh má»™t giÃ¡ trá»‹ kinh táº¿-xÃ£ há»™i giáº£ táº¡o.
- Biáº¿n Ä‘iá»ƒm sá»‘ (MNAR): Äiá»ƒm khuyáº¿t táº¡i má»‘c thá»i gian *t* cÃ³ nghÄ©a lÃ  sinh viÃªn chÆ°a ná»™p bÃ i nÃ o tÃ­nh Ä‘áº¿n ngÃ y Ä‘Ã³. Äiá»u nÃ y báº£n thÃ¢n nÃ³ lÃ  tÃ­n hiá»‡u dá»± Ä‘oÃ¡n máº¡nh vá» tráº¡ng thÃ¡i cÃ³ nguy cÆ¡ (at-risk). Äiá»n báº±ng 0 lÃ m tÃ­n hiá»‡u trá»Ÿ nÃªn rÃµ rÃ ng; chá»‰ bÃ¡o nhá»‹ phÃ¢n `not_submitted` náº¯m báº¯t riÃªng sá»± kiá»‡n váº¯ng máº·t, ngÄƒn sá»‘ 0 bá»‹ nháº§m vá»›i bÃ i ná»™p Ä‘áº¡t Ä‘iá»ƒm 0 thá»±c sá»±.
- `date_registration`: Chá»‰ 45 báº£n ghi bá»‹ áº£nh hÆ°á»Ÿng vÃ  sá»± váº¯ng máº·t cÃ³ váº» khÃ´ng liÃªn quan Ä‘áº¿n káº¿t quáº£ (MCAR). Äiá»n median há»c tá»« táº­p huáº¥n luyá»‡n Ä‘Æ¡n giáº£n vÃ  gÃ¢y ra sai lá»‡ch khÃ´ng Ä‘Ã¡ng ká»ƒ.
- `date_unregistration`: Äa sá»‘ sinh viÃªn hoÃ n thÃ nh mÃ  khÃ´ng há»§y Ä‘Äƒng kÃ½, nÃªn 22.521 giÃ¡ trá»‹ khuyáº¿t lÃ  khÃ´ng trÃ¡nh khá»i vá» máº·t cáº¥u trÃºc. ÄÆ°a cá»™t nÃ y vÃ o lÃ m Ä‘áº·c trÆ°ng sáº½ Ä‘Ã²i há»i Ä‘iá»n ngÃ y há»§y Ä‘Äƒng kÃ½ giáº£ tÆ°á»Ÿng cho pháº§n lá»›n sinh viÃªn, Ä‘iá»u nÃ y khÃ´ng cÃ³ cÆ¡ sá»Ÿ.

**Káº¿t quáº£ kiá»ƒm chá»©ng.** Sau `handle_missing`, `df.isnull().sum()` báº±ng 0 trÃªn má»i cá»™t Ä‘áº·c trÆ°ng á»Ÿ cáº£ táº­p train láº«n táº­p test, Ä‘Æ°á»£c xÃ¡c nháº­n báº±ng phÃ©p kiá»ƒm tra (assertion) trong smoke test cá»§a pipeline.

**Errata (2026-07-12): bÃ i Ä‘Ã¡nh giÃ¡ Ä‘Æ°á»£c báº£o lÆ°u (banked) & `not_submitted`.** Má»™t lá»—i Ä‘Æ°á»£c phÃ¡t hiá»‡n vÃ  sá»­a ngÃ y 2026-07-12 trong `src/data/build_performance_features.py`: cÃ¡c bÃ i Ä‘Ã¡nh giÃ¡ Ä‘Æ°á»£c báº£o lÆ°u Ä‘iá»ƒm tá»« láº§n há»c trÆ°á»›c ("banked", `is_banked = 1`) bá»‹ loáº¡i khá»i táº­p bÃ i "Ä‘Ã£ ná»™p", nhÆ°ng chÃ­nh cÃ¡c bÃ i Ä‘Ã³ váº«n bá»‹ tÃ­nh lÃ  "Ä‘Ã£ Ä‘áº¿n háº¡n" táº¡i má»‘c kiá»ƒm tra â€” khiáº¿n chá»‰ bÃ¡o `not_submitted` bá»‹ gÃ¡n 1 sai cho nhá»¯ng sinh viÃªn Ä‘Ã£ báº£o lÆ°u bÃ i. áº¢nh hÆ°á»Ÿng Ä‘o Ä‘Æ°á»£c: 78 trÃªn 32.593 báº£n ghi ghi danh (0,24%) táº¡i *t* = 100%. Code hiá»‡n Ä‘Ã£ tÃ­nh bÃ i báº£o lÆ°u lÃ  Ä‘Ã£ bao phá»§ háº¡n ná»™p cá»§a nÃ³. CÃ¡c báº£ng káº¿t quáº£ Ä‘Ã£ commit trÆ°á»›c ngÃ y nÃ y Ä‘Æ°á»£c tÃ­nh báº±ng code trÆ°á»›c khi sá»­a vÃ  sáº½ Ä‘Æ°á»£c tÃ­nh láº¡i toÃ n bá»™ trong láº§n cháº¡y chá»‘t bÃ¡o cÃ¡o cuá»‘i (danh má»¥c cáº­p nháº­t sá»‘ liá»‡u Ä‘Æ°á»£c theo dÃµi trong sá»• tay báº£o vá»‡).

---

## 5. Ngoáº¡i Lai

**Má»¥c Ä‘Ã­ch.** CÃ¡c giÃ¡ trá»‹ cá»±c Ä‘oan trong cÃ¡c Ä‘áº·c trÆ°ng tÆ°Æ¡ng tÃ¡c (engagement features) bá»‹ lá»‡ch pháº£i máº¡nh sáº½ lÃ m sai lá»‡ch cÃ¡c mÃ´ hÃ¬nh dá»±a trÃªn khoáº£ng cÃ¡ch vÃ  thá»•i phá»“ng Æ°á»›c lÆ°á»£ng phÆ°Æ¡ng sai trong cÃ¡c mÃ´ hÃ¬nh cÃ¢y. Má»¥c tiÃªu lÃ  giáº£m áº£nh hÆ°á»Ÿng cá»§a giÃ¡ trá»‹ cá»±c Ä‘oan mÃ  khÃ´ng loáº¡i bá» báº£n ghi sinh viÃªn nÃ o.

**PhÃ¡t hiá»‡n.** Quy táº¯c IQR (interquartile range) Ä‘Æ°á»£c Ã¡p dá»¥ng: má»™t giÃ¡ trá»‹ Ä‘Æ°á»£c Ä‘Ã¡nh dáº¥u lÃ  nghi ngá» ngoáº¡i lai khi náº±m dÆ°á»›i Q1 âˆ’ 1,5 Ã— IQR hoáº·c trÃªn Q3 + 1,5 Ã— IQR. NgÆ°á»¡ng Ä‘Æ°á»£c tÃ­nh tá»« táº­p huáº¥n luyá»‡n. KhÃ´ng cÃ³ hÃ ng nÃ o bá»‹ xÃ³a.

**CÃ¡c chiáº¿n lÆ°á»£c biáº¿n Ä‘á»•i.**

- `log1p`: Ãp dá»¥ng cho cÃ¡c Ä‘áº·c trÆ°ng clickstream (dá»¯ liá»‡u click) lá»‡ch pháº£i máº¡nh. PhÃ©p biáº¿n Ä‘á»•i `x â†’ log(1 + x)` nÃ©n Ä‘uÃ´i pháº£i dÃ i trong khi Ã¡nh xáº¡ sá»‘ 0 vá» sá»‘ 0, Ä‘iá»u nÃ y quan trá»ng vÃ¬ nhiá»u sinh viÃªn khÃ´ng cÃ³ hoáº¡t Ä‘á»™ng trong má»™t loáº¡i tÆ°Æ¡ng tÃ¡c nháº¥t Ä‘á»‹nh.
- `winsorize` (cáº¯t ngÆ°á»¡ng): Ãp dá»¥ng á»Ÿ giá»›i háº¡n 1% (Ä‘áº§u vÃ  cuá»‘i 1%). CÃ¡c giÃ¡ trá»‹ dÆ°á»›i phÃ¢n vá»‹ thá»© nháº¥t hoáº·c trÃªn phÃ¢n vá»‹ thá»© 99 Ä‘Æ°á»£c káº¹p vÃ o giÃ¡ trá»‹ biÃªn Ä‘Ã³, báº£o toÃ n thá»© háº¡ng thá»© tá»± cá»§a má»i quan sÃ¡t.
- `none` (khÃ´ng xá»­ lÃ½): Ãp dá»¥ng khi biáº¿n bá»‹ cháº·n tá»± nhiÃªn hoáº·c khi phÃ¢n tÃ­ch IQR khÃ´ng phÃ¡t hiá»‡n ngoáº¡i lai thá»±c sá»±.

**Báº±ng chá»©ng vá» Ä‘á»™ lá»‡ch tá»« phÃ¢n tÃ­ch dá»¯ liá»‡u khÃ¡m phÃ¡ (EDA).** Biáº¿n `max_clicks_single_day` cÃ³ há»‡ sá»‘ lá»‡ch (skewness) xáº¥p xá»‰ 10,6; `total_clicks` xáº¥p xá»‰ 3,0; `mean_clicks_per_active_day` xáº¥p xá»‰ 1,6. CÃ¡c giÃ¡ trá»‹ nÃ y biá»‡n minh cho xá»­ lÃ½ `log1p`.

**Báº£ng 2: Quyáº¿t Ä‘á»‹nh xá»­ lÃ½ ngoáº¡i lai.**

| Biáº¿n (nhÃ³m) | PhÃ¡t hiá»‡n | Chiáº¿n lÆ°á»£c | LÃ½ do |
|---|---|---|---|
| `total_clicks` | IQR | `log1p` | Há»‡ sá»‘ lá»‡ch â‰ˆ 3,0; giÃ¡ trá»‹ max lÃªn tá»›i hÃ ng nghÃ¬n |
| `n_days_active` | IQR | `log1p` | Count lá»‡ch pháº£i máº¡nh |
| `clicks_forumng`, `clicks_oucontent`, `clicks_resource`, `clicks_homepage`, `clicks_oucollaborate`, `clicks_quiz`, `clicks_subpage`, `clicks_url` | IQR | `log1p` | Sá»‘ click theo tá»«ng loáº¡i hoáº¡t Ä‘á»™ng, cÃ¹ng hÃ¬nh dáº¡ng phÃ¢n phá»‘i |
| `max_clicks_single_day` | IQR | `log1p` | max = 7.920; há»‡ sá»‘ lá»‡ch â‰ˆ 10,6 |
| `mean_clicks_per_active_day` | IQR | `log1p` | max = 1.879; há»‡ sá»‘ lá»‡ch â‰ˆ 1,6 |
| `days_since_last_activity` | IQR | `winsorize` (1%) | Chá»‰ 6 báº£n ghi bá»‹ Ä‘Ã¡nh dáº¥u; lá»‡ch nháº¹ |
| `studied_credits` | IQR | `winsorize` (1%) | max = 655; lá»‡ch pháº£i vá»«a pháº£i |
| `num_of_prev_attempts` | IQR | `winsorize` (1%) | IQR = 0, Q1 = Q3 = 0; winsorize báº£o toÃ n tÃ­n hiá»‡u "há»c láº¡i nhiá»u láº§n" quan trá»ng vá»›i sinh viÃªn at-risk |
| `weighted_score_to_date` | IQR | `winsorize` (1%) | Pháº¡m vi lÃ½ thuyáº¿t má»Ÿ; winsorize an toÃ n hÆ¡n log1p cho Ä‘iá»ƒm sá»‘ |
| `mean_score_to_date` | IQR | `none` | Cáº­n trÃªn 103,15 tá»« phÃ¢n tÃ­ch IQR vÆ°á»£t giá»›i háº¡n váº­t lÃ½ 100, cho tháº¥y khÃ´ng cÃ³ ngoáº¡i lai thá»±c sá»± |
| `n_assessments_submitted` | IQR | `none` | Bá»‹ cháº·n bá»Ÿi sá»‘ lÆ°á»£ng bÃ i kiá»ƒm tra cá»§a khÃ³a há»c |
| `date_registration` | IQR | `none` | Pháº¡m vi kÃ½ hiá»‡u tá»± nhiÃªn (Ã¢m = trÆ°á»›c khÃ³a há»c); khÃ´ng cáº§n biáº¿n Ä‘á»•i |

---

## 6. LÃ m Sáº¡ch Thá»i Gian

**Má»¥c Ä‘Ã­ch.** Pipeline táº¡o nhiá»u snapshot Ä‘áº·c trÆ°ng táº¡i cÃ¡c má»‘c kiá»ƒm tra (checkpoint) Ä‘Æ°á»£c xÃ¡c Ä‘á»‹nh trÆ°á»›c (vÃ­ dá»¥: ngÃ y 60, ngÃ y 90, toÃ n khÃ³a). Báº¥t ká»³ báº£n ghi nÃ o cÃ³ ngÃ y sau má»‘c *t* â€” dÃ¹ lÃ  tÆ°Æ¡ng tÃ¡c VLE hay ná»™p bÃ i kiá»ƒm tra â€” Ä‘á»u pháº£i bá»‹ loáº¡i trÆ°á»›c khi tÃ­nh Ä‘áº·c trÆ°ng cho má»‘c Ä‘Ã³.

**PhÆ°Æ¡ng phÃ¡p.** HÃ m `cut_at_checkpoint` (trong `src/data/time_utils.py`) lá»c cÃ¡c hÃ ng Ä‘á»ƒ chá»‰ giá»¯ láº¡i nhá»¯ng hÃ ng cÃ³ ngÃ y â‰¤ *t* trÆ°á»›c khi tá»•ng há»£p Ä‘áº·c trÆ°ng. BÆ°á»›c nÃ y vá»«a lÃ  thao tÃ¡c lÃ m sáº¡ch dá»¯ liá»‡u (loáº¡i bá» cÃ¡c quan sÃ¡t khÃ´ng há»£p lá»‡ vá» máº·t thá»i gian) vá»«a lÃ  biá»‡n phÃ¡p ngÄƒn rÃ² rá»‰ (Ä‘áº£m báº£o khÃ´ng cÃ³ thÃ´ng tin sau ngÃ y dá»± Ä‘oÃ¡n áº£nh hÆ°á»Ÿng Ä‘áº¿n Ä‘áº·c trÆ°ng). NÃ³ Ä‘Æ°á»£c Ã¡p dá»¥ng Ä‘á»™c láº­p cho tá»«ng má»‘c kiá»ƒm tra vÃ  tá»«ng fold cá»§a phÃ¢n chia train/test.

---

## 7. Táº¡i Sao Äiá»u NÃ y Quan Trá»ng Äá»‘i Vá»›i MÃ´ HÃ¬nh HÃ³a

Äáº§u vÃ o sáº¡ch, nháº¥t quÃ¡n vÃ  khÃ´ng rÃ² rá»‰ lÃ  Ä‘iá»u kiá»‡n tiÃªn quyáº¿t Ä‘á»ƒ mÃ´ hÃ¬nh hÃ³a cÃ³ giÃ¡ trá»‹. CÃ¡c hÃ ng trÃ¹ng láº·p lÃ m tÄƒng áº£nh hÆ°á»Ÿng cá»§a má»™t sá»‘ sinh viÃªn lÃªn cÃ¡c tham sá»‘ Ä‘Æ°á»£c há»c; cÃ¡c kÃ½ tá»± khoáº£ng tráº¯ng thá»«a khiáº¿n encoder táº¡o ra cÃ¡c danh má»¥c giáº£; giÃ¡ trá»‹ khuyáº¿t MNAR khÃ´ng Ä‘Æ°á»£c xá»­ lÃ½ lÃ m máº¥t tÃ­n hiá»‡u dá»± Ä‘oÃ¡n thay vÃ¬ Ä‘iá»n chÃºng; Ä‘á»™ lá»‡ch pháº£i chÆ°a Ä‘Æ°á»£c xá»­ lÃ½ khiáº¿n cÃ¡c estimator dá»±a trÃªn gradient vÃ  khoáº£ng cÃ¡ch overfit theo giÃ¡ trá»‹ cá»±c Ä‘oan; vÃ  cÃ¡c báº£n ghi cÃ³ ngÃ y trong tÆ°Æ¡ng lai gÃ¢y rÃ² rá»‰ nhÃ£n (label leakage) lÃ m cho cÃ¡c chá»‰ sá»‘ Ä‘Ã¡nh giÃ¡ trá»Ÿ nÃªn láº¡c quan má»™t cÃ¡ch giáº£ táº¡o. Bá»‘n bÆ°á»›c lÃ m sáº¡ch Ä‘Æ°á»£c mÃ´ táº£ trong chÆ°Æ¡ng nÃ y, Ã¡p dá»¥ng theo thá»© tá»± Ä‘Æ°á»£c thiáº¿t láº­p bá»Ÿi trÃ¬nh tá»± pipeline chá»‘ng rÃ² rá»‰, táº¡o ra bá»™ dá»¯ liá»‡u mÃ  trÃªn Ä‘Ã³ bÆ°á»›c phÃ¢n chia train/test vÃ  giai Ä‘oáº¡n biáº¿n Ä‘á»•i cÃ³ thá»ƒ hoáº¡t Ä‘á»™ng Ä‘Ãºng Ä‘áº¯n vÃ  cÃ³ tÃ­nh tÃ¡i táº¡o.

