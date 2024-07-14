N, M = map(int, input().split())
LAND = [input() for _ in range(N)]
X = 0
Y = 0

for row in range(N):
    cnt = 0
    for col in range(M):
        if LAND[row][col] == 'X':
            break
        else:
            cnt += 1
    if cnt == M:
        X += 1

for col in range(M):
    cnt_1 = 0
    for row in range(N):
        if LAND[row][col] == 'X':
            break
        else:
            cnt_1 += 1
    if cnt_1 == N:
        Y += 1

print(max(X, Y))