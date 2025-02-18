# 코드를 작성해주세요
from collections import deque

N, K = map(int, input().split())
Q = deque(n for n in range(1, N+1))
ans = []
while Q:
    Q.rotate(-(K-1))
    ans.append(Q.popleft())

print('<', end='')
print(*ans, sep=', ', end='>')