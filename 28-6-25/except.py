'''
try:
    code which gives exception
except ExceptionClassName:
    block of code which will be executed instead of error
'''

Num=100
print("Program Execution Begins")
print(Num)
try:
    print(Num/0)
except ZeroDivisionError:
    print("Dividing with zero gives an Infinite Value")
print("Program Execution Ends")




















