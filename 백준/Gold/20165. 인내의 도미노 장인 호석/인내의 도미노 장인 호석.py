# 코드를 작성해주세요
import sys
input = sys.stdin.readline

N, M, R = map(int, input().split())
# 도미노 높이, 도미도 상태
DOMINO = [list(map(int, input().split())) for _ in range(N)]
DOMINO_state = [['S'] * M for _ in range(N)]
# E, W, N, S
D = {
    'E': (0, 1),
    'W': (0, -1),
    'S': (1, 0),
    'N': (-1, 0),
}

ans = 0
for _ in range(R):
    # 공격위치
    A_row, A_col, site = map(str, input().split())
    row, col = int(A_row) - 1, int(A_col) - 1
    # 방향설정
    x, y = D[site]

    # 첫 도미노
    if DOMINO_state[row][col] == 'F':
        height = 0
    else:
        height = DOMINO[row][col]
        DOMINO_state[row][col] = 'F'
        ans += 1
    height -= 1

    # 이후 도미노
    while height:
        row, col = row + x, col + y
        if 0 <= row < N and 0 <= col < M:
            if DOMINO_state[row][col] == 'F':
                pass
            else:
                height = max(DOMINO[row][col], height)
                ans += 1
                DOMINO_state[row][col] = 'F'
            height -= 1
        else:
            break

    # 수비위치 이건 끝
    D_row, D_col = map(int, input().split())
    DOMINO_state[D_row-1][D_col-1] = 'S'

print(ans)
for i in range(N):
    print(*DOMINO_state[i])
