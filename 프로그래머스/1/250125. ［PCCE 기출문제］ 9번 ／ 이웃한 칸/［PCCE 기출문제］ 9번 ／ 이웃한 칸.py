def solution(board, h, w):
    answer = 0
    size = len(board)
    d = [0, 0, -1, 1]
    now = board[h][w]
    for n in range(4):
        nh, nw = h + d[n], w + d[-n - 1]
        if 0 <= nh < size and 0 <= nw < size and board[nh][nw] == now:
            answer += 1
    return answer