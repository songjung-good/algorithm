from collections import deque

C = int(input())
N = int(input())

def dfs(v):
    visited[v] = True
    for g in graph[v]:
        if not visited[g]:
            dfs(g)

def bfs(v):
    Q = deque([v])
    visited[v] = True
    while Q:
        now = Q.popleft()
        for g in graph[now]:
            if not visited[g]:
                visited[g] = True
                Q.append(g)


graph = [[] for _ in range(C+1)]
for _ in range(N):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

visited = [False] * (C+1)

bfs(1)

print(sum(visited) - 1)