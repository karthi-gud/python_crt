dict={101:'python',102:'java',103:'SQL',104:'loly'}
fees={'rahul':200,'raj':201,'karri':202}
print(dict)
print(type(dict))
print(dict[101])  # Use square brackets, not curly braces
#while eriting keeys we dont follow the rules
#1 key should be unique
#2 if we written same key ,the old key will be written
#3 key should be  immutable type ex integer, string or tuple we cannot use list or dictionary keys
print(dict[102])
print(dict[104])
print(fees['raj'])
print(fees['rahul'])
print(dict[102],fees['rahul'])
