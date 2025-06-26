# write a py program to print square numbers from 1 to n using recursion
n = int(input("Enter the number: "))

def squa(a):
    if a > 0:
        squa(a - 1)
        print(f"Square of {a} is {a * a}")

squa(n)
#write a py program to print reverse square numbers from n to 1 using recursion
def reverse_squa(a):
    if a != 0:
        print(f"Square of {a} is {a*a}")
        return reverse_squa(a-1)
    else:
        return
n = int(input("Enter the number: "))
reverse_squa(n)

#write a py program to print prime numbers from 1 to n using recursion