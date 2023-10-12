
T = int(input())

for tc in range(1, T+1):
    N = int(input())
    lst = []

    for i in range(N):
        lst += [1] * i
        if i > 2:
            for j in range(1, N):
                lst[i][j] = lst[i-1][j-1] + lst[i-1][j]

    print(f'{tc}')
    for i in range(N):
        for j in range(i):
            print(lst[i][j], end = " ")
        print()

'''
T = int(input())
for t in range(1, T+1):
    N = int(input())
    MAP = [[0] * (N + 1) for _ in range(N + 1)]
    MAP[1][1] = 1

    for i in range(2, N + 1):
        for j in range(1, i + 1):
            MAP[i][j] = MAP[i-1][j-1] + MAP[i-1][j]
    #
    #
    #
    print(f'#{t}')

    for i in range(1, N + 1):
        for j in range(1, i + 1):
            print(MAP[i][j], end = " ")
        print()


    1
    1 1
    1 2 1
    1 3 3 1
    
'''