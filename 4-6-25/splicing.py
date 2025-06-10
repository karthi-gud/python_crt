#splicing
numbers=[1,2,3,4,5,6,7,8,9]
print(numbers[2:5])  # [3, 4, 5]
print(numbers[2:])   # [3, 4, 5, 6, 7, 8, 9]
print(numbers[:5])   # [1, 2, 3, 4, 5]
print(numbers[2:5:2])  # [3, 5]
print(numbers[::2])  # [1, 3, 5, 7, 9]
print(numbers[::-1])  # [9, 8, 7, 6, 5, 4, 3, 2, 1]
# List comprehension
squares = [x**2 for x in range(10)]
print(squares)  # [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
# List comprehension with condition
evens = [x for x in range(10) if x % 2 == 0]
print(evens)  # [0, 2, 4, 6, 8]


#write apyhon program to reverse rhe lisst of numbers without using reverse method
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
reversed_numbers = []
for i in range(len(numbers) - 1, -1, -1):
    reversed_numbers.append(numbers[i])
print(reversed_numbers)  # [9, 8, 7, 6, 5, 4, 3, 2, 1]

#write a pythhon program to sort a list of numbers without using sort method 
numbers = [5, 2, 9, 1, 5, 6]
for i in range(len(numbers)):
    for j in range(0, len(numbers) - i - 1):
        if numbers[j] > numbers[j + 1]:
            numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]
print(numbers)  # [1, 2, 5, 5, 6, 9]
