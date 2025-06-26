from collections import deque

stack = deque()
stack.append('A')
stack.append('B')
stack.append('C')
print("Stack after pushing:", stack)

top = stack.pop()
print("Popped Element:", top)
print("Stack after popping:", stack)

if not stack:
    print("Stack is empty")
else:
    print("Stack is not Empty")

if stack:  # Check if stack is not empty before accessing top element
    print("Top Element:", stack[-1])
else:
    print("No top element, stack is empty")

