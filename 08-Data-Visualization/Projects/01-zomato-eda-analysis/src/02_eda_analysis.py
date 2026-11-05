import pandas as pd

df = pd.read_csv("08-Data-Visualization/Projects/01-zomato-eda-analysis/data/raw/zomato.csv", encoding="latin1")

# --- Univariate Analysis: Summary Stats ---
stats = df[
    [
        "Aggregate rating",
        "Votes",
        "Average Cost for two",
        "Price range"
    ]
].describe()

print("Summary Statistics:")
print(stats)

# Calculate skewness of Aggregate rating
skewness = df["Aggregate rating"].skew()
print("Skewness of Aggregate Rating:", round(skewness, 3))

# Rating text frequency distribution
rating_counts = df["Rating text"].value_counts()
print("\nRating Text Frequency:")
print(rating_counts)

# Price range distribution counts
price_range_counts = df["Price range"].value_counts().sort_index()
print("\nPrice Range Distribution:")
print(price_range_counts)