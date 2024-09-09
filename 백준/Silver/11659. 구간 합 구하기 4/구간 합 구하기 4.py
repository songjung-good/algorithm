import sys
input = sys.stdin.readline

N, M = map(int, input().split())
num_lst = [0]

now_sum = 0
for num in map(int, input().split()):
    now_sum = now_sum + num
    num_lst.append(now_sum)

for m in range(M):
    start, end = map(int, input().split())
    print(num_lst[end] - num_lst[start-1])