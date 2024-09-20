# Loan Amount Prediction

This project aims to predict the loan amount for customers based on their profiles using machine learning algorithms. By analyzing various features, the model provides insights into how different factors influence loan eligibility and amount.

---

## Project Overview

The loan prediction model leverages a dataset containing customer details to forecast the loan amount they are eligible to receive. Key features include:
- Applicant income
- Credit score
- Loan history
- Employment status

---

## Technologies Used

- **Python**
- **Pandas** and **NumPy**: For data manipulation and preprocessing
- **Scikit-learn**: For building and evaluating machine learning models
- **Streamlit**: For creating an interactive web application to deploy the model

---

## Key Features

- **Data Preprocessing**: Handled missing values and performed feature scaling to prepare the dataset for modeling.
- **Model Training**: Employed various algorithms, including Support Vector Classifier and Logistic Regression, to predict loan amounts.
- **Model Evaluation**: Evaluated model performance using metrics such as accuracy, confusion matrix, and ROC curve.
- **Web App Deployment**: Developed an interactive user interface using Streamlit, allowing users to input their details and receive loan amount predictions.

---

## Project Structure

```
|-- test.csv & train.csv # Contains the loan dataset
|-- loan.ipynb           # Jupyter notebooks for exploratory data analysis and model building
|-- Loan_app.py          # Streamlit app for model deployment
|-- README.md            # Project documentation
```

---

## Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/Geo107/Skill-Vertex/Loan-Mount.git
   cd Loan-Mount
   ```
   
2. **Run the Streamlit app**:
   ```bash
   streamlit run app.py
   ```

---

## Dataset

The dataset used for this project includes features such as:
- **ApplicantIncome**
- **CoapplicantIncome**
- **LoanAmount**
- **Credit_History**
- **Loan_Status**

---

## Model Performance

The model was evaluated based on various metrics, achieving promising results in predicting loan amounts:
- **Accuracy**: 93%
- **Confusion Matrix**
- **ROC Curve**

---

## Conclusion

This project demonstrates the use of machine learning to predict loan amounts, providing valuable insights for financial institutions. The deployed Streamlit app enables users to input their details and receive loan predictions in real-time, showcasing the practical application of predictive modeling.

---

## Future Improvements

- **Hyperparameter Tuning**: To optimize model performance further.
- **Feature Engineering**: To explore additional features that could improve predictions.
- **Integration with Real-time Data**: For live predictions based on incoming customer profiles.

---

## Contact

Feel free to connect with me on [LinkedIn](https://www.linkedin.com/in/geo-m-benny-901935221) for more information or collaboration opportunities.

---

Let me know if you’d like any changes or additional sections!
