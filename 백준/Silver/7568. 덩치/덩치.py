import sys
from collections import deque
input = sys.stdin.readline

N = int(input())
lst = []
ans = [1] * N
for _ in range(N):
    x, y = map(int, input().split())
    lst.append((x,y))

for i in range(N):
    x1, y1 = lst[i]
    for j in range(N):
        if i == j:
            pass
        else:
            x2, y2= lst[j]
            if x1 < x2 and y1 < y2:
                ans[i] += 1

print(*ans)