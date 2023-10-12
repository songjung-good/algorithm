for tc in range(1, 2):
    input()
    ladder = [list(map(int, input().split())) for _ in range(100)]

    di = [0, 0, -1]
    dj = [-1, 1, 0]
    start = 0
    end = 99

    for i in range(100):
        if ladder[99][i] == 1 or ladder[99][i] == 0:
            pass
        if ladder[99][i] == 2:
            start = i
            break

    for i in range(100):
        for j in range(100):

            for k in range[3]:
                ni = i + di[k]
                nj = j + dj[k]
                if 0 <= ni, nj < 100:
                    if ladder[ni][nj] == 1:








    '''
    마지막 줄을 탐색하여 2인 지점부터 출발한다.
    
    출발점 기준 (0,1), (0,-1)지점을 탐색하여 1인 방향을 지정하고
    
    해당 방향으로 0이 나올 때까지 이동, 이후 0이 나오면 위로 이동한다.
    
    양쪽 지점이 0이면 (-1,0)지점으로 이동
    
    (0, y) 지점에 도착하면 y를 출력
    '''