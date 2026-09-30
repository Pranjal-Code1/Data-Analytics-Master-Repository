# Class - 06: Data Distribution, Variance, and Standard Deviation

## 1. What Is Data Distribution?
- When we collect data (marks of students, heights, salaries, etc.), the values are not randomly scattered.
- Instead, they follow a pattern.
- Data distribution refers to how data values are spread, arranged, or distributed across different values.
- It tells us which values occur frequently, which are rare, and whether data is balanced, skewed, or concentrated.
- **Simple Definition:** Data distribution shows how often each value (or range of values) appears in a dataset to help us understand the center, spread, and shape of data.

---

## 2. Types Of Data Distribution
1. **Normal Distribution (Bell-Shaped Curve):**
   - A perfectly balanced distribution.
   - Most values lie around the mean, and very few values are extremely high or extremely low.
   - The graph looks like a bell curve.
   - **Relationship:** $\text{Mean} = \text{Median} = \text{Mode}$.
   - **Examples:** Heights of people, IQ scores, and measurement errors.

2. **Right-Skewed Distribution (Positive Skew):**
   - A skewed distribution is not balanced around the mean, where most data points are concentrated on one side and the tail stretches on the right side.
   - Most values are low, and few values are very high.
   - **Examples:** Income distribution and house prices.
   - **Relationship:** $\text{Mean} > \text{Median} > \text{Mode}$.

3. **Left-Skewed Distribution (Negative Skew):**
   - The tail is longer on the left side.
   - Most values are high, and few values are very low.
   - **Example:** Marks in an easy exam.
   - **Relationship:** $\text{Mean} < \text{Median} < \text{Mode}$.

---

## 3. Population And Sample
- Studying entire data is often time-consuming, expensive, and practically impossible, so we study a small part and make conclusions about the whole.

### Definitions and Notations
- **Population:** The complete set of all items, people, or measurements. Denoted by $N$, and characteristics are called parameters. Examples include all students in a university or all customers of a company.
- **Sample:** A subset of the population selected for study. Denoted by $n$, and characteristics are called statistics. Examples include 100 students selected from the university or a survey of 500 customers.

### Comparison Table
| Feature | Population | Sample |
| :--- | :--- | :--- |
| **Size** | Large ($N$) | Small ($n$) |
| **Measures** | Parameter | Statistics |
| **Usage** | Rare | Common |

---

## 4. Variance
- Mean tells us the center, but variance tells us how spread out the data is.
- Variance is the average of squared distances of each value from the mean.

### Why Do We Square the Differences?
- To avoid positive and negative values cancelling each other.
- To give more weight to values far from the mean.

### Example Calculation
- **Data:** $85, 90, 95, 100, 105$
- **Step 1:** Mean $= 95$
- **Step 2:** Differences from mean: $(85-95), (90-95), (95-95), (100-95), (105-95)$
- **Step 3:** Square the differences and add: $(-10)^2 + (-5)^2 + 0^2 + 5^2 + 10^2 = 250$
- **Step 4:** Divide by number of values: $\text{Variance} = \frac{250}{5} = 50$

---

## 5. Standard Deviation (SD)
- Standard Deviation (SD) is the square root of the variance.

### Why SD Is Better Than Variance?
- Variance is in squared units, whereas SD is in original units of data, making it much easier to interpret.

### Example and Interpretation
- If $\text{Variance} = 50$, then $\text{SD} = \sqrt{50} = 7.071$.
- **Small SD:** Data points are close to the mean.
- **Large SD:** Data points are widely spread.

---

## 6. Summary Notations (Population vs. Sample)
| Measure | Population | Sample |
| :--- | :--- | :--- |
| **Mean** | $\mu$ | $\bar{X}$ |
| **Variance** | $\sigma^2$ | $s^2$ |
| **Standard Deviation** | $\sigma$ | $s$ |
| **Size** | $N$ | $n$ |