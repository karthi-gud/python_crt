n = int(input("Enter the number of rows: "))

# 1. Left-aligned, right angle at bottom-left
for i in range(1, n + 1):
    for j in range(1, n + 1):
        if j <= i:
            print("*", end="")
        else:
            print(" ", end="")
    print()
# Output:
# *
# **
# ***
# ****

print()  # Separator

# 2. Right-aligned, right angle at bottom-right
for i in range(1, n + 1):
    for j in range(1, n + 1):
        if j <= n - i:
            print(" ", end="")
        else:
            print("*", end="")
    print()
# Output:
#    *
#   **
#  ***
# ****

print()  # Separator

# 3. Left-aligned, right angle at top-left (mirror of 1)
for i in range(1, n + 1):
    for j in range(1, n + 1):
        if j <= n - i + 1:
            print("*", end="")
        else:
            print(" ", end="")
    print()
# Output:
# ****
# ***
# **
# *

print()  # Separator

# 4. Right-aligned, right angle at top-right (mirror of 2)
for i in range(1, n + 1):
    for j in range(1, n + 1):
        if j < i:
            print(" ", end="")
        else:
            print("*", end="")
    print()
# Output:
# ****
#  ***
#   **
#    *

n = int(input("Enter the number of rows: "))

# Equilateral triangle
for i in range(1, n + 1):
    # Print spaces
    for j in range(n - i):
        print(" ", end="")
    # Print stars
    for k in range(2 * i - 1):
        print("*", end="")
    print()
# Output for n=4:
#    *
#   ***
#  *****
# *********
