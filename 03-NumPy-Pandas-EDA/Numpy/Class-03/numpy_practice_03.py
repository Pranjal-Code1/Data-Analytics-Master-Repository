import numpy as np

# ==========================================
# 1. ELEMENT-WISE OPERATIONS
# ==========================================
a = np.array([10, 20, 30, 40])
b = np.array([1, 2, 3, 4])

print("Addition:", a + b)
print("Subtraction:", a - b)
print("Multiplication:", a * b)
print("Division:", a / b)

# ==========================================
# 2. BROADCASTING
# ==========================================
arr = np.array([1, 2, 3, 4])
print("Scalar Broadcasting:", arr * 5)

# Adding 1D array to a 2D matrix row-wise
A = np.array([[1, 2, 3], [4, 5, 6]])
B = np.array([10, 20, 30])
print("Matrix-1D Broadcasting Addition:\n", A + B)

# ==========================================
# 3. AGGREGATE FUNCTIONS
# ==========================================
data_1d = np.array([4, 8, 15, 16, 23, 42])
print("Sum:", np.sum(data_1d))
print("Mean:", np.mean(data_1d))
print("Min:", np.min(data_1d))
print("Max:", np.max(data_1d))
print("Standard Deviation:", np.std(data_1d))
print("Variance:", np.var(data_1d))

# ==========================================
# 4. AXIS-BASED OPERATIONS
# ==========================================
data_2d = np.array([[1, 2, 3], 
                    [4, 5, 6], 
                    [7, 8, 9]])

print("Total Sum:", np.sum(data_2d))
print("Row-wise Sum (axis=1):", np.sum(data_2d, axis=1))
print("Column-wise Sum (axis=0):", np.sum(data_2d, axis=0))
print("Row-wise Mean (axis=1):", np.mean(data_2d, axis=1))
print("Column-wise Mean (axis=0):", np.mean(data_2d, axis=0))