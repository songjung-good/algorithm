D = [0, 0, 1, -1]

N, M = map(int, input().split())
PUZZLE = [input() for _ in range(N)]
cnt = 0
for r in range(N):
    for c in range(M):
        now = PUZZLE[r][c]
        if now == 'Y':
            for n in range(4):
                nr, nc = r+D[n], c+D[3-n]
                if 0 <= nr < N and 0 <= nc < M and PUZZLE[nr][nc] == 'X':
                    cnt += 1

print(cnt)