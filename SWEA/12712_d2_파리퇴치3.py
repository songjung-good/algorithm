#1
T = int(input())

for tc in range(1, 1+T):
    N, M = map(int, input().split())
    matrix = []
    for _ in range(N):
        row = list(map(int, input().split()))
        matrix.append(row)

    max_kill = 0

    for i in range(T):
        for j in range(T):              #원점 설정
                               #(i,j)에서 M을 빼서 0이되거나 M을 더해서 N이 되면 조정필요
            kills = 0

            if i - M + 1 < 0:
                if j - M + 1 < 0:
                    for x in range(0, i + M):
                        for y in range(0, j + M):      #범위 설정
                            kills += matrix[x][y]
                    if kills > max_kill:
                        max_kill = kills
                elif j + M - 1 > N:
                    for x in range(0, i + M):
                        for y in range(j - M + 1, N):
                            kills += matrix[x][y]
                    if kills > max_kill:
                        max_kill = kills
                else:
                    for x in range(0, i + M):
                        for y in range(j - M + 1, j + M - 1):
                            kills += matrix[x][y]
                    if kills > max_kill:
                        max_kill = kills
                    pass

            if i + M - 1 > N:
                if j - M + 1 < 0:
                    for x in range(i - M + 1, N):
                        for y in range(0, j + M - 1):
                            kills += matrix[x][y]
                    if kills > max_kill:
                        max_kill = kills
                elif j + M - 1 > N:
                    for x in range(i - M + 1, N):
                        for y in range(j - M + 1, N):
                            kills += matrix[x][y]
                    if kills > max_kill:
                        max_kill = kills
                else:
                    for x in range(i - M + 1, N):
                        for y in range(j - M + 1, j + M - 1):
                            kills += matrix[x][y]
                    if kills > max_kill:
                        max_kill = kills
                    pass
            else:
                if j - M + 1 < 0:
                    for x in range(i - M + 1, i + M - 1):
                        for y in range(0, j + M - 1):
                            kills += matrix[x][y]
                    if kills > max_kill:
                        max_kill = kills
                elif j + M - 1 > N:
                    for x in range(i - M + 1, i + M - 1):
                        for y in range(j - M + 1, N):
                            kills += matrix[x][y]
                    if kills > max_kill:
                        max_kill = kills
                else:
                    for x in range(i - M + 1, i + M - 1):
                        for y in range(j - M + 1, j + M - 1):
                            kills += matrix[x][y]
                    if kills > max_kill:
                        max_kill = kills

    print(f'{tc} {max_kill}')



'''
# +모양과 x모양의 잡는 수를 비교
# range 조정을 해야한다.
# 임시방편 i값과 k값을 비교하여 i가 크면 XXXX
# 방법 2 i, j와 배열 크기 비교
# 방법 3

N은 배열 사이즈

i,j는 원점

M은 범위

i - M + 1 > 0 and i + M - 1 < N 은 상관없음

i - M + 1 < 0 이면 0부터 시작
i + M - 1 > N 이면 N까지만 계산
'''




# # #2
# T = int(input())
#
# for tc in range(1, T+1):
#     N, M = map(int, input().split())
#     matrix = []
#     for _ in range(N):
#         row = list(map(int, input().split()))
#         matrix.append(row)
#
#     max_kill = 0
#
#     for i in range(N - M + 1):
#         for j in range(N - M + 1):
#             kills = 0
#             for x in range(i, i + M):
#                 for y in range(j, j + M):
#                     kills += matrix[x][y]
#
#             if kills > max_kill:
#                 max_kill = kills
#
#     print(f'{tc} {max_kill}')
#
