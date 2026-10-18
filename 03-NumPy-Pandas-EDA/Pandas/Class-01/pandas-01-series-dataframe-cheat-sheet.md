# Pandas Class 01: Introduction, Series, and DataFrames

## 1. What is Pandas?
* Pandas is a powerful Python library designed for data analysis and manipulation.
* It provides two primary core data structures: **Series** (1-dimensional) and **DataFrame** (2-dimensional).
* It streamlines tabular data processing, cleaning, and integration with other scientific libraries like NumPy.

## 2. Installation & Import
* Install via terminal:
  ```bash
  pip install pandas
  ```
* Standard import convention in Python scripts:
  ```python
  import numpy as np
  import pandas as pd
  ```

## 3. Working with Series
A Series is a one-dimensional labeled array comparable to a single column in a spreadsheet.
* **From a Python List:**
  ```python
  data = [90, 85, 78, 92]
  series_list = pd.Series(data, name="Marks")
  ```
* **From a Python Dictionary:**
  ```python
  data_dict = {"Alice": 90, "Bob": 85, "Charlie": 78, "David": 92}
  series_dict = pd.Series(data_dict, name="Marks")
  ```

## 4. Working with DataFrames
A DataFrame is a two-dimensional labeled table similar to an Excel sheet or SQL table.
* **From a Dictionary:**
  ```python
  df_dict = pd.DataFrame({
      "Name": ["Alice", "Bob", "Charlie", "David"],
      "Marks": [90, 85, 78, 92],
      "Subject": ["Math", "Science", "History", "English"]
  })
  ```
* **From a NumPy Array:**
  ```python
  arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
  df_np = pd.DataFrame(arr, columns=["A", "B", "C"])
  ```