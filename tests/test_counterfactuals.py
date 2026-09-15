import pytest
import pandas as pd
from src.xai.counterfactuals import get_safe_medians, generate_counterfactual_plan, ACTIONABLE_FEATURES

def test_generate_counterfactual_plan():
    # Mock data
    X_train = pd.DataFrame({
        "total_clicks": [100, 200, 10, 5],
        "days_since_last_activity": [1, 0, 10, 20],
        "n_assessments_submitted": [3, 4, 0, 1]
    })
    y_train = pd.Series([0, 0, 1, 1])
    
    # Fill missing actionable columns to prevent KeyError
    for f in ACTIONABLE_FEATURES:
        if f not in X_train.columns:
            X_train[f] = 0
            
    medians = get_safe_medians(X_train, y_train)
    
    student = pd.Series({
        "total_clicks": 5,
        "days_since_last_activity": 20,
        "n_assessments_submitted": 0
    })
    
    # Test plan generation
    plan = generate_counterfactual_plan(
        student, 
        medians, 
        feats_up=["total_clicks", "n_assessments_submitted"],
        feats_down=["days_since_last_activity"]
    )
    
    assert "total_clicks" in plan
    assert plan["total_clicks"]["target"] == 150.0  # Median of 100 and 200
    assert plan["days_since_last_activity"]["target"] == 0.5 # Median of 1 and 0
    assert plan["total_clicks"]["direction"] == "tăng"
    assert plan["days_since_last_activity"]["direction"] == "giảm"
