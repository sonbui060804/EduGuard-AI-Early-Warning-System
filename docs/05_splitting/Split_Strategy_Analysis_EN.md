# Data Splitting Strategy: Analysis and Selection

*Comparing splitting strategies and justifying the design for time-aware, imbalanced, grouped data*

**DSP391m â€“ Group 5 Â· Report 2 (Data Tasks), Chapter 3 Â· Work item STT 21 (vanson)**

---

## 1. Why the split needs care here

Three properties of the data constrain the split:

- **Grouped** â€” a student (`id_student`) can appear in several module-presentations, so rows are not independent. A naive row split can place the same student in train and test (*group leakage*).
- **Imbalanced (mildly)** â€” the at-risk class is ~52.8%; a random split can still drift the test-set ratio and bias evaluation.
- **Time-aware** â€” six checkpoints share one comparison axis (RQ1), so the test set must be **identical** across checkpoints or the performance curve is not comparable.

## 2. Strategies compared

| Strategy | How it works | Pros | Cons |
|---|---|---|---|
| Single hold-out | One train/test cut | Simple, fast | High variance; depends on one partition |
| k-fold CV | k rotating validation folds | Uses all data; lower variance | kÃ— cost; single seed still partition-dependent |
| Repeated k-fold | k-fold repeated over several seeds | Robust mean Â± std; seed-independent | Highest cost |
| Nested CV | Inner CV for tuning, outer for estimate | Unbiased estimate with tuning | Very expensive; complex |

## 3. Selected design (per the proposal)

**Hold-out 20% test set + 5-fold cross-validation repeated over 5 seeds on the training set.**

- The **20% test set is fixed once**, by `id_student`, and reused at every checkpoint (STT 8) so the six points are comparable.
- On the remaining 80%, **5-fold Ã— 5-seed** CV revansones variance from any single partition; metrics are reported as **mean Â± standard deviation** across the 25 fits.
- Both the test split and the CV folds are **group-aware (by `id_student`) and stratified (by `at_risk`)** via `StratifiedGroupKFold` (see `src/evaluation/split_harness.py`).

This balances robustness and cost: repeated k-fold gives stable estimates, while a single fixed hold-out test set preserves comparability across checkpoints. Nested CV was judged unnecessarily expensive for the planned scope.

## 4. Reporting convention

Because the positive (at-risk) class is the one we must not miss, headline metrics are **PR-AUC** and **recall on the at-risk class**, reported as **mean Â± std** over folds/seeds. Accuracy is reported only as a secondary figure (it is misleading under any imbalance).

## 5. Verified properties (this dataset)

Using the fixed 20% split on `master_raw` (32,593 rows): **0 students overlap** between train and test, and the at-risk rate is preserved (train â‰ˆ 0.53, test â‰ˆ 0.52, gap â‰¤ 0.02). These checks are asserted in `tests/test_leakage.py`.

## 6. Materialised split and where the data lives

The split is defined **once** and persisted by `src/evaluation/make_split.py`:

| Artifact | Location | Committed? |
|---|---|---|
| Canonical test `id_student` list (5,756 students) | `data/splits/test_student_ids.csv` | yes |
| Verification report (per dataset) | `reports/tables/split_report.csv` | yes |
| Materialised train/test data (master + per checkpoint) | `data/splits/*_train.parquet`, `*_test.parquet` | git-ignored, regenerable |

The split report confirms the design across `master_raw` and **all six checkpoints**: train **26,104** rows Â· test **6,489** rows (5,756 students) Â· at-risk **0.530 / 0.520** Â· **0 overlap** â€” identical at every checkpoint. The modelling phase loads a checkpoint's split with one call:

```python
from src.evaluation.make_split import load_checkpoint_split
X_train, X_test = load_checkpoint_split(40)   # train/test at the 40% checkpoint
```

## References

1. M. Adnan et al., *IEEE Access*, vol. 9, pp. 7519â€“7539, 2021.
2. N. Tomasevic, N. Gvozdenovic, S. Vranes, *Computers & Evansonation*, vol. 143, art. 103676, 2020.

