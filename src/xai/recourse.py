"""
Actionable Recourse using DiCE (Diverse Counterfactual Explanations)
Generates "What-If" scenarios to transition a student from 'at-risk' to 'not-at-risk'.
"""
import joblib
import pandas as pd
import dice_ml
import warnings
import logging
warnings.filterwarnings('ignore')

from src.features.preprocessing import NUMERIC_FEATURES, TARGET_COL, FEATURE_COLUMNS, handle_missing, handle_outliers, transform_test

class EduGuardModelWrapper:
    def __init__(self, bundle):
        self.clf = bundle["model"]
        self.ct = bundle["ct"]
        self.stats = bundle.get("stats", {})
        # Suppress preprocessing logs to prevent spam during DiCE perturbations
        logging.getLogger("src.features.preprocessing").setLevel(logging.WARNING)

    def predict(self, X: pd.DataFrame):
        proba = self.predict_proba(X)
        return (proba[:, 1] >= 0.5).astype(int)

    def predict_proba(self, X: pd.DataFrame):
        # Force numeric types to fix DiCE producing object arrays
        for c in NUMERIC_FEATURES:
            if c in X.columns:
                X[c] = pd.to_numeric(X[c], errors="coerce")
        X_p = handle_missing(X.copy(), stats=dict(self.stats.get("missing", {})))
        X_p = handle_outliers(X_p, stats=dict(self.stats.get("outlier", {})))
        Xt = transform_test(self.ct, X_p)
        return self.clf.predict_proba(Xt)

def get_actionable_features():
    """Returns the list of features that a student can reasonably change mid-course."""
    return [
        "total_clicks",
        "n_days_active",
        "days_since_last_activity",
        "mean_score_to_date",
        "weighted_score_to_date",
        "max_clicks_single_day",
        "mean_clicks_per_active_day",
        "clicks_oucontent",
        "clicks_forumng",
        "clicks_quiz"
    ]

def configure_dice(dataset_path: str, model_path: str):
    """
    Load data and model, and initialize the DiCE Explainer.
    The Pipeline must accept raw data features and return predictions.
    """
    df = pd.read_parquet(dataset_path)
    
    # DiCE needs to know which features are continuous
    # Exclude non-features from df just in case
    d = dice_ml.Data(
        dataframe=df[FEATURE_COLUMNS + [TARGET_COL]], 
        continuous_features=NUMERIC_FEATURES, 
        outcome_name=TARGET_COL
    )
    
    # Load the custom bundle and wrap into a scikit-learn compatible object
    bundle = joblib.load(model_path)
    wrapper = EduGuardModelWrapper(bundle)
    m = dice_ml.Model(model=wrapper, backend="sklearn")
    
    # Random method works efficiently for scikit-learn models as a baseline
    exp = dice_ml.Dice(d, m, method="random") 
    
    return exp

def generate_student_recourse(exp, student_df: pd.DataFrame, num_cfs: int = 3, safe_medians: dict = None):
    """
    Generate counterfactual rules for a specific student dataframe 
    (must be formatted exactly like the training input features).
    """
    actionable_features = get_actionable_features()
    
    # Calculate permitted range based on current values
    # Monotonicity constraints: clicks shouldn't decrease, inactivity shouldn't increase.
    permitted_range = {}
    for col in actionable_features:
        if col not in student_df.columns:
            continue
        val = float(student_df.iloc[0][col])
        if col in ["days_since_last_activity", "not_submitted"]:
            permitted_range[col] = [0.0, max(0.0, val)]
        else:
            # allow growth up to a realistic multiplier of the "safe" median
            if safe_medians and col in safe_medians:
                med = float(safe_medians[col])
                if col.endswith("score_to_date"):
                    upper = min(100.0, max(val + 20.0, med * 1.5))
                elif col == "n_days_active":
                    upper = max(val + 14.0, med * 2.0)
                elif col == "total_clicks":
                    upper = max(val + 200.0, med * 3.0)
                elif "clicks_" in col:
                    upper = max(val + 50.0, med * 3.0)
                else:
                    upper = max(val + 50.0, med * 2.0)
            else:
                # fixed fallback if safe_medians not provided
                if col.endswith("score_to_date"):
                    upper = 100.0
                elif col == "n_days_active":
                    upper = val + 40.0
                elif col == "total_clicks":
                    upper = val + 1500.0
                elif "clicks_" in col:
                    upper = val + 300.0
                else:
                    upper = val + 100.0
            
            permitted_range[col] = [val, upper]

    try:
        # desired_class=0 means 'not-at-risk'
        dice_exp = exp.generate_counterfactuals(
            student_df, 
            total_CFs=num_cfs, 
            desired_class=0,
            features_to_vary=actionable_features,
            permitted_range=permitted_range
        )
        return dice_exp
    except Exception as e:
        print(f"Error generating CE: {e}")
        return None

if __name__ == "__main__":
    # Test script locally
    # Paths will assume executing from project root
    import os
    if os.path.exists("models/xgb_t100.joblib") and os.path.exists("data/checkpoints/dataset_t100.parquet"):
        print("Testing DiCE on a single sample at t=100...")
        exp = configure_dice(
            dataset_path="data/checkpoints/dataset_t100.parquet",
            model_path="models/xgb_t100.joblib"
        )
        df_test = pd.read_parquet("data/checkpoints/dataset_t100.parquet").head(10)
        # Select first at-risk student
        at_risk = df_test[df_test["at_risk"] == 1].head(1)
        if not at_risk.empty:
            print("Found an at-risk student, generating counterfactuals...")
            cfs = generate_student_recourse(exp, at_risk[FEATURE_COLUMNS])
            if cfs:
                cfs.visualize_as_dataframe(show_only_changes=True)
