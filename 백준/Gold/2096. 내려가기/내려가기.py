import sys
input = sys.stdin.readline

N = int(input())
first_lst = list(map(int, input().split()))
max_dp = first_lst[:]
min_dp = first_lst[:]

for _ in range(N-1):
    lst = list(map(int, input().split()))

    max_ = [
        max(max_dp[0], max_dp[1]) + lst[0],
        max(max_dp[0], max_dp[1], max_dp[2]) + lst[1],
        max(max_dp[1], max_dp[2]) + lst[2],
    ]

    min_ = [
        min(min_dp[0], min_dp[1]) + lst[0],
        min(min_dp[0], min_dp[1], min_dp[2]) + lst[1],
        min(min_dp[1], min_dp[2]) + lst[2],
    ]

    max_dp = max_
    min_dp = min_

print(max(max_dp), min(min_dp))