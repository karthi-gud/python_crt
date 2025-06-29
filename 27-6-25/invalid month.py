#write a python program to read the month number as input from the user and check wether it is valid month number or not 


# Read month number from user
month = int(input("Enter month number: "))

# Check if valid month
if 1 <= month <= 12:
    print("Valid month")
else:
    print("Invalid month")
