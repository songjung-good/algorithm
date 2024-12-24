# 코드를 작성해주세요
import sys
input = sys.stdin.readline

N = int(input())
stairs = [0] + [int(input()) for _ in range(N)]

if N == 1:
    print(stairs[1])

else:
    DP = [0] * (N+1)
    DP[1] = stairs[1]
    DP[2] = stairs[1] + stairs[2]

    for i in range(3, N+1):
        # DP[i-2]와 DP[i-3] + stairs[i-1]를 통해  연속 계단 방지
        DP[i] = max(DP[i-2], DP[i-3] + stairs[i-1]) + stairs[i]
        
    print(DP[N])