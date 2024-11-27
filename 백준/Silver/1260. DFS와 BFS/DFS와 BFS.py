def DFS(g, v, node, result):
    v.add(node)
    result.append(node)

    for n in sorted(g[node]):
        if n not in v:
            DFS(g, v, n, result)

    return result

def BFS(g, v):
    visited = set()
    queue = deque([v])
    result = []
    visited.add(v)

    while queue:
        node = queue.popleft()
        result.append(node)
        for n in sorted(g[node]):
            if n not in visited:
                visited.add(n)
                queue.append(n)

    return result

from collections import defaultdict, deque
N, M, V = map(int, input().split())
GRAPH = defaultdict(list)

for _ in range(M):
    u, v = map(int, input().split())
    GRAPH[u].append(v)
    GRAPH[v].append(u)

ans1 = DFS(GRAPH, set(), V, [])
ans2 = BFS(GRAPH, V)
print(*ans1)
print(*ans2)