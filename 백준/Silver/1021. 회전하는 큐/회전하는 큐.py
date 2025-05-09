import sys
from collections import deque
input = sys.stdin.readline

N, M = map(int, input().split())
N_q = deque([i for i in range(1,N+1)])
M_lst = list(map(int, input().split()))

ans = 0
while M_lst:
    cnt = 0
    now = M_lst.pop(0)
    for _ in range(N):
        if N_q[0] == now:
            ans += min(cnt, N-cnt)
            N_q.popleft()
            N -= 1
            break
        else:
            cnt += 1
            N_q.rotate()

print(ans)