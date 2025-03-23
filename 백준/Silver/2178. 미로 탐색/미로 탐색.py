N, M = map(int, input().split())
MAP = [list(map(int, input())) for _ in range(N)]
V = [[0] * M for _ in range(N)]
Q = [(0,0)]
D = [0,0,1,-1]

while Q:
    x, y = Q.pop(0)
    V[x][y] += 1
    cnt = V[x][y]
    for d in range(4):
        nx, ny = x + D[d], y + D[3-d]
        if 0<=nx<N and 0<=ny<M and V[nx][ny]==0 and MAP[nx][ny]==1:
            Q.append((nx,ny))
            V[nx][ny] = cnt


print(V[N-1][M-1])
