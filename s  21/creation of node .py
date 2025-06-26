#creation of nodes
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

node = Node(10)
print(node.data)  # Output: 10
node1 = Node(20)
print(node1.data)  # Output: 20
node2 = Node(30)
print(node2.data)  # Output: 30

# Linking nodes
node.next = node1
node1.next = node2

# Traversing and printing the linked list
current = node
while current:
    print(current.data, end="->")
    current = current.next
print("None")