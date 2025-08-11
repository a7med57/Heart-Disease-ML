# ============================================================
# app.py
# Streamlit UI for Heart Disease Prediction
# ============================================================

import streamlit as st
import pandas as pd
import joblib

# ---- Load model ----
model_path = 'model/final_model.pkl'  # adjust if needed
model = joblib.load(model_path)

st.set_page_config(page_title="Heart Disease Prediction", layout="centered")

# ---- Title ----
st.title("❤️ Heart Disease Prediction App")
st.write("Enter patient information to predict the likelihood of heart disease.")

# ---- Input form ----
with st.form("patient_form"):
    age = st.number_input("Age", min_value=20, max_value=100, value=50)
    sex = st.selectbox("Sex", options=[0, 1], format_func=lambda x: "Female" if x == 0 else "Male")
    cp = st.selectbox("Chest Pain Type (cp)", options=[1, 2, 3, 4])
    trestbps = st.number_input("Resting Blood Pressure (trestbps)", min_value=80, max_value=200, value=120)
    chol = st.number_input("Serum Cholesterol (chol)", min_value=100, max_value=600, value=200)
    fbs = st.selectbox("Fasting Blood Sugar > 120 mg/dl (fbs)", options=[0, 1], format_func=lambda x: "No" if x == 0 else "Yes")
    restecg = st.selectbox("Resting ECG Results (restecg)", options=[0, 1, 2])
    thalach = st.number_input("Max Heart Rate Achieved (thalach)", min_value=60, max_value=220, value=150)
    exang = st.selectbox("Exercise Induced Angina (exang)", options=[0, 1], format_func=lambda x: "No" if x == 0 else "Yes")
    oldpeak = st.number_input("ST Depression (oldpeak)", min_value=0.0, max_value=6.5, value=1.0, step=0.1)
    slope = st.selectbox("Slope of Peak Exercise ST Segment (slope)", options=[1, 2, 3])
    ca = st.selectbox("Number of Major Vessels (ca)", options=[0, 1, 2, 3, 4])
    thal = st.selectbox("Thal", options=[3, 6, 7])

    submit = st.form_submit_button("Predict")

# ---- Prediction ----
if submit:
    input_data = pd.DataFrame([{
        'age': age,
        'sex': sex,
        'cp': cp,
        'trestbps': trestbps,
        'chol': chol,
        'fbs': fbs,
        'restecg': restecg,
        'thalach': thalach,
        'exang': exang,
        'oldpeak': oldpeak,
        'slope': slope,
        'ca': ca,
        'thal': thal
    }])

    prediction = model.predict(input_data)[0]
    probability = model.predict_proba(input_data)[0][1]

    st.subheader("Prediction Result")
    if prediction == 1:
        st.error(f"High risk of heart disease ({probability*100:.2f}% probability).")
    else:
        st.success(f"Low risk of heart disease ({probability*100:.2f}% probability).")
