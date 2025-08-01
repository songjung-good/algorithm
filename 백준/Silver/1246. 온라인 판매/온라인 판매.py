# 코드를 작성해주세요
N, M = map(int, input().split())
price = [int(input()) for _ in range(M)]
price.sort(reverse=True)
max_earn = 0
max_price = 0
for i in range(M):
    now_price = price[i]
    egg = min(N, i+1)
    now_earn = egg*now_price
    if max_earn > now_earn:
        pass
    else:
        max_price = now_price
        max_earn = now_earn
    
print(max_price, max_earn)