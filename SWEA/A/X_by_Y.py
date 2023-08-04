# 1

# A_sqrt = int(input())
# A = int(A_sqrt**(1/2))
#
# N_matrix = []
# line_n = []
# A_matrix = list(map(int, input().split()))
#
# for i in range(0, A):
#
#     for j in range(A*i, A*(i+1)):
#         line_n.append(A_matrix[j])
#         N_matrix += line_n
#
# print(N_matrix)

# 2

# A_sqrt = int(input())
#
# A = int(A_sqrt**(1/2))
#
# N_matrix = []
#
# for i in range(A):
#     A_matrix = list(map(int, input().split()))
#     N_matrix.append(A_matrix)


#3 파리퇴치(초안)
# T = int(input())
#
# for tc in range(1, T + 1):
#     N, M = map(int, input().split())
#     matrix = []
#     row_add = []
#
#     for row in range(N):
#         row_add = list(map(int, input().split()))
#         matrix.append(row_add)                        #리스트에는 .append로 집어넣기
#
#     for i in range(N + 1 - M):
#         for j in range(N + 1 - M):
#             max_kill = 0                              #밖으로 뺴서 누적과 초기화
#             for a in range(M):
#                 for b in range(M):                     # 범위설정하는데 헤메였음
#                     kills = matrix[i + a][j + b]       # 두번 계산할 필요없음
#                     kills += kills
#
#             if kills > max_kill:
#                 max_kill = kills
#                 kills = 0                            #for문으로 초기화 시키기
#
#             else:
#                 kiils = 0
#
#     print(max_kill)



#4 파리퇴치(수정)
T = int(input())


for tc in range(1, T+1):                #case수
    N, M = map(int, input().split())   #N은 행렬의 크기, M은 파리채 크기
    matrix = []
    row_add = []
                                        #행렬만들기
    for row in range(N):               #N개씩 가로에 입력
        row_add = list(map(int, input().split()))
        matrix.append(row_add)         #행렬로 완성

    max_kill = 0
                                        #파리잡기
    for i in range(N+1-M):              #파리채 유효사거리 조정
        for j in range(N+1-M):          #i,j가 파리채 시작지점
            kills = 0
            for a in range(M):
                for b in range(M):      #(i ~ i+a), (j ~ j+b)가 범위
                    kills += matrix[i+a][j+b] #파리채 범위

            if kills > max_kill:    #비교해서 더 많이 잡은쪽 고르기
                max_kill = kills

    print(f'#{tc} {max_kill}')