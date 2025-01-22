import sys
from collections import deque
input = sys.stdin.readline

N = int(input())
lst = deque([])
for _ in range(N):
    lst.appendleft(int(input()))

cnt = 0
past = float("inf")
for _ in range(N):
    now = lst.popleft()
    if now >= past:
        gap = now - past + 1
        cnt += gap
        now -= gap
    past = now

print(cnt)