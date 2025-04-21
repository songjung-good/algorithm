import sys
input = sys.stdin.readline

K, N = map(int, input().split())
LAN = [int(input()) for _ in range(K)]
S, E = 1, max(LAN)

while S <= E:
    cnt = 0
    M = (E + S) // 2
    for l in LAN:
        cnt += l // M
    if cnt >= N:
        S = M+1
    else:
        E = M-1

print(E)