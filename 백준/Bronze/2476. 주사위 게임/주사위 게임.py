N = int(input())
ans = [0] * N
for i in range(N):
    check = [0] * 7
    lst = list(map(int, input().split()))
    cnt = 0
    for l in lst:
        check[l] += 1
    if 3 in check:
        cnt = 10000 + check.index(3) * 1000
    elif 2 in check:
        cnt = check.index(2) * 100 + 1000
    else:
        cnt = max(lst) * 100
    ans[i] = cnt

print(max(ans))