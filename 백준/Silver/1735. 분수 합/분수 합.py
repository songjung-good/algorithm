def gcd(i, j):
    while j:
        i, j = j, i % j
    return i

a, b = map(int, input().split())
d, e = map(int, input().split())
c = gcd(a, b)
f = gcd(d, e)

a, b = a // c, b // c
d, e = d // f, e // f

x = b * d + a * e
y = b * e

z = gcd(x, y)
x, y = x // z, y // z
print(x, y)