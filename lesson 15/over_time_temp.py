import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


df = pd.read_csv('../lesson 15/weather_tokyo_data.csv')

df['temperature'] = pd.to_numeric(df['temperature'], errors='coerce')
over_time = df.groupby('year')['temperature'].mean()

plt.figure(figsize=(10,6))

over_time.plot(kind="line", marker="o", color='green')

plt.title("Temperature Change Over Time")

plt.xlabel("year")
plt.ylabel("temperature")

plt.grid(axis='both', linestyle='--', alpha=0.7)

plt.show()