N, A, D = map(int,input().split())
lst = list(map(int,input().split()))
next = A
ans = 0
for n in range(N):
    if next == lst[n]:
        next += D
        ans += 1

print(ans)