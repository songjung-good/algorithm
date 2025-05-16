N = int(input())
for _ in range(N):
    lst = list(map(int, input().split()))
    cnt = 0
    check = 101
    for i in lst:
        if i % 2:
            pass
        else:
            cnt += i
            if check > i:
                check = i
    print(cnt, check)