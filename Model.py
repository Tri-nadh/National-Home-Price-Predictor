#imports
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
from sklearn.ensemble import GradientBoostingRegressor
from sklearn.model_selection import train_test_split
import numpy as np
import pandas as pd

#Get data
data = pd.read_csv('Data.csv')
data.head()

#Represents Labels and values
X = data[['Population', 'Unirate', 'Supply']]
y = data['Index']

#Split the data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)

#Predict the values
gbr = GradientBoostingRegressor(n_estimators=400, learning_rate=0.1, max_depth=3)
gbr.fit(X_train,y_train)
pred = gbr.predict(X_test)

#Get the score
#Mean squared Errror
mse = np.sqrt(mean_squared_error(y_test,pred))
print(f'Mean error: {mse:3.3} ({mse/np.mean(pred)*100:3.3}%)')
#Accuracy
score = gbr.score(X_train,y_train)
print('Model determination: ', score)

#Save the model
import joblib
joblib.dump(gbr, 'predictor.pkl')
print('Model is saved as predictor.pkl')