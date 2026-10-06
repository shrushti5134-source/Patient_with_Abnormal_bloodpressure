import streamlit as st
import pickle

# Page configuration
st.set_page_config(
    page_title="Blood Pressure AI Assistant",
    page_icon="🩺",
    layout="wide"
)

# Load trained Random Forest model
with open("random_forest.pkl", "rb") as file:
    model = pickle.load(file)

# Title
st.title("🩺 Blood Pressure AI Assistant")

st.write(
    "This application uses a Machine Learning model "
    "to predict blood pressure abnormality."
)

st.divider()

st.header("🔍 Blood Pressure Prediction")

st.header("🔍 Blood Pressure Prediction")

# Patient inputs
col1, col2 = st.columns(2)

with col1:
    hemoglobin = st.number_input(
        "Level of Hemoglobin",
        min_value=8.1,
        max_value=17.56,
        value=13.0
    )

    pedigree = st.number_input(
        "Genetic Pedigree Coefficient",
        min_value=0.0,
        max_value=1.0,
        value=0.5
    )

    age = st.number_input(
        "Age",
        min_value=18,
        max_value=75,
        value=30
    )

    bmi = st.number_input(
        "BMI",
        min_value=10,
        max_value=50,
        value=25
    )

    sex = st.selectbox(
        "Sex",
        options=[0, 1]
    )

    pregnancy = st.selectbox(
        "Pregnancy",
        options=[0, 1]
    )

    smoking = st.selectbox(
        "Smoking",
        options=[0, 1]
    )

with col2:
    physical_activity = st.number_input(
        "Physical Activity",
        min_value=628,
        max_value=49980,
        value=10000
    )

    salt = st.number_input(
        "Salt Content in the Diet",
        min_value=22,
        max_value=49976,
        value=10000
    )

    alcohol = st.number_input(
        "Alcohol Consumption per Day",
        min_value=0.0,
        max_value=499.0,
        value=100.0
    )

    stress = st.selectbox(
        "Level of Stress",
        options=[1, 2, 3]
    )

    kidney = st.selectbox(
        "Chronic Kidney Disease",
        options=[0, 1]
    )

    adrenal = st.selectbox(
        "Adrenal and Thyroid Disorders",
        options=[0, 1]
    )

# Prediction button
if st.button("🔮 Predict Blood Pressure Abnormality"):

    input_data = [[
        hemoglobin,
        pedigree,
        age,
        bmi,
        sex,
        pregnancy,
        smoking,
        physical_activity,
        salt,
        alcohol,
        stress,
        kidney,
        adrenal
    ]]

    prediction = model.predict(input_data)

    st.success(f"Prediction: {prediction[0]}")