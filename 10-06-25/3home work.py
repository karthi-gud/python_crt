# Write a python program to read a string as input from the user and split the string into 3 equal halves using slicing

s = input("Enter a string: ")
n = len(s)
size = n // 3

# If not divisible by 3, the last part will have the extra characters
part1 = s[:size]
part2 = s[size:2*size]
part3 = s[2*size:]

print("First part:",part1)
print("Second part:",part2)
print("Third part:",part3)