def is_balanced(expression):
    stack = []
    pairs = {')': '(', '}': '{', ']': '['}
    for char in expression:
        if char in '([{':
            stack.append(char)
        elif char in ')]}':
            if not stack or stack[-1] != pairs[char]:
                return False
            stack.pop()
    return not stack

# Example usage
expr = input("Enter an expression: ")
if is_balanced(expr):
    print("Balanced")
else:
    print("Not Balanced")