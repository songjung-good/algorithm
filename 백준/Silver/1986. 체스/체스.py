# 코드를 작성해주세요
import sys
input = sys.stdin.readline
Q_r=[-1, -1, 0, 1, 1, 1, 0, -1]
Q_c=[0, 1, 1, 1, 0, -1, -1, -1]
K_r=[-2, -2, -1, 1, 2, 2, -1, 1]
K_c=[-1, 1, 2, 2, -1, 1, -2, -2]

N, M = map(int, input().split())
board = [[True] * M for _ in range(N)]
Q = list(map(int, input().split()))
K = list(map(int, input().split()))
P = list(map(int, input().split()))

for p in range(P[0]):
    now = 2 * p
    board[P[now+1]-1][P[now+2]-1] = None

# 나이트 먼저해서 퀸 움직임 제한하기
for k in range(K[0]):
    now = 2 * k
    r, c = K[now + 1] - 1, K[now + 2] - 1
    board[r][c] = None
    for n in range(8):
        nr, nc = r+K_r[n], c+K_c[n]
        if 0 <= nr < N and 0 <= nc < M and board[nr][nc] != None:
            board[nr][nc] = False

for q in range(Q[0]):
    now = 2 * q
    r, c = Q[now+1] - 1, Q[now + 2] - 1
    board[r][c] = None
    for n in range(8):
        for i in range(1, max(N, M)):
            nr, nc = r + Q_r[n] * i, c + Q_c[n] * i
            if 0 <= nr < N and 0 <= nc < M and board[nr][nc] != None:
                board[nr][nc] = False
            else:
                break

ans = 0
for n in range(N):
    for m in range(M):
        if board[n][m]:
            ans += 1
print(ans)