def find_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False

    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6

    return True

P, K = map(int, input().split())
for k in range(2, K):
    if find_prime(k) and P % k == 0:
        print('BAD', k)
        exit()

print('GOOD')
