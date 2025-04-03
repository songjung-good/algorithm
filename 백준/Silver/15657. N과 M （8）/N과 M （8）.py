N, M = map(int, input().split())
N_lst = list(map(int, input().split()))
N_lst.sort()
lst = [0] * M

def num(lst, n, m):
    if m == M:
        print(*lst)
    else:
        for i in range(n, N):
            lst[m] = N_lst[i]
            num(lst, i, m+1)

num(lst, 0, 0)