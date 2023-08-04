T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    lst = list(map(int, input().split()))

    MAX = 0
    MIN = 99999

    for i in range(N-M+1):
        num = 0
        for j in range(i, i+M):
            num += lst[j]

        if num > MAX:
            MAX = num
        if num < MIN:
            MIN = num

    ans = MAX - MIN

    print(f'#{tc} {ans}')

