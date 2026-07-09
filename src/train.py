import pandas as pd, numpy as np, joblib
from sklearn import linear_model

df = pd.read_csv("data/raw/sensor_data.csv", dtype= np.float16)

X = np.array(df[["Sensor_A", "Sensor_B", "Humidity", "Pressure", "time"]], dtype=np.float16)
Y = np.array(df["True_Temperature"], dtype= np.float16)



linear_reg = linear_model.LinearRegression()

linear_reg.fit(X, Y)

joblib.dump(linear_reg, "models/model1.pkl")