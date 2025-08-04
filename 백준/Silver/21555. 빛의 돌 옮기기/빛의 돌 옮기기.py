# 코드를 작성해주세요
N, K = map(int, input().split())
A_lst = list(map(int, input().split()))
B_lst = list(map(int, input().split()))

dp = [[0] * N for _ in range(2)]
dp[0][0] = A_lst[0]
dp[1][0] = B_lst[0]
for i in range(1, N):
    dp[0][i] = min(dp[0][i-1], dp[1][i-1] + K) + A_lst[i]
    dp[1][i] = min(dp[1][i-1], dp[0][i-1] + K) + B_lst[i]

print(min(dp[0][N-1], dp[1][N-1]))
