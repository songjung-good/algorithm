N, M = map(int, input().split())
BOARD = [input().strip() for _ in range(N)]

BW = ['BWBWBWBW', 'WBWBWBWB'] * 4
WB = ['WBWBWBWB', 'BWBWBWBW'] * 4
min_cnt = 64
for n in range(N-7):
    for m in range(M-7):
        bw_cnt = 0
        wb_cnt = 0

        for i in range(8):
            for j in range(8):

                if BOARD[n+i][m+j] != BW[i][j]:
                    bw_cnt += 1
                if BOARD[n+i][m+j] != WB[i][j]:
                    wb_cnt += 1

        min_cnt = min(min_cnt, bw_cnt, wb_cnt)

print(min_cnt)
