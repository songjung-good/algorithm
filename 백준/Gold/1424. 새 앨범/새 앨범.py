import sys
input = sys.stdin.readline

N = int(input())
L = int(input())
C = int(input())

T = (C + 1) // (L + 1)

ans = 10**18

for k in range(T, 0, -1):
    if k % 13 == 0:
        continue

    q, r = divmod(N, k)

    if r == 0:
        ans = min(ans, q)
        continue

    if q == 0 and r % 13 == 0:
        ans = min(ans, 2)
        continue

    extra = 1
    if r % 13 == 0 and r + 1 == k:
        extra = 2

    ans = min(ans, q + extra)

print(ans)