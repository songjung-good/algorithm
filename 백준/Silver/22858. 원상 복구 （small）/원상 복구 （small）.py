import sys
input = sys.stdin.readline

N, K = map(int, input().split())
S = list(map(int, input().split()))
D = list(map(int, input().split()))

if N == 1:
    pass
else:
    for _ in range(K):
        New_S = [0] * N
        for n in range(N):
            New_S[D[n] - 1] = S[n]
        S = New_S

print(*S)
