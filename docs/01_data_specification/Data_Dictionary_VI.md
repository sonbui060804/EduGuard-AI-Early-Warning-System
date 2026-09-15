# Tá»« Ä‘iá»ƒn dá»¯ liá»‡u báº£ng há»£p nháº¥t OULAD (Ä‘áº§y Ä‘á»§)

*Bao phá»§ 100% cá»™t cá»§a master_raw. Tá»± sinh tá»« báº£ng há»£p nháº¥t.*

**DSP391m â€“ NhÃ³m 5 Â· BÃ¡o cÃ¡o 2 Â· STT 29 (Huy Anh)**

Tá»•ng sá»‘ biáº¿n: **33**

## Identifier

| # | Biáº¿n | Kiá»ƒu | Nguá»“n gá»‘c | MÃ´ táº£ | VÃ­ dá»¥ / Khoáº£ng |
|---|---|---|---|---|---|
| 1 | `code_module` | Danh Ä‘á»‹nh (ID) | Original | MÃ£ mÃ´n há»c; thuá»™c khoÃ¡ tá»•ng há»£p. | 7 unique |
| 2 | `code_presentation` | Danh Ä‘á»‹nh (ID) | Original | MÃ£ ká»³ há»c (B=thÃ¡ng 2, J=thÃ¡ng 10); thuá»™c khoÃ¡ tá»•ng há»£p. | 4 unique |
| 3 | `id_student` | Danh Ä‘á»‹nh (ID) | Original | MÃ£ sinh viÃªn duy nháº¥t; khoÃ¡ nhÃ³m cho GroupKFold (khÃ´ng lÃ  Ä‘áº·c trÆ°ng). | min 3733, max 2.7168e+06 |

## Demographic

| # | Biáº¿n | Kiá»ƒu | Nguá»“n gá»‘c | MÃ´ táº£ | VÃ­ dá»¥ / Khoáº£ng |
|---|---|---|---|---|---|
| 4 | `gender` | Nhá»‹ phÃ¢n | Original | Giá»›i tÃ­nh; mÃ£ hoÃ¡ M=1, F=0. | 2 unique |
| 5 | `region` | Danh Ä‘á»‹nh | Original | VÃ¹ng cá»§a Anh/Ireland (13 giÃ¡ trá»‹); mÃ£ hoÃ¡ one-hot. | 13 unique |
| 6 | `highest_evansonation` | Thá»© báº­c | Original | TrÃ¬nh Ä‘á»™ há»c váº¥n cao nháº¥t; thá»© báº­c 0..4. | 5 unique |
| 7 | `imd_band` | Thá»© báº­c | Original | Chá»‰ sá»‘ nghÃ¨o khÃ³ (IMD) theo vÃ¹ng; thá»© báº­c; 1.111 khuyáº¿t -> 'Unknown'. | 10 unique |
| 8 | `age_band` | Thá»© báº­c | Original | NhÃ³m tuá»•i; thá»© báº­c 0..2. | 3 unique |
| 9 | `num_of_prev_attempts` | Äá»‹nh lÆ°á»£ng (rá»i ráº¡c) | Original | Sá»‘ láº§n há»c láº¡i mÃ´n trÆ°á»›c Ä‘Ã³. | min 0, max 6 |
| 10 | `studied_credits` | Äá»‹nh lÆ°á»£ng (rá»i ráº¡c) | Original | Tá»•ng sá»‘ tÃ­n chá»‰ Ä‘ang há»c. | min 30, max 655 |
| 11 | `disability` | Nhá»‹ phÃ¢n | Original | Khai bÃ¡o khuyáº¿t táº­t; mÃ£ hoÃ¡ Y=1, N=0. | 2 unique |

## Engagement

| # | Biáº¿n | Kiá»ƒu | Nguá»“n gá»‘c | MÃ´ táº£ | VÃ­ dá»¥ / Khoáº£ng |
|---|---|---|---|---|---|
| 12 | `total_clicks` | Äá»‹nh lÆ°á»£ng (liÃªn tá»¥c) | Derived | Tá»•ng lÆ°á»£t click VLE tá»›i má»‘c; lá»‡ch pháº£i -> log1p. | min 0, max 24139 |
| 13 | `n_days_active` | Äá»‹nh lÆ°á»£ng (rá»i ráº¡c) | Derived | Sá»‘ ngÃ y cÃ³ hoáº¡t Ä‘á»™ng (distinct) tá»›i má»‘c. | min 0, max 286 |
| 14 | `max_clicks_single_day` | Äá»‹nh lÆ°á»£ng (liÃªn tá»¥c) | Derived | Sá»‘ click tá»‘i Ä‘a trong má»™t ngÃ y tá»›i má»‘c; lá»‡ch pháº£i máº¡nh -> log1p. | min 0, max 6988 |
| 15 | `clicks_forumng` | Äá»‹nh lÆ°á»£ng (liÃªn tá»¥c) | Derived | Click loáº¡i 'forumng' tá»›i má»‘c. | min 0, max 13154 |
| 16 | `clicks_oucontent` | Äá»‹nh lÆ°á»£ng (liÃªn tá»¥c) | Derived | Click loáº¡i 'oucontent' tá»›i má»‘c. | min 0, max 9308 |
| 17 | `clicks_resource` | Äá»‹nh lÆ°á»£ng (liÃªn tá»¥c) | Derived | Click loáº¡i 'resource' tá»›i má»‘c. | min 0, max 5147 |
| 18 | `clicks_homepage` | Äá»‹nh lÆ°á»£ng (liÃªn tá»¥c) | Derived | Click loáº¡i 'homepage' tá»›i má»‘c. | min 0, max 7277 |
| 19 | `clicks_oucollaborate` | Äá»‹nh lÆ°á»£ng (liÃªn tá»¥c) | Derived | Click loáº¡i 'oucollaborate' tá»›i má»‘c. | min 0, max 316 |
| 20 | `clicks_quiz` | Äá»‹nh lÆ°á»£ng (liÃªn tá»¥c) | Derived | Click loáº¡i 'quiz' tá»›i má»‘c. | min 0, max 13032 |
| 21 | `clicks_subpage` | Äá»‹nh lÆ°á»£ng (liÃªn tá»¥c) | Derived | Click loáº¡i 'subpage' tá»›i má»‘c. | min 0, max 4345 |
| 22 | `clicks_url` | Äá»‹nh lÆ°á»£ng (liÃªn tá»¥c) | Derived | Click loáº¡i 'url' tá»›i má»‘c. | min 0, max 2134 |
| 23 | `mean_clicks_per_active_day` | Äá»‹nh lÆ°á»£ng (liÃªn tá»¥c) | Derived | total_clicks / n_days_active (0 náº¿u khÃ´ng cÃ³ ngÃ y hoáº¡t Ä‘á»™ng); lá»‡ch pháº£i -> log1p. | min 0, max 221.2 |
| 24 | `days_since_last_activity` | Äá»‹nh lÆ°á»£ng (liÃªn tá»¥c) | Derived | Sá»‘ ngÃ y tá»« láº§n hoáº¡t Ä‘á»™ng cuá»‘i tá»›i ngÃ y má»‘c (lá»›n khi máº¥t tÆ°Æ¡ng tÃ¡c). | min 0, max 292 |

## Performance

| # | Biáº¿n | Kiá»ƒu | Nguá»“n gá»‘c | MÃ´ táº£ | VÃ­ dá»¥ / Khoáº£ng |
|---|---|---|---|---|---|
| 25 | `n_assessments_submitted` | Äá»‹nh lÆ°á»£ng (rá»i ráº¡c) | Derived | Sá»‘ bÃ i Ä‘Ã¡nh giÃ¡ Ä‘Ã£ ná»™p (khÃ´ng banked) tá»›i má»‘c. | min 0, max 14 |
| 26 | `mean_score_to_date` | Äá»‹nh lÆ°á»£ng (liÃªn tá»¥c) | Derived | Äiá»ƒm trung bÃ¬nh cÃ¡c bÃ i Ä‘Ã£ ná»™p tá»›i má»‘c [0-100]; 0 náº¿u chÆ°a ná»™p. | min 0, max 100 |
| 27 | `weighted_score_to_date` | Äá»‹nh lÆ°á»£ng (liÃªn tá»¥c) | Derived | Tá»•ng score x weight/100 cÃ¡c bÃ i Ä‘Ã£ ná»™p tá»›i má»‘c. | min 0, max 200 |
| 28 | `not_submitted` | Nhá»‹ phÃ¢n (chá»‰ bÃ¡o) | Derived | 1 náº¿u sinh viÃªn bá» lá»¡ >=1 bÃ i Ä‘Ã£ quÃ¡ háº¡n ná»™p; tÃ­n hiá»‡u nguy cÆ¡. | min 0, max 1 |

## Temporal

| # | Biáº¿n | Kiá»ƒu | Nguá»“n gá»‘c | MÃ´ táº£ | VÃ­ dá»¥ / Khoáº£ng |
|---|---|---|---|---|---|
| 29 | `date_registration` | Äá»‹nh lÆ°á»£ng (liÃªn tá»¥c) | Original | NgÃ y Ä‘Äƒng kÃ½ tÆ°Æ¡ng Ä‘á»‘i so vá»›i ngÃ y báº¯t Ä‘áº§u (cÃ³ thá»ƒ Ã¢m); 45 khuyáº¿t -> trung vá»‹ train. | min -322, max 167 |
| 30 | `date_unregistration` | Äá»‹nh lÆ°á»£ng (liÃªn tá»¥c) | Original | NgÃ y rÃºt mÃ´n; NaN náº¿u khÃ´ng rÃºt. DÃ¹ng Ä‘á»ƒ phÃ¢n tÃ­ch Withdrawn, khÃ´ng lÃ  Ä‘áº·c trÆ°ng. | min -365, max 444 |
| 31 | `module_presentation_length` | Äá»‹nh lÆ°á»£ng (rá»i ráº¡c) | Original | Äá»™ dÃ i mÃ´n-ká»³ tÃ­nh báº±ng ngÃ y; dÃ¹ng Ä‘á»ƒ quy Ä‘á»•i má»‘c sang ngÃ y. | min 234, max 269 |

## Target (raw)

| # | Biáº¿n | Kiá»ƒu | Nguá»“n gá»‘c | MÃ´ táº£ | VÃ­ dá»¥ / Khoáº£ng |
|---|---|---|---|---|---|
| 32 | `final_result` | Danh Ä‘á»‹nh (gá»‘c) | Original | Káº¿t quáº£ gá»‘c (Pass/Distinction/Fail/Withdrawn); nguá»“n cá»§a nhÃ£n. | 4 unique |

## Target

| # | Biáº¿n | Kiá»ƒu | Nguá»“n gá»‘c | MÃ´ táº£ | VÃ­ dá»¥ / Khoáº£ng |
|---|---|---|---|---|---|
| 33 | `at_risk` | Nhá»‹ phÃ¢n (má»¥c tiÃªu) | Derived | 1 náº¿u final_result thuá»™c {Fail, Withdrawn}, ngÆ°á»£c láº¡i 0. Cá»‘ Ä‘á»‹nh qua cÃ¡c má»‘c. | min 0, max 1 |

