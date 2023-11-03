import joblib
import pandas as pd

loaded_model = joblib.load('predictor.pkl')

new_data = pd.DataFrame({'Population': [211531], 'Unirate': [4.0], 'Supply': [3.3]})
predictions = loaded_model.predict(new_data)

print(f'For the given Population:{new_data["Population"]} and Unemployment Rate:{new_data["Unirate"]} and Home supply Rate:{new_data["Supply"]}, the Prediction of S&P Case-Shiller Home Price Index is:{predictions}')