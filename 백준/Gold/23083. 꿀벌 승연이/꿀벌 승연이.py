import sys
from collections import deque
input = sys.stdin.readline

de = [(-1, 1), (0, 1), (1, 0)]
do = [(0, 1), (1, 1), (1, 0)]
MOD = 10**9 + 7

N, M = map(int, input().split())
K = int(input())
MAP = [[False] * M for _ in range(N)]
DP = [[0] * M for _ in range(N)]
DP[0][0] = 1

for _ in range(K):
    x, y = map(int, input().split())
    MAP[x - 1][y - 1] = True

for j in range(M):
    for i in range(N):
        if MAP[i][j] or DP[i][j] == 0:
            continue
        for n in range(3):
            if j % 2:
                x, y = i + do[n][0], j + do[n][1]
            else:
                x, y = i + de[n][0], j + de[n][1]
            if 0 <= x < N and 0 <= y < M and MAP[x][y] == False:
                DP[x][y] = (DP[x][y] + DP[i][j]) % MOD

print(DP[N-1][M-1])