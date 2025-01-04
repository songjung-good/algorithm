N, Q = map(int, input().split())
B_lst = [1] * (N + 1)

for q in range(Q):
    L, I = map(int, input().split())
    B_lst[L] = 0
    n = 0
    while True:
        n += 1
        if (L + (n * I)) > N:
            break
        else:
            B_lst[L + (n * I)] = 0

B_lst.pop(0)
print(sum(B_lst))