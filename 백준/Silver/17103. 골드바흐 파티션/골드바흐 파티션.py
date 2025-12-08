import sys
input = sys.stdin.readline

prime_check = [1] * 1_000_001
prime_check[0] = prime_check[1] = 0
for i in range(2, int(1_000_001 ** 0.5) + 1):
    if prime_check[i] == 1:
        for j in range(i*2, 1_000_001, i):
            prime_check[j] = 0

T = int(input())
for _ in range(T):
    N = int(input())
    ans = 0
    for i in range(2, N//2 + 1):
        if prime_check[i]:
            if prime_check[N-i]:
                ans += 1
    print(ans)
