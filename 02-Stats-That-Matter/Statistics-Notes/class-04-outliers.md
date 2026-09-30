# Class - 04: Outliers

## 1. What Is An Outlier?
* An outlier is a data value that is much smaller or much larger than most of the other values in a dataset.
* In simple terms, it is a value that does not fit the general pattern of the data and "stands out" from the rest.

### Real-Life Intuition
* Imagine a class where most students have average height, but one student is extremely tall. 
* That very tall student stands out from the group and acts as an outlier.

### Why Do Outliers Occur?
Outliers can appear due to:
* Measurement errors
* Data entry mistakes
* Rare but valid real-world events
* Natural variation in data

---

## 2. Example of Outliers
Given dataset: $1, 2, 4, 7, 9, 110$
* Most values lie between $1$ and $9$.
* $110$ is extremely large compared to the others, making it an **outlier**.

### Effect of Outliers on Mean and Median
* **Mean:** 
  $$\text{Mean} = \frac{1 + 2 + 4 + 7 + 9 + 110}{6} = 19.14$$
* **Median:** Sorted data ($1, 2, 4, 7, 9, 110$), the median is the average of the middle values ($4$ and $7$), which equals **$7$**.

---

## 3. Why Outliers Are a Problem

### A. Distort Statistical Measures
* Mean becomes misleading.
* Standard deviation increases unnecessarily.
* Data summary becomes inaccurate.

### B. Affect Machine Learning Models
* Especially in regression models, outliers can dominate the learning process.
* The model tries to fit extreme values, resulting in poor generalization.

### C. Reduce Model Performance
Outliers negatively impact:
* Model accuracy
* Statistical testing
* Feature scaling
* Distance-based algorithms (like KNN and K-Means)

---

## 4. How Do We Detect Outliers?
While this class introduces outliers conceptually, data scientists detect them later using:
* IQR Method
* Boxplots
* Z-Score
* Visualization (scatter plots)
*(In fact, IQR exists mainly to handle outliers.)*

---

## Key Takeaways (Exam-Ready)
* An outlier is a value far from most data points.
* Outliers distort mean and standard deviation.
* Median is more reliable in the presence of outliers.
* Outliers seriously affect machine learning model performance.
* They must be identified and handled carefully.