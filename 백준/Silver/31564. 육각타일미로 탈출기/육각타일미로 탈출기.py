import sys
input = sys.stdin.readline
from collections import deque

N, M, K = map(int, input().split())
MAZE = [[0] * M for _ in range(N)]
for _ in range(K):
    x, y = map(int, input().split())
    MAZE[x][y] = -1

check = deque([(0,0)])
while check:
    a, b = check.popleft()
    cnt = MAZE[a][b]

    if a % 2:
        # 홀수 칸
        dx = [-1, -1, 0, 1,  1, 0]
        dy = [0, 1, 1, 1, 0, -1]

    else:
        # 짝수 칸
        dx = [-1, -1, 0, 1, 1, 0]
        dy = [-1, 0, 1, 0, -1, -1]

    for i in range(6):
        nx, ny = a + dx[i], b + dy[i]
        if 0 <= nx < N and 0 <= ny < M and MAZE[nx][ny] == 0:
            check.append((nx, ny))
            MAZE[nx][ny] = cnt + 1

ans = MAZE[N-1][M-1]
print(ans if ans else -1)
