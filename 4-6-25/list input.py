#write a python program to read the list elements as input from the user & display the list elements using for loop
size=int(input("Enter the size of the list: "))
num_list = []
for i in range(size):
    num = input() 
    num_list.append(num)
print("The list elements are:")
print(num_list) 
