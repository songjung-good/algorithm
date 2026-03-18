N, score, P = map(int, input().split())

if P == 0:
    print(-1)
    exit()

if N == 0:
    print(1)
    exit()

lst = list(map(int, input().split()))

ans = -1
num = 0
for p in range(P):
    if p >= N:
        break
    if lst[p] == score and num == 0:
        num = p+1
    if lst[p] < score:
        ans = p + 1
        break

if ans == -1:
    if N < P:
        ans = N + 1

if num != 0 and ans != -1:
    ans = num

print(ans)
