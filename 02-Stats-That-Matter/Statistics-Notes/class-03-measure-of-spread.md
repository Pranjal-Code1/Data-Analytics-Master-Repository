# Class - 03: Measure Of Spread

## 1. What Is Measure Of Spread?
In Class-02, we learned about **Measure of Central Tendency** (Mean, Median, Mode), which tells us where the center of the data lies. However, the center alone is not enough to understand a dataset.

* **Measure of Spread** tells us how far the data values are spread or scattered around the center.

### Example: Why Measure of Spread Is Important
Imagine two cricket players:
* **Player A scores:** $50, 50, 50, 50, 50$ (very consistent)
* **Player B scores:** $0, 20, 40, 80, 100$ (very inconsistent)

* The mean of both players is **50**.
* But Player B's performance varies a lot, which is known as **Spread**. 
* Two datasets can have the exact same mean but behave very differently.

---

## 2. Types Of Measure Of Spread
Mainly, we study two types of spread:
1. **Range**
2. **Interquartile Range (IQR)**

---

### A. Range
Range is the difference between the largest and the smallest value in a dataset. It gives a basic idea of how wide the data is spread.

$$\text{Range} = \text{Largest Value} - \text{Smallest Value}$$

#### Example:
Given data (marks of students): $10, 20, 25, 30, 35, 40$
* Largest value = $40$
* Smallest value = $10$
* $\text{Range} = 40 - 10 = 30$

#### Key Points About Range:
* Very easy to calculate.
* Gives a quick overview of spread.
* **Highly affected by outliers.**
  * *Example:* If data is $10, 12, 14, 15, 100$, the range is $100 - 10 = 90$, even though most values are close together.
  * This is why Range is not reliable for real-world data.

---

### B. Interquartile Range (IQR)
Because range considers only two values (min and max) and gets distorted by outliers, we use **IQR** to focus on the middle 50% of the data.

* **Quartile** means Quarter ($\frac{1}{4}$th). Data is divided into 4 equal parts.

| Quartile | Meaning | Percentile |
| :--- | :--- | :--- |
| **Q1** | First Quartile | 25% |
| **Q2** | Second Quartile (Median) | 50% |
| **Q3** | Third Quartile | 75% |
| **Q4** | Maximum Value | 100% |

#### Formula:
$$\text{IQR} = Q3 - Q1$$

---

### Step-by-Step Example for IQR
Given sorted data: 
$$12, 12, 13, 14, 15, 17, 20, 20, 28, 29, 31, 35, 46, 48, 51, 59, 60$$

**Step 1: Identify Quartiles**
* $Q1\text{ (25\%)} = 15$
* $Q2\text{ (50\%)} = \text{Median}$
* $Q3\text{ (75\%)} = 46$

**Step 2: Calculate IQR**
$$\text{IQR} = Q3 - Q1$$
$$\text{IQR} = 46 - 15 = 21$$

---

### Why Do We Use IQR?
* Shows the spread of the **middle 50%** of data.
* **Ignores outliers** (extreme values).
* Gives a better and more realistic picture than Range.
* Very important in Data Science & Exploratory Data Analysis (EDA).