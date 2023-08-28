T = int(input())
for tc in range(1, T+1):
    N = int(input())
    board = [list(map(str, input())) for _ in range(N)]

    di = [0, 1, 1, 1]
    dj = [1, 1, 0, -1]
    ans = 'NO'

    for i in range(N):
        for j in range(N):
            if board[i][j] == 'o':
                for k in range(4):
                    cnt = 0
                    for a in range(1, 5):
                        ni = i + di[k] * a
                        nj = j + dj[k] * a
                        if 0 <= ni <N and 0 <= nj <N and board[ni][nj] == 'o':
                            cnt += 1
                        if cnt == 4:
                            ans = 'YES'
                            break
                    if ans == 'YES':
                        break
        if ans == 'YES':
            break

    print(f'#{tc} {ans}')