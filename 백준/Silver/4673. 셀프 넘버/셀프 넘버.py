def d(i):
    n = i
    while i > 0:
        n += i % 10
        i //= 10
    return n

check = [False] * 10001
for i in range(1, 10001):
    now = d(i)
    if now <= 10000:
        check[now] = True

for i in range(1, 10001):
    if not check[i]:
        print(i)