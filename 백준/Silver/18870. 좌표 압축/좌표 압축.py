import sys
input = sys.stdin.readline

N = int(input())
n_lst = list(map(int, input().split()))
sort_lst = sorted(set(n_lst))

index_map = {value: idx for idx, value in enumerate(sort_lst)}

for n in n_lst:
    print(index_map[n], end=' ')