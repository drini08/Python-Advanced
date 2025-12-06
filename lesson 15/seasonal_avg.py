import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


df = pd.read_csv('../lesson 15/weather_tokyo_data.csv')

def get_seasons(month):
    if month in [12, 1, 2]:
        return "winter"
    elif month in [3, 4, 5]:
        return "spring"
    elif month in [6, 7, 8]:
        return "summer"
    elif month in [9, 10, 11]:
        return "autumn"
    else:
        return None

df['date'] = pd.to_datetime(df['year'].astype(str) + "-" + df['day'], errors='coerce')
df['month'] = df['date'].dt.month

seasonal_avg = df.groupby('month')['temperature'].mean()

pd.set_option('display.float_format', lambda x: f"{x:.2f}")
print(seasonal_avg)