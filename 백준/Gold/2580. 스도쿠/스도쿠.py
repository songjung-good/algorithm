import sys
input = sys.stdin.readline

def check_sq(x, y, i):
    min_r, max_r = x//3*3, x//3 * 3 + 3
    min_c, max_c = y//3*3, y//3 * 3 + 3
    lst = []
    for r in range(min_r, max_r):
        for c in range(min_c, max_c):
            lst.append(board[r][c])
            
    if i not in lst:
        return True
    else:
        return False
    
def check_col(y, i):
    if i not in [board[r][y] for r in range(9)]:
        return True
    else:
        return False
        
def check_row(x, i):
    if i not in board[x]:
        return True
    else:
        return False

def find_num(lst):
    for x, y in lst:
        if board[x][y]:
            pass
        else:
            for i in range(1, 10):
                if check_row(x, i) and check_col(y, i) and check_sq(x, y, i):
                    board[x][y] = i
                    if find_num(lst):
                        return True
                    board[x][y] = 0
            return False
    return True

board = [list(map(int, input().split())) for _ in range(9)]
blank = []
for i in range(9):
    for j in range(9):
        if board[i][j] == 0:
            blank.append((i,j))
            
find_num(blank)
for r in board:
    print(*r)