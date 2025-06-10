#write a python program to creat a tuple of programing languages being length as 15 and fiind the maximum element and the minumum element in the tupleand print the sorted tuple and print the reversed tuple
Tuple=('Python', 'Java', 'C++', 'JavaScript', 'Ruby', 'Swift', 'Go', 'Kotlin', 'PHP', 'Perl', 'Rust', 'Scala', 'Dart', 'TypeScript', 'Lua')
print("the og ",Tuple)
print("maximum in the tuple",max(Tuple))
print("minimum in the tuple",min(Tuple))
print("sorted tuple",sorted(Tuple))
print("reversed tuple",Tuple[::-1])
print("reversed tuple using reversed function:", tuple(reversed(Tuple)))
#using of splicing reversed tuple
print("reversed tuple using slicing:", Tuple[::-1])  # This will print the reversed tuple using slicing
#writ a pyhthon program to creater a tuple of names and print he original tuple and print the names which has a length of 5
names_tuple = ('Alice', 'Bob', 'Charlie', 'David', 'Eve', 'Frank', 'Grace', 'Hannah', 'Isaac', 'Jack')
print("Original names tuple:", names_tuple)
print("Names with length of 5:")
for name in names_tuple:
    if len(name) == 5:
        print(name)  # This will print the names with a length of 5
# Write a Python program to create a tuple of numbers and print the original tuple,
# print the numbers that are even, and print the numbers that are odd

