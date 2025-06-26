import tkinter as tk
from tkinter import ttk, messagebox

def calculate_bmi():
    try:
        weight_str = weight_entry.get()
        height_str = height_entry.get()

        if not weight_str or not height_str:
            messagebox.showerror("Error", "Please enter both weight and height.")
            return

        weight = float(weight_str)
        height = float(height_str)

        weight_unit = weight_unit_var.get()
        height_unit = height_unit_var.get()

        # Convert to metric (kg and meters)
        if weight_unit == "lbs":
            weight *= 0.453592  # pounds to kilograms
        if height_unit == "feet":
            height *= 0.3048   # feet to meters

        # Check for valid height (cannot be zero or negative for BMI calculation)
        if height <= 0:
            messagebox.showerror("Error", "Height cannot be zero or negative. Please enter a valid height.")
            return

        bmi = weight / (height ** 2)
        bmi_display.set(f"Your BMI: {bmi:.2f}")

        category = ""
        suggested_weight_range = ""
        suggested_height_range = ""

        # BMI Categories and Suggestions
        if bmi < 18.5:
            category = "Underweight"
            # For underweight, suggest reaching the lower end of normal weight range
            lower_normal_weight = 18.5 * (height ** 2)
            upper_normal_weight = 24.9 * (height ** 2)
            suggested_weight_range = f"Consider aiming for {lower_normal_weight:.1f}-{upper_normal_weight:.1f} kg"
        elif 18.5 <= bmi < 25:
            category = "Normal Weight"
            # For normal weight, suggest staying within the range
            lower_normal_weight = 18.5 * (height ** 2)
            upper_normal_weight = 24.9 * (height ** 2)
            suggested_weight_range = f"Maintain a weight between {lower_normal_weight:.1f}-{upper_normal_weight:.1f} kg"
        elif 25 <= bmi < 30:
            category = "Overweight"
            # For overweight, suggest aiming for the upper end of normal weight range
            lower_normal_weight = 18.5 * (height ** 2)
            upper_normal_weight = 24.9 * (height ** 2)
            suggested_weight_range = f"Consider aiming for {lower_normal_weight:.1f}-{upper_normal_weight:.1f} kg"
        else:
            category = "Obese"
            # For obese, suggest aiming for the upper end of normal weight range
            lower_normal_weight = 18.5 * (height ** 2)
            upper_normal_weight = 24.9 * (height ** 2)
            suggested_weight_range = f"Consider aiming for {lower_normal_weight:.1f}-{upper_normal_weight:.1f} kg"

        bmi_category_display.set(f"Category: {category}")
        suggested_ranges_display.set(f"Suggestions: {suggested_weight_range}") # We'll keep height suggestion simple here

    except ValueError:
        messagebox.showerror("Error", "Invalid input. Please enter numbers for weight and height.")
    except Exception as e:
        messagebox.showerror("An unexpected error occurred", str(e))

# --- Set up the main window ---
root = tk.Tk()
root.title("BMI Calculator")
root.geometry("400x400") # Set initial window size
root.config(bg="#e0f2f7") # Light blue background

# --- Variables to store input and output ---
weight_entry = tk.StringVar()
height_entry = tk.StringVar()
weight_unit_var = tk.StringVar(value="kg") # Default weight unit
height_unit_var = tk.StringVar(value="meters") # Default height unit
bmi_display = tk.StringVar(value="Your BMI: ")
bmi_category_display = tk.StringVar(value="Category: ")
suggested_ranges_display = tk.StringVar(value="Suggestions: ")

# --- Input Frames (for better organization) ---
input_frame = ttk.Frame(root, padding="15")
input_frame.pack(pady=10)

# Weight Input
ttk.Label(input_frame, text="Weight:", font=("Arial", 12)).grid(row=0, column=0, padx=5, pady=5, sticky="w")
ttk.Entry(input_frame, textvariable=weight_entry, width=15, font=("Arial", 12)).grid(row=0, column=1, padx=5, pady=5)
weight_unit_menu = ttk.Combobox(input_frame, textvariable=weight_unit_var,
                                 values=["kg", "lbs"], state="readonly", width=5)
weight_unit_menu.grid(row=0, column=2, padx=5, pady=5)

# Height Input
ttk.Label(input_frame, text="Height:", font=("Arial", 12)).grid(row=1, column=0, padx=5, pady=5, sticky="w")
ttk.Entry(input_frame, textvariable=height_entry, width=15, font=("Arial", 12)).grid(row=1, column=1, padx=5, pady=5)
height_unit_menu = ttk.Combobox(input_frame, textvariable=height_unit_var,
                                 values=["meters", "feet"], state="readonly", width=7)
height_unit_menu.grid(row=1, column=2, padx=5, pady=5)

# --- Calculate Button ---
calculate_button = ttk.Button(root, text="Calculate BMI", command=calculate_bmi, style="TButton")
calculate_button.pack(pady=10)

# --- Results Display Frame ---
results_frame = ttk.LabelFrame(root, text="Results", padding="15")
results_frame.pack(pady=10, fill="x", padx=20)

ttk.Label(results_frame, textvariable=bmi_display, font=("Arial", 14, "bold")).pack(pady=5, anchor="w")
ttk.Label(results_frame, textvariable=bmi_category_display, font=("Arial", 12)).pack(pady=5, anchor="w")
ttk.Label(results_frame, textvariable=suggested_ranges_display, font=("Arial", 10, "italic"), wraplength=300).pack(pady=5, anchor="w")

# --- Run the application ---
root.mainloop()