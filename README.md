# National-Home-Price-Predictor
This ML model predicts the S&P Case-Shiller Home Price Index based on publicly available data such as population, unemployment rate, mortgage rate, and home supply rate.

# Publicly Available Factors
Population: [Download](https://fred.stlouisfed.org/series/POPTHM) <br/>
Unemployment Rate: [Download](https://fred.stlouisfed.org/series/UNRATE) <br/>
Mortgage Rate: [Download](https://fred.stlouisfed.org/series/MORTGAGE30US) <br/>
Home Supply Rate: [Download](https://fred.stlouisfed.org/series/MSACSR) <br/>
Case-Shiller Home Price Index: [Download](https://fred.stlouisfed.org/series/CSUSHPISA) <br/>


# Training
- Model is trained over 20 years of data on different factors with an accuracy of 99.9%.
- Experimented on different ML models like Linear Regression, Decision tree, Random Forest, Support Vector Regressor and selected GradientBoostingRegressor.
- Performed Hyperparameter tuning for better accuracy.

# Access online
[Cloud App](https://home-price-predictor.streamlit.app/)
# Run on your system
```bash
git clone https://github.com/Tri-nadh/National-Home-Price-Predictor
cd National-Home-Price-Predictor/app
pip install requirements.txt
python3 -m streamlit run app.py
```
