from collections import deque

queue = deque()
queue.append('A')
queue.append('B')
queue.append('C')
print("Queue after enqueuing:", queue)

first = queue.popleft()
print("Dequeued Element:", first)
print("Queue after dequeuing:", queue)

if not queue:
    print("Queue is empty")
else:
    print("Queue is not Empty")

if queue:  # Check if queue is not empty before accessing front element
    print("Front Element:", queue[0])
else:
    print("No front element, queue is empty")