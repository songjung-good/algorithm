from itertools import combinations, permutations

N, M = map(int, input().split())
N_lst = list(map(int, input().split()))

if M == 1:
    past = 0
    N_lst.sort()
    for i in N_lst:
        if i == past:
            pass
        else:
            print(i)
        past = i
else:
    comb = list(permutations(N_lst, M))
    comb.sort()
    past = ()
    for i in comb:
        if i == past:
            pass
        else:
            print(*i)
        past = i