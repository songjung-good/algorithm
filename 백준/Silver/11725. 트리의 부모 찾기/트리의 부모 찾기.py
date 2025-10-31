from collections import deque

N = int(input())
graph = [[] for _ in range(N+1)]
for _ in range(N-1):
    n, m = map(int, input().split())
    graph[n].append(m)
    graph[m].append(n)

lst = [0] * (N+1)

q = deque([1])
while q:
    now = q.popleft()
    for i in graph[now]:
        if lst[i] == 0:
            lst[i] = now
            q.append(i)

for i in lst[2:]:
    print(i)