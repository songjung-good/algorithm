

'''
    내장함수 사용
'''
'''
T = int(input())

for tc in range(1, T+1):
    N = int(input())
    lst = list(map(int, input().split()))
    ans_lst = []
    A = True
    while N > 0:
        if A is True:
            lst = sorted(lst)
            ans_lst.append(lst.pop())
            A = False
            N -= 1
        else:
            lst.reverse()
            ans_lst.append((lst.pop()))
            A = True
            N -= 1

    ans = ' '.join(map(str, ans_lst))

    print(f'#{tc} {ans}')
'''



T = int(input())

for tc in range(1, T+1):
    N = int(input)
    lst = list(map(int, input().split()))


    while N > 0:
        max_num = 0
        for i in range(N):
            new_num = lst[i]
            if max_num < new_num:
                max_num = new_num

    print(f'{tc} {ans}')
