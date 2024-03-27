A = int(input())
dp = [0] * (A + 1)  # A까지의 최소 연산 횟수를 저장할 리스트

for i in range(2, A + 1):
    # 현재 수에서 1을 뺀 경우
    dp[i] = dp[i - 1] + 1
    # 현재 수가 2로 나누어 떨어지는 경우
    if i % 2 == 0:
        dp[i] = min(dp[i], dp[i // 2] + 1)
    # 현재 수가 3으로 나누어 떨어지는 경우
    if i % 3 == 0:
        dp[i] = min(dp[i], dp[i // 3] + 1)

print(dp[A])
