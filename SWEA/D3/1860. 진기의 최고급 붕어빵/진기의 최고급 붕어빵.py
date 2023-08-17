T = int(input())
for t in range(1, T+1):
    N, M, K = map(int, input().split())
    sec = sorted(list(map(int, input().split())))
    res = 'Possible'
    B = 0
    cnt = 0
    for i in range(N):
        S = sec[i] // M
        if S - cnt >= 1:
            B += (S - cnt) * K
            cnt += S - cnt
        if B < 1 :
            res = 'Impossible'
            break
        else:
            B -= 1
    print(f'#{t} {res}')