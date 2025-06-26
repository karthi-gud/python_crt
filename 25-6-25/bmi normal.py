def calculate_bmi_terminal():
    """
    Calculates Body Mass Index (BMI) based on user input from the terminal.
    It handles different units and provides a BMI category.
    """
    print("--- Simple BMI Calculator ---")

    # 1. Get Weight Input
    while True:
        try:
            weight_str = input("Enter your weight: ")
            weight = float(weight_str)
            if weight <= 0:
                print("Weight must be a positive number. Please try again.")
            else:
                break
        except ValueError:
            print("Invalid input. Please enter a number for weight.")

    # 2. Get Weight Unit
    while True:
        weight_unit = input("Is your weight in kilograms (kg) or pounds (lbs)? (Type 'kg' or 'lbs'): ").lower().strip()
        if weight_unit in ['kg', 'lbs']:
            break
        else:
            print("Invalid unit. Please type 'kg' or 'lbs'.")

    # 3. Get Height Input
    while True:
        try:
            height_str = input("Enter your height: ")
            height = float(height_str)
            if height <= 0:
                print("Height must be a positive number. Please try again.")
            else:
                break
        except ValueError:
            print("Invalid input. Please enter a number for height.")

    # 4. Get Height Unit
    while True:
        height_unit = input("Is your height in meters (m) or feet (ft)? (Type 'm' or 'ft'): ").lower().strip()
        if height_unit in ['m', 'ft']:
            break
        else:
            print("Invalid unit. Please type 'm' or 'ft'.")

    # --- Convert to Metric (kg and meters) for Calculation ---
    final_weight_kg = weight
    if weight_unit == "lbs":
        final_weight_kg = weight * 0.453592 # Convert pounds to kilograms

    final_height_m = height
    if height_unit == "ft":
        final_height_m = height * 0.3048   # Convert feet to meters

    # --- Calculate BMI ---
    if final_height_m == 0: # Should not happen if input validation is strict, but good to prevent division by zero
        print("Error: Height cannot be zero. Cannot calculate BMI.")
        return

    bmi = final_weight_kg / (final_height_m ** 2)

    # --- Determine BMI Category ---
    category = ""
    if bmi < 18.5:
        category = "Underweight"
    elif 18.5 <= bmi < 25:
        category = "Normal Weight"
    elif 25 <= bmi < 30:
        category = "Overweight"
    else:
        category = "Obese"

    # --- Display Results ---
    print("\n--- BMI Results ---")
    print(f"Your calculated BMI: {bmi:.2f}") # .2f formats to 2 decimal places
    print(f"Your BMI Category: {category}")
    print("--------------------")

# Call the function to run the calculator
if __name__ == "__main__":
    calculate_bmi_terminal()