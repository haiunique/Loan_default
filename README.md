# Loan Default Prediction – Machine Learning Project

Final Project: Credit Risk Analysis & Default Prediction using Python
Author: Your Name
Module: Machine Learning / Data Science
Class: 4th year – Computer Science (AI/ML/Data Science)

 # Project Overview

This project focuses on analyzing customer loan data and building a machine learning model to predict whether a borrower will default on their loan.

It includes 3 main parts:

 Data Analysis & Preprocessing

 Exploratory Data Visualization

 Machine Learning Models for Loan Default Classification

Dataset contains information about customer demographics, income, loan history, credit behavior and repayment status.

# 2. Objectives

💳 Understand factors that affect loan repayment.

📉 Analyze trends between income, loan amount, credit score and default rate.

🤖 Build predictive models to classify customers as:

0 – Non-default (Good borrower)

1 – Default risk (High-risk borrower)

📊 Evaluate models using Accuracy, Precision, Recall, F1-score, ROC-AUC.

# 3. Project Structure 
Loan_Default/
│
├── data/                    # Raw & cleaned datasets (if dataset < 25MB)
├── code/
│   ├── Data_processing.ipynb
│   ├── Model.ipynb
│   └── utils.py (if any)
│
├── app/
│   └── streamlit_app.py     # Web demo with Streamlit
│
├── visualization/           # Graphs, plots, correlation heatmaps
├── documents/               # Report, slides, project descriptions
├── models/                  # Saved models (.pkl, .joblib)
├── README.md
└── requirements.txt

# 4. Dataset Description
Feature	Description
loan_id	Unique ID for each loan
customer_id	Customer identifier
loan_amount	Amount of loan requested
loan_term	Number of months to repay
credit_score	Credit score of customer
income	Annual income
employment_type	Salaried / Self-employed
age	Borrower age
gender	Male / Female
default	Target (0 = paid, 1 = defaulted)
# 5. Machine Learning Models Used

Logistic Regression

Decision Tree / Random Forest

XGBoost / LightGBM (optional advanced)

Model evaluation with:
✔ Confusion Matrix
✔ ROC-AUC Curve
✔ Precision-Recall

# 6. Tech Stack & Requirements
Tool/Library	Purpose
Python	Programming
Pandas, Numpy	Data processing
Matplotlib, Seaborn	Visualization
Scikit-learn	ML models & metrics
Streamlit	Web deployment
Jupyter Notebook	Development
# 7. How to Run the Project
git clone https://github.com/username/Loan_Default.git
cd Loan_Default
pip install -r requirements.txt
streamlit run app/streamlit_app.py

# 8. References

Kaggle Loan Default Datasets

Credit Risk Analysis Papers

Scikit-learn Documentation
