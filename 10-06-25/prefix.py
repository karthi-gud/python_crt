# Write a python program to take name as input from the user including prefix (Mr/Ms)
# Print the gender classification of the name on basis of prefix

string = input("Enter your name with Mr/Ms: ").strip()

if string.lower().startswith("mr"):
    print("Gender: Male")
elif string.lower().startswith("ms"):
    print("Gender: Female")
else:
    print("Prefix not recognized")