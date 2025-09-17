import sys
input = sys.stdin.readline

N, M = map(int, input().split())
# vertex = {}
# edge = {}
for n in range(1, N+1):
    x, y = map(int, input().split())
    # vertex[n] = (x, y)

p1 = 0
p2 = 0
p3 = 0
for _ in range(M):
    x, y, c = map(str, input().split())
    if c == 'R':
        p1 += 1
    elif c == 'B':
        p2 += 1
    else:
        p3 += 1

ans = ['jhnah917','jhnan917']

if p3 % 2:
    p1 += 1

print(ans[0]) if p1 - p2 > 0 else print(ans[1])
