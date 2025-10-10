import sys
input = sys.stdin.readline

N, K = map(int, input().split())
MAP = [list(map(int, input().split())) for _ in range(N)]
ans = [[0]*(N*K) for _ in range(N*K)]
for i in range(N):
    for j in range(N):
        now = MAP[i][j]
        for x in range(i*K, i*K+K):
            for y in range(j*K, j*K+K):
                ans[x][y] = now

for i in ans:
    print(*i)