#writea python program to read a string as a input from the user and replace all vowels with zeros

s = input("Enter a string: ")
for vowel in "aeiouAEIOU":
    s = s.replace(vowel, '0')
print(s)

s = input("Enter a string: ")
result = s.replace('a', '0').replace('e', '0').replace('i', '0').replace('o', '0').replace('u', '0').replace('A', '0').replace('E', '0').replace('I', '0').replace('O', '0').replace('U', '0')
print(f"String with vowels replaced: {result}")





#write the python program to read password as input from the user and check wether it is a valid password or invalid password 
#write apython prohram to note name email contact number 10 digit mail should have valid strucure name @org.com and password should have atleat 3 upper case
#3lowercdscae alphabets 3 special characters and one numbwer password should not be less than 10
#write a pythomn progrma to read A astring as input from the user and split the string into three equal halfs using slicing 