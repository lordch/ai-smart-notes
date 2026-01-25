# ML Pipeline Building Agent

## Domena
Data Science / Machine Learning / Analytics

## Problem klienta
- Budowanie ML pipeline to dużo boilerplate code
- Cross-validation, feature engineering — powtarzalne ale error-prone
- Data scientists spędzają czas na plumbing zamiast modeling
- Prototyp → production gap
- "Zrobiłem model, ale nie wiem czy dobrze"

## Kluczowy insight

> Claude Code jest szczególnie dobry w taskach które są **"hard to make but easy to check"** — ML pipelines to idealny przykład.

## Workflow agentowy

1. **Data exploration**
   - Agent analizuje dataset (shape, dtypes, missing values)
   - Generuje summary statistics
   - Identyfikuje target variable i features

2. **Feature engineering**
   - Agent proponuje transformations
   - Tworzy derived features
   - Handles encoding, scaling

3. **Model building**
   - Agent implementuje pipeline ze proper cross-validation
   - Testuje multiple algorithms
   - Handles train/test split correctly

4. **Evaluation**
   - Proper metrics dla problem type
   - Confusion matrix, feature importance
   - Overfitting checks

5. **Documentation**
   - Agent dokumentuje decisions
   - Zapisuje reproducible code

## Przykładowy prompt
```
Build a classification model for customer churn prediction:

Data: customers.csv
Target: churned (0/1)
Features: all other columns

Requirements:
1. Exploratory analysis first (missing values, distributions)
2. Feature engineering:
   - Handle missing values appropriately
   - Encode categoricals
   - Scale numericals
   - Create interaction features if useful
3. Model:
   - Use proper cross-validation (5-fold stratified)
   - Try: LogisticRegression, RandomForest, XGBoost
   - Hyperparameter tuning for best model
4. Evaluation:
   - ROC-AUC, Precision, Recall, F1
   - Confusion matrix
   - Feature importance plot
5. Output:
   - Trained model (pickle)
   - Evaluation report (markdown)
   - Reproducible training script
```

## Before / After
| Manual | Z agentem |
|--------|-----------|
| 3-4h na pipeline | ~1h z review |
| Często błędy w CV | Proper implementation |
| Boilerplate code | Generated correctly |
| Ad-hoc evaluation | Comprehensive metrics |
| Undocumented | Auto-documented |

## ROI / Metryki
- Time: 3-4h → 1h (70% reduction)
- Quality: proper CV, no data leakage
- Consistency: same structure every time
- Learning: code is readable, can learn from it

## Wymagania wdrożeniowe
- Dane: dataset (CSV, Parquet, etc.)
- Narzędzia: Claude Code + Python (sklearn, pandas, etc.)
- Complexity: **Medium** (standard ML) / **High** (deep learning)
- Review: data scientist should validate logic

## Przykłady zastosowań

| Problem | Algorithm type | Metrics |
|---------|---------------|---------|
| Churn prediction | Classification | AUC, F1 |
| Revenue forecasting | Regression | RMSE, MAE |
| Customer segmentation | Clustering | Silhouette |
| Anomaly detection | Outlier detection | Precision@k |
| Recommendation | Collaborative filtering | MAP, NDCG |

## Warianty / Rozszerzenia
- AutoML mode: "Try all reasonable approaches"
- Explainability: SHAP values, feature importance
- Deployment: export to ONNX, create API endpoint
- Monitoring: data drift detection
- A/B testing setup

## Failure Modes (uwaga!)
- Data leakage: agent może nie wykryć subtle leakage
- Overfitting: ZAWSZE sprawdź test set performance
- Domain knowledge: agent nie zna business context
- Scale: bardzo duże datasets wymagają optimization
- Interpretability: complex models = black box

## Kiedy używać
- Prototyping: szybkie sprawdzenie czy problem jest ML-soluble
- Standard problems: classification, regression, clustering
- Time pressure: potrzeba baseline model szybko
- Learning: chcesz zobaczyć "jak to się robi properly"

## Kiedy NIE używać
- Novel research problems
- Very large scale (distributed computing)
- Production deployment (needs MLOps review)
- Highly regulated domains (needs audit trail)

## Źródło
[Matt Stockton - AI Coding Tools Amplify What You Already Know](https://mattstockton.com/2025/06/21/ai-coding-tools-amplify-what-you-already-know.html)
[Matt Stockton - AI Coding Tools: Why I Use Claude Code](https://mattstockton.com/2025/06/14/ai-coding-tools-journey.html)
[Matt Stockton - Claude Code Posts](../literature/Matt%20Stockton%20-%20Claude%20Code%20Posts.md)
