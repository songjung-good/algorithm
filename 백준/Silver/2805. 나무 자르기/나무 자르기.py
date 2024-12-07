import sys
input = sys.stdin.readline

N, M = map(int, input().split())
TREES = list(map(int, input().split()))

low, high = 0, max(TREES)
res = 0
while low <= high:
    mid = (low + high) // 2

    total = 0
    for t in TREES:
        if t > mid:
            total += (t - mid)

    if total >= M:
        res = mid
        low = mid + 1
    else:
        high = mid - 1

print(res)