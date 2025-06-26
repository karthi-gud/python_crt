from collections import deque

class Queue:
    def __init__(self):
        self.items = deque()
    
    def enqueue(self, item):
        """Add an item to the rear of the queue"""
        self.items.append(item)
        print(f"Enqueued: {item}")
    
    def dequeue(self):
        """Remove and return the front item from the queue"""
        if len(self.items) == 0:
            print("Queue is empty!")
            return None
        item = self.items.popleft()
        print(f"Dequeued: {item}")
        return item
    
    def peek_front(self):
        """Return the front item without removing it"""
        if len(self.items) == 0:
            print("Queue is empty!")
            return None
        return self.items[0]
    
    def peek_rear(self):
        """Return the rear item without removing it"""
        if len(self.items) == 0:
            print("Queue is empty!")
            return None
        return self.items[-1]
    
    def display(self):
        """Display queue contents (helper function)"""
        print(f"Queue: {list(self.items)}")

# Example usage
q = Queue()

print("=== Queue Operations ===")

# Enqueue operations
q.enqueue(10)
q.enqueue(20)
q.enqueue(30)
q.display()

# Peek operations
print(f"Peek front: {q.peek_front()}")
print(f"Peek rear: {q.peek_rear()}")

# Dequeue operation
q.dequeue()
q.display()

print(f"Peek front: {q.peek_front()}")
print(f"Peek rear: {q.peek_rear()}")

# Dequeue all
q.dequeue()
q.dequeue()

# Try operations on empty queue
q.peek_front()
q.peek_rear()
q.dequeue()