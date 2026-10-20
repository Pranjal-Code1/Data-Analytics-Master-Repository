import pandas as pd

# ==========================================
# MINI PRACTICE TASKS: DataFrame Basics
# ==========================================

# 1. Create a DataFrame with at least 5 rows and 4 columns (mix of numeric + text)
data = {
    "Name": ["Alice", "Bob", "Charlie", "David", "Emma"],
    "Age": [25, 30, 35, 40, 22],
    "City": ["Delhi", "Mumbai", "Pune", "Bangalore", "Chennai"],
    "Score": [85, 91, 78, 88, 95]
}

df = pd.DataFrame(data)

# 2. Show the first 3 rows, last 2 rows, and info
print("--- 1. Inspection ---")
print("First 3 rows:\n", df.head(3))
print("\nLast 2 rows:\n", df.tail(2))
print("\nInfo summary:")
print(df.info())

# 3. Select a sub-DataFrame with only 2 columns (e.g., Name and Score)
print("\n--- 2. Selection ---")
sub_df = df[["Name", "Score"]]
print(sub_df)

# 4. Rename one column, set any column as index, then reset it back
print("\n--- 3. Transformation ---")
df_renamed = df.rename(columns={"Score": "Marks"})
print("Renamed 'Score' to 'Marks':\n", df_renamed.head(2))

df_indexed = df_renamed.set_index("Name")
print("\nSet 'Name' as index:\n", df_indexed.head(2))

df_reset = df_indexed.reset_index()
print("\nReset index back to default:\n", df_reset.head(2))

# 5. Print df.shape, df.dtypes, and df.columns
print("\n--- 4. Attributes Recap ---")
print("Shape (rows, columns):", df.shape)
print("\nData types:\n", df.dtypes)
print("\nColumn names:", df.columns)