def find_prime(n):
    if n == 2 or n == 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False

    k = 5
    while k * k <= n:
        if n % k == 0 or n % (k+2) == 0:
            return False
        k += 6
    return True

K, L = map(int, input().split())

for i in range(2, L):
    if find_prime(i):
        if not K % i:
            print('BAD', i)
            exit()

print('GOOD')