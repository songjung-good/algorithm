# 코드를 작성해주세요
N = int(input())
M = int(input())
T = list(map(int, input().split()))
S = [0] * N
for m in range(M):
    W = list(map(int, input().split()))
    for n in range(N):
        if W[n] == T[m]:
            S[n] += 1
        else:
            S[T[m]-1] += 1

for i in S:
    print(i)
        