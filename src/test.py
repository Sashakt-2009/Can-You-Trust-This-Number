import pandas as pd, numpy as np, joblib

from sklearn.metrics import r2_score , mean_squared_error 

df = pd.read_csv("data/raw/sensor_testdata.csv")

x = np.array(df[["Sensor_A", "Sensor_B", "Humidity", "Pressure", "time"]])
y = np.array(df['True_Temperature'])

model = joblib.load("models/model1.pkl")

Y = model.predict(x)

print(f"mean squared error: {mean_squared_error(y, Y)}")
print(f" r^2 score: {r2_score(y, Y)}")