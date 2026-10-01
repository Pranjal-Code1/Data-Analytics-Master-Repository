# Class - 07: Density Curve and Empirical Rule

## 1. What Is A Density Curve?
- A density curve is a smooth curve that represents the overall shape of a data distribution[cite: 33].
- Instead of focusing on individual bars of a histogram, a density curve gives us a clean and continuous picture of how data is distributed[cite: 33].
- A density curve is a smooth picture of data distribution[cite: 33].

---

## 2. Why Do We Need A Density Curve?
- Histograms depend on bin size and can look different if bins change[cite: 34].
- Density curves remove noise[cite: 34].
- Density curves show the true underlying pattern[cite: 34].
- Density curves make comparison easier[cite: 34].

### How a Density Curve is Created (Conceptually)
- Start with a histogram[cite: 35].
- Mark points at the top of each bar[cite: 35].
- Connect these points to form a frequency polygon[cite: 35].
- Smooth the sharp edges to get a density curve[cite: 35].
- Flow: Histogram $\rightarrow$ Frequency Polygon $\rightarrow$ Smoothed Curve $\rightarrow$ Density Curve[cite: 35].

---

## 3. Key Properties of a Density Curve
- The total area under a density curve is always 1 or 100%[cite: 36].
- The area under the curve between two values tells us what percentage of data lies in that interval[cite: 36].
- No data lies outside the curve[cite: 36].
- The shape reflects normal distribution, skewed distribution, or the presence of outliers[cite: 37].
- By looking at the curve, we can guess if data is symmetric, skewed, or concentrated/spread[cite: 37].

---

## 4. Empirical Rule (68-95-99.7 Rule)
- The empirical rule applies only to Normal Distribution (Bell Curve)[cite: 38].
- It tells us how data is distributed around the mean using standard deviation ($\sigma$)[cite: 38].
- Mean $\pm$ 1$\sigma$ covers approximately 68% of data[cite: 38].
- Mean $\pm$ 2$\sigma$ covers approximately 95% of data[cite: 38].
- Mean $\pm$ 3$\sigma$ covers approximately 99.7% of data[cite: 38].

### Understanding the Rule Intuitively
- The mean is at the center and divides data into 50% left and 50% right[cite: 39].
- One standard deviation ($\pm$1$\sigma$) covers most common values[cite: 39].
- Two standard deviations ($\pm$2$\sigma$) covers data close to the mean and almost all practical data[cite: 39].
- Three standard deviations ($\pm$3$\sigma$) covers almost the entire dataset, and values beyond this are very rare (outliers)[cite: 40].

### Why Empirical Rule is Important?
- Values beyond $\pm$3$\sigma$ are suspicious for outlier detection[cite: 41].
- It helps quickly estimate where most data lies for data understanding[cite: 41].
- Many machine learning algorithms assume normality, aiding in feature scaling and anomaly detection[cite: 41].

---

## 5. Density Curve vs. Histogram

| Feature | Histogram | Density Curve |
| :--- | :--- | :--- |
| **Structure** | Discrete Bars[cite: 42] | Smooth Continuous Curve[cite: 42] |
| **Dependency** | Depends on bin size[cite: 42] | Independent of bins[cite: 42] |
| **Visualization** | Rough visualization[cite: 42] | Clean & interpretable[cite: 42] |
| **Basis** | Frequency-based[cite: 42] | Probability-based[cite: 42] |