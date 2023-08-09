T = int(input())

for _ in range(T):
    tc, N = map(str, input().split())
    lst = list(map(str, input().split()))

    # print(tc, lst[int(N) - 1])
    ZRO, ONE, TWO, THR, FOR, FIV, SIX, SVN, EGT, NIN = 0, 0, 0, 0, 0, 0, 0, 0, 0, 0

    for i in range(int(N)):
        if lst[i] == 'ZRO':
            ZRO += 1
        elif lst[i] == 'ONE':
            ONE += 1
        elif lst[i] == 'TWO':
            TWO += 1
        elif lst[i] == 'THR':
            THR += 1
        elif lst[i] == 'FOR':
            FOR += 1
        elif lst[i] == 'FIV':
            FIV += 1
        elif lst[i] == 'SIX':
            SIX += 1
        elif lst[i] == 'SVN':
            SVN += 1
        elif lst[i] == 'EGT':
            EGT += 1
        elif lst[i] == 'NIN':
            NIN += 1

    print(tc)
    print('ZRO ' * ZRO, 'ONE ' * ONE, 'TWO ' * TWO, 'THR ' * THR, 'FOR ' * FOR, 'FIV ' * FIV, 'SIX ' * SIX, 'SVN ' * SVN, 'EGT ' * EGT, 'NIN ' * NIN)

'''
target = ["ZRO", "ONE", "TWO", "THR", "FOR", "FIV", "SIX", "SVN", "EGT", "NIN"]

for _ in range(int(input())):
    num, lst = map(str, input().split())
    str_list = list(map(str, input().split()))
    length = int(lst)

    result = []

    for i in range(10):
        cnt = 0
        for STR in str_list:
            if STR == target[i]:
                cnt += 1

        result += [target[i]] * cnt


    print(num)
    print(*result)

'''
