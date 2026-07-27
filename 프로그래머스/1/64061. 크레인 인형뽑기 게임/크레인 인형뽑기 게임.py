def solution(board, moves):
    answer = 0
    SIZE = len(board)
    basket = []
    # 뽑는 위치
    for col in moves:
        c = col-1
        for row in range(SIZE):
            now = board[row][c]
            if now > 0:
                basket.append(now)
                board[row][c] = 0
                # 바구니 확인
                if len(basket) >= 2:
                    if basket[-2] != now:
                        pass
                    else:
                        basket.pop(-1)
                        basket.pop(-1)
                        answer += 2
                break
    return answer