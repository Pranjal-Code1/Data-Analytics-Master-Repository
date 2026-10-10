"""
Module: NumPy Basics - Class 01 Practice Script
Description: Covers array creation, built-in initialization methods, 
             and random number generation using NumPy.
"""

import numpy as np

print("=== 1. Creating NumPy Arrays from Python Lists ===")

# Creating a 1-D vector from a list
data_list = [1, 2, 3, 4, 5]
vector_arr = np.array(data_list)
print("1-D Vector:", vector_arr)

# Creating a 2-D matrix from a list of lists
matrix_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
matrix_arr = np.array(matrix_list)
print("2-D Matrix:\n", matrix_arr)


print("\n=== 2. Built-in Array Generation Methods ===")

# Zeros and Ones
print("Zeros (1D):", np.zeros(4))
print("Zeros (2D Matrix):\n", np.zeros((3, 4)))

print("Ones (1D):", np.ones(3))
print("Ones (2D Matrix):\n", np.ones((2, 2)))

# Full arrays with a custom value
print("Full Array (1D):", np.full(5, 7))
print("Full Matrix (2D):\n", np.full((3, 3), 7))

# Sequential ranges and spaces
print("Arange (Step-based):", np.arange(0, 10, 2))
print("Linspace (Evenly spaced):", np.linspace(0, 1, 5))
print("Identity Matrix (4x4):\n", np.eye(4))


print("\n=== 3. Random Number Generation ===")

# Random floats between 0 and 1
print("Random Floats (2x3):\n", np.random.rand(2, 3))

# Random integers within a specified range
print("Random Integers (3x3 between 1 and 9):\n", np.random.randint(1, 10, (3, 3)))

# Random values from a standard normal distribution (bell curve)
print("Standard Normal Distribution (2x4):\n", np.random.randn(2, 4))