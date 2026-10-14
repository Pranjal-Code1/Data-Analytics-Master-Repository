import numpy as np

# ==========================================
# 1. FANCY INDEXING
# ==========================================
arr = np.array([10, 20, 30, 40, 50, 60])
print("Original:", arr)
print("Fancy indexing (positions 0, 2, 4):", arr[[0, 2, 4]])

matrix = np.arange(1, 13).reshape(3, 4)
print("Matrix:\n", matrix)
print("Select specific coordinates [row0,col1] & [row1,col2]:", matrix[[0, 1], [1, 2]])

# ==========================================
# 2. CONDITIONAL SELECTION
# ==========================================
data = np.array([5, 12, 18, 7, 30])
print("Indices where data > 10:", np.where(data > 10))
print("Conditional replacement (>10 keep, else 0):", np.where(data > 10, data, 0))

# ==========================================
# 3. SORTING & ORDERING
# ==========================================
vals = np.array([42, 5, 18, 23])
print("Sorted Array:", np.sort(vals))

idx = np.argsort(vals)
print("Sorted Indices:", idx)
print("Reordered using argsort indices:", vals[idx])

mat = np.array([[3, 7, 1], [9, 4, 6]])
print("Sort each row (axis=1):\n", np.sort(mat, axis=1))
print("Sort each column (axis=0):\n", np.sort(mat, axis=0))

# ==========================================
# 4. CONCATENATION & STACKING
# ==========================================
a = np.array([1, 2, 3])
b = np.array([4, 5, 6])
print("Concatenated 1D:", np.concatenate([a, b]))

A = np.array([[1, 2], [3, 4]])
B = np.array([[5, 6], [7, 8]])
print("Vertical Stack (vstack):\n", np.vstack((A, B)))
print("Horizontal Stack (hstack):\n", np.hstack((A, B)))