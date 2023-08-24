#3 하향 방향탐색

T = int(input())
for tc in range(1, T+1):
    #판의 사이즈
    size = int(input())
    #판의 모양
    board = [list(map(str, input())) for _ in range(size)]
    di = [0, 1, 1, 1]
    dj = [1, 1, 0, -1]
    ans = 'NO'

    for i in range(size):
        for j in range(size):
            if board[i][j] == 'o':
                for k in range(4):
                    for a in range(1, 5):
                        ni = i + di[k]*a
                        nj = j + dj[k]*a
                        if 0<= ni < size and 0 <= nj < size:
                            if board[ni][nj] != 'o':
                                break
                            else:
                                if a == 4:
                                    ans = 'YES'

    print(f'#{tc} {ans}')