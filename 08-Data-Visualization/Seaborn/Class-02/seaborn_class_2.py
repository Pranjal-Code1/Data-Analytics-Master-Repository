"""
=============================================================================
Seaborn Class 2: Categorical Plots
=============================================================================
This script covers:
1. Setup & Loading Datasets
2. Estimate & Frequency Plots (barplot & countplot)
3. Quartiles & Distribution Plots (boxplot & violinplot)
4. Observation-Level Scatter Plots (stripplot & swarmplot)
5. Grouping and Categorical Variations using 'hue'
=============================================================================
"""

import matplotlib.pyplot as plt
import seaborn as sns

# -----------------------------------------------------------------------------
# 1. Setup & Load Datasets
# -----------------------------------------------------------------------------
sns.set_style("whitegrid")
sns.set_palette("deep")

tips = sns.load_dataset("tips")
print("\n--- Tips Dataset Sample ---")
print(tips.head())

# -----------------------------------------------------------------------------
# 2. Estimate & Frequency Plots (barplot & countplot)
# -----------------------------------------------------------------------------

# A. Bar Plot: Comparing average total bill by day of the week
plt.figure(figsize=(8, 5))
sns.barplot(data=tips, x="day", y="total_bill", estimator="mean", ci=None)
plt.title("Bar Plot: Average Total Bill by Day")
plt.xlabel("Day of the Week")
plt.ylabel("Average Total Bill ($)")

plt.savefig("bar_avg_total_bill_by_day.png", dpi=300, bbox_inches="tight")
plt.show()
plt.close()

# B. Count Plot: Showing frequency/count of observations per day
plt.figure(figsize=(8, 5))
sns.countplot(data=tips, x="day", hue="sex")
plt.title("Count Plot: Frequency of Tips by Day and Gender")
plt.xlabel("Day of the Week")
plt.ylabel("Count")

plt.savefig("count_tips_by_day.png", dpi=300, bbox_inches="tight")
plt.show()
plt.close()

# -----------------------------------------------------------------------------
# 3. Quartiles & Distribution Plots (boxplot & violinplot)
# -----------------------------------------------------------------------------

# A. Box Plot: Displaying median, quartiles, and outliers
plt.figure(figsize=(8, 5))
sns.boxplot(data=tips, x="day", y="total_bill", hue="smoker")
plt.title("Box Plot: Total Bill Distribution by Day and Smoker Status")
plt.xlabel("Day of the Week")
plt.ylabel("Total Bill ($)")

plt.savefig("box_total_bill_by_day.png", dpi=300, bbox_inches="tight")
plt.show()
plt.close()

# B. Violin Plot: Combining box plot statistics with KDE distribution shape
plt.figure(figsize=(8, 5))
sns.violinplot(data=tips, x="day", y="total_bill", hue="sex", split=True, inner="quart")
plt.title("Violin Plot: Total Bill Distribution Shape by Day and Gender")
plt.xlabel("Day of the Week")
plt.ylabel("Total Bill ($)")

plt.savefig("violin_total_bill_by_day.png", dpi=300, bbox_inches="tight")
plt.show()
plt.close()

# -----------------------------------------------------------------------------
# 4. Observation-Level Scatter Plots (stripplot & swarmplot)
# -----------------------------------------------------------------------------

# A. Strip Plot: Viewing every raw data point with jitter to prevent overlap
plt.figure(figsize=(8, 5))
sns.stripplot(data=tips, x="day", y="total_bill", hue="sex", dodge=True, jitter=True, alpha=0.7)
plt.title("Strip Plot: Raw Observations of Total Bill by Day")
plt.xlabel("Day of the Week")
plt.ylabel("Total Bill ($)")

plt.savefig("strip_total_bill_by_day.png", dpi=300, bbox_inches="tight")
plt.show()
plt.close()

# B. Swarm Plot: Non-overlapping categorical scatter plot showing distribution density
plt.figure(figsize=(8, 5))
sns.swarmplot(data=tips, x="day", y="tip", hue="sex", dodge=True)
plt.title("Swarm Plot: Distribution Density of Tips by Day")
plt.xlabel("Day of the Week")
plt.ylabel("Tip ($)")

plt.savefig("swarm_tips_by_day.png", dpi=300, bbox_inches="tight")
plt.show()
plt.close()

print(
    "\nAll Class 2 categorical plots have been successfully generated and saved!"
)