#Mini Project – Retail Sales Dashboard Using CSV and Matplotlib

# Retail Sales Dashboard

import pandas as pd
import matplotlib.pyplot as plt

# Creating Sales Data

data = {
    "Product": ["Laptop", "Mobile", "Tablet", "Headphones"],
    "Sales": [50000, 30000, 20000, 10000]
}

df = pd.DataFrame(data)

# Save Data into CSV

df.to_csv("sales.csv", index=False)

# Read CSV File

sales_data = pd.read_csv("sales.csv")

print("--- RETAIL SALES DATA ---")
print(sales_data)

# Calculate Total and Average Sales

total = sales_data["Sales"].sum()
average = sales_data["Sales"].mean()

print("\nTotal Sales:", total)
print("Average Sales:", average)

# Find Highest Selling Product

highest = sales_data.loc[
    sales_data["Sales"].idxmax()
]

print("Highest Selling Product:", highest["Product"])
print("Highest Sales:", highest["Sales"])

# Create Bar Chart

plt.bar(
    sales_data["Product"],
    sales_data["Sales"]
)

plt.title("Retail Sales Dashboard")
plt.xlabel("Products")
plt.ylabel("Sales Amount")

plt.show()

# Create Pie Chart

plt.pie(
    sales_data["Sales"],
    labels=sales_data["Product"],
    autopct="%1.1f%%"
)

plt.title("Product Sales Distribution")

plt.show()