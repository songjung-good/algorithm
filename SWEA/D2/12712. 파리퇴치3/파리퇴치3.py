T = int(input())

def line_kill():
    di = [0, 1, 0, -1]
    dj = [1, 0, -1, 0]
    max_line = 0
    sum_line = 0

    for i in range(N):
        for j in range(N):
            for k in range(4):
                for p in range(1, M):

                    ni, nj = i + di[k]*p, j + dj[k]*p
                    if 0 <= ni < N and 0 <= nj < N:
                        sum_line += fly_field[ni][nj]

            sum_line += fly_field[i][j]
            if max_line < sum_line:
                max_line = sum_line
            sum_line = 0

    return max_line

def dia_kill():
    di = [-1, -1, 1, 1]
    dj = [-1, 1, 1, -1]
    max_dia = 0
    sum_dia = 0

    for i in range(N):
        for j in range(N):
            for k in range(4):
                for p in range(1, M):
                    ni, nj = i + di[k]*p, j + dj[k]*p
                    if 0 <= ni < N and 0 <= nj < N:
                        sum_dia += fly_field[ni][nj]

            sum_dia += fly_field[i][j]
            if max_dia < sum_dia:
                max_dia = sum_dia
            sum_dia = 0

    return max_dia

for tc in range(1, T+1):
    #N은 배열의 크기, M은 스프레이 세기
    N, M = map(int, input().split())
    fly_field = [list(map(int, input().split())) for _ in range(N)]
    ans = 0
    if dia_kill() > line_kill():
        ans = dia_kill()
    else:
        ans = line_kill()
        
    print(f'#{tc} {ans}')