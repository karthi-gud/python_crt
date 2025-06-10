#write a python program to remove the duplicate values form the list
list=[1,20,20,32,33,45,45,56,67,67,78,89,89]
print(list)
new_list = []
for i in list:
    if i not in new_list:
        new_list.append(i)
print(new_list)  # [1, 20, 32, 33, 45, 56, 67, 78, 89]


##unique_list = []
#for item in list:
 #   if item not in unique_list:
 #       unique_list.append(item)
#print("List after removing duplicates:", unique_list)  # [1, 20, 32, 33, 45, 56, 67, 78, 89]
#writea python program to input from user print a new list of numbers which are multiples of 5 

