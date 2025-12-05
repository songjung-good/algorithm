def solution(board, k):
    answer = 0
    for i in range(k+1):
        if i < len(board):
            for j in range(k-i+1):
                if j < len(board[i]):
                    answer += board[i][j]
    return answer