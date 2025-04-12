import sys
input = sys.stdin.readline

N = int(input())
M = int(input())
CITY = [[float('inf')] * (N) for _ in range(N)]

# 정점을 0으로
for n in range(N):
    CITY[n][n] = 0
# 각 노드의 비용
for m in range(M):
    a, b, c = map(int, input().split())
    if CITY[a-1][b-1] != float('inf'):
        if CITY[a-1][b-1] > c:
            CITY[a-1][b-1] = c
        else:
            pass
    else:
        CITY[a-1][b-1] = c
# 플로이드-워셜
for k in range(N):
    for i in range(N):
        for j in range(N):
            if CITY[i][j] > CITY[i][k] + CITY[k][j]:
                CITY[i][j] = CITY[i][k] + CITY[k][j]
# 건널 수 없는 곳 확인
for i in range(N):
    for j in range(N):
        if CITY[i][j] == float('inf'):
            CITY[i][j] = 0

for n in range(N):
    print(*CITY[n])
