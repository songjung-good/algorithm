N1, M1 = map(int,input().split())
procession1 = [list(map(int, input().split())) for _ in range(N1)]

N2, M2 = map(int, input().split())
procession2 = [list(map(int, input().split())) for _ in range(N2)]

ans = [[0] * M2 for _ in range(N1)]
for n in range(N1):
    for m in range(M2):
        now = 0
        for x in range(N2):
            now += procession1[n][x] * procession2[x][m]
        ans[n][m] = now

for i in range(N1):
    print(*ans[i])