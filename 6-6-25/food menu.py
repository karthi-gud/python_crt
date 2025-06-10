#write a python prograsem 
# 1. to display a menu of food items (list)
# 2. create a tuple of prices with respect to food items list
# 3. read the input from the user for ordering the food including the quanttity 
#3a. if it exist in the menu -- confirm order
# 3b. if not print a message ----
# 4. while billinig read the phone number , feedback ,read tip amount
# 5. add 18% tax to the total bill print the bill if bill > 0
n=int(input("Enter the number of words you want to input: "))
list=['chicken fry','chicken pakodi','chicken dum','chicken curry','chicken biryani','ice cream','chocolate cake','pasta','pizza','burger']
tuple=(250, 200, 300, 350, 400, 150, 100, 200, 250, 300)
order = {}
while True:
    food_item = input("Enter a food item from the menu (or type 'exit' to finish): ")
    if food_item.lower() == 'exit':
        break
    if food_item in list:
        quantity = int(input(f"How many {food_item} would you like to order? "))
        index = list.index(food_item)
        order[food_item] = (tuple[index], quantity)  # Store price and quantity
        print(f"Order confirmed for {quantity} {food_item}(s).")
    else:
        print("This item is not on the menu. Please choose from the menu.")
# Calculate total bill
total_bill = 0
for item, (price, quantity) in order.items():
    total_bill += price * quantity
# Add tax
tax = total_bill * 0.18
total_bill += tax
# Print the bill
if total_bill > 0:
    print("\n--- Bill Summary ---")
    for item, (price, quantity) in order.items():
        print(f"{item}: {quantity} x {price} = {quantity * price}")
    print(f"Total Bill (including 18% tax): {total_bill:.2f}")
# Collect additional information
phone_number = input("Please enter your phone number: ")
feedback = input("Please provide your feedback: ")
tip = float(input("Please enter the tip amount: "))
total_bill += tip
print(f"Total amount to be paid (including tip): {total_bill:.2f}")
# Thank you for your order!
print("Thank you for your order!")
# This program allows users to order food from a menu, calculates the total bill including tax and tip, and collects feedback.


# Food menu and prices
""""menu = {
    'chicken fry': 250,
    'chicken pakodi': 200,
    'chicken dum': 300,
    'chicken curry': 350,
    'chicken biryani': 400,
    'ice cream': 150,
    'chocolate cake': 100,
    'pasta': 200,
    'pizza': 250,
    'burger': 300
}

print("Welcome to our restaurant!")
print("Menu:", list(menu.keys()))

order = {}
total = 0

# Take orders
while True:
    item = input("\nEnter food item (or 'done' to finish): ").lower()
    
    if item == 'done':
        break
    
    if item in menu:
        qty = int(input(f"Quantity for {item}: "))
        order[item] = order.get(item, 0) + qty
        print(f"Added {qty} {item}(s)")
    else:
        print("Item not available!")

# Calculate bill
if order:
    print("\n--- BILL ---")
    for item, qty in order.items():
        cost = menu[item] * qty
        total += cost
        print(f"{item}: {qty} x ₹{menu[item]} = ₹{cost}")
    
    # Add tax
    tax = total * 0.18
    total += tax
    print(f"\nSubtotal: ₹{total-tax:.2f}")
    print(f"Tax (18%): ₹{tax:.2f}")
    
    # Add tip
    tip = float(input("Enter tip amount: ₹"))
    total += tip
    
    print(f"\nFinal Total: ₹{total:.2f}")
    print("Thank you for your order!")
else:
    print("No items ordered!")"""