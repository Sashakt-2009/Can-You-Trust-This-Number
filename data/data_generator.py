import random 
import pandas as pd 

data = []

for i in range(1000):
    true_temp = random.uniform(15, 40)

    humidity = random.randint(20, 90)
    pressure = random.randint(980, 1030)

    time = random.randint(0,23)

    if 12 <= time <= 15:
        true_temp += 3

    if time <= 4 | 19 <= time:
        true_temp -= 2

    true_temp -= humidity * 0.02

    sensor_a = true_temp + random.uniform(-0.5, 0.5)
    sensor_b = true_temp + random.uniform(-1, 1)

    if random.random() < 0.02:
        sensor_a += random.uniform(8, 15)

    data.append([
        sensor_a,
        sensor_b,
        humidity,
        pressure,
        time,
        true_temp
    ])


df = pd.DataFrame(
    data,
    columns=[
        "Sensor_A",
        "Sensor_B",
        "Humidity",
        "Pressure",
        "time",
        "True_Temperature"
    ]
)

df.to_csv("data/raw/sensor_data.csv", index= False)