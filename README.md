# 🍽️ Restaurant Recommendation Engine

> A machine learning-powered recommendation system that predicts which restaurants a customer is most likely to order from, based on their location, order history, and cuisine preferences.
---

## 🌐 Live Demo

> Deployed on Streamlit Cloud — https://restaurant-recommendation-engine-qsqdppoxcxtk33ecnudfez.streamlit.app/

---

## 📌 Problem Statement

Given customer location, restaurant information, and order history — predict which vendor a customer is most likely to order from next. Built as part of a Data Scientist Intern assignment for **Soulpage IT Solutions**.

---

## 📊 Dataset Overview

| Dataset | Description | Size |
|---|---|---|
| Train Customers | Customer demographics & account info | 34,674 customers |
| Train Locations | Customer delivery locations (masked lat/lon) | Multiple per customer |
| Train Orders | Historical order records with vendor, timing, payment | 135,303 positive samples |
| Vendors | 100 vendor profiles with tags, ratings, location | 100 vendors |
| Test Customers | Customers to generate recommendations for | 9,768 customers |

---

## 🧠 Model Architecture

### Pipeline Overview

```
Raw Data → Cleaning → Negative Sampling → Feature Engineering → XGBoost → Threshold Tuning → Recommendations
```

### 1. Data Cleaning & Preparation
- Merged customer demographics with location data
- Filled missing `gender` → `'Unknown'`, `location_type` → `'Other'`
- Extracted `order_hour` and `order_day_of_week` from timestamps

### 2. Negative Sampling
- **Positive samples:** 135,303 actual orders (target = 1)
- **Negative candidates:** 5,870,158 customer-vendor pairs with no order history
- **Negative samples selected:** 416,521 (7 per customer-location pair)
- **Final training data:** 551,824 rows

### 3. Feature Engineering

| Feature | Description | Importance |
|---|---|---|
| `cuisine_match` | Vendor cuisine tag matches customer's past orders | **0.82** |
| `vendor_rating` | Average vendor rating | 0.054 |
| `vendor_category` | Restaurants / Sweets & Bakes | 0.052 |
| `vendor_order_count` | Overall vendor popularity | 0.051 |
| `distance` | Haversine distance between customer & vendor | 0.020 |

> 💡 **Key Insight:** Cuisine preference (0.82) is far more predictive than delivery distance (0.020) — customers prioritize *what* they eat over *how far* it is.

### 4. Modeling

- **Baseline:** Logistic Regression — ROC AUC: 0.69, Class 1 Recall: 18%
- **Final Model:** XGBoost (GPU-accelerated) with `scale_pos_weight` for class imbalance
- **Threshold Optimization:** Optimal threshold of **0.6968** found via Precision-Recall curve

---

## 📈 Model Performance

| Metric | Logistic Regression | XGBoost (Final) |
|---|---|---|
| ROC AUC | 0.69 | **0.97** |
| Class 1 Precision | 47% | **87%** |
| Class 1 Recall | 18% | **82%** |
| Class 1 F1-Score | 26% | **0.84** |

---

## 📦 Project Structure

```
Restaurant-Recommendation-Engine/
└── Resturant/
    ├── app.py                        # Streamlit web application
    ├── final_xgboost_model.json      # Trained XGBoost model (Booster format)
    ├── final_recommendations.csv     # 66,756 pre-computed recommendations
    ├── requirements.txt              # Python dependencies
    └── README.md
```

---

## 🚀 Getting Started

### Prerequisites
```bash
pip install -r requirements.txt
```

### Run Locally
```bash
streamlit run app.py
```

App opens at `http://localhost:8501`

### Load Model & Data
```python
import xgboost as xgb
import pandas as pd

# ✅ Load model using Booster (compatible with xgboost 3.2.0)
booster = xgb.Booster()
booster.load_model("final_xgboost_model.json")

# Run prediction
dmatrix = xgb.DMatrix(feature_vector)
proba = booster.predict(dmatrix)[0]

# Load recommendations
df = pd.read_csv("final_recommendations.csv")
```

---

## 🌐 Deployment

Deployed on **Streamlit Cloud** (free):

1. Push repo to GitHub
2. Go to [share.streamlit.io](https://share.streamlit.io)
3. Connect repo → set main file path to `Resturant/app.py`
4. Click Deploy → get a live public URL

---

## 📋 Requirements

```
streamlit==1.57.0
xgboost== 3.2.0
pandas== 3.0.2
numpy==2.4.4
scikit-learn==1.8.0
```

---

## 🔑 Key Results

- ✅ **66,756** prioritized recommendations generated for 9,768 test customers
- ✅ Formatted as `CID X LOC_NUM X VENDOR` for submission
- ✅ `cuisine_match` identified as the **#1 predictor** (importance: 0.82)
- ✅ Training pipeline scaled to **539,000+ rows**
- ✅ ROC AUC improved from **0.69 → 0.97** over baseline
- ✅ Successfully deployed on Streamlit Cloud using `xgb.Booster()` for version compatibility

---

## 👤 Author

**Bilal Siddiqui**
CSE (AI & Data Science) — ISL Engineering College, Hyderabad
GitHub: [@BilalSiddiqui-exe](https://github.com/BilalSiddiqui-exe)

---

## 📄 License

This project was built as part of a Data Scientist Intern assignment for Soulpage IT Solutions.
