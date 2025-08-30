import sys
input = sys.stdin.readline

# N은 정점의 수, M은 간선의 수
N, M = map(int,input().split())
graph = [[] for _ in range(N+1)]
visited = [False] * (N+1)
for i in range(M):
    a, b = map(int, input().split())
    graph[b].append(a)

ans = 0
goal = int(input())
cnt = 1
now = 0
work = [goal]
while cnt > now:
    num = work[now]
    if visited[num]:
        pass
    else:
        visited[num] = True
        ans += 1
        for g in graph[num]:
            if visited[g]:
                pass
            else:
                work.append(g)
                cnt += 1
    now += 1

print(ans-1)
