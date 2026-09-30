# Class - 05: 5 Number Summary & Box Plots

## 1. What Is the Five Number Summary?
* The Five Number Summary is a quick statistical method used to describe a dataset using five key values.
* It gives us a complete snapshot of the center, the spread, and the extreme values of the data, making it widely used in Exploratory Data Analysis (EDA).

### The Five Key Values
1. **Minimum:** Smallest value in the dataset.
2. **First Quartile (Q1):** 25th percentile.
3. **Median (Q2):** 50th percentile (middle value).
4. **Third Quartile (Q3):** 75th percentile.
5. **Maximum:** Largest value in the dataset.

---

## 2. Example: Calculating the 5 Number Summary
Given sorted dataset: $10, 12, 14, 15, 18, 20, 22, 25, 30$

* **Minimum:** $10$
* **Maximum:** $30$
* **Median (Q2):** Middle value $= 18$
* **First Quartile (Q1):** Lower half ($10, 12, 14, 15$). Median of lower half: $Q1 = \frac{12 + 14}{2} = 13$
* **Third Quartile (Q3):** Upper half ($20, 22, 25, 30$). Median of upper half: $Q3 = \frac{22 + 25}{2} = 23.5$

---

## 3. Detecting and Removing Outliers
Outliers distort the mean, standard deviation, and ML model performance, so we detect and remove them carefully.

### Formulas
* **Interquartile Range (IQR):** 
  $$IQR = Q3 - Q1$$
* **Fence Formulas:**
  * **Lower Fence** = $Q1 - 1.5 \times IQR$
  * **Upper Fence** = $Q3 + 1.5 \times IQR$
* Any value less than the lower fence or greater than the upper fence is considered an outlier.

---

## 4. Box Plots
* A Box Plot is a graphical representation of the Five Number Summary.
* It shows spread, center, quartiles, and outliers in a single diagram.

### Understanding the Box Plot Components
* **The Box:** Represents the IQR ($Q3 - Q1$). Each section represents $25\%$ of the data.
* **Whiskers:** Extend from the box to the minimum and maximum values.
* **Median Line:** Divides the box; if the median is closer to one side, the data is skewed.

### Why Box Plots Are Powerful
* Visualizes distribution instantly.
* Identifies outliers easily.
* Compares multiple datasets effectively.