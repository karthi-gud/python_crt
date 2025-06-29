import numpy as np
import matplotlib.pyplot as plt

# Create a figure to hold all subplots (recommended when using subplots)
plt.figure(figsize=(12, 8)) # Adjusted for better visual spacing of 6 plots

# Plot 1: Top-Left
x = np.array([0, 1, 2, 3])
y = np.array([3, 8, 1, 10])
plt.subplot(2, 3, 1) # 2 rows, 3 columns, 1st plot
plt.plot(x, y)
plt.title("Plot-1", loc="left")

# Plot 2: Top-Middle
x = np.array([0, 1, 2, 3])
y = np.array([10, 20, 30, 40])
plt.subplot(2, 3, 2) # 2 rows, 3 columns, 2nd plot
plt.plot(x, y)
plt.title("Plot-2", loc="left")

# Plot 3: Top-Right
x = np.array([0, 1, 2, 3])
y = np.array([3, 8, 1, 10])
plt.subplot(2, 3, 3) # 2 rows, 3 columns, 3rd plot
plt.plot(x, y)
plt.title("Plot-3")

# Plot 4: Bottom-Left
x = np.array([0, 1, 2, 3])
y = np.array([10, 20, 30, 40])
plt.subplot(2, 3, 4) # 2 rows, 3 columns, 4th plot
plt.plot(x, y)
plt.title("Plot-4")

# Plot 5: Bottom-Middle
x = np.array([0, 1, 2, 3])
y = np.array([3, 8, 1, 10])
plt.subplot(2, 3, 5) # 2 rows, 3 columns, 5th plot
plt.plot(x, y)
plt.title("Plot-5")

# Plot 6: Bottom-Right
x = np.array([0, 1, 2, 3])
y = np.array([10, 20, 30, 40])
plt.subplot(2, 3, 6) # 2 rows, 3 columns, 6th plot
plt.plot(x, y)
plt.title("Plot-6", loc="left")

# Corrected line: Ensure no extra spaces or hidden characters here
plt.tight_layout()

plt.show()