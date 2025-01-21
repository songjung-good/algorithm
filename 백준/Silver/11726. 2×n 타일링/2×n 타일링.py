n = int(input())

if n <= 3:
    print(n % 10007)
else:
    a, b = 2, 3
    for _ in range(4, n + 1):
        a, b = b, a + b
    print(b % 10007)
