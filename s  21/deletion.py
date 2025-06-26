#deletion first node
def delete_first_node(self):
    if self.head is None:
        return  # List is empty, nothing to delete
    self.head = self.head.next  # Move head to the next node
# Example usage
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        last = self.head
        while last.next:
            last = last.next
        last.next = new_node

    def delete_first_node(self):
        if self.head is None:
            return  # List is empty, nothing to delete
        self.head = self.head.next  # Move head to the next node

    def display(self):
        current = self.head
        while current:
            print(current.data, end="->")
            current = current.next
        print("None")   
# Example usage
ll = LinkedList()
ll.append("Apple")
ll.append("Banana")
ll.append("Cherry")
print("Before deletion:")
ll.display()
ll.delete_first_node()
print("After deletion:")
ll.display()
# Output: