import sys
from collections import deque
input = sys.stdin.readline

def BFS(start):
    q = deque([start])
    visited = [-1] * N
    visited[start] = 0

    while q:
        now = q.popleft()
        for next in GRAPH[now]:
            if visited[next] == -1:
                visited[next] = visited[now] + 1
                q.append(next)

    return sum(visited)

N, M = map(int,input().split())
GRAPH = [[] for _ in range(N)]

for _ in range(M):
    n, m = map(int, input().split())
    GRAPH[n-1].append(m-1)
    GRAPH[m-1].append(n-1)

min_gap = 1e9
ans = 0
for n in range(N):
    cnt = BFS(n)
    if min_gap > cnt:
        min_gap = cnt
        ans = n+1

print(ans)