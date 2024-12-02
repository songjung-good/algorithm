M, N = map(int, input().split())
BOX = []
red_to = []
green_to = 0
day = 0
for n in range(N):
    tomato = list(map(int, input().split()))
    BOX.append(tomato)
    for m in range(M):
        if tomato[m] == 1:
            red_to.append((n,m))
        elif tomato[m] == 0:
            green_to += 1

d = [0, 0, -1, 1]
while red_to:
    new_red = []
    for x, y in red_to:
        for z in range(4):
            dx = x + d[z]
            dy = y + d[3-z]
            if 0 <= dx < N and 0 <= dy < M and BOX[dx][dy] == 0:
                BOX[dx][dy] = 1
                new_red.append((dx, dy))
                green_to -= 1
    if new_red:
        day += 1
    red_to = new_red

if green_to > 0:
    print(-1)
else:
    print(day)
