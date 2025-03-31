import sys
import heapq
input = sys.stdin.readline

def dijkstra(S, E, graph, D):
    D[S] = 0
    heap = [(0, S)] # (거리, 정점)

    while heap:
        dist, now = heapq.heappop(heap)

        if D[now] < dist:
            continue

        for next, cost in graph[now]:
            new_dist = dist + cost
            if new_dist < D[next]:
                D[next] = new_dist
                heapq.heappush(heap, (new_dist, next))

# 정점 수 N, 간선 수 M
N = int(input())
M = int(input())
graph = [[] for _ in range(N+1)]
D = [float('inf')] * (N+1)

for _ in range(M):
    u, v, w = map(int, input().split())
    graph[u].append((v,w))

S, E = map(int,input().split())

dijkstra(S, E, graph, D)

print(D[E])
