def summ(a,b):
    res = b
    if a!=0:
        res = res + a
        return summ(a-1,res)
    else:
        return res
print(summ(3,0))

def add_list(n, sum):
    if n == 0:
        return sum
    return add_list(n - 1, sum + n)

print(add_list(5, 0))

# write a py program to sum of elements of list using recursion
def add_list(lst, sum):
    if lst:
        sum = sum + lst[0]
        return add_list(lst[1:], sum)
    return sum

print(add_list([1, 2, 3, 4, 5], 0))
