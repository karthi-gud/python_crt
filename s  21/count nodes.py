def count_nodes(self):
    count = 0
    current = self.head
    while current:
        count += 1
        current = current.next
    return count
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

    def count_nodes(self):
        count = 0
        current = self.head
        while current:
            count += 1
            current = current.next
        return count
# Example usage
ll = LinkedList()
ll.append(1)
ll.append(2)
ll.append(3)
print("Number of nodes:", ll.count_nodes())