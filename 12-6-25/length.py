#compare two strings of the same length and print the index where there is change

s1 = input("Enter first string: ")
s2 = input("Enter second string: ")

if len(s1) != len(s2):
    print("Strings are not of the same length.")
else:
    for i in range(len(s1)):
        if s1[i] != s2[i]:
            print(f"Change at index {i}: '{s1[i]}' -> '{s2[i]}'")