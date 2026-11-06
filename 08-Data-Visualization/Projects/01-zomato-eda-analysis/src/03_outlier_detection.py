import pandas as pd

df = pd.read_csv("08-Data-Visualization/Projects/01-zomato-eda-analysis/data/raw/zomato.csv", encoding="latin1")

# --- Outlier & Extremes Inspection ---
# Inspecting extreme values using describe percentiles or sorting
print("Top 5 Highest Votes:")
print(df[['Restaurant Name', 'Votes', 'Aggregate rating']].sort_values(by='Votes', ascending=False).head())

print("\nTop 5 Highest Average Cost for Two:")
print(df[['Restaurant Name', 'Average Cost for two', 'City']].sort_values(by='Average Cost for two', ascending=False).head())

# Checking bounds for numerical variables
print("\nNumerical Quantiles (Outlier Indicator):")
print(df[['Average Cost for two', 'Votes']].quantile([0.25, 0.50, 0.75, 0.90, 0.99]))