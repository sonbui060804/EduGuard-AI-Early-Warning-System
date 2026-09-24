"""
Actionable Recourse using DiCE (Diverse Counterfactual Explanations)
Generates "What-If" scenarios to transition a student from 'at-risk' to 'not-at-risk'.
"""
import joblib
import pandas as pd
import dice_ml
import warnings
warnings.filterwarnings('ignore')

from src.features.preprocessing import NUMERIC_FEATURES, TARGET_COL, FEATURE_COLUMNS

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
    
    # Load the Scikit-Learn Pipeline (Preprocessor + XGBoost/LightGBM)
    pipeline = joblib.load(model_path)
    m = dice_ml.Model(model=pipeline, backend="sklearn")
    
    # Random method works efficiently for scikit-learn models as a baseline
    exp = dice_ml.Dice(d, m, method="random") 
    
    return exp

def generate_student_recourse(exp, student_df: pd.DataFrame, num_cfs: int = 3):
    """
    Generate counterfactual rules for a specific student dataframe 
    (must be formatted exactly like the training input features).
    """
    actionable_features = get_actionable_features()
    
    try:
        # desired_class=0 means 'not-at-risk'
        dice_exp = exp.generate_counterfactuals(
            student_df, 
            total_CFs=num_cfs, 
            desired_class=0,
            features_to_vary=actionable_features,
            # we can add permitted_range to ensure monotonicity (e.g. total_clicks can't decrease) 
            # but for demo, standard limits are fine.
        )
        return dice_exp
    except Exception as e:
        print(f"Error generating CE: {e}")
        return None

if __name__ == "__main__":
    # Test script locally
    # Paths will assume executing from project root
    import os
    if os.path.exists("models/xgb_t100.joblib") and os.path.exists("data/splits/dataset_t100.parquet"):
        print("Testing DiCE on a single sample at t=100...")
        exp = configure_dice(
            dataset_path="data/splits/dataset_t100.parquet",
            model_path="models/xgb_t100.joblib"
        )
        df_test = pd.read_parquet("data/splits/dataset_t100.parquet").head(10)
        # Select first at-risk student
        at_risk = df_test[df_test["at_risk"] == 1].head(1)
        if not at_risk.empty:
            print("Found an at-risk student, generating counterfactuals...")
            cfs = generate_student_recourse(exp, at_risk[FEATURE_COLUMNS])
            if cfs:
                cfs.visualize_as_dataframe(show_only_changes=True)
