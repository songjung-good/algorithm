import sys
input = sys.stdin.readline

N, M = map(int, input().split())
MAP = [list(map(int, input().split())) for _ in range(N)]

# 누적합 배열
prefix = [[0] * (M + 1) for _ in range(N + 1)]
for i in range(1, N + 1):
    for j in range(1, M + 1):
        prefix[i][j] = (MAP[i-1][j-1]
                        + prefix[i-1][j]
                        + prefix[i][j-1]
                        - prefix[i-1][j-1])

Q = int(input())
for _ in range(Q):
    A, B, X, Y = map(int, input().split())
    # A, B, X, Y가 1-index 기준
    res = (prefix[X][Y]
           - prefix[A-1][Y]
           - prefix[X][B-1]
           + prefix[A-1][B-1])
    print(res)
