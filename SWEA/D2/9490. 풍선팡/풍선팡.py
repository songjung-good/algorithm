'''
M개씩
N개의 줄
'''
def balloon_pang():
    di = [0, 1, 0, -1]
    dj = [1, 0, -1, 0]
    ans = 0
    flower_sum = 0

    for i in range(N):
        for j in range(M):
            power = balloon_map[i][j]
            for p in range(1, power + 1):
                for k in range(4):
                    ni, nj = di[k]*p + i, dj[k]*p+ j
                    if 0 <= ni < N and 0 <= nj < M:
                        flower_sum += balloon_map[ni][nj]

            flower_sum += power
            if ans < flower_sum:
                ans = flower_sum
            flower_sum = 0
    return ans

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    balloon_map = [list(map(int, input().split())) for _ in range(N)]
    answer = balloon_pang()

    print(f'#{tc} {answer}')