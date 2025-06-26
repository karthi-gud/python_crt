import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D # This is essential for 3D plots
import seaborn as sns # For nice color palettes, though we'll customize a bit

# --- 1. Set a dark, futuristic style ---
plt.style.use('dark_background') # Start with a dark background
sns.set_palette('viridis') # A good default color palette for continuous data

# --- 2. Create Data for the 3D Plot ---
# We'll create a meshgrid for X and Y coordinates
x = np.linspace(-5, 5, 100)
y = np.linspace(-5, 5, 100)
X, Y = np.meshgrid(x, y)

# Create a complex, wavy Z-axis data for a futuristic surface
# Using multiple sine and cosine waves for an intricate pattern
Z = np.sin(np.sqrt(X**2 + Y**2) * 2) + np.cos(X * Y / 3) * 0.5 + np.sin(X/2) * np.cos(Y/2) * 0.8

# --- 3. Create the 3D Figure and Axes ---
fig = plt.figure(figsize=(10, 8)) # Set the figure size
ax = fig.add_subplot(111, projection='3d') # Add a 3D subplot

# --- 4. Plot the 3D Surface ---
# Using `plot_surface` for a continuous, flowing look
# `cmap` (colormap) is crucial for the futuristic feel.
# 'viridis', 'plasma', 'magma', 'cividis' are good choices for dark backgrounds.
# 'coolwarm' or 'RdBu' can give a different contrast.
surface = ax.plot_surface(X, Y, Z, cmap='plasma', edgecolor='none', alpha=0.8)

# --- 5. Add Futuristic Touches and Labels ---
ax.set_title('Futuristic Waveform Surface', fontsize=20, color='cyan', fontweight='bold')
ax.set_xlabel('X-Axis (Frequency)', fontsize=12, color='lightgray')
ax.set_ylabel('Y-Axis (Amplitude)', fontsize=12, color='lightgray')
ax.set_zlabel('Z-Axis (Signal Strength)', fontsize=12, color='lightgray')

# Customize tick labels color
ax.tick_params(axis='x', colors='lightgray')
ax.tick_params(axis='y', colors='lightgray')
ax.tick_params(axis='z', colors='lightgray')

# Remove grid lines for a cleaner, more abstract look
ax.grid(False)

# Customize the background pane colors to be dark
ax.xaxis.pane.fill = False
ax.yaxis.pane.fill = False
ax.zaxis.pane.fill = False
ax.xaxis.pane.set_edgecolor('lightgray')
ax.yaxis.pane.set_edgecolor('lightgray')
ax.zaxis.pane.set_edgecolor('lightgray')

# Add a color bar to show the Z-axis mapping
cbar = fig.colorbar(surface, shrink=0.5, aspect=10, pad=0.1)
cbar.set_label('Value', color='lightgray', fontsize=12)
cbar.ax.yaxis.set_tick_params(colors='lightgray')

# Adjust the view angle for a more dramatic perspective
ax.view_init(elev=30, azim=-120) # elev is elevation, azim is azimuth

# --- 6. Show the Plot ---
plt.show()