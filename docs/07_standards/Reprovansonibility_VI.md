# HÆ°á»›ng Dáº«n TÃ¡i Táº¡o Káº¿t Quáº£

**Phá»¥ Ä‘á»:** ToÃ n bá»™ nhá»¯ng gÃ¬ ngÆ°á»i Ä‘á»c bÃªn ngoÃ i cáº§n Ä‘á»ƒ tÃ¡i táº¡o báº£ng tá»•ng há»£p vÃ  cÃ¡c sáº£n pháº©m dá»¯ liá»‡u phÃ¡i sinh

_DSP391m â€“ NhÃ³m 5 Â· BÃ¡o cÃ¡o 2 (Data Tasks), ChÆ°Æ¡ng 3 Â· Háº¡ng má»¥c STT 31 (Huy Anh)_

---

## 1. Má»¥c ÄÃ­ch

Kháº£ nÄƒng tÃ¡i táº¡o káº¿t quáº£ (reprovansonibility) lÃ  yÃªu cáº§u báº­c nháº¥t trong cÃ´ng viá»‡c khoa há»c dá»¯ liá»‡u. HÆ°á»›ng dáº«n nÃ y ghi láº¡i cÃ¡c bÆ°á»›c chÃ­nh xÃ¡c, mÃ´i trÆ°á»ng (environment) vÃ  cÃ¡c biá»‡n phÃ¡p kiá»ƒm soÃ¡t nguá»“n gá»‘c dá»¯ liá»‡u (data provenance) Ä‘á»ƒ báº¥t ká»³ ngÆ°á»i Ä‘á»c bÃªn ngoÃ i nÃ o â€” bao gá»“m thÃ nh viÃªn nhÃ³m trong tÆ°Æ¡ng lai vÃ  ngÆ°á»i Ä‘Ã¡nh giÃ¡ â€” Ä‘á»u cÃ³ thá»ƒ tÃ¡i táº¡o má»i sáº£n pháº©m Ä‘áº§u ra cá»§a pipeline nÃ y, tá»«ng bit má»™t, báº¯t Ä‘áº§u tá»« bá»™ dá»¯ liá»‡u thÃ´ OULAD Ä‘Ã£ táº£i vá».

---

## 2. TÃ­nh Táº¥t Äá»‹nh

Má»™t háº¡t giá»‘ng ngáº«u nhiÃªn toÃ n cá»¥c (global random seed) duy nháº¥t Ä‘Æ°á»£c sá»­ dá»¥ng xuyÃªn suá»‘t táº¥t cáº£ cÃ¡c script, notebook vÃ  trÆ°á»ng há»£p kiá»ƒm thá»­:

```python
RANDOM_SEED = 42
```

Má»i lá»‡nh gá»i Ä‘áº¿n `numpy.random`, `random`, cÃ¡c bá»™ chia dá»¯ liá»‡u (splitters) cá»§a `sklearn` vÃ  báº¥t ká»³ hÃ m láº¥y máº«u nÃ o Ä‘á»u pháº£i dÃ¹ng háº±ng sá»‘ nÃ y. Háº±ng sá»‘ Ä‘Æ°á»£c Ä‘á»‹nh nghÄ©a má»™t láº§n trong `src/config.py` vÃ  Ä‘Æ°á»£c nháº­p (import) á»Ÿ má»i nÆ¡i khÃ¡c; tuyá»‡t Ä‘á»‘i khÃ´ng Ä‘Æ°á»£c hard-code cá»¥c bá»™.

---

## 3. Nguá»“n Gá»‘c Dá»¯ Liá»‡u

### 3.1 Tá»‡p KÃª Khai Dá»¯ Liá»‡u ThÃ´

Tá»‡p `data/raw/data_manifest.txt` Ä‘Æ°á»£c táº¡o tá»± Ä‘á»™ng bá»Ÿi `setup_raw_data.py` vÃ  ghi láº¡i cÃ¡c trÆ°á»ng sau cho má»—i trong báº£y tá»‡p CSV cá»§a OULAD:

| TrÆ°á»ng | MÃ´ táº£ |
|---|---|
| TÃªn tá»‡p (Filename) | TÃªn tá»‡p chÃ­nh xÃ¡c (vÃ­ dá»¥: `studentInfo.csv`) |
| MÃ£ bÄƒm MD5 (MD5 hash) | Chuá»—i hex cá»§a tá»‡p Ä‘Ã£ táº£i vá» chÆ°a qua chá»‰nh sá»­a |
| KÃ­ch thÆ°á»›c (Size, MB) | Dung lÆ°á»£ng tá»‡p lÃ m trÃ²n hai chá»¯ sá»‘ tháº­p phÃ¢n |
| NgÃ y táº£i vá» (Download date) | NgÃ y táº£i tá»‡p theo Ä‘á»‹nh dáº¡ng ISO-8601 |

Báº£y tá»‡p Ä‘Æ°á»£c bao gá»“m: `courses.csv`, `assessments.csv`, `vle.csv`, `studentInfo.csv`, `studentRegistration.csv`, `studentAssessment.csv`, `studentVle.csv`.

### 3.2 Báº£o Vá»‡ Chá»‰ Äá»c

Sau khi tá»‡p kÃª khai Ä‘Æ°á»£c ghi, `setup_raw_data.py` Ä‘áº·t má»—i tá»‡p CSV thÃ´ thÃ nh chá»‰ Ä‘á»c (read-only) (`chmod 444` trÃªn Linux/macOS; `attrib +R` trÃªn Windows), ngÄƒn ngá»«a ghi Ä‘Ã¨ vÃ´ Ã½.

### 3.3 XÃ¡c Minh TÃ­nh ToÃ n Váº¹n

Äá»ƒ xÃ¡c minh tÃ­nh toÃ n váº¹n dá»¯ liá»‡u (data integrity) vÃ o báº¥t ká»³ thá»i Ä‘iá»ƒm nÃ o, hÃ£y cháº¡y láº¡i `setup_raw_data.py`. Script sáº½ tÃ­nh láº¡i MD5 cá»§a má»—i tá»‡p vÃ  so sÃ¡nh vá»›i tá»‡p kÃª khai Ä‘Ã£ lÆ°u. Báº¥t ká»³ sá»± khÃ´ng khá»›p nÃ o sáº½ lÃ m dá»«ng chÆ°Æ¡ng trÃ¬nh vá»›i ngoáº¡i lá»‡ (exception) trÆ°á»›c khi báº¥t ká»³ bÆ°á»›c nÃ o á»Ÿ háº¡ nguá»“n Ä‘Æ°á»£c thá»±c thi.

---

## 4. MÃ´i TrÆ°á»ng

- **PhiÃªn báº£n Python:** 3.13 (quáº£n lÃ½ qua Conda; xem bá»™ phiÃªn báº£n Ä‘Ã£ kiá»ƒm chá»©ng á»Ÿ Má»¥c 4.1)
- **Ghim phiÃªn báº£n phá»¥ thuá»™c (Dependency pinning):** `requirements.txt` (cÃ i Ä‘áº·t qua pip, phiÃªn báº£n chÃ­nh xÃ¡c) vÃ  `environment.yml` (toÃ n bá»™ mÃ´i trÆ°á»ng Conda, bao gá»“m cÃ¡c gÃ³i ngoÃ i Python)
- **LÆ°u Ã½ vá» váº½ biá»ƒu Ä‘á»“:** Viá»‡c táº¡o hÃ¬nh áº£nh báº±ng Matplotlib yÃªu cáº§u mÃ´i trÆ°á»ng cÃ³ bá»™ phÃ´ng chá»¯/freetype hoáº¡t Ä‘á»™ng Ä‘Æ°á»£c. TrÃªn cÃ¡c mÃ¡y chá»§ headless tá»‘i giáº£n, hÃ£y cÃ i `libfreetype6-dev` (Debian/Ubuntu) hoáº·c tÆ°Æ¡ng Ä‘Æ°Æ¡ng trÆ°á»›c khi cháº¡y bÆ°á»›c EDA.

Äá»ƒ tÃ¡i táº¡o mÃ´i trÆ°á»ng:

```bash
conda env create -f environment.yml
conda activate dsp
```

Hoáº·c chá»‰ dÃ¹ng pip:

```bash
pip install -r requirements.txt
```

### 4.1 MÃ´i TrÆ°á»ng ÄÃ£ Kiá»ƒm Chá»©ng (2026-07-12)

ToÃ n bá»™ sáº£n pháº©m Ä‘Ã£ commit (bundle mÃ´ hÃ¬nh, báº£ng, hÃ¬nh) Ä‘Æ°á»£c build trÃªn Windows vá»›i bá»™ gÃ³i sau â€” `environment.yml` hiá»‡n ghim Ä‘Ãºng bá»™ nÃ y:

| GÃ³i | PhiÃªn báº£n | GÃ³i | PhiÃªn báº£n |
|---|---|---|---|
| Python | 3.13.9 | matplotlib | 3.10.8 |
| numpy | 2.3.5 | seaborn | 0.13.2 |
| pandas | 2.3.3 | joblib | 1.5.2 |
| scipy | 1.16.3 | shap | 0.52.0 |
| pyarrow | 21.0.0 | lime | 0.2.0.1 |
| scikit-learn | 1.8.0 | loguru | 0.7.3 |
| xgboost | 3.1.3 | imbalanced-learn | 0.14.2 |
| lightgbm | 4.6.0 | | |

(KÃ¨m `python-dotenv`, `pytest`, `jupyter`, `nbformat`; `pandoc` 3.8 Ä‘á»ƒ sinh docx/deck.)

**TÆ°Æ¡ng thÃ­ch bundle.** CÃ¡c bundle `.joblib` Ä‘Ã£ commit lÃ  pickle cá»§a scikit-learn 1.8 / numpy 2.x. Vá»›i bá»™ pin cÅ© (Python 3.11 / scikit-learn 1.5 / numpy < 2), bundle ANN (`models/ann_t100.joblib`) load tháº¥t báº¡i (`MT19937 is not a known BitGenerator`), cÃ¡c bundle cÃ²n láº¡i chá»‰ load Ä‘Æ°á»£c kÃ¨m `InconsistentVersionWarning` (káº¿t quáº£ khÃ´ng Ä‘Æ°á»£c Ä‘áº£m báº£o). LuÃ´n dÃ¹ng Ä‘Ãºng mÃ´i trÆ°á»ng Ä‘Ã£ ghim á»Ÿ trÃªn.

**Guard phÃ¢n chia dá»¯ liá»‡u.** `data/splits/test_student_ids.csv` (5.756 sinh viÃªn) lÃ  nguá»“n sá»± tháº­t Ä‘Ã£ commit. `python -m src.evaluation.make_split` cÃ³ guard: náº¿u tá»‡p id Ä‘Ã£ tá»“n táº¡i, lá»‡nh chá»‰ náº¡p láº¡i chá»© khÃ´ng bao giá» tá»± tÃ­nh láº¡i phÃ©p chia. TÃ¡ch láº¡i (`--rederive`) báº±ng phiÃªn báº£n scikit-learn khÃ¡c sáº½ Ä‘á»•i 4.574/5.756 id vÃ  vÃ´ hiá»‡u má»i sá»‘ liá»‡u Ä‘Ã£ cÃ´ng bá»‘ â€” chá»‰ dÃ nh cho quyáº¿t Ä‘á»‹nh cá»§a cáº£ nhÃ³m.

---

## 5. CÃ¡c BÆ°á»›c TÃ¡i Táº¡o ChÃ­nh XÃ¡c

Cháº¡y táº¥t cáº£ lá»‡nh tá»« **thÆ° má»¥c gá»‘c cá»§a dá»± Ã¡n (project root)** theo thá»© tá»± dÆ°á»›i Ä‘Ã¢y. Má»—i bÆ°á»›c lÃ  idempotent (tá»©c lÃ  cháº¡y láº¡i nhiá»u láº§n váº«n cho cÃ¹ng káº¿t quáº£).

```
1. python setup_raw_data.py
```
XÃ¡c minh báº£y tá»‡p CSV thÃ´ vá»›i tá»‡p kÃª khai, ghi `data/raw/data_manifest.txt` náº¿u chÆ°a cÃ³, vÃ  Ä‘áº·t cÃ¡c tá»‡p thÃ nh chá»‰ Ä‘á»c.

```
2. python -m src.data.time_utils
```
XÃ¢y dá»±ng `data/checkpoint_map.csv` vÃ  cháº¡y tá»± kiá»ƒm tra (self-check) Ä‘á»ƒ xÃ¡c nháº­n cÃ¡c má»‘c checkpoint (checkpoint boundaries) Ä‘Ãºng vá» máº·t thá»i gian (khÃ´ng rÃ² rá»‰ dá»¯ liá»‡u tÆ°Æ¡ng lai táº¡i báº¥t ká»³ checkpoint nÃ o).

```
3. python -m src.data.build_master_table
```
Táº¡o ra:
- `data/interim/master_raw.parquet` â€” báº£ng tá»•ng há»£p (32.593 hÃ ng Ã— 33 cá»™t)
- `data/interim/master_join_log.csv` â€” sá»‘ hÃ ng sau má»—i bÆ°á»›c káº¿t há»£p báº£ng trÃ¡i (left-join)
- `data/interim/master_cleaning_log.csv` â€” há»“ sÆ¡ ghi láº¡i má»i quyáº¿t Ä‘á»‹nh lÃ m sáº¡ch dá»¯ liá»‡u

```
4. python -m src.data.make_checkpoints
```
Táº¡o ra:
- `data/checkpoints/dataset_t10.parquet` Ä‘áº¿n `dataset_t100.parquet` (sÃ¡u tá»‡p táº¡i cÃ¡c má»‘c 10 %, 30 %, 50 %, 70 %, 90 %, 100 % cá»§a module)
- `data/checkpoints/checkpoint_summary.csv`

BÆ°á»›c nÃ y **cÃ³ thá»ƒ tiáº¿p tá»¥c sau giÃ¡n Ä‘oáº¡n (resumable)**: náº¿u bá»‹ dá»«ng giá»¯a chá»«ng, cháº¡y láº¡i sáº½ bá» qua cÃ¡c tá»‡p checkpoint Ä‘Ã£ ghi vÃ  tiáº¿p tá»¥c tá»« chá»— dá»«ng.

```
5. python -m src.eda.eda
```
Táº¡o ra:
- `reports/figures/*.png` â€” toÃ n bá»™ hÃ¬nh áº£nh phÃ¢n tÃ­ch khÃ¡m phÃ¡ dá»¯ liá»‡u (EDA figures)
- `reports/eda_findings.json` â€” thá»‘ng kÃª tÃ³m táº¯t dáº¡ng machine-readable

YÃªu cáº§u bá»™ phÃ´ng chá»¯/freetype hoáº¡t Ä‘á»™ng Ä‘Æ°á»£c (xem Má»¥c 4).

```
6. pytest tests/test_leakage.py
```
Cháº¡y kiá»ƒm tra rÃ² rá»‰ thá»i gian (temporal-leakage checks) vÃ  kiá»ƒm tra tÃ­nh toÃ n váº¹n phÃ¢n chia dá»¯ liá»‡u (split-integrity tests). Táº¥t cáº£ bÃ i kiá»ƒm thá»­ pháº£i vÆ°á»£t qua trÆ°á»›c khi báº¯t Ä‘áº§u báº¥t ká»³ cÃ´ng viá»‡c mÃ´ hÃ¬nh hÃ³a nÃ o.

---

## 6. CÃ¡c Äáº£m Báº£o Vá» TÃ­nh TÃ¡i Táº¡o

| Thuá»™c tÃ­nh | Äáº£m báº£o |
|---|---|
| Thá»±c thi notebook | Táº¥t cáº£ notebook cháº¡y tá»« Ä‘áº§u Ä‘áº¿n cuá»‘i (top-to-bottom) khÃ´ng cÃ³ lá»—i khi thá»±c hiá»‡n qua Restart & Run All |
| CÃ¡c bÆ°á»›c cháº¡y lÃ¢u | BÆ°á»›c 3 vÃ  4 Ä‘Æ°á»£c lÆ°u checkpoint vÃ  cÃ³ thá»ƒ tiáº¿p tá»¥c sau giÃ¡n Ä‘oáº¡n; má»™t láº§n cháº¡y bá»‹ ngáº¯t khÃ´ng bao giá» lÃ m há»ng Ä‘áº§u ra |
| Ghi nguyÃªn tá»­ (Atomic writes) | Táº¥t cáº£ tá»‡p Parquet Ä‘Æ°á»£c ghi vÃ o Ä‘Æ°á»ng dáº«n táº¡m thá»i rá»“i Ä‘á»•i tÃªn vÃ o vá»‹ trÃ­ cuá»‘i cÃ¹ng; náº¿u bá»‹ dá»«ng giá»¯a quÃ¡ trÃ¬nh ghi, tá»‡p trÆ°á»›c Ä‘Ã³ váº«n cÃ²n nguyÃªn |
| Sá»­ dá»¥ng seed | `RANDOM_SEED = 42` Ä‘Æ°á»£c dÃ¹ng cho má»i phÃ©p toÃ¡n ngáº«u nhiÃªn |

---

## 7. CÃ¡c Thá»±c Táº¿ ÄÃ£ ÄÆ°á»£c XÃ¡c Minh

CÃ¡c thá»±c táº¿ sau Ä‘Æ°á»£c thiáº¿t láº­p trong láº§n cháº¡y chuáº©n (canonical run) vÃ  pháº£i Ä‘Ãºng sau báº¥t ká»³ láº§n tÃ¡i táº¡o nÃ o:

- `master_raw.parquet` chá»©a **32.593 hÃ ng Ã— 33 cá»™t**.
- Táº¥t cáº£ phÃ©p káº¿t há»£p báº£ng trÃ¡i trong `build_master_table` báº£o toÃ n Ä‘Ãºng **32.593 hÃ ng** â€” khÃ´ng cÃ³ hÃ ng nÃ o bá»‹ trÃ¹ng láº·p vÃ  khÃ´ng cÃ³ hÃ ng nÃ o bá»‹ máº¥t.
- Báº£ng tá»•ng há»£p chá»©a **0 khÃ³a trÃ¹ng láº·p (duplicate keys)** (xÃ¡c minh bá»Ÿi `pytest tests/test_leakage.py`).
- Tá»· lá»‡ cÃ³ nguy cÆ¡ (at-risk rate) trong báº£ng tá»•ng há»£p lÃ  **52,8 %**.
- SÃ¡u táº­p dá»¯ liá»‡u checkpoint chia sáº» danh sÃ¡ch (roster) giá»‘ng há»‡t nhau gá»“m **32.593 lÆ°á»£t ghi danh (28.785 sinh viÃªn duy nháº¥t)** â€” khÃ´ng cÃ³ sinh viÃªn nÃ o xuáº¥t hiá»‡n á»Ÿ má»™t checkpoint mÃ  khÃ´ng cÃ³ á»Ÿ checkpoint khÃ¡c.

---

_NhÃ³m 1 DSP391m. Cáº­p nháº­t láº§n cuá»‘i: 2026-07-12._

