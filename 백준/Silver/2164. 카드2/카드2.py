import sys
from collections import deque
input = sys.stdin.readline

N = int(input())
queue = deque(range(0, N+1, 2))
queue.popleft()

if N == 1:
    print(1)

elif N == 2:
    print(2)
    
elif N % 2 == 1:
    while len(queue) > 1:
        queue.append(queue.popleft())
        queue.popleft()
    print(queue[0])

else:
    while len(queue) > 1:
        queue.popleft()
        queue.append(queue.popleft())
    print(queue[0])