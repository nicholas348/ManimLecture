import numpy as np
from scipy.optimize import minimize

# Define a simple quadratic function: f(x) = (x - 3)^2
def objective_function(x):
    return (x - 3)**2

# Provide an initial guess
initial_guess = 0

# Minimize the function
result = minimize(objective_function, initial_guess)

print(f"Minimum found at x = {result.x[0]:.2f}")




from scipy.integrate import quad

# Define a function to integrate: f(x) = x^2
def integrand(x):
    return x**2

# Integrate from x=0 to x=1
area, error = quad(integrand, 0, 1)

print(f"The integral of x^2 from 0 to 1 is: {area:.4f}")


from scipy import signal
import matplotlib.pyplot as plt

# Generate a signal with noise
t = np.linspace(0, 1, 1000)
clean_signal = np.sin(2 * np.pi * 5 * t)
noisy_signal = clean_signal + 0.5 * np.random.normal(size=1000)

# Create a low-pass filter
b, a = signal.butter(3, 0.05)
filtered_signal = signal.filtfilt(b, a, noisy_signal)

# (Plotting code would go here to visualize the result)


from scipy.interpolate import interp1d

# Sample data points
x = np.array([0, 1, 2, 3])
y = np.array([0, 2, 0, 2])

# Create a cubic interpolation function
f_cubic = interp1d(x, y, kind='cubic')

# Predict a value between 1 and 2
x_new = 1.5
print(f"Interpolated value at 1.5: {f_cubic(x_new):.2f}")


from scipy.interpolate import interp1d

# Sample data points
x = np.array([0, 1, 2, 3])
y = np.array([0, 2, 0, 2])

# Create a cubic interpolation function
f_cubic = interp1d(x, y, kind='cubic')

# Predict a value between 1 and 2
x_new = 1.5
print(f"Interpolated value at 1.5: {f_cubic(x_new):.2f}")


from scipy import linalg

# Define a matrix
A = np.array([[1, 2], [3, 4]])

# Compute the determinant
det = linalg.det(A)

# Compute the inverse
inv = linalg.inv(A)

print(f"Determinant: {det}")