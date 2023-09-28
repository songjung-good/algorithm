import sys
input = sys.stdin.readline

N, K = map(int, input().split())
num_lst = []
for i in range(1, N+1):
    if N % i == 0:
        num_lst.append(i)
if len(num_lst) >= K:
    print(num_lst[K-1])
else:
    print(0)