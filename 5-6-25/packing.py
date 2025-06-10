#write a python program take a list of toys names (some repeated)     remove duplicates    sort and display the final toy list to pack
toys = input("Enter a list of toy names separated by commas: ")
toys_list = [toy.strip() for toy in toys.split(',')]
toys_list = list(set(toys_list))  # Remove duplicates
toys_list.sort()  # Sort the list
print("Final toy list to pack:")
for toy in toys_list:
    print(toy)  # Display the sorted list of unique toy names
# Example input: "teddy bear, doll, car, teddy bear, ball, doll"

