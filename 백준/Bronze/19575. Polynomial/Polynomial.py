import sys
input = sys.stdin.readline

MOD = 10 ** 9 + 7
N, x = map(int,input().split())
a, i = map(int, input().split())
d=[0]*(N+1)
d[i] = a

for _ in range(N):
    a, i = map(int, input().split())
    d[i] = (d[i+1] * x + a) % MOD

print(d[0])