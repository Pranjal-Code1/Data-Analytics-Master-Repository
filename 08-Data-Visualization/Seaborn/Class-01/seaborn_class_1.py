"""
=============================================================================
Seaborn Class 1: Introduction & Relational Plots
=============================================================================
This script covers:
1. Introduction & Environment Setup
2. Loading Built-in Datasets
3. Relational Plots (Scatter Plots & Line Plots) with Advanced Parameters
4. Aesthetics, Themes, and Color Palettes
5. Automatically Saving Plots as Image Files
=============================================================================
"""

import matplotlib.pyplot as plt
import seaborn as sns

# -----------------------------------------------------------------------------
# 1. Setup & Version Check
# -----------------------------------------------------------------------------
print(f"Seaborn Version: {sns.__version__}")

# -----------------------------------------------------------------------------
# 2. Loading Built-in Datasets
# -----------------------------------------------------------------------------
# Seaborn comes with built-in datasets for practicing data visualization
tips = sns.load_dataset("tips")
iris = sns.load_dataset("iris")

print("\n--- Tips Dataset Sample ---")
print(tips.head())

# -----------------------------------------------------------------------------
# 3. Relational Plots (scatterplot & lineplot)
# -----------------------------------------------------------------------------

# A. Scatter Plot: Examining the relationship between total bill and tip
plt.figure(figsize=(8, 5))
sns.scatterplot(
    data=tips,
    x="total_bill",
    y="tip",
    hue="time",  # Differentiate points by time of day (Lunch/Dinner)
    style="sex",  # Differentiate markers by gender
    size="size",  # Scale size based on party size
    sizes=(20, 200),
    palette="deep",
)
plt.title("Scatter Plot: Total Bill vs Tip (Categorized)")
plt.xlabel("Total Bill ($)")
plt.ylabel("Tip ($)")

# Save the plot automatically instead of just showing it
plt.savefig("scatter_total_bill_vs_tip.png", dpi=300, bbox_inches="tight")
plt.show()
plt.close()  # Close the figure to free memory

# B. Line Plot: Showing trends over a category (Average tip by day)
plt.figure(figsize=(8, 5))
sns.lineplot(data=tips, x="day", y="tip", estimator="mean", marker="o")
plt.title("Line Plot: Average Tip by Day")
plt.xlabel("Day of the Week")
plt.ylabel("Average Tip ($)")

plt.savefig("line_avg_tip_by_day.png", dpi=300, bbox_inches="tight")
plt.show()
plt.close()

# -----------------------------------------------------------------------------
# 4. Styling & Custom Themes
# -----------------------------------------------------------------------------
# Available themes: 'darkgrid', 'whitegrid', 'dark', 'white', 'ticks'
sns.set_style("whitegrid")

# Available color palettes: 'deep', 'muted', 'pastel', 'bright', 'dark', 'colorblind'
sns.set_palette("muted")

plt.figure(figsize=(8, 5))
sns.scatterplot(data=iris, x="sepal_length", y="sepal_width", hue="species")
plt.title("Iris Dataset: Sepal Length vs Sepal Width (Styled)")
plt.xlabel("Sepal Length")
plt.ylabel("Sepal Width")

plt.savefig("styled_iris_scatter.png", dpi=300, bbox_inches="tight")
plt.show()
plt.close()

print(
    "\nAll plots have been successfully generated and saved to your directory!"
)