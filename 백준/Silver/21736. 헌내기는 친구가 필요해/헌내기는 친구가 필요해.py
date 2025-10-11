import sys
from collections import deque
input = sys.stdin.readline

N, M = map(int, input().split())
camp= [input().rstrip() for _ in range(N)]

for n in range(N):
    for m in range(M):
        if camp[n][m] == 'I':
            start = (n, m)
            break

Q = deque([start])
V = [[False] * M for _ in range(N)]
D = [0, 0, 1, -1]

ans = 0
while Q:
    x, y = Q.popleft()
    V[x][y] = True
    if camp[x][y] == 'P':
        ans += 1
    for d in range(4):
        dx, dy = D[d] + x, D[3-d] + y
        if 0 <= dx < N and 0 <= dy < M and V[dx][dy] == False:
            if camp[dx][dy] != 'X':
                Q.append((dx,dy))
            V[dx][dy] = True

if ans:
    print(ans)
else:
    print('TT')