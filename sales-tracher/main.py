import pandas as pd

df = pd.read_csv('sales.csv')
df['total_sales'] = df['price'] * df['quantity']

print("--- Sales Summary ---")
print(df)
print("\nTotal Revenue:", df['total_sales'].sum())