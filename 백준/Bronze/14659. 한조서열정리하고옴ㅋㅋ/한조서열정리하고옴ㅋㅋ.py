N = int(input())
lst = list(map(int, input().split()))
ans = 0
now = 0
cnt = 0
for n in range(1, N):
    if lst[now] > lst[n]:
        cnt += 1
    else:
        if ans < cnt:
            ans = cnt
        cnt = 0
        now = n
if ans < cnt:
    ans = cnt
print(ans)