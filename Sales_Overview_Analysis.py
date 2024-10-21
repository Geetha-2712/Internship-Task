import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

data = pd.read_csv('amazon_sales_data.csv')

# Ensure 'Order_Date' is in datetime format
data['Date'] = pd.to_datetime(data['Date'], errors='coerce')

# Group by the actual 'Order_Date' and sum the 'Amount'
sales_over_time = data.groupby('Date').agg({'Amount': 'sum'}).reset_index()

# Plot sales trends directly by date
plt.figure(figsize=(12, 6))
sns.lineplot(x='Date', y='Amount', data=sales_over_time, marker='o')
plt.title('Sales Trends Over Time', fontsize=14)
plt.xlabel('Date', fontsize=12)
plt.ylabel('Sales Amount', fontsize=12)

# Rotate x-axis labels for better readability
plt.xticks(rotation=45)

# Adjust layout and show the plot
plt.tight_layout()
plt.show()
