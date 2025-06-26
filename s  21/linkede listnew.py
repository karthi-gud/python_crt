class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def Addnode(self, data):
        N_node = Node(data)
        N_node.next = self.head
        self.head = N_node

    def Display(self):
        current = self.head
        while current:
            print(current.data, end="->")
            current = current.next
        print("None")

# Example usage:
Ll = LinkedList()
Ll.Addnode("Apple")
Ll.Addnode("Banana")
Ll.Addnode("Cherry")
Ll.Display()