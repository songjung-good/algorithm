a, b = map(int, input().split())
R = int(input())

GARDEN = [[0] * (R - i) for i in range(R)]

time = 0
GARDEN[a][b] = 1

while GARDEN[a][b] <= 1:
    if a + 1 + b + 1 < R:
        a += 1
        b += 1
    else:
        a //= 2
        b //= 2
    GARDEN[a][b] += 1
    time += 1

print(time)