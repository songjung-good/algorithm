import sys
input = sys.stdin.readline

N, M = map(int,input().split())
INF = 1e9
DP = [[INF] * N for _ in range(N)]

# 자신과의 거리 0
for n in range(N):
    DP[n][n] = 0

# 직접 닿은 거리 1
for _ in range(M):
    n, m = map(int,input().split())
    DP[n-1][m-1] = 1
    DP[m-1][n-1] = 1

# 나머지
for i in range(N):
    for j in range(N):
        for k in range(N):
            DP[j][k] = min(DP[j][k], DP[j][i] + DP[i][k])

min_gap = INF
ans = 0
for n in range(N):
    cnt = sum(DP[n])
    if min_gap > cnt:
       min_gap = cnt
       ans = n

print(ans+1)