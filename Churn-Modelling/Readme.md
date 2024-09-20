# Customer Churn Modeling (Telecom Sector)

This project focuses on predicting customer churn in the telecom sector using machine learning algorithms. The model helps identify customers who are likely to leave the service provider, enabling proactive retention strategies. The project includes data preprocessing, model building, evaluation, and deployment via a **Streamlit** web app.

---

## Project Overview

Customer churn refers to the percentage of customers who stop using a company's services during a given time frame. In this project, I developed a classification model to predict whether a customer will churn based on features like:
- Monthly charges
- Tenure
- Contract type
- Payment method

---

## Technologies Used

- **Python**
- **Pandas** and **NumPy**: For data manipulation and preprocessing
- **Scikit-learn**: For machine learning algorithms
- **TensorFlow/Keras**: For building deep learning models
- **Matplotlib** and **Seaborn**: For data visualization
- **Streamlit**: For creating an interactive web application
- **Kaggle**: As a source for dataset exploration
- **Medium** and **Towards Data Science**: For learning resources

---

## Key Features

- **Data Preprocessing**: Handled missing values, feature scaling, and one-hot encoding for categorical features.
- **Model Training**: Used machine learning algorithms like Logistic Regression, KNN, and Deep Learning (using TensorFlow/Keras).
- **Model Evaluation**: Evaluated models using metrics like accuracy, precision, recall, F1-score, and AUC.
- **Web App Deployment**: Deployed the final model with an intuitive user interface using Streamlit, allowing users to input customer data and receive churn predictions in real-time.

---

## Project Structure

```
|-- test.csv             # Contains the test dataset
|-- train.csv            # Contains train dataset
|-- Customer2.ipynb      # Jupyter notebooks for exploratory data analysis and model building
|-- Churn_Model1.pkl     # Saved machine learning models
|-- Churn_app1.py        # Streamlit app for model deployment
|-- README.md            # Project documentation
```

---

## Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/Geo107/Skill-Vertex/Churn-Modelling.git
   cd Churn-Model
   ```
   
2. **Run the Streamlit app**:
   ```bash
   streamlit run Churn_app1.py
   ```

---

## Dataset

The dataset used for this project contains various features of telecom customers, including:
- **Customer ID**
- **Tenure**: Number of months the customer has been with the company
- **Contract**: Type of contract (monthly, yearly, etc.)
- **MonthlyCharges**: Customer's monthly charges
- **Churn**: Whether the customer has churned (Yes/No)

---

## Model Performance

The model was evaluated using several metrics:
- **Accuracy**: 90%
- **Precision, Recall, F1-Score**
- **Confusion Matrix**

---

## Conclusion

This project provides a solid foundation for predicting customer churn and deploying machine learning models in real-world applications. The deployed Streamlit app makes it easy for businesses to analyze customer data and receive predictions on potential churn.

---

## Future Improvements

- **Hyperparameter Tuning**: To improve model performance.
- **Feature Engineering**: To extract more insights from customer behavior.
- **Integration with Real-time Data**: For live prediction as new data comes in.

---

## Contact

Feel free to connect with me on [LinkedIn](https://www.linkedin.com/in/geo-m-benny-901935221) for more information or collaboration opportunities.

---

Let me know if you'd like any modifications or additional sections!
