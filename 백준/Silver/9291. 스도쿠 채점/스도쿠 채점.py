N = int(input())
for n in range(1, N + 1):
    if n != 1:
        input()

    MAP = [list(map(int, input().split())) for _ in range(9)]
    check = True

    # 가로 / 세로 검사
    for i in range(9):
        check1 = [False] * 10
        check2 = [False] * 10

        for j in range(9):
            if check1[MAP[i][j]]:
                check = False
                break
            if check2[MAP[j][i]]:
                check = False
                break

            check1[MAP[i][j]] = True
            check2[MAP[j][i]] = True

        if not check:
            break

    # 3x3 블록 검사
    if check:
        for si in range(0, 9, 3):      # 블록 시작 행
            for sj in range(0, 9, 3):  # 블록 시작 열
                check3 = [False] * 10

                for i in range(si, si + 3):
                    for j in range(sj, sj + 3):
                        if check3[MAP[i][j]]:
                            check = False
                            break
                        check3[MAP[i][j]] = True

                    if not check:
                        break

                if not check:
                    break
            if not check:
                break

    ans = 'CORRECT'
    if not check:
        ans = 'INCORRECT'

    print(f'Case {n}: {ans}')