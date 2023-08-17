'''
T = int(input())
for tc in range(1, T+1):
    #N 고객 수, M 빵만드는 시간, K 만드는 붕어빵 수
    N, M, K = map(int, input().split())
    #고객이 오는 시간
    customer_lst = list(map(int, input().split()))
    customer_lst.sort()
    time = 0
    bread = 0
    ans = 'Impossible'
    # 0 ~ M 까지 손님오면 불가능
    # M ~ 2M 까지 손님 K명 이상이면 불가능
    # 조건 다 맞추고 N이 0이면 가능
    while True:
        time += M - 1
        if len(customer_lst) == 0:
            ans = 'Possible'
            break
        if time % M == 0 and time != 0:
            bread += K
        if time == customer_lst[0]:
            if bread > 0:
                bread -= 1
            else:
                break
            customer_lst.pop(0)
        time += 1
        if time % M == 0 and time != 0:
            bread += K

    print(f'#{tc} {ans}')
'''
T = int(input())
for tc in range(1, T+1):
    #N 고객 수, M 빵만드는 시간, K 만드는 붕어빵 수
    N, M, K = map(int, input().split())
    #고객이 오는 시간
    customer_lst = list(map(int, input().split()))
    customer_lst.sort()
    time = 0
    bread = 0
    # 0 ~ M 까지 손님오면 불가능
    # M ~ 2M 까지 손님 K명 이상이면 불가능
    # 조건 다 맞추고 N이 0이면 가능
    for i in range(N):
        bread = customer_lst[i] // M * K - (i + 1)
        if bread >= 0:
            ans = 'Possible'
        else:
            ans = 'Impossible'
            break

    print(f'#{tc} {ans}')