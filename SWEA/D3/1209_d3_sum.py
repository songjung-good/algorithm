    #case 수 10개
    # 행렬 사이즈 100*100


for _ in range(1, 11):
    tc = int(input())
    lst = []

    for _ in range(100):
        lst.append(list(map(int, input().split()))) #100*100행렬 생성

        #1 행값 구하기
    best_row = 0            #최대값 설정
    row_sum = 0             #구간합 설정
    for i in range(100):
        for j in range(100):
            row_sum += lst[i][j]
        if best_row < row_sum:  #행의 합 끝날때 마다 구간합과 최대값비교
            best_row = row_sum
        row_sum = 0

        #2 열값 구하기
    best_col = 0            #최대값 설정
    col_sum = 0             #구간합 설정
    for i in range(100):
        for j in range(100):
            col_sum += lst[j][i]    #j행 마다 i자리의 합
        if best_col < col_sum:      #열의 합과 최대값 비교
            best_col = col_sum
        col_sum = 0

        #3 대각선 구하기
    best_crs = 0            #최대값 설정
    sum_c = 0               #구간합 설정
    sum_d = 0               #구간합 설정
    for i in range(100):
        sum_c += lst[i][i]          #좌에서 우로 대각선
        sum_d += lst[i][99-i]      #우에서 좌로 대각선
        if sum_d <= sum_c:
            best_crs = sum_c
        else:
            best_crs =sum_d

    answer = [best_row, best_col, best_crs]
    answer.sort()
    ans = answer[2]

    # A=len(lst)
    # print(A)
    print(f'#{tc} {ans}')



# 2 전부 다 비교하기
for _ in range(1, 11):
    tc = int(input())
    lst = []

    for _ in range(100):
        lst.append(list(map(int, input().split()))) #100*100행렬 생성

    sum_x_list = []
    sum_y_list = []
    sum_dia1 = 0
    sum_dia2 = 0

    for x in range(100):
        sum_dia1 += lst[x][x]
        sum_dia2 += lst[x][99-x]

        sum_x = 0
        sum_y = 0

        for y in range(100):
            sum_x = lst[x][y]
            sum_y = lst[y][x]

        sum_x_list.append(sum_x)
        sum_y_list.append(sum_y)

    max_sum = 0
    if sum_dia1 > sum_dia2:
        max_sum = sum_dia1
    else:
        max_sum = sum_dia2

    for i in range(100)


#3 최소한의 코드
for t in range(1, 11):
    input()

    lst = [list(map(int, input().split())) for _ in range(100)]

    SUM, rdia, ldia = 0, 0, 0             #각각 0이 부여됨

    for i in range(100):
        # print(sum(lst[i]))                  #행의 합
        # print(sum(list(zip(*lst))[i]))      #열의 합
        rdia += lst[i][i]                   #우로가는 대각선
        ldia += lst[i][99-i]                #좌로가는 대각선

        SUM = max(SUM, sum(lst[i]), sum(list(zip(*lst))[i]))

    print(f'#{t} {SUM}')