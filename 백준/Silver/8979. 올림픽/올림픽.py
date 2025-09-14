import sys
input = sys.stdin.readline

N, M = map(int, input().split())
MAP = [list(map(int, input().split())) for _ in range(N)]

MAP.sort(key=lambda x: (-x[1], -x[2], -x[-3]))

rank = {MAP[0][0]: 1}
now = 1

for i in range(1, N):
    if MAP[i][1:] == MAP[i-1][1:]:
        rank[MAP[i][0]] = now
    else:
        now += 1
        rank[MAP[i][0]] = now

print(rank[M])