'''
#1
N, M = map(int, input().split())
chess_board = [list(map(str, input().split())) for _ in range(N)]

cnt_A = 0
cnt_B = 0

for i in range(N - 7):
    for j in range(M - 7):
        for x in range(8):
            for y in range(8):
                if ((i+x) + (j+y)) % 2 == 0:
                    if chess_board[i + x][j + y] == 'W':
                        chess_board[i + x][j + y] = 'B'
                        cnt_A += 1
                    if chess_board[i + x][j + y] == 'B':
                        chess_board[i + x][j + y] = 'W'
                        cnt_B += 1
                if ((i+x) + (j+y)) % 2 == 1:
                    if chess_board[i + x][j + y] == 'B':
                        chess_board[i + x][j + y] = 'W'
                        cnt_A += 1
                    if chess_board[i + x][j + y] == 'W':
                        chess_board[i + x][j + y] = 'B'
                        cnt_B += 1

    if cnt_B >= cnt_A:
        print(cnt_A)
    else:
        print(cnt_B)

'''






#2
N, M = map(int, input().split())
chess_board = [list(map(str, input().split())) for _ in range(N)]

cnt_A = 0
cnt_B = 0

for i in range(N - 7):              #시작점 설정
    for j in range(M - 7):
        for x in range(7):          #색칠 범위 설정
            for y in range(7):
                if ((i+x) + (j+y)) % 2 == 0:
                    if chess_board[i + x][j + y] == 'W':
                        cnt_A += 1
                    else:
                        cnt_B += 1
                else:
                    if chess_board[i + x][j + y] == 'B':
                        cnt_A += 1
                    else:
                        cnt_B += 1

    if cnt_B >= cnt_A:
        print(cnt_A)
    else:
        print(cnt_B)

    cnt_B = 0
    cnt_A = 0