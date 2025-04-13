N, M = map(int,input().split())
A = {}
A_lst = list(map(int,input().split()))
for a in A_lst:
    A[a] = 1
B_lst = list(map(int,input().split()))
for b in B_lst:
    if b in A:
        N -= 1
    else:
        N += 1

print(N)