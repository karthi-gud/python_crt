#write a python program to print even numbers from 1 to n using list comprehension
n = int(input("Enter the value of n: "))
even_numbers = [i for i in range(1, n+1) if i % 2 == 0]
print("Even numbers from 1 to", n, "are:", even_numbers)