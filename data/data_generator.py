import random
import pandas as pd

# Create an empty list to collect synthetic sensor samples.
data = []

for i in range(1000):  # Generate 1000 synthetic data points.

    # Start with a base true temperature in a realistic range.
    true_temp = random.uniform(15, 40)

    # Simulate environmental conditions.
    humidity = random.randint(20, 90)
    pressure = random.randint(980, 1030)

    # Simulate the hour of the day.
    time = random.randint(0, 23)

    if 12 <= time <= 15:
        true_temp += 3

    # Nighttime hours lower the true temperature slightly.
    if time <= 4 or 19 <= time:
        true_temp -= 2

    # Higher humidity reduces the true temperature value.
    true_temp -= humidity * 0.02

    # Generate two sensor measurements near the true temperature.
    sensor_a = true_temp + random.uniform(-0.5, 0.5)
    sensor_b = true_temp + random.uniform(-1, 1)

    # Occasionally create an anomalous spike for sensor A.
    if random.random() < 0.02:
        sensor_a += random.uniform(8, 15)

    data.append([
        sensor_a,
        sensor_b,
        humidity,
        pressure,
        time,
        true_temp,
    ])


df = pd.DataFrame(
    data,
    columns=[               # converts `data` array to pd.DataFrame
        "Sensor_A",
        "Sensor_B",
        "Humidity",
        "Pressure",
        "time",
        "True_Temperature"
    ]
)

df.to_csv("data/raw/sensor_data.csv", index= False)  # saves DataFrame to `data/raw/sensor_data.csv` 