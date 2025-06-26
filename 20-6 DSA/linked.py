class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

first = Node(10)
second = Node(20)
third = Node(30)
forth = Node(50)
fifth = Node(60)

head = first
head.next = second
second.next = third
third.next = forth
forth.next = fifth

current = head
while current:
    print(current.data, end="->")
    current = current.next
print("None")

#write a python program to create a linked list of size n take the value of n asa input from the user
n = int(input("Enter the size of the linked list: "))
head = None
tail = None
for i in range(n):
    data = int(input("Enter the value for node {}: ".format(i + 1)))
    new_node = Node(data)
    if head is None:
        head = new_node
        tail = new_node
    else:
        tail.next = new_node
        tail = new_node

current = head
while current:
    print(current.data, end="->")
    current = current.next
print("None")
