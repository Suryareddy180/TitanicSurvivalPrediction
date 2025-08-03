import streamlit as st
import pickle
import numpy as np

# Load model
with open('titanic_model.pkl', 'rb') as f:
    model = pickle.load(f)

# Custom page config
st.set_page_config(
    page_title="Titanic Survival Predictor 🚢",
    page_icon="🌊",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# Custom CSS for styling
st.markdown("""
    <style>
        .main-title {
            font-size: 40px;
            text-align: center;
            font-weight: bold;
            color: #006994;
        }
        .result-box {
            background-color: #f0f9ff;
            padding: 20px;
            border-radius: 15px;
            border: 2px solid #91d1f2;
            text-align: center;
            font-size: 24px;
            font-weight: bold;
            color: #2b6777;
        }
        .footer {
            position: fixed;
            bottom: 10px;
            width: 100%;
            text-align: center;
            font-size: 13px;
            color: gray;
        }
    </style>
""", unsafe_allow_html=True)

# Title
st.markdown('<div class="main-title">🚢 Titanic Survival Prediction</div>', unsafe_allow_html=True)
st.markdown("---")
st.markdown("🔍 *Fill in the passenger details below to see if they would have survived the Titanic disaster.*")

# Input form
with st.form("titanic_form"):
    col1, col2 = st.columns(2)

    with col1:
        pclass = st.selectbox("🎫 Passenger Class", [1, 2, 3], index=0, help="1 = 1st, 2 = 2nd, 3 = 3rd class")
        age = st.slider("🎂 Age", 1, 100, 25)
        fare = st.number_input("💵 Fare ($)", min_value=0.0, max_value=600.0, value=50.0)

    with col2:
        sex = st.radio("⚧️ Sex", ['male', 'female'])
        sibsp = st.number_input("👨‍👩‍👧‍👦 Siblings/Spouses Aboard", min_value=0, max_value=10, value=0)

    submit = st.form_submit_button("🔮 Predict")

# Encoding & Prediction
if submit:
    sex_encoded = 1 if sex == 'male' else 0
    input_data = np.array([[pclass, sex_encoded, age, sibsp, fare]])
    prediction = model.predict(input_data)[0]
    result = "✅ Survived" if prediction == 1 else "❌ Did Not Survive"

    st.markdown('<div class="result-box">🧠 Prediction: ' + result + '</div>', unsafe_allow_html=True)
