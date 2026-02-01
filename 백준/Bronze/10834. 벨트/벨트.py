M = int(input())
x, y = 1, 0
for _ in range(M):
    a, b, i = map(int, input().split())
    if i == 1:
        if y:
            y = 0
        else:
            y = 1

    x = x * (b / a)

print(y, int(x))