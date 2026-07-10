import pandas as pd
import numpy as np
import joblib, matplotlib.pyplot as plt
from sklearn.metrics import root_mean_squared_error, r2_score ,mean_absolute_error

# Load the test dataset.
df = pd.read_csv("data/raw/sensor_testdata.csv")

# Separate features and true target values.
x = np.array(df[["Sensor_A", "Sensor_B", "Humidity", "Pressure", "time"]])
y = np.array(df["True_Temperature"])

# Load the saved trained model.
model = joblib.load("models/model1.pkl")

# Make predictions on the test features.
y_predict = model.predict(x)

# Print evaluation metrics for model performance.
print(f"root mean squared error: {root_mean_squared_error(y, y_predict)}")
print(f"mean absloute error: {mean_absolute_error(y, y_predict)}")
print(f"r^2 score: {r2_score(y, y_predict)}")
residual = y - y_predict

# Print parameter coefficients and intercepts
print(model.coef_)
print(model.intercept_)

# Plot a graph between target value and true value
fig, ax1 = plt.subplots()
ax1.set_ylabel("True_Temperature")
ax1.set_xlabel("Predicted_Temperature")
ax1.scatter(y, y_predict)

fig, ax2 = plt.subplots()
ax2.scatter(y_predict, residual)
ax2.set_ylabel("Residuals")
ax2.set_xlabel("Predicted_Temperature")
ax2.axhline(y=0, color="red", linestyle="--")
plt.show()