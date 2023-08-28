T = int(input())
for t in range(1, T+1):
    N, M = map(int, input().split())
    lst = [input() for _ in range(N)]
    lst_wbr = [[0] * 3 for _ in range(N)]

    for i in range(N):
        lst_wbr[i][0] += (lst[i].count('W'))
        lst_wbr[i][1] += (lst[i].count('B'))
        lst_wbr[i][2] += (lst[i].count('R'))

    min_v = float('inf')
    for j in range(N - 2):
        cnt_w = 0
        for w in range(j+1):
            cnt_w += M - lst_wbr[w][0]

        for k in range(j+1, N - 1):
            cnt_b = 0
            for b in range(j+1, k+1):
                cnt_b += M - lst_wbr[b][1]

            cnt_r = 0
            for r in range(k+1, N):
                cnt_r += M - lst_wbr[r][2]
            if min_v > cnt_w + cnt_b + cnt_r:
                min_v = cnt_w + cnt_b + cnt_r

    print(f'#{t} {min_v}')