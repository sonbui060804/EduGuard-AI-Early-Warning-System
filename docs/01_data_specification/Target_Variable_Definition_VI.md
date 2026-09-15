# Äá»‹nh nghÄ©a biáº¿n má»¥c tiÃªu vÃ  quy Æ°á»›c xá»­ lÃ½ Withdrawn theo thá»i gian

*NhÃ£n nhá»‹ phÃ¢n at-risk cho bÃ i toÃ¡n phÃ¡t hiá»‡n sá»›m sinh viÃªn nguy cÆ¡ trÃªn OULAD*

**DSP391m â€“ NhÃ³m 5 Â· BÃ¡o cÃ¡o 2 (TÃ¡c vá»¥ dá»¯ liá»‡u), ChÆ°Æ¡ng 3 Â· Háº¡ng má»¥c STT 1 (cáº£ nhÃ³m) & STT 26 (Vinh)**
*Tham chiáº¿u: biÃªn báº£n thá»‘ng nháº¥t nhÃ³m BB-B0-N1 (BÆ°á»›c 0).*

---

## 1. PhÃ¡t biá»ƒu bÃ i toÃ¡n

Äá» tÃ i lÃ  bÃ i toÃ¡n **phÃ¢n loáº¡i nhá»‹ phÃ¢n** (binary classification): táº¡i má»—i má»‘c tiáº¿n Ä‘á»™ khoÃ¡ há»c, dá»± Ä‘oÃ¡n sinh viÃªn cÃ³ **nguy cÆ¡ (at-risk)** hay khÃ´ng. KhÃ´ng thá»±c hiá»‡n há»“i quy Ä‘iá»ƒm; chá»‰ sá»­ dá»¥ng OULAD. NhÃ£n Ä‘Æ°á»£c suy ra tá»« trÆ°á»ng `final_result` trong báº£ng `studentInfo` vÃ  **cá»‘ Ä‘á»‹nh xuyÃªn suá»‘t sÃ¡u má»‘c thá»i gian**.

## 2. Ãnh xáº¡ `final_result` sang nhÃ£n nhá»‹ phÃ¢n

| `final_result` | Ã nghÄ©a | NhÃ³m | NhÃ£n (mÃ£) |
|---|---|---|---|
| Distinction | Äáº¡t loáº¡i giá»i | Äáº¡t | not-at-risk (0) |
| Pass | Äáº¡t | Äáº¡t | not-at-risk (0) |
| Fail | TrÆ°á»£t mÃ´n | Nguy cÆ¡ | at-risk (1) |
| Withdrawn | RÃºt mÃ´n | Nguy cÆ¡ | at-risk (1) |

```python
df["at_risk"] = df["final_result"].isin(["Fail", "Withdrawn"]).astype(int)
# 1 = at-risk (lá»›p dÆ°Æ¡ng cáº§n phÃ¡t hiá»‡n); 0 = not-at-risk
```

**Há»£p nháº¥t Distinction vÃ o Pass.** BÃ i toÃ¡n lÃ  nhá»‹ phÃ¢n; Distinction lÃ  káº¿t quáº£ *tá»‘t hÆ¡n* Pass vÃ  khÃ´ng thuá»™c Ä‘á»‘i tÆ°á»£ng cáº§n can thiá»‡p. Viá»‡c há»£p nháº¥t giÃºp Ä‘á»‹nh nghÄ©a lá»›p rÃµ rÃ ng, trÃ¡nh táº¡o thÃªm má»™t lá»›p quÃ¡ nhá», vÃ  bÃ¡m Ä‘Ãºng má»¥c tiÃªu *phÃ¡t hiá»‡n nguy cÆ¡* thay vÃ¬ *xáº¿p háº¡ng má»©c Ä‘á»™ Ä‘áº¡t*.

## 3. PhÃ¢n phá»‘i lá»›p thá»±c táº¿ (khÃ´ng dÃ¹ng sá»‘ liá»‡u minh hoáº¡ trÃªn slide)

Äo trÃªn 32.593 báº£n ghi sinh viÃªnâ€“mÃ´nâ€“ká»³ cá»§a `studentInfo`:

| Lá»›p | GiÃ¡ trá»‹ `final_result` | Sá»‘ lÆ°á»£ng | Tá»‰ lá»‡ |
|---|---|---|---|
| not-at-risk (0) | Pass (12.361) + Distinction (3.024) | 15.385 | 47,2% |
| at-risk (1) | Fail (7.052) + Withdrawn (10.156) | 17.208 | **52,8%** |

NhÆ° váº­y lá»›p at-risk lÃ  **lá»›p Ä‘a sá»‘ nháº¹** (â‰ˆ52,8%); má»©c **máº¥t cÃ¢n báº±ng lÃ  nháº¹**. Con sá»‘ "68/32" Ä‘Ã´i khi xuáº¥t hiá»‡n trÃªn slide chá»‰ **mang tÃ­nh minh hoáº¡** vÃ  khÃ´ng Ä‘Æ°á»£c trÃ­ch dáº«n nhÆ° sá»‘ liá»‡u cá»§a bá»™ dá»¯ liá»‡u. DÃ¹ máº¥t cÃ¢n báº±ng nháº¹, viá»‡c Ä‘Ã¡nh giÃ¡ váº«n dÃ¹ng **PR-AUC vÃ  recall trÃªn lá»›p at-risk**, vÃ¬ bá» sÃ³t má»™t sinh viÃªn nguy cÆ¡ lÃ  sai láº§m tá»‘n kÃ©m nháº¥t (xem STT 25).

## 4. Quy Æ°á»›c xá»­ lÃ½ Withdrawn theo thá»i gian â€” PhÆ°Æ¡ng Ã¡n A (Ä‘Ã£ chá»n)

Táº¡i má»‘c *t%*, má»™t sinh viÃªn Withdrawn cÃ³ thá»ƒ rÃºt mÃ´n **trÆ°á»›c** hoáº·c **sau** ngÃ y má»‘c. NhÃ³m chá»n **PhÆ°Æ¡ng Ã¡n A â€” nhÃ£n cá»‘ Ä‘á»‹nh, giá»¯ nguyÃªn quáº§n thá»ƒ**:

1. NhÃ£n cá»§a má»—i sinh viÃªn **cá»‘ Ä‘á»‹nh** theo `final_result` táº¡i má»i má»‘c (nhÃ£n khÃ´ng Ä‘á»•i theo *t*).
2. Táº­p sinh viÃªn **Ä‘á»“ng nháº¥t** qua cáº£ sÃ¡u má»‘c vÃ  táº­p kiá»ƒm tra, Ä‘Ã¡p á»©ng yÃªu cáº§u táº­p kiá»ƒm tra cá»‘ Ä‘á»‹nh (STT 8).
3. Sinh viÃªn Withdrawn rÃºt trÆ°á»›c má»‘c *t* váº«n Ä‘Æ°á»£c **giá»¯** trong dá»¯ liá»‡u má»‘c *t* vÃ  váº«n **gÃ¡n nhÃ£n at-risk**. Äáº·c trÆ°ng cá»§a há» chá»‰ pháº£n Ã¡nh hoáº¡t Ä‘á»™ng tá»›i ngÃ y rÃºt nÃªn ráº¥t tháº¥p â€” vÃ  chÃ­nh **sá»± suy giáº£m hoáº¡t Ä‘á»™ng nÃ y lÃ  tÃ­n hiá»‡u cáº£nh bÃ¡o sá»›m**, khÃ´ng pháº£i lá»—i dá»¯ liá»‡u.
4. HÃ m cáº¯t theo thá»i gian (STT 11) tá»± Ä‘á»™ng loáº¡i má»i sá»± kiá»‡n cÃ³ ngÃ y vÆ°á»£t má»‘c, nÃªn **khÃ´ng phÃ¡t sinh rÃ² rá»‰ thá»i gian**.

**Háº¡n cháº¿ cáº§n ghi nháº­n.** á»ž cÃ¡c má»‘c muá»™n, sinh viÃªn rÃºt sá»›m gáº§n nhÆ° khÃ´ng cÃ²n hoáº¡t Ä‘á»™ng nÃªn mÃ´ hÃ¬nh dá»… phÃ¡t hiá»‡n, cÃ³ thá»ƒ khiáº¿n recall vÃ  PR-AUC láº¡c quan hÆ¡n thá»±c táº¿. BÃ¡o cÃ¡o lÆ°á»£ng hoÃ¡ háº¡n cháº¿ nÃ y báº±ng phÃ¢n tÃ­ch Ä‘á»™ nháº¡y trÃªn nhÃ³m cÃ²n-Ä‘ang-há»c trÃ¬nh bÃ y á»Ÿ Má»¥c 5 â€” phiÃªn báº£n phÃ­a-Ä‘Ã¡nh-giÃ¡ cá»§a phÆ°Æ¡ng Ã¡n thay tháº¿ *PhÆ°Æ¡ng Ã¡n B (kiá»ƒm duyá»‡t theo má»‘c)*.

## 5. Hai khung Ä‘á»c cá»§a biáº¿n má»¥c tiÃªu (lÃ m rÃµ estimand)

NhÃ£n cá»‘ Ä‘á»‹nh cá»§a PhÆ°Æ¡ng Ã¡n A há»— trá»£ hai estimand (Ä‘á»‘i tÆ°á»£ng suy luáº­n) khÃ¡c nhau, vÃ  má»i chá»‰ sá»‘ cÃ´ng bá»‘ pháº£i nÃªu rÃµ nÃ³ thuá»™c khung nÃ o.

1. **PhÃ¢n loáº¡i káº¿t quáº£ cuá»‘i khoÃ¡ â€” khung benchmark chÃ­nh.** CÃ¢u há»i "lÆ°á»£t ghi danh nÃ y sáº½ káº¿t thÃºc báº±ng Fail hay Withdrawn?" Ä‘Æ°á»£c Ä‘á»‹nh nghÄ©a trÃªn toÃ n bá»™ 32.593 báº£n ghi ghi danh táº¡i má»i má»‘c. ÄÃ¢y lÃ  khung cho phÃ©p so sÃ¡nh káº¿t quáº£ vá»›i cÃ¡c nghiÃªn cá»©u ná»n (Adnan vÃ  cá»™ng sá»±, 2021; Tomasevic vÃ  cá»™ng sá»±, 2020) â€” vá»‘n cÅ©ng giá»¯ nguyÃªn toÃ n bá»™ quáº§n thá»ƒ â€” vÃ  lÃ  khung cá»§a cÃ¡c báº£ng benchmark chÃ­nh cá»§a Ä‘á» tÃ i.

2. **Cáº£nh bÃ¡o sá»›m Ä‘á»ƒ can thiá»‡p â€” khung cÃ²n-Ä‘ang-há»c.** Can thiá»‡p chá»‰ Ä‘áº¿n Ä‘Æ°á»£c vá»›i sinh viÃªn chÆ°a rÃºt mÃ´n, nÃªn cÃ¢u há»i váº­n hÃ nh "giáº£ng viÃªn cáº§n liÃªn há»‡ ai táº¡i má»‘c *t*?" chá»‰ cÃ³ nghÄ©a trÃªn nhÃ³m cÃ²n Ä‘ang há»c táº¡i ngÃ y má»‘c. Ngay táº¡i *t* = 10%, Ä‘Ã£ cÃ³ 4.833 trÃªn 32.593 lÆ°á»£t ghi danh rÃºt trÆ°á»›c ngÃ y má»‘c (923 trong sá»‘ Ä‘Ã³ thuá»™c táº­p kiá»ƒm tra); vá»›i cÃ¡c báº£n ghi nÃ y khÃ´ng cÃ²n gÃ¬ Ä‘á»ƒ dá»± Ä‘oÃ¡n â€” chá»‰ cÃ²n ghi nháº­n.

**Há»‡ quáº£ Ä‘o Ä‘Æ°á»£c.** Recall trÃªn lá»›p at-risk cá»§a XGBoost táº¡i *t* = 40/80/100% lÃ  0,81/0,90/0,93 trÃªn toÃ n quáº§n thá»ƒ nhÆ°ng chá»‰ 0,678/0,779/0,841 trÃªn nhÃ³m cÃ²n-Ä‘ang-há»c (`reports/tables/sensitivity_active_xgb.csv`, sinh bá»Ÿi `tools/sensitivity_active.py`). Theo tiÃªu chÃ­ recall â‰¥ 0,80 cá»§a RQ1, toÃ n quáº§n thá»ƒ Ä‘áº¡t tá»« *t* = 40%, trong khi nhÃ³m cÃ²n-Ä‘ang-há»c chá»‰ Ä‘áº¡t táº¡i *t* = 100%. Nháº¥t quÃ¡n vá»›i Ä‘iá»u Ä‘Ã³, Ä‘áº·c trÆ°ng SHAP máº¡nh nháº¥t lÃ  `days_since_last_activity` (trung bÃ¬nh |SHAP| 3,57): trÃªn toÃ n quáº§n thá»ƒ, má»™t pháº§n sá»©c máº¡nh cá»§a mÃ´ hÃ¬nh lÃ  *phÃ¡t hiá»‡n sinh viÃªn Ä‘Ã£ rá»i Ä‘i*, chá»© khÃ´ng chá»‰ *dá»± bÃ¡o nguy cÆ¡ tÆ°Æ¡ng lai*. ÄÃ¢y **khÃ´ng pháº£i rÃ² rá»‰** â€” nhÃ£n khÃ´ng há» lá»t vÃ o Ä‘áº·c trÆ°ng, vÃ  má»©c hoáº¡t Ä‘á»™ng tháº¥p cá»§a sinh viÃªn Ä‘Ã£ rÃºt lÃ  hÃ nh vi tháº­t â€” mÃ  lÃ  **váº¥n Ä‘á» Ä‘á»‹nh nghÄ©a quáº§n thá»ƒ**.

**Quy táº¯c bÃ¡o cÃ¡o.** Má»i phÃ¡t biá»ƒu dáº¡ng "dá»± Ä‘oÃ¡n Ä‘Ã¡ng tin cáº­y tá»« *t* = 40%" pháº£i nÃªu rÃµ quáº§n thá»ƒ Ä‘Æ°á»£c nÃ³i tá»›i. Do Ä‘Ã³ Ä‘á» tÃ i bÃ¡o cÃ¡o song song cáº£ hai khung: káº¿t quáº£ toÃ n quáº§n thá»ƒ lÃ  benchmark chÃ­nh, káº¿t quáº£ nhÃ³m cÃ²n-Ä‘ang-há»c lÃ  phÃ¢n tÃ­ch Ä‘á»™ nháº¡y hÆ°á»›ng tá»›i can thiá»‡p.

## 6. Há»‡ quáº£ cho cÃ¡c bÆ°á»›c phÃ­a sau

Má»i háº¡ng má»¥c phá»¥ thuá»™c "BÆ°á»›c 0" Ä‘á»u káº¿ thá»«a Ä‘á»‹nh nghÄ©a nÃ y: quy táº¯c phÃ²ng rÃ² rá»‰ (STT 12), kháº£o sÃ¡t lÆ°á»£c Ä‘á»“ vÃ  báº£ng quy Ä‘á»•i má»‘c (STT 9, 10), thiáº¿t káº¿ phÃ¢n chia (STT 21), vÃ  tÃ i liá»‡u nguá»“n gá»‘c/Ä‘áº¡o Ä‘á»©c (STT 30). TÃªn cá»™t má»¥c tiÃªu lÃ  `at_risk`; `final_result` chá»‰ Ä‘Æ°á»£c giá»¯ láº¡i nhÆ° nguá»“n gá»‘c thÃ´ cá»§a nhÃ£n.

## TÃ i liá»‡u tham kháº£o

1. M. Adnan vÃ  cá»™ng sá»±, "Predicting at-Risk Students at Different Percentages of Course Length for Early Intervention," *IEEE Access*, vol. 9, tr. 7519â€“7539, 2021.
2. N. Tomasevic, N. Gvozdenovic, S. Vranes, "An overview and comparison of supervised data mining techniques for student exam performance prediction," *Computers & Evansonation*, vol. 143, art. 103676, 2020.
3. J. Kuzilek, M. Hlosta, Z. Zdrahal, "Open University Learning Analytics dataset," *Scientific Data*, vol. 4, art. 170171, 2017.

