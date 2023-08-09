for tc in range(1, 11):
    N, case = map(int, input().split())
    case = str(case)

    while N > 1:
        for i in range(N):
            if case[i] == case[i+1]:
                ''.join(case[i])
                N -= 2
                break
            else:
                N = 0

    print(f'#{tc} {case}')
