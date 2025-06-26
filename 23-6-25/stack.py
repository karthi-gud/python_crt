class Stack:
    def __init__(self):  # Fixed constructor name
        self.Stack = []

    def push(self, data):
        self.Stack.append(data)
        print(f"{data} element is appended")

    def isempty(self):
        return len(self.Stack) == 0

    def pop(self):
        if self.isempty():
            print("Stack is empty")
        else:
            removed = self.Stack.pop()
            print(f"{removed} element is removed")

    def peak(self):
        if self.isempty():
            print("Stack is empty")
        else:
            print(f"The peak element is: {self.Stack[-1]}")

    def Display(self):
        for i in self.Stack:
            print(i)

            '''###    def Display(self):
        for i in reversed(self.Stack):
            print(i)'''

# Using the stack
stack = Stack()
stack.push(100)
stack.push(105)
stack.push(150)
stack.push(78)
stack.peak()
stack.Display()