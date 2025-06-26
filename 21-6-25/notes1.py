class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insert_fruit(self, data):
        new = Node(data)
        new.next = self.head
        self.head = new

    def show(self):
        temp = self.head
        while temp:
            print(temp.data, end="->")
            temp = temp.next
        print("None")

# Example usage:
ll = LinkedList()
ll.insert_fruit("Apple")
ll.insert_fruit("Banana")
ll.insert_fruit("Cherry")
ll.show()