di = [0, 1]
dj = [1, 0]

def maze(row, col, sum_num):
    global ans

    for k in range(2):
        ni = row + di[k]
        nj = col + dj[k]

        if ni == N-1 and nj == N-1:
            ans = min(ans, sum_num + MAP[ni][nj])
            return

        if ni < N and nj < N:
            maze(ni, nj, sum_num + MAP[ni][nj])


T = int(input())
for tc in range(1, 1+T):
    N = int(input())
    MAP = [list(map(int, input().split())) for _ in range(N)]
    ans = float('inf')

    maze(0, 0, MAP[0][0])

    print(f'#{tc} {ans}')
