my_set = {10, 20, 30, 40, 50, 60}
print(type(my_set))
my_set.add(90)
print(my_set)
print(sorted(my_set))
#update
set_2={60,50,66,55}
my_set.update(set_2)
print(sorted(my_set))
#remove
my_set.remove(90)##my_set.discard(90)
print(my_set)
#remove multiple elements
#for item in [90, 10, 20]:
#   my_set.discard(item)  # or use my_set.remove(item) if you want an error when not found
#print(my_set)
