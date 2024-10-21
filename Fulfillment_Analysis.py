import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

data = pd.read_csv('amazon_sales_data.csv')

# Analyze fulfillment methods
fulfillment_distribution = data['fulfilled-by'].value_counts()

# Plot fulfillment method distribution
plt.figure(figsize=(10, 6))
sns.barplot(x=fulfillment_distribution.index, y=fulfillment_distribution.values)
plt.title('Distribution of Fulfillment Methods')
plt.xlabel('Fulfillment Method')
plt.ylabel('Count')
plt.show()

# Analyze delivery times based on fulfillment methods
data['Delivery_Time'] = (data['Delivery_Date'] - data['Order_Date']).dt.days
fulfillment_delivery = data.groupby('Fulfillment_Method')['Delivery_Time'].mean().reset_index()

# Plot average delivery time by fulfillment method
plt.figure(figsize=(10, 6))
sns.barplot(x='Fulfillment_Method', y='Delivery_Time', data=fulfillment_delivery)
plt.title('Average Delivery Time by Fulfillment Method')
plt.xlabel('Fulfillment Method')
plt.ylabel('Average Delivery Time (days)')
plt.show()
