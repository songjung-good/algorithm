'''
    빨강은 1
    파랑은 2
    보라는 3
'''
'''
#1

T = int(input())
for tc in range(1, T+1):
    N = int(input())                            #색칠 횟수
    info = []                                   #색칠 정보 받는 곳

    lst = [[0] * 10 for _ in range(10)]         #10x10 도화지

    for _ in range(N):                          #색 정보 저장
        info = [list(map(int, input().split())) for _ in range(5)]   #

    for i in range(len(lst)):
        color = lst[i][4]
        start_row = lst[i][0]
        end_row = lst[i][2]
        start_col = lst[i][1]
        end_col = lst[i][3]

        for j in range(end_row - start_row + 1):
            for k in range(end_col - start_col + 1):
                lst[j][k] += color

    print(f'#{tc} {lst}')
'''



#2 수정본
T = int(input())
for tc in range(1, T+1):
    N = int(input())                            #색칠 횟수
    info = []                                   #색칠 정보 받는 곳
    ans = 0                                     #보라색 개수

    lst = [[0] * 10 for _ in range(10)]         #10x10 도화지

    info = [list(map(int, input().split())) for _ in range(N)]

    for i in range(len(info)):
        color = info[i][4]
        start_row = info[i][0]
        end_row = info[i][2]
        start_col = info[i][1]
        end_col = info[i][3]

        for j in range(start_row, end_row + 1):
            for k in range(start_col, end_col + 1):
                lst[j][k] += color
                if lst[j][k] == 3:
                    ans += 1

    print(f'#{tc} {ans}')

