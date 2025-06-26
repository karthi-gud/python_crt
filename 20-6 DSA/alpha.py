#write a python program to print alphabets from a to z using recursion
def print_alphabets(current='a'):
    if current > 'z':
        return
    print(current)
    print_alphabets(chr(ord(current) + 1))
n = int(input("Enter the value of n: "))
print_alphabets()


def alpha(ch):
    if ch>=ord('A') and ch<=ord('Z'):
        print(chr(ch))
        return alpha(ch+1)
ch=65
alpha(ch)
print("--------------------")
def alpha_lower(ch):
    if ch >= ord('A') and ch <= ord('Z'):
        print(chr(ch))
        return alpha_lower(ch + 1)
ch = 97
alpha_lower(ch)
