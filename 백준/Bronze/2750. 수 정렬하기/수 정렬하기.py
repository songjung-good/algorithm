import sys
input = sys.stdin.readline

N = int(input())
num_lst = [list(map(int, input().split())) for _ in range(N)]

num_lst.sort()
for i in num_lst:
    print(*i)
