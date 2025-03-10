# 코드를 작성해주세요
import math
def is_prime(num):
    for i in prime:
        if num % i == 0:
            return False
    prime.append(num)
    return True

prime = [2]
N = int(input())
if N == 1:
    print()
    exit()
else:
    M = int(math.sqrt(N) + 1)
    for m in range(2, M+2):
        if m == 2 or is_prime(m):
            while True:
                if N % m == 0:
                    print(m)
                    N = N // m
                else:
                    break
        else:
            pass
        if N == 1:
            exit()
    print(N)