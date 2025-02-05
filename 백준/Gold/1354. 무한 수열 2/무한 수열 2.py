import sys
input = sys.stdin.readline

DP = {
    0: 1,
}
N, P, Q, X, Y = map(int, input().split())

def dp(num):
    if num in DP:
        return DP[num]

    A = max(0, num // P - X)
    B = max(0, num // Q - Y)

    DP[num] = dp(A) + dp(B)
    return DP[num]

print(dp(N))