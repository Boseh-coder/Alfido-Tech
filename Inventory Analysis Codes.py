# Import Libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


# Loading datasets
purchase_prices_df = pd.read_csv("C:/Users/USER/Desktop/Alfido Tech Internship/2017PurchasePricesDec.csv")
beg_inv_df  = pd.read_csv("C:/Users/USER/Desktop/Alfido Tech Internship/BegInvFINAL12312016.csv")
end_inv_df  = pd.read_csv("C:/Users/USER/Desktop/Alfido Tech Internship/EndInvFINAL12312016.csv")
invoice_df = pd.read_csv("C:/Users/USER/Desktop/Alfido Tech Internship/InvoicePurchases12312016.csv")
purchases_df = pd.read_csv("C:/Users/USER/Desktop/Alfido Tech Internship/PurchasesFINAL12312016.csv")
sales_df = pd.read_csv("C:/Users/USER/Desktop/Alfido Tech Internship/SalesFINAL12312016.csv")



from IPython.display import display

# Display each DataFrame in a table
print("Purchase Prices Data:")
display(purchase_prices_df.head())

print("Beginning Inventory Data:")
display(beg_inv_df.head())

print("End Inventory Data:")
display(end_inv_df.head())

print("Invoice Purchases Data:")
display(invoice_df.head())

print("Purchases Data:")
display(purchases_df.head())

print("Sales Data:")
display(sales_df.head())


# Checking for missing data in each dataset
datasets = [purchase_prices_df, beg_inv_df, end_inv_df, invoice_df, purchases_df, sales_df]
dataset_names = ["purchase_prices_df", "beg_inv_df", "end_inv_df", "invoice_df", "purchases_df", "sales_df"]

for name, data in zip(dataset_names, datasets):
    missing_values = data.isnull().sum()
    non_zero_missing_values = missing_values[missing_values > 0]

    if not non_zero_missing_values.empty:
        print(f"\nMissing values in {name}:")
        print(non_zero_missing_values)



        # Handling missing values for purchase_prices dataset
      cols_to_check = ['Description', 'Size', 'Volume']
      for col in cols_to_check:
          purchase_prices_df = purchase_prices_df[purchase_prices_df[col].notna()]

      # Handling missing values for end_inv dataset
      if end_inv_df['Store'].nunique() == end_inv_df['City'].nunique():
          city_store_mapping = end_inv_df[['Store', 'City']].drop_duplicates().set_index('Store').to_dict()['City']
          end_inv_df['City'] = end_inv_df['City'].fillna(end_inv_df['Store'].map(city_store_mapping))
      else:
          end_inv_df['City'].fillna('Unknown', inplace=True)

      # Handling missing values for invoice_purchases dataset
      invoice_df['Approval'].fillna('Pending', inplace=True)

      # Handling missing values for purchases dataset
      purchases_df = purchases_df[purchases_df['Size'].notna()]

      # Checking for missing data in each dataset
      datasets = [purchase_prices_df, beg_inv_df, end_inv_df, invoice_df, purchases_df, sales_df]
      dataset_names = ["purchase_prices_df", "beg_inv_df", "end_inv_df", "invoice_df", "purchases_df", "sales_df"]

      for name, data in zip(dataset_names, datasets):
          missing_values = data.isnull().sum()
          non_zero_missing_values = missing_values[missing_values > 0]

          if not non_zero_missing_values.empty:
              print(f"\nMissing values in {name}:")
              print(non_zero_missing_values)
          else:
              print(f"\nNo missing values in {name}.")


    # Explore unique values and data types of each column
    print("\nData Types and Unique Values:")
    datasets = [purchase_prices_df, beg_inv_df, end_inv_df, invoice_df, purchases_df, sales_df]
    dataset_names = ["purchase_prices_df", "beg_inv_df", "end_inv_df", "invoice_df", "purchases_df", "sales_df"]

    for name, data in zip(dataset_names, datasets):
    data_info = data.info()
    print(f"\nData Types and Unique Values in {name}:")
    print(data_info)


# Display basic statistics of numerical columns for purchase_prices_df
print("Basic Statistics:")
print(purchase_prices_df.describe())

# Display basic statistics for other datasets
datasets = [beg_inv_df, end_inv_df, invoice_df, purchases_df, sales_df]
dataset_names = ["beg_inv_df", "end_inv_df", "invoice_df", "purchases_df", "sales_df"]

for name, data in zip(dataset_names, datasets):
    if data.select_dtypes(include='number').columns.any():  # Check if there are numerical columns
        print(f"\nBasic Statistics for {name}:")
        print(data.describe())
    else:
        print(f"\nNo numerical columns in {name}.")


        import pandas as pd
        import matplotlib.pyplot as plt

        sales_data = {
            'Classification': ['Raw Materials', 'Work-in-Progress', 'Finished Goods'] * 10,
            'Volume': [100, 300, 1200] * 10,
            'SalesQuantity': [50, 200, 800] * 10
        }

        # Create a sample sales_df dataframe
        sales_df = pd.DataFrame(sales_data)


        # 1. Assess Current Inventory Levels
        avg_inventory = sales_df.groupby('Classification')['Volume'].mean()
        min_inventory = sales_df.groupby('Classification')['Volume'].min()
        max_inventory = sales_df.groupby('Classification')['Volume'].max()

        plt.figure(figsize=(10, 6))
        avg_inventory.plot(kind='bar', color='blue', label='Average')
        min_inventory.plot(kind='bar', color='green', label='Minimum')
        max_inventory.plot(kind='bar', color='orange', label='Maximum')
        plt.title('Current Inventory Levels by Category')
        plt.xlabel('Category')
        plt.ylabel('Volume')
        plt.legend()
        plt.show()


        # 2. Analyze Inventory Turnover Ratios
        inventory_turnover = sales_df.groupby('Classification')['SalesQuantity'].sum() / sales_df.groupby('Classification')['Volume'].mean()

        plt.figure(figsize=(8, 8))
        plt.pie(inventory_turnover, labels=inventory_turnover.index, autopct='%1.1f%%', startangle=90)
        plt.title('Distribution of Inventory Turnover Ratios')
        plt.show()


        # Evaluate Carrying Costs
        sales_df['StorageCost'] = sales_df['SalesQuantity'] * 0.02
        sales_df['InsuranceCost'] = sales_df['SalesQuantity'] * 0.01
        sales_df['OtherCost'] = 50

        carrying_costs = sales_df.groupby('Classification')[['StorageCost', 'InsuranceCost', 'OtherCost']].sum()

        plt.figure(figsize=(10, 6))
        carrying_costs.plot(kind='bar', stacked=True)
        plt.title('Components of Carrying Costs by Category')
        plt.xlabel('Category')
        plt.ylabel('Cost')
        plt.legend(title='Cost Component')
        plt.show()

        # Assuming 'SalesDate' is in datetime format
      sales_df['SalesDate'] = pd.to_datetime(sales_df['SalesDate'])

      # Set 'SalesDate' as the index for time series analysis
      sales_df.set_index('SalesDate', inplace=True)

      # Plotting the time series data
      plt.figure(figsize=(12, 6))
      sales_df.resample('M')['SalesQuantity'].sum().plot(marker='o', color='green')
      plt.title('Monthly Distribution of Sales')
      plt.xlabel('Date')
      plt.ylabel('Total Sales Quantity')
      plt.grid(True)
      plt.show()


      category_column = 'Volume'

      # Total sales quantity for each category
      total_sales_by_category = sales_df.groupby(category_column)['SalesQuantity'].sum()

      # Plotting the sales quantities by category
      plt.figure(figsize=(10, 6))
      total_sales_by_category.plot(kind='bar', color='skyblue')
      plt.title('Total Sales Quantity by Category')
      plt.xlabel('Category')
      plt.ylabel('Total Sales Quantity')
      plt.show()


      category_column = 'Volume'

      # Average sales quantity for each category
      average_sales_by_category = sales_df.groupby(category_column)['SalesQuantity'].mean()

      # Plotting the average sales quantities by category
      plt.figure(figsize=(10, 6))
      average_sales_by_category.plot(kind='bar', color='skyblue')
      plt.title('Average Sales Quantity by Category')
      plt.xlabel('Category')
      plt.ylabel('Average Sales Quantity')
      plt.show()
      import matplotlib.pyplot as plt
      import seaborn as sns


      # 'VendorName'
    top_vendors_sales = sales_df.groupby('VendorName')['SalesQuantity'].sum().sort_values(ascending=False).head(10)

    # Plotting the sales for the top 10 vendors
    plt.figure(figsize=(12, 6))
    top_vendors_sales.plot(kind='bar', color='purple')
    plt.title('Sales by Top 10 Vendors')
    plt.xlabel('Vendor Name')
    plt.ylabel('Total Sales Quantity')
    plt.show()

    import matplotlib.pyplot as plt

    # Convert 'InvoiceDate' to datetime format
    invoice_df['InvoiceDate'] = pd.to_datetime(invoice_df['InvoiceDate'])

    # Plot the monthly distribution of purchases
    plt.figure(figsize=(12, 6))
    invoice_df.resample('M', on='InvoiceDate')['Dollars'].sum().plot(marker='o')
    plt.title('Monthly Distribution of Purchases')
    plt.xlabel('Date')
    plt.ylabel('Total Dollars Spent')
    plt.grid(True)
    plt.show()


    # Evaluate vendor performance based on total dollars spent
    vendor_performance = invoice_df.groupby('VendorName')['Dollars'].sum().sort_values(ascending=False)

    plt.figure(figsize=(10, 6))
    vendor_performance.head(10).plot(kind='bar', color='skyblue')
    plt.title('Top 10 Vendors by Dollar Spent')
    plt.xlabel('Vendor')
    plt.ylabel('Dollar Spent')
    plt.show()


    # Assuming you have a DataFrame named 'purchases_df' with relevant columns
    top_vendors = purchases_df.groupby('VendorName')['Dollars'].sum().sort_values(ascending=False).head(10)

    # Pie chart for distribution of purchase costs among the top vendors
    plt.figure(figsize=(10, 6))
    top_vendors.plot(kind='pie', autopct='%1.1f%%', startangle=140)
    plt.title('Distribution of Purchase Costs Among Top Vendors')
    plt.ylabel('')  # to remove the default 'Dollars' label from the y-axis
    plt.show()


    import numpy as np

    # Calculate EOQ for each product
    invoice_df['EOQ'] = np.sqrt((2 * 1000 * invoice_df['Dollars']) / purchase_prices_df['PurchasePrice'])

    # Visualize the EOQ distribution
    plt.figure(figsize=(12, 6))
    plt.scatter(invoice_df['Quantity'], invoice_df['EOQ'], alpha=0.5)
    plt.title('EOQ Analysis for Raw Materials')
    plt.xlabel('Quantity Purchased')
    plt.ylabel('Economic Order Quantity (EOQ)')
    plt.grid(True)
    plt.show()


    # Analyze top-performing products based on sales quantity
    top_products = sales_df.groupby('Description')['SalesQuantity'].sum().sort_values(ascending=False).head(10)
    print("Top 10 Products by Sales Quantity:\n", top_products)

    # Analyze top vendors by purchase volume
    vendor_purchase_volume = purchases_df.groupby('VendorName')['Quantity'].sum().sort_values(ascending=False).head(10)
    print("\nTop 10 Vendors by Purchase Volume:\n", vendor_purchase_volume)

    # Visualize the distribution of sales quantities for different product classifications
    plt.figure(figsize=(12, 6))
    sns.boxplot(x='Classification', y='SalesQuantity', data=sales_df)
    plt.title('Distribution of Sales Quantities by Product Classification')
    plt.xlabel('Product Classification')
    plt.ylabel('Sales Quantity')
    plt.show()


    import matplotlib.pyplot as plt
    import seaborn as sns

    # Group by product and sum the sales quantity
    top_selling_products = sales_df.groupby('Description')['SalesQuantity'].sum().sort_values(ascending=False)

    # Display the top-selling products
    print("Top Selling Products:")
    print(top_selling_products.head(10))

    # Visualize the distribution of sales quantity
    plt.figure(figsize=(12, 6))
    sns.barplot(x=top_selling_products.head(10).index, y=top_selling_products.head(10).values)
    plt.title('Top Selling Products by Sales Quantity')
    plt.xlabel('Product Description')
    plt.ylabel('Total Sales Quantity')
    plt.xticks(rotation=45, ha='right')
    plt.show()


    vendor_product_count = sales_df.groupby('VendorName')['Description'].nunique().sort_values(ascending=False)

    # Display the number of unique products sourced from each vendor
    print("Number of Products Sourced from Each Vendor:")
    print(vendor_product_count)
