import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns 

# Download the dataset

df=pd.read_csv('Delivery_Logistics.csv')
# Display the first few rows of the dataset
print(df.head())

df['delivery_cost'] = df['delivery_cost'].round(2)

# Data cleaning and changing data types for strings
df['delivery_time_hours'] = df['delivery_time_hours'].astype(str)
df['expected_time_hours'] = df['expected_time_hours'].astype(str)

# Extract numeric values and convert to integers
df['delivery_time_hours'] = df['delivery_time_hours'].str.extract(r'(\d+)$').astype(int)
df['expected_time_hours'] = df['expected_time_hours'].str.extract(r'(\d+)$').astype(int)


print(df['delivery_time_hours'].dtype)
print(df['delivery_time_hours'].head(10))

df.to_csv("Delivery_Logistics_clean.csv", index=False) # Save the cleaned dataset

# Bascic information about the dataset

print('\n' +'='*60)
print('BASIC INFORMATION')   # title
print('='*60)

print(f'Dataset dimensions: {df.shape}')  # display dimensions of the dataset
print(f'Number of rows:{df.shape[0]}')    # display number of rows
print(f'Number of columns:{df.shape[1]}')  # display number of columns

# Preview the data

print('\n' +'='*60)
print('DATA PREVIEW')
print('='*60)

print('First 5 delivery:')
print(df.head())
print('Last 5 delivery:')
print(df.tail())

# Data types

print('\n' +'='*60)
print('DATA TYPES')
print('='*60)

print(f'\n{df.info()}')

# Numerical statistics

print('\n' +'='*60)
print('NUMERICAL STATISTICS')
print('='*60)

print(f'\n {df.describe()}')

numeric_columns=df.select_dtypes(include='number').columns # returns column names
if len(numeric_columns)>0:
    print('Statistics for numerical features:')
    print(df[numeric_columns].describe()) # shows columns with names and mathematical calculations!
else:
    print('No numerical features in the data.')
#print(numeric_columns)

# Categorical statistics

print('\n' +'='*60) 
print('CATEGORICAL STATISTICS')
print('='*60)

categorical_columns=df.select_dtypes(include='object').columns
if len (categorical_columns)>0:
    for column in categorical_columns:
        print(f'\n Column: {column}')   # display column name
        print(f'Unique values: {df[column].unique()}')  # display unique values in the column
        print(f'Number of unique values:{len(df[column].unique())}') # display number of unique values
        print('3 most frequent values:')   
        print(df[column].value_counts().head(3))  # display 3 most frequent values
        percentages=(df[column].value_counts(normalize=True).head(3) * 100).round(2)    # percentage representation
        print(percentages.astype(str) + '%')
else:
    print('No categorical columns in the data.')

# Missing values analysis

print('\n' +'='*60)
print('MISSING VALUES ANALYSIS')
print('='*60)

missing_values=df.isnull().sum()
#print(missing_values)

if missing_values.sum() > 0:
    print('Missing values in columns:')
    for column in df.columns:
        missing = df[column].isnull().sum()    # number of missing values
        if missing > 0:
            missing_percentage = missing / len(df) * 100   # percentage of missing values
            print(f'Column: {column} - Missing values: {missing} ({missing_percentage:.2f}%)') # display missing values info
else:
    print('No missing values in the dataset.')

# Visualizations

print('\n' +'='*60)
print('VISUALIZATIONS')
print('='*60)

# Bar chart for delivery partner ratings

if 'delivery_partner' in df.columns: 

    counts = df['delivery_partner'].value_counts().sort_values(ascending=True)  # count occurrences of each delivery partner
    colors = plt.cm.tab20(np.linspace(0, 1, len(counts))) # color palette
    
    plt.figure(figsize=(9,4))             # set figure size

    bars = plt.barh(counts.index, counts.values, color=colors)  # create horizontal bar chart
    for bar, value in zip(bars, counts.values):   
        plt.text(value + 10,
            bar.get_y() + bar.get_height() / 2, # add text labels to bars
            str(value),                         # label value
            va='center')                        # vertical alignment
    plt.tight_layout()                          # adjust layout
    plt.show()  # display the plot

# Bar chart of package types delivered

if 'package_type' in df.columns:
    
    counts = df['package_type'].value_counts() # count occurrences of each package type
                
    plt.figure(figsize=(10,6))   # figure size
    plt.bar(counts.index, counts.values, color='skyblue', edgecolor='black') # bar chart
    plt.title('Types of packages delivered', fontsize=16, fontweight='bold', color='navy') # title
    plt.xlabel('Package type')  # x-axis
    plt.ylabel('Count')         # y-axis
    plt.xticks(rotation=45, ha='right', color='purple') # rotate x-axis labels
    plt.tight_layout()                # adjust layout
    plt.show()
    
# Box plot of delivery delays by region

if 'region' in df.columns and 'delivery_time_hours' in df.columns and 'expected_time_hours' in df.columns:
    df['delay'] = df['delivery_time_hours'] - df['expected_time_hours']

    plt.figure(figsize=(10,6))
    sns.boxplot(data=df, x='region', y='delay', palette='Set2')

    plt.title('Delivery Delays by Region', fontsize=16, fontweight='bold')
    plt.xlabel('Region')
    plt.ylabel('Delay (hours)')

    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

# Pie chart of delivery status

if 'delivery_status' in df.columns:
    status_counts = df['delivery_status'].value_counts()
    
    colors=[]
    for label in status_counts.index:
        if label== 'failed':
            colors.append('red')
        elif label=='delivered':
            colors.append('lightgreen')
        else:
            colors.append('yellow')
            
    plt.figure(figsize=(8,8))
    plt.pie(status_counts.values, labels=status_counts.index, autopct='%1.2f%%', startangle=140, colors=colors)
    plt.title('Delivery Status Distribution', fontsize=16, fontweight='bold')
    plt.xticks(rotation=45, ha='right')
    plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
    plt.show()
    
# Line plot of average delivery ratings by partner

if 'delivery_partner' in df.columns and 'delivery_rating' in df.columns:
    
    partner_ratings=df.groupby('delivery_partner')['delivery_rating'].mean().sort_values(ascending=False)
    
    plt.figure(figsize=(10,6))
    plt.plot(partner_ratings.index, partner_ratings.values, marker='o',linewidth=2, color='navy')
    plt.title('Average Delivery Ratings by Partner', fontsize=16, fontweight='bold')
    plt.xlabel('Delivery Partner')
    plt.ylabel('Average Rating')
    plt.xticks(rotation=45, ha='right')
    plt.grid(linestyle= '--', alpha=0.3)
    
        
    plt.tight_layout()
    plt.show()
    
# Histogram of delivery costs, package weight and distance

if 'delivery_cost' in df.columns and 'package_weight_kg' in df.columns and 'distance_km' in df.columns:
    
    df_head=df.head(10)
    plt.figure(figsize=(15,5))

    # Delivery Cost 
    plt.subplot(1,3,1)
    plt.hist(df['delivery_cost'], bins=10, color='lavender', edgecolor='black')
    plt.title('Delivery Cost', fontsize=12, fontweight='bold')
    plt.xlabel('Delivery Cost ($)')
    plt.ylabel('Frequency')
    plt.grid(alpha=0.3)
    
    # Package Weight 
    plt.subplot(1,3,2)
    plt.hist(df['package_weight_kg'], bins=10, color='pink', edgecolor='black')
    plt.title('Package Weight', fontsize=12, fontweight='bold')
    plt.xlabel('Package weight (kg)')
    plt.ylabel('Frequency')
    plt.grid(alpha=0.3)
    
    # Distance
    plt.subplot(1,3,3)
    plt.hist(df['distance_km'], bins=10, color='salmon', edgecolor='black')
    plt.title('Distance', fontsize=12, fontweight='bold')
    plt.xlabel('Distance (km)')
    plt.ylabel('Frequency')
    plt.grid(alpha=0.3)
    
    plt.tight_layout()
    plt.show()

# Scatter plot of delivery cost vs. distance

if 'delivery_cost' in df.columns and 'distance_km' in df.columns:
    df['distance_bin'] = pd.cut(df['distance_km'], bins=10)

    # Calculate mean delivery cost for each distance bin
    mean_cost = df.groupby('distance_bin')['delivery_cost'].mean()

    plt.figure(figsize=(10,5))
    plt.plot(mean_cost.index.astype(str), mean_cost.values, marker='o',linestyle='-', linewidth=2,color='navy')
    plt.title('Average delivery cost depending on distance', fontsize=14, fontweight='bold')
    plt.xlabel('distance (km)')
    plt.ylabel('delivery cost ($)')
    plt.grid(alpha=0.3)
    plt.xticks(rotation=45)

    plt.tight_layout()
    plt.show()