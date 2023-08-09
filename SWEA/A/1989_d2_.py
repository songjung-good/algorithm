T = int(input())

for tc in range(1, T + 1):
    str_1 = input()

    ans = 1
    for i in range(len(str_1)):
        if str_1[i] != str_1[-i-1]:
            ans = 0

    print(f'#{tc} {ans}')




    '''
        [1]과 [-1] 비교
    '''