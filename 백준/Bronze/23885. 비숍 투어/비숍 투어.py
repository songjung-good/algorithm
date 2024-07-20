def check(x, y, N, M):
    if x < 1 or y < 1 or x > N or y > M:
        return 1
    else:
        return 0

N, M = map(int,input().split())
sx, sy = map(int,input().split())
ex, ey = map(int,input().split())
S = (sx+sy) % 2
E = (ex+ey) % 2

A = check(sx, sy, N, M)
B = check(ex, ey, N, M)

if A == 1 or B == 1:
    print('NO')
elif S == E:
    print('YES')
elif S != E:
    print('NO')