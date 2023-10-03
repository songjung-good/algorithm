import sys
input = sys.stdin.readline

num_lst = [0] * 10001
N = int(input())

for _ in range(N):
    num_lst[int(input())] += 1

for i in range(1, 10001):
    if num_lst[i] > 0:
        for _ in range(num_lst[i]):
            print(i)
