# Credit Scoring Model

## Project Overview

The Credit Scoring Model is a Machine Learning project developed to predict the credit risk of loan applicants based on their financial and personal information.

The model analyzes various factors such as age, income, employment length, loan amount, interest rate, and credit history to determine whether a customer is likely to default on a loan.

---

## Objective

To build a classification model that can predict loan risk and help financial institutions make better lending decisions.

---

## Dataset

Dataset Used: Credit Risk Dataset

Features Included:

- Person Age
- Person Income
- Home Ownership
- Employment Length
- Loan Intent
- Loan Grade
- Loan Amount
- Interest Rate
- Loan Percent Income
- Previous Loan Default
- Credit History Length

Target Variable:

- loan_status
  - 0 = Low Credit Risk
  - 1 = High Credit Risk

---

## Technologies Used

- Python
- Pandas
- NumPy
- Scikit-Learn
- Joblib
- Streamlit

---

## Machine Learning Workflow

1. Data Collection
2. Data Preprocessing
3. Handling Missing Values
4. Label Encoding
5. Feature Selection
6. Train-Test Split
7. Model Training
8. Model Evaluation
9. Model Saving
10. Deployment using Streamlit

---

## Algorithm Used

Random Forest Classifier

The Random Forest algorithm was used to classify loan applicants into low-risk and high-risk categories.

---

## Model Evaluation

Evaluation Metrics:

- Accuracy Score
- Precision
- Recall
- F1 Score
- Confusion Matrix

---

## Project Structure

```text
CodeAlpha_CreditScoringModel/
│
├── credit_risk_dataset.csv
├── Credit_Scoring.ipynb
├── credit_model.pkl
├── app.py
├── requirements.txt
└── README.md
```

## Running the Project

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the Streamlit application:

```bash
streamlit run app.py
```

---

## Results

The trained model successfully predicts loan risk based on applicant information and can assist in credit approval decision-making.

---

## Future Improvements

- Hyperparameter Tuning
- Feature Engineering
- XGBoost Implementation
- Model Deployment on Cloud
- Real-time Prediction System

---

## Internship Project

This project was developed as part of the Machine Learning Internship Program at CodeAlpha.

---

## Author

Anmol

B.Tech CSE Student

Machine Learning Enthusiast
