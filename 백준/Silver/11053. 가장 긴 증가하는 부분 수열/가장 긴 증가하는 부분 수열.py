N = int(input())
N_lst = list(map(int, input().split()))
len_lst = [0] * N
len_lst[N-1] = 1

for n in range(N-2,-1,-1):
    now = N_lst[n]
    cnt = 0
    for m in range(n+1, N):
        if now >= N_lst[m]:
            pass
        else:
            if len_lst[m] > cnt:
                cnt = len_lst[m]
    len_lst[n] = cnt + 1

print(max(len_lst))