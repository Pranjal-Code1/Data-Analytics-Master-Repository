"""
# Seaborn – Class 4: Regression & Mixed Plots

## Regression & Mixed Plots
Seaborn provides plots that combine **relationships** and **statistical models** or mix multiple plot types.

- regplot() / lmplot() → scatter + regression line  
- jointplot() → scatter with hist/KDE  
- pairplot() → multiple relationships in one go
"""

import matplotlib.pyplot as plt
import seaborn as sns

# Load sample dataset
tips = sns.load_dataset("tips")

# ==========================================
# 1. regplot() – Scatter + Regression Line
# ==========================================
print("Generating regplot...")
plt.figure(figsize=(8, 6))
sns.regplot(x="total_bill", y="tip", data=tips, color="green")
plt.title("regplot(): Bill vs Tip with Regression Line")
plt.show()


# ==========================================
# 2. lmplot() – Regression with Facets
# ==========================================
print("Generating lmplot...")
# lmplot is similar to regplot but creates its own figure grid and supports grouping/faceting
sns.lmplot(
    x="total_bill", y="tip", hue="sex", data=tips, height=5, aspect=1.2
)
plt.title("lmplot(): Regression by Gender")
plt.show()


# ==========================================
# 3. jointplot() – Scatter + Histogram / KDE
# ==========================================
print("Generating jointplot...")
# jointplot combines bivariate scatter plots with univariate marginal distributions
sns.jointplot(x="total_bill", y="tip", data=tips, kind="scatter", color="purple")
plt.show()


# ==========================================
# 4. pairplot() – Relationships Between Many Variables
# ==========================================
print("Generating pairplot...")
# pairplot builds a grid of pairwise relationships across the entire dataset
sns.pairplot(tips, hue="sex", palette="Set2")
plt.show()