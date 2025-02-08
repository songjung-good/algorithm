N = int(input())
MAP = [list(map(int, input().split())) for _ in range(N)]

ans = [0] * N

if N == 2:
    ans[0] = 1
    ans[1] = MAP[0][1] - 1
else:
    ans[0] = (MAP[0][1] + MAP[0][2] - MAP[1][2]) // 2
    for i in range(1, N):
        ans[i] = MAP[0][i] - ans[0]

print(*ans)
