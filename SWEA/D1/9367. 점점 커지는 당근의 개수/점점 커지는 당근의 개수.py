T = int(input())
for tc in range(1, T+1):
    N = int(input())
    ans = 0
    carrot = list(map(int, (input().split())))

    prev_i = 0
    cnt = 0
    for i in range(len(carrot)):
        if prev_i < carrot[i]:
            cnt += 1
        else:
            cnt = 1
        if ans < cnt:
            ans = cnt
        prev_i = carrot[i]

    print(f'#{tc} {ans}')