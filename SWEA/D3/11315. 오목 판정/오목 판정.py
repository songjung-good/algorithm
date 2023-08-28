def check():
    global res
    for k in range(N):
        for l in range(N):
            if res == 'YES':
                return
            for dx, dy in [[-1, -1], [-1, 0], [-1, 1], [0, -1], [0, 1], [1, -1], [1, 0], [1, 1]]:
                cnt = 0
                for n in range(5):
                    nx, ny = k + (dx * n), l + (dy * n)
                    if 0 <= nx < N and 0 <= ny < N:
                        if MAP[nx][ny] == 1:
                            cnt += 1
                if cnt == 5:
                    res = 'YES'
                    return

T = int(input())
for t in range(1, T+1):
    N = int(input())
    MAP = [[0] * N for _ in range(N)]
    res = 'NO'
    for i in range(N):
        string = input()
        for j in range(N):
            if string[j] == 'o':
                MAP[i][j] = 1
    check()
    print(f'#{t} {res}')