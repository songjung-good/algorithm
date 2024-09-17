N, M = map(int, input().split())
MAP = [list(map(int, input().split())) for _ in range(N)]
GOAL = []
for n in range(N):
    for m in range(M):
        if MAP[n][m] == 1:
            GOAL.append([n,m])

X = abs(GOAL[0][0] - GOAL[1][0])
Y = abs(GOAL[0][1] - GOAL[1][1])

A = X + Y
print(A)