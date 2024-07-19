from math import prod
N = int(input())
NUM_lst = list(map(int, input().split()))
MAX_NUM = 0
for i in range(1, N-2):
    for j in range(i+1, N-1):
        for k in range(j+1, N):
            SUM_num = prod(NUM_lst[:i]) + prod(NUM_lst[i:j]) + prod(NUM_lst[j:k]) + prod(NUM_lst[k:])
            MAX_NUM = max(MAX_NUM, SUM_num)

print(MAX_NUM)