# EduGuard: AI-Powered Early Warning and Actionable Recourse System for Students

## Revised Report 1 Draft - Weeks 1-2

> **Status note.** This document is a Weeks 1-2 project draft. It records the problem definition, literature review, research gap, objectives, scope, data requirements, and proposed methodology. Any model metrics, explanation-stability values, fairness results, deployment claims, and recourse results remain subject to later experimental validation.

## Abstract

Online learning platforms generate detailed records of student engagement, assessment activity, and course participation. These records create an opportunity for early identification of students who may fail or withdraw, but a useful early-warning system must do more than produce a high prediction score. It must use only information available at the prediction time, distinguish students who remain reachable from students who have already withdrawn, provide explanations that instructors can understand, and support feasible educational action.

This project proposes EduGuard, a time-aware and interpretable early-warning framework based on the Open University Learning Analytics Dataset (OULAD). The planned study will use demographic, VLE-engagement, registration, and assessment data at six course-progress checkpoints: 10%, 20%, 40%, 60%, 80%, and 100%. Logistic Regression, Random Forest, XGBoost, LightGBM, and an artificial neural network will be compared under a student-level, leakage-safe evaluation design. SHAP and LIME will be investigated for post-hoc explanation, while explanation stability and imbalance-handling strategies will be evaluated as research questions rather than assumed results. Counterfactual actionable recourse is defined as a planned extension and will only be claimed as a contribution after implementation and validation.

## 1. Introduction and Background

Virtual Learning Environments (VLEs) record student activity such as accessing learning materials, visiting forums, submitting assessments, and participating in course activities. Educational Data Mining and Learning Analytics use these traces to study student performance, failure, and withdrawal. However, students may disengage gradually without receiving support until the outcome is difficult to change.

OULAD provides a suitable research setting because it contains anonymised student information, registration records, VLE clickstream data, assessment records, and course metadata. The project will use the dataset to investigate whether an early-warning model can identify at-risk students at multiple points in a course while maintaining an honest distinction between outcome classification and intervention-oriented prediction.

## 2. Motivation and Problem Statement

The motivation for EduGuard is both educational and methodological. Instructors need timely information about which students may require attention while there is still an opportunity to respond. At the same time, the evidence supporting an alert must be evaluated carefully. A model evaluated on every historical enrolment may receive an easier task when some students have already withdrawn by the prediction point. Such performance may be relevant to final-outcome classification, but it should not automatically be interpreted as successful forecasting for students who are still enrolled.

Predictive accuracy alone is also insufficient. A black-box risk score does not explain whether a student was flagged because of inactivity, non-submission, weak assessment performance, or another factor. Without an explanation, an instructor may not know which support action is appropriate. Explanations should also be checked for stability because a feature ranking that changes substantially across runs may be difficult to trust.

The project therefore defines the problem as follows: develop a binary, time-aware early-warning system using only information available up to each course-progress checkpoint. The system should prevent temporal and student-level leakage, compare performance on both the full and still-enrolled populations, produce interpretable explanations, and investigate whether explanations can be translated into feasible support recommendations.

## 3. Objectives and Scope of the Project

### 3.1 General Objective

The general objective is to design and evaluate a time-aware, interpretable early-warning framework for identifying students at risk of failing or withdrawing from an online course. At Weeks 1-2, this objective is expressed as a research and implementation plan; empirical claims will be added after the relevant experiments are completed.

### 3.2 Specific Objectives

1. Specify the data requirements and analytical grain for the OULAD-based study.
2. Integrate the seven OULAD relational tables into a reproducible analytical pipeline.
3. Define demographic, engagement, registration, and assessment features that can be computed at multiple course-progress checkpoints.
4. Compare five supervised-learning model families under a common student-level evaluation protocol.
5. Determine the earliest checkpoint at which predictions meet a pre-defined reliability criterion.
6. Evaluate SHAP and LIME explanations and define quantitative explanation-stability measures.
7. Compare no resampling, class weighting, SMOTE, and ADASYN as controlled robustness conditions.
8. Separate full-cohort outcome classification from still-enrolled intervention-oriented evaluation.
9. Design, and later validate, constrained counterfactual recourse for actionable educational support.

### 3.3 Research Questions

- **RQ1:** At which course-progress checkpoint can at-risk prediction be considered sufficiently reliable, and which candidate algorithm performs best under the common evaluation protocol?
- **RQ2:** How consistent are SHAP and LIME explanations across random seeds, checkpoints, and model-training conditions?
- **RQ3:** How do class weighting, SMOTE, and ADASYN affect predictive metrics and explanation stability when the at-risk class is only mildly imbalanced?
- **RQ4:** As a planned extension, can constrained counterfactual explanations produce feasible intervention suggestions for students who remain enrolled?

RQ4 is a planned research direction at the current stage. It must not be presented as a completed result until the recourse module, constraints, tests, and evaluation have been completed.

### 3.4 Expected Contribution

The expected contribution is an integrated research framework connecting time-aware prediction, explainability, population-aware evaluation, and potential intervention support. The project will seek to provide a reproducible comparison of models and data-processing decisions rather than claiming universal predictive performance.

### 3.5 Methodological Contribution

The proposed methodological contribution is a leakage-safe experimental design. It will use cutoff-based feature construction, a frozen split at the student level, train-only preprocessing, identical test students across checkpoints, and explicit reporting of the evaluation population. The study will also define quantitative comparison procedures for explanation stability and class-imbalance strategies.

### 3.6 Market-Specific Contribution

The intended application context is online and blended higher education, where institutions already collect learning-management-system traces but may lack an interpretable early-warning workflow. EduGuard is designed as a transferable research pattern for this context. Transferability to other institutions, platforms, or countries remains a hypothesis and requires external validation.

### 3.7 Practical Contribution

The planned practical output is an evidence-based prototype workflow for instructors and academic-support staff. It may later include checkpoint-specific risk scores, explanations, and constrained support suggestions. At this stage, the project does not claim that the system can make autonomous student decisions or that its recommendations have already improved educational outcomes.

### 3.8 Scope

**Included:**

- OULAD's seven relational tables and their documented relationships;
- one student-module-presentation enrolment as the analytical unit;
- the binary target `at_risk`, with Fail and Withdrawn grouped as at-risk;
- six proposed checkpoints: 10%, 20%, 40%, 60%, 80%, and 100%;
- demographic, VLE-engagement, registration, and assessment features;
- five candidate supervised-learning algorithms;
- group-aware splitting, train-only preprocessing, SHAP/LIME analysis, and imbalance comparison;
- a planned counterfactual-recourse extension.

**Excluded or deferred:**

- automatic decisions about students;
- fully autonomous intervention;
- causal claims about whether an intervention changes student outcomes;
- detailed grade forecasting;
- claims of fairness certification;
- deployment effectiveness beyond OULAD;
- final model metrics and recourse quality before the experiments are completed.

## 4. Related Work and Research Gap

### 4.1 At-Risk Prediction on OULAD

Adnan et al. [1] provide an important precedent for time-aware prediction on OULAD. They use cumulative features at course-progress points from 20% to 100%. EduGuard adopts the general checkpoint principle and proposes an additional 10% checkpoint. The main difference to be tested is the use of a frozen student-level split and separate full-cohort and still-enrolled reporting.

Tomasevic et al. [2] compare supervised methods on a DDD-module subset and report that engagement and assessment features are more informative than demographic variables. Their handling of missing values and conventional random splitting motivates EduGuard's decision to treat non-submission as a potential signal and to control student-level overlap.

Liu et al. [3] show the value of aggregating clickstream activity over temporal intervals. EduGuard follows the feature-compression principle but proposes recomputing the features at relative course-progress checkpoints and retaining students with no recorded clicks as observations rather than removing them automatically.

### 4.2 Explainable AI and Recourse

Gunasekara and Saarela [4] demonstrate the use of SHAP and LIME for educational prediction on an OULAD subset. Their explanations are mainly qualitative, motivating a planned quantitative analysis of stability across seeds and checkpoints. Counterfactual research, including Wachter et al. [5], Mothilal et al. [6], and OULAD-related work such as Tsiakmaki et al. [7], shows that actionable explanations are a relevant research direction. Therefore, EduGuard should not claim that counterfactual work is absent; its proposed gap is the integration of recourse with checkpoint-based, dual-cohort, leakage-safe evaluation and explanation-stability analysis.

### 4.3 Research Gap Graph

The research gap is an integration gap rather than a claim that every individual component is new.

| Study | OULAD scope | Time-aware | XAI | Quantitative stability | Imbalance comparison | Recourse |
|---|---|---|---|---|---|---|
| Adnan et al. [1] | Full OULAD | Yes | No | Not reported | Class merging | No |
| Tomasevic et al. [2] | DDD subset | Partial | No | Not reported | Not reported | No |
| Liu et al. [3] | Reduced clickstream subset | Temporal aggregation | No | Not reported | Not specified | No |
| Gunasekara and Saarela [4] | Three-module subset | Not central | SHAP + LIME | Mainly qualitative | Not central | No |
| Tsiakmaki et al. [7] | OULAD-related | Not central | Counterfactuals | Not reported | Not central | Yes |
| **EduGuard proposal** | **Full OULAD** | **Six checkpoints** | **SHAP + LIME** | **Planned quantitative analysis** | **Controlled comparison** | **Planned constrained recourse** |

The proposed research gap is the lack of a single, consistently evaluated workflow that combines time-aware prediction, student-level leakage control, dual-cohort reporting, quantitative explanation stability, imbalance analysis, and pedagogically constrained recourse on the full OULAD setting.

## 5. Data Requirements and Proposed Methodology

OULAD contains seven relational tables covering student information, registration, VLE activity, VLE metadata, assessment submissions, assessment metadata, and course metadata. The proposed analytical unit is one `(id_student, code_module, code_presentation)` enrolment.

The target will be derived from `final_result`: Fail and Withdrawn will be mapped to at-risk, while Pass and Distinction will be mapped to not-at-risk. This label definition and its approximately mild class imbalance will be verified from the raw data before modelling.

Features will be constructed from three main groups: demographic and contextual variables, VLE-engagement variables, and assessment-performance variables. Time-dependent records will be truncated at the relevant checkpoint so that no event after the prediction time enters an earlier feature vector.

The proposed evaluation will use a frozen student-level split. All records associated with an `id_student` will remain in the same partition. Missing-value handling, scaling, encoding, outlier thresholds, and resampling will be fitted or applied within the training data only. The final study will report recall and PR-AUC as primary metrics, with F1, ROC-AUC, calibration, and subgroup analysis as supporting metrics.

## 6. Work Plan for a Ten-Week Project

| Period | Planned work | Evidence expected |
|---|---|---|
| Weeks 1-2 | Problem definition, literature review, research graph, data specification, ethics and scope | Proposal, reviewed references, data requirements |
| Weeks 3-4 | Raw-data verification, master-table construction, cleaning, checkpoint design | Data dictionary, cleaning log, leakage tests |
| Weeks 5-6 | Baseline feature pipeline, frozen split, initial model training | Baseline metrics and reproducible training artifacts |
| Weeks 7-8 | Cross-validation, threshold analysis, SHAP/LIME, imbalance comparison | Validated result tables and explanation analyses |
| Week 9 | Counterfactual-recourse prototype and dashboard integration, if feasible | Recourse constraints, tests, prototype outputs |
| Week 10 | Reproducibility run, report freeze, figures, references, presentation | Final report and submission package |

## References

[1] M. Adnan et al., “Predicting at-Risk Students at Different Percentages of Course Length for Early Intervention Using Machine Learning Models,” *IEEE Access*, vol. 9, pp. 7519-7539, 2021.

[2] N. Tomasevic, N. Gvozdenovic, and S. Vranes, “An Overview and Comparison of Supervised Data Mining Techniques for Student Exam Performance Prediction,” *Computers & Education*, vol. 143, art. 103676, 2020.

[3] Y. Liu et al., “Predicting Student Performance Using Clickstream Data and Machine Learning,” *Education Sciences*, vol. 13, no. 1, art. 17, 2023.

[4] S. Gunasekara and M. Saarela, “Explainable AI in Education: Techniques and Qualitative Assessment,” *Applied Sciences*, vol. 15, no. 3, art. 1239, 2025.

[5] S. Wachter, B. Mittelstadt, and C. Russell, “Counterfactual Explanations Without Opening the Black Box,” *Harvard Journal of Law & Technology*, vol. 31, no. 2, pp. 841-887, 2018.

[6] R. K. Mothilal, A. Sharma, and C. Tan, “Explaining Machine Learning Classifiers through Diverse Counterfactual Explanations,” in *Proceedings of the ACM Conference on Fairness, Accountability, and Transparency*, 2020, pp. 607-617.

[7] M. Tsiakmaki et al., “Counterfactual Explanations for Student Success Prediction: A Comparative Study on OULAD,” in *Proceedings of the Workshop on Explainability and Transparency in Educational AI*, CEUR-WS, 2023.
