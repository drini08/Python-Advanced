import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


df = pd.read_csv('../lesson 15/weather_tokyo_data.csv')


hottest = df[df['temperature']==df['temperature'].max()]
coldest = df[df['temperature']==df['temperature'].min()]

print("Hottest Day:")
print(hottest)

print("Coldest Day:")
print(coldest)