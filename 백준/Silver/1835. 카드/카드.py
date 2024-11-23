from collections import deque

N = int(input())
result = deque()

for n in range(N, 0, -1):
    result.appendleft(n)
    for _ in range(n):
        result.rotate(1)

print(*result)