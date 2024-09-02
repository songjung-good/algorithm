import sys
input = sys.stdin.readline

N = int(input())
tri = 2 * N
cnt = 1
for i in range(tri):
    cnt = cnt * (i + 1)
for j in range(N):
    cnt = cnt // (j + 1)
    cnt = cnt // (j + 1)
print(cnt, N**2)