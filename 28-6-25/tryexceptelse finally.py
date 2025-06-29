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
finally:
    print("inside finally")
print('rest of the code')
