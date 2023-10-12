
arr = [[0] * 100 for _ in range(100)]

N = int(input())


for _ in range(N):
    row_x, col_y = map(int, input().split())
    for i in range(10):
        for j in range(10):
            arr[89 - col_y + i][row_x + j - 1] = 1

ans = 0

for i in range(100):
    for j in range(100):
        if arr[i][j] == 1:
            ans += 1

print(ans)