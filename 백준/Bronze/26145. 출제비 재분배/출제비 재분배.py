import sys
input = sys.stdin.readline

N, M = map(int, input().split())
S_lst = list(map(int, input().split()))
S = [0] * (N+M)

for n in range(N):
    num = list(map(int, input().split()))
    S[n] += S_lst[n] - sum(num)
    for i in range(N+M):
        S[i] += num[i]

print(*S)
