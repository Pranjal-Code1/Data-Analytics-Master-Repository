# Class 02: NumPy Indexing, Slicing, Reshaping, and Flattening

## 1. Array Attributes
Attributes help inspect array structure without modifying data:
* **`.shape`**: Returns a tuple of dimensions (rows, columns).
* **`.ndim`**: Returns the total number of dimensions (axes).
* **`.size`**: Returns the total count of elements in the array.
* **`.dtype`**: Returns the data type of the elements stored.
0
## 2. Indexing & Slicing
* **1D Operations:** Access items like Python lists (`arr[0]`, `arr[-1]`) and slice ranges (`arr[2:8]`, `arr[::-1]` for reversing).
* **2D Operations:** Access specific coordinates using `arr[row, col]` or slice sub-matrices (e.g., `arr[0:2, 1:3]`).

## 3. Boolean Indexing
* Generate boolean masks using conditions (e.g., `arr > 5`).
* Pass the mask directly into the array brackets (e.g., `arr[arr > 5]`) to filter matching elements automatically.

## 4. Reshaping & Flattening
* **`.reshape(rows, cols)`**: Changes the array dimensions while keeping the total number of elements constant.
* **`.flatten()`**: Converts any multi-dimensional matrix back into a single-dimensional 1D array.