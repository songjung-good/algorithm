from collections import deque
import sys
input = sys.stdin.readline

N, M, R = map(int, input().split())
GRAPH = [[] for _ in range(N+1)]
for _ in range(M):
    x, y = map(int, input().split())
    GRAPH[x].append(y)
    GRAPH[y].append(x)

node = [-1] * (N+1)
node[R] = 0
V = [False] * (N+1)
V[R] = True

Q = deque([(R,0)])
while Q:
    now, c = Q.popleft()
    for q in GRAPH[now]:
        if not V[q]:
            node[q] = c+1
            V[q] = True
            Q.append((q, c+1))

for i in range(1, N+1):
    print(node[i])