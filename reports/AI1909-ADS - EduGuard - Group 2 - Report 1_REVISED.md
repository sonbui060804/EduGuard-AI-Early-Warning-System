# EduGuard: AI-Powered Early Warning and Actionable Recourse System for Students

**AI1909 - ADS | Group 2**  
**Report 1: Weeks 1-2 Research and Implementation Plan**

> **Status of this report:** This is a research and implementation plan. The statements below describe planned analyses unless they are explicitly identified as project findings.

## Abstract

Virtual Learning Environments (VLEs) record activities such as opening learning materials, visiting forums, submitting assessments, and participating in course activities. These records are used in Educational Data Mining and Learning Analytics to study student performance and withdrawal. Because student engagement may decrease gradually, early information may help instructors offer support while intervention is still possible.

The Open University Learning Analytics Dataset (OULAD) is suitable for this project because it contains anonymised student information, registration records, VLE activity, assessment records, and course information. EduGuard will study whether a model can identify at-risk students at different points in a course. The project distinguishes between predicting the final outcome and identifying students who are still eligible for support at the time of prediction.

## 1. Motivation and Problem Statement

Instructors need timely information about which students may need help. This information is useful only if it is available while there is still time to respond. The model must therefore be evaluated carefully. A model evaluated on students who have already withdrawn may be useful for final-outcome prediction, but that evaluation does not answer the operational question of identifying students who are still enrolled and can receive support.

Accuracy alone is also insufficient. A risk score does not explain whether a student was flagged because of inactivity, missing work, low assessment scores, or another factor. Without such information, an instructor may not know what type of support is appropriate. EduGuard will therefore assess explanation stability, because explanations that change substantially across retraining runs or modelling choices may be difficult to trust.

The project will develop a binary, time-aware early-warning system using only information available up to each checkpoint. The pipeline will address temporal leakage and student-level leakage. It will report results for both the full evaluation cohort and the active-at-checkpoint cohort. It will also investigate whether model explanations can be connected to possible support recommendations.

## 2. Related Work and Research Gap

### 2.1 At-Risk Prediction and Time-Aware Modelling

Kuzilek, Hlosta, and Zdrahal introduced OULAD, which contains seven related tables and 32,593 student-module-presentation registrations across 22 module presentations [1]. The data include demographic information, VLE activity, assessment records, and course information. The released data are anonymised.

Tomasevic et al. compared supervised learning methods for exam-performance prediction on an OULAD subset. Their study used two DDD presentations and 3,166 students after excluding students without an exam result [3]. Their results suggested that combining VLE activity with assessment scores can be useful. The comparison did not include the complete set of gradient-boosted models planned here.

Adnan et al. studied prediction at several percentages of course length using cumulative features at 0%, 20%, 40%, 60%, 80%, and 100% [2]. Their evaluation used accuracy, precision, recall, F-score, and AUC. Their findings motivate the use of time-aware checkpoints in this project, which additionally includes a 10% checkpoint. They combined Pass with Distinction and Fail with Withdrawn rather than treating the four final outcomes as separate classes.

A key methodological requirement for EduGuard is to split data by student identifier. A registration may contain repeated observations or multiple presentations, so a row-level random split could allow information from the same student to appear in both training and test data. The project will use a frozen student-level split and will document the split procedure explicitly.

### 2.2 Explainable AI for Educational Prediction

SHAP and LIME are commonly used to explain machine-learning predictions [4], [5]. SHAP can describe global feature contributions and individual predictions. LIME explains one prediction by fitting a simple local model around that case. Their outputs can depend on sampling, model fitting, and the selected data slice.

Previous educational studies have often assessed explanations using feature-importance plots or qualitative discussion [4], [5]. EduGuard will supplement visual inspection with numerical stability measures. The analysis will ask whether important features remain similar when the model is retrained, when the checkpoint changes, or when the imbalance-handling strategy changes.

### 2.3 Class-Imbalance Handling

SMOTE creates synthetic minority-class observations from existing observations. ADASYN creates more observations in regions that are harder to classify. Class weighting changes the relative penalty of errors without adding synthetic rows.

Under the project label mapping, `at_risk = 1` represents Fail or Withdrawn and `at_risk = 0` represents Pass or Distinction. In the current OULAD preparation, at-risk registrations account for 17,208 of 32,593 registrations, or approximately 52.8%. Therefore, at-risk is a slight majority rather than a rare minority. The comparison of SMOTE, ADASYN, and class weighting is consequently a robustness experiment, not a claim that a severely under-represented at-risk class must be recovered.

Because missing an at-risk student is operationally important, recall for the at-risk class and PR-AUC will be reported alongside precision, F1, ROC-AUC, calibration, and confusion matrices. Any resampling must be applied only inside the training folds and never to validation or test data.

### 2.4 Research Gap

The group screened 30 readings and retained 27 independent papers after removing duplicates. The report below summarises the most relevant evidence. The complete screening list, inclusion criteria, and paper-to-claim mapping should be included in the final literature-review appendix.

| Research area | Evidence reviewed | Limitation identified | EduGuard response |
|---|---|---|---|
| OULAD outcome prediction | Kuzilek et al. [1]; Tomasevic et al. [3] | Different feature sets and model comparisons make direct comparison difficult | Use a reproducible feature pipeline and a common evaluation protocol |
| Time-aware prediction | Adnan et al. [2] | Prediction quality changes with course progress; active-student performance may differ from full-cohort performance | Evaluate checkpoints from 10% to 100% and report two cohorts |
| Explainable AI in education | Gunasekara and Saarela [4]; Alamri and Alharbi [5] | Explanation quality is often assessed mainly through plots or qualitative discussion | Measure ranking agreement and variation across seeds, checkpoints, and imbalance strategies |
| Class-imbalance handling | SMOTE, ADASYN, and class-weighting literature | Effects on explanation stability are not consistently measured | Compare no resampling, class weighting, SMOTE, and ADASYN |
| Counterfactual explanations | Wachter et al. [6]; Mothilal et al. [7] and education-focused work identified in the review | A mathematically valid counterfactual may be pedagogically infeasible | Constrain future recourse by actionability, immutability, feasibility, and cost |

The project will combine time-aware prediction and XAI on OULAD, compare neural and ensemble models, and measure explanation stability. It will also investigate whether imbalance-handling choices affect both predictive metrics and explanations. Counterfactual recourse is a planned extension and will not be presented as a completed contribution until its constraints and evaluation have been implemented.

## 3. Objective of the Project

### 3.1 General Objective

The general objective is to design and evaluate a time-aware early-warning framework for identifying students who may fail or withdraw from an online course. At the Weeks 1-2 stage, this objective is a research and implementation plan; results will be added after the experiments are completed.

### 3.2 Specific Objectives

1. Define the data requirements and unit of analysis for the OULAD study.
2. Combine the seven OULAD tables in a reproducible data pipeline.
3. Create demographic, engagement, registration, and assessment features at multiple course-progress checkpoints.
4. Compare five supervised-learning model families under the same student-level evaluation process: Logistic Regression, Random Forest, XGBoost, LightGBM, and an artificial neural network implemented as an MLP classifier.
5. Identify the earliest checkpoint at which the predefined reliability criterion is met.
6. Test SHAP and LIME and define numerical measures for explanation stability.
7. Compare no resampling, class weighting, SMOTE, and ADASYN, with resampling restricted to training folds.
8. Report results separately for all eligible registrations and for students active at the checkpoint.
9. Design and later test counterfactual recourse for possible educational support.

### 3.3 Research Questions

**RQ1.** At course-progress checkpoints of 10%, 20%, 40%, 60%, 80%, and 100%, which algorithm gives the best at-risk prediction on OULAD, and at which checkpoint does it first meet the predefined reliability criterion?

**RQ2.** How consistent are SHAP and LIME explanations for the same model, and how does explanation stability change across checkpoints and imbalance-handling strategies?

**RQ3.** How does imbalance handling, including SMOTE, ADASYN, and class weighting, affect predictive performance and explanation stability?

**RQ4.** Can constrained counterfactual explanations generate minimal and feasible support plans for at-risk students, and how does the required recourse effort vary across course-progress checkpoints?

RQ4 is a planned research direction at this stage. It must not be presented as a completed result until the recourse module, actionability constraints, validity tests, and evaluation have been completed.

### 3.4. Operational Definitions

- **Registration:** one student-module-presentation record, which is the primary unit of analysis.
- **Checkpoint:** a percentage of the relevant course length. Only features available on or before that point may be used.
- **Full cohort:** all registrations eligible for evaluation at the given checkpoint, including registrations whose final outcome is later observed.
- **Active-at-checkpoint cohort:** registrations for students who have not withdrawn before the checkpoint, according to the project’s documented activity and outcome rules. The final implementation must state the exact rule and apply it without using post-checkpoint information.
- **Reliable checkpoint:** the earliest checkpoint satisfying a criterion fixed before final test evaluation. The criterion should specify the target metric, minimum threshold, and uncertainty rule, for example recall at or above a project-defined threshold with a bootstrap confidence interval that does not fall below that threshold.
- **Actionable feature:** a feature that an instructor or student could plausibly influence during the intervention period. Immutable attributes such as age and gender will not be changed by recourse generation.

## 4. Structure of the Thesis

The final report will be organised into six main sections:

1. **Introduction and literature review:** educational motivation, research questions, and planned contributions.
2. **Related work:** OULAD prediction, time-aware learning analytics, XAI, class imbalance, and actionable recourse.
3. **Data and methodology:** OULAD, target definition, feature creation, checkpoints, leakage prevention, student-level splitting, cross-validation, and preprocessing.
4. **Model comparison and time-aware prediction:** model results for RQ1, reliability analysis, and comparison of the two evaluation cohorts.
5. **Imbalance and explanation stability:** effects of imbalance strategies and SHAP/LIME stability for RQ2 and RQ3.
6. **Discussion and conclusion:** limitations, findings, deployment considerations, monitoring recommendations, and future work, including evaluation on other institutions and constrained counterfactual recourse.

## References

[1] J. Kuzilek, M. Hlosta, and Z. Zdrahal, “Open University Learning Analytics Dataset,” *Scientific Data*, 2017.

[2] M. Adnan et al., “Predicting at-Risk Students at Different Percentages of Course Length for Early Intervention Using Machine Learning Models,” *IEEE Access*, vol. 9, pp. 7519-7539, 2021.

[3] N. Tomasevic, N. Gvozdenovic, and S. Vranes, “An Overview and Comparison of Supervised Data Mining Techniques for Student Exam Performance Prediction,” *Computers & Education*, vol. 143, art. 103676, 2020.

[4] S. Gunasekara and M. Saarela, “Explainable AI in Education: Techniques and Qualitative Assessment,” *Applied Sciences*, vol. 15, no. 3, art. 1239, 2025.

[5] A. Alamri and A. Alharbi, “Explainable Student Performance Prediction: A Systematic Review,” *IEEE Access*, 2021.

[6] S. Wachter, B. Mittelstadt, and C. Russell, “Counterfactual Explanations without Opening the Black Box: Automated Decisions and the GDPR,” *Harvard Journal of Law & Technology*, vol. 31, no. 2, pp. 841-887, 2018.

[7] R. K. Mothilal, A. Sharma, and C. Tan, “Explaining Machine Learning Classifiers through Diverse Counterfactual Explanations,” in *Proceedings of the ACM Conference on Fairness, Accountability, and Transparency*, 2020, pp. 607-617.

> **Reference completion note:** The final submission must add complete bibliographic entries for the education-specific counterfactual, dropout/survival-analysis, and temporal clickstream papers used in the 27-paper review. A topic description is not a valid reference. Each entry should include authors, title, venue, year, volume/pages or article number, and DOI or stable URL where available.

## Evaluation of the Revision

### Changes made

- Converted the report into a reproducible Markdown version while leaving the original DOCX unchanged.
- Added an explicit report status so planned work is not confused with completed results.
- Replaced the research-gap image with a searchable Markdown table.
- Defined the registration unit, checkpoint, full cohort, active-at-checkpoint cohort, reliability criterion, and actionable feature.
- Listed the five planned model families explicitly.
- Clarified that at-risk is a slight majority under the current label mapping and that resampling is a robustness experiment.
- Added the requirement that resampling occur only inside training folds.
- Replaced absolute wording such as “never studied” with evidence-bounded wording.
- Removed vague placeholder references from the numbered bibliography and marked the remaining bibliography work explicitly.
- Added an honest limitation: the claim of 30 readings and 27 independent papers still requires a screening table or appendix for verification.

### Assessment after revision

**Improved:** The report is now clearer, more auditable, and less likely to overclaim. The research questions are connected to measurable procedures, and the distinction between prediction of final outcome and intervention for active students is explicit.

**Still required before submission:**

1. Complete the full 27-paper bibliography and provide a screening/mapping appendix.
2. Verify every bibliographic detail, especially publication year, authorship, title, DOI, and page or article numbers.
3. Fix the active-at-checkpoint cohort rule in the methodology and ensure it does not use post-checkpoint information.
4. Pre-register the reliability threshold, target metric, confidence-interval method, and model-selection rule.
5. Add the final citations for education-specific counterfactual and temporal-prediction studies instead of leaving them as topic descriptions.

**Overall assessment:** Suitable as a revised Weeks 1-2 research-plan draft. Not yet ready as a final literature review until the reference and evidence-traceability items above are completed.
