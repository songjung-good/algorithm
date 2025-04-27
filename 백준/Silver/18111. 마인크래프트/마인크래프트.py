import sys
input = sys.stdin.readline

N, M, B = map(int, input().split())
GROUND = [list(map(int, input().split())) for _ in range(N)]

# 입력 데이터에서 최소 높이와 최대 높이를 구함
min_height = min(map(min, GROUND))
max_height = max(map(max, GROUND))

TIME = float('inf')
HEIGHT = 0

for h in range(min_height, max_height + 1):
    surplus, required = 0, 0

    for i in range(N):
        for j in range(M):
            now = GROUND[i][j]

            if now < h:
                required += h - now
            else:
                surplus += now - h

    if surplus + B < required:
        pass
    else:
        t = surplus * 2 + required
        if t <= TIME:
            HEIGHT = h
            TIME = t


print(TIME, HEIGHT)