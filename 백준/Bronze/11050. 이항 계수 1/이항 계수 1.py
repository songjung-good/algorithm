# 코드를 작성해주세요
from itertools import combinations

N, K = map(int, input().split())
num_lst = [n for n in range(N)]

combi_lst = list(combinations(num_lst, K))

print(len(combi_lst))
    