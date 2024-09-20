import streamlit as st
import pandas as pd
import numpy as np
from sklearn import datasets
from sklearn.ensemble import RandomForestClassifier

st.write("""
# Iris Flower Prediction


This model predicts what kind of iris flower is using Random Forest Machine Learning algorithm

""")

st.sidebar.header('User Input Parameters')

def user_input():
    sepal_length = st.sidebar.slider('Sepal Length',4.0,8.0,5.2)
    sepal_width = st.sidebar.slider('Sepal Width',2.0,5.0,3.2)
    petal_length = st.sidebar.slider('Petal Length',0.1,6.9,1.3)
    petal_width = st.sidebar.slider('Petal Width',0.1,2.5,0.2)
    data = {    
        'Sepal Length': sepal_length,
        'Sepal Width':sepal_width,
        'Petal Length':petal_length,
        'Petal Width': petal_width
    }

    feature = pd.DataFrame(data,index=[0])
    return feature

df = user_input()

st.subheader("User Input Features")
st.write(df)

iris = datasets.load_iris()
x = iris.data
y = iris.target

b = RandomForestClassifier()
b.fit(x,y)

prediction = b.predict(df)
prediction_prob = b.predict_proba(df)

st.subheader("Class Names")
st.write(iris.target_names)

st.subheader("Prediction")
st.write(iris.target_names[prediction])

st.subheader("Prediction Probability")
st.write(prediction_prob)