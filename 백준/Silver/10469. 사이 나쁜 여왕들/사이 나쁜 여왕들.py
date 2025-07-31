# 코드를 작성해주세요
BOARD = [list(input()) for _ in range(8)]
dx = [-1,-1,0,1,1,1,0,-1]
dy = [0,1,1,1,0,-1,-1,-1]
cnt = 0
for r in range(8):
    for l in range(8):
        if BOARD[r][l] == '*':
            cnt += 1
            for d in range(8):
                for i in range(1,8):
                    nx = dx[d]*i+r
                    ny = dy[d]*i+l
                    if 0 <= nx < 8 and 0 <= ny < 8:
                        if BOARD[nx][ny] == '*':
                            print('invalid')
                            exit()
                    else:
                        break
if cnt == 8:
    print('valid')
else:
    print('invalid')