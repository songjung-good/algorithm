import math
origin = [['A', 'B', 'C', 'D'], ['E', 'F', 'G', 'H'], ['I', 'J', 'K', 'L'], ['M', 'N', 'O', '.']]
MAP=[list(map(str, input())) for _ in range(4)]

gap = 0

for i in range(4):
    for j in range(4):
        now = origin[i][j]
        if now == '.':
            pass
        else:
            for x in range(4):
                for y in range(4):
                    if MAP[x][y] == now:
                        gap += abs(i - x) + abs(j-y)
                        break
print(gap)