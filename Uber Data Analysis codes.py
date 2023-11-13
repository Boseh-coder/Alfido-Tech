# Import python libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
uber_data = pd.read_csv('C:/Users/USER/Desktop/Alfido Tech Internship/UberDataset.csv')
print(uber_data.head())

print(uber_data.info())

print(uber_data.describe())

# data cleaning
print("Missing values before dropping:", uber_data.isnull().sum())
uber_data = uber_data.dropna()
print("Missing values after dropping:", uber_data.isnull().sum())
print(uber_data.head())

# Convert data types (datetime conversion)
uber_data['START_DATE'] = pd.to_datetime(uber_data['START_DATE'])
uber_data['END_DATE'] = pd.to_datetime(uber_data['END_DATE'])
print(uber_data.head())

# Calculate duration of rides
uber_data['Duration'] = (uber_data['END_DATE'] - uber_data['START_DATE']).dt.total_seconds() / 60  # Convert to minutes

# Plot distribution of ride durations
plt.figure(figsize=(10, 6))
sns.histplot(uber_data['Duration'], bins=30, kde=True)
plt.title('Distribution of Ride Durations')
plt.xlabel('Duration (minutes)')
plt.ylabel('Frequency')
plt.show()

# Plot distribution of ride purposes
plt.figure(figsize=(12, 6))
sns.countplot(x='PURPOSE', data=uber_data, order=uber_data['PURPOSE'].value_counts().index)
plt.title('Distribution of Ride Purposes')
plt.xlabel('Purpose')
plt.ylabel('Count')
plt.xticks(rotation=45, ha='right')
plt.show()

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Assuming uber_data is your DataFrame
# Convert 'START_DATE' to datetime format
uber_data['START_DATE'] = pd.to_datetime(uber_data['START_DATE'])

# Extract information about the month, day, and hour
uber_data['Month'] = uber_data['START_DATE'].dt.month
uber_data['Day'] = uber_data['START_DATE'].dt.day
uber_data['Hour'] = uber_data['START_DATE'].dt.hour

# Plot the number of rides per month
plt.figure(figsize=(12, 6))
sns.countplot(x='Month', data=uber_data)
plt.title('Number of Rides per Month')
plt.xlabel('Month')
plt.ylabel('Number of Rides')
plt.show()


# Plot the number of rides per day
plt.figure(figsize=(12, 6))
sns.countplot(x='Day', data=uber_data)
plt.title('Number of Rides per Day')
plt.xlabel('Day')
plt.ylabel('Number of Rides')
plt.show()


# Driver activity overtime

plt.figure(figsize=(15, 6))
plt.subplot(1, 2, 1)
sns.countplot(x='Hour', data=uber_data)
plt.title('Number of Rides per Hour')

plt.subplot(1, 2, 2)
sns.countplot(x='Day_of_Week', data=uber_data, order=['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'])
plt.title('Number of Rides per Day of the Week')

plt.tight_layout()
plt.show()



plt.figure(figsize=(12, 6))
sns.barplot(x='PURPOSE', y='Duration', data=uber_data)
plt.title('Average Working Hours for Each Purpose')
plt.xlabel('Purpose')
plt.ylabel('Average Working Hours (minutes)')
plt.xticks(rotation=45, ha='right')
plt.show()


import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

# Calculate total working hours per category
category_hours = uber_data.groupby('CATEGORY')['MILES'].sum()

# Calculate the average working hours per category
average_category_hours = category_hours.mean()

# Plotting
plt.figure(figsize=(10, 6))
sns.barplot(x=category_hours.index, y=category_hours.values)
plt.axhline(y=average_category_hours, color='red', linestyle='--', label='Average')
plt.title('Total Working Hours by Category')
plt.xlabel('Category')
plt.ylabel('Total Working Hours (miles)')
plt.xticks(rotation=45, ha='right')
plt.legend()
plt.show()

print(f"Average Working Hours of Categories: {average_category_hours:.2f} miles")



# Popular ride purposes
ride_purpose_counts = uber_data['PURPOSE'].value_counts()
plt.figure(figsize=(12, 6))
sns.barplot(x=ride_purpose_counts.values, y=ride_purpose_counts.index, palette='viridis')
plt.title('Ride Counts by Purpose')
plt.xlabel('Number of Rides')
plt.ylabel('Purpose')
plt.show()


# User Behavior by Distance
plt.figure(figsize=(10, 6))
sns.scatterplot(x='MILES', y='Duration', data=uber_data)
plt.title('Scatter Plot of Ride Duration vs. Distance')
plt.xlabel('Distance (miles)')
plt.ylabel('Duration (minutes)')
plt.show()


# User Behavior by Purpose and Day of the Week
plt.figure(figsize=(15, 8))
sns.countplot(x='Day_of_Week', hue='PURPOSE', data=uber_data, order=['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'])
plt.title('Ride Counts by Purpose and Day of the Week')
plt.xlabel('Day of the Week')
plt.ylabel('Number of Rides')
plt.legend(title='Purpose', bbox_to_anchor=(1.05, 1), loc='upper left')
plt.show()

# Load your dataset
uber_data = pd.read_csv('C:/Users/USER/Desktop/Alfido Tech Internship/UberDataset.csv')

start_counts = uber_data['START'].value_counts().head(10)

# Plot the top 10 starting points
plt.figure(figsize=(12, 6))
sns.barplot(x=start_counts.values, y=start_counts.index, palette='viridis')
plt.title('Top 10 Starting Points')
plt.xlabel('Number of Rides')
plt.ylabel('Starting Point')
plt.show()

# Calculate the counts of destinations
popular_destinations = uber_data['STOP'].value_counts().head(10)

# Plot the top 10 popular destinations
plt.figure(figsize=(12, 6))
sns.barplot(x=popular_destinations.values, y=popular_destinations.index, palette='viridis')
plt.title('Top 10 Popular Destinations')
plt.xlabel('Number of Rides')
plt.ylabel('Destination')
plt.show()


import seaborn as sns

# Select numeric columns for correlation analysis
numeric_columns = uber_data[['MILES', 'Duration']]

# Calculate the correlation matrix
correlation_matrix = numeric_columns.corr()

# Plot the heatmap
plt.figure(figsize=(12, 8))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt='.2f', linewidths=0.5)
plt.title('Correlation Matrix between Miles and Duration')
plt.show()
