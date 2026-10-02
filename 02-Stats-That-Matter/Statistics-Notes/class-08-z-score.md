# Class - 08: Z-Score & Data Distribution

## 1. What Is A Z-Score?
- A Z-score tells us how many standard deviations a data point is away from the mean.
- It measures the relative position of a value in a distribution rather than its absolute value.
- It indicates whether a value is above the mean, below the mean, and how far from the mean.

### Formula
$$z = \frac{x - \mu}{\sigma}$$

- **$x$** = Data Point
- **$\mu$** = Mean
- **$\sigma$** = Standard Deviation

---

## 2. Interpretation of Z-Score
- **$z = 0$**: Value is exactly at the mean.
- **$z > 0$**: Value is above the mean.
- **$z < 0$**: Value is below the mean.

### Example Calculation
- **Given:** 
  - Mean = $8$
  - Standard Deviation = $1$
  - Data Point = $9.5$
- **Calculation:** 
  $$z = \frac{9.5 - 8}{1} = 1.5$$
- **Meaning:** $9.5$ is $1.5$ standard deviations above the mean.

---

## 3. Z-Score and Percentage (Z-Table)
- Z-score helps calculate how much percentage of data lies below or above a value.
- For $Z = 1.50$, the Z-table value is approximately $0.93319$.
- **Percentage Conversion:** 
  $$0.93319 \times 100 = 93.31\%$$
- $93.31\%$ of data lies below this value.

---

## 4. Why Z-Score Is Important?
1. **Outlier Detection:** Values with $|z| > 3$ are suspicious and treated as outliers.
2. **Normalization (ML):** Used in standard scaling to convert features to the same scale.
3. **Probability & Statistics:** Used with normal distribution as a foundation of hypothesis testing.

---

## 5. Z-Score vs. Empirical Rule

| Feature | Empirical Rule | Z-Score |
| :--- | :--- | :--- |
| **Precision** | Approximate | Exact |
| **Scope** | 68-95-99.7 rule | Any value |
| **Nature** | Visual understanding | Mathematical precision |