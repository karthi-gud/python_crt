#write a python program to read the list of character as input from the user convert a word and print the data type mus be in string
size=int(input("enter the input value :"))
char_list=[]
for i in range(size):
    ch=input("enter the characters :")
    char_list.append(ch)
print(char_list)
str="".join(char_list) 
print(str)   
    
