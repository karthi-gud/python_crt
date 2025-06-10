color=['white','black','red','green','blue','yellow','purple','cyan','orange']
print(color)
del color[2]
print(color)
del color[3:5]
print(color)

###built in list functions in python 
#len()
#max()
#min()
#sum()
#sorted()
#list()
#any()
#all()
#write a python program to read the size of list as input from the user and take the list elements
#  also input from the user and find the length of the list or the maximum number present in the list 
# and minum element ,the summation elements of the list print the sorted list in asending order
size = int(input("Enter the size of the list: "))
num = []
for i in range(size):
    temp = int(input(f"Enter element at{i} index:"))
    num.append(temp)
    print(f"given list :{num}")
    print(f"maximum element :", max(num))
    print(f"minimum element :", min(num))
    print(f"length of the list :", len(num))
    print(f"sum of the elements :", sum(num))
    print(f"sorted list :", sorted(num))
    print(f"list in ascending order :", list(num))