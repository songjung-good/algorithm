N = int(input())
n_lst = [1, 1]

if N == 1:
    print(4)
elif N == 2:
    print(6)
elif N == 3:
    print(10)
else:
    for n in range(2, N):
        n_lst.append(n_lst[n-1] + n_lst[n-2])

    ans = n_lst[-1] * 3 + n_lst[-2] * 2 + n_lst[-3] * 2 + n_lst[-4]
    print(ans)
