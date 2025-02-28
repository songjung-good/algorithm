import sys

# 입력 받기
N = int(sys.stdin.readline().strip())
customers = []

for _ in range(N):
    # 각 고객이 제시한 가격과 배송비를 입력 받음
    price, shipping = map(int, sys.stdin.readline().strip().split())
    customers.append((price, shipping))

# 최대 이익과 그 때의 제시 가격을 저장할 변수
max_profit = 0
optimal_price = 0

# 가능한 모든 제시 가격(고객이 제시한 가격들 중에서)에 대해 계산
possible_prices = sorted(set(price for price, _ in customers))

for offer_price in possible_prices:
    total_profit = 0
    
    # 각 고객에 대해 이익 계산
    for customer_price, shipping in customers:
        # 고객이 제시한 가격이 우리가 제시한 가격보다 크거나 같은 경우에만 구매
        if customer_price >= offer_price:
            # 판매 이익 = 제시 가격 - 배송비
            profit = offer_price - shipping
            # 이익이 0보다 큰 경우만 더함
            if profit > 0:
                total_profit += profit
    
    # 최대 이익 갱신
    if total_profit > max_profit:
        max_profit = total_profit
        optimal_price = offer_price
    # 이익이 같으면 더 작은 가격 선택
    elif total_profit == max_profit and total_profit > 0 and offer_price < optimal_price:
        optimal_price = offer_price

# 결과 출력
print(optimal_price)