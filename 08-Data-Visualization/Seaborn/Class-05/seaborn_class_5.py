"""
===============================================================================
SEABORN NOTES - CLASS 5 & 6: MATRIX/GRID PLOTS + STYLING
===============================================================================
Topics Covered:
1. Matrix & Grid Plots
   - Heatmaps (sns.heatmap)
   - Cluster Maps (sns.clustermap)
2. Customizing Aesthetics & Themes
   - Plot Styles (set_style)
   - Color Palettes (set_palette / custom palettes)
   - Scaling Contexts (set_context)
===============================================================================
"""

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns

# Load built-in sample datasets
tips = sns.load_dataset("tips")
flights = sns.load_dataset("flights")

# =============================================================================
# 1. MATRIX / GRID PLOTS
# =============================================================================
# Matrix or grid-style plots are useful for:
# - Showing correlations between variables
# - Visualizing pivot tables
# - Discovering patterns and hierarchical clusters in large datasets

# --- A. HEATMAPS (heatmap) ---
print("Generating Correlation Heatmap...")
plt.figure(figsize=(8, 5))

# Calculate numerical correlation matrix
corr = tips.corr(numeric_only=True)

# Plot correlation heatmap
sns.heatmap(corr, annot=True, cmap="coolwarm", fmt=".2f", linewidths=0.5)
plt.title("Correlation Heatmap - Tips Dataset")
plt.tight_layout()
plt.show()


# --- B. CLUSTERMAPS (clustermap) ---
print("Generating Clustermap...")

# Prepare pivot table for flights dataset
flights_pivot = flights.pivot(index="month", columns="year", values="passengers")

# Clustermap uses hierarchical clustering to group similar rows and columns
sns.clustermap(flights_pivot, cmap="viridis", annot=True, fmt="d", figsize=(10, 8))
plt.title("Cluster Map - Flight Passengers (Grouped by Similarity)", y=1.05)
plt.show()


# =============================================================================
# 2. STYLING & THEMES
# =============================================================================
# Seaborn allows easy control over background grids, color palettes, and text scaling.

# --- A. Background Styles ---
# Options: 'darkgrid', 'whitegrid', 'dark', 'white', 'ticks'
sns.set_style("darkgrid")

# --- B. Color Palettes ---
# Options include: 'deep', 'muted', 'pastel', 'bright', 'dark', 'colorblind', 'Set2', 'coolwarm', etc.
sns.set_palette("Set2")

# --- C. Scaling Context ---
# Options: 'paper', 'notebook' (default), 'talk', 'poster' (scales elements like font size & line thickness)
sns.set_context("notebook")

# Demonstrate custom styling on a scatterplot
print("Generating Styled Scatterplot...")
plt.figure(figsize=(8, 5))
sns.scatterplot(x="total_bill", y="tip", hue="sex", style="smoker", data=tips, s=80)
plt.title("Styled Scatter Plot with Darkgrid & Set2 Palette")
plt.tight_layout()
plt.show()

# Reset to default seaborn theme for clean execution in future scripts
sns.set_theme()
print("Execution completed.")