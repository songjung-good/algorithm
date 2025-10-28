import sys
input = sys.stdin.readline

N, K = map(int, input().split())
lst = [tuple(map(int, input().split())) for _ in range(N)]

dp = [0] * (K + 1)

for w, v in lst:
    if w > K:
        pass
    else:
        for weight in range(K, w - 1, -1):
            dp[weight] = max(dp[weight], dp[weight - w] + v)

print(dp[K])