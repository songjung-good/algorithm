def D(num):
    if num == 1:
        return 5
    else:
        return (num * 3 + 1) + D(num - 1)

N = int(input())
ans = 0
for n in range(N):
    now = n + 1
    if now == 1:
        ans += 5
    else:
        ans += (now * 3 + 1)

print(ans%45678)
