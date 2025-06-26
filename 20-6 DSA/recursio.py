#a recursion a function call by itself
def add(*arg):
    sum=0
    for i in arg:
        sum+=i
    return sum  
# Example usage
result = add(1, 2, 3, 4, 5)
print("Sum of numbers:", result)
# recursion syntax in python
def function_name(parameters):
    # Base case
    if condition:
        return value
    else:
        # Recursive case
        return function_name(modified_parameters)   
# Example of a recursive function to calculate factorial
def factorial(n):
    # Base case
    if n == 0 or n == 1:
        return 1
    else:
        # Recursive case
        return n * factorial(n - 1) 
# Example usage
result = factorial(5)
print("Factorial of 5:", result)
# Example of a recursive function to calculate Fibonacci sequence
def fibonacci(n):
    # Base case
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        # Recursive case
        return fibonacci(n - 1) + fibonacci(n - 2)
# Example usage
result = fibonacci(6)
print("Fibonacci of 6:", result)
