"""
Module: Pandas Basics - Class 01 Practice Script
Description: Introduction to Pandas Series, DataFrames, and creation methods.
"""

import pandas as pd
import numpy as np

print("=== 1. Creating Series ===")
# Series from a Python list
marks_list = [90, 85, 78, 92]
series_from_list = pd.Series(marks_list, name="Marks")
print("Series from list:\n", series_from_list)

# Series from a Python dictionary
marks_dict = {"Alice": 90, "Bob": 85, "Charlie": 78, "David": 92}
series_from_dict = pd.Series(marks_dict, name="Marks")
print("\nSeries from dictionary:\n", series_from_dict)


print("\n=== 2. Creating DataFrames from Dictionaries ===")
data = {
    "Name": ["Alice", "Bob", "Charlie", "David"],
    "Marks": [90, 85, 78, 92],
    "Subject": ["Math", "Science", "History", "English"]
}
df_from_dict = pd.DataFrame(data)
print(df_from_dict)


print("\n=== 3. Creating DataFrames from NumPy Arrays ===")
arr_2d = np.array([[1, 2, 3],
                   [4, 5, 6],
                   [7, 8, 9]])
df_from_numpy = pd.DataFrame(arr_2d, columns=["A", "B", "C"])
print(df_from_numpy)