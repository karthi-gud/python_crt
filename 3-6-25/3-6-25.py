#print the number is positive or negative
n = int(input())
if n > 0:
    print(f"{n}is a Positive")
elif n < 0:
    print(f"{n}is a Negative")
else:
    print(f"{n}is a Zero")
#using of ternary operator
print(f"{n} is a {'Positive' if n > 0 else 'Negative' if n < 0 else 'Zero'}")
#write a python program from user to check wether it is a digit or number
n = input("Enter a number: ")
if n.isdigit():
    print(f"{n} is a digit")
else:
    print(f"{n} is not a digit")    
#using of ternary operator
print(f"{n} is a {'digit' if n.isdigit() else 'not a digit'}") 
#write a python program to read the input integer from the user and check wether it is 2 digit number or not a two digit number
n = int(input("Enter a number: "))
if 10 <= abs(n) < 100:
    print(f"{n} is a two digit number")
else:   
    print(f"{n} is not a two digit number")     
#using of ternary operator
print(f"{n} is a {'two digit number' if 10 <= abs(n) < 100 else 'not a two digit number'}")
#to read amount as input from the user and print the number of notes required in india currency dimesions
amount = int(input("Enter the amount: "))
print("2000 notes:", amount // 2000)
amount %= 2000  
print("500 notes:", amount // 500)
amount %= 500   
print("200 notes:", amount // 200)
amount %= 200
print("100 notes:", amount // 100)
amount %= 100
print("50 notes:", amount // 50)
amount %= 50
print("20 notes:", amount // 20)
amount %= 20
print("10 notes:", amount // 10)
amount %= 10
print("5 notes:", amount // 5)
amount %= 5
print("2 notes:", amount // 2)
amount %= 2
print("1 notes:", amount // 1)
amount %= 1
#write a python program to read an integer value as input fo the user and print multiplication table of that number
n = int(input("Enter a number: "))
for i in range(1, 11):
    print(f"{n} x {i} = {n * i}")
# writ a multiplication from 1 to n where n is a n user input
n = int(input("Enter a number: "))
for i in range(1, n + 1):
    for j in range(1, 11):
        print(f"{i} x {j} = {i * j}")
    print()  # Print a new line after each table
# write a python program to print reversed multiplication table of n
n = int(input("Enter a number: "))
for i in range(10, 0, -1):
    print(f"{n} x {i} = {n * i}")   
#write a pyton to print the reversed multiplication tables of ont to n where n is a user input
n = int(input("Enter a number: "))
for i in range(n, 0, -1):
    for j in range(10, 0, -1):
        print(f"{i} x {j} = {i * j}")
    print()  # Print a new line after each table
#write a python program to print the reversed multiplication table from n to one
n = int(input("Enter a number: "))
for i in range(n, 0, -1):
    for j in range(10, 0, -1):
        print(f"{i} x {j} = {i * j}")
    print()  # Print a new line after each table
#write a python program to read the integer value as user and print the sum of all the digits of that number
n = input("Enter a number: ")
sum_of_digits = sum(int(digit) for digit in n)
print(f"The sum of the digits of {n} is {sum_of_digits}")

#write a python program to read the input as integer print the number of even digits and the number of odd digits in that number
#write a pyrhon program to read the integer value from the user and find the summation of even digits and the odd digits present in that particular number
# writea pyhon program to read ther input value from the user and fiond the number of zeros present in the user entered number