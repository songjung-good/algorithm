T = int(input())
for tc in range(1, T+1):
    # H : 호텔의 층, W : 층마다 방의 수, N : 마지막 손님
    H, W, N = map(int, input().split())
    cnt = 0

    for j in range(1, W+1):
        for i in range(1, H+1):
            cnt+=1
            if cnt == N:
                break
        if cnt == N:
            break

    if j >= 10:
        ans = str(i) + str(j)
    else:
        ans = str(i) + '0' + str(j)

    print(ans)