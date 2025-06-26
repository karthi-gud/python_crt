from collections import deque

queue = deque()

def add_customer(name):
    queue.append(name)
    print(f"Customer '{name}' added to the queue.")

def serve_customer():
    if queue:
        served = queue.popleft()
        print(f"Customer '{served}' has been served and removed from the queue.")
    else:
        print("No customers to serve.")

def display_queue():
    if queue:
        print("Customers in queue:", list(queue))
    else:
        print("No customers in the queue.")

# Example usage
add_customer("Alice")
add_customer("Bob")
add_customer("Charlie")
display_queue()
serve_customer()
display_queue()
serve_customer