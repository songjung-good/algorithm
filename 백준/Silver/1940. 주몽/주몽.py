import sys
from collections import deque
input = sys.stdin.readline

N = int(input())
M = int(input())
N_q = deque(list(map(int,input().split())))
check = {}
ans = 0

for n in range(N):
    now = N_q[0]
    num = M - now
    if now in check:
        ans += 1
        del check[now]
    else:
        check[num] = True
    N_q.rotate()
print(ans)
