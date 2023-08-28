import sys

input = sys.stdin.readline

def dfs(x, y, shape):
    global ans
    if x == n-1 and y == n-1:
        ans += 1
        return

    if shape == 0 or shape == 2:
        if y + 1 < n:
            if a[x][y+1] == 0:
                dfs(x, y+1, 0)
    if shape == 1 or shape == 2:
        if x + 1 < n:
            if a[x+1][y] == 0:
                dfs(x+1, y, 1)
    if shape == 0 or shape == 1 or shape == 2:
        if x + 1 < n and y + 1 < n:
            if a[x+1][y] == 0 and a[x][y+1] == 0 and a[x+1][y+1] == 0:
                dfs(x+1, y+1, 2)


n = int(input())
a = [list(map(int, input().split())) for _ in range(n)]
ans = 0
dfs(0, 1, 0)
print(ans)

# def bfs(coord, d):
#     global cnt
#     if coord == (N - 1, N - 1):
#         cnt += 1
#         return
#     x, y = coord
#     if d == (1, 1):
#         D = D11
#     elif d == (1, 0):
#         D = D10
#     else:
#         D = D01
#
#     for dx, dy in D:
#         nx, ny = x + dx, y + dy
#         if 0 <= nx < N and 0 <= ny < N:
#             if lst[nx][ny] == 0:
#                 if dx != dy:
#                     bfs((nx, ny), (dx, dy))
#                 else:
#                     if lst[x][ny] == 0 and lst[nx][y] == 0:
#                         bfs((nx, ny), (dx, dy))
#
#
#
# D11 = [(1, 1), (1, 0), (0, 1)]
# D10 = [(1, 1), (1, 0)]
# D01 = [(1, 1), (0, 1)]
#
# N = int(input())
# lst = [list(map(int, input().split())) for _ in range(N)]
# cnt = 0
# bfs((0, 1), (0, 1))
# print(cnt)