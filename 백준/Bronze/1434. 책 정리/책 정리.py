N, M = map(int, input().split())
N_lst = list(map(int, input().split()))
M_lst = list(map(int, input().split()))

x, y = 0, 0
while N > x and M > y:
    if N_lst[x] >= M_lst[y]:
        N_lst[x] -= M_lst[y]
        y += 1
    else:
        x += 1

print(sum(N_lst))