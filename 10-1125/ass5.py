#writea  python program to read a string as input from the user and print number of 
#1 print number of upper case lettters
#2 print count of lower case numbers 
#3 print the sount of numeric valueues
#4 print he count of special characters
str=input("enter the string :")
uppercase_alpha=0
lowercase_alpha=0
numeric_values=0
special_character=0
for i in str:
    if i.isupper():
        uppercase_alpha+=1
    elif i.islower():
        lowercase_alpha+=1
    elif i.isdigit():
        numeric_values+=1
    else: 
        special_character+=1
print(uppercase_alpha)
print(lowercase_alpha)
print(numeric_values)
print(special_character)
