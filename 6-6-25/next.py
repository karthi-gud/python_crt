#write a python program to declare a list of grocerry items and create the input read the input fromm the user from one to five 
#1 to display the list of grocerry items in sorted way
#2 to take the input from the userr and add items to the cart
#3 to give the cart items
#4 to update the quantity ar item present in the cart
#5 generare a bill including item name, quantity, price and if the final bill amount is greater than 1000 then the user will get 10 $discount
#if the user purchases any item more than 10 kg reduce the amout of 1kg frm that particular items price 
# if the user purchase any particular product add buy one get one free offer to it
#so add 25% gst to the overall bill and print the final bill
#other than 1-5 options print a message that the option is not available
#after printing bill exit the program
#write a python program to declare a list of grocery items and create the input read the input from the user from one to five
items = ['oil','rice','dal','salt','pepper']
tuple=(50, 40, 60, 20, 30) 
cart = {}
while True:
    print("\n Grocery menu:")
    for i, item in enumerate(items):
        print(f"{i + 1}. {item} - ${tuple[i]}")
    print("6. Exit")
    choice = int(input("Enter your choice (1-6): "))

    if choice == 1:
        print("\nGrocery items in sorted order:")
        for item in sorted(items):
            print(item)
    elif choice == 2:
        item_name = input("Enter the grocery item you want to add to the cart: ")
        if item_name in items:
            quantity = int(input(f"Enter the quantity of {item_name} (in kg): "))
            index = items.index(item_name)
            if item_name in cart:
                cart[item_name]['quantity'] += quantity
            else:
                cart[item_name] = {'quantity': quantity, 'price': tuple[index]}
            print(f"{quantity} kg of {item_name} added to the cart.")
        else:
            print("Item not found in the grocery list.")
    elif choice == 3:
        if cart:
            print("\nItems in your cart:")
            for item, details in cart.items():
                print(f"{item}: {details['quantity']} kg at ${details['price']} each")
        else:
            print("Your cart is empty.")
    elif choice == 4:
        item_name = input("Enter the grocery item you want to update: ")
        if item_name in cart:
            quantity = int(input(f"Enter the new quantity for {item_name} (in kg): "))
            cart[item_name]['quantity'] = quantity
            print(f"Updated {item_name} quantity to {quantity} kg.")
        else:
            print("Item not found in the cart.")
    elif choice == 5:
        if not cart:
            print("Your cart is empty. Cannot generate bill.")
            continue
        
        total_bill = 0
        discount = 0
        gst = 0.25
        print("\n--- Bill Summary ---")
        for item, details in cart.items():
            quantity = details['quantity']
            price_per_kg = details['price']
            item_total = quantity * price_per_kg
            
            # Apply discount for more than 10 kg
            if quantity > 10:
                item_total -= price_per_kg
            # Apply buy one get one free offer
            if quantity >= 2:
                item_total -= price_per_kg * (quantity // 2)
            total_bill += item_total
        # Apply discount if total bill is greater than 1000
        if total_bill > 1000:
            discount = 10
            total_bill -= discount
        # Apply GST
        total_bill += total_bill * gst
        print(f"Total Bill (after discount and GST): ${total_bill:.2f}")
        print(f"Discount applied: ${discount}")
        print("Thank you for shopping with us!")
    elif choice == 6:
        print("Exiting the program. Thank you!")
        break
    else:
        print("Invalid option. Please choose a valid option (1-6).")
# This program allows users to manage a grocery list, add items to a cart, update quantities, and generate a bill with discounts and GST.
# This program allows users to manage a grocery list, add items to a cart, update quantities, and generate a bill with discounts and GST.
# This program allows users to manage a grocery list, add items to a cart, update quantities, and generate a bill with discounts and GST.


