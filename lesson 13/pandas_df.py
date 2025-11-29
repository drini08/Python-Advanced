import pandas as pd

data = {"Name": ['Alice', 'Bob', 'Charles'],
        "Age": [25, 24 ,33],
        "City": ["Berlin", 'Frankfurt', 'Stuttgart']}

df = pd.DataFrame(data)
print(df)

