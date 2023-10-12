#1
'''
for tc in range(1, 11):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(8)]

    for i in range(0, 8):                       #행 탐색
        for j in range(0, 8-N+1):
            for _ in range(N//2):
                if arr[i][-j-1] == arr[i][j]:

'''

#2
'''
    글자판에서 행에서의 회문갯수와
    열에서의 회문개수를 구하여 더한다.
    
    회문 글자수를 기준을 1회 탐색 기준으로 삼는다.
    회문 글자수 N, 글자판 arr, 
    ㅂ(0과 N) (1과 N+1) ... (8-N과 8) 
'''

for tc in range(1, 11):
    N = int(input())
    arr = [list(map(str, input())) for _ in range(8)]

    ans = 0
    cnt_1 = N // 2
    cnt = 0
    for i in range(8):
        for j in range(9-N):
            for k in range(N//2):
                if arr[i][j+k] == arr[i][j + N - 1 - k]:
                    cnt += 1
            if cnt_1 == cnt:
                ans += 1
            cnt = 0

    cnt = 0
    for j in range(8):
        for i in range(9-N):
            for k in range(N // 2):
                if arr[i+k][j] == arr[i + N - 1 - k][j]:
                    cnt += 1
            if cnt_1 == cnt:
                ans += 1
            cnt = 0

    print(f'{tc} {ans}')