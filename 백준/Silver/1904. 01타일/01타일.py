N = int(input())
dp = [0] * 1000001
dp[1] = 1
dp[2] = 2

for n in range(3, N+1):
    dp[n] = (dp[n-1] + dp[n-2]) % 15746

print(dp[N])