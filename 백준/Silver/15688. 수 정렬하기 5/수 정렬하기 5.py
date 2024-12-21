# 코드를 작성해주세요
import sys
input = sys.stdin.readline

N = int(input())
n_lst = []
for _ in range(N):
    n_lst.append(int(input()))

n_lst = sorted(n_lst)
for n in n_lst:
    print(n)