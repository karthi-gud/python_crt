dict1 = {101:'python', 102:'java', 103:'SQL', 104:'loly'}
dict2 = dict1.copy()

print("Original:", dict1)
print("Copy:", dict2)

# Modifying the copy doesn't affect the original
dict2[105] = 'C++'
print("After modifying copy:")
print("Original:", dict1)
print("Copy:", dict2)

dict1 = {101:'python', 102:'java'}
dict2 = dict1.copy()

dict2[103] = 'SQL'  # Add to copy
dict2[101] = 'C++'  # Modify existing in copy

print("Original:", dict1)
print("Copy:", dict2)