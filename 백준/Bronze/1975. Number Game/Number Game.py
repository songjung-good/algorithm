import sys
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    N = int(input())
    ans = 0

    i = 2

    while i * i <= N:
        temp = N
        while temp % i == 0:
            ans += 1
            temp //= i
        i += 1

    while i <= N:
        if N % i == 0:
            ans += 1
        i += 1

    print(ans)
