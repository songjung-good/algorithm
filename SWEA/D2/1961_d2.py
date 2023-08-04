T = int(input())

for tc in range(1, T+1):
    size = int(input())
    lst = [list(map(int, input().split())) for _ in range(size)]

    ans_lst = []
    for i in range(size):
        a, b, c = [], [], []
        for j in range(size):
            a += str(lst[size-1-j][i])
            b += str(lst[size-1-i][size-1-j])
            c += str(lst[j][i])





    print(f'#{tc} {}')