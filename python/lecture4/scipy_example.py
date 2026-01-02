import numpy as np
from scipy import *

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