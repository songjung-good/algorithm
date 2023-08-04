T = int(input())

di = [0, 1, 0, -1] #원점으로 부터 상하좌우 좌표값
dj = [1, 0, -1, 0]
max_flower = 0

for tc in range(1, T+1):
    N, M = map(int, input().split()) # N은 행의 수, M은 행의 원소 수
    lst = [list(map(int, input().split())) for _ in range(N)] #행의 수만큼 반복

    for i in range(N):          #행
        for j in range(M):      #열
            flower_sum = lst[i][j]
            for k in range(4):
                ni, nj = i + di[k], j + dj[k]
                if 0 <= ni < N and 0 <= nj < M:
                    flower_sum += lst[ni][nj]
            if max_flower < flower_sum:
                max_flower = flower_sum

    print(f'#{tc} {max_flower}')