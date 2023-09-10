import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
# from pandas.api.types import CategoricalDtype

# Step 1: Load the dataset
df = pd.read_csv('p1.csv')

# Step 2: Explore the dataset
print(df.head())  # Display the first few rows of data
print(df.info())  # Get data types and non-null counts

# Step 3: Data Preprocessing (Example: Convert 'order_date' to datetime)
df['order_date'] = pd.to_datetime(df['order_date'])

# Step 4: Revenue Growth Over Time (Time Series Plot)
daily_revenue = df.groupby('order_date')['revenue'].sum()

plt.figure(figsize=(12, 6))
plt.plot(daily_revenue.index, daily_revenue.values, marker='o', linestyle='-')
plt.title('Daily Revenue Over Time')
plt.xlabel('Date')
plt.ylabel('Revenue')
plt.grid(True)

# Step 5: Top-Selling Products (Bar Chart)
top_products = df.groupby('product_name')['quantity'].sum().nlargest(10)

plt.figure(figsize=(10, 6))
sns.barplot(x=top_products.values, y=top_products.index, palette='viridis')
plt.title('Top-Selling Products')
plt.xlabel('Quantity Sold')
plt.ylabel('Product Name')

# Step 6: Customer Demographics (Pie Chart - Example: Age Groups)
# age_groups = df.groupby('customer_age_group')['customer_id'].count()

plt.figure(figsize=(8, 8))
plt.pie(customer_age_group,
        labels=age_groups.index,
        autopct='%1.1f%%',
        startangle=140)
plt.title('Customer Age Group')
plt.axis(
    'equal')  # Equal aspect ratio ensures that the pie is drawn as a circle.

# Show all plots
plt.show()
