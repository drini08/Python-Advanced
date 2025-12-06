import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


df = pd.read_csv('../lesson 15/weather_tokyo_data.csv')

df.columns = df.columns.str.strip()

df['temperature'] = pd.to_numeric(df['temperature'], errors='coerce')

df['date'] = pd.to_datetime(df['year'].astype(str) + "-" + df['day'], errors='coerce')
df['month'] = df['date'].dt.month

avg_temp = df['temperature'].mean()
print(f"\nAverage temperature for entire dataset: {avg_temp:.2f}°C")

monthly_avg = df.groupby('month')['temperature'].mean()
print("\nMonthly Average Temperature:")
pd.set_option('display.float_format', lambda x: f"{x:.2f}")
print(monthly_avg)


plt.figure(figsize=(10, 6))
bars = plt.bar(monthly_avg.index, monthly_avg.values, color='skyblue')


for bar in bars:
    yval = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2, yval + 0.3, f"{yval:.2f}",
             ha='center', va='bottom')

plt.title("Average Temperature per Month")
plt.xlabel("Month")
plt.ylabel("Average Temperature (°C)")
plt.tight_layout()
plt.show()
