import streamlit as st
import pandas as pd
import joblib

# Load Trained Model
model = joblib.load("credit_model.pkl")

st.title("Credit Scoring Model")
st.write("Predict Loan Risk using Machine Learning")

# User Inputs

person_age = st.number_input("Age", min_value=18, max_value=100)

person_income = st.number_input("Annual Income")

person_emp_length = st.number_input("Employment Length (Years)")

loan_amnt = st.number_input("Loan Amount")

loan_int_rate = st.number_input("Interest Rate")

loan_percent_income = st.number_input("Loan Percent Income")

cb_person_cred_hist_length = st.number_input(
    "Credit History Length"
)

person_home_ownership = st.selectbox(
    "Home Ownership",
    [0, 1, 2, 3]
)

loan_intent = st.selectbox(
    "Loan Intent",
    [0, 1, 2, 3, 4, 5]
)

loan_grade = st.selectbox(
    "Loan Grade",
    [0, 1, 2, 3, 4, 5, 6]
)

cb_person_default_on_file = st.selectbox(
    "Previous Default",
    [0, 1]
)

# Prediction

if st.button("Predict"):

    input_data = pd.DataFrame({
        "person_age": [person_age],
        "person_income": [person_income],
        "person_home_ownership": [person_home_ownership],
        "person_emp_length": [person_emp_length],
        "loan_intent": [loan_intent],
        "loan_grade": [loan_grade],
        "loan_amnt": [loan_amnt],
        "loan_int_rate": [loan_int_rate],
        "loan_percent_income": [loan_percent_income],
        "cb_person_default_on_file": [cb_person_default_on_file],
        "cb_person_cred_hist_length": [cb_person_cred_hist_length]
    })

    prediction = model.predict(input_data)

    if prediction[0] == 1:
        st.error("High Credit Risk ❌")
    else:
        st.success("Low Credit Risk / Loan Approved ✅")