'''
    그날 가격을 보고 이후 가격들 중에 더 비싼 가격이 있다면 구입
    그날 가격이 이후 가격들 중에 제일 비싸면 앞에 구입한 것을 팔고 차익 실현
'''
'''
#1
T = int(input())        #케이스 수
for tc in range(1, 1+T):
    N = int(input())    # 거래일 수
    price = list(map(int, input().split()))

    buy_price = 0
    buy_cnt = 0
    earn = 0

    for day in range(N):                    #마지막 일 까지 반복
        for future in range(day+1, N):      #해당 날짜로 부터 미래의 가격 확인
            if price[day] < price[future]:  #오늘보다 미래의 가격이 크면
                buy_cnt += 1                #구입한다.
                buy_price += price[day]     #구입가에 추가
                break
            
                earn += price[day] * buy_cnt - buy_price    #지금까지 구입한거 다 팔아
                buy_price = buy_cnt = 0
                break

    print(f'#{tc} {earn}')
'''

#2
'''
    뒤에서 부터 본다면
    해당 날보다 싸면 구입
    비싼 날이 나오면 구입한거 다 팔고 이익실현
'''
'''
T = int(input())        #케이스 수
for tc in range(1, 1+T):
    N = int(input())    # 거래일 수
    price = list(map(int, input().split()))

    sell_price = 0
    earn = 0

    for day in range(N):                    #마지막 일 까지 반복
        for past in range(day+1, N):      #해당 날짜로 부터 과거의 가격 확인
            if price[-1 - day] < price[-1 - past]:  #오늘보다 과거의 가격이 크면
                earn += sell_price - price[-1 - day]    #오늘가격에 구입하여 미래의 비싼가격에 판다.
                break
            else:                           #오늘 보다 과거의 가격이 싸면
                sell_price = price[-1 - day]
                break

    print(f'#{tc} {earn}')
'''
#3
T = int(input())        #케이스 수
for tc in range(1, 1+T):
    N = int(input())    # 거래일 수
    price = list(map(int, input().split()))

    sell_price = 0
    earn = 0

    for day in range(N):                    #마지막 일 까지 반복
        if sell_price <= price[-1 - day]:
            sell_price = price[-1 -day]
        elif sell_price > price[-1 -day]:
            earn += sell_price - price[-1 -day]

    print(f'#{tc} {earn}')