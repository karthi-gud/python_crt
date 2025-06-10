#writea python program to read a string as a input from the user and replace all vowels with zeros

s = input("Enter a string: ")
for vowel in "aeiouAEIOU":
    s = s.replace(vowel, '0')
print(s)

s = input("Enter a string: ")
result = s.replace('a', '0').replace('e', '0').replace('i', '0').replace('o', '0').replace('u', '0').replace('A', '0').replace('E', '0').replace('I', '0').replace('O', '0').replace('U', '0')
print(f"String with vowels replaced: {result}")





#write the python program to read password as input from the user and check wether it is a valid password or invalid password 