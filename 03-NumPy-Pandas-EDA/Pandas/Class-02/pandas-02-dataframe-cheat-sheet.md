# Pandas Cheat Sheet: DataFrame Basics & Inspection

## 1. Inspecting Data
Quick ways to understand the structure and contents of your dataset:
* **Head:** Returns the first *n* rows (default is 5).
  ```python
  df.head(3)
  ```
* **tail(n):** returns the last *n* rows
``` python
df.tail(2)
```
* **info():** provides a concise summary including column names, non-null counts, and data types
```python
df.info()
```
* **shape →** returns a tuple representing dimensions (rows, columns)
```python
df.shape
```
* **dtypes:** returns the data type of each column
```python
df.dtypes
```

## 2. Selecting Columns & Rows
Ways to access specific parts of a DataFrame:

* **Single Column:** Extracts a single column as a pandas Series.
```python
df["Name"]
```
* **Multiple Columns:** Extracts a sub-DataFrame containing specified columns.
```python
df[["Name", "Score"]]
```
* **Label-Based Selection (.loc):** Accesses rows and columns by their labels/names.
```python
df.loc[2, "Score"]
df.loc[1:3, ["Name", "Age"]]
```
* **Integer-Index Selection (.iloc):** Accesses rows and columns by their integer positions.
```python
df.iloc[3]
df.iloc[0:3, 0:2]
```

## 3. Index & Columns Overview
Inspecting the structural components of a DataFrame:
* **Index (df.index):** Returns row labels or range index.
```python
df.index
```
* **Columns (df.columns):** Returns the names of all columns.
```python
df.columns
```
* **Values (df.values):** Returns the underlying NumPy array containing data only.
```python
df.values
```
## 4. Renaming Columns & Setting an Index
Modifying DataFrame structure and labels:
* **Renaming Columns:** Changes specified column names using a dictionary mapping.
```python
df_renamed = df.rename(columns={"Score": "Marks"})
```
* **Setting an Index:** Promotes an existing column to become the DataFrame index.
```python
df_indexed = df_renamed.set_index("Name")
```
* **Resetting the Index:** Reverts the index back to default integer numbering.
```python
df_reset = df_indexed.reset_index()
```
