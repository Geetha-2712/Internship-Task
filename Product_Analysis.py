import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

data = pd.read_csv('amazon_sales_data.csv')

# Distribution of product categories
product_category_distribution = data['Category'].value_counts()

# Plot product category distribution
plt.figure(figsize=(10, 6))
sns.barplot(x=product_category_distribution.index, y=product_category_distribution.values)
plt.title('Distribution of Product Categories')
plt.xlabel('Product Category')
plt.ylabel('Count')
plt.xticks(rotation=90)
plt.show()

# Analyze sizes and quantities sold
size_quantity = data.groupby('Size')['Qty'].sum().reset_index()

# Plot quantity sold by size
plt.figure(figsize=(10, 6))
sns.barplot(x='Size', y='Quantity', data=size_quantity)
plt.title('Quantity Sold by Size')
plt.xlabel('Size')
plt.ylabel('Total Quantity Sold')
plt.show()
