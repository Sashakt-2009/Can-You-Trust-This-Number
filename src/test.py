import pandas as pd
import numpy as np
import joblib
from sklearn.metrics import mean_squared_error, r2_score

# Load the test dataset.
df = pd.read_csv("data/raw/sensor_testdata.csv")

# Separate features and true target values.
x = np.array(df[["Sensor_A", "Sensor_B", "Humidity", "Pressure", "time"]])
y = np.array(df["True_Temperature"])

# Load the saved trained model.
model = joblib.load("models/model1.pkl")

# Make predictions on the test features.
Y = model.predict(x)

# Print evaluation metrics for model performance.
print(f"mean squared error: {mean_squared_error(y, Y)}")
print(f"r^2 score: {r2_score(y, Y)}")