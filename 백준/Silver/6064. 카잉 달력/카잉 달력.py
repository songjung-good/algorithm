# 코드를 작성해주세요
def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def lcm(a, b):
    return a * b // gcd(a, b)


T = int(input())
for _ in range(T):
    M, N, x, y = map(int, input().split())

    x -= 1
    y -= 1

    max_year = lcm(M, N)
    year = x

    while year < max_year:
        if year % N == y:
            print(year + 1)
            break
        year += M
    else:
        print(-1)
