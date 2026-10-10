import numpy as np

# ==========================================
# 1. ATTRIBUTES OF AN ARRAY
# ==========================================
arr = np.array([[1, 2, 3], [4, 5, 6]])
print("Array:\n", arr)
print("Shape:", arr.shape)       # (2, 3) -> 2 rows, 3 cols
print("Dimensions:", arr.ndim)  # 2D array
print("Size:", arr.size)         # Total elements (6)
print("Data type:", arr.dtype)   # e.g., int64

# ==========================================
# 2. INDEXING AND SLICING
# ==========================================
# 1D Indexing
arr_1d = np.array([10, 20, 30, 40, 50])
print("1D First Element:", arr_1d[0])
print("1D Last Element:", arr_1d[-1])

# 2D Indexing & Slicing
matrix = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print("Row 0:", matrix[0])
print("Element at [1,1]:", matrix[1, 1])
print("2D Sliced Matrix:\n", matrix[0:2, 1:3])

# ==========================================
# 3. BOOLEAN INDEXING
# ==========================================
data = np.array([5, 10, 15, 20, 25])
print("Boolean Mask (>12):", data > 12)
print("Filtered Array:", data[data > 12])

# ==========================================
# 4. RESHAPING AND FLATTENING
# ==========================================
# Reshaping 12 elements into a 3x4 grid
flat_arr = np.arange(12)
reshaped_matrix = flat_arr.reshape(3, 4)
print("Reshaped Matrix:\n", reshaped_matrix)

# Flattening back to 1D
print("Flattened Array:", reshaped_matrix.flatten())