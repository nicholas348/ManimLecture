import matplotlib.pyplot as plt
import numpy as np

# 1. Prepare the data
x = np.linspace(0, 10, 100) # 100 points from 0 to 10
y1 = np.sin(x)
y2 = np.cos(x)

# 2. Create the plot
plt.figure(figsize=(8, 5)) # Set the window size

# 3. Add data with styling
plt.plot(x, y1, label='Sine Wave', color='blue', linestyle='-', linewidth=2)
plt.plot(x, y2, label='Cosine Wave', color='red', linestyle='--', linewidth=2)

# 4. Customize the chart
plt.title('Trigonometric Functions', fontsize=14)
plt.xlabel('Time (s)')
plt.ylabel('Amplitude')
plt.grid(True, linestyle=':', alpha=0.6) # Add a subtle grid
plt.legend() # Show the labels defined in plt.plot

# 5. Display the result
plt.show()