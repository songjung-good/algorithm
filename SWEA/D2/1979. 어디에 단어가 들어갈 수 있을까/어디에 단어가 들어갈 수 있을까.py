#테스트케이스 받기
T = int(input())
#테케만큼 반복
for tc in range(1, T+1):
    # 정답 가능 칸 수 저장
    ans = 0
    #N은 퍼즐판의 크기, K는 단어의 길이
    N, K = map(int, input().split())
    #퍼즐판 받아오기
    board = [list(map(int, input().split())) for _ in range(N)]
    #행 부터 검사
    for i in range(N):
        cnt_row = 0
        cnt_col = 0
        for j in range(N):
            #1이면 cnt에 저장하여 빈칸 길이
            if board[i][j] == 1:
                cnt_row += 1
                if j == N-1:
                    if cnt_row == K:
                        ans += 1
                    cnt_row = 0

            #0이면 저장된 cnt와 문자 길이 비교
            else:
                if cnt_row == K:
                    ans += 1
                cnt_row = 0
            #열 검사
            if board[j][i] == 1:
                cnt_col += 1
                if j == N-1:
                    if cnt_col == K:
                        ans += 1
                    cnt_col = 0
            else:
                if cnt_col == K:
                    ans += 1
                cnt_col = 0

    print(f'#{tc} {ans}')



'''
#테스트케이스 받기
T = int(input())
#테케만큼 반복
for tc in range(1, T+1):
    # 정답 가능 칸 수 저장
    ans = 0
    #N은 퍼즐판의 크기, K는 단어의 길이
    N, K = map(int, input().split())
    #퍼즐판 받아오기
    board = [list(map(int, input().split())) for _ in range(N)]
    #행 부터 검사
    for i in range(N):
        cnt = 0
        for j in range(N):
            #1이면 cnt에 저장하여 빈칸 길이
            if board[i][j] == 1:
                cnt += 1
                if j == N-1 and cnt == K:
                    ans += 1

            #0이면 저장된 cnt와 문자 길이 비교
            else:
                if cnt == K:
                    ans += 1
                cnt = 0
    #열 검사
    for i in range(N):
        cnt = 0
        for j in range(N):
            if board[j][i] == 1:
                cnt += 1
                if i == N-1 and cnt == K:
                    ans += 1
            else:
                if cnt == K:
                    ans += 1
                cnt = 0

    print(f'#{tc} {ans}')
'''