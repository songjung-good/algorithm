from itertools import combinations

def max_num(arr):
    max_sum = 0

    for comb in combinations(arr, 3):
        total = sum(comb)
        total = total % 10
        if total > max_sum:
            max_sum = total

    return max_sum

N = int(input())
sum_lst = []
for n in range(N):
    lst = list(map(int, input().split()))
    sum_lst.append(max_num(lst))

ans = 0
cnt = 0
for i in range(N):
    if sum_lst[i] >= cnt:
        cnt = sum_lst[i]
        ans = i+1
print(ans)