'''
    V개 노드
    E개의 간선
    출발 S 도착 G

    1. graph에서 출발지점 찾는다.

'''
'''
#1
T = int(input())
for tc in range(1, T+1):
    V, E = map(int, input().split())    #V는 노드 수, E는 간선 수
    node = [''] * V      #노드 생성
    graph = [list(map(int, input().split())) for i in range(E)]     #그래프 경로
    S, G = map(int, input().split())    #S는 출발노드, G는 도착노드

    for i in range(E):
        node[graph[i][0]] += str(graph[i][1])

    graph[S]

    ans = 0
    print(graph)
    print(f'#{tc} {node}')

'''


def dfs(v, visited, graph, end):
    if v == end:  # 도착 정점에 도달한 경우
        return True

    visited[v] = True  # 현재 정점을 방문 처리

    for neighbor in graph[v]:
        if not visited[neighbor]:
            if dfs(neighbor, visited, graph, end):
                return True

    return False


T = int(input())

for tc in range(1, T + 1):
    V, E = map(int, input().split()) #V는 노드 수, E는 간선 수
    graph = [[] for _ in range(V + 1)]  # 각 정점의 이웃들을 저장하는 리스트
    visited = [False] * (V + 1)  # 정점 방문 여부를 나타내는 리스트

    for _ in range(E):
        v1, v2 = map(int, input().split())
        graph[v1].append(v2)  # 방향 그래프이므로 v1에서 v2로 가는 간선 추가

    start, end = map(int, input().split())  # 시작 정점과 도착 정점

    if dfs(start, visited, graph, end):
        result = 1
    else:
        result = 0

    print(f'#{tc} {result}')
