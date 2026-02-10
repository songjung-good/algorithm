import sys
input = sys.stdin.readline

D, K = map(int, input().split())

for i in range(1, K):
    for j in range(i, K):
        dp = [i, j]
        for k in range(3, D+1):
            dp[0], dp[1] = dp[1], dp[0] + dp[1]

        if dp[1] == K:
            print(i)
            print(j)
            exit()
