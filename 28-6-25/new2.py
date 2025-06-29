a=10
b=5
try: 
    d=a/b
    print(d)
    print('Inside try')
except ZeroDivisionError:
    print("Division by Zero Not Allowed")
else:
    print("Inside Else")
print("Rest of the Code")