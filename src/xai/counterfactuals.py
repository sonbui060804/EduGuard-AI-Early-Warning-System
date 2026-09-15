"""
Phase 3: Actionable Recourse via Diverse Counterfactuals
Author: Nhom 5 (EduGuard)
"""
import pandas as pd
import numpy as np

ACTIONABLE_FEATURES = {
    "total_clicks": "tăng",
    "n_days_active": "tăng",
    "mean_clicks_per_active_day": "tăng",
    "clicks_forumng": "tăng",
    "clicks_oucontent": "tăng",
    "clicks_resource": "tăng",
    "n_assessments_submitted": "tăng",
    "weighted_score_to_date": "tăng",
    "not_submitted": "giảm",
    "days_since_last_activity": "giảm",
}

def get_safe_medians(X_train, y_train):
    """
    Returns the median of the safe (y=0) cohort for the actionable features.
    """
    safe_students = X_train[y_train == 0]
    return safe_students[list(ACTIONABLE_FEATURES.keys())].median()

def generate_counterfactual_plan(student_profile, safe_medians, feats_up, feats_down, factor_up=1.0, factor_down=0.5):
    """
    Generates a targeted counterfactual plan for an at-risk student.
    """
    plan = {}
    for feat in feats_up:
        current_val = student_profile.get(feat, 0)
        target_val = float(safe_medians.get(feat, current_val * 1.5 * factor_up))
        if target_val > current_val:
            plan[feat] = {"current": current_val, "target": target_val, "direction": "tăng"}
            
    for feat in feats_down:
        current_val = student_profile.get(feat, 0)
        target_val = max(0.0, float(safe_medians.get(feat, current_val * factor_down)))
        if target_val < current_val:
            plan[feat] = {"current": current_val, "target": target_val, "direction": "giảm"}
            
    return plan
