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