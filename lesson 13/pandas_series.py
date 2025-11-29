import pandas as pd

products = ['Apples', 'Bananas', 'Grapes', 'Lunchly Boxes', '67 Nuts']

sales = [150, 180, 120, 200, 320]

sales_series = pd.Series(sales, index=products)
print(sales_series)

print(sales_series['Grapes'])

total_sales = sales_series.sum()
print(total_sales)

best_seller = sales_series.idxmax()
print(f"Best Selling Product: {best_seller}!")

worst_seller = sales_series.idxmin()
print(f"Worst Selling Product: {worst_seller}!")