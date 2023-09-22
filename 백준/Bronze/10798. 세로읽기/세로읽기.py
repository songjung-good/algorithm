board = [input() for _ in range(5)]
ans = ""
for j in range(15):
    for i in range(5):
        try:
            ans += board[i][j:j+1]
        except:
            pass
print(ans)
