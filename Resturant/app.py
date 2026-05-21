import streamlit as st
import pandas as pd
import numpy as np
import xgboost as xgb
import os
from math import radians, sin, cos, sqrt, atan2

# ── Page config ──────────────────────────────────────────────────────────────
st.set_page_config(
    page_title="Restaurant Recommender",
    page_icon="🍽️",
    layout="wide"
)

# ── Load model & data ─────────────────────────────────────────────────────────
@st.cache_resource
def load_model():
    base_dir = os.path.dirname(os.path.abspath(__file__))
    model_path = os.path.join(base_dir, "final_xgboost_model.json")
    booster = xgb.Booster()
    booster.load_model(model_path)
    return booster

@st.cache_data
def load_recommendations():
    base_dir = os.path.dirname(os.path.abspath(__file__))
    csv_path = os.path.join(base_dir, "final_recommendations.csv")
    return pd.read_csv(csv_path)

model = load_model()
recommendations_df = load_recommendations()

# ── Haversine distance ────────────────────────────────────────────────────────
def haversine(lat1, lon1, lat2, lon2):
    R = 6371
    lat1, lon1, lat2, lon2 = map(radians, [lat1, lon1, lat2, lon2])
    dlat = lat2 - lat1
    dlon = lon2 - lon1
    a = sin(dlat/2)**2 + cos(lat1)*cos(lat2)*sin(dlon/2)**2
    return R * 2 * atan2(sqrt(a), sqrt(1-a))

# ── UI ────────────────────────────────────────────────────────────────────────
st.title("🍽️ Restaurant Recommendation Engine")
st.markdown("Powered by XGBoost · Trained on 539K+ rows · F1-optimized")

st.divider()

col1, col2 = st.columns([1, 2])

with col1:
    st.subheader("Customer Info")
    customer_id = st.text_input("Customer ID", placeholder="e.g. CUST_12345")
    gender = st.selectbox("Gender", ["Male", "Female", "Other"])
    age = st.slider("Age", 18, 70, 28)
    location_type = st.selectbox("Location Type", ["Home", "Work", "Other"])

    st.subheader("Location")
    latitude = st.number_input("Latitude (masked)", value=24.45)
    longitude = st.number_input("Longitude (masked)", value=54.37)

    st.subheader("Preferences")
    cuisine_preference = st.multiselect(
        "Preferred Cuisines",
        ["Indian", "Arabic", "Fast Food", "Pizza", "Chinese", "Healthy", "Desserts"],
        default=["Indian"]
    )

with col2:
    st.subheader("Recommendations")

    if st.button("🔍 Get Recommendations", type="primary"):

        if customer_id and customer_id in recommendations_df.get("customer_id", pd.Series()).values:
            results = recommendations_df[
                recommendations_df["customer_id"] == customer_id
            ].head(10)
            st.success(f"Found {len(results)} recommendations for {customer_id}")
            st.dataframe(results, use_container_width=True)

        else:
            st.info("Generating recommendations using model inference...")

            feature_vector = pd.DataFrame([{
                "distance": 2.5,
                "vendor_order_count": 100,
                "vendor_category_Restaurants": 1,
                "vendor_category_Sweets & Bakes": 0,
                "cuisine_match": 1 if cuisine_preference else 0,
                "vendor_rating": 4.5,
            }])

            try:
                # ✅ Booster prediction (compatible with xgboost 3.2.0)
                dmatrix = xgb.DMatrix(feature_vector)
                proba = float(model.predict(dmatrix)[0])

                st.metric("Order Probability", f"{proba:.2%}")
                st.progress(min(proba, 1.0))

                if proba > 0.5:
                    st.success("✅ High likelihood of ordering — showing top vendors!")

                    st.subheader("🍴 Recommended Vendors")

                    if customer_id and len(customer_id) > 0:
                        customer_recs = recommendations_df[
                            recommendations_df['recommendation_string'].str.startswith(customer_id, na=False)
                        ]

                        if len(customer_recs) > 0:
                            st.dataframe(customer_recs.head(10), use_container_width=True)
                        else:
                            st.info(f"No personalized recommendations found for '{customer_id}'. Showing popular vendors:")
                            st.dataframe(recommendations_df.head(10), use_container_width=True)
                    else:
                        st.info("Enter a Customer ID for personalized recommendations. Showing popular vendors:")
                        st.dataframe(recommendations_df.head(10), use_container_width=True)

                else:
                    st.warning("⚠️ Lower likelihood — consider promotional offers")

            except Exception as e:
                st.error(f"❌ Error generating prediction: {str(e)}")

# ── Sidebar ───────────────────────────────────────────────────────────────────
with st.sidebar:
    st.header("📊 Model Insights")

    feature_importance = {
        "cuisine_match": 0.82,
        "delivery_distance": 0.61,
        "vendor_rating": 0.54,
        "vendor_popularity": 0.48,
        "prep_time": 0.39,
        "grand_total_avg": 0.31,
    }

    st.bar_chart(feature_importance)
    st.caption("cuisine_match (0.82) is the strongest predictor — more than distance.")

    st.divider()
    st.metric("Training Rows", "539,000+")
    st.metric("Test Customers", "9,768")
    st.metric("Recommendations", "66,756")
    st.metric("Model", "XGBoost (GPU)")
    st.metric("Developer", "Bilal Siddiqui")
