T = int(input())
for tc in range(1, T+1):
    board = [list(map(str, input())) for _ in range(5)]
    ans = ''

    while True:
        stop = 0
        for i in range(5):
            if len(board[i]) > 0:
                word = board[i].pop(0)
                ans += word
            else:
                stop += 1
        if stop == 5:
            break

    print(f'#{tc} {ans}')