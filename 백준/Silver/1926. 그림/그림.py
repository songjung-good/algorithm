import sys
input = sys.stdin.readline

N, M = map(int, input().split())
MAP = [list(map(int, input().split())) for _ in range(N)]
D = [1, -1, 0, 0]

max_size = 0
pic = 0
V = [[0] * M for _ in range(N)]
for r in range(N):
    for c in range(M):
        Q = []
        size = 0
        if V[r][c] == 1:
            pass
        elif MAP[r][c] == 0:
            V[r][c] = 1
        else:
            Q.append((r,c))
            V[r][c] = 1
            while Q:
                row, col = Q.pop(0)
                size += 1
                for d in range(4):
                    n_row, n_col = row+D[d], col+D[3-d]
                    if 0<=n_row<N and 0<=n_col<M and V[n_row][n_col] == 0 and MAP[n_row][n_col] == 1:
                        Q.append((n_row, n_col))
                        V[n_row][n_col] = 1
            pic += 1
        if max_size < size:
            max_size = size

print(pic)
print(max_size)