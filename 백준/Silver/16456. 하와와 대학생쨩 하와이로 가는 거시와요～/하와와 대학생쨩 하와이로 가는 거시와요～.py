# 코드를 작성해주세요
N = int(input())
DP = [0] * 50001
DP[1] = 1 % 1000000009
DP[2] = 1 % 1000000009
DP[3] = 2 % 1000000009

if N <= 3:
    print(DP[N] % 1000000009)
else:
    for i in range(4, N+1):
        DP[i] = (DP[i-1] + DP[i-3]) % 1000000009
    print(DP[N])