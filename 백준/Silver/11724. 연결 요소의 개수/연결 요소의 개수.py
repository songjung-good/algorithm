import sys
from collections import deque
input = sys.stdin.readline

def bfs(num):
    Q = deque(graph[num])
    while Q:
        now = Q.popleft()
        visited[now] = True
        for i in graph[now]:
            if i in Q or visited[i]:
                pass
            else:
                Q.append(i)

# N은 정점의 수, M은 간선의 수
N, M = map(int,input().split())
graph=[[] for _ in range(N+1)]

visited = [False] * (N+1)
for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

ans = 0
for n in range(1, N+1):
    if visited[n]:
        pass
    else:
        visited[n] = True
        bfs(n)
        ans += 1

print(ans)