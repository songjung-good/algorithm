N, M = map(int,input().split())
l, r = 1, M
cnt = 0
for _ in range(int(input())):
    j=int(input())
    if l <= j <= r:
        pass
    else:
        if l > j:
            num = l - j
            cnt += num
            l, r = l - num, r - num
        elif r < j:
            num = j - r
            cnt += num
            l, r = l + num, r + num
print(cnt)