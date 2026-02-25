# 코드를 작성해주세요
N = int(input())
price = int(input())
min_price = price + 0
if N >= 20:
    min_price = min(min_price, price * 0.75)
if N >= 15:
    min_price = min(min_price, max(price - 2000, 0))
if N >= 10:
    min_price = min(min_price, price * 0.9)
if N >= 5:
    min_price = min(min_price, max(price - 500, 0))

print(int(min_price))