#write a pyhon program to read the string a s in put from the user
#1 reverse the string 
#2 conver the string into lower case 
#3 conver the string into upper case
#4 conver the characters of the string to lower case if it is in upper case if it is in upper cover to lowerr case
#5 check the string is starting with letter A 
#6 print the count of the character a from the given string and replace all "p" to letter "j"
s = input("Enter a string: ")
print(f"Reversed: {s[::-1]}")
print(f"Lowercase: {s.lower()}")
print(f"Uppercase: {s.upper()}")
print(f"Swapped case: {s.swapcase()}")
print(f"Starts with 'A': {s.lower().startswith('a')}")
print(f"Count of 'a': {s.lower().count('a')}")
print(f"Replace 'p' with 'j': {s.replace('p', 'j').replace('P', 'j')}")


print(s[::-1])
print(s.lower())
print(s.upper())
print(s.swapcase())
print(s.startswith('P'))
print(s.count('p'))
print(s.lower().replace('p', 'j'))
