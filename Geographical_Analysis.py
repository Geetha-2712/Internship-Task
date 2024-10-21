import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

data = pd.read_csv('amazon_sales_data.csv')

# Sales by region or state
sales_by_region = data.groupby('ship-state')['Amount'].sum().reset_index()

# Plot geographical sales distribution
plt.figure(figsize=(10, 6))
sns.barplot(x='ship-state', y='Amount', data=sales_by_region)
plt.title('Sales by State')
plt.xlabel('State')
plt.ylabel('Total Sales')
plt.xticks(rotation=90)
plt.show()
