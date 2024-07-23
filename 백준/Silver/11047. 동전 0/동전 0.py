import sys
input = sys.stdin.readline

N, K = map(int, input().split())
COINS = []
CNT = 0
for n in range(N):
    COINS.insert(0, int(input()))

for i in COINS:
    coin = K // i
    CNT = CNT + coin
    K = K - (i * coin)

print(CNT)
