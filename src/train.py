import pandas as pd
import numpy as np
import joblib
from sklearn import linear_model

# Load the synthetic training dataset.
df = pd.read_csv("data/raw/sensor_data.csv", dtype=np.float16)

# Select feature columns and target column.
X = np.array(
    df[["Sensor_A", "Sensor_B", "Humidity", "Pressure", "time"]],
    dtype=np.float16,
)
Y = np.array(df["True_Temperature"], dtype=np.float16)

# Train a linear regression model on the sensor data.
linear_reg = linear_model.LinearRegression()
linear_reg.fit(X, Y)

# Save the trained model so it can be loaded later.
joblib.dump(linear_reg, "models/model1.pkl")