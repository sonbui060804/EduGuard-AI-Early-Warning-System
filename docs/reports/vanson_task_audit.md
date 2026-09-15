# Audit pháº§n nhiá»‡m vá»¥ cá»§a Ngá»c Sang trong repo

NgÃ y kiá»ƒm tra: 2026-06-14

## Káº¿t luáº­n nhanh

Trong zip, file `src/features/preprocessing.py` Ä‘Ã£ gom pháº§n code cho Ngá»c Sang tá»« Task 16 Ä‘áº¿n Task 20 vÃ  Task 22. RiÃªng STT20 Ä‘Ã£ cÃ³ code vÃ  Ä‘Ã£ Ä‘Æ°á»£c smoke test thÃ nh cÃ´ng. Repo trÆ°á»›c khi bá»• sung chÆ°a cÃ³ thÆ° má»¥c `reports`, vÃ¬ váº­y pháº§n bÃ¡o cÃ¡o chÆ°Æ¡ng cho STT20 Ä‘Æ°á»£c bá»• sung táº¡i `reports/data_tasks/stt20_scaling_report.md`.

## Tráº¡ng thÃ¡i tá»«ng task

| STT | Ná»™i dung | Tráº¡ng thÃ¡i trong zip | Báº±ng chá»©ng |
| --- | --- | --- | --- |
| 16 | PhÃ¢n loáº¡i kiá»ƒu biáº¿n | ÄÃ£ cÃ³ | `NUMERIC_FEATURES`, `ORDINAL_FEATURES`, `NOMINAL_FEATURES`, `BINARY_FEATURES`, `ORDINAL_ORDERS` trong `preprocessing.py`; output trÆ°á»›c Ä‘Ã³ cÃ³ `variable_typing.xlsx`. |
| 17 | Xá»­ lÃ½ giÃ¡ trá»‹ khuyáº¿t | ÄÃ£ cÃ³ | `log_missing()` vÃ  `handle_missing()`, cÃ³ log vÃ  assert khÃ´ng cÃ²n missing. |
| 18 | Xá»­ lÃ½ ngoáº¡i lai | ÄÃ£ cÃ³ | `OUTLIER_STRATEGY`, `log_outliers()`, `handle_outliers()`, khÃ´ng xoÃ¡ báº£n ghi tuá»³ tiá»‡n. |
| 19 | MÃ£ hoÃ¡ biáº¿n phÃ¢n loáº¡i | ÄÃ£ cÃ³ | `BinaryEncoder`, `build_ordinal_encoder()`, `build_onehot_encoder()`, `ColumnTransformer`. |
| 20 | Chuáº©n hoÃ¡ thang Ä‘o | ÄÃ£ cÃ³ vÃ  Ä‘Ã£ kiá»ƒm thá»­ | `build_scaler()`, nhÃ¡nh `num` trong `ColumnTransformer`, `fit_transform_train()`, `transform_test()`, smoke test Ä‘áº¡t. |
| 21 | PhÃ¢n tÃ­ch chiáº¿n lÆ°á»£c phÃ¢n chia dá»¯ liá»‡u | ChÆ°a tháº¥y trong `preprocessing.py` | Task nÃ y thÆ°á»ng thuá»™c `split_harness.py`/bÃ¡o cÃ¡o phÃ¢n chia; khÃ´ng náº±m trong module preprocessing cá»§a zip. |
| 22 | TrÃ¬nh tá»± pipeline anti-leakage | ÄÃ£ cÃ³ | `preprocess()` ghi rÃµ missing -> outlier -> fit train -> transform test; note resampling chá»‰ trÃªn train. |

## Káº¿t quáº£ smoke test STT20

Lá»‡nh Ä‘Ã£ cháº¡y:

```powershell
$env:PYTHONIOENCODING='utf-8'
.\.venv\Scripts\python.exe .\src\features\preprocessing.py
```

Káº¿t quáº£:

- `X_train_proc shape`: `(200, 38)`
- `X_test_proc shape`: `(50, 38)`
- `n_features`: `38`
- KhÃ´ng cÃ²n NaN sau transform.
- `scaler.mean_[:4] = [2.045, 330.935, -9.63, 7.5868]`, chá»‰ tÃ­nh tá»« X_train.
- Module in káº¿t luáº­n: táº¥t cáº£ kiá»ƒm tra Ä‘áº¡t.

## Viá»‡c Ä‘Ã£ bá»• sung trong láº§n nÃ y

- Táº¡o `reports/data_tasks/stt20_scaling_report.md`: pháº§n bÃ¡o cÃ¡o chÆ°Æ¡ng cho STT20.
- Táº¡o `reports/data_tasks/vanson_task_audit.md`: audit tráº¡ng thÃ¡i cÃ¡c task cá»§a Ngá»c Sang trong zip.

## Viá»‡c cÃ²n thiáº¿u náº¿u muá»‘n hoÃ n táº¥t toÃ n bá»™ pháº§n Ngá»c Sang

- STT21 cáº§n má»™t file riÃªng vá» chiáº¿n lÆ°á»£c phÃ¢n chia dá»¯ liá»‡u náº¿u giÃ¡o viÃªn yÃªu cáº§u Ngá»c Sang phá»¥ trÃ¡ch má»¥c nÃ y. Hiá»‡n zip chÆ°a cÃ³ artifact rÃµ rÃ ng cho STT21 trong `src/features/preprocessing.py`.

