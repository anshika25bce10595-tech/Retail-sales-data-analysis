import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("Sample - Superstore.csv",encoding = "latin1")

print("FIRST 5 ROWS:")
print(df.head())

print("\nDATASET INFO:")
print(df.info())

print("\nMISSING VALUES:")
print(df.isnull().sum())

total_sales = df['Sales'].sum()
print("\nTOTAL SALES:")
print(total_sales)

category_sales = df.groupby('Category')['Sales'].sum()

print("\nSALES BY CATEGORY:")
print(category_sales)

plt.figure(figsize=(8,5))
sns.barplot(x=category_sales.index, y=category_sales.values)

plt.title("Sales by Category")
plt.xlabel("Category")
plt.ylabel("Sales")

plt.show()

profit = df.groupby('Category')['Profit'].sum()

plt.figure(figsize=(8,5))
sns.barplot(x=profit.index, y=profit.values)

plt.title("Profit by Category")
plt.xlabel("Category")
plt.ylabel("Profit")

plt.show()

print("\nPROJECT COMPLETED SUCCESSFULLY!")