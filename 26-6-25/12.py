import numpy as np
import matplotlib.pyplot as plt

# Create a single figure to hold all subplots.
# You can adjust figsize (width, height) to make it larger or smaller.
plt.figure(figsize=(12, 10)) # A good size to display 4 plots clearly

# --- Plot 1: Top-Left ---
# plt.subplot(rows, columns, plot_number)
plt.subplot(2, 2, 1) # This places the plot in the first position of a 2x2 grid
x1 = np.array([0, 1, 2, 3])
y1 = np.array([3, 8, 1, 10])
plt.plot(x1, y1, marker='o', linestyle='-', color='skyblue')
plt.title("Plot 1: Sales Trends (Line)")
plt.xlabel("Quarter")
plt.ylabel("Revenue (Units)")
plt.grid(True, linestyle='--', alpha=0.7) # Add a subtle grid

# --- Plot 2: Top-Right ---
plt.subplot(2, 2, 2) # This places the plot in the second position
x2 = np.array([0, 1, 2, 3])
y2 = np.array([10, 20, 30, 40])
plt.plot(x2, y2, marker='^', linestyle='--', color='lightcoral')
plt.title("Plot 2: Growth Over Time (Dashed Line)")
plt.xlabel("Year")
plt.ylabel("Growth Index")
plt.grid(True, linestyle='--', alpha=0.7)

# --- Plot 3: Bottom-Left ---
plt.subplot(2, 2, 3) # This places the plot in the third position
x3 = np.array([0, 1, 2, 3])
y3 = np.array([6, 2, 9, 5])
plt.bar(x3, y3, color='lightgreen') # Using a bar chart for variety
plt.title("Plot 3: Customer Feedback (Bar)")
plt.xlabel("Category")
plt.ylabel("Satisfaction Score")
plt.grid(axis='y', linestyle='--', alpha=0.7) # Grid only on y-axis for bar chart

# --- Plot 4: Bottom-Right ---
plt.subplot(2, 2, 4) # This places the plot in the fourth position
x4 = np.array([0, 1, 2, 3])
y4 = np.array([45, 25, 60, 35])
plt.plot(x4, y4, marker='s', linestyle=':', color='mediumpurple')
plt.title("Plot 4: Resource Usage (Dotted Line)")
plt.xlabel("Phase")
plt.ylabel("Usage (%)")
plt.grid(True, linestyle='--', alpha=0.7)

# Adjust layout to prevent titles/labels from overlapping between subplots
plt.tight_layout()

# Display the figure with all four plots
plt.show()















import numpy as np
import matplotlib.pyplot as plt

# Create a single figure to hold all subplots
plt.figure(figsize=(12, 10)) # Good size for four plots

# --- Plot 1: Steady Sales Growth ---
plt.subplot(2, 2, 1) # Top-Left
months = np.array(['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun'])
sales1 = np.array([50, 55, 60, 65, 70, 75])
plt.plot(months, sales1, marker='o', linestyle='-', color='skyblue')
plt.title("Plot 1: Monthly Sales Growth")
plt.xlabel("Month")
plt.ylabel("Units Sold")
plt.grid(True, linestyle='--', alpha=0.7)

# --- Plot 2: Quarterly Revenue Fluctuations ---
plt.subplot(2, 2, 2) # Top-Right
quarters = np.array(['Q1', 'Q2', 'Q3', 'Q4'])
revenue2 = np.array([120, 90, 150, 110]) # Fluctuating revenue
plt.plot(quarters, revenue2, marker='^', linestyle='--', color='lightcoral')
plt.title("Plot 2: Quarterly Revenue Fluctuations")
plt.xlabel("Quarter")
plt.ylabel("Revenue ($K)")
plt.grid(True, linestyle='--', alpha=0.7)

# --- Plot 3: Product A vs. Product B Sales ---
plt.subplot(2, 2, 3) # Bottom-Left
years = np.array([2022, 2023, 2024, 2025])
product_a_sales = np.array([80, 95, 110, 105])
product_b_sales = np.array([70, 75, 85, 100])
plt.plot(years, product_a_sales, marker='s', linestyle='-', color='lightgreen', label='Product A')
plt.plot(years, product_b_sales, marker='D', linestyle='--', color='gold', label='Product B')
plt.title("Plot 3: Product Sales Comparison")
plt.xlabel("Year")
plt.ylabel("Units Sold")
plt.legend() # Show the legend for product A and B
plt.grid(True, linestyle='--', alpha=0.7)

# --- Plot 4: Weekly Sales Performance ---
plt.subplot(2, 2, 4) # Bottom-Right
weeks = np.array(['Week 1', 'Week 2', 'Week 3', 'Week 4'])
performance4 = np.array([70, 65, 80, 72])
plt.plot(weeks, performance4, marker='x', linestyle=':', color='mediumpurple')
plt.title("Plot 4: Weekly Performance Index")
plt.xlabel("Week")
plt.ylabel("Sales Index")
plt.grid(True, linestyle='--', alpha=0.7)

# Adjust layout to prevent titles/labels from overlapping
plt.tight_layout()

# Display the figure with all four plots
plt.show()