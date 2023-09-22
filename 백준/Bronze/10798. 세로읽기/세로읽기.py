board = [input() for _ in range(5)]
ans = ""
for j in range(15):
    for i in range(5):
        if j < len(board[i]):
            ans += board[i][j]
print(ans)
