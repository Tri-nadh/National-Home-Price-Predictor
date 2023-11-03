import streamlit as st
import joblib
import pandas as pd

data = pd.read_csv('Data.csv')
print(data.head())
st.markdown("<h1 style='text-align: center;'>Home Price Predictor</h1>", unsafe_allow_html=True)
loaded_model = joblib.load('predictor.pkl')
population = st.number_input('Enter the Nation Population:')
unirate = st.number_input('Enter the Nation Unemployment Rate:')
supply = st.number_input('Enter the Nation Home supply Rate:')
mortgage = st.number_input('Enter the Nation Mortgage Rate:')


new_data = pd.DataFrame({'Population': [population], 'Unirate': [unirate], 'Supply': [supply], 'Mortgages':[mortgage]})
predictions = loaded_model.predict(new_data)


if st.button("Generate Query"):
    st.write(' The prediction of S&P Case-Schiller Home Price Index is:', predictions)

