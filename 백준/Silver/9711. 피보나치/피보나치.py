dp = [0] * 10001
fibo_len = 2
dp[0] = 1
dp[1] = 1

def fibo(num):
    global fibo_len, dp
    if fibo_len >= num:
        return dp[num-1]
    else:
        for i in range(fibo_len, num):
            dp[i] = dp[i-2] + dp[i-1]
        fibo_len = num
        return dp[num-1]

T = int(input())
for t in range(1, T+1):
    P, Q = map(int, input().split())
    ans = fibo(P) % Q
    print(f"Case #{t}: {ans}")
