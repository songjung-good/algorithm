z, a, b, c, d, e, f, g, h, i = 0, 0, 0, 0, 0, 0, 0, 0, 0, 0
number = 1
for j in range(3):
    num = int(input())
    number *= num

for k in str(number):
    if k == '1':
        a += 1
    elif k == '2':
        b += 1
    elif k == '3':
        c += 1
    elif k == '4':
        d += 1
    elif k == '5':
        e += 1
    elif k == '6':
        f += 1
    elif k == '7':
        g += 1
    elif k == '8':
        h += 1
    elif k == '9':
        i += 1
    else:
        z += 1
print(z)
print(a)
print(b)
print(c)
print(d)
print(e)
print(f)
print(g)
print(h)
print(i)

