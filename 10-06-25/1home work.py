# Write a python program to read password as input from the user and check whether it is valid or invalid
# At least 3 upper case letters
# At least 3 lower case letters
# At least 3 special characters
# At least 1 number
# Password length should not be less than 10

import string

password = input("Enter your password: ")

upper = lower = digit = special = 0

for ch in password:
    if ch.isupper():
        upper += 1
    elif ch.islower():
        lower += 1
    elif ch.isdigit():
        digit += 1
    elif ch in string.punctuation:
        special += 1
    else:
        special += 1  # Count any other non-alphanumeric as special

if (len(password) >= 10 and
    upper >= 3 and
    lower >= 3 and
    special >= 3 and
    digit >= 1):
    print("Valid password")
else:
    print("Invalid password")