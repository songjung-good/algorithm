T = int(input())
for t in range(1, T+1):
    N = int(input())
    lst = [list(map(int, input().split())) for _ in range(N)]
    size = N ** 2
    coords = [0] * size
    for i in range(N):
        for j in range(N):
            num = lst[i][j] - 1
            coords[num] = (i, j)

    max_move = 0
    move = 1
    min_start = 0
    start_num = 0
    now_num = 0

    while now_num < size - 1 :
        if size - start_num < max_move:
            break

        x, y = coords[now_num]
        now_num += 1
        for dx, dy in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
            nx, ny = x + dx, y + dy
            if coords[now_num] == (nx, ny):
                move += 1
                break
        else:
            if max_move < move:
                max_move = move
                min_start = start_num
            move = 1
            start_num = now_num

    if now_num == size - 1:
        if max_move < move:
            max_move = move

    print(f'#{t} {min_start + 1} {max_move}')