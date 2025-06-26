import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

# --- 1. Set a nice style for the plots ---
# This makes plots generally look more professional and aesthetically pleasing
sns.set_style("whitegrid") # or "darkgrid", "ticks", "white", "dark"
plt.style.use('seaborn-v0_8-deep') # Using a specific Seaborn style for colors

# --- 2. Create some interesting data ---
# Let's imagine daily temperature fluctuations or stock prices
dates = pd.to_datetime(pd.date_range(start='2024-01-01', periods=100, freq='D'))
temperature = 20 + 5 * np.sin(np.linspace(0, 3 * np.pi, 100)) + np.random.randn(100) * 1.5
humidity = 60 + 10 * np.cos(np.linspace(0, 2 * np.pi, 100)) + np.random.randn(100) * 2

# Create a DataFrame for better organization
df = pd.DataFrame({
    'Date': dates,
    'Temperature': temperature,
    'Humidity': humidity
})

# --- 3. Create the beautiful graph ---
plt.figure(figsize=(12, 6)) # Set the size of the plot (width, height)

# Plot Temperature
sns.lineplot(x='Date', y='Temperature', data=df, label='Temperature (°C)',
             color='#FF6347', linewidth=2.5) # Tomato color, thicker line

# Plot Humidity on a secondary y-axis (if it makes sense for your data)
# This requires a bit more matplotlib specific code
ax2 = plt.gca().twinx() # Create a second y-axis that shares the same x-axis
sns.lineplot(x='Date', y='Humidity', data=df, label='Humidity (%)',
             color='#4682B4', linewidth=2.5, ax=ax2) # SteelBlue color, thicker line

# --- 4. Add Impressive Touches ---
plt.title('Daily Weather Trends: Temperature and Humidity', fontsize=18, fontweight='bold', color='#333333')
plt.xlabel('Date', fontsize=14, color='#555555')

# Set labels for both y-axes
plt.ylabel('Temperature (°C)', fontsize=14, color='#FF6347') # Temperature label on left
ax2.set_ylabel('Humidity (%)', fontsize=14, color='#4682B4') # Humidity label on right

plt.tick_params(axis='x', labelsize=12) # Size of x-axis ticks
plt.tick_params(axis='y', labelsize=12) # Size of left y-axis ticks
ax2.tick_params(axis='y', labelsize=12) # Size of right y-axis ticks

plt.legend(loc='upper left', fontsize=12, frameon=True, shadow=True, borderpad=1) # Place legend, add shadow
ax2.legend(loc='upper right', fontsize=12, frameon=True, shadow=True, borderpad=1)

plt.grid(True, linestyle='--', alpha=0.7) # Make grid lines subtle
plt.tight_layout() # Adjust plot to ensure everything fits without overlapping

# Add a subtle text annotation
plt.text(df['Date'].iloc[0], plt.ylim()[0] * 1.05, "Data from Jan-Apr 2024",
         fontsize=10, color='gray', ha='left', va='bottom')

# --- 5. Show the plot ---
plt.show()