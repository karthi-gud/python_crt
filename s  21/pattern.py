n=int(input("Enter the number of rows: "))
for i in range(1,n+1):
    for j in range(1,n+1):
        print(j,end="")
    print()
# Output:
# 1234  
n=int(input("Enter the number of rows: "))
for i in range(1,n+1):
    for j in range(1,i+1):
        print(j,end="")
    print()
# Output:
# 1
# 12
# 123
n=int(input("Enter the number of rows: "))
for i in range(1,n+1):
    for j in range(1,n+1):
        print("*",end="")
    print()
# Output:
# ****
#to print right angle triangle
n=int(input("Enter the number of rows: "))
for i in range(1,n+1):
    for j in range(1,i+1):
        print("*",end="")
    print()
