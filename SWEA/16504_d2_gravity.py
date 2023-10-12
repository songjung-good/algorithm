T = int(input())            #케이스 수

for tc in range(1, T + 1):
    N = int(input())        #방의 가로길이(90도 방의 행의 수)

    lst = [[0] * 100 for i in range(N)]     #각 행이 100칸 인 2차원 리스트
    add_box = list(map(int, input().split()))   #각 행에 들어갈 상자 수

    for i in range(N):                  #행의 수 만큼 반복
        box = add_box[i]                #각 행에 상자의 수
        for j in range(box):            #상자 수만큼 반복한다.
            lst[i][j] += 1              #상자자리에 1추가

    ans = 0                             #답
    max_height = N

    #1  각 열에 1 또는 0의 갯수를 파악하여 높이 측정
    # for k in range(N):
    #     box = add_box[k]
    #     for j in range(box):
    #         for i in range(N):
    #             if lst[i][j] == 1:
    #                 max_height -= 1
    #             if ans < max_height:
    #                 ans = max_height
    #             if i == N-1:
    #                 max_height = N

    #2
    for i in range(N):
        box = add_box[i]
        for j in range(box):
            if lst[i][j] == 1:


    print(f'#{tc} {ans}')