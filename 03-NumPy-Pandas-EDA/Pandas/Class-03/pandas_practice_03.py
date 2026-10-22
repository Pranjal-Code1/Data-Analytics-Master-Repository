import pandas as pd
import numpy as np

# ==========================================
# PRACTICE: Data Cleaning Essentials
# ==========================================

# 1. Create a messy DataFrame with missing values, wrong data types, typos, and duplicates
data = {
    "Name": ["Alice", "Bob", "Chrlie", "David", "Alice", None],
    "Age": ["25", "30", None, "40", "25", "30"],      # Ages stored as strings, with missing value
    "City": ["Delhi", "Mumbai", "Pun", "Bangalore", "Delhi", "Mumbai"],  # Typo: "Pun" -> "Pune"
    "Score": [85, None, 78, 88, 85, 91],              # Missing value in Score
    "Extra": ["x", "y", "z", "x", "y", "z"]           # Extra column to drop
}

df = pd.DataFrame(data)
print("Original messy DataFrame:")
print(df)
print("-" * 40)

# 2. Handle missing values
df["Age"] = pd.to_numeric(df["Age"], errors="coerce")
df["Age"] = df["Age"].fillna(df["Age"].median())
df["Score"] = df["Score"].fillna(df["Score"].mean())
df["Name"] = df["Name"].fillna("Unknown")

print("After handling missing values:")
print(df)
print("-" * 40)

# 3. Change data types
df["Age"] = df["Age"].astype(int)
df["Score"] = df["Score"].astype(float)

print("Data types after conversion:")
print(df.dtypes)
print("-" * 40)

# 4. Replace incorrect values (typos/names)
df["City"] = df["City"].replace({"Pun": "Pune"})
df["Name"] = df["Name"].replace({"Chrlie": "Charlie"})

# 5. Drop unnecessary columns
df = df.drop(columns=["Extra"])

# 6. Remove duplicates
print(f"Number of duplicate rows: {df.duplicated().sum()}")
df = df.drop_duplicates()

# 7. Final clean DataFrame output & Info check
print("-" * 40)
print("Final Clean DataFrame:")
print(df)
print("\nDataFrame Info:")
df.info()