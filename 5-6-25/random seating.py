#write a python progrmam store 10 studen names   swap the positio of any two students   print the new seating arrangement
# Initialize a list with 10 student names
students = [
    "Alice", "Bob", "Charlie", "David", "Eve",
    "Frank", "Grace", "Hannah", "Ian", "Jack"
]
# Display the original seating arrangement
print("Original seating arrangement:")
for i, student in enumerate(students, start=1):
    print(f"{i}. {student}")
# Get the positions of the two students to swap
pos1 = int(input("Enter the position of the first student to swap (1-10): ")) - 1
pos2 = int(input("Enter the position of the second student to swap (1-10): ")) - 1
# Validate positions
if 0 <= pos1 < len(students) and 0 <= pos2 < len(students):
    # Swap the students
    students[pos1], students[pos2] = students[pos2], students[pos1]
    # Display the new seating arrangement
    print("\nNew seating arrangement:")
    for i, student in enumerate(students, start=1):
        print(f"{i}. {student}")
else:
    print("Invalid positions entered. Please enter numbers between 1 and 10.")
# This code allows the user to swap the positions of two students in a list of 10 students and displays the new seating arrangement.
# Note: The code assumes that the user will enter valid integers for positions.
# If the user enters invalid positions, an error message will be displayed.
#writea a python program to read 2 integer values as iput from user and sweap the numbers
# Read two integer values from the user
num1 = int(input("Enter the first integer: "))
num2 = int(input("Enter the second integer: "))
# Swap the numbers
num1, num2 = num2, num1
# Display the swapped numbers
print(f"After swapping: First integer = {num1}, Second integer = {num2}")
# This code reads two integer values from the user, swaps them, and displays the swapped values.
#write a python program to read 2 integer values as input from user and swap the numbers
# Read two integer values from the user
# num1 = int(input("Enter the first integer: "))
# num2 = int(input("Enter the second integer: "))
# Swap the numbers
# num1, num2 = num2, num1
# Display the swapped numbers
# print(f"After swapping: First integer = {num1}, Second integer = {num2}")
# This code reads two integer values from the user, swaps them, and displays the swapped values.

    #write a python program to read 2 integer vlue from as input from user 1-> add 2 numbers withou using adition operator without using pre defined methods and functions
   # 2->substract without suing - operator and without using pre defined methods a or function