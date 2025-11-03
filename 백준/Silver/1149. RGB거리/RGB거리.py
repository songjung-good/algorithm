N = int(input())
MAP = [list(map(int, input().split())) for _ in range(N)]

cost = MAP[0]

cnt = 1
while N > cnt:
    now = MAP[cnt]
    A = min(now[0] + cost[1], now[0] + cost[2])
    B = min(now[1] + cost[0], now[1] + cost[2])
    C = min(now[2] + cost[0], now[2] + cost[1])
    cost = [A, B, C]
    cnt += 1

print(min(cost))