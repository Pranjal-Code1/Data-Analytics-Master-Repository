# Pandas Cheat Sheet: Data Cleaning Essentials

## 1. Handling Missing Values
Detecting, removing, or filling missing data in your dataset:

* **Detect Missing Values (`isna` / `isnull`):** Returns a boolean DataFrame showing `True` where values are missing.
  ```python
  df.isna()
  df.isnull().sum()  # Count of missing values per column
  ```
* **Drop Missing Values (`dropna`):** Removes rows or columns containing missing values.
  ```python
  df.dropna()          # Drops any row with at least one NaN
  df.dropna(axis=1)    # Drops any column with at least one NaN
  ```
* **Fill Missing Values (`fillna`):** Replaces missing values with a specified value, statistical metric, or method.
  ```python
  df["Age"] = df["Age"].fillna(df["Age"].mean())
  df["City"] = df["City"].fillna("Unknown")
  df["Score"] = df["Score"].fillna(0)
  ```

## 2. Changing Data Types (`astype`)
Converting column data types for compatibility or memory optimization:
* **Cnvert Column Type:**
  ```python
  df["Age"] = df["Age"].astype(float)
  df["Name"] = df["Name"].astype("category")
  df["Score"] = df["Score"].astype(str)
  ```

## 3. Replacing Values (`replace`)
Substituting specific values, typos, or mapping categories:
* **Replace Single or Multiple Values:**
  ```python
  df["Name"] = df["Name"].replace("Bob", "Robert")
  df["Score"] = df["Score"].replace({88: 90, 95: 99})
  ```
* **Replace Using Substrings / Patterns:**
  ```python
  df["City"] = df["City"].replace({"Pun": "Pune"}, regex=False)
  ```

## 4. Dropping Rows & Columns (`drop`)
Removing unwanted structural elements from your DataFrame:

* **Drop Rows by Index:**
  ```python
  df = df.drop(2)        # Drops a single row by index label
  df = df.drop([0, 4])   # Drops multiple rows
  ```
* **Drop Columns:**
  ```python
  df = df.drop("Score", axis=1)              # Drop a single column
  df = df.drop(["Age", "Score"], axis=1)     # Drop multiple columns
  df.drop("Score", axis=1, inplace=True)     # Modify DataFrame directly
  ```

## 5. Detecting & Removing Duplicates
Managing repeated rows in your dataset:

* **Detect Duplicates:**
  ```python
  df.duplicated()         # Returns boolean Series
  df.duplicated().sum()   # Total count of duplicate rows
* **Remove Duplicates:**
  ```python
  df.drop_duplicates()                     # Keeps first occurrence (default)
  df.drop_duplicates(keep="last")          # Keeps last occurrence
  df.drop_duplicates(keep=False)           # Removes all duplicate rows
  df.drop_duplicates(subset=["Name"])      # Checks duplicates based on specific columns
  ```