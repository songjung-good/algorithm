import sys
input = sys.stdin.readline

N = int(input())
sum_lst = [0] * N
sum_lst[0] = int(input())

for n in range(2, N+1):
    lst = list(map(int, input().split()))
    for i in range(n):
        if i == 0:
            lst[0] = sum_lst[0] + lst[0]
        elif i == n:
            lst[i] = sum_lst[i - 1] + lst[i]
        else:
            lst[i] = max(sum_lst[i] + lst[i], sum_lst[i-1] + lst[i])
    sum_lst[:n] = lst

print(max(sum_lst))