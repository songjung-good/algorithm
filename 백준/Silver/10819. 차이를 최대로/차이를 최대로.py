import sys
from itertools import permutations

input = sys.stdin.readline

N = int(input().strip())
A = list(map(int, input().split()))

ans = 0

for p in permutations(A):
    s = 0
    for i in range(N - 1):
        diff = p[i] - p[i + 1]
        if diff < 0:
            diff = -diff
        s += diff
    if s > ans:
        ans = s

print(ans)