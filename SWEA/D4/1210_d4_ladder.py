'''
#1 오류발생
for tc in range(1, 11):
    input()
    ladder = [list(map(int, input().split())) for _ in range(100)]

    di = [0, 0, -1]  # 좌, 우, 상 탐색
    dj = [-1, 1, 0]
    start_col = 0  # 시작지점 열
    start_row = 99  # 시작지점 행

    for i in range(100):  # 시작지점을 찾는다.
        if ladder[99][i] == 1 or ladder[99][i] == 0:  # 0,1 이면 넘긴다.
            pass
        if ladder[99][i] == 2:  # 2 지점의 인덱스를 추출
            start_col = i
            break

    while start_row != 0:  # [0]의 행에 도착하면 중단
        for k in range(3):  # 좌, 우, 상 방향으로 확인
            ni = start_row + di[k]  # 확인하는 행의 위치
            nj = start_col + dj[k]  # 확인하는 열의 위치
            if 0 <= nj < 100:
                if ladder[ni][nj] == 1:
                    ladder[start_row][start_col] = 0
                    start_col = nj
                    break
        start_row -= 1

    print(f'#{tc} {start_col}')
'''


#2
for tc in range(1, 11):
    input()
    ladder = [list(map(int, input().split())) for _ in range(100)]

    di = [0, 0, -1]                         #좌, 우, 상 탐색
    dj = [-1, 1, 0]
    start_col = 0                           #시작지점 열
    start_row = 99                          #시작지점 행

    for i in range(100):                      # 시작지점을 찾는다.
        if ladder[99][i] == 1 or ladder[99][i] == 0:    # 0,1 이면 넘긴다.
            pass
        elif ladder[99][i] == 2:              # 2 지점의 인덱스를 추출
            start_col = i
            break

    while start_row != 0:                 # [0]의 행에 도착하면 중단
        for k in range(3):              # 좌, 우, 상 방향으로 확인
            ni = start_row + di[k]      # 확인하는 행의 위치
            nj = start_col + dj[k]      # 확인하는 열의 위치
            if 0 <= nj < 100:
                if k == 0:
                    if ladder[ni][nj] == 1:
                        ladder[start_row][start_col] = 0  # 기존 위치 0으로
                        start_col = nj                  # 열의 위치 조정
                elif k == 1:
                    if ladder[ni][nj] == 1:
                        ladder[start_row][start_col] = 0  # 기존 위치 0으로
                        start_col = nj                  # 열의 위치 조정
                else:
                    if ladder[ni][nj] == 1:
                        ladder[start_row][start_col] = 0  # 기존 위치 0으로
                        start_row -= 1  # 열의 위치 조정

    print(f'#{tc} {start_col}')




    '''
    마지막 줄을 탐색하여 2인 지점(탈출지점)부터 출발한다.
    
    출발점 기준 (0,1), (0,-1)지점을 탐색하여 1인 방향을 지정하고
    
    해당 방향으로 0이 나올 때까지 이동, 이후 0이 나오면 위로 이동한다.
    
    좌 우가 모두 0이면 (-1,0)지점으로 이동
        
    (0, y) 지점에 도착하면 y를 출력
    '''



#3

T = 10
for t in range(1, T+1):
    input()

    MAP = [list(map(int,input().split())) for _ in range(100)]
    # 2차원 리스트 만들기 로직

    # 나는 도착점부터 올라갈거다
    # 올라가는길에 좌, 우를 우선할거다
    # 반복문 -> 내가 출발점에 도착했을때

    for n in range(100):
        if MAP[99][n] == 2:
            x = n
            break

    # 출발점
    y = 99

    while True:
        # 출발점에 도착하면 끝내겠다
        if y == 0:
            break

        #맵의 오른쪽을 벗어나지 않으면서 + 오른쪽에 값이 존재하는경우

        if x < 99 and MAP[y][x+1]:
            while x < 99 and MAP[y][x+1]:
                x += 1
            else:
                y -= 1

        #왼쪽 로직 오른쪽을 복사해서 일부만 바꾼다

        elif x > 0 and MAP[y][x - 1]:
            while x > 0 and MAP[y][x - 1]:
                x -= 1
            else:
                y -= 1

        else:
            y -= 1


    p
rint(f"#{t} {x}")
