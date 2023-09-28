import sys
input = sys.stdin.readline

while True:
    n = int(input())
    num_lst = []
    if n == -1:
        break

    for i in range(1, n):
        if n % i == 0:
            num_lst.append(i)

    sum_n = sum(num_lst)

    if sum_n != n:
        print(f'{n} is NOT perfect.')
    else:
        print(f'{n} = ', end="")
        s = len(num_lst)
        for i in range(s-1):
            print(num_lst[i], end=" + ")

        print(num_lst[s-1])