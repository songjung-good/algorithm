T = int(input())
for t in range(T):
    word = input()

    lcheck = 0
    rcheck = 0
    check = ''
    for i in word:
        # 입력받은 정수가 아직 없을 때(왼쪽 수식)
        if check == '':
            if i == '!':
                lcheck = lcheck + 1
            else:
                check = i
        # 입력받은 정수가 있을 때(오른쪽 수식)
        else:
            if i == '!':
                rcheck = rcheck + 1

    if rcheck:
        check = '1'
    if lcheck % 2 == 1:
        if check == '1':
            check = '0'
        else:
            check = '1'

    print(check)