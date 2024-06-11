MAP = [list(map(str, input().split())) for _ in range(10)]
ans = 0

for row in range(10):
    now = ''
    for col in range(10):
        if col != 0 and now != MAP[row][col]:
            break
        else:
            now = MAP[row][col]
        if col == 9:
            ans = 1
    if ans == 1:
        break

if ans != 1:
    for col in range(10):
        for row in range(10):
            if row != 0 and now != MAP[row][col]:
                break
            else:
                now = MAP[row][col]
            if row == 9:
                ans = 1
        if ans == 1:
            break

print(ans)