#write a  py program to print natural numbers from 1 to n using recursion where n is input
# Write a Python program to print natural numbers from 1 to n using recursion where n is input
def print_natural_numbers(n, current=1):
    if current > n:
        return
    print(current)
    print_natural_numbers(n, current + 1)

n = int(input("Enter the value of n: "))
print_natural_numbers(n)

#from reverse

n=int(input("Enter the value of n: "))
i=0
def natural(n,i):
    i=i+1
    if n==0:
        return
    natural(n-1,i)
    print(i)
natural(n,i)

