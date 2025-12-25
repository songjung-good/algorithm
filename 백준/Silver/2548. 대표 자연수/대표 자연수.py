import sys
input = sys.stdin.readline
N = int(input())
lst = list(map(int, input().split()))
a, b = min(lst), max(lst)
gap = float('inf')
ans = 0

for i in range(a, b+1):
    now = 0
    for j in lst:
        now += abs(i-j)
    if gap > now:
        gap = now
        ans = i

print(ans)