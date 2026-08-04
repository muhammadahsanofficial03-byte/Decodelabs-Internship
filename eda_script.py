import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# 1. Load the Evidence (Dataset)
excel_path = 'Dataset for Data Analytics (1).xlsx'
df = pd.read_excel(excel_path)

# 2. Data Forensics: Handling Missing Values
# The only missing data was in 'CouponCode'. We fill NaNs with 'NO_COUPON'.
df['CouponCode'] = df['CouponCode'].fillna('NO_COUPON')
print(f"Remaining missing values: {df.isnull().sum().sum()}")

# 3. The IQR Method: Unmasking Outliers
Q1 = df['TotalPrice'].quantile(0.25)
Q3 = df['TotalPrice'].quantile(0.75)
IQR = Q3 - Q1
lower_bound = Q1 - 1.5 * IQR
upper_bound = Q3 + 1.5 * IQR

# Filter the dataset to isolate the 'Suspects' (Outliers)
outliers = df[(df['TotalPrice'] < lower_bound) | (df['TotalPrice'] > upper_bound)]
print(f"Total Outliers Detected: {len(outliers)}")
print("\nOutlier Data Points (The Signals):")
print(outliers[['OrderID', 'Product', 'Quantity', 'TotalPrice']])

# 4. Visual Evidence: The Boxplot
# Setting a clean, minimalist style to "Cut the Noise"
sns.set_style("whitegrid")
plt.figure(figsize=(10, 4))

# Creating the boxplot and highlighting outliers in red
sns.boxplot(
    x=df['TotalPrice'], 
    color='#00d2ff', 
    flierprops={'marker': 'o', 'markerfacecolor': 'red', 'markersize': 8, 'markeredgecolor': 'black'}
)

# Adding clear, impactful headlines
plt.title('Distribution of Total Price (Highlighting 8 High-Value Outliers)', fontsize=14, fontweight='bold', pad=15)
plt.xlabel('Total Price ($)', fontsize=12)
sns.despine(left=True) # Removes border lines for a cleaner look

plt.tight_layout()
plt.show()