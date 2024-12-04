# 코드를 작성해주세요
N = int(input())
N_lst = list(map(int, input().split()))

for n in range(N):
    num = N_lst[n]
    if num >= 300:
        print(1, end=' ')
    elif num >= 275:
        print(2, end=' ')
    elif num >= 250:
        print(3, end=' ')
    else:
        print(4, end=' ')