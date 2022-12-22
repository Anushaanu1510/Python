from collections import deque
queue= deque(['Eric','John','Michel'])
print(queue)
queue.append('Terry')
queue.append('Graham')
print(queue)

queue.pop()
print(queue)

queue.popleft()
print(queue)