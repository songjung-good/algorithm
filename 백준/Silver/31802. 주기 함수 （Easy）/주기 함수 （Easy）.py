def chg(num, p):
    A = num % p
    B = num // p
    return A, B

p = int(input())
lst = list(map(int, input().split()))
a, b = map(int, input().split())

a_x, a_y = chg(a, p)
b_x, b_y = chg(b, p)

ans = 0

if a_y == b_y:
    for i in range(a_x, b_x):
        ans += lst[i]
else:
    for i in range(a_x, p):
        ans += lst[i]
    for i in range(b_x):
        ans += lst[i]
    ans += ((abs(b_y - a_y) - 1) * sum(lst))

print(ans)