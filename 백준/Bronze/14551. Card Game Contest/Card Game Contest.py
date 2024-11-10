N, M = map(int, input().split())
ans = 1
for n in range(N):
    A = int(input())
    if A == 0:
        pass
    else:
        ans *= A

print(ans%M)