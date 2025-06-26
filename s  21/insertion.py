# Insertion in a linked list using a temp variable

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insert(self, data):
        temp = Node(data)
        temp.next = self.head
        self.head = temp

    def display(self):
        current = self.head
        while current:
            print(current.data, end="->")
            current = current.next
        print("None")

# Example usage
ll = LinkedList()
ll.insert("Apple")
ll.insert("Banana")
ll.insert("Cherry")
ll.display()  # Output: Cherry->Banana->Apple