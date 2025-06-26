'''class Stack:
    def __init__(self):
        self.Stack = []

    def push(self, data):
        self.Stack.append(data)

    def size(self):
        return len(self.Stack)

# Example usage
stack = Stack()
stack.push(10)
stack.push(20)
stack.push(30)
print("Size of the stack:", stack.size())'''


class Stack:
    def __init__(self):
        self.Stack = []

    def push(self, data):
        self.Stack.append(data)
        print(f"{data} pushed to stack")

    def pop(self):
        if self.isempty():
            print("Stack is empty")
        else:
            removed = self.Stack.pop()
            print(f"{removed} popped from stack")

    def isempty(self):
        return len(self.Stack) == 0

    def peek(self):
        if self.isempty():
            print("Stack is empty")
        else:
            print(f"Top element is {self.Stack[-1]}")

    def size(self):
        return len(self.Stack)

    def display(self):
        print("Stack elements (top to bottom):")
        for item in reversed(self.Stack):
            print(item)

# Example usage
stack = Stack()
stack.push(10)
stack.push(20)
stack.push(30)
stack.display()
stack.peek()
print("Size of the stack:", stack.size())
stack.pop()
stack.display()
print("Size of the stack:", stack.size())