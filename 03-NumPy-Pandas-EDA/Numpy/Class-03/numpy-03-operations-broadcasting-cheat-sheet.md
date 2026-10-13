# Class 03: NumPy Array Operations, Broadcasting, and Aggregations

## 1. Element-Wise Operations
NumPy arrays support vectorized calculations where arithmetic operators (`+`, `-`, `*`, `/`) apply directly to corresponding elements simultaneously without explicit loops.

## 2. Broadcasting
Broadcasting automates shape matching during arithmetic operations:
* **Scalar Broadcasting:** Scales every element in an array by a single numerical value.
* **Dimension Broadcasting:** Allows operations between arrays of different shapes (such as adding a 1D array to a 2D matrix row-wise) as long as dimensions align properly.

## 3. Aggregate Functions
Built-in statistical functions make data summarization fast:
* `np.sum()`, `np.mean()`
* `np.min()`, `np.max()`
* `np.std()`, `np.var()`

## 4. Axis-Based Operations
Control the direction of statistical calculations using the `axis` parameter:
* **`axis=0`**: Computes metrics down columns (across rows).
* **`axis=1`**: Computes metrics across rows (across columns).