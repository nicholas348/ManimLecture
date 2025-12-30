import numpy as np#导入numpy 库，标记为numpy
print(np.pi)#输出numpy库中的pi值

from numpy import *#导入numpy中的所有模块
print(pi)


#常见库 1:numpy


import numpy as np

# 1. CREATING ARRAYS
# ---------------------------------------------------------
print("--- 1. Creation ---")
# Creating from a list
simple_arr = np.array([10, 20, 30])

# Creating a 2D array (3 rows, 3 columns)
matrix = np.array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
])

# Creating placeholders
zeros = np.zeros((2, 5))     # 2 rows, 5 columns of 0.0
identity = np.eye(3)         # 3x3 Identity matrix (1s on diagonal)
random_vals = np.random.randint(0, 100, (3, 3)) # 3x3 matrix of random ints

print(f"Random Matrix:\n{random_vals}\n")


# 2. INSPECTING PROPERTIES
# ---------------------------------------------------------
print("--- 2. Inspection ---")
print(f"Shape: {matrix.shape}")  # (3, 3)
print(f"Data Type: {matrix.dtype}")  # int64 or int32
print(f"Total Elements: {matrix.size}\n")


# 3. INDEXING AND SLICING
# ---------------------------------------------------------
# Syntax: array[row_index, column_index]
print("--- 3. Indexing & Slicing ---")
print(f"Element at Row 0, Col 1: {matrix[0, 1]}")

# Slicing: [start:stop]
print(f"First two rows:\n{matrix[0:2, :]}")
print(f"The second column: {matrix[:, 1]}\n")


# 4. VECTORIZED MATH (NO FOR-LOOPS!)
# ---------------------------------------------------------
print("--- 4. Vectorized Operations ---")
arr = np.array([1, 2, 3])

# All operations are applied element-wise
print(f"Add 10: {arr + 10}")
print(f"Square: {arr ** 2}")
print(f"Boolean Mask (val > 1): {arr > 1}\n")


# 5. AGGREGATIONS (AXIS CONTROL)
# ---------------------------------------------------------
# axis=0: Vertical (Column-wise)
# axis=1: Horizontal (Row-wise)
print("--- 5. Aggregations ---")
test_data = np.array([[1, 2], [3, 4]])

print(f"Total Sum: {np.sum(test_data)}")
print(f"Sum of each column: {np.sum(test_data, axis=0)}")
print(f"Max of each row: {np.max(test_data, axis=1)}\n")


# 6. RESHAPING
# ---------------------------------------------------------
print("--- 6. Reshaping")
flat = np.arange(12)  # [0, 1, ..., 11]
reshaped = flat.reshape(3, 4) # Changes 1x12 into 3x4
print(f"Reshaped 3x4 Matrix:\n{reshaped}")



from scipy import optimize, interpolate, integrate, linalg
import matplotlib.pyplot as plt

# 1. OPTIMIZATION (Finding Minima/Maxima)
# ---------------------------------------------------------
# Let's find the minimum of a simple function: f(x) = x^2 + 10sin(x)
print("--- 1. Optimization ---")

def f(x):
    return x**2 + 10*np.sin(x)

# minimize(function, initial_guess)
result = optimize.minimize(f, x0=0)
print(f"Minimum found at x = {result.x[0]:.4f}")

# 2. INTERPOLATION (Filling in the gaps)
# ---------------------------------------------------------
# Used when you have sparse data points and need to predict values between them.
print("\n--- 2. Interpolation ---")

x_data = np.linspace(0, 10, 10)
y_data = np.cos(x_data)

# Create an interpolation function (cubic makes it a smooth curve)
f_interp = interpolate.interp1d(x_data, y_data, kind='cubic')

x_new = np.linspace(0, 10, 100)
y_new = f_interp(x_new)
print("Interpolation function created for smooth curve fitting.")

# 3. INTEGRATION (Calculating Area Under Curve)
# ---------------------------------------------------------
# We use 'quad' (quadrature) to integrate a function from point a to b.
print("\n--- 3. Integration ---")

# Integrate f(x) = x^2 from 0 to 1
# Analytical answer is 1/3
area, error = integrate.quad(lambda x: x**2, 0, 1)
print(f"Integral of x^2 from 0 to 1: {area:.4f}")
print(error)

# 4. LINEAR ALGEBRA
# ---------------------------------------------------------
# While NumPy has linalg, SciPy's version is more advanced and faster.
print("\n--- 4. Linear Algebra ---")

# Solving a system of equations:
# 3x + 2y = 2
# 1x - 1y = 4
A = np.array([[3, 2], [1, -1]])
b = np.array([2, 4])

solution = linalg.solve(A, b)
print(f"Solution to system: x={solution[0]}, y={solution[1]}")

# Finding the determinant
det = linalg.det(A)
print(f"Determinant of A: {det}")