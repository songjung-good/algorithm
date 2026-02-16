n=int(input())
dp = [0, 1]
if n in [0, 1]:
    print(dp[n])
else:
    for _ in range(n-1):
        dp[0], dp[1] = dp[1], dp[0] + dp[1]

    print(dp[1])