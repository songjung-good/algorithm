def bfs(point):
    di = [0, 1, 0, -1]
    dj = [1, 0, -1, 0]

    Queue = []
    Queue.append(point)
    goal = 0
    while Queue and goal == 0:
        row, col = Queue.pop(0)
        #지나온 길을 벽으로 바꾼다.
        maze[row][col] = 1
        for k in range(4):
            ni, nj = di[k] + row, dj[k] + col
            if 1 <= ni < 100 and 1 <= nj < 100:
                if maze[ni][nj] == 3:
                    goal = 1
                elif maze[ni][nj] == 0:
                    Queue.append((ni, nj))

    return goal

for tc in range(1, 11):
    input()  # 첫 줄은 무시
    maze = [list(map(int, input())) for _ in range(100)]  # 각 줄의 문자열을 숫자 리스트로 변환

    # 시작점 찾기
    for j in range(1,99):
        if maze[1][j] == 2:
            start_point = (1, j)

    # BFS
    ans = bfs(start_point)

    print(f'#{tc} {ans}')
