import pandas as pd

# Load the dataset
df = pd.read_csv("08-Data-Visualization/Projects/01-zomato-eda-analysis/data/raw/zomato.csv", encoding="latin1")
print("Dataset loaded successfully!")

# Show the first 5 rows
print(df.head())

# Dataset dimensions and columns
print("Rows:", df.shape[0])
print("Columns:", df.shape[1])
print("\nColumn Names:")
for column in df.columns:
    print(column)

# Data types of each column
print("\nData Types:")
print(df.dtypes)

# Detailed info — memory usage, non-null counts
print("\nDataFrame Info:")
df.info()

# Statistical summary of numerical columns
print("\nStatistical Summary:")
print(df.describe())

# Get numerical and categorical columns
numerical_cols = df.select_dtypes(include="number").columns
categorical_cols = df.select_dtypes(include="object").columns

print("Numerical Columns:")
print(numerical_cols)
print("\nCategorical Columns:")
print(categorical_cols)

# --- Data Quality Assessment ---
missing_values = df.isnull().sum()
print("\nMissing Values per Column:")
print(missing_values)

# Check duplicate rows
duplicates = df.duplicated().sum()
print("Duplicate Rows:", duplicates)

# Fill missing values in the Cuisines column with "Unknown"
print("Missing Cuisines before fill:", df["Cuisines"].isnull().sum())
df["Cuisines"] = df["Cuisines"].fillna("Unknown")
print("Missing values in Cuisines filled with 'Unknown'")

# Check for inconsistent values in Yes/No columns
for col in ['Has Table booking', 'Has Online delivery', 'Is delivering now']:
    print(f"{col}: {df[col].unique()}")

# Calculate data completeness
total_values = df.shape[0] * df.shape[1]
missing_values_total = df.isnull().sum().sum()
complete_values = total_values - missing_values_total
completeness = complete_values / total_values * 100

print("Data Completeness:", round(completeness, 2), "%")
print("Dataset is ready for analysis!") 