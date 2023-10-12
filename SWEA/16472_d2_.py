'''
for tc in range(1, 11):
    N, case = map(int, input().split())
    case = str(case)

    while N > 1:
        i = 0
        while i < N - 1:
            if case[i] == case[i+1]:
                if i + 2 < N:
                    case = case[:i] + case[i + 2:]
                elif i == 0:
                    case = case[i + 2:]
                else:
                    case = case[:i]
                N -= 2
                break
            else:
                i += 1
        else:
            N = 0

    print(f'#{tc} {case}')
'''


list(map(int, input().split()))

T = int(input())
for tc in range(1, T+1):
    lst = []
    top = -1
    for i in input():
        if lst[top] == i:
            top -= 1
        else:
            lst[top] = i
            top += 1

    ans = top
    print(f'#{tc} {ans}')