import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler

data = pd.read_csv('amazon_sales_data.csv')

# ==============================
# 1. Sales Overview
# ==============================
total_sales = data['Amount'].sum()
total_quantity = data['Qty'].sum()
average_order_value = data['Amount'].mean()

print(f"Total Sales Amount: ${total_sales:.2f}")
print(f"Total Quantity Sold: {total_quantity}")
print(f"Average Order Value: ${average_order_value:.2f}")

# ==============================
# 2. Product Preferences
# ==============================
# Analyze sales by category
category_summary = data.groupby('Category').agg({'Amount': 'sum', 'Qty': 'sum'}).reset_index()

# Visualize total sales by category
plt.figure(figsize=(12, 6))
sns.barplot(x='Category', y='Amount', data=category_summary)
plt.title('Total Sales Amount by Category')
plt.xlabel('Category')
plt.ylabel('Total Sales Amount')
plt.xticks(rotation=45)
plt.show()

# ==============================
# 3. Customer Segmentation
# ==============================
# Create a summary of orders
order_summary = data.groupby('Order ID').agg({'Amount': 'sum', 'Qty': 'sum'}).reset_index()

# Standardize the features
scaler = StandardScaler()
X_scaled = scaler.fit_transform(order_summary[['Amount', 'Qty']])

# K-Means Clustering
kmeans = KMeans(n_clusters=3, random_state=42)  # Adjust number of clusters as needed
order_summary['Segment'] = kmeans.fit_predict(X_scaled)

# Analyze customer segments
segment_summary = order_summary.groupby('Segment').agg({'Amount': 'mean', 'Qty': 'mean', 'Order ID': 'count'}).reset_index()
print("Customer Segments Summary:")
print(segment_summary)

# Visualize customer segments
plt.figure(figsize=(10, 6))
sns.scatterplot(x='Amount', y='Qty', hue='Segment', data=order_summary, palette='Set2')
plt.title('Customer Segmentation Based on Amount and Quantity')
plt.xlabel('Total Amount Spent')
plt.ylabel('Total Quantity Purchased')
plt.legend(title='Segment')
plt.show()

# ==============================
# 4. Geographical Analysis
# ==============================
# Analyze sales by shipping city
geographical_summary = data.groupby('ship-city').agg({'Amount': 'sum', 'Qty': 'sum'}).reset_index()

# Visualize sales by city
plt.figure(figsize=(12, 6))
sns.barplot(x='ship-city', y='Amount', data=geographical_summary)
plt.title('Total Sales Amount by Shipping City')
plt.xlabel('Shipping City')
plt.ylabel('Total Sales Amount')
plt.xticks(rotation=45)
plt.show()

# ==============================
# 5. Recommendations
# ==============================
print("\nBusiness Insights and Recommendations:")
if average_order_value < 50:
    print("- Consider strategies to increase the average order value, such as upselling or bundling products.")
else:
    print("- The average order value is satisfactory; continue current sales strategies.")

if total_sales < 5000:
    print("- Total sales are below target; consider launching promotional campaigns or discounts.")
else:
    print("- Total sales are strong; consider expanding inventory to capitalize on demand.")

if segment_summary['Order ID'].max() < 20:
    print("- A limited number of orders are driving most sales; consider diversifying product offerings to attract more customers.")
else:
    print("- A healthy number of orders are contributing to sales; maintain current inventory and marketing strategies.")

# Additional insights based on product preferences
top_category = category_summary.loc[category_summary['Amount'].idxmax()]
print(f"- The top-performing category is '{top_category['Category']}' with total sales of ${top_category['Amount']:.2f}.")
print("- Consider focusing marketing efforts on this category to maximize sales.")
