# Get word from user
word = input("Enter a word: ")

# Count letters
letter_count = len(word)

# Print word that many times
for i in range(letter_count):
    print(word)

# Get word from user
word = input("Enter a word: ")

# Get dimensions
rows = len(word)
cols = len(word)





# Print rectangle with word only on outer layer
for i in range(rows):
    for j in range(cols):
        # Check if position is on the border (outer layer)
        if i == 0 or i == rows-1 or j == 0 or j == cols-1:
            print(word[j % len(word)], end="")
        else:
            print(" ", end="")
    print()  # New line after each row
# Get word from user
word = input("Enter a word: ")

# Get number of letters
n = len(word)





# Print pattern using the input word
for i in range(n):
    print(word * (i + 1))


# Get word from user
word = input("Enter a word: ")

# Get number of letters
n = len(word)






# Print + shape using the input word
for i in range(n):
    for j in range(n):
        # Print word if it's the middle row or middle column
        if i == n//2 or j == n//2:
            print(word[j % len(word)], end="")
        else:
            print(" ", end="")
    print()  # New line after each row


    



    # Get word from user
word = input("Enter a word: ")

# Get number of letters
n = len(word)

# Print squares of numbers in right angle triangle
num = 1
for i in range(1, n + 1):
    for j in range(i):
        print(num * num, end=" ")
        num += 1
    print()  # New line after each row




# Get word from user
word = input("Enter a word: ")

# Get number of letters
n = len(word)

# Print diamond pattern using the input word
# Upper half (including middle)
for i in range(n):
    # Print leading spaces
    print(" " * (n - i - 1), end="")
    
    # Print word letters
    for j in range(i + 1):
        print(word[j % len(word)] + " ", end="")
    
    print()  # New line

# Lower half
for i in range(n - 2, -1, -1):
    # Print leading spaces
    print(" " * (n - i - 1), end="")
    
    # Print word letters
    for j in range(i + 1):
        print(word[j % len(word)] + " ", end="")
    
    print()  # New line