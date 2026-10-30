"""
===============================================================================
SEABORN NOTES - CLASS 3: ADVANCED VISUALIZATIONS & CUSTOMIZATION
===============================================================================
Topics Covered:
1. Matrix Plots (Heatmaps & Clustermaps)
2. Multi-Plot Grids (FacetGrid, PairGrid)
3. Advanced Regression Plots (lmplot vs regplot)
4. Plot Aesthetics & Styling (Themes, Palettes, Contexts)
5. Exporting Plots for Projects / GitHub
===============================================================================
"""

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns

# Set standard background theme
sns.set_theme(style="whitegrid")

# Load built-in datasets for demonstration
tips = sns.load_dataset("tips")
flights = sns.load_dataset("flights")
iris = sns.load_dataset("iris")

# =============================================================================
# 1. MATRIX PLOTS
# =============================================================================
# Matrix plots visualize data that is in a 2D grid/matrix format (e.g., correlations or pivot tables).

# --- A. HEATMAPS ---
# Frequently used to visualize correlation matrices or pivot tables.

plt.figure(figsize=(8, 6))
# Calculate numerical correlation matrix
numeric_tips = tips.select_dtypes(include=[np.number])
corr_matrix = numeric_tips.corr()

# Key parameters: annot (show values), cmap (color map), fmt (number formatting)
sns.heatmap(corr_matrix, annot=True, cmap="coolwarm", vmin=-1, vmax=1, linewidths=1)
plt.title("Correlation Heatmap - Tips Dataset")
plt.tight_layout()
plt.show()

# Heatmap using Pivot Table
flights_pivot = flights.pivot(index="month", columns="year", values="passengers")

plt.figure(figsize=(10, 6))
sns.heatmap(flights_pivot, cmap="YlGnBu", annot=True, fmt="d", cbar_kws={'label': 'Passengers'})
plt.title("Flight Passengers Across Years and Months")
plt.tight_layout()
plt.show()


# --- B. CLUSTERMAPS ---
# Uses hierarchical clustering to group similar rows and columns together.

sns.clustermap(flights_pivot, cmap="mako", standard_scale=1, figsize=(8, 8))
plt.suptitle("Clustered Heatmap - Flight Data", y=1.02)
plt.show()


# =============================================================================
# 2. MULTI-PLOT GRIDS
# =============================================================================
# Grids allow you to map plots onto subplots based on categorical variables.

# --- A. FACETGRID ---
# Creates a grid of graphs based on categories.

g = sns.FacetGrid(tips, col="time", row="smoker", hue="sex", height=3.5, aspect=1.2)
g.map(sns.scatterplot, "total_bill", "tip", alpha=0.8)
g.add_legend()
g.fig.subplots_adjust(top=0.9)
g.fig.suptitle("FacetGrid: Total Bill vs Tip grouped by Time, Smoker, and Sex")
plt.show()


# --- B. PAIRGRID ---
# Allows custom customization compared to standard sns.pairplot().

g = sns.PairGrid(iris, hue="species", corner=True)  # corner=True removes duplicate upper triangle
g.map_diag(sns.histplot, kde=True)                  # Diagonal plots
g.map_offdiag(sns.scatterplot)                      # Off-diagonal plots
g.add_legend()
g.fig.suptitle("Custom PairGrid - Iris Dataset", y=1.02)
plt.show()


# =============================================================================
# 3. ADVANCED REGRESSION PLOTS
# =============================================================================
# Compare sns.regplot (Axes-level) vs sns.lmplot (Figure-level with facet capabilities).

# --- A. regplot ---
fig, ax = plt.subplots(figsize=(7, 5))
sns.regplot(data=tips, x="total_bill", y="tip", ax=ax, color="purple", scatter_kws={'alpha': 0.6})
ax.set_title("Regression Plot using regplot")
plt.show()

# --- B. lmplot ---
# Combines regplot with FacetGrid for multi-categorical regression visualization.
sns.lmplot(
    data=tips,
    x="total_bill",
    y="tip",
    hue="smoker",
    col="time",
    row="sex",
    height=3.5,
    markers=["o", "x"]
)
plt.subplots_adjust(top=0.9)
plt.suptitle("lmplot across multiple facets")
plt.show()


# =============================================================================
# 4. PLOT AESTHETICS & STYLING
# =============================================================================

# --- A. Seaborn Contexts (Scales fonts/lines for different mediums) ---
# Options: 'paper', 'notebook' (default), 'talk', 'poster'
sns.set_context("talk")  # Larger text for presentations

plt.figure(figsize=(8, 4))
sns.boxplot(data=tips, x="day", y="total_bill", palette="Set2")
plt.title("Context Set to 'talk'")
plt.show()

# Reset context back to default for general work
sns.set_context("notebook")


# --- B. Color Palettes ---
# Categorical: 'deep', 'muted', 'bright', 'pastel', 'dark', 'colorblind'
# Sequential: 'Blues', 'Reds', 'Greens', 'crest', 'viridis'
# Diverging: 'Coolwarm', 'vlag', 'Spectral'

sns.palplot(sns.color_palette("viridis", 8))
plt.title("Viridis Palette")
plt.show()


# =============================================================================
# 5. SAVING & EXPORTING PLOTS
# =============================================================================
# How to save high-resolution figures for reports or GitHub READMEs.

plt.figure(figsize=(8, 5))
sns.violinplot(data=tips, x="day", y="total_bill", hue="sex", split=True, palette="pastel")
plt.title("Final Cleaned Plot for Export")

# Save high-res PNG (300 DPI)
plt.savefig("seaborn_class3_plot.png", dpi=300, bbox_inches="tight")
print("Plot successfully saved as 'seaborn_class3_plot.png'")

plt.close() # Close figure buffer