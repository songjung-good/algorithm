N = int(input())
graph = [[] for _ in range(N+1)]

for i in range(1, N):
    m = int(input())
    graph[i] = list(map(int, input().split()))

visited = [0] * (N + 1)
stack = [0] * (N + 1)

def dfs(node):
    if stack[node]:
        return True
    if visited[node]:
        return False

    visited[node] = 1
    stack[node] = 1

    for neighbor in graph[node]:
        if dfs(neighbor):
            return True

    stack[node] = 0
    return False

if dfs(1):
    print("CYCLE")
else:
    print("NO CYCLE")
