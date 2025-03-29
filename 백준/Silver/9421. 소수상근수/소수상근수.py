import math
def prime(n):
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def check(n):
    while n != 1:
        now = str(n)
        next = 0
        for i in now:
            next += int(i) ** 2

        if next in check_lst:
            return False

        check_lst.add(next)
        n = next
    return True

N = int(input())
prime_lst = set()

for n in range(2, N):
    if prime(n):
        check_lst = set()
        check_lst.add(int(n))
        if check(n):
            print(n)