T = int(input())
for tc in range(1, 1+T):
    N = int(input())
    farm = [list(map(int, input())) for _ in range(N)]
    center = N//2
    R = N//2

    ans_lst = []

    for row in range(center-R, center+R+1):
        for col in range(center-R, center+R+1):

            if 0 <= row < N and 0 <= col < N and abs(row - center) + abs(col - center) <= R:
                ans_lst.append(farm[row][col])
            pass


    print(f'#{tc} {sum(ans_lst)}')