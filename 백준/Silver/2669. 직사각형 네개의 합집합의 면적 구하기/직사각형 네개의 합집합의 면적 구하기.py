
field = [[0] * 101 for _ in range(101)]
ans = 0
cnt = 0

for _ in range(4):
    ldx, ldy, rux, ruy = map(int, input().split())

    for i in range(ldx, rux):
        for j in range(ldy, ruy):
            if field[i][j] == 0:
                field[i][j] = 1
                ans += 1

print(ans)