'''
118까지이므로 118까지의 수 중 소수를 먼저 정하고
그 소수의 합으로 만들 수 있는 수만 골라보자
'''
import math

# 소수의 배열
PRIME_N = []
for P in range(2, 119):
    S = int(math.sqrt(P))
    check = 0
    for p in range(2, S+1):
        A = P % p
        if A == 0:
            check = 1
            break

    if check == 0:
        PRIME_N.append(P)

# 소수의 합인지 확인
def check_num(n):
    check = 'No'
    if n == 2 or n == 3:
        check = 'No'
    for x in PRIME_N:
        f_num = n - x
        for y in PRIME_N:
            if y == f_num:
                check = 'Yes'

    return  check

N = int(input())
for _ in range(N):
    a = int(input())
    ans = check_num(a)
    print(ans)