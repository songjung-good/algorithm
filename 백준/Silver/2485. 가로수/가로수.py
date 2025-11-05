from math import gcd
from functools import reduce

N = int(input())
trees = [int(input()) for _ in range(N)]
dist = [trees[i+1] - trees[i] for i in range(N-1)]

g = reduce(gcd, dist)

ans=(trees[N-1] - trees[0]) // g - N
print(ans+1)