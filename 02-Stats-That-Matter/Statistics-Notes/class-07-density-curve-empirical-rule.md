# Class - 07: Density Curve and Empirical Rule

## 1. What Is A Density Curve?
- A density curve is a smooth curve that represents the overall shape of a data distribution.
- Instead of focusing on individual bars of a histogram, a density curve gives us a clean and continuous picture of how data is distributed.
- **Simple Definition:** A density curve is a smooth picture of data distribution.

---

## 2. Why Do We Need A Density Curve?
- **Histograms:** Depend on bin size and can look different if bins change.
- **Density Curves:** 
  - Remove noise.
  - Show the true underlying pattern.
  - Make comparison easier.

### How a Density Curve is Created (Conceptually)
- Start with a histogram.
- Mark points at the top of each bar.
- Connect these points to form a frequency polygon.
- Smooth the sharp edges to get a density curve.
- **Flow:** Histogram $\rightarrow$ Frequency Polygon $\rightarrow$ Smoothed Curve $\rightarrow$ Density Curve.

---

## 3. Key Properties of a Density Curve
1. **Total Area = 100%:** The total area under a density curve is always 1 (or 100%).
2. **Area Represents Probability:** The area under the curve between two values tells us what percentage of data lies in that interval. No data lies outside the curve.
3. **Shape Reflects Distribution:** The shape reflects normal distribution, skewed distribution, or the presence of outliers, letting us easily judge if data is symmetric, skewed, concentrated, or spread.

---

## 4. Empirical Rule (68-95-99.7 Rule)
- The empirical rule applies only to Normal Distribution (Bell Curve).
- It tells us how data is distributed around the mean using standard deviation ($\sigma$).

### The Rule Itself
- **Mean $\pm$ 1$\sigma$:** $\approx 68\%$ of data.
- **Mean $\pm$ 2$\sigma$:** $\approx 95\%$ of data.
- **Mean $\pm$ 3$\sigma$:** $\approx 99.7\%$ of data.

### Understanding the Rule Intuitively
- **Mean at the Center:** Divides data into 50% left and 50% right.
- **One Standard Deviation ($\pm$1$\sigma$):** Covers most common values.
- **Two Standard Deviations ($\pm$2$\sigma$):** Covers data close to the mean and almost all practical data.
- **Three Standard Deviations ($\pm$3$\sigma$):** Covers almost the entire dataset; values beyond this are very rare and considered outliers.

### Why Empirical Rule is Important?
1. **Outlier Detection:** Values beyond $\pm$3$\sigma$ are suspicious.
2. **Data Understanding:** Quickly estimates where most data lies.
3. **Machine Learning:** Many algorithms assume normality; it helps in feature scaling and anomaly detection.

---

## 5. Density Curve vs. Histogram

| Feature | Histogram | Density Curve |
| :--- | :--- | :--- |
| **Structure** | Discrete Bars | Smooth Continuous Curve |
| **Dependency** | Depends on bin size | Independent of bins |
| **Visualization** | Rough visualization | Clean & interpretable |
| **Basis** | Frequency-based | Probability-based |