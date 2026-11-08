import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("08-Data-Visualization/Projects/01-zomato-eda-analysis/data/raw/zomato.csv", encoding="latin1")

# --- Figure 1: Missing Values Bar Chart ---
missing_values = df.isnull().sum()
missing_values = missing_values[missing_values > 0]

if not missing_values.empty:
    plt.figure(figsize=(8, 5))
    missing_values.plot(kind="bar")
    plt.title("Missing Values per Column")
    plt.xlabel("Column")
    plt.ylabel("Missing Count")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

# --- Figure 2: Distribution of Aggregate Rating (Histogram) ---
plt.figure(figsize=(8, 5))
plt.hist(df["Aggregate rating"], bins=20, edgecolor='black')
plt.title("Distribution of Aggregate Rating")
plt.xlabel("Rating")
plt.ylabel("Number of Restaurants")
plt.tight_layout()
plt.show()

# --- Figure 3: Frequency Distribution of Rating Text (Bar Chart) ---
plt.figure(figsize=(8, 5))
df["Rating text"].value_counts().plot(kind="bar", color='skyblue', edgecolor='black')
plt.title("Frequency Distribution of Rating Text")
plt.xlabel("Rating Category")
plt.ylabel("Number of Restaurants")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# --- Figure 4: Box Plot for Votes ---
plt.figure(figsize=(6, 5))
plt.boxplot(df["Votes"])
plt.title("Box Plot: Votes")
plt.ylabel("Number of Votes")
plt.tight_layout()
plt.show()

# --- Figure 5: Box Plot for Average Cost for Two ---
plt.figure(figsize=(6, 5))
plt.boxplot(df["Average Cost for two"])
plt.title("Box Plot: Average Cost for Two")
plt.ylabel("Cost")
plt.tight_layout()
plt.show()