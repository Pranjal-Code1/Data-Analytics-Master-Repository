# NumPy Cheat Sheet: Arrays & Built-in Methods

## 1. Importing NumPy
To use NumPy in your Python scripts or notebooks, import it with the standard alias:
```python
import numpy as np
```
### 2. Creating NumPy Arrays from Python Lists
NumPy arrays (ndarray) are the core data structures used for fast numerical computing:

**1-D Vector from a List:**

```python
data_list = [1, 2, 3, 4, 5]
vector_arr = np.array(data_list)
print("1-D Vector:", vector_arr)
```
**2-D Matrix from a List of Lists:**

```python
matrix_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
matrix_arr = np.array(matrix_list)
print("2-D Matrix:\n", matrix_arr)
```
### 3. Built-in Array Generation Methods
Instead of manual lists, use NumPy built-in functions for efficient initialization:

**Zeros Array:** Creates an array filled entirely with zeros.

```python
zeros_arr = np.zeros((3, 3), dtype=int)
```
**Ones Array:** Creates an array filled entirely with ones.

```python
ones_arr = np.ones((2, 4), dtype=float)
```
**Arange:** Generates values within a given interval with a specified step size.

```python
range_arr = np.arange(0, 10, 2)  # Output: [0, 2, 4, 6, 8]
```

**Linspace:** Generates evenly spaced numbers over a specified range.

```python
linear_arr = np.linspace(0, 1, 5)  # 5 numbers between 0 and 1
```

### 4.Random Number Generation (np.random)
**Uniform Distribution (Values between 0 and 1):**

```python
rand_arr = np.random.rand(3, 3)
Standard Normal Distribution (Mean = 0, Variance = 1):
```

```python
randn_arr = np.random.randn(3, 3)
Random Integers:
```

```python
randint_arr = np.random.randint(1, 10, size=(2, 3))
```

### 5. Essential Array Attributes
You can inspect the metadata of any NumPy array using these built-in attributes:

**arr.ndim**: Returns the number of dimensions (axes) of the array.

**arr.shape:** Returns a tuple representing the size in each dimension (rows, columns).

**arr.size:** Returns the total number of elements in the array.

**arr.dtype:** Returns the data type of the elements (e.g., int64, float64).