# 코드를 작성해주세요
import math
A=input()
n = ''
m = ''
for a in A:
    if a == ':':
        n = m
        m = ''
    else:
        m += a

n, m = int(n), int(m)
if n % m == 0:
    n = n // m
    m = 1
elif m % n == 0:
    m = m // n
    n = 1
while True:
    if n == 1 or m == 1:
        break
    num = int(math.sqrt(n))+1
    check = True
    for i in range(2, num):
        if n % i == 0:
            a = n // i
            if m % i == 0:
                n = n // i
                m = m // i
                check = False
                break
            elif m % a == 0:
                n = n // a
                m = m // a
                check = False
                break
    if check:
        break
        
print(f'{n}:{m}')