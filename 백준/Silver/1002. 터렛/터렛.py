T = int(input())
for _ in range(T):
    x1, y1, r1, x2, y2, r2 = map(int, input().split())
    if r1 == r2 and x1 == x2 and y1 == y2:
        print(-1)
    else:
        d = ((x1-x2)**2 + (y1-y2)**2) ** 0.5
        if abs(r1-r2) < d < r1 + r2:
            print(2)
        elif r1+r2 == d or abs(r1-r2) == d:
            print(1)
        else:
            print(0)