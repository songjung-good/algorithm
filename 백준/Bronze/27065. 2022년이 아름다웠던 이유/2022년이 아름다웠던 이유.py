import math

def sum_proper_divisors(n):
    total = 1
    for i in range(2, int(math.isqrt(n)) + 1):
        if n % i == 0:
            total += i
            if i != n // i:
                total += n // i
    return total

T = int(input())
for _ in range(T):
    YEAR = int(input())
    sum_div = sum_proper_divisors(YEAR)
    if sum_div > YEAR:
        # YEAR의 모든 진약수가 과잉수인지 체크
        is_smallest = True
        for i in range(1, YEAR):
            if YEAR % i == 0:
                if sum_proper_divisors(i) > i:
                    is_smallest = False
                    break
        print('Good Bye' if is_smallest else 'BOJ 2022')
    else:
        print('BOJ 2022')