'''

    달팽이는 1부터 N*N까지의 숫자가 시계방향으로 이루어져 있다.

    3x3은 3 2 2 1 1            5번ㄴ
    4x4는 4 3 3 2 2 1 1          7번
    5x5는 5 4 4 3 3 2 2 1 1      9번
    의 모양이다.

'''
'''
#1
T = int(input())

for tc in range(1, T+1):
    N = int(input())
    lst = []                    #빈 행렬

    for _ in range(N):          #NxN행렬에 0을 넣은 함수 만듬
        lst += [0] * N


    ans = 0

    print(f'{tc} {ans}')
'''

#2 방향배열
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

for tc in range(1, int(input()) + 1):
    N = int(input())
    lst = [[0] * N for _ in range(N)]
                              #lst = [[0] * N] * N의 형식은 같은 값을 참조하므로 금지
    i, j, num, direc = 0, 0, 1, 0         #i, j는 좌표값, num 좌표에 넣을 숫자

    lst[i][j] = num
    num += 1

    while num <= N*N:
        ni = i + dx[direc]
        nj = j + dy[direc]

        if 0 <= ni < N and 0 <= nj < N and lst[ni][nj] == 0:
            i = ni
            j = nj
            lst[ni][nj] = num
            num += 1
        else:
            direc = (direc + 1) % 4

    #반복문 통해 리스트 풀기
    #1
    print(f'#{tc}')

    for i in range(N):
        for j in range(N):
            print(lst[i][j], end=" ")
        print()
    #2
    for i in range(N):
        print(*lst[i])

    #3
    for M in lst:
        print(*M)

