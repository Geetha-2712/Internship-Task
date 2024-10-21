import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
data = pd.read_csv('amazon_sales_data.csv')


# 1. Sales Overview: Total Sales and Total Quantity
total_sales = data['Amount'].sum()
total_quantity = data['Qty'].sum()
print(f"Total Sales Amount: ${total_sales:.2f}")
print(f"Total Quantity Sold: {total_quantity}")

# 2. Sales Distribution: Visualizing the distribution of sales amounts
plt.figure(figsize=(10, 6))
sns.histplot(data['Amount'], bins=30, kde=True)
plt.title('Distribution of Sales Amounts')
plt.xlabel('Sales Amount')
plt.ylabel('Frequency')
plt.show()

# 3. Quantity Distribution: Visualizing the distribution of quantities sold
plt.figure(figsize=(10, 6))
sns.histplot(data['Qty'], bins=30, kde=True)
plt.title('Distribution of Quantities Sold')
plt.xlabel('Quantity Sold')
plt.ylabel('Frequency')
plt.show()

# 4. Top Orders: Identify the top 10 orders by amount
top_orders = data.nlargest(10, 'Amount')
plt.figure(figsize=(10, 6))
sns.barplot(x='Order ID', y='Amount', data=top_orders)
plt.title('Top 10 Orders by Sales Amount')
plt.xlabel('Order ID')
plt.ylabel('Sales Amount')
plt.xticks(rotation=45)
plt.show()

# 5. Relationship between Quantity and Amount: Scatter plot
plt.figure(figsize=(10, 6))
sns.scatterplot(x='Qty', y='Amount', data=data)
plt.title('Relationship between Quantity Sold and Sales Amount')
plt.xlabel('Quantity Sold')
plt.ylabel('Sales Amount')
plt.show()
