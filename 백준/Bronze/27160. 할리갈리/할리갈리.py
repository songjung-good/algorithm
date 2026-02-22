N = int(input())
dict = {}
for _ in range(N):
    S, X = input().split()
    if S in dict:
        dict[S] += int(X)
    else:
        dict[S] = int(X)

ans = 'NO'
for d in dict:
    if dict[d] == 5:
        ans = 'YES'

print(ans)