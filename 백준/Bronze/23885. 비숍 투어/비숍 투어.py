N, M = map(int,input().split())
sx, sy = map(int,input().split())
ex, ey = map(int,input().split())
SX = sx % 2
SY = sy % 2
EX = ex % 2
EY = ey % 2

if N == 1 or M == 1:
    if sx == ex and sy == ey:
        print('YES')
    else:
        print('NO')
elif SX == EX:
    if SY == EY:
        print('YES')
    else:
        print('NO')
elif SX != EX:
    if SY != EY:
        print('YES')
    else:
        print('NO')
