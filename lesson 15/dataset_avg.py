import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv('../lesson 15/weather_tokyo_data.csv')

df['temperature'] = pd.to_numeric(df['temperature'], errors='coerce')

date_temp = df.groupby('year')['temperature'].mean()

pd.set_option('display.float_format', lambda x: f"{x:.2f}")
print(date_temp)
