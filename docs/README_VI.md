# BÃ¡o cÃ¡o 2 â€” TÃ¡c vá»¥ dá»¯ liá»‡u Â· Má»¥c lá»¥c tÃ i liá»‡u

**DSP391m â€“ NhÃ³m 5.** ThÆ° má»¥c nÃ y chá»©a cÃ¡c sáº£n pháº©m ChÆ°Æ¡ng 3/4 cho **Task 3 (Thu tháº­p & Tiá»n xá»­ lÃ½ dá»¯ liá»‡u)**. TÃ i liá»‡u song ngá»¯ (`_EN` / `_VI`), cÃ³ cáº£ Markdown vÃ  Word (`.docx`); cÃ¡c báº£ng tra cá»©u Ä‘á»ƒ dáº¡ng Excel; báº£n gá»‘c cÃ³ chá»¯ kÃ½ giá»¯ á»Ÿ dáº¡ng PDF trong `08_agreements/`. Má»¥c lá»¥c tiáº¿ng Anh: [`README_EN.md`](README_EN.md).

## Báº£n Ä‘á»“ phá»§ Task 3

Cáº¥u trÃºc thÆ° má»¥c bÃ¡m theo nÄƒm phÃ¢n tÃ­ch yÃªu cáº§u cá»§a Task 3, má»—i yÃªu cáº§u á»©ng vá»›i má»™t vá»‹ trÃ­:

| YÃªu cáº§u Task 3 | ThÆ° má»¥c | TÃ i liá»‡u chÃ­nh |
|---|---|---|
| 1 â€” XÃ¡c Ä‘á»‹nh dá»¯ liá»‡u cáº§n cÃ³ cho Ä‘á» tÃ i | `01_data_specification/` | `Data_Specification`, `Target_Variable_Definition`, `Data_Dictionary` (.md/.docx/.xlsx), `Variable_Typing.xlsx` |
| 2 â€” PhÃ¢n tÃ­ch phÆ°Æ¡ng phÃ¡p thu tháº­p dá»¯ liá»‡u | `02_collection/` | `Data_Collection_Methods`, `Data_Source_License_Ethics` |
| 3 â€” PhÃ¢n tÃ­ch phÆ°Æ¡ng phÃ¡p lÃ m sáº¡ch dá»¯ liá»‡u | `03_cleaning/` | `Cleaning_Methods`, `Leakage_Prevention_Rules` |
| 4 â€” Chuáº©n hoÃ¡ & biáº¿n Ä‘á»•i dá»¯ liá»‡u | `04_transformation/` | `Transformation_Standardisation`, `Preprocessing_Sequence`, `Feature_Naming_Convention` |
| 5 â€” PhÃ¢n tÃ­ch tÃ¡ch táº­p train/test | `05_splitting/` | `Split_Strategy_Analysis` |
| Há»— trá»£ â€” cÆ¡ sá»Ÿ báº±ng chá»©ng | `06_references/` | `Base_Studies_Comparison`, `Method_Justification` |
| Há»— trá»£ â€” quy chuáº©n & tÃ¡i láº­p | `07_standards/` | `Chart_Standards`, `Reprovansonibility` |
| Há»— trá»£ â€” báº£n gá»‘c cÃ³ chá»¯ kÃ½ | `08_agreements/` | `Step0_Agreement_Nhom1.pdf`, `Leakage_Rules_Signed_Nhom1.pdf` |

Sáº£n pháº©m tá»•ng há»£p hiá»‡n hÃ nh lÃ  chuá»—i notebook `notebooks/00â€¦06` cÃ¹ng bá»™ docs nÃ y (kÃ¨m slide trong `reports/slides/`); vá»›i chÆ°Æ¡ng nÃ y, báº£n thá»±c thi tÆ°Æ¡ng á»©ng lÃ  `notebooks/01_build_master_table.ipynb` (dá»±ng/lÃ m sáº¡ch) vÃ  `notebooks/02_eda.ipynb` (EDA ChÆ°Æ¡ng 4).

## MÃ£ nguá»“n, dá»¯ liá»‡u vÃ  káº¿t quáº£ (ngoÃ i `docs/`)

| Khu vá»±c | Vá»‹ trÃ­ |
|---|---|
| Pipeline dá»¯ liá»‡u | `src/data/` (tÆ°Æ¡ng tÃ¡c, káº¿t quáº£, báº£ng há»£p nháº¥t, má»‘c thá»i gian), `src/features/preprocessing.py` |
| Bá»™ phÃ¢n chia | `src/evaluation/split_harness.py` |
| EDA | `src/eda/` â†’ biá»ƒu Ä‘á»“ á»Ÿ `reports/figures/`, báº£ng thá»‘ng kÃª á»Ÿ `reports/tables/` |
| Kiá»ƒm thá»­ | `tests/test_leakage.py` (bá»™ kiá»ƒm thá»­ rÃ² rá»‰/phÃ¢n chia tá»± Ä‘á»™ng) |
| Bá»™ sinh | `tools/` (docx, notebook, tá»« Ä‘iá»ƒn dá»¯ liá»‡u, phÃ¢n loáº¡i biáº¿n, sÆ¡ Ä‘á»“ trÃ¬nh tá»±) |

## Dá»¯ liá»‡u train / test

PhÃ©p phÃ¢n chia Ä‘Æ°á»£c Ä‘á»‹nh nghÄ©a **má»™t láº§n** á»Ÿ cáº¥p sinh viÃªn â€” **táº­p kiá»ƒm tra 20% cá»‘ Ä‘á»‹nh** theo `id_student` (phÃ¢n táº§ng theo `at_risk`, seed 42) â€” vÃ  dÃ¹ng láº¡i Ä‘á»“ng nháº¥t trÃªn `master_raw` vÃ  cáº£ sÃ¡u má»‘c, Ä‘á»ƒ sÃ¡u Ä‘iá»ƒm hiá»‡u nÄƒng so sÃ¡nh Ä‘Æ°á»£c (STT 7, 8, 15).

| Sáº£n pháº©m | Vá»‹ trÃ­ | CÃ³ commit? |
|---|---|---|
| Äá»‹nh nghÄ©a phÃ¢n chia (danh sÃ¡ch `id_student` táº­p test, 5.756 SV) | `data/splits/test_student_ids.csv` | âœ… cÃ³ commit |
| BÃ¡o cÃ¡o kiá»ƒm chá»©ng phÃ¢n chia (kÃ­ch thÆ°á»›c, tá»‰ lá»‡ lá»›p, 0 trÃ¹ng) | `reports/tables/split_report.csv` | âœ… cÃ³ commit |
| Dá»¯ liá»‡u train/test Ä‘Ã£ táº¡o (master + tá»«ng má»‘c) | `data/splits/*_train.parquet`, `*_test.parquet` | git bá» qua (tÃ¡i táº¡o Ä‘Æ°á»£c) |

Sinh báº±ng `python -m src.evaluation.make_split --materialise`. Lá»‡nh nÃ y cÃ³ guard: luÃ´n tÃ¡i dÃ¹ng `test_student_ids.csv` Ä‘Ã£ commit, khÃ´ng bao giá» tá»± Ã½ tÃ­nh láº¡i phÃ©p chia (cá» `--rederive` chá»‰ dÃ nh cho quyáº¿t Ä‘á»‹nh cá»§a cáº£ nhÃ³m, vÃ¬ tÃ¡ch láº¡i sáº½ Ä‘á»•i 4.574/5.756 id). á»ž giai Ä‘oáº¡n mÃ´ hÃ¬nh, náº¡p trá»±c tiáº¿p phÃ¢n chia cá»§a má»™t má»‘c:

```python
from src.evaluation.make_split import load_checkpoint_split
X_train, X_test = load_checkpoint_split(40)   # train/test cho má»‘c 40%
```

ÄÃ£ kiá»ƒm chá»©ng: train â‰ˆ 26.104 dÃ²ng Â· test â‰ˆ 6.489 dÃ²ng (5.756 SV) Â· at-risk 0,530 / 0,520 Â· **0 sinh viÃªn trÃ¹ng** â€” Ä‘á»“ng nháº¥t qua cáº£ sÃ¡u má»‘c.

## TÃ¡i táº¡o toÃ n bá»™

```bash
python setup_raw_data.py                 # kiá»ƒm tra 7 CSV gá»‘c + manifest
python -m src.data.time_utils            # data/checkpoint_map.csv
python -m src.data.build_master_table    # master_raw.parquet (+ nháº­t kÃ½ join/lÃ m sáº¡ch)
python -m src.data.make_checkpoints      # sÃ¡u bá»™ dá»¯ liá»‡u theo má»‘c
python -m src.evaluation.make_split --materialise  # phÃ¢n chia train/test cá»‘ Ä‘á»‹nh (+ bÃ¡o cÃ¡o)
python -m src.eda.eda                    # biá»ƒu Ä‘á»“ + báº£ng + eda_findings.json
pytest tests/test_leakage.py             # kiá»ƒm thá»­ rÃ² rá»‰/phÃ¢n chia tá»± Ä‘á»™ng
```

> LÆ°u Ã½: viá»‡c sinh biá»ƒu Ä‘á»“ matplotlib cáº§n mÃ´i trÆ°á»ng cÃ³ font hoáº¡t Ä‘á»™ng (xem `MEMORY`/tÃ i liá»‡u tÃ¡i láº­p). Dá»¯ liá»‡u phÃ¡i sinh `*.parquet` bá»‹ git bá» qua vÃ  Ä‘Æ°á»£c pipeline tÃ¡i táº¡o.

