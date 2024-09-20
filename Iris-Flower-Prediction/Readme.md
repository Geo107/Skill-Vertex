# Iris Flower Prediction

This project focuses on classifying iris flower species based on sepal and petal measurements. Using machine learning algorithms, the goal is to accurately predict the species of an iris flower from the famous Iris dataset. The project includes data preprocessing, model training, evaluation, and deployment via a **Streamlit** web app.

---

## Project Overview

The Iris dataset contains three species of iris flowers: **Setosa**, **Versicolor**, and **Virginica**, along with four features:
- Sepal length
- Sepal width
- Petal length
- Petal width

This project aims to build a classification model that predicts the species based on these features.

---

## Technologies Used

- **Python**
- **Pandas** and **NumPy**: For data manipulation and preprocessing
- **Scikit-learn**: For implementing machine learning algorithms
- **Matplotlib** and **Seaborn**: For data visualization
- **Streamlit**: For creating an interactive web application

---

## Key Features

- **Data Exploration**: Visualized the dataset to understand feature distributions and relationships.
- **Model Training**: Employed various classification algorithms, including Logistic Regression and K-Nearest Neighbors (KNN).
- **Model Evaluation**: Evaluated models using metrics like accuracy, confusion matrix, and classification report.
- **Web App Deployment**: Deployed the trained model with a user-friendly interface using Streamlit, allowing users to input measurements and receive predictions.

---

## Project Structure

```
|-- Iris.csv             # Contains the Iris dataset
|-- iris_notebook.ipynb  # Jupyter notebooks for exploratory data analysis and model building
|-- iris_app.py          # Streamlit app for model deployment
|-- README.md            # Project documentation
```

---

## Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/Geo107/Skill-Vertex/Iris-Flower-Prediction.git
   cd Iris-Flower-Prediction
   ```
2. **Run the Streamlit app**:
   ```bash
   streamlit run iris_app.py
   ```

---

## Dataset

The Iris dataset is included in the project and contains the following columns:
- **SepalLengthCm**
- **SepalWidthCm**
- **PetalLengthCm**
- **PetalWidthCm**
- **Species**: The species of the iris flower (Setosa, Versicolor, Virginica)

---

## Model Performance

The model was evaluated using various metrics, with the best model achieving high accuracy on the test set. Key performance indicators include:
- **Accuracy**: 96.36%
- **Confusion Matrix**
- **Classification Report**

---

## Conclusion

This project demonstrates the application of machine learning for classification tasks using the Iris dataset. The deployed Streamlit app allows users to easily classify iris flowers based on their measurements, showcasing a practical use case for machine learning.

---

## Future Improvements

- **Hyperparameter Tuning**: To enhance model performance.
- **Explore Additional Algorithms**: Testing other classification algorithms for better accuracy.
- **Expand Dataset**: Including more flower species for a broader classification model.

---

## Contact

Feel free to connect with me on [LinkedIn](https://www.linkedin.com/in/geo-m-benny-901935221) for more information or collaboration opportunities.

---

Let me know if you need any adjustments or additional information!
