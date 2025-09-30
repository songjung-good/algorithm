import sys
from collections import deque
input = sys.stdin.readline

def drop_stone(row, col):
    global BOARD, dic
    while row < R:
        if row == R-1:
            return
        if BOARD[row+1][col] == '.':
            row += 1
            dic[drop].append((row, col))
        elif BOARD[row+1][col] == 'X':
            return
        elif BOARD[row+1][col] == 'O':
            if 0 <= col - 1 < C and BOARD[row][col-1] == '.' and BOARD[row+1][col-1] == '.':
                row += 1
                col -= 1
                dic[drop].append((row, col))
            elif  0 <= col + 1 < C and BOARD[row][col+1] == '.' and BOARD[row+1][col+1] == '.':
                row += 1
                col += 1
                dic[drop].append((row, col))
            else:
                return

R, C = map(int, input().split())
BOARD = [list(input().rstrip()) for _ in range(R)]
dic = {}

N = int(input())
for _ in range(N):
    drop = int(input()) - 1
    if not drop in dic:
        dic[drop] = deque([(0, drop)])
        drop_stone(0, drop)
    if drop in dic:
        while True:
            x, y = dic[drop].pop()
            if BOARD[x][y] == '.':
                BOARD[x][y] = 'O'
                if len(dic[drop]):
                    x, y = dic[drop][-1]
                    drop_stone(x, y)
                break
            else:
                x, y = dic[drop][-1]
                drop_stone(x, y)

for r in BOARD:
    print(''.join(r))
