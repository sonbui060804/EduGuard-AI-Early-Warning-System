# Chiáº¿n lÆ°á»£c phÃ¢n chia dá»¯ liá»‡u: PhÃ¢n tÃ­ch vÃ  lá»±a chá»n

*So sÃ¡nh cÃ¡c chiáº¿n lÆ°á»£c phÃ¢n chia vÃ  láº­p luáº­n cho thiáº¿t káº¿ phÃ¹ há»£p dá»¯ liá»‡u theo thá»i gian, máº¥t cÃ¢n báº±ng vÃ  cÃ³ nhÃ³m*

**DSP391m â€“ NhÃ³m 5 Â· BÃ¡o cÃ¡o 2 (TÃ¡c vá»¥ dá»¯ liá»‡u), ChÆ°Æ¡ng 3 Â· Háº¡ng má»¥c STT 21 (Ngá»c Sang)**

---

## 1. VÃ¬ sao viá»‡c phÃ¢n chia cáº§n tháº­n trá»ng

Ba Ä‘áº·c tÃ­nh cá»§a dá»¯ liá»‡u rÃ ng buá»™c cÃ¡ch phÃ¢n chia:

- **CÃ³ nhÃ³m (grouped)** â€” má»™t sinh viÃªn (`id_student`) cÃ³ thá»ƒ xuáº¥t hiá»‡n á»Ÿ nhiá»u mÃ´nâ€“ká»³, nÃªn cÃ¡c báº£n ghi khÃ´ng Ä‘á»™c láº­p. PhÃ¢n chia theo dÃ²ng má»™t cÃ¡ch ngÃ¢y thÆ¡ cÃ³ thá»ƒ Ä‘Æ°a cÃ¹ng má»™t sinh viÃªn vÃ o cáº£ train vÃ  test (*rÃ² rá»‰ theo nhÃ³m*).
- **Máº¥t cÃ¢n báº±ng (nháº¹)** â€” lá»›p at-risk chiáº¿m ~52,8%; phÃ¢n chia ngáº«u nhiÃªn váº«n cÃ³ thá»ƒ lÃ m lá»‡ch tá»‰ lá»‡ táº­p kiá»ƒm tra vÃ  gÃ¢y sai lá»‡ch Ä‘Ã¡nh giÃ¡.
- **Theo thá»i gian (time-aware)** â€” sÃ¡u má»‘c dÃ¹ng chung má»™t trá»¥c so sÃ¡nh (RQ1), nÃªn táº­p kiá»ƒm tra pháº£i **Ä‘á»“ng nháº¥t** qua cÃ¡c má»‘c, náº¿u khÃ¡c thÃ¬ Ä‘Æ°á»ng cong hiá»‡u nÄƒng khÃ´ng so sÃ¡nh Ä‘Æ°á»£c.

## 2. CÃ¡c chiáº¿n lÆ°á»£c Ä‘Æ°á»£c so sÃ¡nh

| Chiáº¿n lÆ°á»£c | CÃ¡ch hoáº¡t Ä‘á»™ng | Æ¯u Ä‘iá»ƒm | NhÆ°á»£c Ä‘iá»ƒm |
|---|---|---|---|
| Hold-out Ä‘Æ¡n | Má»™t láº§n cáº¯t train/test | ÄÆ¡n giáº£n, nhanh | PhÆ°Æ¡ng sai cao; phá»¥ thuá»™c má»™t láº§n phÃ¢n chia |
| k-fold CV | k fold kiá»ƒm Ä‘á»‹nh luÃ¢n phiÃªn | DÃ¹ng háº¿t dá»¯ liá»‡u; phÆ°Æ¡ng sai tháº¥p hÆ¡n | Chi phÃ­ k láº§n; má»™t seed váº«n phá»¥ thuá»™c phÃ¢n chia |
| k-fold láº·p láº¡i | k-fold láº·p qua nhiá»u seed | Trung bÃ¬nh Â± Ä‘á»™ lá»‡ch á»•n Ä‘á»‹nh; khÃ´ng phá»¥ thuá»™c seed | Chi phÃ­ cao nháº¥t |
| Nested CV | CV trong Ä‘á»ƒ tinh chá»‰nh, ngoÃ i Ä‘á»ƒ Æ°á»›c lÆ°á»£ng | Æ¯á»›c lÆ°á»£ng khÃ´ng thiÃªn lá»‡ch khi cÃ³ tinh chá»‰nh | Ráº¥t tá»‘n kÃ©m; phá»©c táº¡p |

## 3. Thiáº¿t káº¿ lá»±a chá»n (theo Ä‘á» cÆ°Æ¡ng)

**Hold-out 20% táº­p kiá»ƒm tra + kiá»ƒm Ä‘á»‹nh chÃ©o 5-fold láº·p qua 5 seed trÃªn táº­p huáº¥n luyá»‡n.**

- **Táº­p kiá»ƒm tra 20% cá»‘ Ä‘á»‹nh má»™t láº§n**, theo `id_student`, vÃ  dÃ¹ng láº¡i á»Ÿ má»i má»‘c (STT 8) Ä‘á»ƒ sÃ¡u Ä‘iá»ƒm so sÃ¡nh Ä‘Æ°á»£c.
- TrÃªn 80% cÃ²n láº¡i, CV **5-fold Ã— 5 seed** giáº£m phÆ°Æ¡ng sai do má»™t láº§n phÃ¢n chia; chá»‰ sá»‘ bÃ¡o cÃ¡o dáº¡ng **trung bÃ¬nh Â± Ä‘á»™ lá»‡ch chuáº©n** qua 25 láº§n khá»›p.
- Cáº£ phÃ¢n chia kiá»ƒm tra láº«n cÃ¡c fold CV Ä‘á»u **báº£o toÃ n nhÃ³m (theo `id_student`) vÃ  phÃ¢n táº§ng (theo `at_risk`)** qua `StratifiedGroupKFold` (xem `src/evaluation/split_harness.py`).

Thiáº¿t káº¿ nÃ y cÃ¢n báº±ng Ä‘á»™ á»•n Ä‘á»‹nh vÃ  chi phÃ­: k-fold láº·p cho Æ°á»›c lÆ°á»£ng á»•n Ä‘á»‹nh, cÃ²n má»™t táº­p kiá»ƒm tra hold-out cá»‘ Ä‘á»‹nh giá»¯ kháº£ nÄƒng so sÃ¡nh qua cÃ¡c má»‘c. Nested CV Ä‘Æ°á»£c Ä‘Ã¡nh giÃ¡ lÃ  quÃ¡ tá»‘n kÃ©m so vá»›i pháº¡m vi dá»± kiáº¿n.

## 4. Quy Æ°á»›c bÃ¡o cÃ¡o chá»‰ sá»‘

VÃ¬ lá»›p dÆ°Æ¡ng (at-risk) lÃ  lá»›p khÃ´ng Ä‘Æ°á»£c bá» sÃ³t, chá»‰ sá»‘ chÃ­nh lÃ  **PR-AUC** vÃ  **recall trÃªn lá»›p at-risk**, bÃ¡o cÃ¡o dáº¡ng **trung bÃ¬nh Â± Ä‘á»™ lá»‡ch** qua cÃ¡c fold/seed. Accuracy chá»‰ bÃ¡o cÃ¡o nhÆ° chá»‰ sá»‘ phá»¥ (dá»… gÃ¢y hiá»ƒu nháº§m khi cÃ³ máº¥t cÃ¢n báº±ng).

## 5. Thuá»™c tÃ­nh Ä‘Ã£ kiá»ƒm chá»©ng (trÃªn dá»¯ liá»‡u nÃ y)

DÃ¹ng phÃ¢n chia 20% cá»‘ Ä‘á»‹nh trÃªn `master_raw` (32.593 dÃ²ng): **0 sinh viÃªn trÃ¹ng** giá»¯a train vÃ  test, vÃ  tá»‰ lá»‡ at-risk Ä‘Æ°á»£c báº£o toÃ n (train â‰ˆ 0,53, test â‰ˆ 0,52, chÃªnh lá»‡ch â‰¤ 0,02). CÃ¡c kiá»ƒm tra nÃ y Ä‘Æ°á»£c kháº³ng Ä‘á»‹nh trong `tests/test_leakage.py`.

## 6. PhÃ¢n chia Ä‘Ã£ váº­t cháº¥t hoÃ¡ vÃ  dá»¯ liá»‡u náº±m á»Ÿ Ä‘Ã¢u

PhÃ©p phÃ¢n chia Ä‘Æ°á»£c Ä‘á»‹nh nghÄ©a **má»™t láº§n** vÃ  lÆ°u láº¡i bá»Ÿi `src/evaluation/make_split.py`:

| Sáº£n pháº©m | Vá»‹ trÃ­ | CÃ³ commit? |
|---|---|---|
| Danh sÃ¡ch `id_student` táº­p test (5.756 SV) | `data/splits/test_student_ids.csv` | cÃ³ |
| BÃ¡o cÃ¡o kiá»ƒm chá»©ng (theo tá»«ng dataset) | `reports/tables/split_report.csv` | cÃ³ |
| Dá»¯ liá»‡u train/test Ä‘Ã£ táº¡o (master + tá»«ng má»‘c) | `data/splits/*_train.parquet`, `*_test.parquet` | git bá» qua, tÃ¡i táº¡o Ä‘Æ°á»£c |

BÃ¡o cÃ¡o phÃ¢n chia xÃ¡c nháº­n thiáº¿t káº¿ trÃªn `master_raw` vÃ  **cáº£ sÃ¡u má»‘c**: train **26.104** dÃ²ng Â· test **6.489** dÃ²ng (5.756 SV) Â· at-risk **0,530 / 0,520** Â· **0 trÃ¹ng** â€” y há»‡t á»Ÿ má»i má»‘c. Giai Ä‘oáº¡n mÃ´ hÃ¬nh náº¡p phÃ¢n chia cá»§a má»™t má»‘c báº±ng má»™t lá»‡nh:

```python
from src.evaluation.make_split import load_checkpoint_split
X_train, X_test = load_checkpoint_split(40)   # train/test táº¡i má»‘c 40%
```

## TÃ i liá»‡u tham kháº£o

1. M. Adnan vÃ  cá»™ng sá»±, *IEEE Access*, vol. 9, tr. 7519â€“7539, 2021.
2. N. Tomasevic, N. Gvozdenovic, S. Vranes, *Computers & Evansonation*, vol. 143, art. 103676, 2020.

