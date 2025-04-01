import sys
input = sys.stdin.readline

N, M = map(int, input().split())
MAP = [list(map(int, input().split())) for _ in range(N)]
SUM_MAP = [[0]*(N+1) for _ in range(N+1)]

for i in range(N):
    now = 0
    for j in range(N):
        now += MAP[i][j]
        SUM_MAP[i+1][j+1] = SUM_MAP[i][j+1] + now

for _ in range(M):
    ans = 0
    x1, y1, x2, y2 = map(int, input().split())
    print(SUM_MAP[x2][y2] - SUM_MAP[x2][y1-1] - SUM_MAP[x1-1][y2] + SUM_MAP[x1-1][y1-1])
