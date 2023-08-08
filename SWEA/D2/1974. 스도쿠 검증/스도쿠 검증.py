T = int(input())

for tc in range(1, 1+T):
    arr = [list(map(int, input().split())) for _ in range(9)]
    ans = 1

    for i in range(9):
        check = []
        for j in range(9):
            if arr[i][j] not in check:
                check.append(arr[i][j])
            elif arr[i][j] in check:
                ans = 0
                break

    if ans != 0:
        for i in range(9):
            check = []
            for j in range(9):
                if arr[j][i] not in check:
                    check.append(arr[j][i])
                else:
                    ans = 0
                    break

    if ans != 0:
        for k in range(3):
            check = []
            for i in range(3):
                for j in range(3):
                    if arr[i+(3*k)][j+(3*k)] not in check:
                        check.append(arr[i+(3*k)][j+(3*k)])
                    else:
                        ans = 0
                        break

    print(f'#{tc} {ans}')