a=(10,20,30,40,50,60,70,80,90,100)
b=(1,2,3,4,5,6,7,8,9,10)
result=a+b
print(result)  # This will print the concatenated tuple
# Repetition operator
b=(1,2,3,4,5,6,7,8,9,10)
result=b*3
print(result)  # This will print the tuple repeated 3 times
# Note: Tuples are immutable, so you cannot change their elements after creation.
# However, you can create a new tuple by concatenating or repeating existing tuples.
# Example of tuple unpacking
n1, n2, n3, n4, n5, n6, n7, n8, n9, n10 = result
print(n1, n2, n3, n4, n5, n6, n7, n8, n9, n10)  # This will print the values of the tuple elements
# Tuple unpacking
print(n1, type(n1))  # This will print the value and type of n1
print(n2, type(n2))  # This will print the value and type of n2
# Note: The tuple unpacking above assumes that the tuple has exactly 10 elements.
# If the tuple has a different number of elements, you will need to adjust the unpacking accordingly.
# Example of tuple unpacking with fewer elements
# If you have a tuple with fewer elements, you can unpack it like this:
