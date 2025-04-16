# 🏦 Loan Default Prediction Using Machine Learning

This project predicts whether a loan application will be approved or not, based on applicant details. It's inspired by real-life banking challenges and uses classification algorithms like Logistic Regression to automate decision-making.

---

## 🚀 Objective

To build a machine learning model that classifies loan applications as **Approved (Y)** or **Not Approved (N)** using applicant information such as income, credit history, and education.

---

## 📁 Dataset

- 📦 [Loan Prediction Dataset on Kaggle](https://www.kaggle.com/datasets/anmolkumar/analytics-vidhya-loan-prediction)
- **train.csv** – Includes features + `Loan_Status` (Y/N)
- **test.csv** – Includes only features (no target)
- **sample_submission.csv** – Shows required output format
- **final_submission.csv** – Your final model predictions

---

## 📌 Features Used

| Feature | Description |
|---------|-------------|
| Gender | Applicant's gender |
| Married | Marital status |
| Dependents | Number of dependents |
| Education | Graduate / Not Graduate |
| Self_Employed | Self employment status |
| ApplicantIncome | Income of the applicant |
| LoanAmount | Loan amount requested |
| Loan_Amount_Term | Loan term in months |
| Credit_History | 1 = Good history, 0 = No history |
| Property_Area | Urban / Rural / Semiurban |

---

## 🧠 ML Workflow

1. **Data Cleaning**
   - Handled missing values (mode/median)
   - Encoded categorical columns (Label Encoding)

2. **Exploratory Data Analysis (EDA)**
   - Class balance check
   - Count plots for key features
   - Correlation heatmap

3. **Model Building**
   - Split train data (80/20)
   - Logistic Regression used
   - Accuracy checked using `accuracy_score`

4. **Final Prediction**
   - Cleaned `test.csv` the same way
   - Model made predictions
   - Output saved in `final_submission.csv` (Y/N format)

---

## 📊 Model Performance

- **Algorithm:** Logistic Regression
- **Accuracy:** ~81% (approx.)
- Predicts loan approval based on key features like Credit History, Income, Education

---

## 📂 Folder Structure

---

## 🔚 Conclusion

This project builds a complete machine learning pipeline for binary classification. The model automates loan approval prediction using simple features and achieves decent performance.

You can improve it further by:
- Trying advanced models (Random Forest, XGBoost)
- Doing feature engineering
- Hyperparameter tuning
- Cross-validation

---

## 🙋 Author

**Akhil**  
*Master’s in Data Science & Analytics (FAU)*  
[GitHub Profile](https://github.com/akhil0404-tech)

