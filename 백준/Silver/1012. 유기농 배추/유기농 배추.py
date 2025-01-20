from collections import deque
import sys
input = sys.stdin.readline

D = [0, 0, 1, -1]

def bfs(s_row, s_col):
    queue = deque([(s_row, s_col)])
    while queue:
        r, c = queue.popleft()
        # 체크한 밭은 0으로 중복확인 제거
        for n in range(4):
            nr = D[n] + r
            nc = D[3-n] + c
            if 0 <= nr < N and 0 <= nc < M and FARM[nr][nc] == 1:
                FARM[nr][nc] = 0
                queue.append((nr, nc))

# 테스트 수 T, 가로길이 M, 세로길이 N, 배추 수 K
T = int(input())
for _ in range(T):
    M, N, K = map(int, input().split())
    # 배추 밭 FARM, 1은 배추 위치, 0은 빈 땅
    FARM = [[0] * M for _ in range(N)]
    for _ in range(K):
        col, row = map(int, input().split())
        FARM[row][col] = 1

    # 지렁이 있는 그룹 수 CNT
    CNT = 0
    for m in range(M):
        for n in range(N):
            if FARM[n][m] == 1:
                bfs(n, m)
                CNT += 1

    print(CNT)