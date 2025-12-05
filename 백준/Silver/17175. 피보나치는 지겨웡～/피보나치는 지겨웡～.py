import sys
input = sys.stdin.readline

fibo = [1] * 51

N = int(input())
for n in range(2, N+1):
    fibo[n] = (fibo[n-2] + fibo[n-1] + 1) % 1_000_000_007

print(fibo[N])