#writa a python program to read the list of elements as input from the user and proint ther new list which are multiple of 5
user_input = input("Enter a list of numbers separated by spaces: ")
numbers = list(map(int, user_input.split()))
multiples_of_5 = [num for num in numbers if num % 5 == 0]
print("Numbers that are multiples of 5:", multiples_of_5)  # Example output: [5, 10, 15]

#write a python program to read the list elemnts from the user and chesk wether the list elements are multiples of 3 and 5 or not and print the list of elements which are multiples of 3 and 5