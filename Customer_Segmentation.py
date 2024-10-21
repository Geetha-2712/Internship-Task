import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler

data = pd.read_csv('amazon_sales_data.csv')

# 1. Create a summary of orders (assuming each Order ID is unique)
order_summary = data.groupby('Order ID').agg({'Amount': 'sum', 'Qty': 'sum'}).reset_index()

# 2. Standardize the features
scaler = StandardScaler()
X_scaled = scaler.fit_transform(order_summary[['Amount', 'Qty']])

# 3. K-Means Clustering
kmeans = KMeans(n_clusters=3, random_state=42)  # Adjust the number of clusters as needed
order_summary['Segment'] = kmeans.fit_predict(X_scaled)

# 4. Analyze customer segments
segment_summary = order_summary.groupby('Segment').agg({'Amount': 'mean', 'Qty': 'mean', 'Order ID': 'count'}).reset_index()
print("Customer Segments Summary:")
print(segment_summary)

# 5. Visualize the customer segments
plt.figure(figsize=(10, 6))
sns.scatterplot(x='Amount', y='Qty', hue='Segment', data=order_summary, palette='Set2')
plt.title('Customer Segmentation Based on Amount and Quantity')
plt.xlabel('Total Amount Spent')
plt.ylabel('Total Quantity Purchased')
plt.legend(title='Segment')
plt.show()

