#writea python program input a list of numbers create two new lists one for the even numbers and othewr is for the odd numbers display both the list
user_input = input("Enter a list of numbers separated by spaces: ")
numbers = list(map(int, user_input.split()))
even_numbers = [num for num in numbers if num % 2 == 0]
odd_numbers = [num for num in numbers if num % 2 != 0]
print("Even numbers:", even_numbers)  
print("Odd numbers:", odd_numbers)  