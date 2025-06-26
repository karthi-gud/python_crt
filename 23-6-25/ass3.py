# writ a python program to take the length q as input from the user and add the elements by using enquee method and print the elements present in the quee and remove elements one by one from the quee and check wtherr the quee is empty or not and print the front peek and and rear peek
from collections import deque

queue = deque()
q = int(input("Enter the length of the queue: "))

# Enqueue elements
for i in range(q):
    elem = input(f"Enter element {i+1}: ")
    queue.append(elem)

print("Elements present in the queue:", list(queue))

# Remove elements one by one
while queue:
    print(f"Dequeued element: {queue.popleft()}")
    print("Current queue:", list(queue))
    if queue:
        print("Front peek:", queue[0])
        print("Rear peek:", queue[-1])
    else:
        print("Queue is now empty.")

if not queue:
    print("Queue is empty.")
else:
    print("Queue is not empty.")