import math, sys
input = sys.stdin.readline

def check(num):
    if num in [2, 3]:
        return True
    elif num % 2 == 0:
        return False
    else:
        root_n = int(math.sqrt(num)) + 1
        for i in range(3, root_n, 2):
            if num % i == 0:
                return False
        return True

while True:
    N = int(input())
    if N == 0:
        break

    ans = 0
    for n in range(N+1, 2*N+1):
        if check(n):
            ans += 1

    print(ans)